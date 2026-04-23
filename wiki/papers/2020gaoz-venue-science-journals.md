---
id: paper:2020gaoz-venue-science-journals
type: paper
title: "Graphene reinforced carbon fibers"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - method:classical-md
  - task:experiment-integrated
  - material:graphene-carbon-nano
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:polymer
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1126/sciadv.aaz4191"
year: 2020
authors:
  - "Zan Gao"
  - "Jiadeng Zhu"
  - "Siavash Rajabpour"
  - "Kaushik Joshi"
  - "Małgorzata Kowalik"
  - "Brendan Croom"
  - "Yosyp Schwab"
  - "Liwen Zhang"
  - "Clifton Bumgardner"
  - "Kenneth R. Brown"
  - "Diana Burden"
  - "James William Klett"
  - "Adri C. T. van Duin"
  - "Leonid V. Zhigilei"
  - "Xiaodong Li"
venue: "Sci. Adv."
pdf_sha256: "17c764a50db859c577e6ab0664a079ca84ba90c4a2ddcb1cd15622a8fe64a86b"
pdf_path: "papers/GaoZ_Science_Advances_2020_graphene_reinforcement.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020gaoz-venue-science-journals -->

## Summary

**Polyacrylonitrile (PAN)** dominates industrial **carbon fiber** production, yet **tensile strength** and **modulus** remain limited by **voids**, **misorientation**, and **defect** chemistry during **oxidative stabilization** and **high-temperature carbonization**. **Gao** et al. report **Science Advances** experiments showing that embedding only **0.075 wt% graphene** in PAN precursor fibers increases **tensile strength** by roughly **225%** and **Young’s modulus** by roughly **184%** relative to **neat PAN** controls under matched processing. **Adri C. T. van Duin** joins a collaboration that couples those measurements to **ReaxFF** reactive simulations of **PAN-derived** chemistry near **graphene** and to **large-scale molecular dynamics** workflows (including **Zhigilei**-group methodologies referenced in the paper) that resolve **porosity** and **orientation** evolution. The **article** frames **trace graphene** primarily as a **microstructure-directing** additive during **pyrolytic** **conversion**, not as a **continuous** **load path** that would dominate **mechanics** by **volume** **fraction** alone.

## Methods

Precursor **PAN/graphene** fibers are fabricated and subjected to **stabilization** and **carbonization** ramps documented in Methods; **single-fiber** mechanical tests extract **strength** and **modulus**. **Microscopy** and **spectroscopy** quantify **void** content, **turbostratic** versus **graphitic** order, and **preferred orientation** of carbon layers. On the simulation side, **ReaxFF** **reactive molecular dynamics** in **LAMMPS**-class workflows captures **bond-breaking** and **cross-linking** chemistry as **PAN** converts near **graphene** edges and basal planes, with **amorphous** / **slab**-like supercells of **O(10^3–10^4) atoms** (as reported). **PBC** enclose the reactive cells where the manuscript uses bulk-like models. **NVT** or **NPT** **ensemble** usage follows the published stages; **N/A —** exact **NPT** barostat and **GPa**-level **pressure** if only **NVT** windows are used for a given step—see PDF. **Timestep** in **femtoseconds** and **production** **duration** in **ns** or long **ps** are given in the article/SI. A **thermostat** (e.g. **Nosé–Hoover**-style) is used for temperature control to target **K**-scale **temperature** ramps. **N/A — electric field**; **N/A — umbrella** / **metadynamics** in the main narrative unless SI states otherwise. **Hydrostatic pressure** control: **N/A** when **NVT** only.

## Findings

The **0.075 wt%** additive produces **macroscopic** gains far larger than a simple **rule-of-mixtures** estimate, implicating **microstructural** control rather than graphene acting only as a rigid inclusion. **ReaxFF** and **MD** narratives tie graphene to **templated graphitic domains**, **reduced nanovoids**, and **enhanced chain alignment** during pyrolysis—mechanisms consistent with the measured **strength** and **modulus** boosts. The work positions **trace graphene** as a processing aid that steers **carbonization microstructure** more than it increases bulk density alone. Experimental sections document fiber processing windows, imaging of voids and orientation, and statistical treatment of mechanical tests; simulation sections should be read alongside those micrographs to avoid over-interpreting any single reactive trajectory as representative of full furnace gradients. Correlative **SEM**/**TEM** and **spectroscopy** in the article illustrate how **graphene** templates **turbostratic** **graphitic** **domains** while **suppressing** **micron-scale voids** that otherwise nucleate during **PAN** **densification**, giving a structural rationale for simultaneous **strength** and **modulus** gains that exceed simple **composite** **averaging**.

## Limitations

Industrial translation requires cost and batch reproducibility studies; atomistic models simplify full fiber texture and furnace gradients.

## Relevance to group

**van Duin-group** **ReaxFF** on **PAN carbonization** with **graphene additives**, paired with **experimental** mechanical data.

## Citations and evidence anchors

- DOI: [10.1126/sciadv.aaz4191](https://doi.org/10.1126/sciadv.aaz4191)

## Related topics

- [[reaxff-family]]
