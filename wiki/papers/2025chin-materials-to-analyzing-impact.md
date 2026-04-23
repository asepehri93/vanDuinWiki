---
id: paper:2025chin-materials-to-analyzing-impact
type: paper
title: "Analyzing the impact of Se concentration during the molecular beam epitaxy deposition of 2D SnSe with atomistic-scale simulations and explainable machine learning"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:ml-atomistic
  - method:reaxff
  - task:experiment-integrated
  - material:widegap-semiconductor
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:machine-learning-potential
  - keyword:2d-materials
  - keyword:oxide-surface
  - keyword:lammps
  - keyword:berendsen-thermostat
  - keyword:nvt-simulation
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.mtadv.2025.100640"
year: 2025
authors:
  - "Jonathan R. Chin"
  - "Isaiah A. Moses"
  - "Mengyi Wang"
  - "Marshall B. Frye"
  - "Mingyu Yu"
  - "Nadire Nayir"
  - "Maria Hilse"
  - "Adri C. T. van Duin"
  - "Stephanie Law"
  - "Wesley Reinhart"
  - "Lauren M. Garten"
venue: "Mater. Today Adv. 28 (2025) 100640"
pdf_sha256: "5d09662f067f1533865f5de77253f8457c9a649347ae4ffbc6b2e20df19b0b94"
pdf_path: "papers/Chin_SnSe_Material_Today_Advances_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025chin-materials-to-analyzing-impact -->

## Summary

The study combines **molecular beam epitaxy (MBE)** growth of **SnSe** on **MgO(001)** with **RHEED**, **AFM**, **unsupervised ML** on images ( **ResNet50** embeddings + **PCA** / **NMF** ), and **ReaxFF MD in AMS** on **Se-covered MgO** to relate **Se:Sn flux ratio** and **deposition order** (**Se-first**, **Sn-first**, **co-deposition**) to **grain morphology** and **nucleation density**. **ReaxFF simulations** support a mechanism where **Se passivates under-coordinated surface oxygens**, suppressing **heterogeneous nucleation** relative to **Sn-first** conditions.

## Methods

- **MBE and characterization:** SnSe films grown under controlled **Se:Sn** flux ratios (**1.17:1** and **1.34:1** reported in the abstract statistics) and deposition sequences; **RHEED** tracks **\[010\]\(_\mathrm{SnSe}\) ∥ \[100\]\(_\mathrm{MgO}\)** epitaxy across conditions; **AFM** quantifies **grain step heights**, **number density**, and texture.
- **Machine learning:** **ResNet50** convolutional embeddings of **AFM** (and related) images projected with **PCA** (e.g., **PC1** vs deposition order, **PC5** vs flux ratio as described); **non-negative matrix factorization** and **synthetic visual counterfactuals** (optimization detailed in the methods sections) aid interpretability.
- **ReaxFF MD (AMS):** **Molecular dynamics** in **Amsterdam Modeling Suite (AMS)** with **reactive ReaxFF**; **Mg–Se** and **O–Se** terms adapted from prior work. **Supercell** **41.94 × 41.94 × 150 Å\(^3\)**, **18.87 Å**-thick **MgO(001)** **slab** + vacuum, **3D PBC** **periodic** in-plane. A **2 Å** **Se** adlayer (**400 Se** **atoms**) initializes **Se-first**; after minimization, **NVT** at **100 K** for **25 ps**, desorbed Se removed (**260 Se** remain), then **NPT** heating **100 → 1200 K** over **550 ps** (**0.002 K/fs**), ending near **T ≈ 1200 K** **temperature**. **Berendsen** **thermostats**: **100 fs** (MgO) and **10\(^7\) fs** (Se) damping. **0.25 fs** **timestep**. **NPT** **barostat** in the heating **stage** controls **1 bar**-class **pressure** in **z** as in the article. **N/A — electric field**; **N/A** — **umbrella sampling** / **metadynamics** in the segment summarized.
## Findings

- **RHEED:** **\[010\]\(_\mathrm{SnSe}\) ∥ \[100\]\(_\mathrm{MgO}\)** orientation persists across the conditions highlighted.
- **AFM + ML:** Higher **Se** (e.g., **1.34:1**) correlates with **thinner** grains; **Se-first** at **1.34:1** reduces **mean step height** by **~36%** to **~0.7 nm** versus the comparison called out in the abstract. **Grain number density** drops with **Se-first** by **~0%** and **~47%** at **1.17:1** and **1.34:1**, respectively (as stated).
- **ReaxFF:** **Se** adsorbs preferentially atop **surface O** sites at low **T**; upon heating, much **Se** desorbs (**~70%** fraction desorbed by **~900 K** in the profile shown), but **residual Se** is argued to **passivate** **under-coordinated O**, lowering **nucleation propensity** versus **Sn-first**, consistent with **fewer, larger** grains when **Se-first**.
## Limitations

- **ML embeddings** emphasize **texture** features; physical interpretability relies on **counterfactual** and **NMF** visualizations that are still **statistical** summaries of image appearance.
- **Simulations** use a **thin Se layer** on **MgO** rather than full **Sn + Se** co-deposition kinetics; **Sn** chemistry is inferred indirectly from **Se** passivation arguments.

## Relevance to group

Adri C. T. van Duin is a co-author; the project pairs **interpretable ML** with **AMS ReaxFF** for **2D chalcogenide** **MBE** on **oxides**.

## Citations and evidence anchors

- DOI: [10.1016/j.mtadv.2025.100640](https://doi.org/10.1016/j.mtadv.2025.100640)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
