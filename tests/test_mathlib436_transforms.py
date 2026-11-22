#!/usr/bin/env python3
"""Unit tests for WERR-Lean-Triage v0.4 deterministic Mathlib 4.36 transforms."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from mathlib436_transforms import (
    aemeasurable_candidates,
    transform_finsupp_mapdomain_apply,
    transform_invalid_alt_zero,
    transform_is_maximal_under,
    transform_ldl_lower_inv_triangular,
    transform_mvpolynomial_coeff,
    transform_mvpolynomial_coeff_zero,
    transform_noncomputable_def,
    transform_polynomial_coeff,
    transform_power_series_ddx,
    transform_prod_le_zero,
)


def test_mvpolynomial_coeff_qualified_and_nested():
    src = "theorem t (hk : MvPolynomial.coeff k' (substF h g (MvPolynomial.monomial k 1)) ≠ 0) : True := trivial\n"
    err = "foo.lean:1:10: error(lean.unknownIdentifier): Unknown constant `MvPolynomial.coeff`"
    out, notes = transform_mvpolynomial_coeff(src, err)
    assert "(substF h g (MvPolynomial.monomial k 1)).coeff k'" in out, out
    assert notes == ["mvpoly_coeff_dot(1)"]


def test_mvpolynomial_coeff_bare():
    src = "open MvPolynomial\ndef f (ω : MvPolynomial ι K) (d : ι →₀ ℕ) := w (coeff d ω)\n"
    err = "foo.lean:2:45: error(lean.unknownIdentifier): Unknown identifier `coeff`"
    out, notes = transform_mvpolynomial_coeff(src, err)
    assert "w (ω.coeff d)" in out, out
    assert notes == ["mvpoly_coeff_dot(1)"]


def test_polynomial_coeff():
    src = "theorem t (h0 : ‖Polynomial.coeff F (0 : ℕ)‖ < 1) : True := trivial\n"
    err = "foo.lean:1:18: error(lean.unknownIdentifier): Unknown constant `Polynomial.coeff`"
    out, notes = transform_polynomial_coeff(src, err)
    assert "‖F.coeff (0 : ℕ)‖" in out, out
    assert notes == ["poly_coeff_dot(1)"]


def test_prod_le_zero():
    src = "exact Finset.prod_le_prod h1 h2\nexact prod_le_one h3\nexact prod_le_prod_of_subset_of_one_le h4\n"
    err = "foo.lean:1:8: error: failed to synthesize\n  MulLeftMono ℝ"
    out, notes = transform_prod_le_zero(src, err)
    assert "Finset.prod_le_prod₀" in out
    assert "prod_le_one₀" in out
    assert "prod_le_prod_of_subset_of_one_le₀" in out
    assert len(notes) == 3


def test_is_maximal_under():
    src = "have hmax : (Q.under (𝓞 L)).IsMaximal := Ideal.isMaximal_comap_of_isIntegral_of_isMaximal Q\n"
    err = "Application type mismatch in Ideal.isMaximal_comap_of_isIntegral_of_isMaximal Q"
    out, notes = transform_is_maximal_under(src, err)
    assert "Ideal.isMaximal_under_of_isIntegral_of_isMaximal Q" in out
    assert len(notes) == 1


def test_ldl_lower_inv():
    src = (
        "  have hLi : (LDL.lowerInv hS).IsLowerTriangular := fun i j hij =>\n"
        "    LDL.lowerInv_triangular hS (OrderDual.toDual_lt_toDual.1 hij)\n"
    )
    err = "Unknown identifier `LDL.lowerInv_triangular`"
    out, notes = transform_ldl_lower_inv_triangular(src, err)
    assert ":= LDL.isLowerTriangular_lowerInv hS\n" in out, out
    assert notes == ["ldl_lower_inv_triangular(1)"]


def test_power_series_ddx():
    src = "def numSer : A⟦X⟧ := X * d⁄dX A (epSer W) - 2 * epSer W\n"
    err = "Application type mismatch: The argument A ... in the application d⁄dX A"
    out, notes = transform_power_series_ddx(src, err)
    assert "X * d⁄dX (epSer W) - 2 * epSer W" in out, out
    assert notes == ["powerseries_ddx_implicit_ring(1)"]


def test_invalid_alt_zero():
    src = (
        "    induction x with\n"
        "    | zero =>\n"
        "      exact 0\n"
        "    | tmul m c =>\n"
        "      exact 1\n"
    )
    err = "foo.lean:2:4: error: Invalid alternative name `zero`: There are no unhandled alternatives"
    out, notes = transform_invalid_alt_zero(src, err)
    assert "| zero =>" not in out
    assert "exact 0" not in out
    assert "| tmul m c =>" in out
    assert notes == ["prune_dead_zero_alt:L[2]"]


def test_noncomputable_def():
    src = "def nhd (x : ℝ) : Set ℝ := Set.univ\n"
    err = "foo.lean:1:0: error: failed to compile definition, consider marking it as 'noncomputable'"
    out, notes = transform_noncomputable_def(src, err)
    assert out.startswith("noncomputable def nhd"), out
    assert notes == ["noncomputable:L[1]"]


def test_aemeasurable_candidates():
    err = "hc : Continuous (sphereMap e)\n⊢ AEMeasurable (sphereMap e) (sphereSurface N)"
    cands = aemeasurable_candidates(err)
    assert "exact hc.measurable.aemeasurable" in cands
    assert "fun_prop" in cands


def test_mvpolynomial_coeff_zero():
    src = "  ext d\n  rw [coeff_zero]\n  by_contra hd\n"
    err = "foo.lean:2:6: error(lean.unknownIdentifier): Unknown identifier `coeff_zero`"
    out, notes = transform_mvpolynomial_coeff_zero(src, err)
    assert "  simp only [AddMonoidAlgebra.coeff_zero, Finsupp.zero_apply]\n" in out, out
    assert notes == ["mvpoly_coeff_zero(1)"]


def test_finsupp_mapdomain_apply():
    src = "    exact (Finsupp.mapDomain_apply hinj (ν k) ((), i)).symm\n"
    err = "foo.lean:86:35: error: Application type mismatch: Finsupp.mapDomain_apply hinj"
    out, notes = transform_finsupp_mapdomain_apply(src, err)
    assert "Finsupp.mapDomain_apply_of_injective hinj" in out, out
    assert notes == ["finsupp_mapdomain_apply_of_injective(1)"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"PASS {name}")
    print("ALL UNIT TESTS PASSED!")
