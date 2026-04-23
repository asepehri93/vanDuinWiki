---
id: paper:2017smith-chemical-sci-ani-1-extensible
type: paper
title: "ANI-1: an extensible neural network potential with DFT accuracy at force field computational cost"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - method:ml-potential
  - method:dft-static
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:dft-static
  - keyword:qm-training-data
candidate_tags: []
source_refs: []
doi: "10.1039/C6SC05720A"
year: 2017
authors:
  - "Justin S. Smith"
  - "Olexandr Isayev"
  - "Adrian E. Roitberg"
venue: "Chemical Science 8, 3192–3203 (2017)"
pdf_sha256: "3a9eb5422eb89de2620fd5abbd7579a2e5b41298b9f99b167551a3c988a0eecf"
pdf_path: "papers/Others/Smith_Isayev_Roitberg_NN_CHO_ChemSci_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017smith-chemical-sci-ani-1-extensible -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **Chem. Sci.** (**DOI** in front matter). Training sizes and error metrics must match **Tables** in the article.

## Summary

**ANI-1** is a **neural network potential** built in the **ANAKIN-ME (ANI)** framework: atomic environments are encoded with **Behler–Parrinello**-type **symmetry functions** to produce **atomic environment vectors (AEVs)**, enabling learning across **conformational** space for **organic** molecules. The model targets **DFT** accuracy for **energies** (and **forces** via automatic differentiation in application) at cost far below repeated **DFT** evaluations, with emphasis on **extensibility** to additional elements and training corpora.

Training draws from **GDB**-class **organic** configurations; **normal mode sampling (NMS)** augments **conformational** diversity beyond minima-only datasets. Demonstrations include molecules **substantially larger** than any single training structure—up to **54 atoms** in showcased cases—testing **transferability** beyond the maximum training size.

## Methods

### 1 — MD application (atomistic dynamics)

**N/A** — the publication centers on **training** and **benchmarking** a **machine-learned potential**; production **molecular dynamics** with **ANI-1** is illustrated as an **application mode** (forces from automatic differentiation) but the indexed excerpt does not restate a canonical **timestep/thermostat** production protocol.

### 2 — “Force-field training” (ANI-1 supervised learning)

**ANI-1** is built in the **ANAKIN-ME (ANI)** framework: **Behler–Parrinello**-style **symmetry functions** feed **atomic environment vectors (AEVs)**, which in turn drive **atomic neural-network** contributions summed to a **system energy** (*Chem. Sci.* **8**, 3192–3203). Training uses **DFT-labeled** **C/H/N/O** organics drawn from **GDB**-class pools with up to **eight heavy atoms** per training structure; **normal mode sampling (NMS)** augments **conformational** coverage beyond minima-only sets.

### 3 — Static QM / DFT-only (reference data engine)

Reference **QM** data are **DFT** total energies (and, by implication, forces where differentiated) used for **supervised learning** of **ANI-1**. **Functional, basis set, dispersion corrections, and k-point** conventions for those reference calculations are **N/A** on the indexed excerpt—confirm against **Tables** and **Methods** in **`pdf_path`** before reproducing numerics.

### 4 — Review / non-simulation framing

**N/A** — primary **methods / performance** paper, not a literature review.

## Findings

### Outcomes and mechanisms

**ANI-1** reproduces **DFT-quality total energies** on held-out **CHNO** molecules within the training manifold, with **AEVs** providing a representation that generalizes across **conformational** degrees of freedom.

### Comparisons

Case studies include molecules **up to ~54 atoms**—**substantially larger** than any single **training** example—demonstrating **transfer** beyond the maximum **training** size cited in the abstract/indexed introduction.

### Sensitivity / design levers

**Training pool composition** (GDB subset + **NMS** augmentation) and **element coverage** (**C/H/N/O** only in **ANI-1**) control where the learned potential is trustworthy.

### Limitations, outlook, and corpus honesty

**Reactive** bond-topology exploration, **open-shell** chemistry, and **elements outside CHNO** require **retraining** or architectural extensions as discussed in the article conclusions. **RMSE**/**MAE** tables in *Chem. Sci.* are authoritative for quantitative claims—this wiki summarizes narrative only.

## Limitations

Coverage is limited to **CHNO** and **configurations** represented in training; **reactive** chemistry and **open-shell** species require **retraining** or different architectures. **ANI-1** is not a **reactive** **ReaxFF** substitute for **bond-topology** exploration without additional design.

For **pipeline** designers: **ANI** models pair naturally with **conformational** sampling for **organics** and **electrolyte** additives where **ReaxFF** is unnecessary or where **DFT** is too costly, but **electrode** **redox**, **SEI** chemistry, and **oxide** **dissolution** usually still point to **ReaxFF** or **QM** depending on **element** coverage.

## Relevance to group

Complements **ReaxFF**/**QM** workflows: MLIPs can sit between **DFT** accuracy and **classical FF** throughput for **organic**-phase simulations where **reactive** coverage is not required.

**ANI-1** also matters historically as an early widely cited demonstration that **symmetry-aware** machine learning can beat **hand-tuned** descriptors for **organic** **conformational** space—useful context when users ask how **NequIP**/**MACE**-class models relate to earlier **ANI** generations.

## Citations and evidence anchors

- DOI [10.1039/C6SC05720A](https://doi.org/10.1039/C6SC05720A).
- Excerpt alignment: `normalized/extracts/2017smith-chemical-sci-ani-1-extensible_p1-2.txt`.

## MAS / retrieval

`paper_keywords` includes **`keyword:qm-training-data`** because **ANI-1** is explicitly about **DFT**-derived corpora—important for disambiguating **machine-learning potential** questions from **ReaxFF** **parameterization** questions.

## Related topics

- [[reaxff-family]]
