---
id: paper:2013russo-venue-research
type: paper
title: "Combustion of 1,5-dinitrobiuret (DNB) in the presence of nitric acid using ReaxFF molecular dynamics simulations (galley PDF)"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:energetic-materials
  - keyword:lammps
  - keyword:nve-simulation
  - keyword:galley-or-proof-pdf
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp403511q"
year: 2013
authors:
  - "Michael F. Russo, Jr."
  - "Dmitry Bedrov"
  - "Shashank Singhai"
  - "Adri C. T. van Duin"
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "180a26366631567e13040135ae633d547f0789653c31933f470027a058dacfac"
pdf_path: "papers/Russo_DNB_HNO3_JPCA_2013_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013russo-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    This slug is a **galley** PDF for the JPCA article also covered by [[2013russo-venue-jp403511q]].

## Summary

Reactive MD with a ReaxFF parametrization fit to quantum data for model species explores mixtures of **1,5-dinitrobiuret (DNB)** and **nitric acid** at 0.5 and 1.0 g/mL, targeting dense vapor- and liquid-like conditions. Simulations identify composition regimes where kinetics produce a **sharp thermal-energy release** interpreted as **spontaneous ignition / hypergolic-like** behavior, with discussion of dominant mechanistic steps.

## Methods

Grounding (galley): `papers/Russo_DNB_HNO3_JPCA_2013_galley.pdf`; `normalized/extracts/2013russo-venue-research_p1-2.txt` aligns with the same Computational Methods narrative as [[2013russo-venue-jp403511q]]. Prefer **`paper:2013russo-venue-jp403511q`** for **non-galley** pagination when available.

### 1 — MD application (mixtures + ramps)

- **Engine / code:** **Reactive MD** with **ReaxFF**; parameter distribution supports **standalone ReaxFF**, **LAMMPS**, and **ADF ReaxFF** (Computational Methods excerpt; same text as [[2013russo-venue-jp403511q]]).
- **System / PBC (mixtures, excerpt-backed):** **18 DNB + 18 HNO\(_3\)** and **37 + 37** in **2.5 nm** periodic cubes for **~0.5** and **~1.0 g/mL**, plus an **18 DNB / 180 HNO\(_3\)** case with enlarged box side lengths **3.65 nm** and **2.91 nm** as printed in the excerpt ([[2013russo-venue-jp403511q]] galley/VOR Methods opening).
- **Mixture equilibration/production protocol:** After minimization, each mixture system is run for **5 ps** **NVT** equilibration at **500 K** using a **Berendsen** thermostat (**500 fs** damping), followed by **NVE** production at **500 K** with **\(\Delta t = 0.1\) fs**, typically **500 ps** total (some runs extended/shortened depending on reactivity). These lines are readable from the **same article text** in `papers/Russo_DNB_HNO3_JPCA_2013.pdf` (Simulation Details); the galley **`pdf_path`** on this slug is harder to extract reliably, so prefer the non-galley PDF bytes when auditing.
- **Single-molecule ramps (excerpt-backed):** **20** runs with **one DNB** in a **2.5 nm** periodic box, **Berendsen** heating to **4000 K**, **500 fs** damping, **0.1 fs** timestep; **terminal NO\(_2\)** loss is the dominant first step in **all 20** simulations (Computational Methods excerpt).
- **Barostat:** N/A — not stated for these excerpts.
- **Temperature:** **4000 K** ramp target for single-molecule tests; mixture run temperatures are **not stated** on the indexed excerpt pages.
- **Pressure:** N/A.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training

Same **Jaguar B3LYP / 6-311G++\*\*** QM reference energies for **DNB dissociations** and **DCA→DNB** steps, trained into the **C/H/O/N hypergolic ReaxFF** extension, with **~6–8 kcal/mol** agreement claims for highlighted steps ([[2013russo-venue-jp403511q]] excerpt).

## Findings

- **Outcomes & mechanisms:** **Sharp thermal-energy release** at some **mixture compositions/densities**, interpreted as **spontaneous ignition / hypergolic-like** behavior (abstract), with mechanistic decomposition tied to **DNB/HNO\(_3\)** chemistry in the Results discussion.
- **Comparisons:** **QM energy matching** for trained channels and positioning vs **hypergolic ionic liquid** motivation literature (Introduction excerpt).
- **Sensitivity / design levers:** **0.5 vs 1.0 g/mL** and **stoichiometry variants** (including highly asymmetric ratios and pure-component controls) are explicit composition knobs in the Methods narrative on this galley-oriented page.
- **Limitations & outlook:** Reactive FF studies omit **multiphase fluid transport** and **drop-test hydrodynamics**; see **Limitations** section on this page for modeling scope caveats.
- **Corpus honesty:** **Galley PDF**; confirm numbers against **`paper:2013russo-venue-jp403511q`** + non-galley PDF if discrepancies are suspected.

## Limitations

Reactive FF fidelity is limited by training chemistry; real propellant interfaces involve multiphase flow and transport not fully captured in these atomistic cells.

## Relevance to group

ReaxFF application to **ionic-liquid / hypergolic-chemistry** motifs linked to nitric-acid oxidizers, with PSU authorship.

## Citations and evidence anchors

- DOI: [10.1021/jp403511q](https://doi.org/10.1021/jp403511q)
- Extract: `normalized/extracts/2013russo-venue-research_p1-2.txt`

## Related topics

- [[2013russo-venue-jp403511q]]
- [[reaxff-family]]
