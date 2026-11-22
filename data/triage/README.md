# Port triage

Depth-0 modules compiled **unchanged** on `leanprover/lean4:v4.36.0` with Mathlib `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`, one Lean process per module, on Google Cloud.

| Status | Modules |
|---|---:|
| ok | 2,489 |
| fail | 451 |
| **total** | **2,940** |

`results.json` lists each module's status, compile time and, for failures, the first compiler output (`excerpt`).
`ok` modules need only a `port/patches/<ID>.json` with `"notes": "unchanged"`. Start porting from `fail`.
Triage covers 2,940 of the 5,927 depth-0 modules so far.

The failing modules, grouped by packet with their first error: [failing.md](failing.md).
