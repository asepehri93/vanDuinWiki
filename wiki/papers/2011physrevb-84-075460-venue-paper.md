---
id: paper:2011physrevb-84-075460-venue-paper
type: paper
title: "Reparameterization of the REBO-CHO potential for graphene oxide molecular dynamics simulations"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:2d-layered, material:graphene-carbon-nano, method:classical-md, task:parameterization, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.84.075460"
year: 2011
authors: ["Fonseca, Alexandre F.", "Lee, Geunsik", "Borders, Tammie L.", "Zhang, Hengji", "Kemper, Travis W.", "Shan, Tzu-Ray", "Sinnott, Susan B.", "Cho, Kyeongjae"]
venue: "Physical Review B"
pdf_sha256: "c249f461a3e1484ee4c9756c350c34131b67f28864c0f6af8ddaf920f7a0c8af"
pdf_path: "papers/Others/PhysRevB.84.075460.pdf"
extraction_quality: partial
group_affiliation: false
---

<!-- id:paper:2011physrevb-84-075460-venue-paper -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

This **Physical Review B** article modifies the **second-generation REBO-CHO** reactive empirical bond-order potential (carbon/hydrogen/oxygen) to better describe **graphene oxide (GO)**. Using **DFT** as reference data, the authors optimize parameters affecting **oxygen binding to graphene** and **C–O bond distances**, focusing changes on the **bond-order term** so prior REBO-CHO training for other uses is largely preserved. The introduction positions GO as technologically relevant (e.g., reduction routes to graphene, battery electrodes mentioned in context) and contrasts **REBO efficiency** with **ReaxFF/DFT** cost for large-scale GO simulations.

## Methods

- **Classical MD** with **REBO-CHO**, selectively **reparameterizing the bond-order component** against DFT energetics/structures for oxygen–graphene interactions.
- Benchmarking against DFT for binding energies, equilibrium C–O distances, and selected GO sample properties (per paper outline in extract).

## Findings

- Identifies shortcomings of the prior REBO-CHO parameterization for GO and proposes a bond-order-focused remedy aligned with DFT references in the excerpted introduction and methods outline.

## Limitations

- This is **REBO**, not ReaxFF; transferability across oxygen chemistries and defects should be validated case-by-case.
- Extract is **partial**; quantitative error tables and full GO test cases are not captured in pages 1–2 alone.

## Relevance to group

Useful cross-reference for **reactive carbon–oxygen classical potentials** and GO modeling choices adjacent to ReaxFF-centric workflows.

## Citations and evidence anchors

- Title page and Secs. I–II introduction: motivation, REBO vs ReaxFF discussion, GO focus (Phys. Rev. B 84, 075460; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
