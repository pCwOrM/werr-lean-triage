# WERR-Lean-Triage: System-1 0-VRAM Porting & Tactic Router for Lean 4

An experimental, zero-VRAM **System-1 diagnostic triage and tactic-routing engine** designed to accelerate large-scale Lean 4 toolchain migrations—specifically benchmarked on the **Lean 4.33.1 → Lean 4.36.0** porting campaign of Levent Alpöge's formalized Riemann Hypothesis archive (`rohanarun/alpoge-rh-replay/port/triage`).

> [!IMPORTANT]
> **Scientific Scope & Honesty Statement**  
> `werr-lean-triage` is strictly a **System-1 heuristic prioritizer and mechanical repair router**. It is **not** a proof checker or kernel and makes zero claims of proof validity on its own. Every candidate patch or tactic sequence it proposes **must** be compiled and verified with `0 sorry` / `0 admit` by the official pinned `leanprover/lean4:v4.36.0` kernel (`src/port_patch_runner.py`).

---

## 1. Empirical Findings from 2,940 Real Depth-0 Modules

Analyzing [`rohanarun/alpoge-rh-replay/port/triage/results.json`](data/triage/results.json) (`leanprover/lean4:v4.36.0`, Mathlib `fc4f59e577fe`):

- **Total triaged depth-0 modules:** `2,940`
- **Compile unchanged (`ok`):** `2,489` (`84.66%`)
- **Fail unchanged (`fail`):** `451` (`15.34%`)

### Repair-Lane Breakdown of the 451 Failures

| Repair Lane | Count | Share (%) | System-1 Offloadable? |
| :--- | ---: | ---: | :---: |
| `LANE_B_RENAME_MIGRATION` (`unknown_identifier`, `unknown_constant`, `invalid_field_or_struct`) | 182 | **40.4%** | Yes (0-VRAM lookup) |
| `LANE_D_SIGNATURE_OR_LLM` (`app_type_mismatch`, `type_mismatch`, `typeclass_synthesis`) | 179 | **39.7%** | Escalate to System-2 |
| `LANE_A_TRIVIAL_PRUNE` (`no_goals_to_be_solved`, `invalid_alternative_name`) | 50 | **11.1%** | Yes (0-VRAM prune) |
| `LANE_C_TACTIC_CLOSER` (`unsolved_goals`, `simp`/`rw`/`rfl` failures) | 37 | **8.2%** | Yes (0-VRAM tactic router) |
| `LANE_E_HEARTBEAT_ESCALATE` (`heartbeat_timeout`) | 3 | **0.7%** | Escalate to System-2 |

**Key Insight:** **59.6% (269 / 451)** of depth-0 porting failures fall into mechanical System-1 lanes (`LANE_A` + `LANE_B` + `LANE_C`)—dominated by systematic Mathlib 4.34–4.36 renames such as `continuous_finset_sum` (12), `integral_finset_sum` (11), `Finsupp.finset_sum_apply` (9), `MvPolynomial.coeff` (14), and `Submodule.IsLattice.span_eq_top` (4).

---

## 2. Offline A/B Routing Benchmark (v0.1)

Measured locally on all 451 real failing compiler excerpts (zero server CPU load, zero GPU/VRAM):

| Policy | VRAM | Latency (µs / module) | Lane Agreement (%) | System-1 Offload Candidates |
| :--- | :---: | ---: | ---: | ---: |
| Fixed-Order Baseline | 0 B | 2.03 µs | 39.69% (179/451) | 0 |
| **WERR System-1 Router (v0.1)** | **0 B** | **774.39 µs** | **50.11% (226/451)** | **296** |

Full tables and top renamed symbols are recorded in [`reports/triage_benchmark_report.md`](reports/triage_benchmark_report.md).

---

## 3. Repository Layout

- `src/triage_parser.py` — Parses Lean 4.36.0 compiler diagnostics, extracts failing line numbers, error classes, and missing Mathlib symbols.
- `src/werr_tactic_router.py` — 0-VRAM System-1 router combining diagnostic cues with quadratic polynomial escape dynamics ($z_{n+1} = z_n^2 + c$).
- `src/benchmark_ab.py` — Reproducible offline A/B benchmark harness against fixed-order baselines.
- `src/port_patch_runner.py` — Post-replay live verification harness that applies candidate patches on `leanprover/lean4:v4.36.0`, checks `0 sorry`, and emits `PORTING.md`-compliant `.patch` + `.json` pairs.
- `reports/` — Generated JSON & Markdown benchmark reports.

---

## 4. Quickstart

```bash
python3 src/triage_parser.py
python3 src/benchmark_ab.py
```

### Next Step (Live Lean 4.36.0 Verification)
Once the active Lean 4.33.1 replay build completes on the Linux build server, run `src/port_patch_runner.py` against a clean `leanprover/lean4:v4.36.0` checkout to measure **true end-to-end compiled patch pass rate (0 sorry)** and contribute verified porting PRs to `rohanarun/alpoge-rh-replay`.
