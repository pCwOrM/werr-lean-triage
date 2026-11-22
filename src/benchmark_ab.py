#!/usr/bin/env python3
"""
Honest A/B Benchmark: Fixed-Order vs. Rule-Based vs. WERR System-1 TacticRouter
on 2,940 real Lean 4.33.1 -> 4.36.0 depth-0 triage records (451 failures)
from rohanarun/alpoge-rh-replay/port/triage/results.json.
"""
from __future__ import annotations

import json
import time
from collections import Counter
from pathlib import Path

from triage_parser import parse_results, summarize
from werr_tactic_router import route_fixed_baseline, route_werr_system1


def main():
    root = Path(__file__).resolve().parents[1]
    results_path = root / "data" / "triage" / "results.json"
    reports_dir = root / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    meta, records = parse_results(results_path)
    summary = summarize(records)
    fails = [r for r in records if r.status != "ok"]

    # 1. Fixed-Order Baseline
    t0 = time.perf_counter()
    fixed_preds = [route_fixed_baseline(r) for r in fails]
    fixed_ms = (time.perf_counter() - t0) * 1000.0
    fixed_exact = sum(1 for r, p in zip(fails, fixed_preds) if p.predicted_lane == r.repair_lane)

    # 2. WERR System-1 Router
    t0 = time.perf_counter()
    werr_preds = [route_werr_system1(r) for r in fails]
    werr_ms = (time.perf_counter() - t0) * 1000.0
    werr_exact = sum(1 for r, p in zip(fails, werr_preds) if p.predicted_lane == r.repair_lane)

    # Breakdown of System-1 actionable vs System-2 escalation
    gt_system1_lanes = {"LANE_A_TRIVIAL_PRUNE", "LANE_B_RENAME_MIGRATION", "LANE_C_TACTIC_CLOSER"}
    gt_actionable = sum(1 for r in fails if r.repair_lane in gt_system1_lanes)
    werr_actionable = sum(1 for p in werr_preds if p.system1_actionable)

    top_tactic_dist = Counter(p.ranked_tactics[0][0] for p in werr_preds if p.ranked_tactics)
    lane_dist = Counter(p.predicted_lane for p in werr_preds)

    # Save sample routing table (first 20 failures)
    sample_routes = []
    for r, p in zip(fails[:20], werr_preds[:20]):
        sample_routes.append({
            "id": r.id,
            "module": r.module,
            "gt_category": r.primary_category,
            "gt_lane": r.repair_lane,
            "werr_lane": p.predicted_lane,
            "top_tactic": p.ranked_tactics[0][0] if p.ranked_tactics else None,
            "top_score": p.ranked_tactics[0][1] if p.ranked_tactics else 0.0,
            "system1_actionable": p.system1_actionable,
            "missing_symbols": r.missing_symbols[:3],
        })

    report = {
        "source_dataset": "rohanarun/alpoge-rh-replay/port/triage/results.json",
        "target_lean": meta.get("lean"),
        "target_mathlib": meta.get("mathlib"),
        "dataset_summary": summary,
        "ab_benchmark": {
            "evaluated_failures": len(fails),
            "fixed_baseline": {
                "lane_agreement_count": fixed_exact,
                "lane_agreement_pct": round(100.0 * fixed_exact / max(1, len(fails)), 2),
                "total_ms": round(fixed_ms, 3),
                "us_per_module": round(1000.0 * fixed_ms / max(1, len(fails)), 2),
                "system1_offload_candidates": 0,
            },
            "werr_system1_router": {
                "lane_agreement_count": werr_exact,
                "lane_agreement_pct": round(100.0 * werr_exact / max(1, len(fails)), 2),
                "total_ms": round(werr_ms, 3),
                "us_per_module": round(1000.0 * werr_ms / max(1, len(fails)), 2),
                "vram_bytes": 0,
                "predicted_system1_actionable": werr_actionable,
                "ground_truth_system1_lanes": gt_actionable,
                "predicted_lane_distribution": dict(lane_dist.most_common()),
                "top_tactic_distribution": dict(top_tactic_dist.most_common()),
            },
        },
        "honest_scope_note": (
            "This offline A/B benchmark measures diagnostic triage speed and repair-lane routing "
            "accuracy on real Lean 4.36.0 compiler excerpts. True end-to-end patch success rate "
            "(compiled pass rate with 0 sorry) MUST be measured live against leanprover/lean4:v4.36.0 "
            "using src/port_patch_runner.py once the active replay build finishes."
        ),
        "sample_routes": sample_routes,
    }

    (reports_dir / "triage_benchmark_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    md_lines = [
        "# WERR-Lean-TacticRouter: Offline Triage Benchmark Report",
        "",
        f"- **Dataset:** `{report['source_dataset']}`",
        f"- **Target Toolchain:** `{meta.get('lean')}` / Mathlib `{str(meta.get('mathlib'))[:12]}`",
        f"- **Total Depth-0 Modules Triaged:** `{summary['total_triaged']}` (`{summary['ok_unchanged']}` unchanged OK = `{summary['ok_rate_pct']}%`, `{summary['fail_count']}` failing)",
        "",
        "## 1. Empirical Error Taxonomy (451 Real Failures)",
        "",
        "| Compiler Error Category | Count | Share (%) |",
        "| :--- | ---: | ---: |",
    ]
    for cat, cnt in summary["by_category"].items():
        md_lines.append(f"| `{cat}` | {cnt} | {100.0 * cnt / len(fails):.1f}% |")

    md_lines += [
        "",
        "## 2. Repair-Lane Distribution (Ground Truth)",
        "",
        "| Repair Lane | Count | Share (%) | System-1 Candidate? |",
        "| :--- | ---: | ---: | :---: |",
    ]
    for lane, cnt in summary["by_lane"].items():
        is_s1 = "Yes (0-VRAM)" if lane in gt_system1_lanes else "No (Escalate to System-2)"
        md_lines.append(f"| `{lane}` | {cnt} | {100.0 * cnt / len(fails):.1f}% | {is_s1} |")

    fb = report["ab_benchmark"]["fixed_baseline"]
    wb = report["ab_benchmark"]["werr_system1_router"]
    md_lines += [
        "",
        "## 3. Offline A/B Routing Comparison (451 Failures)",
        "",
        "| Policy | VRAM | Latency (µs / module) | Lane Agreement (%) | System-1 Offload Candidates |",
        "| :--- | :---: | ---: | ---: | ---: |",
        f"| Fixed-Order Baseline | 0 B | {fb['us_per_module']} µs | {fb['lane_agreement_pct']}% ({fb['lane_agreement_count']}/{len(fails)}) | 0 |",
        f"| **WERR System-1 Router** | **0 B** | **{wb['us_per_module']} µs** | **{wb['lane_agreement_pct']}% ({wb['lane_agreement_count']}/{len(fails)})** | **{wb['predicted_system1_actionable']}** |",
        "",
        "## 4. Top Missing / Renamed Mathlib Symbols (4.33.1 → 4.36.0)",
        "",
        "| Symbol | Occurrences |",
        "| :--- | ---: |",
    ]
    for sym, cnt in summary["top_missing_symbols"][:15]:
        md_lines.append(f"| `{sym}` | {cnt} |")

    md_lines += [
        "",
        "## 5. Honest Scope & Next Live Verification Step",
        "",
        f"> {report['honest_scope_note']}",
        "",
    ]

    (reports_dir / "triage_benchmark_report.md").write_text("\n".join(md_lines), encoding="utf-8")
    print(json.dumps(report["ab_benchmark"], indent=2))
    print(f"Saved reports to {reports_dir}")


if __name__ == "__main__":
    main()
