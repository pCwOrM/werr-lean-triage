# WERR-Lean-Triage: 0-VRAM System-1 Porting & Migration Helper for Lean 4

[![Lean 4.36.0 Verified](https://img.shields.io/badge/Lean_4.36.0_Live_Verified-77%2F269_(28.62%25)_0_sorry-brightgreen.svg)](reports/live_436_v03_report.md)
[![Mathlib Renames](https://img.shields.io/badge/Mathlib_4.33%E2%86%924.36-5%2C703_Official_Renames-blue.svg)](data/mathlib_433_to_436_renames.json)
[![VRAM](https://img.shields.io/badge/VRAM-0_Bytes_(CPU--Only)-purple.svg)](#2-live-lean-4360-verification-results-v03)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-orange.svg)](LICENSE)

An open-source, zero-VRAM **System-1 diagnostic triage and multi-pass mechanical repair helper** built to accelerate the **Lean `v4.33.1` → `v4.36.0` / Mathlib `v4.36.0`** porting campaign for Levent Alpöge's formalized Riemann Hypothesis archive ([`rohanarun/alpoge-rh-replay`](https://github.com/rohanarun/alpoge-rh-replay)).

> [!IMPORTANT]
> **Scientific Scope & Honesty Statement**  
> `werr-lean-triage` is strictly a **System-1 triage router and mechanical migration helper**. It is **not** a proof kernel or theorem prover, and makes zero claims of proof validity on its own. Every candidate patch it generates is compiled and verified (`exit 0`, zero `sorry`, zero `admit`, zero new `axiom`, statement-preserving) by the official pinned `leanprover/lean4:v4.36.0` compiler before being emitted.

---

## 1. Empirical Error Taxonomy (2,940 Real Depth-0 Modules)

Parsed from [`rohanarun/alpoge-rh-replay/port/triage/results.json`](data/triage/results.json) (`leanprover/lean4:v4.36.0`, Mathlib `fc4f59e577fe`):

- **Total triaged depth-0 modules:** `2,940`
- **Compile unchanged (`ok`):** `2,489` (`84.66%`) — **0 LLM tokens needed**
- **Fail unchanged (`fail`):** `451` (`15.34%`)

| Repair Lane | Count | Share of Failures | Handled By |
| :--- | ---: | ---: | :--- |
| `LANE_B_RENAME_MIGRATION` (`unknown_identifier`, `unknown_constant`, `invalid_field_or_struct`) | 182 | **40.4%** | System-1 (5,703 Mathlib renames) |
| `LANE_A_TRIVIAL_PRUNE` (`no_goals_to_be_solved`, `invalid_alternative_name`) | 50 | **11.1%** | System-1 (closed-goal line prune) |
| `LANE_C_TACTIC_CLOSER` (`unsolved_goals`, `simp`/`rw`/`rfl` failures) | 37 | **8.2%** | System-1 (ranked tactic closers) |
| `LANE_D_SIGNATURE_OR_LLM` (`app_type_mismatch`, `type_mismatch`, `typeclass_synthesis`) | 179 | **39.7%** | Escalate to System-2 (LLM / human) |
| `LANE_E_HEARTBEAT_ESCALATE` (`heartbeat_timeout`) | 3 | **0.7%** | Escalate to System-2 (human refactor) |

---

## 2. Live Lean `v4.36.0` Verification Results (`v0.3`)

We extracted **5,703 official `@[deprecated]` rename/alias entries** directly from the Mathlib `v4.33.1` and `v4.36.0` source trees (`src/extract_mathlib_renames.py`) and evaluated our 4-pass iterative mechanical repair engine (`src/live_436_benchmark.py`) across all **269 System-1 candidate failures** (`LANE_A` + `LANE_B` + `LANE_C`) on real `leanprover/lean4:v4.36.0`:

| Version | Strategy | Evaluated Modules | Live Verified `0 sorry` Fixes | Fix Rate | Wall Time | VRAM / API Cost |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `v0.2` | Single-pass, 9 hand-guessed renames | 120 | 2 | 1.67% | 430.4s | 0 B / \$0 |
| **`v0.3`** | **4-pass iterative + 5,703 official Mathlib renames + namespace preservation** | **269** | **77** | **28.62%** | **953.7s** (8 workers) | **0 B / \$0** |

* **Combined Zero-LLM Coverage on Depth-0:** `2,489` unchanged + `77` mechanically verified fixes = **`2,566 / 2,940` (`87.28%`)** compiling on Lean `v4.36.0` with **zero LLM API calls** and **`0 sorry`**.
* **Full table of all 77 verified modules & exact mechanical repairs:** [`reports/live_436_v03_report.md`](reports/live_436_v03_report.md) ([JSON](reports/live_436_v03_report.json)).

### Examples of Verified Real Fixes (`0 sorry`, `leanprover/lean4:v4.36.0`)
- `M020874`: `SchwartzMap.fourierTransformCLE → FourierTransform.fourierCLE`
- `M030617`: `integral_finset_sum → integral_finsetSum; tendsto_finset_sum → tendsto_finsetSum; tendsto_finset_prod → tendsto_finsetProd` (3 renames in one file)
- `M081483`: `Finsupp.finset_sum_apply → Finsupp.finsetSum_apply; Polynomial.eval_finset_sum → Polynomial.eval_finsetSum; Polynomial.finset_sum_coeff → Polynomial.finsetSum_coeff`
- `M091697`: `LinearMap.exists_monic_and_coeff_mem_pow_and_aeval_eq_zero_of_range_le_smul → LinearMap.exists_monic_and_natDegree_eq_and_coeff_mem_pow_and_aeval_eq_zero`
- `M046242`, `M062816`: Pruned redundant closed-goal line (`No goals to be solved`)

---

## 3. Quickstart for Contributors

### 1. Inspect Triage Breakdown
```bash
python3 src/cli.py triage --results data/triage/results.json
```

### 2. Regenerate the Official Mathlib Rename Dictionary (Any Two Mathlib Commits)
```bash
python3 src/extract_mathlib_renames.py \
  --mathlib-old /path/to/mathlib-v4.33.1/Mathlib \
  --mathlib-new /path/to/mathlib-v4.36.0/Mathlib \
  --out data/mathlib_433_to_436_renames.json
```

### 3. Run Verified `0 sorry` Mechanical Repair on a Single Module
```bash
python3 src/cli.py repair \
  --module Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinrankEqZeroOfDualKilledByTensor \
  --id M031586 \
  --checkout /path/to/prepared-lean436-checkout \
  --out-dir ./verified_patches
```

### 4. Batch Parallel Run Over a Triage File
```bash
python3 src/live_436_benchmark.py \
  --checkout /path/to/prepared-lean436-checkout \
  --results data/triage/results.json \
  --renames data/mathlib_433_to_436_renames.json \
  --out-dir ./verified_patches \
  --report ./reports/live_run.json \
  --workers 8
```

---

## 4. Limitations & Dual-System Design

`werr-lean-triage` intentionally **does not** attempt to guess complex semantic API changes (`Application type mismatch`, `Type mismatch`, missing typeclass instances, or `MvPolynomial.coeff` signature changes). Instead, it solves mechanical migrations deterministically at 0 cost and cleanly escalates the remaining ~10–15% hard modules to a System-2 solver (human contributor or coding LLM), with the Lean `v4.36.0` kernel serving as the sole ground-truth authority.

---

## License

Licensed under the [Apache License 2.0](LICENSE) (matching the Mathlib4 standard).
