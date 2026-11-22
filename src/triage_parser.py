#!/usr/bin/env python3
"""Diagnostic parser for Lean 4.33.1 -> 4.36.0 porting triage records."""
from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional

ERROR_PATTERNS = [
    ("no_goals_to_be_solved", r"No goals to be solved"),
    ("invalid_alternative_name", r"Invalid alternative name"),
    ("unknown_identifier", r"Unknown identifier [`']([^`']+)[`']"),
    ("unknown_constant", r"Unknown constant [`']([^`']+)[`']"),
    ("invalid_field_or_struct", r"(?:Invalid field|is not a field of structure)"),
    ("unsolved_goals", r"unsolved goals"),
    ("simp_failed", r"(?:'simp' made no progress|Tactic 'simp' failed|tactic 'simp' failed)"),
    ("rewrite_failed", r"Tactic 'rewrite' failed|tactic 'rewrite' failed"),
    ("rfl_failed", r"Tactic 'rfl' failed|tactic 'rfl' failed"),
    ("app_type_mismatch", r"Application type mismatch"),
    ("type_mismatch", r"Type mismatch|type mismatch"),
    ("function_expected", r"Function expected at"),
    ("typeclass_synthesis", r"failed to synthesize"),
    ("default_value_synthesis", r"could not synthesize default value"),
    ("invalid_projection", r"Invalid projection"),
    ("heartbeat_timeout", r"maximum number of heartbeats|deterministic\) timeout"),
    ("already_declared", r"has already been declared"),
]

# Ground-truth repair lane mapping based on Lean 4.33 -> 4.36 porting mechanics
CATEGORY_TO_LANE = {
    "no_goals_to_be_solved": "LANE_A_TRIVIAL_PRUNE",
    "invalid_alternative_name": "LANE_A_TRIVIAL_PRUNE",
    "unknown_identifier": "LANE_B_RENAME_MIGRATION",
    "unknown_constant": "LANE_B_RENAME_MIGRATION",
    "invalid_field_or_struct": "LANE_B_RENAME_MIGRATION",
    "unsolved_goals": "LANE_C_TACTIC_CLOSER",
    "simp_failed": "LANE_C_TACTIC_CLOSER",
    "rewrite_failed": "LANE_C_TACTIC_CLOSER",
    "rfl_failed": "LANE_C_TACTIC_CLOSER",
    "app_type_mismatch": "LANE_D_SIGNATURE_OR_LLM",
    "type_mismatch": "LANE_D_SIGNATURE_OR_LLM",
    "function_expected": "LANE_D_SIGNATURE_OR_LLM",
    "typeclass_synthesis": "LANE_D_SIGNATURE_OR_LLM",
    "default_value_synthesis": "LANE_D_SIGNATURE_OR_LLM",
    "invalid_projection": "LANE_D_SIGNATURE_OR_LLM",
    "heartbeat_timeout": "LANE_E_HEARTBEAT_ESCALATE",
    "already_declared": "LANE_B_RENAME_MIGRATION",
    "other": "LANE_D_SIGNATURE_OR_LLM",
}

LINE_RE = re.compile(r"\.lean:(\d+):(\d+):\s*error:\s*(.+)")
MISSING_SYM_RE = re.compile(r"Unknown (?:identifier|constant) [`']([^`']+)[`']")
FIELD_RE = re.compile(r"[`']([^`']+)[`'] is not a field of structure [`']([^`']+)[`']")


@dataclass
class TriageRecord:
    id: str
    module: str
    status: str
    seconds: float
    errors: int
    primary_category: str
    all_categories: List[str]
    repair_lane: str
    first_error_line: Optional[int]
    missing_symbols: List[str]
    excerpt_len: int
    excerpt: str


def classify_excerpt(excerpt: str) -> tuple[str, List[str]]:
    if not excerpt:
        return "other", []
    found = []
    for name, pat in ERROR_PATTERNS:
        if re.search(pat, excerpt):
            found.append(name)
    if not found:
        return "other", ["other"]
    return found[0], found


def parse_results(results_path: Path) -> tuple[dict, List[TriageRecord]]:
    raw = json.loads(results_path.read_text(encoding="utf-8"))
    meta = {"lean": raw.get("lean"), "mathlib": raw.get("mathlib")}
    records: List[TriageRecord] = []
    for row in raw["results"]:
        ex = row.get("excerpt", "") or ""
        if row["status"] == "ok":
            records.append(
                TriageRecord(
                    id=row["id"],
                    module=row["module"],
                    status="ok",
                    seconds=float(row.get("seconds", 0.0)),
                    errors=0,
                    primary_category="ok",
                    all_categories=[],
                    repair_lane="UNCHANGED_OK",
                    first_error_line=None,
                    missing_symbols=[],
                    excerpt_len=0,
                    excerpt="",
                )
            )
            continue

        primary, all_cats = classify_excerpt(ex)
        lane = CATEGORY_TO_LANE.get(primary, "LANE_D_SIGNATURE_OR_LLM")
        m_line = LINE_RE.search(ex)
        first_line = int(m_line.group(1)) if m_line else None
        syms = sorted(set(MISSING_SYM_RE.findall(ex)))
        for fld, st in FIELD_RE.findall(ex):
            syms.append(f"{st}.{fld}")

        records.append(
            TriageRecord(
                id=row["id"],
                module=row["module"],
                status=row["status"],
                seconds=float(row.get("seconds", 0.0)),
                errors=int(row.get("errors", 0)),
                primary_category=primary,
                all_categories=all_cats,
                repair_lane=lane,
                first_error_line=first_line,
                missing_symbols=syms,
                excerpt_len=len(ex),
                excerpt=ex,
            )
        )
    return meta, records


def summarize(records: List[TriageRecord]) -> Dict:
    fails = [r for r in records if r.status != "ok"]
    cat_counts = Counter(r.primary_category for r in fails)
    lane_counts = Counter(r.repair_lane for r in fails)
    sym_counts = Counter(s for r in fails for s in r.missing_symbols)
    return {
        "total_triaged": len(records),
        "ok_unchanged": len(records) - len(fails),
        "fail_count": len(fails),
        "ok_rate_pct": round(100.0 * (len(records) - len(fails)) / max(1, len(records)), 2),
        "by_category": dict(cat_counts.most_common()),
        "by_lane": dict(lane_counts.most_common()),
        "top_missing_symbols": sym_counts.most_common(25),
    }


if __name__ == "__main__":
    p = Path(__file__).resolve().parents[1] / "data" / "triage" / "results.json"
    meta, recs = parse_results(p)
    print(json.dumps({"meta": meta, "summary": summarize(recs)}, indent=2))
