---
id: paper:2023li-venue-paper
type: paper
title: "Accurate Surface and Finite Temperature Bulk Properties of Lithium Metal at Large Scales using Machine Learning Interaction Potentials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:ml-atomistic
  - material:li-metal-anode
  - method:ml-potential
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2023
authors:
  - "Mgcini Keith Phuthi"
  - "Archie Mingze Yao"
  - "Simon Batzner"
  - "Albert Musaelian"
  - "Boris Kozinsky"
  - "Ekin Dogus Cubuk"
  - "Venkatasubramanian Viswanathan"
venue: "arXiv:2305.06925v2 (22 May 2023); corpus PDF Others/Li_metal_NN_2023.pdf"
pdf_sha256: "e2839bb59367e3945b8edf83e8b03693275e249a5bb75b54b6e1b58f0cc5b646"
pdf_path: "papers/Others/Li_metal_NN_2023.pdf"
extraction_quality: partial
group_affiliation: false
---

<!-- id:paper:2023li-venue-paper -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This manuscript trains **machine learning interatomic potentials (MLIPs)** for **elemental lithium** on **DFT** labels and uses them to reach **large-scale** MD covering **thermodynamics**, **phonons**, **temperature-dependent elastic constants**, and **surface** properties argued to be cumbersome for direct **AIMD** at comparable cost. A highlighted empirical observation in the abstract is a **Bell–Evans–Polanyi-style relation** linking **self-adsorption energies** to **minimum surface diffusion barriers** on **high Miller-index** facets—motivated by **lithium metal anode** morphology and dendrite debates where **surface transport** coefficients matter.

## Methods

DFT dataset construction; MLIP training; large-cell MD for bulk and surface observables; comparison to DFT/Experiment where cited in the paper.

## Findings

Reports **state-of-the-art fidelity** for multiple Li properties within the study’s benchmark set; emphasizes practical access to **surface** behaviors at scales beyond routine AIMD (per abstract framing).


## Limitations

Generalization outside training distribution, switch to reactive environments (electrolyte, SEI chemistry), and explicit **kinetic pathways** for plating/stripping require separate models and validation.

## Relevance to group

The corpus stores this PDF under a legacy **`2023li-*` slug** while the extracted title/authors correspond to **Phuthi et al.**; kept for manifest linkage—scientific indexing should follow the **actual title** above, not the filename slug.

## Citations and evidence anchors

https://arxiv.org/abs/2305.06925 — Preprint landing page and PDF pagination for quotes.

## Related topics

- [[2023musaelian-nat-learning-local]]