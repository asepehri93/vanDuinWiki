---
id: paper:2024tigany-zarrouk-j-am-chem-so-experiment-driven-atomistic
type: paper
title: "Experiment-Driven Atomistic Materials Modeling: A Case Study Combining X-Ray Photoelectron Spectroscopy and Machine Learning Potentials to Infer the Structure of Oxygen-Rich Amorphous Carbon"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - domain:carbon-hydrocarbon
  - method:ml-potential
  - method:monte-carlo
  - task:method-development
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:dft-static
  - keyword:monte-carlo-sampling
  - keyword:validation-experiment
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/jacs.4c01897"
year: 2024
authors:
  - "Tigany Zarrouk"
  - "Rina Ibragimova"
  - "Albert P. Bartók"
  - "Miguel A. Caro"
venue: "J. Am. Chem. Soc."
pdf_sha256: "77492bfdc065943c17457cd7fe43d21d7c1e641b69f4a998f03dd83f127fc2da"
pdf_path: "papers/Others/experiment-driven-atomistic-materials-modeling-a-case-study-combining-x-ray-photoelectron-spectroscopy-and-machine.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024tigany-zarrouk-j-am-chem-so-experiment-driven-atomistic -->

!!! abstract "Scope"
    **Experiment-driven** structure generation: **grand-canonical Monte Carlo** with a **modified Hamiltonian** couples an **ML interatomic potential** and an **ML XPS model** (trained on **GW/DFT**) to build **oxygen-rich amorphous carbon (a-COₓ)** models that match **XPS** and stay **low in energy**.

## Summary

The authors address **atomistic structure determination** for **disordered** materials by **jointly** satisfying **experimental X-ray photoelectron spectroscopy (XPS)** and **DFT-level energetics**, instead of post hoc picking structures from generic MD/MC sampling. They introduce a workflow that combines **machine-learned potentials (MLPs)** with **ML-predicted XPS** (trained on **GW and DFT** references) inside **grand-canonical Monte Carlo** using a **modified Hamiltonian / generalized dynamics** formalism so that sampling **steers toward experimental observables** while remaining **chemically reasonable** (low energy). The **case study** is **oxygenated amorphous carbon**, **a-COₓ**, motivated by questions such as **how much oxygen** can be incorporated before decomposition to **CO/CO₂**, and by applications/tribology contexts noted in the introduction.

## Methods

**1 — MD application — N/A as primary** engine: the workflow centers on **sampling** driven by **MLIPs** and **ML XPS** inside **GCMC**, not a classical **production MD** run described in the short extract.

**2 — Force-field training / MLIP —** **ML** **interatomic** **potential** (**MLIP**) supplies **energies** and **forces**; **ML XPS** maps **atomic** **structure** to **spectra**; both trained on **DFT**/**GW**-level references per the **article** (see **PDF** for architecture and data volume).

**3 — Static QM / DFT (reference for ML).** **GW** and **DFT** data underpin **XPS** **training** and **energy** labels; the extract **stops** early in **XPS** **interpretation**—**N/A** for a full DFT **parameter** table on this page.

**4 — Sampling (grand-canonical Monte Carlo).** **GCMC** with a **modified Hamiltonian** (generalized-dynamics / sampling formalism) couples **ML** **energy** models and **ML XPS** so that drawn **a-CO\(_x\)** **configurations** track **XPS** while remaining **low** in **DFT**-consistent **energy** (abstract / §2). The paper contrasts this with “**generate** many **candidates** then **pick** **closest** to **experiment**” **pipelines** as **slow** and **not** **guaranteed**. The extract in-repo **ends** early in **XPS** **interpretation**; **move** **sets** and **full** **validation** are in the **PDF**.

## Findings

**Outcomes, comparisons, and generality (abstract / introduction).** **a-CO\(_x\)** **models** that **fit** **experimental** **XPS** while remaining **favorable** **vs** **DFT**-level **energetics** when using the **ML XPS** + **MLIP** **pair**. **Network**-based **XPS** **deconvolution** into **structural** **motifs** highlights **limits** of **standard** **peak** **assignment** and yields **atomic**-scale **insight** for **oxygenated** **amorphous** **carbon**. The **workflow** is framed as **portable** to **other** **experimental** **observables** beyond **XPS**.

**Corpus honesty** — see **`## Limitations`**; **RMSE**/**range** **numbers** require the **full** **JACS** **PDF**.
## Limitations

The checked-in extract is **short** relative to the full *JACS* paper; **numerical benchmarks** (RMSE on XPS, DFT energy windows, composition ranges) should be taken from the **PDF**. ML XPS and MLIPs inherit **data and functional** errors from their training sets.

## Relevance to group

This is **not** a van Duin-group paper; it is included as corpus context on **ML-driven structure inference** and **spectroscopy-informed sampling**, adjacent to broader **reactive MD / materials informatics** themes.

## Citations and evidence anchors

- DOI: [10.1021/jacs.4c01897](https://doi.org/10.1021/jacs.4c01897)

## Related topics

- [[graphene-nanocarbon]]
