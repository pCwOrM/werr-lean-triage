#!/usr/bin/env python3
"""
Turnkey CLI for WERR-Lean-Triage (0-VRAM System-1 Lean 4.33.1 -> 4.36.0 Porting Helper).

Examples:
  # 1. Triage a results.json file and print System-1 vs System-2 breakdown
  python3 src/cli.py triage --results data/triage/results.json

  # 2. Attempt verified 0-sorry System-1 mechanical repair on a single Lean module
  python3 src/cli.py repair --module Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinrankEqZeroOfDualKilledByTensor \
    --id M031586 --checkout /path/to/lean436 --out-dir ./patches
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from triage_parser import TriageRecord, parse_results, summarize
from live_436_benchmark import attempt_module_repair


def main():
    root = Path(__file__).resolve().parents[1]
    default_renames = root / "data" / "mathlib_433_to_436_renames.json"

    p = argparse.ArgumentParser(description="WERR-Lean-Triage CLI for Lean 4.33.1 -> 4.36.0 porting")
    sub = p.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("triage", help="Summarize compiler error taxonomy & repair lanes from triage JSON")
    t.add_argument("--results", type=Path, default=root / "data" / "triage" / "results.json")

    r = sub.add_parser("repair", help="Run multi-pass verified System-1 repair on one Lean module")
    r.add_argument("--module", required=True, help="Lean module name (e.g. Foo.Bar.Baz)")
    r.add_argument("--id", default="M000000", help="Module tracker ID (e.g. M031586)")
    r.add_argument("--checkout", type=Path, required=True, help="Prepared Lean 4.36.0 project checkout")
    r.add_argument("--out-dir", type=Path, required=True, help="Output directory for verified .patch & .json")
    r.add_argument("--renames", type=Path, default=default_renames)

    args = p.parse_args()
    if args.cmd == "triage":
        meta, recs = parse_results(args.results)
        print(json.dumps({"meta": meta, "summary": summarize(recs)}, indent=2, ensure_ascii=False))
        return

    dep_map = json.loads(args.renames.read_text(encoding="utf-8"))
    rec = TriageRecord(
        id=args.id, module=args.module, status="fail", seconds=0.0, errors=1,
        primary_category="unknown", all_categories=[], repair_lane="LANE_B_RENAME_MIGRATION",
        first_error_line=None, missing_symbols=[], excerpt_len=0, excerpt=""
    )
    env = dict(os.environ)
    res = attempt_module_repair(rec, args.checkout.resolve(), args.out_dir.resolve(), env, dep_map)
    print(json.dumps(res, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
