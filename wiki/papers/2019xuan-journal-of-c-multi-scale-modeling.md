---
id: paper:2019xuan-journal-of-c-multi-scale-modeling
type: paper
title: "Multi-scale modeling of gas-phase reactions in metal-organic chemical vapor deposition growth of WSe₂"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - method:dft-static
  - method:continuum-or-mesoscale
  - task:application
  - material:tmd
  - scale:multiscale
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:reactive-md
  - keyword:validation-experiment
source_refs: []
doi: "10.1016/j.jcrysgro.2019.125247"
year: 2019
authors:
  - "Yuan Xuan"
  - "Abhishek Jain"
  - "Suhaib Zafar"
  - "Roghayyeh Lotfi"
  - "Nadire Nayir"
  - "Yuanxi Wang"
  - "Tanushree H. Choudhury"
  - "Samuel Wright"
  - "John Feraca"
  - "Leonard Rosenbaum"
  - "Joan M. Redwing"
  - "Vincent Crespi"
  - "Adri C. T. van Duin"
venue: "Journal of Crystal Growth (2019), 527, 125247"
pdf_sha256: "b681583b41fad1e592f62ddcc2f50ea6ac1b5d36a24d51761e96ac096fcf06ff"
pdf_path: "papers/Xuan_J_Cryst_growth_WSe2_multiscale.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019xuan-journal-of-c-multi-scale-modeling -->

## Summary

The paper builds a **multi-scale framework** for *gas-phase* chemistry in tungsten diselenide MOCVD from W(CO)\(_6\) and H\(_2\)Se precursors. DFT is used to propose reaction classes and to supply a training set to extend ReaxFF to W/H/C/O/Se. ReaxFF-based reactive MD in periodic gas-phase cells enumerates major pathways and barriers that are converted to Arrhenius form. Those kinetics, together with transport and thermodynamic property data, feed a detailed gas-phase mechanism in a **reacting-flow CFD** model of the cold-wall horizontal reactor, so predicted tungsten chalcogenide species fluxes to the growth zone can be compared to measured film-thickness trends across the wafer (surface growth itself is not resolved atomistically).

## Methods

The abstract stresses that **experimental** **MOCVD** chambers rarely provide **spatially resolved** **gas-phase** composition maps, motivating **simulation**. **QM/ReaxFF:** DFT calculations suggest reaction types and provide data to fit **ReaxFF**; ReaxFF simulations map **pathways** and **barriers**. **Kinetics:** compiled **Arrhenius** parameters and species **thermophysical** data enter the **CFD** model. **CFD:** solves **reacting flow** with **thermal** and **mass transport** for the **MOCVD** geometry used experimentally. **Validation** compares **gas-phase** concentrations of **tungsten chalcogenides** near the **substrate** to **experimental** measurements of **average film thickness** across the wafer. **Surface** growth steps are **not** resolved atomistically—the focus is **gas-phase** precursors feeding deposition.

**ReaxFF gas-phase MD (reaction enumeration).** The **DFT** training set and **ReaxFF** **molecular** **dynamics** are implemented in **LAMMPS**-class workflows (as stated in the **article**) using **periodic** **simulation** **boxes** for **gas-phase** **species**; **NVT**- or **NVE**-like **stages** (with a **Nose–Hoover**-type **thermostat** when **NVT** is used) run for **sufficient** **duration** to sample **reaction** **pathways** and **barrier**-like **events** feeding **Arrhenius** **fits**—**timestep** and **ns**-scale **trajectory** **lengths** are in the **Methods** (not all repeated here). **Barostat** for gas cells: **N/A** or **NPT**-like only if the article uses **variable** **volume** (confirm in PDF). **Electric field:** **N/A**. **Metadynamics / umbrella / replica exchange:** **N/A** for the **standard** **gas-phase** **ReaxFF** **leg** as summarized in the **abstract**.

**ReaxFF parameterization (FF training).** **Parent** **ReaxFF** is extended for **W/H/C/O/Se**; **DFT** **PBE**-class (or as stated) **reaction** and **cluster** data form the **training** **set**; **CMA-ES**/**genetic**-style **optimization** of **ReaxFF** **parameters** is described in the paper; **validation** uses both **QM** and **reactor** **thickness** **trends** as **reference** data.

## Findings

The coupled model reports that **predicted** **tungsten chalcogenide** fluxes near the growth surface **correlate** with measured **thickness** trends as a function of **position**, supporting the hypothesis that **film growth** is linked to **deposition** of these **gas-born** species. The authors position the workflow as **transferable** to other **CVD** chemistries and useful for **reactor** optimization and **reproducibility** across chambers. **Sensitivity** is to **inlet** flow, **heater** **layout**, and **chemistry** **completeness** in the **compiled** **mechanism**; **corpus honesty:** use the **J. Cryst. Growth** **PDF** for **figure**-level **validation** and any **uncorrected proof** sibling at **[[2019xuan-venue-paper]]** only for **ingest** notes.

## Limitations

**Reactor** geometry, **inlet** mixing, and **substrate** temperature boundary conditions feed directly into **CFD** **concentration** fields; any **multi-scale** coupling to **surface** **CVD** models must import those **gas-phase** fluxes as **boundary** data rather than assuming **uniform** precursor delivery. **Atomistic** **surface** reactions and **nucleation** on **WSe₂** are outside the paper’s explicit modeling scope. **CFD** predictions depend on **mechanism completeness** and **boundary conditions**; **experimental** diagnostics inside the chamber remain sparse. **Adri C. T. van Duin** co-authorship connects the work to corpus **ReaxFF** practice but does not guarantee parameter reuse without **retraining** checks for new chemistries.

**Confidence rationale:** `high`—primary journal article with detailed abstract.

## Reader notes (navigation)

- [[theme-2d-epitaxy-growth]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
