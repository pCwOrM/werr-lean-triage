#!/usr/bin/env python3
"""
Live Lean 4.36.0 Porting Patch Verification Harness (Post-Replay Execution).

Takes System-1 candidate repairs routed by WERR-Lean-TacticRouter, applies them
to an isolated checkout of leanprover/lean4:v4.36.0 + Mathlib fc4f59e577,
verifies compilation with exit code 0 and ZERO `sorry` / `admit`, and emits
PORTING.md-compliant unified diffs (`port/patches/<ID>.patch` + `<ID>.json`).

NOTE: Run ONLY when the server has free CPU capacity (after active replay builds finish).
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

TARGET_LEAN = "leanprover/lean4:v4.36.0"
TARGET_MATHLIB = "fc4f59e577feb1a4956671bc04ac18aaaf8cd842"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def has_forbidden_axiom(text: str) -> bool:
    for bad in ("sorry", "admit", "axiom "):
        for line in text.splitlines():
            stripped = line.split("--", 1)[0]
            if bad in stripped:
                return True
    return False


def verify_candidate_patch(
    module_id: str,
    module_name: str,
    checkout: Path,
    patched_text: str,
    out_dir: Path,
    notes: str = "ported via werr-lean-triage",
) -> bool:
    rel_src = Path("src") / (module_name.replace(".", "/") + ".lean")
    src_file = checkout / rel_src
    orig_text = src_file.read_text(encoding="utf-8")
    orig_sha = sha256_file(src_file)

    if has_forbidden_axiom(patched_text):
        raise ValueError(f"Rejected patch for {module_id}: contains sorry/admit/axiom")

    try:
        src_file.write_text(patched_text, encoding="utf-8")
        res = subprocess.run(
            ["elan", "run", TARGET_LEAN, "lake", "build", f"+{module_name}:olean"],
            cwd=str(checkout),
            capture_output=True,
            text=True,
            timeout=600,
        )
        if res.returncode != 0:
            return False

        out_dir.mkdir(parents=True, exist_ok=True)
        diff = "".join(
            difflib.unified_diff(
                orig_text.splitlines(keepends=True),
                patched_text.splitlines(keepends=True),
                fromfile=f"a/{rel_src.as_posix()}",
                tofile=f"b/{rel_src.as_posix()}",
            )
        )
        (out_dir / f"{module_id}.patch").write_text(diff, encoding="utf-8")
        meta = {
            "module": module_name,
            "source_sha256": orig_sha,
            "lean": TARGET_LEAN,
            "mathlib": TARGET_MATHLIB,
            "notes": notes,
        }
        (out_dir / f"{module_id}.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        return True
    finally:
        # Always restore clean pinned source tree
        src_file.write_text(orig_text, encoding="utf-8")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Verify Lean 4.36.0 porting patches with 0 sorry.")
    p.add_argument("--check-only", action="store_true", help="Print configuration and exit.")
    args = p.parse_args()
    print(json.dumps({"target_lean": TARGET_LEAN, "target_mathlib": TARGET_MATHLIB, "ready": True}, indent=2))
