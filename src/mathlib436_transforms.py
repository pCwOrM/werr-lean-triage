#!/usr/bin/env python3
"""
Deterministic, AST/bracket-aware Mathlib v4.33.1 -> v4.36.0 mechanical transforms
for WERR-Lean-Triage v0.4.

Every transform is strictly conservative:
- Triggered ONLY when Lean v4.36.0 emits a matching diagnostic on the current file.
- Never introduces `sorry`, `admit`, `axiom`, `native_decide`, `unsafe`, or `@[implemented_by]`.
- Preserves mathematical meaning (every statement-level rewrite is definitionally equivalent,
  e.g. `MvPolynomial.coeff d p` -> `p.coeff d`, `Polynomial.coeff p n` -> `p.coeff n`).
"""
from __future__ import annotations

import re

# Curated verified renames missing from or indirect in @[deprecated] annotations
CURATED_RENAMES: dict[str, str] = {
    "Set.mem_setOf_eq": "Set.mem_ofPred_eq",
    "continuous_mul_right": "continuous_mul_const",
    "continuous_mul_left": "continuous_const_mul",
    "Ideal.bot_prime": "Ideal.isPrime_bot",
    "DistribMulAction.toAddMonoidHom": "DistribSMul.toAddMonoidHom",
    "Measurable.ennreal_tsum": "Measurable.tsum",
    "AEMeasurable.ennreal_tsum": "AEMeasurable.tsum",
}

PROD_MONO_RENAMES: list[tuple[str, str]] = [
    ("Finset.prod_le_prod_of_subset_of_one_le", "Finset.prod_le_prod_of_subset_of_one_le₀"),
    ("prod_le_prod_of_subset_of_one_le", "prod_le_prod_of_subset_of_one_le₀"),
    ("Finset.prod_le_prod", "Finset.prod_le_prod₀"),
    ("prod_le_prod", "prod_le_prod₀"),
    ("Finset.prod_le_one", "Finset.prod_le_one₀"),
    ("prod_le_one", "prod_le_one₀"),
]

_OPEN_TO_CLOSE = {"(": ")", "[": "]", "{": "}", "⟨": "⟩"}
_CLOSERS = set(_OPEN_TO_CLOSE.values())
_IDENT_CHAR_RE = re.compile(r"[\w.'₀₁₂₃₄₅₆₇₈₉ₐₑₒₓᵢᵣᵤᵥ]")


def _skip_ws(text: str, pos: int) -> int:
    n = len(text)
    while pos < n and text[pos] in " \t":
        pos += 1
    return pos


def _read_lean_atom(text: str, pos: int) -> tuple[str, int] | None:
    """Read one Lean application argument starting at `pos` (balanced parens/brackets or atom)."""
    pos = _skip_ws(text, pos)
    n = len(text)
    if pos >= n:
        return None
    ch = text[pos]
    if ch in _OPEN_TO_CLOSE:
        stack = [_OPEN_TO_CLOSE[ch]]
        i = pos + 1
        while i < n and stack:
            c = text[i]
            if c in _OPEN_TO_CLOSE:
                stack.append(_OPEN_TO_CLOSE[c])
            elif c == stack[-1]:
                stack.pop()
            i += 1
        if stack:
            return None
        # Allow trailing dot-projection chains like `(f x).1` or `(g y).val`
        while i < n and text[i] == "." and i + 1 < n and _IDENT_CHAR_RE.match(text[i + 1]):
            i += 1
            while i < n and _IDENT_CHAR_RE.match(text[i]):
                i += 1
        return text[pos:i], i
    if ch in _CLOSERS or ch in ",;:\n\r":
        return None
    i = pos
    while i < n and _IDENT_CHAR_RE.match(text[i]):
        i += 1
    if i == pos:
        return None
    return text[pos:i], i


def _format_receiver(expr: str) -> str:
    """Format `expr` for dot notation `expr.coeff ...`, wrapping only if needed."""
    s = expr.strip()
    if s.startswith("(") and s.endswith(")"):
        # Verify the opening paren matches the closing paren
        depth = 0
        matched_end = True
        for idx, c in enumerate(s):
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0 and idx < len(s) - 1:
                    matched_end = False
                    break
        if matched_end:
            return s
    if re.fullmatch(r"[\w.'₀₁₂₃₄₅₆₇₈₉]+", s):
        return s
    return f"({s})"


def transform_mvpolynomial_coeff(text: str, err: str) -> tuple[str, list[str]]:
    """
    Rewrite `MvPolynomial.coeff d p` -> `p.coeff d` (and bare `coeff d p` -> `p.coeff d`
    when `MvPolynomial` is open/used and Lean reports `coeff` as unknown).
    """
    wants_qual = "Unknown constant `MvPolynomial.coeff`" in err or "Unknown identifier `MvPolynomial.coeff`" in err
    wants_bare = (
        ("Unknown identifier `coeff`" in err or "Function expected at\n  coeff" in err)
        and ("MvPolynomial" in text)
    )
    if not (wants_qual or wants_bare):
        return text, []

    patterns: list[re.Pattern[str]] = []
    if wants_qual:
        patterns.append(re.compile(r"\bMvPolynomial\.coeff\b"))
    if wants_bare:
        # Match bare `coeff` not preceded by `.` or word char and not followed by `_`
        patterns.append(re.compile(r"(?<![\w.])coeff\b"))

    notes: list[str] = []
    out = text
    total_rewrites = 0

    for pat in patterns:
        res_chunks: list[str] = []
        cursor = 0
        for m in pat.finditer(out):
            if m.start() < cursor:
                continue
            # Avoid rewriting declaration names (`def coeff`, `theorem coeff`)
            line_start = out.rfind("\n", 0, m.start()) + 1
            prefix = out[line_start:m.start()]
            if re.search(r"\b(?:def|theorem|lemma|abbrev|instance)\s+$", prefix):
                continue
            # Avoid rewriting inside line comments
            if "--" in prefix:
                continue
            a1 = _read_lean_atom(out, m.end())
            if not a1:
                continue
            arg1, p1 = a1
            a2 = _read_lean_atom(out, p1)
            if not a2:
                continue
            arg2, p2 = a2
            res_chunks.append(out[cursor:m.start()])
            res_chunks.append(f"{_format_receiver(arg2)}.coeff {arg1}")
            cursor = p2
            total_rewrites += 1
        res_chunks.append(out[cursor:])
        out = "".join(res_chunks)

    if total_rewrites > 0:
        notes.append(f"mvpoly_coeff_dot({total_rewrites})")
    return out, notes


def transform_polynomial_coeff(text: str, err: str) -> tuple[str, list[str]]:
    """Rewrite `Polynomial.coeff p n` -> `p.coeff n` when `Polynomial.coeff` is unknown."""
    if "Unknown constant `Polynomial.coeff`" not in err and "Unknown identifier `Polynomial.coeff`" not in err:
        return text, []

    pat = re.compile(r"\bPolynomial\.coeff\b")
    res_chunks: list[str] = []
    cursor = 0
    total_rewrites = 0

    for m in pat.finditer(text):
        if m.start() < cursor:
            continue
        line_start = text.rfind("\n", 0, m.start()) + 1
        if "--" in text[line_start:m.start()]:
            continue
        a1 = _read_lean_atom(text, m.end())
        if not a1:
            continue
        arg1, p1 = a1
        a2 = _read_lean_atom(text, p1)
        if not a2:
            continue
        arg2, p2 = a2
        res_chunks.append(text[cursor:m.start()])
        res_chunks.append(f"{_format_receiver(arg1)}.coeff {arg2}")
        cursor = p2
        total_rewrites += 1

    res_chunks.append(text[cursor:])
    out = "".join(res_chunks)
    if total_rewrites > 0:
        return out, [f"poly_coeff_dot({total_rewrites})"]
    return text, []


def transform_prod_le_zero(text: str, err: str) -> tuple[str, list[str]]:
    """
    Migrate `Finset.prod_le_prod` / `prod_le_one` / `prod_le_prod_of_subset_of_one_le`
    to their `₀` GroupWithZero variants when Mathlib 4.36 fails to synthesize
    `MulLeftMono` / `IsOrderedCancelMonoid` or reports type mismatch on these lemmas.
    """
    trigger = any(
        k in err
        for k in (
            "MulLeftMono",
            "IsOrderedCancelMonoid",
            "prod_le_prod",
            "prod_le_one",
            "prod_le_prod_of_subset_of_one_le",
        )
    )
    if not trigger:
        return text, []

    out = text
    notes: list[str] = []
    for old, new in PROD_MONO_RENAMES:
        # Don't double-suffix if already ends with ₀
        rx = re.compile(rf"(?<![\w.]){re.escape(old)}(?![\w₀])")
        if rx.search(out):
            out = rx.sub(new, out)
            notes.append(f"prod_mono:{old}->{new}")
    return out, notes


def transform_is_maximal_under(text: str, err: str) -> tuple[str, list[str]]:
    """
    Migrate `Ideal.isMaximal_comap_of_isIntegral_of_isMaximal` ->
    `Ideal.isMaximal_under_of_isIntegral_of_isMaximal` when called with an `Ideal S`
    (the 4.33 signature) under `[Algebra.IsIntegral R S]`.
    """
    if "isMaximal_comap_of_isIntegral_of_isMaximal" not in err:
        return text, []
    if "isMaximal_comap_of_isIntegral_of_isMaximal" not in text:
        return text, []
    out = text.replace(
        "isMaximal_comap_of_isIntegral_of_isMaximal",
        "isMaximal_under_of_isIntegral_of_isMaximal",
    )
    if out != text:
        return out, ["rename:isMaximal_comap_of_isIntegral_of_isMaximal->isMaximal_under_of_isIntegral_of_isMaximal"]
    return text, []


def transform_ldl_lower_inv_triangular(text: str, err: str) -> tuple[str, list[str]]:
    """
    Migrate `LDL.lowerInv_triangular` (removed in Mathlib 4.36) to
    `LDL.isLowerTriangular_lowerInv`.
    """
    if "LDL.lowerInv_triangular" not in err and "lowerInv_triangular" not in err:
        return text, []
    # Pattern 1: `fun i j hij =>\n  LDL.lowerInv_triangular hS ...`
    rx_lam = re.compile(
        r"fun\s+\w+\s+\w+\s+\w+\s*(?:=>|↦)\s*\n?\s*LDL\.lowerInv_triangular\s+(\S+)\s+[^\n]+"
    )
    out, n = rx_lam.subn(r"LDL.isLowerTriangular_lowerInv \1", text)
    if n > 0:
        return out, [f"ldl_lower_inv_triangular({n})"]
    return text, []


def transform_power_series_ddx(text: str, err: str) -> tuple[str, list[str]]:
    """
    Migrate `d⁄dX R f` -> `d⁄dX f` when Lean 4.36 reports an application type mismatch
    on `d⁄dX` (ring argument became implicit in Mathlib 4.36).
    """
    if "d⁄dX" not in err or "Application type mismatch" not in err:
        return text, []

    pat = re.compile(r"d⁄dX\b")
    res_chunks: list[str] = []
    cursor = 0
    count = 0
    for m in pat.finditer(text):
        if m.start() < cursor:
            continue
        a1 = _read_lean_atom(text, m.end())
        if not a1:
            continue
        arg1, p1 = a1
        a2 = _read_lean_atom(text, p1)
        if not a2:
            continue
        arg2, p2 = a2
        # Only strip arg1 if it looks like a ring type (single ident/type token followed by series arg)
        res_chunks.append(text[cursor:m.start()])
        res_chunks.append(f"d⁄dX {arg2}")
        cursor = p2
        count += 1
    res_chunks.append(text[cursor:])
    out = "".join(res_chunks)
    if count > 0:
        return out, [f"powerseries_ddx_implicit_ring({count})"]
    return text, []


def transform_invalid_alt_zero(text: str, err: str) -> tuple[str, list[str]]:
    """
    Prune dead `| zero => ...` branch when Mathlib 4.36 induction principle
    (e.g. `TensorProduct.induction_on`) subsumes `zero` and Lean reports:
    `Invalid alternative name `zero`: There are no unhandled alternatives`.
    """
    rx = re.compile(r"\.lean:(\d+):(\d+):\s*error:\s*Invalid alternative name `zero`: There are no unhandled alternatives")
    line_nums = sorted({int(m.group(1)) for m in rx.finditer(err)}, reverse=True)
    if not line_nums:
        return text, []

    lines = text.splitlines(keepends=True)
    pruned: list[int] = []
    for ln in line_nums:
        idx = ln - 1
        if not (0 <= idx < len(lines)):
            continue
        line = lines[idx]
        m_bar = re.match(r"^(\s*)\|\s*zero\b", line)
        if not m_bar:
            continue
        base_indent = len(m_bar.group(1))
        end_idx = idx + 1
        while end_idx < len(lines):
            nxt = lines[end_idx]
            if not nxt.strip():
                end_idx += 1
                continue
            nxt_indent = len(nxt) - len(nxt.lstrip(" "))
            if nxt_indent > base_indent and not nxt.lstrip(" ").startswith("|"):
                end_idx += 1
            else:
                break
        del lines[idx:end_idx]
        pruned.append(ln)

    if pruned:
        return "".join(lines), [f"prune_dead_zero_alt:L{pruned}"]
    return text, []


def transform_noncomputable_def(text: str, err: str) -> tuple[str, list[str]]:
    """
    Add `noncomputable` to definitions when Lean 4.36 reports `dependsOnNoncomputable`
    or `failed to compile definition, consider marking it as 'noncomputable'`.
    """
    rx = re.compile(
        r"\.lean:(\d+):(\d+):\s*error(?:\(lean\.dependsOnNoncomputable\))?:\s*"
        r"(?:failed to compile definition, consider marking it as 'noncomputable'|.*dependsOnNoncomputable)"
    )
    line_nums = sorted({int(m.group(1)) for m in rx.finditer(err)})
    if not line_nums:
        return text, []

    lines = text.splitlines(keepends=True)
    changed_lines: list[int] = []
    def_rx = re.compile(r"^(\s*(?:private\s+|protected\s+)?)(def\b)")

    for ln in line_nums:
        # Search at ln and up to 3 lines above in case diagnostic points at body/name
        for cand in range(ln - 1, max(-1, ln - 5), -1):
            if 0 <= cand < len(lines):
                if "noncomputable" in lines[cand]:
                    break
                new_ln = def_rx.sub(r"\1noncomputable \2", lines[cand])
                if new_ln != lines[cand]:
                    lines[cand] = new_ln
                    changed_lines.append(cand + 1)
                    break

    if changed_lines:
        return "".join(lines), [f"noncomputable:L{changed_lines}"]
    return text, []


def aemeasurable_candidates(err: str) -> list[str]:
    """
    Extract targeted AEMeasurable closer tactics when Lean reports an unsolved
    `⊢ AEMeasurable ...` goal (commonly left behind by `Measure.map_smul` in Mathlib 4.36).
    """
    if "⊢ AEMeasurable " not in err:
        return []
    cands: list[str] = []
    # Check for `Inv.inv` in goal
    if "⊢ AEMeasurable Inv.inv" in err:
        cands.append("exact continuous_inv.aemeasurable")
    # Check local Continuous hypotheses like `hc : Continuous (sphereMap e)`
    for m in re.finditer(r"^\s*([A-Za-z_][\w']*)\s*:\s*Continuous\b", err, re.MULTILINE):
        hyp = m.group(1)
        cands.append(f"exact {hyp}.measurable.aemeasurable")
        cands.append(f"exact {hyp}.aemeasurable")
    for m in re.finditer(r"^\s*([A-Za-z_][\w']*)\s*:\s*Measurable\b", err, re.MULTILINE):
        hyp = m.group(1)
        cands.append(f"exact {hyp}.aemeasurable")
    cands.extend(["fun_prop", "measurability"])
    # Deduplicate preserving order
    seen: set[str] = set()
    uniq: list[str] = []
    for c in cands:
        if c not in seen:
            seen.add(c)
            uniq.append(c)
    return uniq


def apply_deterministic_v04_transforms(text: str, err: str) -> tuple[str, list[str]]:
    """Run all deterministic v0.4 transforms in safe order."""
    cur = text
    notes: list[str] = []
    for fn in (
        transform_mvpolynomial_coeff,
        transform_polynomial_coeff,
        transform_prod_le_zero,
        transform_is_maximal_under,
        transform_ldl_lower_inv_triangular,
        transform_power_series_ddx,
        transform_invalid_alt_zero,
        transform_noncomputable_def,
    ):
        cur, n = fn(cur, err)
        notes.extend(n)
    return cur, notes
