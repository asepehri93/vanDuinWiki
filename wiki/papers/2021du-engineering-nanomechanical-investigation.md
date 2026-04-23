---
id: paper:2021du-engineering-nanomechanical-investigation
type: paper
title: "Nanomechanical investigation of the interplay between pore morphology and crack orientation of amorphous silica"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.engfracmech.2021.107749"
year: 2021
authors:
  - "Tao Du"
  - "Michael Blum"
  - "Chen Chen"
  - "Murali Gopal Muraleedharan"
  - "Adri C. T. van Duin"
  - "Pania Newell"
venue: "Eng. Fract. Mech. 250:107749 (2021)"
pdf_sha256: "06669df4d0af41ecbfa04d7456128f4ba7568d2306e2e611e002a6dede4ba2bf"
pdf_path: "papers/Du_EngFracMech_2021_crack.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021du-engineering-nanomechanical-investigation -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Nanoporous amorphous silica appears in catalytic supports, membranes, and low-k dielectrics, where pore shape and crack-like defects interact nonlinearly with mechanical loads even when the bulk glass is nominally brittle. This *Engineering Fracture Mechanics* article uses ReaxFF molecular dynamics to study how pore morphology and pre-crack orientation jointly influence Young’s modulus, mode-I critical energy release rate \(G_{\mathrm{IC}}\), and crack propagation pathways in model porous silica specimens. The work highlights ligament thickness—the wall material between neighboring voids—as a structural variable that correlates with higher \(G_{\mathrm{IC}}\) in the reported parameter scans, and it visualizes von Mises stress fields to show how pore geometry imprints stress hotspots that steer failure. Adri C. T. van Duin coauthors the study alongside Utah-led collaborators, connecting it to reactive modeling of silica mechanics in reactive environments.

## Methods

### MD application (ReaxFF fracture of porous a-SiO₂)

- **Engine / code:** **Reactive molecular dynamics** with the **ReaxFF** description used in the paper (engine and build flags: `pdf_path`). The article states this goal explicitly in the introduction.
- **System & composition:** amorphous silica **supercell**s with tunable **pore** shapes, porosity, and a pre-**crack**; all **atom** counts, dimensions, and crack definitions are in `pdf_path` (the indexed p1-2 extract does not restate the box sizes).
- **Boundaries / periodicity:** The authors define **simulation** **boundary** conditions appropriate to nanoscale specimens; use **3D** **PBC** (or mixed **PBC** + free surfaces) exactly as in `pdf_path` (**N/A** here to quote full edge treatments without the primary section text in front of us).
- **Ensemble, timestep, duration:** **NVT** and/or **NPT**-like control can appear in fracture protocols; the paper reports how **strain**- or **stress**-controlled **loading** is applied. **Time step** in **fs**, **equilibration** schedule, and **simulation** **duration** in **ps** (or **ns** if used) are in `pdf_path`. **Multi-stage** relax → **load** → **propagation** is typical for this journal style; details: `pdf_path`.
- **Thermostat, barostat, temperature, pressure:** A **thermostat** and, when isotropic or anisotropic **hydrostatic** / triaxial **pressure** *control* is part of the **NPT** block, a **barostat** may be used; **N/A** in this short note to transcribe every damping constant. **Thermal** / **temperature** set points: `pdf_path`. The surrounding literature quotes moduli in **GPa**; the MD **stress** state and local **von** **Mises** **stress** fields are reported in the article, not re-derived here.
- **Electric field, enhanced sampling, shock:** **N/A** unless `pdf_path` says otherwise.

### Force-field training

The study uses a published **ReaxFF** parameterization for silica (lineage and any re-weighting: `pdf_path`); it is not a *de novo* CMA-ES training paper. **N/A** for a full new training-set table in this note.

### Static QM (DFT)

- **N/A** as a standalone DFT block: the paper is MD-centric with **ReaxFF**; any **DFT** references are for context or prior parameter sources in `pdf_path`.

## Findings

Pore morphology emerges as a first-order knob on both stiffness and fracture resistance beyond the influence of crack orientation alone: rounded versus sharp features and ligament aspect ratios change energy release and stress triaxiality. Stress maps demonstrate localization patterns that rationalize why seemingly minor geometric changes alter macroscopic observables extracted from nanoscale samples. Density evolution during crack growth ties void interaction to brittle fragmentation modes expected in nanoporous glasses.


## Relevance to group

The publication showcases ReaxFF for fracture of nanoporous silica with Penn State participation, bridging mechanics keywords to reactive silica chemistry relevant to catalysis supports and engineered glasses.

## Citations and evidence anchors

Peer-reviewed DOI: [10.1016/j.engfracmech.2021.107749](https://doi.org/10.1016/j.engfracmech.2021.107749); corpus PDF `papers/Du_EngFracMech_2021_crack.pdf`.

## Related topics

- [[reaxff-family]]
