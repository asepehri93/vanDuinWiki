---
id: paper:2019rahnamoun-polymer-176-chemical-dynamics
type: paper
title: "Chemical dynamics characteristics of Kapton polyimide damaged by electron beam irradiation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:ereaxff
  - task:experiment-integrated
  - task:validation
  - material:polymer-organic
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:polymer
  - keyword:nve-simulation
  - keyword:validation-experiment
  - keyword:charge-equilibration
source_refs: []
doi: "10.1016/j.polymer.2019.05.035"
year: 2019
authors:
  - "Ali Rahnamoun"
  - "Daniel P. Engelhart"
  - "Sunita Humagain"
  - "Hilmar Koerner"
  - "Elena Plis"
  - "W. Joshua Kennedy"
  - "Russell Cooper"
  - "Steven G. Greenbaum"
  - "Ryan Hoffmann"
  - "Adri C. T. van Duin"
venue: "Polymer, 176 (2019) 135-145"
pdf_sha256: "02c1f2263512b96b37bfe4ff634e82d161ade880da087426183027175753aee7"
pdf_path: "papers/Rahnamound_Kapton_eBeam_Polymer2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019rahnamoun-polymer-176-chemical-dynamics -->

## Summary

Reactive molecular dynamics with a **polarizable ReaxFF** description is combined with experiments (IR, EPR, solid-state NMR, WAXD, SAXS, DMA) to study electron-beam damage in **PMDA–ODA (Kapton-H)** polyimide. The **Polymer** article (**2019**, **176**, **135–145**, **DOI** **10.1016/j.polymer.2019.05.035**) links **sequential** **energy** **deposition** segments meant to mimic **electron** **stopping** in **thin** **films** with **bond-level** **cleavage** **statistics**—especially **imide** **ring** **opening** and **cross-linking**—that **FTIR**/**EPR**/**NMR** **signatures** corroborate on **irradiated** **coupons**. The simulation protocol approximates energy deposition from keV-scale electron irradiation by **sequential “electron beam” segments** of charged dummy particles, followed by **microcanonical (NVE) relaxation**, and compares computed chemistry and mechanical response to measurements on pristine and irradiated films.


## Methods

**1 — MD application (polarizable eReaxFF, approximate e-beam).** **Engine:** **molecular dynamics** with **polarizable** **eReaxFF** for **PMDA–ODA (Kapton-H)** in **3D** **PBC** (as in the published **cell** setup). **System:** **Kapton** **slab** / **film** model of the size reported in the article (see **Polymer** for **atom** counts and **box**). **Ensemble:** **NVT** **equilibration** at **300 K** with a **thermostat** as stated, then **NVE** during **sequential** **“electron beam”** **deposition** and **post**-**exposure** **relaxation**; **0.1 fs**-class **timestep** is typical of **ReaxFF** in this work—**confirm** in **Methods**. **Beam model:** **strings of immobile dummy atoms** at **1 Å** spacing, **charge** **−1/0** **toggling**, **2 fs** “**on**” per site, **Coulomb**-coupled **energy** **transfer** **~21 eV** per **segment** (as in the article); **10 fs** **NVE** between **segments**; **0.5 ns** **NVE** after full **sequence** to follow **rearrangement**. **Barostat / NPT production:** **N/A** for the **NVE**-**dominant** **damage** **protocol** after equilibration. **Pressure** **control:** **N/A** in the **NVE** **stages** described. **External uniform E-field, shear, shock, umbrella / metadynamics:** **N/A**—the model uses **local** **Coulomb** **deposition** from **dummy** **charges**, not a **continuum** **E**-**field** **ramp** in the sense of **FF** **efield** **fixes**.

**2 — Force-field training.** Uses a **cited** **polarizable** **ReaxFF** **line** for **polymer** **chemistry**—**not** a full **de novo** **ReaxFF** **fit** reported as the **main** result of this **Polymer** paper.

**3 — Experiments (irradiation + multi-technique).** **90 keV** **e-beam** on **~76 µm** **Kapton** in **vacuum** (**~94.8 Gy/s**, **<10⁻⁶** **Torr** as stated). **FTIR**, **EPR**, **¹³C** **MAS** **NMR**, **WAXD**, **SAXS**, **DMA** track **imide** **loss**, **radicals**, **order**, and **mechanical** **softening** vs **computation** as in **Results**.

**4 — Static DFT as sole outcome.** **N/A.**
## Findings

**Outcomes / mechanisms.** **Damage** localizes in **imide** **motifs**; **cross**-**linking** **tracks** **higher** **Tg**-like **hardening** and **embrittlement** in **DMA**. **C–H** **cleavage** during **beam** **pulses** and **imide**-**ring** **transformations** afterward are prominent in **trajectory** **statistics**; **most** **scission** is **imide**-**centric** relative to **ether**/**carbonyl** paths in the **paper**’s **tally**. **eReaxFF** (polarizable) is used because **Coulomb**-mediated **deposition** **couples** to **evolving** **atomic** **charges**; **fixed**-**charge** **ReaxFF** is argued to be **inadequate** for **exothermic** **relaxation** after **pulses** in that **model**.

**Comparisons.** **FTIR** / **EPR** / **NMR** / **WAXD** / **SAXS** / **DMA** support **trends** in **chemistry** and **mechanics** in the way the **Results** table and figures claim.

**Sensitivity / design levers.** **Dose** and **time**-**in**-**the**-**MD**-**vs**-**expt** are **not** 1:1: **cumulative** **experimental** **dose** and **~ns** **MD** are **stated** **limitations** in the **authored** discussion.

**Limitations and outlook (as in the source).** The **beam** is a **Coulomb**-**heating** / **stopping**-inspired **approximation**, not **ab initio** **radiolysis**. Extrapolating to **space**-**relevant** **dose** **histories** requires the **caveats** in the **article**.

## Relevance to group

Demonstrates **polarizable ReaxFF** workflows for **polymer radiolysis** with **multi-technique experimental validation** (van Duin co-author).

## Citations and evidence anchors

DOI: [10.1016/j.polymer.2019.05.035](https://doi.org/10.1016/j.polymer.2019.05.035)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
