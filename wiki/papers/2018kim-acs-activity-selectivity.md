---
id: paper:2018kim-acs-activity-selectivity
type: paper
title: "Activity, Selectivity, and Durability of Ruthenium Nanoparticle Catalysts for Ammonia Synthesis by Reactive Molecular Dynamics Simulation: The Size Effect"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reactive-md
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.8b05070"
year: 2018
authors:
  - "Sung-Yup Kim"
  - "Hong Woo Lee"
  - "Sung Jin Pai"
  - "Sang Soo Han"
venue: "ACS Appl. Mater. Interfaces 2018, 10, 26188–26194"
pdf_sha256: "ec5bf6a861ccb3a40d2f37371dd6f6b5d39a46b419ffd80ad0fad9f9559134c5"
pdf_path: "papers/ReaxFF_others/Kim_Han_Ru_NH3)ACI_AMI_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018kim-acs-activity-selectivity -->

## Summary

Develops a **ReaxFF** parameterization for the **Ru–N–H** ternary system (trained against **DFT** data summarized in the paper and **SI**), then uses **LAMMPS** **ReaxFF MD** to study **NH₃ formation** from **N₂** and **H₂** over **Ru nanoparticles** (diameters **3–10 nm**). The study reports **size-dependent** patterns in **activity**, **selectivity**, and **mechanical durability** metrics derived from **surface-site** distributions and **stress** measures. The introduction recalls that **NH₃** synthesis remains difficult because **N₂** is strongly triple-bonded, that industrial **Haber–Bosch** conditions are hot and pressurized, and that **Ru**, **Os**, and **Fe** rank highly on volcano-style activity plots—with **Ru** often outperforming **Fe** in both theory and experiment. The authors motivate **ReaxFF MD** as a route to **durability** and **selectivity** metrics that are hard to reach from static **DFT** alone because of system size and time-scale limits.

## Methods

- **Force field:** **ReaxFF** parameters for **Ru–N–H** optimized with a **successive one-parameter search** against **first-principles** training sets (equations of state, **surface energies**, **adsorption** and **reaction pathways**, bond dissociations); parameter tables referenced in **Table S4** (**SI**).
- **MD:** **LAMMPS**; **Verlet** integration with **0.5 fs** timestep; **NVT** at **1500 K** with a **Nosé–Hoover** thermostat (**damping 0.01 fs⁻¹**); **N₂/H₂** pressures explored in **300–1000 atm** as described in the article; spherical **Ru NP** on a **Ru slab** support model (see Fig. 1). The abstract states simulations **predict activities, selectivities, and durabilities** jointly and discuss **temperature and pressure** effects alongside **size**.

**Additional controls.** **PBC:** **three-dimensional PBC** for the **supported NP** supercells. **Barostat:** **N/A — NPT** not used for the summarized **constant-volume** **NVT** production. **Gas pressure:** **300–1000 atm** **N₂/H₂** ratios set **gas** **density** in the fixed **simulation** cell rather than via fluctuating volume. **Electric field:** **N/A — bias** not applied. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not reported. **Equilibration / production lengths** in **ps**/**ns**—see **`pdf_path`**/**SI** for full staging.

## Findings

**Outcomes.** **NH₃** **formation** **activity** peaks near **4 nm** **Ru** **particles** in the explored grid, while **10 nm** particles show the strongest **selectivity** among reported cases; **hcp/fcc/top** **site** populations shift with **size** and help rationalize **reactivity**.

**Comparisons.** Results are discussed relative to **Haber–Bosch** **literature** and **volcano** trends for **Ru**/**Fe** catalysts, with explicit caveats about the elevated **1500 K** **acceleration** strategy.

**Sensitivity.** **H₂ pressure** raises **selectivity** more steeply than **N₂ pressure** in the scanned window; **mean stress** vs **stress concentration** trades off with **diameter**, yielding **5 nm** as the best **durability** compromise in the study.

**Limitations and PDF grounding.** High **temperature**/**pressure** **MD** is a **kinetic accelerator**, not a literal industrial reactor replica—see article **barrier** checks. All quantitative tables: **`pdf_path`**.
## Limitations

- Operating conditions (**1500 K**, high **gas pressures**) are chosen to **accelerate** chemistry in MD and are **not** direct **Haber–Bosch** process replicas; the paper discusses **barrier** checks to motivate the elevated temperature approach.

## Relevance to group

Illustrates **ReaxFF training** from **DFT** plus **large-scale** **catalytic** **MD** on **metal NPs**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acsami.8b05070](https://doi.org/10.1021/acsami.8b05070)

## Related topics

- [[reaxff-family]]
