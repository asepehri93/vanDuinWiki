---
id: paper:2018ashraf-fuel-235-201-pyrolysis-binary
type: paper
title: "Pyrolysis of binary fuel mixtures at supercritical conditions: A ReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2018.07.077"
year: 2018
authors:
  - "Chowdhury Ashraf"
  - "Sharmin Shabnam"
  - "Abhishek Jain"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Fuel 235 (2018) 194–207"
pdf_sha256: "f6e0cac3c7eb0cf6be258ea4e3431cf6f2b7fd1eb924ee23c9c11525e954c89d"
pdf_path: "papers/Ashraf_Shabnam_Fuel_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018ashraf-fuel-235-201-pyrolysis-binary -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Supercritical pressures in propulsion/combustion hardware invalidate low-P Arrhenius kinetic models that neglect pressure effects on pathways. This work uses ReaxFF MD to study **binary fuel pyrolysis** at supercritical conditions for JP-10/toluene and n-dodecane/toluene mixtures, comparing to detailed continuum chemistry where the continuum model fails to capture atomistic trends. Mixing ratio and density change cooperative decomposition: a more reactive component can accelerate breakdown of a less reactive partner beyond naive “fastest reaction dominates” intuition; pyrolysis products from one species can promote chemistry in others. The study maps regimes where first-order kinetics and simple Arrhenius behavior break down.

## Methods

- **ReaxFF MD:** High P/T reactive simulations of liquid fuel mixtures.
- **Reference:** Continuum reactor/kinetic modeling with detailed chemistry for contrast.

## Findings

- Mixture behavior is not governed only by the lowest activation-energy component; product distributions mediate cross-reactivity.
- Highlights when continuum kinetics miss pressure-dependent pathways accessible in atomistic simulation.


## Limitations

- Force-field uncertainty for large oxygenated product spaces; validation against experiment at matching P/T remains essential.

## Relevance to group

Application-forward **combustion/fuels + ReaxFF** paper for high-pressure pyrolysis of realistic mixtures.

## Citations and evidence anchors

- DOI: [10.1016/j.fuel.2018.07.077](https://doi.org/10.1016/j.fuel.2018.07.077)
- Abstract: `normalized/extracts/2018ashraf-fuel-235-201-pyrolysis-binary_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Supercritical fuel pyrolysis and mixture effects
- ReaxFF for hydrocarbon cracking at extreme conditions
