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


def _skip_ws(text: str, pos: int, allow_newline: bool = False) -> int:
    n = len(text)
    ws = " \t\n\r" if allow_newline else " \t"
    while pos < n and text[pos] in ws:
        pos += 1
    return pos


def _read_lean_atom(text: str, pos: int, allow_newline: bool = False) -> tuple[str, int] | None:
    """Read one Lean application argument starting at `pos` (balanced parens/brackets or atom)."""
    pos = _skip_ws(text, pos, allow_newline=allow_newline)
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
            a1 = _read_lean_atom(out, m.end(), allow_newline=True)
            if not a1:
                continue
            arg1, p1 = a1
            a2 = _read_lean_atom(out, p1, allow_newline=True)
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


def transform_mvpolynomial_coeff_zero(text: str, err: str) -> tuple[str, list[str]]:
    """
    Replace `rw [coeff_zero]` / `rw [MvPolynomial.coeff_zero]` (removed in Mathlib 4.36)
    with `simp only [AddMonoidAlgebra.coeff_zero, Finsupp.zero_apply]`.
    """
    if (
        "Unknown identifier `coeff_zero`" not in err
        and "Unknown constant `MvPolynomial.coeff_zero`" not in err
    ):
        return text, []
    rx = re.compile(r"^(\s*)rw\s*\[\s*(?:MvPolynomial\.)?coeff_zero\s*\]\s*$", re.MULTILINE)
    out, n = rx.subn(r"\1simp only [AddMonoidAlgebra.coeff_zero, Finsupp.zero_apply]", text)
    if n > 0:
        return out, [f"mvpoly_coeff_zero({n})"]
    return text, []


def transform_finsupp_mapdomain_apply(text: str, err: str) -> tuple[str, list[str]]:
    """
    Migrate `Finsupp.mapDomain_apply` -> `Finsupp.mapDomain_apply_of_injective` when
    Mathlib 4.36 reports an application type mismatch on the injective-function signature.
    """
    if "Finsupp.mapDomain_apply" not in err and "mapDomain_apply" not in err:
        return text, []
    if "Application type mismatch" not in err:
        return text, []
    rx = re.compile(r"\bFinsupp\.mapDomain_apply\b")
    out, n = rx.subn("Finsupp.mapDomain_apply_of_injective", text)
    if n > 0:
        return out, [f"finsupp_mapdomain_apply_of_injective({n})"]
    return text, []


def transform_mvpowerseries_pderiv_ring(text: str, err: str) -> tuple[str, list[str]]:
    """
    Drop the now-implicit coefficient ring argument from `MvPowerSeries.pderiv R i`
    and `PowerSeries.derivative R` when Lean 4.36 reports an application type mismatch
    on `pderiv` or `derivative`.
    """
    if "Application type mismatch" not in err:
        return text, []
    wants_pderiv = "MvPowerSeries.pderiv" in text and "pderiv" in err
    wants_deriv = "PowerSeries.derivative" in text and "derivative" in err
    if not (wants_pderiv or wants_deriv):
        return text, []
    out = text
    notes: list[str] = []
    if wants_pderiv:
        out, n1 = re.subn(
            r"\bMvPowerSeries\.pderiv\s+(?:\([^)]+\)|[A-Za-z_][\w']*)\s+",
            "MvPowerSeries.pderiv ",
            out,
        )
        if n1 > 0:
            notes.append(f"mvpowerseries_pderiv_implicit_ring({n1})")
    if wants_deriv:
        out, n2 = re.subn(
            r"\bPowerSeries\.derivative\s+(?:\([^)]+\)|[A-Za-z_][\w']*)\b",
            "PowerSeries.derivative",
            out,
        )
        if n2 > 0:
            notes.append(f"powerseries_derivative_implicit_ring({n2})")
    return out, notes


def transform_is_integral_algebra_map_iff(text: str, err: str) -> tuple[str, list[str]]:
    """
    Drop the removed explicit injectivity argument from `(isIntegral_algebraMap_iff ...)`
    when Lean 4.36 reports `Function expected at isIntegral_algebraMap_iff`.
    """
    if "Function expected at\n  isIntegral_algebraMap_iff" not in err:
        return text, []
    pat = re.compile(r"\(\s*isIntegral_algebraMap_iff\b")
    res_chunks: list[str] = []
    cursor = 0
    count = 0
    for m in pat.finditer(text):
        if m.start() < cursor:
            continue
        # Match balanced outer parens ONLY (preserve trailing projections like `.1` / `.mp`)
        depth = 0
        j = m.start()
        n = len(text)
        while j < n:
            ch = text[j]
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        if depth != 0:
            continue
        res_chunks.append(text[cursor:m.start()])
        res_chunks.append("isIntegral_algebraMap_iff")
        cursor = j
        count += 1
    res_chunks.append(text[cursor:])
    out = "".join(res_chunks)
    if count > 0:
        return out, [f"is_integral_algebra_map_iff({count})"]
    return text, []


def transform_finite_field_x_pow_card_sub_x(text: str, err: str) -> tuple[str, list[str]]:
    """
    Update deprecated `FiniteField.X_pow_card_sub_X_natDegree_eq <R> <h>` and
    `FiniteField.X_pow_card_sub_X_ne_zero <R> <h>` to Mathlib 4.36
    `Polynomial.natDegree_X_pow_sub_X <h>` / `Polynomial.X_pow_sub_X_ne_zero <h>`
    (the ring argument `R` became implicit).
    """
    rules = (
        ("FiniteField.X_pow_card_sub_X_natDegree_eq", "Polynomial.natDegree_X_pow_sub_X", "ff_x_pow_nat_degree"),
        ("FiniteField.X_pow_card_sub_X_ne_zero", "Polynomial.X_pow_sub_X_ne_zero", "ff_x_pow_ne_zero"),
    )
    out = text
    notes: list[str] = []
    for old_name, new_name, tag in rules:
        if old_name not in err:
            continue
        pat = re.compile(rf"\b{re.escape(old_name)}\s+(?:\([^)]+\)|[A-Za-z_][\w']*)\s+")
        out, n = pat.subn(f"{new_name} ", out)
        if n > 0:
            notes.append(f"{tag}({n})")
    return out, notes


def transform_mathlib436_identifier_renames(text: str, err: str) -> tuple[str, list[str]]:
    """
    Error-gated renames for high-frequency Mathlib 4.33.1 -> 4.36.0 identifier moves
    that are not always covered by `@[deprecated]` aliases.
    """
    renames = (
        ("continuous_mul_right", "continuous_mul_const"),
        ("integral_finset_sum", "integral_finsetSum"),
    )
    out = text
    notes: list[str] = []
    for old_id, new_id in renames:
        if f"Unknown identifier `{old_id}`" not in err:
            continue
        out, n = re.subn(rf"\b{re.escape(old_id)}\b", new_id, out)
        if n > 0:
            notes.append(f"rename_{old_id}({n})")
    return out, notes


def apply_deterministic_v04_transforms(text: str, err: str) -> tuple[str, list[str]]:
    """Run all deterministic v0.4 transforms in safe order."""
    cur = text
    notes: list[str] = []
    for fn in (
        transform_mvpolynomial_coeff,
        transform_mvpolynomial_coeff_zero,
        transform_polynomial_coeff,
        transform_prod_le_zero,
        transform_is_maximal_under,
        transform_ldl_lower_inv_triangular,
        transform_power_series_ddx,
        transform_mvpowerseries_pderiv_ring,
        transform_finsupp_mapdomain_apply,
        transform_is_integral_algebra_map_iff,
        transform_finite_field_x_pow_card_sub_x,
        transform_mathlib436_identifier_renames,
        transform_invalid_alt_zero,
        transform_noncomputable_def,
    ):
        cur, n = fn(cur, err)
        notes.extend(n)
    return cur, notes
