---
id: paper:2023roshan-venue-paper
type: paper
title: "Supporting Information: Optimization of ReaxFF Reactive Force Field Parameters for Cu/Si/O Systems via Neural Network Inversion (with application to copper oxide interaction with silicon)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - material:oxide
  - method:reaxff
  - method:ml-potential
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2023
authors:
  - "Kamyar Akbari Roshan"
  - "Mahdi Khajeh Talkhoncheh"
  - "Mert Yigit Sengul"
  - "David Jonathan Miller"
  - "Adri C. T. van Duin"
venue: "Supporting information PDF (corpus: Roshan_JPCC_CuSiO_2023_SI.pdf)"
pdf_sha256: "2143b19e62e9e29cb669413e8af52f5393b41ee8a9139a9319f7f9ed4d20975f"
pdf_path: "papers/Roshan_JPCC_CuSiO_2023_SI.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2023roshan-venue-paper -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

Supporting information for a **J. Phys. Chem. C**-class contribution on **data-driven optimization of Cu/Si/O ReaxFF parameters** via **neural network inversion**, applied to **copper oxide ↔ silicon** interfacial chemistry. The local extract chiefly tabulates **parameter sensitivity**, allowed ranges, and structured **Cu–O**/**O–Cu–O** term blocks—material typically accompanying the primary article’s force-field optimization narrative.

## Methods

Supplemental tables mapping ReaxFF parameter classes (bonds, off-diagonal terms, valence angles) to optimization bounds and sensitivities for **Cu/Si/O** training workflows using NN-guided inversion (see main article for equations and loss definition).

## Findings

Provides reproducibility detail for optimized parameter sets and sensitivity ranking—interpretation belongs with the main text’s validation against quantum or experimental reference data.

## Limitations

SI alone lacks the main manuscript’s motivating simulations and figures; treat as auxiliary tables only.

## Relevance to group

Documents **group methodology** connecting **ReaxFF fitting** to **modern ML inversion** tools for **oxide/metal** interfaces relevant to microelectronics and corrosion-style problems.

## Citations and evidence anchors

Locate the primary J. Phys. Chem. C article sharing this SI filename stem (`Roshan_JPCC_CuSiO_2023.pdf` if present in corpus) for DOI and pagination.

## Related topics

- [[reaxff-family]]
- [[2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based]]
