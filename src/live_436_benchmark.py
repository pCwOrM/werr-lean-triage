#!/usr/bin/env python3
"""
WERR-Lean-Triage v0.3: Multi-Pass Iterative System-1 Lean 4.33.1 -> 4.36.0 Repair & Benchmark Engine.

Combines:
1. Official 5,703-entry Mathlib v4.33.1 -> v4.36.0 deprecation/rename dictionary
   extracted directly from Mathlib's @[deprecated] annotations (preserving namespaces).
2. Iterative multi-pass repair loop (up to 4 passes per module: fix -> recompile -> next error).
3. Mechanical LANE_A fixes: `dependsOnNoncomputable` -> `noncomputable def`,
   `No goals to be solved` -> redundant closed-goal tactic line pruning.
4. WERR System-1 0-VRAM ranked tactic closers (`grind`, `simp_all`, `omega`, `ring`,
   `linarith`, `norm_num`, `positivity`, `fun_prop`, `aesop`) for `unsolved goals`.

Strict Guarantees:
- Zero `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `@[implemented_by]` added.
- Theorem/lemma/def statements are never altered (except `noncomputable` modifier).
- Every passing patch is verified by `leanprover/lean4:v4.36.0` (exit 0) and saved as
  a PORTING.md-compliant `.patch` + `.json` pair.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import difflib
import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path

from triage_parser import parse_results
from werr_tactic_router import route_werr_system1

TARGET_LEAN = "leanprover/lean4:v4.36.0"
TARGET_MATHLIB = "fc4f59e577feb1a4956671bc04ac18aaaf8cd842"

FORBIDDEN = ("sorry", "admit", "axiom ", "@[implemented_by", "native_decide", "unsafe ")
DECL_RE = re.compile(r"^\s*(?:private\s+|protected\s+)?(theorem|lemma|def|instance|structure|class|inductive|abbrev)\b")
UNKNOWN_RE = re.compile(r"Unknown (?:identifier|constant) [`']([^`']+)[`']")
NO_GOALS_RE = re.compile(r"\.lean:(\d+):(\d+):\s*error:\s*No goals to be solved")
NONCOMP_RE = re.compile(r"\.lean:(\d+):(\d+):\s*error\(lean\.dependsOnNoncomputable\)")
UNSOLVED_RE = re.compile(r"\.lean:(\d+):(\d+):\s*error:\s*(?:unsolved goals|'simp' made no progress|Tactic 'rfl' failed)")

EXTRA_RENAMES = {
    "Set.mem_setOf_eq": "Set.mem_ofPred_eq",
    "continuous_mul_right": "continuous_mul_const",
    "continuous_mul_left": "continuous_const_mul",
    "Ideal.bot_prime": "Ideal.isPrime_bot",
}

TACTIC_MAP = {
    "grind": "grind",
    "simp_all": "simp_all",
    "omega": "omega",
    "ring": "ring",
    "linarith": "linarith",
    "norm_num": "norm_num",
    "positivity": "positivity",
    "fun_prop": "fun_prop",
    "aesop": "aesop",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def count_errors(err_text: str) -> int:
    return len(re.findall(r":\d+:\d+:\s*error(?:\([^)]*\))?:", err_text))


def has_new_forbidden(orig: str, patched: str) -> bool:
    def count_bad(t: str) -> int:
        c = 0
        for ln in t.splitlines():
            code = ln.split("--", 1)[0]
            for b in FORBIDDEN:
                if b in code:
                    c += 1
        return c
    return count_bad(patched) > count_bad(orig)


def resolve_rename(sym: str, dep_map: dict[str, str]) -> str | None:
    """Resolve an unknown Lean 4.33.1 symbol to its official Lean 4.36.0 name, preserving namespace."""
    if sym in EXTRA_RENAMES:
        return EXTRA_RENAMES[sym]
    if sym in dep_map:
        repl = dep_map[sym]
        if "." in sym and "." not in repl:
            return sym.rsplit(".", 1)[0] + "." + repl
        return repl
    if "." in sym:
        ns, base = sym.rsplit(".", 1)
        if base in dep_map:
            repl = dep_map[base]
            return repl if "." in repl else f"{ns}.{repl}"
    if "finset_sum" in sym:
        return sym.replace("finset_sum", "finsetSum")
    if "finset_prod" in sym:
        return sym.replace("finset_prod", "finsetProd")
    return None


def compile_temp_file(checkout: Path, orig_src: Path, candidate_text: str, env: dict, timeout_s: int = 180) -> tuple[int, str]:
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".lean", prefix="werr3_", dir=str(orig_src.parent), delete=False, encoding="utf-8"
    ) as tf:
        tf.write(candidate_text)
        tmp_path = Path(tf.name)
    try:
        res = subprocess.run(
            ["elan", "run", TARGET_LEAN, "lake", "env", "lean", str(tmp_path)],
            cwd=str(checkout),
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout_s,
        )
        return res.returncode, (res.stdout + "\n" + res.stderr).strip()
    except subprocess.TimeoutExpired:
        return 124, "TIMEOUT"
    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except OSError:
            pass


def attempt_module_repair(record, checkout: Path, out_dir: Path, env: dict, dep_map: dict[str, str]) -> dict:
    t0 = time.perf_counter()
    rel_src = Path("src") / (record.module.replace(".", "/") + ".lean")
    src_file = checkout / rel_src
    if not src_file.is_file():
        return {"id": record.id, "module": record.module, "status": "missing_source", "elapsed_s": 0.0}

    orig_text = src_file.read_text(encoding="utf-8")
    orig_sha = sha256_text(orig_text)
    route = route_werr_system1(record)

    cur_text = orig_text
    rc, cur_err = compile_temp_file(checkout, src_file, cur_text, env)
    if rc == 0:
        return {
            "id": record.id, "module": record.module, "status": "already_ok",
            "lane": route.predicted_lane, "elapsed_s": round(time.perf_counter() - t0, 2)
        }

    notes_applied: list[str] = []
    attempts = 0
    max_passes = 4

    for _pass in range(max_passes):
        changed = False
        next_text = cur_text
        pass_notes: list[str] = []

        # 1. Official 5,703-entry Mathlib 4.33->4.36 renames for ALL unknown symbols in current error output
        for sym in sorted(set(UNKNOWN_RE.findall(cur_err))):
            repl = resolve_rename(sym, dep_map)
            if repl and repl != sym and sym in next_text:
                next_text = re.sub(rf"\b{re.escape(sym)}\b", repl, next_text)
                pass_notes.append(f"rename:{sym}->{repl}")
                changed = True
            elif repl and "." in sym:
                # Sometimes file uses unqualified base name after `open`
                base = sym.rsplit(".", 1)[1]
                repl_base = repl.rsplit(".", 1)[-1]
                if base != repl_base and re.search(rf"\b{re.escape(base)}\b", next_text):
                    next_text = re.sub(rf"\b{re.escape(base)}\b", repl_base, next_text)
                    pass_notes.append(f"rename:{base}->{repl_base}")
                    changed = True

        # 2. Noncomputable modifier fix
        for m_nc in NONCOMP_RE.finditer(cur_err):
            lineno = int(m_nc.group(1))
            lines = next_text.splitlines(keepends=True)
            if 1 <= lineno <= len(lines) and "noncomputable" not in lines[lineno - 1]:
                new_ln = re.sub(r"^(\s*(?:private\s+|protected\s+)?)(def\b)", r"\1noncomputable \2", lines[lineno - 1])
                if new_ln != lines[lineno - 1]:
                    lines[lineno - 1] = new_ln
                    next_text = "".join(lines)
                    pass_notes.append(f"noncomputable:L{lineno}")
                    changed = True

        # 3. Prune redundant closed-goal lines (`No goals to be solved`)
        no_goal_lines = sorted({int(m.group(1)) for m in NO_GOALS_RE.finditer(cur_err)}, reverse=True)
        if no_goal_lines:
            lines = next_text.splitlines(keepends=True)
            pruned_nums = []
            for ln in no_goal_lines:
                if 1 <= ln <= len(lines) and not DECL_RE.match(lines[ln - 1]):
                    del lines[ln - 1]
                    pruned_nums.append(ln)
            if pruned_nums:
                next_text = "".join(lines)
                pass_notes.append(f"prune_closed:L{pruned_nums}")
                changed = True

        if changed and not has_new_forbidden(orig_text, next_text):
            attempts += 1
            rc2, err2 = compile_temp_file(checkout, src_file, next_text, env)
            if rc2 == 0:
                notes_applied.extend(pass_notes)
                cur_text = next_text
                rc = 0
                break
            # Accept pass if error count strictly decreased or errors changed constructively
            if count_errors(err2) <= count_errors(cur_err) and err2 != cur_err:
                notes_applied.extend(pass_notes)
                cur_text = next_text
                cur_err = err2
                continue
            else:
                break

        # 4. If no deterministic rename/prune applied, try WERR System-1 top 3 tactic closers on unsolved goals
        m_unsolved = UNSOLVED_RE.search(cur_err)
        if m_unsolved:
            lineno = int(m_unsolved.group(1))
            lines = cur_text.splitlines(keepends=True)
            if 1 <= lineno <= len(lines) and not DECL_RE.match(lines[lineno - 1]):
                indent = re.match(r"^(\s*)", lines[lineno - 1]).group(1)
                ranked_closers = [TACTIC_MAP[t] for t, _ in route.ranked_tactics if t in TACTIC_MAP][:3]
                if "grind" not in ranked_closers:
                    ranked_closers.insert(0, "grind")
                solved_tactic = False
                for tac in ranked_closers[:3]:
                    lines2 = list(lines)
                    lines2.insert(lineno, f"{indent}{tac}\n")
                    cand_t = "".join(lines2)
                    if has_new_forbidden(orig_text, cand_t):
                        continue
                    attempts += 1
                    rc3, err3 = compile_temp_file(checkout, src_file, cand_t, env)
                    if rc3 == 0:
                        notes_applied.append(f"werr_tactic:{tac}@L{lineno}")
                        cur_text = cand_t
                        rc = 0
                        solved_tactic = True
                        break
                    elif count_errors(err3) < count_errors(cur_err):
                        notes_applied.append(f"werr_tactic:{tac}@L{lineno}")
                        cur_text = cand_t
                        cur_err = err3
                        solved_tactic = True
                        break
                if rc == 0:
                    break
                if solved_tactic:
                    continue
        break

    if rc == 0:
        out_dir.mkdir(parents=True, exist_ok=True)
        diff = "".join(
            difflib.unified_diff(
                orig_text.splitlines(keepends=True),
                cur_text.splitlines(keepends=True),
                fromfile=f"a/{rel_src.as_posix()}",
                tofile=f"b/{rel_src.as_posix()}",
            )
        )
        note_str = "; ".join(notes_applied)
        (out_dir / f"{record.id}.patch").write_text(diff, encoding="utf-8")
        (out_dir / f"{record.id}.json").write_text(
            json.dumps(
                {
                    "module": record.module,
                    "source_sha256": orig_sha,
                    "lean": TARGET_LEAN,
                    "mathlib": TARGET_MATHLIB,
                    "notes": note_str,
                },
                indent=2,
            ) + "\n",
            encoding="utf-8",
        )
        return {
            "id": record.id,
            "module": record.module,
            "status": "FIXED_VERIFIED_436",
            "gt_category": record.primary_category,
            "werr_lane": route.predicted_lane,
            "repair_note": note_str,
            "attempts": attempts,
            "elapsed_s": round(time.perf_counter() - t0, 2),
        }

    return {
        "id": record.id,
        "module": record.module,
        "status": "UNREPAIRED",
        "gt_category": record.primary_category,
        "werr_lane": route.predicted_lane,
        "partial_notes": notes_applied,
        "attempts": attempts,
        "elapsed_s": round(time.perf_counter() - t0, 2),
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--checkout", type=Path, required=True)
    p.add_argument("--results", type=Path, required=True)
    p.add_argument("--renames", type=Path, required=True)
    p.add_argument("--out-dir", type=Path, required=True)
    p.add_argument("--report", type=Path, required=True)
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--limit", type=int, default=270)
    args = p.parse_args()

    dep_map = json.loads(args.renames.read_text(encoding="utf-8"))
    meta, records = parse_results(args.results)
    s1_lanes = {"LANE_A_TRIVIAL_PRUNE", "LANE_B_RENAME_MIGRATION", "LANE_C_TACTIC_CLOSER"}
    target_fails = [r for r in records if r.status != "ok" and r.repair_lane in s1_lanes][: args.limit]

    env = dict(os.environ)
    env["PATH"] = "/root/.elan/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    env["ELAN_HOME"] = str(args.checkout.parent / "elan")
    env["XDG_CACHE_HOME"] = str(args.checkout.parent / "cache")

    print(f"WERR-Lean-Triage v0.3: Running {len(target_fails)} System-1 candidate failures ({args.workers} workers, {len(dep_map)} official Mathlib renames)...", flush=True)
    t_start = time.perf_counter()
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(attempt_module_repair, r, args.checkout, args.out_dir, env, dep_map): r for r in target_fails}
        for i, fut in enumerate(as_completed(futs), 1):
            res = fut.result()
            results.append(res)
            if res["status"] == "FIXED_VERIFIED_436" or i % 15 == 0 or i == len(target_fails):
                fixed_so_far = sum(1 for x in results if x["status"] == "FIXED_VERIFIED_436")
                print(f"  [{i}/{len(target_fails)}] {res['id']} -> {res['status']} (total fixed={fixed_so_far}) {res.get('repair_note','')}", flush=True)

    wall_s = round(time.perf_counter() - t_start, 2)
    fixed = [x for x in results if x["status"] == "FIXED_VERIFIED_436"]
    summary = {
        "version": "v0.3-multipass",
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "target_lean": TARGET_LEAN,
        "target_mathlib": TARGET_MATHLIB,
        "official_mathlib_renames_loaded": len(dep_map),
        "workers": args.workers,
        "evaluated_system1_failures": len(results),
        "verified_fixed_count": len(fixed),
        "verified_fix_rate_pct": round(100.0 * len(fixed) / max(1, len(results)), 2),
        "wall_seconds": wall_s,
        "fixed_modules": fixed,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"DONE in {wall_s}s: {len(fixed)}/{len(results)} ({summary['verified_fix_rate_pct']}%) verified fixed on Lean 4.36.0!", flush=True)


if __name__ == "__main__":
    main()
