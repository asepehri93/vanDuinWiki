---
id: paper:2021susanna-monti-acs-diverse-phases
type: paper
title: "Diverse Phases of Carbonaceous Materials from Stochastic Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - domain:reactive-md
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:enhanced-sampling
  - keyword:thermal-decomposition
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.0c08029"
year: 2021
authors:
  - "Susanna Monti"
  - "Giovanni Barcaro"
  - "William A. Goddard III"
  - "Alessandro Fortunelli"
venue: "ACS Nano"
pdf_sha256: "bf99be1ba34fd41ba6886ddc2d4e29c246fdb8c341af1b19ad5c2f2ed76bbfee"
pdf_path: "papers/ReaxFF_others/Monti_ACSNano_2021_carbon_formation.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2021susanna-monti-acs-diverse-phases -->

## Summary

Amorphous and glassy carbons exhibit rich, density-dependent morphologies that are hard to tie to atomistic structure. The authors introduce **DynReaxMas** (dynamic reactive massaging of the potential energy surface): a protocol that combines **ReaxFF** molecular modeling with **potential energy surface transformations** and **global optimization** in a multidescriptor representation. The goal is to sample distinct local minima and morphologies at synthesis-relevant temperatures (on the order of ~2000 K in the discussion) without relying solely on extreme simulated-annealing temperatures that distort experimental comparability. The motivation is explicitly **structural diversity**: **mass density** alone is an insufficient **order parameter** when **pore** **statistics** and **graphitic** **domain** textures diverge at the same nominal density.

## Methods

**1 — MD application (ReaxFF + DynReaxMas).** **LAMMPS** **molecular dynamics** with **ReaxFF** drives **amorphous** / **glassy** **carbon** **supercells** under **3D** **PBC** with target **mass** **densities** **1.15**, **0.50**, and **0.16 g cm⁻³**; **NVT** **thermostat** **control** reaches ~**2000** **K** in the discussion without using only unphysical extreme **annealing** as the sole **sampling** tool. **Timestep** (**fs**), **equilibration** and **production** **lengths** in **ps**–**ns**, and **thermostat** **damping** are in *ACS Nano*. **Barostat** / **Hydrostatic** **pressure** sweeps: **N/A** in the density-targeted **protocol** excerpted here. **N/A —** applied **external** **electric** **field**. **Enhanced** **sampling** here is **DynReaxMas** (**PES** “massaging” + **global** **optimization** in a **multidescriptor** space), **not** **umbrella** / **replica** **exchange**; **N/A** to treat it as **metadynamics** in the conventional sense.

**2 — Force-field training. N/A** — the paper **applies** a published **ReaxFF** for **disordered** **carbon** rather than deriving a new **parameter** **set** in this work.

**3 — Experiments (comparison to literature).** **HRTEM**- and **porosity**-inspired **experimental** **hints** **benchmark** the predicted **morphology** **classes** (no new **furnace** **synthesis** report as the main claim).
## Findings

At a given density, multiple distinct phases can appear—consistent with experimental observations that mass density alone is insufficient as a descriptor. As density decreases, the authors trace transitions such as uniform versus bimodal pore-size distributions (at 1.15 and 0.50 g cm⁻³) and, at 0.16 g cm⁻³, agglomerated versus sparse motifs subdivided into “boxed” versus hollow fibrillar morphologies. Several predicted phases align with experimental hints from local density, pore statistics, and HRTEM, supporting DynReaxMas as a systematic way to classify amorphous carbonaceous structures and generate 3D models for interpretation.

**Comparisons, sensitivity, limitations (corpus).** Phases are **compared** to **HRTEM**/**porosity** **benchmarks** from the **literature**; **density** and **descriptor** **choice** are the main **levers**. PES **transformation** logs must be archived for **reproducibility** (see **Limitations** below).

## Limitations

The method’s cost and descriptor choices still bound how exhaustively phase space can be explored; transfer to every synthesis route or chemistry variant may need additional validation. Because **DynReaxMas** manipulates the **PES** during search, users must document **which** **transformations** were applied when comparing structures across runs—otherwise **reproducibility** across software versions can suffer. **Experimental** **glassy** **carbon** synthesis spans **precursor** **chemistry** and **furnace** **schedules** not uniquely determined by **mass** **density** targets alone. **DynReaxMas** outputs should be archived with **descriptor** **vectors** and **PES** **transformation** **logs** so independent groups can **replay** searches without guessing **hidden** **state**.

## Relevance to group

Demonstrates advanced ReaxFF-based sampling for disordered carbon morphologies—adjacent to reactive carbon chemistry and materials simulation themes in the corpus.

## Reader notes (navigation)

- [[reaxff-family]]
