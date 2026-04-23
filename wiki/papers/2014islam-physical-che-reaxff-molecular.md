---
id: paper:2014islam-physical-che-reaxff-molecular
type: paper
title: "ReaxFF molecular dynamics simulations on lithiated sulfur cathode materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:sulfur-cathode
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/c4cp04532g"
year: 2014
authors:
  - "Islam, Md Mahbubul"
  - "Ostadhossein, Alireza"
  - "Borodin, Oleg"
  - "Yeates, A. Todd"
  - "Tipton, William W."
  - "Hennig, Richard G."
  - "Kumar, Nitin"
  - "van Duin, Adri C. T."
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "2d41456bb91442675e451b81a994f8366567f12421c47c845e1bdd7ce2a09cb7"
pdf_path: "papers/Islam_PCCP_LiS_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014islam-physical-che-reaxff-molecular -->

!!! note "NON_PRIMARY sibling"

    The corpus also ingests a **proof** PDF under **`2014islam-venue-rsc-cp`**. This entry (**`Islam_PCCP_LiS_2014.pdf`**) is the **version-of-record**-aligned article PDF for the same DOI per [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section **D**.

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **PCCP** article identified by `doi`, `title`, and `pdf_path`, starting from the **abstract** in `normalized/extracts/2014islam-physical-che-reaxff-molecular_p1-2.txt`.

## Summary

Islam *et al.* develop a **ReaxFF interatomic potential** for **Li–S** interactions and apply it to **molecular dynamics** of **amorphous lithiated sulfur (a-Li\(_x\)S)**, motivated by **Li–S battery** cathodes where **sulfur** offers very high theoretical capacity but suffers from **volume change**, **polysulfide dissolution**, and coupled **mechanical** and **transport** challenges. The study addresses a gap noted in the introduction: extensive **electrochemical** characterization exists, but **mechanical properties** of **lithiated sulfur** phases are comparatively under-characterized at the **atomistic** level. The authors compute how **ultimate strength**, **yield strength**, and **Young’s modulus** evolve with **lithiation**, reporting **nonlinear strengthening** with **Li** content. They further compute **diffusion coefficients** for **Li** and **S** across **Li** loadings, construct an **open-circuit voltage** profile during discharge using a **grand canonical Monte Carlo (GCMC)** scheme, and compile a **Li–S binary phase diagram** using **genetic algorithm**-based tools described in the article.

## Methods

### Force-field training (Li–S ReaxFF)

- New **ReaxFF** interaction terms for **Li–S** (and associated cross terms needed for condensed phases) are fit to **QM** reference data enumerated in the **PCCP** article; the abstract stresses addressing a gap in **atomistic mechanical** characterization of **lithiated sulfur**.

### Reactive MD on amorphous lithiated sulfur

- **MD** samples **a-Li\(_x\)S** cells to compute **stress–strain** responses and extract **mechanical moduli** (**ultimate strength**, **yield**, **Young’s modulus**) as functions of **lithiation**.
- **Diffusion:** trajectories yield **Li** and **S** **diffusion coefficients** vs **Li** content to connect atomic transport with rate limitations.

### Open-circuit voltage and phase diagrams

- **Grand canonical Monte Carlo (GCMC)** is used to construct **open-circuit voltage** profiles along a model **discharge** pathway.
- A **genetic-algorithm**-based workflow assembles the **Li–S binary phase diagram** referenced in the abstract.

### Integration / numerical settings

- **Ensemble, timestep, thermostat, electrostatic cutoffs, and cell sizes** are specified in **PCCP** Methods/**ESI**; **N/A — not recoverable from `normalized/extracts/2014islam-physical-che-reaxff-molecular_p1-2.txt` alone**—use `papers/Islam_PCCP_LiS_2014.pdf`.

### 1 — MD application (a-Li\(_x\)S)

- **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** as described in **PCCP**; **N/A — LAMMPS/other executable string not on indexed extract** (standard for this lineage—confirm in PDF).
- **System size & composition:** **Amorphous lithiated sulfur** (**a-Li\(_x\)S**) **supercells** spanning **Li** loadings studied for **stress–strain** and **diffusion** (**abstract**); **exact atom counts** are **N/A — not on extract p1–2** (article).
- **Boundaries / periodicity:** **3D PBC** is the standard framing for bulk **a-Li\(_x\)S** cells in this study class; **N/A — explicit PBC wording not on extract p1–2** (confirm in PDF).
- **Ensemble:** **N/A — ensemble (NVT vs NPT) not stated on extract p1–2** (Methods).
- **Timestep / duration / stages / thermostat:** **N/A — not stated on extract p1–2** (Methods/ESI).
- **Barostat / hydrostatic pressure control:** **N/A — not stated on extract p1–2** (use article; if strictly **NVT**, pressure regulation is not central).
- **Temperature:** **N/A — explicit simulation temperature set points not on extract p1–2** (Methods).
- **Electric field:** **N/A — not indicated** in the abstract-level summary used here.
- **Replica / enhanced sampling (MD):** **N/A — not indicated** for the **MD** segments in the abstract-level summary; **GCMC** is used separately for **OCV** construction (see below).

### 2 — Force-field training (Li–S ReaxFF)

- **Parent FF / elements:** new **Li–S** (and coupled) **ReaxFF** terms extending the reactive Hamiltonian for **lithiated sulfur** phases (**abstract**).
- **QM reference / training set / optimizer:** enumerated against **DFT** references in the article; **N/A — functional/basis/k-point tables not on extract p1–2** (Methods/ESI).
- **External reference data:** **DFT** training benchmarks as cited in **PCCP** (full tables in article/SI).

### 3 — Grand canonical Monte Carlo and phase-diagram exploration

- **GCMC** constructs **open-circuit voltage** profiles along a model **discharge** pathway (**abstract**).
- A **genetic-algorithm**-based workflow assembles the **Li–S binary phase diagram** referenced in the **abstract** (article Methods).

## Findings

- **Mechanical response:** strength metrics **improve** with increasing **Li** content, but the improvement is **not linear** with **lithiation**, indicating complex **structure–property** coupling in the **amorphous** matrix.
- **Transport:** **Li** and **S** **diffusivities** vary with **Li** loading, informing rate limitations in **lithiated sulfur** phases.
- **Voltage:** **GCMC**-derived **OCV** profiles provide a **thermodynamic** window for discharge behavior alongside the **MD** structural narrative.
- **Phase space:** the **binary phase diagram** compilation contextualizes **two-phase** vs **single-phase** regions relevant to **cathode** design.
- The authors position these simulation outputs as **fundamental** inputs for interpreting **morphological** degradation and **mechanical failure** in **Li–S** cathodes, while noting broader battery challenges (**polysulfide** shuttling, **electronic conductivity**) that lie outside the reactive force-field scope.

## Limitations

**Amorphous** models simplify composite **cathode** microstructures; **ReaxFF** cannot replace detailed **QM** for all **redox** energetics.

## Relevance to group

**van Duin** senior author on **Li–S** **ReaxFF** with multi-institution collaboration (ARL/AFRL/Cornell/Sandia network in affiliations).

## Citations and evidence anchors

- DOI `10.1039/c4cp04532g` (abstract and ESI notice in extract page 1).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
