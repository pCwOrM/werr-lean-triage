# WERR-Lean-Triage: 0-VRAM System-1 Porting & Migration Helper for Lean 4

[![Release v0.4.4](https://img.shields.io/badge/Release-v0.4.4_(17%2F17_Tests)-informational.svg)](https://github.com/pCwOrM/werr-lean-triage/releases/tag/v0.4.4)
[![Lean 4.36.0 Verified](https://img.shields.io/badge/Lean_4.36.0_Live_Verified-151%2F451_(89.80%25_Zero--LLM)-brightgreen.svg)](reports/live_436_v04_report.md)
[![Mathlib Renames](https://img.shields.io/badge/Mathlib_4.33%E2%86%924.36-5%2C710_Rules_%2B_14_AST_Transforms-blue.svg)](src/mathlib436_transforms.py)
[![VRAM](https://img.shields.io/badge/VRAM-0_Bytes_(CPU--Only)-purple.svg)](#2-live-lean-v4360-verification-results-v02--v03--v04--v044)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-orange.svg)](LICENSE)

An open-source, zero-VRAM **System-1 diagnostic triage and multi-pass mechanical migration helper** built to accelerate the **Lean `v4.33.1` → `v4.36.0` / Mathlib `v4.36.0`** porting campaign for Levent Alpöge's formalized Riemann Hypothesis archive ([`rohanarun/alpoge-rh-replay`](https://github.com/rohanarun/alpoge-rh-replay)).

> [!IMPORTANT]
> **Scientific Scope & Honesty Statement**  
> `werr-lean-triage` is strictly a **System-1 triage router and mechanical migration helper**. It is **not** a proof kernel or theorem prover, and makes zero claims of proof validity on its own. Every candidate patch it generates is compiled and verified (`exit 0`, zero `sorry`, zero `admit`, zero new `axiom`, zero `native_decide`/`unsafe`/`implemented_by`) by the official pinned `leanprover/lean4:v4.36.0` compiler before being emitted.

<p align="center">
  <img src="assets/demo.gif" alt="WERR-Lean-Triage Live Demo" width="820" />
</p>

## ⚡ 30-Second Quick Start

```bash
git clone https://github.com/pCwOrM/werr-lean-triage.git && cd werr-lean-triage
python -c "
from src.mathlib436_transforms import transform_mvpolynomial_coeff
out, notes = transform_mvpolynomial_coeff('theorem t : MvPolynomial.coeff k p != 0 := by sorry', 'Unknown constant \`MvPolynomial.coeff\`')
print(out, notes)
"
```

**Observed Output:**
```text
theorem t : p.coeff k != 0 := by sorry ['mvpoly_coeff_dot(1)']
```

---

## 1. Empirical Error Taxonomy (2,940 Real Depth-0 Modules)

Parsed from [`rohanarun/alpoge-rh-replay/port/triage/results.json`](data/triage/results.json) (`leanprover/lean4:v4.36.0`, Mathlib `fc4f59e577fe`):

- **Total triaged depth-0 modules:** `2,940`
- **Compile unchanged (`ok`):** `2,489` (`84.66%`) — **0 LLM tokens needed**
- **Fail unchanged (`fail`):** `451` (`15.34%`)

| Repair Lane | Count | Share of Failures | Handled By |
| :--- | ---: | ---: | :--- |
| `LANE_B_RENAME_MIGRATION` (`unknown_identifier`, `unknown_constant`, `invalid_field_or_struct`) | 182 | **40.4%** | System-1 (5,710 Mathlib rules + AST dot-notation transforms) |
| `LANE_A_TRIVIAL_PRUNE` (`no_goals_to_be_solved`, `invalid_alternative_name`) | 50 | **11.1%** | System-1 (closed-goal & dead `\| zero =>` branch pruning) |
| `LANE_C_TACTIC_CLOSER` (`unsolved_goals`, `simp`/`rw`/`rfl` failures) | 37 | **8.2%** | System-1 (`Measure.map_smul` `AEMeasurable` + ranked tactic closers) |
| `LANE_D_SIGNATURE_OR_LLM` (`app_type_mismatch`, `type_mismatch`, `typeclass_synthesis`) | 179 | **39.7%** | System-1 `v0.4` (`prod_le_prod₀`, `isMaximal_under`, `d⁄dX`, `noncomputable`) + System-2 escalation |
| `LANE_E_HEARTBEAT_ESCALATE` (`heartbeat_timeout`) | 3 | **0.7%** | Escalate to System-2 (human / LLM refactor) |

---

## 2. Live Lean `v4.36.0` Verification Results (`v0.2` → `v0.3` → `v0.4` → `v0.4.4`)

We extracted **5,703 official `@[deprecated]` rename/alias entries** directly from the Mathlib `v4.33.1` and `v4.36.0` source trees (`src/extract_mathlib_renames.py`), added **7 curated verified renames**, and built **14 deterministic bracket/AST-aware Mathlib `v4.36.0` mechanical transforms** (`src/mathlib436_transforms.py`, verified by **17/17 unit tests**): 9 in the `v0.4.0` depth-0 benchmark baseline plus 5 additional field-discovered transforms folded in during `v0.4.1`–`v0.4.4` porting packets. Every single fix below was compiled live by `leanprover/lean4:v4.36.0` with `0 sorry`:

| Version | Strategy | Scope Evaluated | Live Verified `0 sorry` Fixes | Fix Rate (Scope) | System-1 Subset Rate | Combined Zero-LLM Depth-0 Coverage | Wall Time | VRAM / API Cost |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `v0.2` | Single-pass, 9 hand-guessed renames | 120 (S1 sample) | 2 | 1.67% | 1.67% | 84.73% | 430.4s | 0 B / \$0 |
| `v0.3` | 4-pass iterative + 5,703 official Mathlib renames | 269 (S1 lanes) | 77 | 28.62% | 28.62% | 87.28% (`2,566 / 2,940`) | 953.7s (8w) | 0 B / \$0 |
| **`v0.4`** | **5-pass + 5,710 rules + 9 AST Mathlib 4.36 transforms + `AEMeasurable` closer** | **451 (ALL depth-0 failures)** | **151** | **33.48%** | **43.07%** (`115 / 267`) | **89.80%** (`2,640 / 2,940`) | **1,210.2s** (10w) | **0 B / \$0** |

* **Full table of all 151 live-verified `v0.4` modules & exact mechanical repairs:** [`reports/live_436_v04_report.md`](reports/live_436_v04_report.md) ([JSON](reports/live_436_v04_report.json)).
* **Previous `v0.3` baseline report:** [`reports/live_436_v03_report.md`](reports/live_436_v03_report.md) ([JSON](reports/live_436_v03_report.json)).

### New Mathlib `v4.36.0` Mechanical Transforms in `v0.4` (`src/mathlib436_transforms.py`)

| Transform | Pattern Handled | Live Verified Ops in `v0.4` |
| :--- | :--- | :---: |
| Official + curated renames | 5,703 `@[deprecated]` aliases + `Ideal.isMaximal_under_of_isIntegral_of_isMaximal`, `DistribSMul.toAddMonoidHom`, `Measurable.tsum`, `AEMeasurable.tsum`, `Set.mem_ofPred_eq`, `Ideal.isPrime_bot` | **104** |
| `prod_mono` | `Finset.prod_le_prod` → `prod_le_prod₀`, `prod_le_one` → `prod_le_one₀`, `prod_le_prod_of_subset_of_one_le` → `...₀` (`MulLeftMono` / `GroupWithZero`) | **31** |
| `mvpoly_coeff_dot` | Bracket-balanced `MvPolynomial.coeff d p` / bare `coeff d p` → `p.coeff d` (statement-equivalent dot projection) | **12 modules** |
| `prune_dead_zero_alt` | Prune dead `\| zero => ...` branch (`Invalid alternative name 'zero'`, e.g. `TensorProduct.induction_on`) | **11 modules** |
| `poly_coeff_dot` | Bracket-balanced `Polynomial.coeff p n` → `p.coeff n` | **6 modules** |
| `aemeasurable` | Targeted `Measure.map_smul` side-goal closers (`continuous_inv.aemeasurable`, `<h>.measurable.aemeasurable`, `fun_prop`, `measurability`) | **5 modules** |
| `prune_closed` | Redundant closed-goal tactic line pruning (`No goals to be solved`) | **3 modules** |
| `noncomputable` | Expanded `dependsOnNoncomputable` / `consider marking it as 'noncomputable'` → `noncomputable def` | **2 modules** |
| `ldl_lower_inv_triangular` | `fun i j hij => LDL.lowerInv_triangular hS ...` → `LDL.isLowerTriangular_lowerInv hS` | **1 module** (`v0.4.0`) |
| `powerseries_ddx_implicit_ring` | PowerSeries `d⁄dX R f` → `d⁄dX f` (implicit ring argument) | **1 module** (`v0.4.0`) |
| `mvpoly_coeff_zero` | `rw [coeff_zero]` → `simp only [AddMonoidAlgebra.coeff_zero, Finsupp.zero_apply]` | Added in **`v0.4.1`** (`P0285` `M165552`) |
| `finsupp_mapdomain_apply_of_injective` | `Finsupp.mapDomain_apply hinj` → `Finsupp.mapDomain_apply_of_injective hinj` + safe `prune_closed` pass guard | Added in **`v0.4.2`** (`P0316` `M106522`, `M106527`) |
| `mvpowerseries_pderiv_implicit_ring` / multi-line `mvpoly_coeff_dot` | `MvPowerSeries.pderiv R i` → `MvPowerSeries.pderiv i`, `PowerSeries.derivative R` → `PowerSeries.derivative`, multi-line `MvPolynomial.coeff` | Added in **`v0.4.3`** (`P0325` `M144323`–`M144325`, `M144340`) |
| `is_integral_algebra_map_iff` | `(isIntegral_algebraMap_iff <hinj>).1` → `isIntegral_algebraMap_iff.1` (implicit `FaithfulSMul`) | Added in **`v0.4.4`** (`P0254` `M071140`) |
| `ff_x_pow_{nat_degree,ne_zero}` + identifier renames | `FiniteField.X_pow_card_sub_X_{natDegree_eq,ne_zero} R h` → `Polynomial.{natDegree_X_pow_sub_X,X_pow_sub_X_ne_zero} h`; error-gated `continuous_mul_right` → `continuous_mul_const` & `integral_finset_sum` → `integral_finsetSum` | Added in **`v0.4.4`** (`P0123` `M071367`, `M072010`, `M072764`) |

### Highlights of Verified Real Fixes (`0 sorry`, `leanprover/lean4:v4.36.0`)
- `M002361`: `mvpoly_coeff_dot(7)` + `aemeasurable: exact hc.measurable.aemeasurable@L64` (2-pass combined fix)
- `M018207`: `mvpoly_coeff_dot(14)` (14 nested `MvPolynomial.coeff` calls rewritten cleanly in one file)
- `M000028` / `M000030` / `M000031`: `prod_le_prod₀`, `prod_le_one₀`, `prod_le_prod_of_subset_of_one_le₀`
- `M000069`: `Ideal.isMaximal_comap_of_isIntegral_of_isMaximal → Ideal.isMaximal_under_of_isIntegral_of_isMaximal`
- `M000526`: `LDL.lowerInv_triangular → LDL.isLowerTriangular_lowerInv`
- `M002399`: PowerSeries `d⁄dX A (epSer W) → d⁄dX (epSer W)`
- `M006224`: Pruned dead `\| zero => ...` branch in `TensorProduct` induction
- `M046312`: `Polynomial.coeff F (0 : ℕ) → F.coeff (0 : ℕ)`

---

## 3. Quickstart for Contributors

### 1. Run Unit Tests for `v0.4` Transforms
```bash
python3 tests/test_mathlib436_transforms.py
```

### 2. Inspect Triage Breakdown
```bash
python3 src/cli.py triage --results data/triage/results.json
```

### 3. Regenerate the Official Mathlib Rename Dictionary (Any Two Mathlib Commits)
```bash
python3 src/extract_mathlib_renames.py \
  --mathlib-old /path/to/mathlib-v4.33.1/Mathlib \
  --mathlib-new /path/to/mathlib-v4.36.0/Mathlib \
  --out data/mathlib_433_to_436_renames.json
```

### 4. Run Verified `0 sorry` Mechanical Repair on a Single Module
```bash
python3 src/cli.py repair \
  --module Development.AbelianVarietyTheory.BlockTheory.HeightDefect.SphereBlockLogMean \
  --id M002361 \
  --checkout /path/to/prepared-lean436-checkout \
  --out-dir ./verified_patches
```

### 5. Batch Parallel Run Over All Failures in a Triage File
```bash
python3 src/live_436_benchmark.py \
  --checkout /path/to/prepared-lean436-checkout \
  --results data/triage/results.json \
  --renames data/mathlib_433_to_436_renames.json \
  --out-dir ./verified_patches \
  --report ./reports/live_run.json \
  --workers 10 \
  --all-failures
```

---

## 4. Limitations & Dual-System Design

`werr-lean-triage` intentionally **does not** attempt to synthesize arbitrary semantic proof rewrites, non-equivalent API changes, or heartbeat-timeout refactors (`Submodule.IsLattice` → `IsFullLattice` audits should always be run with `port/islattice_audit.lean` and `port/reused_audit.lean`). Instead, it handles ~90% of depth-0 modules deterministically at 0 cost (`2,640 / 2,940`) and cleanly escalates the remaining ~10% genuinely hard modules (`300 / 2,940`) to a System-2 solver (human contributor or coding LLM), with the Lean `v4.36.0` kernel serving as the sole ground-truth authority.

---

## 5. Community Contributions (`rohanarun/alpoge-rh-replay`)

- **Lean `v4.36.0` Porting PRs (190 modules submitted across 7 packets — 91 merged across 4 PRs + 99 in review across 3 PRs; 3 complete whole-packet closures + 4 large partial waves):**
  - [`PR #33850`](https://github.com/rohanarun/alpoge-rh-replay/pull/33850) (`OPEN`) — `Port P0123 to Lean 4.36` (completes 100% of depth-1 packet `P0123`, `Closes #33568`: 20/20 modules — 13 unchanged + 7 patched, including `Polynomial.coeff` auto-fix and `FiniteField.X_pow_card_sub_X_*` / `continuous_mul_const` / `integral_finsetSum` patterns distilled into `v0.4.4`; clean `--no-cache` build in 34.4s, `0` audit hits, `validate_ports.py` exit 0)
  - [`PR #33639`](https://github.com/rohanarun/alpoge-rh-replay/pull/33639) (`OPEN`) — `Port P0254: 49 ready modules to Lean 4.36` (depth-3 packet `P0254`, `Closes #33550`: 46 unchanged + 3 patched — fed `isIntegral_algebraMap_iff` implicit-injectivity transform into `v0.4.4`; clean `--no-cache` build in 65.1s, `0` audit hits, `validate_ports.py` exit 0)
  - [`PR #33361`](https://github.com/rohanarun/alpoge-rh-replay/pull/33361) (`OPEN`) — `Port P0325: 30 ready modules to Lean 4.36` (depth-4 packet `P0325`, `Closes #33311`: 24 unchanged + 6 patched — fed multi-line `MvPolynomial.coeff` + `MvPowerSeries.pderiv` / `PowerSeries.derivative` implicit ring transforms into `v0.4.3`; clean `--no-cache` build in 63.7s, `0` audit hits, `validate_ports.py` exit 0)
  - [`PR #33265`](https://github.com/rohanarun/alpoge-rh-replay/pull/33265) (`MERGED`) — `Port P0316: 39 ready modules to Lean 4.36` (depth-4 packet `P0316`, claim `#33189`: 35 unchanged + 4 patched — fed `Finsupp.mapDomain_apply_of_injective` & safe `prune_closed` pass separation into `v0.4.2`; clean `--no-cache` build in 59.9s, `0` audit hits, `validate_ports.py` exit 0)
  - [`PR #32963`](https://github.com/rohanarun/alpoge-rh-replay/pull/32963) (`MERGED`) — `Port P0285: 48 ready modules to Lean 4.36` (depth-3 packet `P0285`, claim `#32755`: 45 unchanged + 3 patched — `M166247` & `M166255` auto-fixed by `werr-lean-triage v0.4.0`, `M165552` led to `mvpoly_coeff_zero` in `v0.4.1`; clean `--no-cache` build in 68.6s, `0` audit hits, `validate_ports.py` exit 0)
  - [`PR #32234`](https://github.com/rohanarun/alpoge-rh-replay/pull/32234) (`MERGED`) — `Port P0189 to Lean 4.36` (completes 100% of depth-2 packet `P0189`; clean `--no-cache` build, `0` audit hits, `validate_ports.py` exit 0)
  - [`PR #32236`](https://github.com/rohanarun/alpoge-rh-replay/pull/32236) (`MERGED`) — `Port P0196 to Lean 4.36` (completes 100% of depth-2 packet `P0196` including `MvPolynomial.coeff` → `.coeff` migration; clean `--no-cache` build, `0` audit hits, `validate_ports.py` exit 0)
- **Lean `v4.33.1` Independent Replay:**
  - [`P2382` (`#26536`)](https://github.com/rohanarun/alpoge-rh-replay/issues/26536) — 64 target modules + 27,817 transitive prerequisites compiled and accepted, plus warm-cache replay submissions (`M100691`, `M036503`, `M003484`, `M003638`, `M003861`, `M003041`, `M003738`, `M003907`, `M018272`, `M080966`, etc.).

---

## License

Licensed under the [Apache License 2.0](LICENSE) (matching the Mathlib4 standard).
