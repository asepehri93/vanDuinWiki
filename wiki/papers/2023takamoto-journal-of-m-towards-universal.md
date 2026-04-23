---
id: paper:2023takamoto-journal-of-m-towards-universal
type: paper
title: "Towards universal neural network interatomic potential"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - method:ml-potential
  - task:application
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:aimd
  - keyword:dft-static
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1016/j.jmat.2022.12.007"
year: 2023
authors:
  - "So Takamoto"
  - "Daisuke Okanohara"
  - "Qing-Jie Li"
  - "Ju Li"
venue: "J. Materiomics"
pdf_sha256: "3d9c6cd0730104a19bfdef533e496a5e5eb468a1da6a8d0b9bab5cbd59438cdb"
pdf_path: "papers/ReaxFF_others/TeaNet_2023_J_Materionomics.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023takamoto-journal-of-m-towards-universal -->

## Summary

The opening uses an analogy to **Newton’s** gravitational law to motivate the idea that a **learned** \(U(\mathbf{r})\) could enable predictive **MD** across chemistry if it were **accurate** and **fast** enough. Takamoto et al. write a **J. Materiomics** perspective on **universal neural network interatomic potentials (NNIPs)**—models that aim to approximate the **potential energy surface** \(U(\mathbf{r}_1,\ldots,\mathbf{r}_N)\) with **chemical accuracy** (~**1 kcal mol⁻¹**) across elements—positioned against **wavefunction methods**, **DFT**, and **classical** empirical potentials. The opening frames **DFT** as a **second-generation** “universal” approach whose **O(N³)** scaling limits **ab initio MD** to short times and modest sizes, while **NNIPs** trained on **DFT** data promise **faster** energies/forces for larger systems if **dataset coverage** and **extrapolation** risks are managed.

## Methods

### Perspective genre (D)

**Expository** survey of **universal NNIPs**: **architecture** concepts, **DFT** training corpora, **MD** integration—**not** a **ReaxFF** fit or single **benchmark** study.

### Referenced implementations

**TeaNet**-class ideas referenced conceptually (`TeaNet_2023_J_Materionomics.pdf` in `papers/`).

**Dataset and coverage language (perspective).** The article discusses how **universal** potentials hinge on **broad** **DFT** databases that span **chemistries** and **configurations**, and why **out-of-distribution** failures remain common when **elements** or **coordination** environments are absent from training. For **MD** integration, the perspective stresses **energy/force** consistency, **symmetry** preservation, and **long-time** **stability**—criteria that must be checked alongside raw **meV/atom** errors on static snapshots.

**N/A (owned LAMMPS / ReaxFF in this *J. Materiomics* perspective).** This **expository** paper does not publish a **reproducible** LAMMPS **NVT**/**NPT** **RMD** recipe, **timestep**, **E-field** **RMD**, or **metadynamics** setup; **N/A** for a **ReaxFF** **parametrization** (block 2) or a **new** static **DFT** dataset (block 3). **Numbers** and **architectures** are **cited** from the **NNIP** literature, not **owned** as a **single** **benchmark** **study** in this file.

## Findings

### Accuracy/cost framing

Discusses ~**1 kcal mol\(^{-1}\)** targets vs **barrier**/**thermo** reliability; **NNIPs** can extend **size/time** vs **AIMD** with **OOD** failure risks.

### Relation to empirical potentials

Contrasts **classical** empirical models with **NNIPs** on **transferability** and **coverage**.

### Complementarity with ReaxFF

Positions **MLIPs** and **ReaxFF** in different **accuracy/cost** regimes for **reactive** large-scale work.

### GNN benchmark note

Cites **meV/atom**-level errors for some **GNN** models on covered chemistries vs broader **universal** QM coverage trade-offs.

## Limitations

Downstream **hybrid** workflows in this corpus may pair **NNIPs** with **ReaxFF** in different regimes: **NNIPs** for **local** **QM fidelity** on small **active** regions and **ReaxFF** for **reactive** **large-cell** dynamics where **ML** coverage is insufficient—choices must be justified per system. **No single architecture** is validated end-to-end in the excerpt alone; performance depends on **training data** and **architecture** choices discussed in the full text and cited literature. Relationship to **van Duin** group work is **indirect** (file lives under `ReaxFF_others` as **MLIP** context).

**Confidence rationale:** `med`—perspective paper; faithful high-level summary.

## Reader notes (navigation)

For **Phase 5** **retrieval**, tag this paper under **MLIP** **keywords** separately from **ReaxFF** **lineage** pages to reduce **false positives** on **reactive** **combustion** queries.

- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
