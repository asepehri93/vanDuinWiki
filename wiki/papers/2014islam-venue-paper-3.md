---
id: paper:2014islam-venue-paper-3
type: paper
title: "ReaxFF molecular dynamics simulations on lithiated sulfur cathode materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - material:sulfur-cathode
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:monte-carlo-sampling
  - keyword:galley-or-proof-pdf
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
pdf_sha256: "bc69d058e11c175d5ddfdd3b1b485a5af8746a67ad2ab176d835fb2e97272f8d"
pdf_path: "papers/Islam_PCCP_LiS_JustAccepted.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2014islam-venue-paper-3 -->

Accepted-manuscript PDF for the PCCP Li–S ReaxFF study: parameter development plus MD, GCMC, and genetic-algorithm phase-diagram tools for lithiated sulfur cathode mechanics.

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the RSC **Accepted Manuscript** text in the ingested PDF. For pagination, proofs, and the final PCCP layout, prefer the **version-of-record** article.

## Summary

Introduces a ReaxFF parametrization for Li–S interactions and applies it to amorphous lithiated sulfur (a-LiₓS) to connect lithiation with mechanical moduli and strengths, Li/S diffusion coefficients versus loading, GCMC-based open-circuit voltage trends, and a genetic-algorithm-assisted Li–S phase diagram survey—framed for sulfur cathode mechanics in Li–S batteries (abstract; extract). The study targets the mechanical response of the sulfur cathode as it converts among lithiated amorphous states, a problem distinct from ideal crystalline Li₂S benchmarks because discharge products in real cells are often disordered and compositionally graded.

## Methods

According to the accepted-manuscript abstract (extract page 1), the workflow comprises five coupled tasks: development of a ReaxFF potential for Li–S interactions; molecular dynamics on amorphous lithiated sulfur (a-LiₓS) to extract elastic moduli and strengths as a function of lithiation; evaluation of Li and S diffusion coefficients across Li loading; grand canonical Monte Carlo sampling to construct an open-circuit voltage profile during discharge; and genetic-algorithm exploration of the Li–S binary phase diagram. Detailed simulation cells, thermostats, and GCMC chemical potentials appear in the full article. The ReaxFF development step necessarily couples to quantum training sets for Li–S clusters and condensed phases referenced in the PCCP paper, while MD segments must span the elastic sampling window long enough to estimate moduli on disordered cells.

### 1 — MD application (a-LiₓS)

- **Engine / code / cell sizes / timestep / thermostat / barostat:** **N/A — not stated on the indexed extract for this accepted-manuscript PDF**; use **`[[2014islam-physical-che-reaxff-molecular]]`** + **`papers/Islam_PCCP_LiS_2014.pdf`** for version-of-record Methods detail.
- **System size & composition:** **Amorphous lithiated sulfur** (**a-LiₓS**) **supercells** across **Li** loadings per the **abstract**; **exact atom counts** are **N/A — not on extract p1–2**.
- **Boundaries / periodicity:** **3D PBC** is the usual bulk model for **a-LiₓS** **MD** in this article class; **N/A — explicit PBC statement not on extract p1–2**.
- **Ensemble:** **N/A — not on extract p1–2** (VOR Methods).
- **Duration / stages (equilibration vs production):** **N/A — not on extract p1–2** (VOR Methods).
- **Temperature:** **N/A — explicit thermostat/set-point table not on extract p1–2** (VOR Methods).
- **Hydrostatic pressure / barostat:** **N/A — pressure control not on extract p1–2** (confirm NVT vs NPT in VOR PDF).
- **Electric field:** **N/A — not indicated** in the abstract workflow summarized here.
- **Replica / enhanced sampling (MD):** **N/A — not indicated** in the abstract-level summary; **GCMC** is a separate electrochemical sampling tool in this study.

### 2 — Force-field training (Li–S)

- **Training problem:** new **ReaxFF** terms for **Li–S** interactions trained with **DFT** reference data as described in **PCCP**; **N/A — QM level-of-theory tables not on extract p1–2** (article/SI).

### 3 — GCMC and genetic-algorithm phase diagram

- **GCMC** for **open-circuit voltage** during **discharge** and **genetic-algorithm** exploration of the **Li–S binary phase diagram** as stated in the **abstract** (extract page 1); **N/A — statistical-mechanics settings not on extract p1–2**.

## Findings

The abstract reports non-monotonic mechanical strengthening with lithium content, concentration-dependent Li and S diffusivities, a GCMC-derived open-circuit voltage curve, and a genetic-algorithm-assembled phase diagram intended to connect atomistic structure with Li–S cathode mechanics and electrochemistry (extract page 1). For edited figures and final pagination, prefer the version-of-record page [[2014islam-physical-che-reaxff-molecular]]. Together, the electrochemical and mechanical outputs are presented as mutually consistent checks on the same reactive Hamiltonian for lithiated sulfur.

## Limitations

Ingested PDF is an **accepted manuscript** with placeholder DOI metadata in some headers; **final DOI** is `10.1039/c4cp04532g` as on the published article page [[2014islam-physical-che-reaxff-molecular]].

## Reader notes (navigation)

Canonical curated page for the final article PDF: [[2014islam-physical-che-reaxff-molecular]] (`papers/Islam_PCCP_LiS_2014.pdf`).

## Citations and evidence anchors

- Final DOI `10.1039/c4cp04532g` (sibling page front matter).
- Accepted-manuscript abstract (extract page 1).

## Related topics

- [[2014islam-physical-che-reaxff-molecular]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
