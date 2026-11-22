#!/usr/bin/env python3
"""
Extract official Mathlib deprecation/rename pairs directly from Mathlib source trees.

Usage:
  python3 src/extract_mathlib_renames.py \
    --mathlib-old /path/to/mathlib-v4.33.1/Mathlib \
    --mathlib-new /path/to/mathlib-v4.36.0/Mathlib \
    --out data/mathlib_433_to_436_renames.json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

RE_ALIAS = re.compile(
    r"@\[deprecated[^\]]*\]\s*(?:protected\s+|private\s+)?alias\s+([A-Za-z0-9_.'₀-₉]+)\s*:=\s*([A-Za-z0-9_.'₀-₉]+)",
    re.S,
)
RE_DECL = re.compile(
    r"@\[deprecated\s+([A-Za-z0-9_.'₀-₉]+)\s*\(since[^\]]*\]\s*(?:protected\s+|private\s+|noncomputable\s+)*(?:theorem|lemma|def|abbrev)\s+([A-Za-z0-9_.'₀-₉]+)",
    re.S,
)


def extract_renames(dirs: list[Path]) -> dict[str, str]:
    dep_map: dict[str, str] = {}
    for root in dirs:
        if not root.is_dir():
            continue
        for f in root.rglob("*.lean"):
            txt = f.read_text(encoding="utf-8", errors="ignore")
            if "@[deprecated" not in txt:
                continue
            for old_n, new_n in RE_ALIAS.findall(txt):
                dep_map[old_n] = new_n
            for new_n, old_n in RE_DECL.findall(txt):
                dep_map[old_n] = new_n
    return dep_map


def main():
    p = argparse.ArgumentParser(description="Extract Mathlib @[deprecated] rename dictionary.")
    p.add_argument("--mathlib-old", type=Path, required=True, help="Path to old Mathlib/ directory (e.g. v4.33.1)")
    p.add_argument("--mathlib-new", type=Path, required=True, help="Path to new Mathlib/ directory (e.g. v4.36.0)")
    p.add_argument("--out", type=Path, required=True, help="Output JSON dictionary path")
    args = p.parse_args()

    dep_map = extract_renames([args.mathlib_old, args.mathlib_new])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(dep_map, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Extracted {len(dep_map)} official Mathlib renames -> {args.out}")


if __name__ == "__main__":
    main()
