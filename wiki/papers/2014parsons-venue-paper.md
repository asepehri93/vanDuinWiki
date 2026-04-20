---
id: paper:2014parsons-venue-paper
type: paper
title: "Modeling of molecular nitrogen collisions and dissociation processes for direct simulation Monte Carlo"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4903782"
year: 2014
authors:
  - "Parsons, Neal"
  - "Levin, Deborah A."
  - "van Duin, Adri C. T."
  - "Zhu, Tong"
venue: "Journal of Chemical Physics"
pdf_sha256: "603e82b2bc83b8196b1a85514b17d0b32d16434f3b15fa6f4253fa4ccce4e5b8"
pdf_path: "papers/Parsons_N2_N2_JCP_2014.PDF"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2014parsons-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Hypersonic DSMC modeling needs reliable N₂–N₂ collision and dissociation cross sections under strong thermal nonequilibrium. The study generate a new potential energy surface via a ReaxFF fit to advanced ab initio data, then drive MD/quasi-classical trajectories (MD/QCT) to obtain reaction probabilities and total cross sections. The MD/QCT dissociation model shows more physically behaved nonequilibrium dissociation than a baseline total collision energy model and aligns with equilibrium rates and shock-tube references; total cross sections match established variable hard sphere forms (abstract; introduction opening, extract pages 1–2).

## Methods

ReaxFF-fitted PES; MD/QCT for N₂(¹Σg⁺)–N₂(¹Σg⁺) collisions targeting hypersonic shock conditions; comparison to DSMC chemistry models (abstract; introduction).

## Findings

Abstract states improved nonequilibrium behavior, good agreement with equilibrium kinetics and shock data, and VHS-consistent total cross sections.

## Limitations

Focus on nitrogen dimer chemistry only; broader air chemistry set still requires complementary models.

## Relevance to group

van Duin contribution on using ReaxFF as an ab initio bridge to gas-phase collisional data for aerospace DSMC partners at Penn State.

## Citations and evidence anchors

- J. Chem. Phys. 141, 234307 (2014); DOI `10.1063/1.4903782` (extract page 1).
- Abstract paragraph (extract page 1).

## Related topics

- [[reaxff-family]]
