#!/usr/bin/env python3
"""
WERR-Lean-Triage v0.4: Multi-Pass Iterative System-1 Lean 4.33.1 -> 4.36.0 Repair & Benchmark Engine.

Combines:
1. Official 5,703-entry Mathlib v4.33.1 -> v4.36.0 deprecation/rename dictionary
   extracted directly from Mathlib's @[deprecated] annotations (preserving namespaces)
   plus curated verified renames (`DistribSMul.toAddMonoidHom`, `Measurable.tsum`, etc.).
2. AST/bracket-aware Mathlib v4.36.0 mechanical transforms (`mathlib436_transforms.py`):
   - `MvPolynomial.coeff d p` / bare `coeff d p` -> `p.coeff d`
   - `Polynomial.coeff p n` -> `p.coeff n`
   - `Finset.prod_le_prod` / `prod_le_one` / `prod_le_prod_of_subset_of_one_le` -> `₀` GroupWithZero variants
   - `Ideal.isMaximal_comap_of_isIntegral_of_isMaximal` -> `Ideal.isMaximal_under_of_isIntegral_of_isMaximal`
   - `LDL.lowerInv_triangular` -> `LDL.isLowerTriangular_lowerInv`
   - PowerSeries `d⁄dX R f` -> `d⁄dX f` (implicit ring argument)
   - Dead `| zero => ...` alternative pruning (`Invalid alternative name 'zero'`)
   - Expanded `noncomputable def` modifier insertion
3. Redundant closed-goal line pruning (`No goals to be solved`).
4. Targeted `Measure.map_smul` / `⊢ AEMeasurable ...` side-goal closers + WERR System-1
   0-VRAM ranked tactic closers (`grind`, `simp_all`, `omega`, `ring`, `linarith`,
   `norm_num`, `positivity`, `fun_prop`, `aesop`).
5. Iterative multi-pass repair loop (up to 5 passes per module: fix -> recompile -> next error).

Strict Guarantees:
- Zero `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, `implemented_by` added.
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

from mathlib436_transforms import (
    CURATED_RENAMES,
    aemeasurable_candidates,
    apply_deterministic_v04_transforms,
)
from triage_parser import parse_results
from werr_tactic_router import route_werr_system1

TARGET_LEAN = "leanprover/lean4:v4.36.0"
TARGET_MATHLIB = "fc4f59e577feb1a4956671bc04ac18aaaf8cd842"

FORBIDDEN_RE = re.compile(r"\b(sorry|admit|axiom|native_decide|unsafe|implemented_by)\b")
DECL_RE = re.compile(r"^\s*(?:private\s+|protected\s+)?(theorem|lemma|def|instance|structure|class|inductive|abbrev)\b")
UNKNOWN_RE = re.compile(r"Unknown (?:identifier|constant) [`']([^`']+)[`']")
NO_GOALS_RE = re.compile(r"\.lean:(\d+):(\d+):\s*error:\s*No goals to be solved")
UNSOLVED_RE = re.compile(r"\.lean:(\d+):(\d+):\s*error:\s*(?:unsolved goals|'simp' made no progress|Tactic 'rfl' failed)")

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
            c += len(FORBIDDEN_RE.findall(code))
        return c
    return count_bad(patched) > count_bad(orig)


def resolve_rename(sym: str, dep_map: dict[str, str]) -> str | None:
    """Resolve an unknown Lean 4.33.1 symbol to its official Lean 4.36.0 name, preserving namespace."""
    if sym in CURATED_RENAMES:
        return CURATED_RENAMES[sym]
    if sym in dep_map:
        repl = dep_map[sym]
        if "." in sym and "." not in repl:
            return sym.rsplit(".", 1)[0] + "." + repl
        return repl
    if "." in sym:
        ns, base = sym.rsplit(".", 1)
        if base in CURATED_RENAMES:
            repl = CURATED_RENAMES[base]
            return repl if "." in repl else f"{ns}.{repl}"
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
        mode="w", suffix=".lean", prefix="werr4_", dir=str(orig_src.parent), delete=False, encoding="utf-8"
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


def _find_map_smul_insert_pos(lines: list[str], err_lineno: int) -> tuple[int, str] | None:
    """Find the line containing `Measure.map_smul` at or after `err_lineno` within the same proof block."""
    start = max(0, err_lineno - 1)
    for idx in range(start, min(len(lines), start + 120)):
        if idx > start and DECL_RE.match(lines[idx]):
            break
        if "Measure.map_smul" in lines[idx]:
            indent = re.match(r"^(\s*)", lines[idx]).group(1)
            return idx + 1, indent
    return None


def _format_porting_note(notes_applied: list[str]) -> str:
    raw = "; ".join(notes_applied)
    stmt_equiv = any(
        n.startswith(("mvpoly_coeff_dot", "poly_coeff_dot", "powerseries_ddx", "noncomputable:"))
        for n in notes_applied
    )
    if stmt_equiv:
        return f"Statement/definition-equivalent mechanical port (v0.4): {raw}"
    return f"Proof-only mechanical port (v0.4): {raw}"


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
            "lane": record.repair_lane, "elapsed_s": round(time.perf_counter() - t0, 2)
        }

    notes_applied: list[str] = []
    attempts = 0
    max_passes = 5

    for _pass in range(max_passes):
        changed = False
        next_text = cur_text
        pass_notes: list[str] = []

        # 1. Official 5,703-entry Mathlib 4.33->4.36 + curated renames
        for sym in sorted(set(UNKNOWN_RE.findall(cur_err))):
            repl = resolve_rename(sym, dep_map)
            if repl and repl != sym and sym in next_text:
                next_text = re.sub(rf"\b{re.escape(sym)}\b", repl, next_text)
                pass_notes.append(f"rename:{sym}->{repl}")
                changed = True
            elif repl and "." in sym:
                base = sym.rsplit(".", 1)[1]
                repl_base = repl.rsplit(".", 1)[-1]
                if base != repl_base and re.search(rf"\b{re.escape(base)}\b", next_text):
                    next_text = re.sub(rf"\b{re.escape(base)}\b", repl_base, next_text)
                    pass_notes.append(f"rename:{base}->{repl_base}")
                    changed = True

        # 2. v0.4 deterministic Mathlib 4.36 transforms (coeff dot-notation, prod_le_prod₀,
        #    isMaximal_under, LDL.isLowerTriangular_lowerInv, d⁄dX, dead | zero =>, noncomputable)
        v4_text, v4_notes = apply_deterministic_v04_transforms(next_text, cur_err)
        if v4_notes and v4_text != next_text:
            next_text = v4_text
            pass_notes.extend(v4_notes)
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
            if count_errors(err2) <= count_errors(cur_err) and err2 != cur_err:
                notes_applied.extend(pass_notes)
                cur_text = next_text
                cur_err = err2
                continue
            # If combined pass didn't improve (e.g., aggressive transform conflicted), fall through to targeted closers

        # 4. Targeted AEMeasurable side-goal closer (`Measure.map_smul` in Mathlib 4.36)
        ae_tacs = aemeasurable_candidates(cur_err)
        if ae_tacs:
            m_unsolved = UNSOLVED_RE.search(cur_err)
            if m_unsolved:
                err_ln = int(m_unsolved.group(1))
                lines = cur_text.splitlines(keepends=True)
                ins = _find_map_smul_insert_pos(lines, err_ln)
                if ins is not None:
                    ins_idx, indent = ins
                    solved_ae = False
                    for tac in ae_tacs[:4]:
                        lines2 = list(lines)
                        lines2.insert(ins_idx, f"{indent}{tac}\n")
                        cand_t = "".join(lines2)
                        if has_new_forbidden(orig_text, cand_t):
                            continue
                        attempts += 1
                        rc3, err3 = compile_temp_file(checkout, src_file, cand_t, env)
                        if rc3 == 0:
                            notes_applied.append(f"aemeasurable:{tac}@L{ins_idx + 1}")
                            cur_text = cand_t
                            rc = 0
                            solved_ae = True
                            break
                        elif count_errors(err3) < count_errors(cur_err):
                            notes_applied.append(f"aemeasurable:{tac}@L{ins_idx + 1}")
                            cur_text = cand_t
                            cur_err = err3
                            solved_ae = True
                            break
                    if rc == 0:
                        break
                    if solved_ae:
                        continue

        # 5. WERR System-1 top 3 ranked tactic closers on unsolved goals
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
        note_str = _format_porting_note(notes_applied)
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
            "gt_lane": record.repair_lane,
            "gt_category": record.primary_category,
            "werr_lane": route.predicted_lane,
            "repair_note": note_str,
            "raw_ops": notes_applied,
            "attempts": attempts,
            "elapsed_s": round(time.perf_counter() - t0, 2),
        }

    return {
        "id": record.id,
        "module": record.module,
        "status": "UNREPAIRED",
        "gt_lane": record.repair_lane,
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
    p.add_argument("--all-failures", action="store_true", help="Evaluate ALL failing modules across all lanes (451 depth-0)")
    p.add_argument("--ids", type=str, default="", help="Optional comma-separated module IDs to run (smoke test)")
    p.add_argument("--limit", type=int, default=500)
    args = p.parse_args()

    dep_map = json.loads(args.renames.read_text(encoding="utf-8"))
    meta, records = parse_results(args.results)
    s1_lanes = {"LANE_A_TRIVIAL_PRUNE", "LANE_B_RENAME_MIGRATION", "LANE_C_TACTIC_CLOSER"}

    if args.ids:
        want = {x.strip() for x in args.ids.split(",") if x.strip()}
        target_fails = [r for r in records if r.id in want]
    elif args.all_failures:
        target_fails = [r for r in records if r.status != "ok"][: args.limit]
    else:
        target_fails = [r for r in records if r.status != "ok" and r.repair_lane in s1_lanes][: args.limit]

    env = dict(os.environ)
    env["PATH"] = "/root/.elan/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    env["ELAN_HOME"] = "/root/.elan" if Path("/root/.elan/bin/elan").exists() else str(args.checkout.parent / "elan")
    env["XDG_CACHE_HOME"] = str(args.checkout.parent / "cache")

    mode_label = "ALL-LANES" if args.all_failures else ("IDS" if args.ids else "SYSTEM1-LANES")
    print(f"WERR-Lean-Triage v0.4 ({mode_label}): Running {len(target_fails)} failures ({args.workers} workers, {len(dep_map)} official + {len(CURATED_RENAMES)} curated renames)...", flush=True)
    t_start = time.perf_counter()
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(attempt_module_repair, r, args.checkout, args.out_dir, env, dep_map): r for r in target_fails}
        for i, fut in enumerate(as_completed(futs), 1):
            res = fut.result()
            results.append(res)
            if res["status"] == "FIXED_VERIFIED_436" or i % 20 == 0 or i == len(target_fails):
                fixed_so_far = sum(1 for x in results if x["status"] == "FIXED_VERIFIED_436")
                print(f"  [{i}/{len(target_fails)}] {res['id']} -> {res['status']} (total fixed={fixed_so_far}) {res.get('repair_note','')}", flush=True)

    wall_s = round(time.perf_counter() - t_start, 2)
    fixed = [x for x in results if x["status"] == "FIXED_VERIFIED_436"]
    s1_eval = [x for x in results if x.get("gt_lane") in s1_lanes]
    s1_fixed = [x for x in s1_eval if x["status"] == "FIXED_VERIFIED_436"]
    lane_d_fixed = [x for x in fixed if x.get("gt_lane") not in s1_lanes]

    summary = {
        "version": "v0.4-multipass-transforms",
        "mode": mode_label,
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "target_lean": TARGET_LEAN,
        "target_mathlib": TARGET_MATHLIB,
        "official_mathlib_renames_loaded": len(dep_map),
        "curated_renames_loaded": len(CURATED_RENAMES),
        "workers": args.workers,
        "evaluated_failures": len(results),
        "verified_fixed_count": len(fixed),
        "verified_fix_rate_pct": round(100.0 * len(fixed) / max(1, len(results)), 2),
        "system1_subset_evaluated": len(s1_eval),
        "system1_subset_fixed": len(s1_fixed),
        "system1_subset_fix_rate_pct": round(100.0 * len(s1_fixed) / max(1, len(s1_eval)), 2),
        "lane_d_e_bonus_fixed": len(lane_d_fixed),
        "wall_seconds": wall_s,
        "fixed_modules": sorted(fixed, key=lambda x: x["id"]),
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"DONE in {wall_s}s: {len(fixed)}/{len(results)} ({summary['verified_fix_rate_pct']}%) verified fixed on Lean 4.36.0! "
        f"(System-1 269-subset: {len(s1_fixed)}/{len(s1_eval)} = {summary['system1_subset_fix_rate_pct']}%, LANE_D/E bonus: +{len(lane_d_fixed)})",
        flush=True,
    )


if __name__ == "__main__":
    main()
