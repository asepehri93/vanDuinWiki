---
id: paper:2023li-venue-paper
type: paper
title: "Accurate Surface and Finite Temperature Bulk Properties of Lithium Metal at Large Scales using Machine Learning Interaction Potentials"
updated: "2026-04-22"
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
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2023li-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Lithium metal anodes** demand **accurate** **surface** **energetics** and **diffusion** **coefficients** across **facets** that **plating** and **stripping** expose, yet **ab initio molecular dynamics** is **expensive** for **large** **disordered** **grains**. This **arXiv:2305.06925v2** manuscript (**Phuthi**, **Yao**, **Batzner**, **Musaelian**, **Kozinsky**, **Cubuk**, **Viswanathan**) trains **machine learning interatomic potentials (MLIPs)** for **elemental Li** on **DFT** **labels**, then runs **large-cell** **MD** to extract **phonons**, **temperature-dependent elastic constants**, **bulk** **thermodynamics**, and **surface** **properties** such as **step** **energies** and **diffusion barriers** on **high-index** **facets**. The **abstract** highlights an **empirical Bell–Evans–Polanyi-style correlation** between **self-adsorption energies** and **minimum** **surface** **diffusion** **barriers**, linking **atomistic** **descriptors** to **morphology** debates in **Li** **metal** **batteries**.

## Methods

### Training data (C)

**DFT** snapshots for **bulk** distortions, **vacancies**, and **surface** slabs (**PBE**-class details in **arXiv** PDF).

### MLIP fitting (A)

**Equivariant neural** potentials fit to **energies/forces** (architecture in paper).

### Large-scale MD benchmarks (B)

**Phonons**, **elastic constants** (**finite displacement** / **stress–strain**); **surface** **adatom** diffusion sampled on **high-index** facets for **barrier distributions**.

The **arXiv** manuscript emphasizes **scalability**: once the **MLIP** matches **DFT** on **training** **manifolds**, **large** **disordered** **grain** **morphologies** become accessible for **finite-temperature** **sampling** of **facet-specific** **kinetics** that would be **prohibitively expensive** with **on-the-fly** **AIMD** at comparable **system** sizes.

## Findings

### Accuracy vs DFT

**MLIP** matches **DFT** within stated **tolerances** and enables **dynamics** beyond long **AIMD** feasibility.

### Descriptor trend

**Bell–Evans–Polanyi**-style link between **self-adsorption** energies and **minimum diffusion barriers** across facets.

### Scope limits

No **electrolyte**/**SEI** chemistry—**elemental Li** only.

### Corpus hygiene

Legacy **`2023li-*`** slug; cite **Phuthi et al.** **arXiv:2305.06925**.

**MAS note:** the **`doi`** field is empty in this stub because the corpus registers an **arXiv** preprint; if a **journal** **version** appears later, update **`doi`**, **`venue`**, and **`pdf_path`** in a controlled ingest without silently rewriting **`paper_id`**.

## Limitations

Generalization outside training distribution, switch to reactive environments (electrolyte, SEI chemistry), and explicit **kinetic pathways** for plating/stripping require separate models and validation.

## Relevance to group

The corpus stores this PDF under a legacy **`2023li-*` slug** while the extracted title/authors correspond to **Phuthi et al.**; kept for manifest linkage—scientific indexing should follow the **actual title** above, not the filename slug.

## Citations and evidence anchors

https://arxiv.org/abs/2305.06925 — Preprint landing page and PDF pagination for quotes.

## Related topics

- [[2023musaelian-nat-learning-local]]
