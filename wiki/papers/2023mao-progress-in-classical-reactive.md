---
id: paper:2023mao-progress-in-classical-reactive
type: paper
title: "Classical and reactive molecular dynamics: Principles and applications in combustion and energy systems"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - method:classical-md
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reactive-md
  - keyword:combustion
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.pecs.2023.101084"
year: 2023
authors:
  - "Qian Mao"
  - "Muye Feng"
  - "Xi Zhuo Jiang"
  - "Yihua Ren"
  - "Kai H. Luo"
  - "Adri C. T. van Duin"
venue: "Prog. Energy Combust. Sci."
pdf_sha256: "1c808c0789f28cbd9af2c2041c82562e4a28b35fed005d64cb7571e1fb723f83"
pdf_path: "papers/Mao_ReaxFF_Combustion_review_ProgCombSci_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023mao-progress-in-classical-reactive -->

## Summary

Molecular dynamics has become a standard engineering-facing tool for predicting material properties and reactive flows when sufficient computational resources are available. Mao, Feng, Jiang, Ren, Luo, and van Duin review how classical and reactive MD are used in combustion and energy systems, spanning gas-, liquid-, and solid-fuel oxidation and pyrolysis, catalytic and heterogeneous combustion, electrochemistry, nanoparticle and flame synthesis, heat transfer, phase change, and nanoscale fluid phenomena. The article first presents MD methodology for nonreactive and reactive potentials, emphasizing ReaxFF development trained on quantum chemistry and/or experiments. It then discusses numerical methods, boundary conditions, post-processing, and computational cost, followed by selected application vignettes that illustrate how reactive MD exposes pathways and energetics in complex environments. The review explicitly frames MD’s expansion from fundamental science into engineering design loops enabled by petascale computing, while warning that predictive use still hinges on validated potentials and adequate sampling.

## Methods

### Review structure (D)

**Narrative** synthesis of **classical** and **reactive** MD for **combustion/energy**: **integrators**, **ensembles**, **timestep** selection, **thermostats/barostats**, **nonequilibrium** driving, **reaction-network** statistics.

### Reactive force fields (A)

**Bond-order** **ReaxFF**-style formalisms and **training** workflows at **textbook** level with pointers to **primary** parametrization studies.

### Boundary conditions and applications (B)

**Confined flows**, **interfaces**, **reactive walls** relevant to **energy** devices.

### Traceability rule

Any **specific** **numerical** claim requires the **cited** **primary** paper—not this review alone.

### 4 — Reviews, perspectives, non-simulation (primary genre)

**Literature** scope, **comparison** logic, and **vignette** **pointers** replace a single **simulation** table. For **reactive** and **classical** **MD** (LAMMPS-class engines, **NVT**/**NPT**/**NVE** choices, **0.25** **fs** order-of-magnitude for some **ReaxFF** work, **thermostats**/**barostats**, **PBC** in **condensed** phases, **K**-scale **temperatures** in **reactor**-like **phenomena**, **ns**-length **reactive** **trajectories** in **turbulent**-flame **surrogates**): the review **teaches** what **categories** to document but does **not** **fix** one **atom** count, one **kPa**/**GPa** **target**, or one **rare**-**event** **sampling** run—**N/A** in that **single-study** sense. **FF training** and **static** **QM** subsections in cited **primary** work must be read **per** **reference**; the review **synthesizes** **ReaxFF** **development** **concepts** without substituting a **de novo** training recipe here.

## Findings

### Capabilities highlighted (abstract themes)

**ReaxFF MD** used to map **pyrolysis/oxidation** pathways, **soot**/nanoparticle phenomena in **flames**, and **catalytic/interfacial** chemistry where **bond rearrangement** matters; **nanoscale** **flow/heat/phase** phenomena complement **continuum** models.

### Validation framing

Emphasizes **force-field error** and **sampling** limits as ongoing constraints.

### Pedagogical use

Useful as a **syllabus map**; **project** workflows still need **potential** validation against **target** chemistry.

The **Prog. Energy Combust. Sci.** scope statement (see **Introduction**) also situates **MD** within **petascale** **engineering** workflows: reactive simulations are increasingly used to **inform** **kinetic** **submodels** and **material** **selection**, but the review repeatedly cautions that **predictive** deployment still requires **validated** **potentials** and **sufficient** **sampling** of **rare** **events** in **heterogeneous** environments.

## Limitations

Breadth limits depth per application; quantitative conclusions must be traced to original studies. Force-field accuracy remains system dependent.

Readers should treat the **application vignettes** as **illustrative**: each cited **primary** study will specify **ensemble**, **boundary** **conditions**, and **validation** metrics that this **review** cannot reproduce in full without duplicating entire **bibliographies**.

## Relevance to group

Adri C. T. van Duin is a co-author; central reference for ReaxFF in combustion within the corpus.

## Citations and evidence anchors

- DOI: [10.1016/j.pecs.2023.101084](https://doi.org/10.1016/j.pecs.2023.101084)

## Related topics

- [[reaxff-family]]
