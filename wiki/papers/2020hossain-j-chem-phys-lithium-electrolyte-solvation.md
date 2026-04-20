---
id: paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation
type: paper
title: "Lithium-electrolyte solvation and reaction in the electrolyte of a lithium ion battery: A ReaxFF reactive force field study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/5.0003333"
year: 2020
authors:
  - "Md Jamil Hossain"
  - "Gorakh Pawar"
  - "Boryann Liaw"
  - "Kevin L. Gering"
  - "Eric J. Dufek"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys. 152, 184301 (2020)"
pdf_sha256: "231221cee087887ad21069d25969689ef4e9868cd8d1eaa27af75711e788734b"
pdf_path: "papers/Hossain_JCP_2020_EC_Li.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2020hossain-j-chem-phys-lithium-electrolyte-solvation -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This JCP paper extends ReaxFF to **organic carbonate electrolyte** species (e.g., EC, EMC, VC) and LiPF6-related chemistry so that Li solvation, solvent exchange, and decomposition pathways near reducing anode conditions can be studied reactively. DFT data on Li-associated initiation reactions and solvation structures augment the training set; the parametrization introduces distinct treatments so that **Li⁺** and **neutral Li** can reproduce similar solvation energetics while differing in chemical reactivity—neutral Li drives electrolyte decomposition, modeled with a Monte Carlo-style charge/state update compatible with ReaxFF dynamics. Decomposition barriers depend on EC coordination number around neutral Li.

## Methods

- **ReaxFF training:** Fit to DFT energies/reaction energetics for electrolyte fragments, Li⁺/Li0 solvation, and decomposition precursors.
- **Reactive sampling:** Protocol to reduce Li⁺ to Li⁰ within MD to trigger decomposition sequences.

## Findings

- Force field distinguishes Li atom vs Li⁺ behavior needed for anode-side electrolyte reduction scenarios.
- Demonstrates sensitivity of decomposition barriers to local solvation shell structure.


## Limitations

- Complex commercial electrolyte mixtures and long-time SEI evolution require careful interpretation; parameter transfer should be checked when moving to new salts or additives.

## Relevance to group

Central reference for **Li-ion electrolyte reactivity** with ReaxFF at PSU/INL collaboration—connects to SEI formation narratives in the battery literature.

## Citations and evidence anchors

- DOI: [10.1063/5.0003333](https://doi.org/10.1063/5.0003333)
- Abstract: `normalized/extracts/2020hossain-j-chem-phys-lithium-electrolyte-solvation_p1-2.txt`

## Reader notes (navigation)

- Pairs with **solid electrolyte** parameterization ([[2018shin-physical-che-development-reaxff]]) to show **two regimes**: ceramic lattice transport vs **organic** bond chemistry at the anode.  
- **Theme:** [[batteries-interfaces-reaxff]]; **workflow:** [[reaxff-parameterization-workflow]].  
- **Frozen eval:** FF2, BAT1 in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
- Carbonate electrolytes, Li⁰ vs Li⁺ chemistry, and anode-side decomposition
- ReaxFF parameterization for organics containing Li, P, F
