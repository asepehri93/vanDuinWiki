---
id: paper:2023dhakane-carbon-trend-graph-dynamical
type: paper
title: "A Graph Dynamical neural network approach for decoding dynamical states in ferroelectrics"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:ml-atomistic
  - method:reaxff
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:reactive-md
  - keyword:lammps
  - keyword:machine-learning-potential
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1016/j.cartre.2023.100264"
year: 2023
authors:
  - "Abhijeet Dhakane"
  - "P. Ganesh"
venue: "Carbon Trends"
pdf_sha256: "9e969644e3faf7e6d30c071e07317e5dde146dcc4f9c745f7a3ea8788c12edb8"
pdf_path: "papers/Dhakane_Ganesh_CarbonTrends_GraphNN_BaTiO3_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023dhakane-carbon-trend-graph-dynamical -->


## Summary

Large-scale **reactive molecular dynamics** of pristine and oxygen-vacancy-containing **BaTiO₃** domain-wall dynamics uses a **ReaxFF** parameterization developed earlier by the authors (PCCP 2019 reference in the article). **Graph dynamical neural networks** (implemented with **PyTorch**) build **Koopman-matrix / Markov-state–style** models on local polarization features to resolve spatially and temporally heterogeneous dynamics, including how **isolated oxygen vacancies** create **defect dipoles** and slow both dipole relaxation and domain-wall motion. The paper’s contribution is therefore **two-layer**: (i) long **reactive trajectories** that retain bond-order chemistry with **charged defects**, and (ii) a learned **dynamical coarse-graining** that separates fast vs slow collective modes along **domain walls**. The ML stage is presented as an interpretability layer on top of the MD data, not a replacement for the reactive force field itself.

## Methods

### Reactive MD data generation (B)

- **Force field:** **ReaxFF** for **BaTiO\(_3\)** ferroelectricity with **oxygen vacancies**, using the authors’ prior parameterization (**PCCP 2019** reference in the article).
- **Scale:** ~**80,000-atom** cells with **pristine** and **defective** **domain-wall** configurations.
- **Observables:** **Bond-order** chemistry with **charged point defects**; **local polarization** fields resolved in space/time.

### Feature construction for ML

- **Order parameters:** **Local polarization vectors** label **bulk-like**, **domain-wall**, and **defect-adjacent** environments.

### Graph dynamical network + Markov modeling

- **Architecture:** **Graph dynamical network** adapted to **solid** **ferroelectric** order parameters; **Koopman-matrix** estimation yields **Markov state models** separating **fast** vs **slow** collective modes along **walls** and near **defects**.
- **Implementation:** **PyTorch** on **multi-GPU** nodes (details in *Carbon Trends* **Methods**).

### MD application (integrated)

**Engine / code:** **LAMMPS** with the authors’ **ReaxFF** for **BaTiO\(_3\)**. **System & composition:** order **tens of thousands of atoms** (**~80,000-atom** cells) with **pristine** and **O\(_v\)**-containing **domain-wall** **supercells**; full dimensions in the article. **3D PBC** **bulk** **ferroelectric** cells. **Ensemble, timestep, equilibration/production (ps/ns), thermostat (Nosé–Hoover-style controls), NVT vs NPT, target temperature in K, stress/pressure, electric bias to drive polarization, and rare-event (metadynamics/REX) usage:** in **Computational** section—**N/A — not listed numerically in this short wiki summary**; **N/A — industrial-scale electric field** biasing distinct from the **reactive** trajectories here unless the article adds it. **N/A — umbrella sampling** in the main story.

## Findings

### Oxygen vacancies

**Isolated vacancies** create **defect dipoles** and **~1–2 unit cell**-wide regions of **slow dipole relaxation**, **slowing** intrinsic **domain-wall** motion.

### Wall heterogeneity

**Rough**, **vacancy-influenced** walls exhibit **spatially varying** dynamics distinct from **mean** wall speeds.

### Relative timescales (order-of-magnitude)

**Domain walls** between **symmetry-related** domains can relax **~10× faster** than **bulk-like** regions, while **high-curvature** segments can be **~10× slower** than the **average** wall—suggesting **frequency-selective** excitation of wall segments as a design lever. **Comparisons** to **continuum/phase-field** and **experimental** time scales in the text are **qualitative** for this **MD+ML** workflow. **Limitations & outlook (as in the review posture of the work):** **eReaxFF** and the **Koopman** **graph** model inherit **ReaxFF** and **featurization** **uncertainties**; **open questions** include how **O\(_v\)**-rich **walls** couple to **MHz–GHz** **driving** in real **devices** beyond the **simulation** **window** described. **Corpus view:** this summary tracks the **VOR** **narrative**; **sensitivity** of the inferred **slow** **modes** to **temperature** and **vacancy** **concentration** is **tunable** in principle but should be re-read from the **primary** **figures** when reusing **numbers**.

## Limitations

ML analysis depends on the sufficiency of the reactive FF for BaTiO₃ under the simulated conditions; wall dynamics at experimental timescales may require complementary continuum or phase-field models. The graph/Koopman construction also depends on feature choices for **local polarization**; different featurizations could shift the inferred **slow modes** without changing the underlying trajectory data.

## Relevance to group

Combines **ReaxFF MD** with **graph-based dynamical coarse-graining** for defective ferroelectrics—an explicit **ML + reactive MD** workflow aligned with group interests in complex oxides.

## Citations and evidence anchors

- DOI: [10.1016/j.cartre.2023.100264](https://doi.org/10.1016/j.cartre.2023.100264)

## Related topics

- [[reaxff-family]]
- [[theme-ferroelectrics-polar-oxides]]
