# WERR-Lean-TacticRouter: Offline Triage Benchmark Report

- **Dataset:** `rohanarun/alpoge-rh-replay/port/triage/results.json`
- **Target Toolchain:** `leanprover/lean4:v4.36.0` / Mathlib `fc4f59e577fe`
- **Total Depth-0 Modules Triaged:** `2940` (`2489` unchanged OK = `84.66%`, `451` failing)

## 1. Empirical Error Taxonomy (451 Real Failures)

| Compiler Error Category | Count | Share (%) |
| :--- | ---: | ---: |
| `unknown_identifier` | 83 | 18.4% |
| `unknown_constant` | 77 | 17.1% |
| `app_type_mismatch` | 60 | 13.3% |
| `other` | 43 | 9.5% |
| `unsolved_goals` | 37 | 8.2% |
| `type_mismatch` | 35 | 7.8% |
| `no_goals_to_be_solved` | 35 | 7.8% |
| `invalid_field_or_struct` | 22 | 4.9% |
| `function_expected` | 19 | 4.2% |
| `invalid_alternative_name` | 15 | 3.3% |
| `typeclass_synthesis` | 12 | 2.7% |
| `default_value_synthesis` | 8 | 1.8% |
| `heartbeat_timeout` | 3 | 0.7% |
| `invalid_projection` | 2 | 0.4% |

## 2. Repair-Lane Distribution (Ground Truth)

| Repair Lane | Count | Share (%) | System-1 Candidate? |
| :--- | ---: | ---: | :---: |
| `LANE_B_RENAME_MIGRATION` | 182 | 40.4% | Yes (0-VRAM) |
| `LANE_D_SIGNATURE_OR_LLM` | 179 | 39.7% | No (Escalate to System-2) |
| `LANE_A_TRIVIAL_PRUNE` | 50 | 11.1% | Yes (0-VRAM) |
| `LANE_C_TACTIC_CLOSER` | 37 | 8.2% | Yes (0-VRAM) |
| `LANE_E_HEARTBEAT_ESCALATE` | 3 | 0.7% | No (Escalate to System-2) |

## 3. Offline A/B Routing Comparison (451 Failures)

| Policy | VRAM | Latency (µs / module) | Lane Agreement (%) | System-1 Offload Candidates |
| :--- | :---: | ---: | ---: | ---: |
| Fixed-Order Baseline | 0 B | 2.03 µs | 39.69% (179/451) | 0 |
| **WERR System-1 Router** | **0 B** | **774.39 µs** | **50.11% (226/451)** | **296** |

## 4. Top Missing / Renamed Mathlib Symbols (4.33.1 → 4.36.0)

| Symbol | Occurrences |
| :--- | ---: |
| `coeff` | 16 |
| `MvPolynomial.coeff` | 14 |
| `continuous_finset_sum` | 12 |
| `integral_finset_sum` | 11 |
| `Finsupp.finset_sum_apply` | 9 |
| `Polynomial.eval_finset_sum` | 7 |
| `eval_finset_sum` | 7 |
| `Polynomial.coeff` | 7 |
| `Finsupp.coe_finset_sum` | 5 |
| `Polynomial.finset_sum_coeff` | 5 |
| `Submodule.IsLattice.span_eq_top` | 4 |
| `coeff_add` | 4 |
| `tendsto_finset_sum` | 4 |
| `Algebra.adjoinCommRingOfComm` | 4 |
| `integrable_finset_sum` | 3 |

## 5. Honest Scope & Next Live Verification Step

> This offline A/B benchmark measures diagnostic triage speed and repair-lane routing accuracy on real Lean 4.36.0 compiler excerpts. True end-to-end patch success rate (compiled pass rate with 0 sorry) MUST be measured live against leanprover/lean4:v4.36.0 using src/port_patch_runner.py once the active replay build finishes.
