"""Transducer-Absence Class (TAC) engine.

Session: 2026-08-28T13:40:00-EDT
Author of session synthesis: Haley Bird (archive) / autonomous research agent

This module does not claim a new physical mechanism. It classifies
scientific problems that share a structure:

    robust-or-claimed EFFECT + unlocated CONVERTER + optional
    industrial/policy action preceding mechanism + optional
    homonymic collapse of unequal claims under one popular name.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable, Literal

ConverterStatus = Literal["located", "candidate", "absent", "contested"]


@dataclass(frozen=True)
class Phenomenon:
    name: str
    realm: str
    effect: str
    claimed_converter: str
    converter_status: ConverterStatus
    effect_confidence: float
    converter_located: float
    industrial_pressure: float
    cross_realm_links: int
    primary_source: str
    unproved_sentence: str
    prior_session_covered: bool
    spokenness: float
    notes: str = ""

    def __post_init__(self) -> None:
        for label, val in (
            ("effect_confidence", self.effect_confidence),
            ("converter_located", self.converter_located),
            ("industrial_pressure", self.industrial_pressure),
            ("spokenness", self.spokenness),
        ):
            if not (0.0 <= val <= 1.0):
                raise ValueError(f"{label} must be in [0,1], got {val}")
        if self.cross_realm_links < 0:
            raise ValueError("cross_realm_links must be >= 0")


def tac_score(p: Phenomenon) -> dict:
    """Return raw TAC, ignorance volume, and policy risk."""
    absence = 1.0 - p.converter_located
    ignorance = p.effect_confidence * absence
    policy_risk = ignorance * (1.0 + p.industrial_pressure)
    connectivity = 1.0 + 0.12 * p.cross_realm_links
    novelty = 1.15 if not p.prior_session_covered else 0.72
    return {
        "tac_raw": round(policy_risk * connectivity * novelty, 4),
        "ignorance_volume": round(ignorance, 4),
        "policy_risk": round(policy_risk, 4),
    }


def unspoken_score(p: Phenomenon, tac: dict) -> dict:
    """Down-rank famous unsolved problems. unspoken_TAC = TAC_raw * (1 - spokenness)^1.4"""
    if not (0.0 <= p.spokenness <= 1.0):
        raise ValueError("spokenness out of range")
    factor = (1.0 - p.spokenness) ** 1.4
    return {
        "unspoken_tac": round(tac["tac_raw"] * factor, 4),
        "spokenness": p.spokenness,
        "unspoken_factor": round(factor, 4),
    }


@dataclass(frozen=True)
class HomonymMember:
    label: str
    mechanism: str
    status: str
    evidence: float
    policy_object: bool
    used_in_prior_hypothesis: bool

    def __post_init__(self) -> None:
        if not (0.0 <= self.evidence <= 1.0):
            raise ValueError("evidence must be in [0,1]")


def homonym_collapse_index(members: Iterable[HomonymMember]) -> dict:
    """Detect when one popular name covers unequal claims and the weakest is the policy/hypothesis beam."""
    items = list(members)
    if len(items) < 2:
        raise ValueError("homonym collapse requires >= 2 members")
    ev = [m.evidence for m in items]
    mean = sum(ev) / len(ev)
    var = sum((e - mean) ** 2 for e in ev) / len(ev)
    weak = min(items, key=lambda m: m.evidence)
    contamination = 0.0
    if weak.policy_object:
        contamination += 0.5
    if weak.used_in_prior_hypothesis:
        contamination += 0.5
    active = contamination >= 0.5 and var > 0.04
    return {
        "n_members": len(items),
        "mean_evidence": round(mean, 4),
        "evidence_variance": round(var, 4),
        "weakest": weak.label,
        "weakest_evidence": weak.evidence,
        "contamination_index": round(contamination * (1.0 + var), 4),
        "verdict": "HOMONyMIC COLLAPSE ACTIVE" if active else "labels aligned",
    }


def falsification_ladder(p: Phenomenon) -> list:
    """Cheapest-first observations that would locate or kill the converter."""
    if p.converter_status == "located":
        return ["Converter already located; replication, not discovery, is the task."]
    realm_default = {
        "outer_space": "Independent instrument, independent team, pre-registered reduction.",
        "ocean": "In-situ sensor with nodule-absent and nodule-present controls; report H2 if electrolysis is claimed.",
        "earth_crust": "Isotopic origin of O atoms + killed-control vs live-microbe incubations.",
        "animals": "Single-cell recording from the candidate organ while the field is rotated.",
        "humans": "Pre-registered replication with sham-field controls and open data.",
        "land": "Bring one type strain into culture, or prove unculturability with a defined medium matrix.",
    }
    steps = [
        f"State the converter as a yes/no: '{p.claimed_converter}'.",
        "Publish the negative-control outcome that would kill the claim.",
        realm_default.get(p.realm, "Independent replication with the converter physically removed."),
        "If the effect survives converter-removal, the named converter is wrong — not 'darker'.",
        "If two mechanisms share one name, split the name before any policy citation.",
    ]
    if p.industrial_pressure >= 0.5:
        steps.insert(0, "MORATORIUM ON ACTION: industrial_pressure>=0.5 and converter unlocated.")
    return steps


def rank_phenomena(phenomena: list) -> list:
    """Full ranking with TAC, unspoken TAC, and falsification ladder."""
    if not phenomena:
        raise ValueError("phenomena must be non-empty")
    rows = []
    for p in phenomena:
        tac = tac_score(p)
        unsp = unspoken_score(p, tac)
        row = asdict(p)
        row.update(tac)
        row.update(unsp)
        row["falsification_ladder"] = falsification_ladder(p)
        rows.append(row)
    rows.sort(key=lambda r: r["unspoken_tac"], reverse=True)
    for i, r in enumerate(rows, 1):
        r["rank_unspoken"] = i
    return rows
