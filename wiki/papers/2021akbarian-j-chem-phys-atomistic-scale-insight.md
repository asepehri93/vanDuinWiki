---
id: paper:2021akbarian-j-chem-phys-atomistic-scale-insight
type: paper
title: "Atomistic-scale insight into the polyethylene electrical breakdown: An eReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:ereaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/5.0033645"
year: 2021
authors:
  - "Dooman Akbarian"
  - "Karthik Ganeshan"
  - "W. H. Hunter Woodward"
  - "Jonathan Moore"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys. 154:024904 (2021)"
pdf_sha256: "632c88d5b7e60ec90b5cbc17b824924a25b6bcc4b5449a1f783514b3252ae1d2"
pdf_path: "papers/Akbarian_JCP_2020_eReaxFF.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2021akbarian-j-chem-phys-atomistic-scale-insight -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

An **eReaxFF** (explicit electron) MD framework, checked against DFT references in the paper, probes time-dependent dielectric breakdown in polyethylene, including effects of density, voids, and XLPE-related by-products such as acetophenone. Higher PE density increases time-to-breakdown in the simulations; adding electron-affine byproducts like acetophenone can shorten TDDB. During breakdown, electron transport localizes through void channels between electrodes; the acetophenone radical anion strongly shifts secondary reaction energetics versus neutral acetophenone.

## Methods

eReaxFF molecular dynamics with explicit electronic degrees of freedom as formulated in their eReaxFF line; scenarios varying morphology and additives.

## Findings

Atomistic picture tying microstructure and impurities to breakdown statistics and pathway; qualitative insights on percolation through void space and role of charged radical species.

## Limitations

System sizes and timescales remain below real cable insulation; eReaxFF approximations apply.

## Relevance to group

Shows group direction on polarizable/explicit-electron extensions of ReaxFF for dielectric polymers—adjacent to high-voltage materials and electronics applications.

## Citations and evidence anchors

`papers/Akbarian_JCP_2020_eReaxFF.pdf` — abstract (TDDB trends, void paths, acetophenone). https://doi.org/10.1063/5.0033645

## Related topics

- [[2021itai-leven-j-chem-theor-recent-advances]]
- [[reaxff-family]]
