---
id: paper:2018berman-nat-operando-tribochemical
type: paper
title: "Operando tribochemical formation of onion-like carbon leads to macroscale superlubricity"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:2d-layered
  - method:reaxff
  - task:experiment-integrated
  - domain:reactive-md
paper_keywords:
  - keyword:tribology
  - keyword:reaxff-application
  - keyword:validation-experiment
  - keyword:2d-materials
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1038/s41467-018-03549-6"
year: 2018
authors:
  - "Diana Berman"
  - "Badri Narayanan"
  - "Mathew J. Cherukara"
  - "Subramanian K. R. S. Sankaranarayanan"
  - "Ali Erdemir"
  - "Alexander Zinovev"
  - "Anirudha V. Sumant"
venue: "Nature Communications 9, 1164 (2018)"
pdf_sha256: "13594f39fe8e752eabdeda81fa318d184ecfc8253f73097c2b258768e09ecc0f"
pdf_path: "papers/ReaxFF_others/Berman_Narayanan_Carbon_MoS2_NatureComm_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018berman-nat-operando-tribochemical -->

Experiments on hydrogenated DLC sliding on MoS₂ with nanodiamond in dry N₂ are paired with ReaxFF MD and DFT to show sulfur-driven amorphization of nanodiamond into onion-like carbon that supports macroscale superlubricity.

## Summary

Combined **experiments** and **reactive molecular dynamics** show **tribochemical** evolution of **hydrogenated DLC (H-DLC)** slid against **2D MoS₂** with **nanodiamond** in **dry nitrogen**: **sulfur** from dissociated **MoS₂** drives **amorphization** of **nanodiamond** and formation of **onion-like carbon (OLC)** in the contact, enabling **macroscale superlubricity** through reduced **real contact** and **incommensurate** interface structure. The study is motivated by superlubricity regimes where third-body carbon chemistry and 2D sulfide decomposition co-determine interface composition, not by DLC or MoS₂ alone.

## Methods

From the article PDF (`pdf_path`).

- **Experiments:** **Dry** **N2** tribology with **H-DLC** on **MoS2** **2D** material plus **nanodiamond** third body; **operando** surface analysis (instrumentation in the article and **Methods** there).
- **Reactive MD (ReaxFF):** **C / Mo / S** interactions use **ReaxFF** parameters from **Mattsson et al.** (as cited). **S-doped** **nanodiamond** models (**~3 nm** diameter, **7200 C** atoms) with **1-15%** **S** substitution; initial **Maxwell** velocities at **2000 K**; **canonical RMD** in **LAMMPS** with **0.25 fs** timestep and **Nose-Hoover** thermostat (**2000 K** segment **1 ns**, then cool **2000 K** to **300 K** over **2 ns** as stated). Supercells use **three-dimensional periodic boundary conditions** as in the published setup. **Barostat:** **N/A —** the quoted heating/cooling trajectory is **NVT**-style **canonical** **RMD** without a **Parrinello–Rahman** hydrostatic **barostat**; separate **MoS₂** contact models that quote **~1 GPa** **stress** are described in **Supplementary** figures and should be read there for any **pressure** coupling details.
- **DFT (VASP):** **PBE** **PAW** calculations for substitutional defect energetics (**520 eV** cutoff, **Gamma-centered 6x6x6 k-mesh**, **64-atom** diamond supercell) as described under **Density functional theory** in the article.

**Correspondence to experiment:** **Dry N₂** **tribometry** with **H-DLC**/**MoS₂**/**nanodiamond** contacts is paired with **operando** surface probes in the article so **macroscopic** **friction** trends can be read alongside **evolving** **carbon**/**sulfur** chemistry inferred from **simulation** and **spectroscopy**.

## Findings

- **Tribochemical** reactions occur even under **dry**, **additive-free** conditions when **H-DLC**, **MoS₂**, and **nanodiamond** co-participate in the contact.
- Simulations support that **S** transport from **MoS₂** contributes to **nanodiamond amorphization** and subsequent **OLC** formation.
- **In situ OLC** is argued to reduce **contact area** and promote **incommensurate** sliding against **H-DLC**, consistent with measured **superlubricity**.
- Experimental **operando** characterization in the article ties macroscopic friction reduction to evolving surface carbon phases; the MD portion supplies an atomistic sulfur-mediated amorphization pathway consistent with those observations.

## Limitations

- Transferability to **liquid-lubricated** or different **DLC** chemistries requires separate validation.
- Reactive MD at 2000 K explores sulfur-driven amorphization kinetics that are far from room-temperature tribology; quantitative timescales therefore require careful mapping back to experimentally relevant contact temperatures and shear rates discussed in the Nature Communications article.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
