#!/usr/bin/env python3
"""
WERR-Lean-TacticRouter (System-1 0-VRAM Heuristic Policy for Lean 4.33 -> 4.36 Porting).

Uses deterministic quadratic polynomial escape dynamics (z_{n+1} = z_n^2 + c)
to project Lean 4 compiler diagnostics and goal signatures into a zero-VRAM,
sub-millisecond repair-lane & tactic priority distribution.

IMPORTANT SCIENTIFIC SCOPE:
This router is strictly a System-1 heuristic prioritizer (triage gate).
It NEVER claims proof validity on its own; every suggested repair or tactic
MUST be verified by the standard Lean 4.36.0 kernel (0 sorry).
"""
from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from typing import Dict, List, Tuple

from triage_parser import TriageRecord

# Ordered candidate tactic bank for Lean 4.36.0 Mathlib
TACTIC_BANK = [
    "delete_redundant_line",  # for no_goals_to_be_solved
    "rename_mathlib_ident",   # for unknown_identifier / unknown_constant
    "simp_all",               # general simplification
    "grind",                  # Lean 4.20+ SMT/congruence closer
    "omega",                  # linear integer/nat arithmetic
    "ring",                   # commutative ring identities
    "linarith",               # linear real/rational inequalities
    "norm_num",               # numerical normalization
    "positivity",             # positivity goals
    "fun_prop",               # continuity / measurability / differentiability
    "aesop",                  # automated tableau search
    "escalate_system2_llm",   # fallback to System-2 LLM when System-1 fails
]

# Domain-aware keyword weights for lightweight feature extraction (zero GPU/VRAM)
DOMAIN_SIGNALS = {
    "delete_redundant_line": (
        "No goals to be solved",
        "Invalid alternative name",
        "no unhandled alternatives",
    ),
    "rename_mathlib_ident": (
        "Unknown identifier",
        "Unknown constant",
        "is not a field of structure",
        "Invalid field",
        "has already been declared",
    ),
    "simp_all": (
        "'simp' made no progress",
        "Tactic 'simp' failed",
        "Tactic 'rfl' failed",
        "Tactic 'rewrite' failed",
        "unsolved goals",
    ),
    "grind": (
        "unsolved goals",
        "Tactic 'rfl' failed",
        "Tactic 'rewrite' failed",
        "⊢ ",
    ),
    "omega": (
        "unsolved goals",
        "Nat.",
        "Int.",
        "Fin ",
        "Finset.card",
        "List.length",
    ),
    "ring": (
        "unsolved goals",
        "CommRing",
        "Polynomial",
        "MvPolynomial",
        "Matrix.det",
    ),
    "linarith": (
        "unsolved goals",
        "Real.",
        "ENNReal",
        "NNReal",
        "norm_",
    ),
    "norm_num": (
        "unsolved goals",
        "Rat.",
        "Nat.cast",
        "Int.cast",
        "OfNat.ofNat",
    ),
    "positivity": (
        "unsolved goals",
        "0 <",
        "0 ≤",
        "norm_nonneg",
        "Real.exp_pos",
    ),
    "fun_prop": (
        "unsolved goals",
        "Continuous",
        "ContDiff",
        "Measurable",
        "Differentiable",
        "Integrable",
    ),
    "aesop": (
        "unsolved goals",
        "Submodule",
        "Ideal.",
        "Set.mem",
    ),
    "escalate_system2_llm": (
        "Application type mismatch",
        "Type mismatch",
        "type mismatch",
        "Function expected at",
        "failed to synthesize",
        "could not synthesize default value",
        "Invalid projection",
        "maximum number of heartbeats",
        "deterministic) timeout",
    ),
}


@dataclass
class RouteDecision:
    task_id: str
    predicted_lane: str
    ranked_tactics: List[Tuple[str, float]]
    system1_actionable: bool
    boundary_energy: float


def polynomial_escape_response(cx: float, cy: float, max_iter: int = 32) -> float:
    """
    Deterministic quadratic polynomial escape dynamics (z_{n+1} = z_n^2 + c).
    Returns a smooth bounded stability/escape score in [0.0, 1.0].
    """
    zx, zy = 0.0, 0.0
    for i in range(max_iter):
        zx2 = zx * zx
        zy2 = zy * zy
        if zx2 + zy2 > 4.0:
            # Smooth normalized escape velocity
            return (i + 1.0) / float(max_iter)
        zy = 2.0 * zx * zy + cy
        zx = zx2 - zy2 + cx
    return 1.0


def feature_to_boundary_coords(text: str, tactic: str) -> Tuple[float, float]:
    """
    Map (diagnostic text, candidate tactic) deterministically onto a resonant
    patch near the boundary of the Mandelbrot set (partial M) around c = -0.75 + 0.1i.
    """
    sig = f"{tactic}|{text[:512]}".encode("utf-8", errors="ignore")
    digest = hashlib.blake2b(sig, digest_size=8).digest()
    u = int.from_bytes(digest[:4], "big") / float(2**32)
    v = int.from_bytes(digest[4:], "big") / float(2**32)
    # Perturb tightly around the period-2 bulb neck (-0.75, 0.12) where escape sensitivity is maximal
    cx = -0.75 + (u - 0.5) * 0.18
    cy = 0.12 + (v - 0.5) * 0.18
    return cx, cy


def route_werr_system1(record: TriageRecord) -> RouteDecision:
    """
    System-1 0-VRAM Tactic & Repair-Lane Router.
    Combines deterministic lexical/AST-cue scoring with polynomial boundary dynamics
    tie-breaking & multi-scale energy modulation.
    """
    if record.status == "ok":
        return RouteDecision(
            task_id=record.id,
            predicted_lane="UNCHANGED_OK",
            ranked_tactics=[],
            system1_actionable=True,
            boundary_energy=0.0,
        )

    text = f"{record.module}\n{record.excerpt}"
    scores: Dict[str, float] = {}
    energies: List[float] = []

    for tactic in TACTIC_BANK:
        cues = DOMAIN_SIGNALS[tactic]
        hits = sum(1 for kw in cues if kw in text)
        base_score = 1.0 - math.exp(-0.9 * hits) if hits > 0 else 0.0

        # Multi-scale harmonic tripod (0.60x, 1.00x, 1.15x) over polynomial escape dynamics
        cx, cy = feature_to_boundary_coords(text, tactic)
        e_low = polynomial_escape_response(cx * 0.60, cy * 0.60, max_iter=24)
        e_mid = polynomial_escape_response(cx, cy, max_iter=32)
        e_hi = polynomial_escape_response(cx * 1.15, cy * 1.15, max_iter=32)
        boundary_mod = 0.25 * e_low + 0.50 * e_mid + 0.25 * e_hi
        energies.append(boundary_mod)

        # Diagnostic evidence dominates; boundary dynamics modulates tie-breaks & confidence
        scores[tactic] = round(base_score * 0.90 + boundary_mod * 0.10, 6)

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    top_tactic = ranked[0][0]

    # Map top-ranked System-1 tactic to operational repair lane
    if top_tactic == "delete_redundant_line":
        lane = "LANE_A_TRIVIAL_PRUNE"
        actionable = True
    elif top_tactic == "rename_mathlib_ident":
        lane = "LANE_B_RENAME_MIGRATION"
        actionable = True
    elif top_tactic in ("simp_all", "grind", "omega", "ring", "linarith", "norm_num", "positivity", "fun_prop", "aesop"):
        lane = "LANE_C_TACTIC_CLOSER"
        actionable = True
    else:
        lane = "LANE_E_HEARTBEAT_ESCALATE" if "heartbeat" in text.lower() else "LANE_D_SIGNATURE_OR_LLM"
        actionable = False

    return RouteDecision(
        task_id=record.id,
        predicted_lane=lane,
        ranked_tactics=ranked[:5],
        system1_actionable=actionable,
        boundary_energy=round(sum(energies) / max(1, len(energies)), 5),
    )


def route_fixed_baseline(record: TriageRecord) -> RouteDecision:
    """Naive fixed-order baseline: always tries simp_all first, then escalates to LLM."""
    if record.status == "ok":
        return RouteDecision(record.id, "UNCHANGED_OK", [], True, 0.0)
    return RouteDecision(
        task_id=record.id,
        predicted_lane="LANE_D_SIGNATURE_OR_LLM",
        ranked_tactics=[("simp_all", 0.5), ("aesop", 0.3), ("escalate_system2_llm", 0.2)],
        system1_actionable=False,
        boundary_energy=0.0,
    )
