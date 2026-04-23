---
id: paper:2016yoon-venue-microsoft-word
type: paper
title: "Supporting information: ReaxFF short-range repulsion training for noble gas ion irradiation of graphene"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: null
year: 2016
authors:
  - "Kichul Yoon"
  - "Ali Rahnamoun"
  - "Jacob L. Swett"
  - "Vighter Iberi"
  - "David A. Cullen"
  - "Ivan V. Vlassiouk"
  - "Alex Belianinov"
  - "Xiahan Sang"
  - "Olga S. Ovchinnikova"
  - "Adam J. Rondinone"
  - "Raymond R. Unocic"
  - "Adri C. T. van Duin"
venue: null
pdf_sha256: "724a1acf490af3ba44dfe468756819eab959b497cdc73836ec8a740148e89a11"
pdf_path: "papers/Yoon_ACSNano_SI.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016yoon-venue-microsoft-word -->

!!! note "Supporting information PDF"

    This slug tracks the **ACS Nano SI** PDF (`papers/Yoon_ACSNano_SI.pdf`). The **peer-reviewed article** + **DOI** live on **`[[2016yoon-venue-nn6b03036]]`**.

## Summary

The **Supporting Information** for **Yoon *et al.*, *ACS Nano* 2016** documents how **short-range noble-gas-ion / carbon repulsion** was added to the **graphene** **ReaxFF** description used in the main irradiation study. **DFT** benchmarks use **benzene + noble-gas ion** clusters as a **planar aromatic proxy** for **graphene**, comparing energies to **ZBL** universal repulsion and to the fitted **ReaxFF** terms. **B3LYP** with **6-311G\*\*** bases is used for **He / Ne / Ar** complexes and **LACV3P\*\*** for **Kr** (stated in **§S1**). **Three impact sites**—**ring center**, **C–C bond center**, and **atop C**—anchor the training geometries referenced in **Figure S1**.

## Methods

**1 — MD application (production irradiation MD).** **§S1** of this **SI** focuses on **QM** training of **short-range ion–carbon repulsion**; the **LAMMPS** **ReaxFF** irradiation workflow is published in **`[[2016yoon-venue-nn6b03036]]`**. The following bullets summarize that **VOR** protocol so readers do not have to cross-open files for the headline **MD** controls: **Engine / code:** **LAMMPS** with **ReaxFF** (**C-2013-class** parameters plus the **SI** repulsion extension). **System size & composition:** periodic **graphene** supercells with in-plane footprint **~52 × 40 Å\(^2\)** plus **He\(^+\)**, **Ne\(^+\)**, **Ar\(^+\)**, or **Kr\(^+\)** projectiles; exact **atom** counts follow the **VOR** **Methods** text. **Boundaries / periodicity:** **in-plane periodic** graphene with **thermostatted** edge regions acting as heat baths. **Ensemble:** **NVE** during each impact cascade; **Nosé–Hoover** coupling on edge atoms between impacts. **Timestep:** **0.005–0.02 fs** during collisions. **Duration / stages:** high effective **dose** rates with **ps**-scale collision segments, followed by **25 ps** anneals at **1500 K** and longer **1.25 ns** anneals at **2000 K** for selected cases (**VOR**). **Thermostat:** **Nosé–Hoover** on edge regions. **Barostat / hydrostatic pressure control:** **N/A —** not **NPT**. **Temperature:** **300 K** pre-equilibration of the sheet; **1500 K**/**2000 K** post-irradiation anneals as quoted above. **Pressure:** **N/A —** no external stress target. **Electric field:** **N/A —** not applied. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training (ReaxFF ion–C repulsion).** **Goal:** augment the **C-2013-class** **ReaxFF** description so **high-energy noble-gas impacts** retain accurate **nuclear repulsion** without spoiling equilibrium **graphene** chemistry. **QM training data / training set:** **DFT** interaction energies for **noble-gas ion + benzene** clusters at the **B3LYP/6-311G\*\*** level (**LACV3P\*\*** for **Kr**), compared against **ZBL** **reference data** curves (**§S1**). **Geometry coverage:** **He**, **Ne**, **Ar**, and **Kr** ions approached at the **three** impact sites enumerated above. **Optimization:** iterative **ReaxFF** parameter adjustments to minimize disagreement with the **DFT/ZBL** training curves (details + parameter tables reside in the **SI PDF**).

**3 — Static QM beyond training scans.** **N/A —** **§S1** focuses on the **repulsive** training **surfaces** only.

**4 — Experiments.** **N/A —** **STEM**/**He-ion** comparisons live in the **main** article.
## Findings

**Outcomes / mechanism (parameter layer).** **Figure S1** documents that **DFT**, **ZBL**, and the updated **ReaxFF** **short-range** terms track each other for the **benzene + ion** **relative energy** curves at the three **impact sites** sampled.

**Comparisons.** Training explicitly **benchmarks** against **DFT** and **universal ZBL** repulsion rather than against experiment at this stage.

**Sensitivity / levers.** **Ion species** (**He/Ne/Ar/Kr**) and **approach site** (**ring**, **bond**, **atop**) shift the **repulsive** energy **surfaces** that the **ReaxFF** fit must reproduce.

**Limitations / outlook.** **Benzene** is a **proxy**; final **performance** must be judged in the **periodic graphene** cascades reported in **`[[2016yoon-venue-nn6b03036]]`**, where **electronic stopping** remains neglected.

**Corpus honesty.** This slug is **SI-only**; cite the **main** article for **DOI**, **dose**, **timestep**, **anneal**, and **experimental** comparisons.

## Limitations

- **SI fragment** — always pair with the **VOR** article page for **DOI**, **pagination**, and **experimental** comparisons.

## Relevance to group

Documents **PSU/ORNL** **ReaxFF** extension work underpinning **ion-engineered graphene defect** simulations in the corpus.

## Citations and evidence anchors

- Companion article: **`[[2016yoon-venue-nn6b03036]]`** (`papers/Yoon_ACSNano_2016.pdf`).
- SI PDF: `papers/Yoon_ACSNano_SI.pdf`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
