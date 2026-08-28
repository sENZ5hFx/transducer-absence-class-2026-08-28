# Transducer-Absence Class — Structural Novelty Session

**Timestamp:** 2026-08-28T13:40:00-EDT  
**Session ID:** 2026-08-28-tac-homonym-collapse  
**Author:** Haley Bird (Fishers, IN)  
**Status:** research-stage classification. Not a physical discovery, not peer review, not a patent, not proof.

> Claim hygiene: copyright may protect this expression. It does not confer scientific priority, patent rights, or validation of any natural hypothesis.

## Primary insight

After subtracting this archive's prior syntheses (Dark Biosphere Hypothesis 2026-05-14; undersampling 2026-08-03; deep-biosphere-as-space-prior 2026-08-14), the remaining gap is not "the deep is unexplored."

**The Transducer-Absence Class.** Science detects a signal from an invisible layer and names the layer *dark* instead of locating the converter. When one name covers unequal claims, the weakest claim becomes the policy object.

That collapse is **ACTIVE** for "dark oxygen" (index 1.0644):

| ID | Mechanism | Evidence | Policy object? | Load-bearing in May 14 hypothesis? |
|---|---|---|---|---|
| A | Microbial NO / chlorite dismutation | 0.85 established | no | no |
| B | Crustal radiolytic ± biotic O2 in 1.2-Gyr brine (Moab Khotsong; Ruff; New Yorker 13 Aug 2026; NASA OxyMoRon) | 0.78 observed; split unproved | no | no |
| C | Nodule electrolysis / geobattery (Sweetman 2024) | 0.28 — Nature Geoscience Editor's Note **8 Apr 2026** | **yes** | **yes** |

Correction: (C) cannot carry that weight. (B) is the stronger quieter phenomenon and is itself mechanistically unproved.

## Unspoken unproved things, by realm

Ranked by unspoken-TAC (famous unsolved problems downranked).

1. **Land — Omnitrophota.** Ancient globally common bacterial phylum, still mostly uncultured. No laboratory transducer.
2. **Animals — magnetoreceptor cell.** Sense robust in birds, turtles, salmon, insects. Sixty years on, the converting cell is unlocated in any animal (Hore 2026). CRY4a is a candidate, not a located receptor.
3. **Earth crust — radiolytic/biotic dark oxygen.** Trace O2 in water isolated ~1.2 Gyr at Moab Khotsong. Biology vs radioactivity unproved. NASA already using it as an astrobiology prior.
4. **Humans / every cell — ordered water in transcription.** Li et al., Molecular Cell 2026: RNA Pol II at 1.96–2.33 Å contains 700–1,350 ordered waters that participate in catalysis. Authors call water the "dark matter of transcription."
5. **Humans — biophoton signaling.** Ultraweak photon emission is real. That the glow carries information is unproved.
6. **Ocean — hadal microbial dark matter.** MEER: 7,564 species, 89.4% unreported (Xiao et al., Cell 2025). Previously covered Aug 3/14 — retained, not claimed as new.
7. **Space — 3I/ATLAS water.** Third interstellar object (Jul 2025); ≥30× semi-heavy water. No source-star map.
8. **Space — icy-moon habitability converter.** Habitable → inhabited is undefined. Honest analog is crustal O2 (B), not (C).
9. **Ocean / policy — nodule DOP.** Unreplicated, under editor's note, highest industrial pressure.
10. **Space / spoken — Hubble crisis.** Local H0 ~73.2–73.5 vs Planck 67.27; H0DN ~7.1σ vs CMB (Cai & Wang 2026).
11. **Humans / spoken — consciousness.** No converter from spike to feel. Last on an unspoken list because it is the most spoken unproved thing.

**Falsification rule:** if the effect survives physical removal of the named converter, the converter is wrong — the phenomenon does not become darker. If two mechanisms share one name, split the name before any policy citation.

## Engine

See `tac_engine.py`.

```
TAC_raw = effect_confidence × (1 − converter_located) × (1 + industrial_pressure) × (1 + 0.12 × links) × novelty
unspoken_TAC = TAC_raw × (1 − spokenness)^1.4
```

## Capability gap

No existing tool tracks scientific-name homonym collapse against evidential status and policy/hypothesis use in real time.

## Files

- `tac_engine.py` — scorer, unspokenness penalty, homonym-collapse index, falsification ladder
- `SESSION_LOG.json` — structured session log
- `ranking.json` — full 14-phenomenon ranking
- `SESSION_OUTPUT.md` — full labeled workflow

## Notion

https://app.notion.com/p/3ca4e96f134c81e09ea7d9f59eb4887a
