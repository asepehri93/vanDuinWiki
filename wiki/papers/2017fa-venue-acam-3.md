---
id: paper:2017fa-venue-acam-3
type: paper
title: "Pyrolysis simulations of Fugu coal by large-scale ReaxFF molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors:
  - "Mingjie Gao"
  - "Xiaoxia Li"
  - "Mo Zheng"
  - "Li Guo"
venue: "2017 International Conference on Coal Science & Technology / 2017 Australia-China Symposium on Energy (Beijing)"
pdf_sha256: "1b581faf2757ffbe8e3ae499c140f4f0a39c9e2e2fab4f71b6d38d6f0582e945"
pdf_path: "papers/ReaxFF_others/Chinese_Coal_Abstracts/Pyrolysis simulations of Fugu Coal by Largr-scale ReaxFF molecular dynamics.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017fa-venue-acam-3 -->

## Evidence and attribution

!!! note "Authority of statements"

    This page summarizes the **conference abstract PDF** in `pdf_path` (2017 International Conference on Coal Science & Technology / Australia–China Symposium on Energy). It is **not** a full journal article; numerical claims track the abstract text.

## Summary

**Pyrolysis** is the first chemical step in most **coal conversion** routes and strongly influences downstream processes. The abstract describes **isothermal ReaxFF molecular dynamics** on a **multi-component Fugu sub-bituminous coal** model with **23,898 atoms** to study **pyrolysis properties**. Simulations run **2.0 ns** from **1200–2200 K** and **250 ps** at **2400 K** and **2600 K**. Products are **lumped** by **carbon number** into **char**, **heavy tar**, **light tar**, and **gas**. The authors report that simulated **product profiles vs temperature** follow **experimental trends**, with **total gas yield** in **fair agreement** with literature values despite differing temperature windows. **Time evolution** analysis suggests **high-temperature, short-duration** runs can **roughly reproduce** distributions that would require **much longer time** at lower temperatures. **VARxMD** (a C++ visualization/analysis tool for reactive MD) parses **detailed reaction pathways**. Keywords listed: **coal pyrolysis**, **multi-component structure model**, **product evolution**, **reaction mechanism**, **ReaxFF MD**.

## Methods

**1 — MD application (atomistic dynamics).** **Engine / code:** **GPU-enabled ReaxFF MD** in **GMD-Reax** (cited in the conference PDF). **System:** **multi-component Fugu sub-bituminous coal** model **C\(_{11995}\)H\(_{10363}\)N\(_{159}\)O\(_{1366}\)S\(_{15}\)** totaling **23,898 atoms** in a cubic cell (**indexed extract**). **Sampling protocol:** **isothermal ReaxFF MD** for **2.0 ns** each at **1200, 1400, 1600, 1800, 2000, and 2200 K**, plus shorter **250 ps** runs at **2400 K** and **2600 K** to probe the **elevated-temperature acceleration** strategy. **Ensemble:** **NVT** with **periodic boundary conditions in all directions** of the cubic box. **Timestep:** **0.25 fs** in the indexed §2.2 text (the same paragraph’s “**0.25 ps**” unit is treated as a **typo** in the source—confirm against the PDF if ambiguous). **Thermostat:** **Berendsen** with **0.1 ps** damping constant. **Cutoffs:** bond-order threshold **0.3** and nonbonded cutoff **10 Å** as stated in §2.2. **Post-processing:** **VARxMD** for reaction mining and product classification. **Barostat / pressure:** **N/A —** **NVT** at unspecified volume; no **NPT** or stress control reported. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used (standard **NVT** reactive MD).

**2 — Force-field training.** **N/A —** the indexed pages describe **application** of **ReaxFF** to a constructed coal model, not a new QM refit in this file.

**3 — Static QM / DFT-only.** **N/A —** **DFT** is not the production engine for the pyrolysis trajectories summarized here.

## Findings

**Outcomes / mechanisms.** **Temperature-dependent** evolution of **char / heavy tar / light tar / gas** lumps (carbon-number rules as in the authors’ prior work) shows radical-driven chemistry consistent with the **ReaxFF coal** literature cited in the introduction.

**Comparisons.** Normalized **tar + gas** trends vs **fluidized-bed pyrolysis experiments** (figure referenced in the extract) are described as agreeing on **trend**; **total gas yield** from simulation is reported in **fair agreement** with literature experiments **despite different temperature windows**.

**Sensitivity / design levers.** The authors compare **long lower-T** runs vs **short higher-T** runs to argue that **high-T** simulations can **approximately reproduce** product partitioning that would take **much longer** at lower **temperature**.

**Limitations / outlook (as authored).** Model construction details are deferred (“**will be reported elsewhere**” in the extract); quantitative agreement is framed cautiously given **temperature-window** mismatch.

**Corpus / PDF honesty.** Grounded in the **conference PDF** and `normalized/extracts/2017fa-venue-acam-3_p1-2.txt`; there is **no DOI** in front matter—treat as **non-journal** grey literature.

## Limitations

**Conference abstract** only—no **peer-reviewed DOI**, and **extraction** may omit figures/tables from a longer manuscript. **ReaxFF** parameters for this **coal** model require verification against the **group’s archived parameter tables**. **Reactor-scale** extrapolation is not claimed.

## Relevance to group

Illustrates **VARxMD + large-system ReaxFF** coal pyrolysis workflows represented in the corpus **Chinese Coal Abstracts** folder—useful as a **pointer** to methodology talks even without a journal DOI.

## Citations and evidence anchors

- No DOI; `papers/ReaxFF_others/Chinese_Coal_Abstracts/Pyrolysis simulations of Fugu Coal by Largr-scale ReaxFF molecular dynamics.pdf`; extract `normalized/extracts/2017fa-venue-acam-3_p1-2.txt`.

## Related topics

- [[reaxff-family]]
