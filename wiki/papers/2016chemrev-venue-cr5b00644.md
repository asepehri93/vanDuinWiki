---
id: paper:2016chemrev-venue-cr5b00644
type: paper
title: "Modeling molecular interactions in water: from pairwise to many-body potential energy functions"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:methods-software
  - task:review
  - method:classical-md
  - method:aimd
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemrev.5b00644"
year: 2016
authors:
  - "Gerardo Andrés Cisneros"
  - "Kjartan Thor Wikfeldt"
  - "Lars Ojamäe"
  - "Jibao Lu"
  - "Yao Xu"
  - "Hedieh Torabifard"
  - "Albert P. Bartók"
  - "Gábor Csányi"
  - "Valeria Molinero"
  - "Francesco Paesani"
venue: "Chem. Rev."
pdf_sha256: "6fc812873486e810b6a394dff8a129f47c028b71425d16ca509093efefe098a8"
pdf_path: "papers/Others/ChemRev_water_2016.pdf"
extraction_quality: good
group_affiliation: false
---

<!-- id:paper:2016chemrev-venue-cr5b00644 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **Chemical Reviews** article surveys **analytical potential energy functions** for **water**, organized around the **many-body expansion** of interaction energies. It contrasts **pairwise-additive** models with **implicit** and **explicit many-body** corrections, emphasizing how modern potentials that correctly encode **two- and three-body short-range terms** plus **long-ranged many-body polarization / coupling** can reproduce **gas- through condensed-phase** benchmarks from **high-level electronic structure** and **experiment**. The review is a methodological map for choosing **force fields vs. ab initio MD** when simulating **aqueous interfaces, solvation, and phase behavior**.

## Methods

Synthetic literature review (no new ReaxFF parameterization in this reference).

## Findings

- **Hierarchy of models** (pairwise → polarizable → explicit many-body) is tied to **accuracy vs. cost** trade-offs documented with extensive citations in the review.
- **Recent potentials** are argued to approach a **“universal”** water model class for broad thermodynamic and structural observables when many-body physics is treated consistently.

## Limitations

As a **review**, it does not substitute for **primary validation** on a user-specific electrolyte or interface composition.

## Relevance to group

Provides **external methodological context** for any **ReaxFF / classical / QM** simulation of **aqueous electrolytes, silica, and oxide interfaces** common in the group’s applied papers.

## Citations and evidence anchors

- Title page and TOC in `papers/Others/ChemRev_water_2016.pdf`; **DOI:** `10.1021/acs.chemrev.5b00644`.

## Related topics

- [[reaxff-family]]
