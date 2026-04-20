---
id: paper:2016dyilmaz-venue-paper
type: paper
title: "Investigating structure–property relations of poly(p-phenylene terephthalamide) fibers via reactive molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2016
authors:
  - "Dündar E. Yilmaz"
  - "Nebahat Bulut"
venue: "Preprint / institutional manuscript (see PDF)"
pdf_sha256: "e1ee05134713e2eaf6b0e3040833fdc1603fab0c945f1d96568533436b809fa2"
pdf_path: "papers/ReaxFF_others/dyilmaz.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2016dyilmaz-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Reactive MD with ReaxFF** is applied to **poly(p-phenylene terephthalamide) (PPTA, Kevlar-class)** fiber models with varying **radius**, **crystallinity**, and **core–shell** arrangements. **Quasi-static tensile deformation** up to **~15% strain** is used to extract **Young’s moduli** and to follow how **crystalline vs. disordered** fractions and **domain boundaries** control **failure initiation**. The study introduce an **order parameter** based on the **cross-sectional area fraction** of crystalline domains to rationalize modulus trends in **core–shell** geometries.

## Methods

- **ReaxFF MD** of constructed **PPTA fiber** supercells with **tensile strain increments**.
- Post-processing of **stress–strain** behavior and **chain scission** locations.

## Findings

- Reported moduli are **~226 GPa (disordered)** vs **~311 GPa (crystalline)** in the abstract’s numerical examples.
- **Core–shell** moduli scale approximately **linearly** with the crystalline area fraction according to the proposed order parameter.
- **Failure** begins at **domain boundaries** separating ordered regions.

## Limitations

- **DOI not recorded** in normalized metadata; treat bibliographic details as **manuscript-stage** until reconciled with a published version.
- **Strain rate / system size** effects typical of MD mechanics studies apply.

## Relevance to group

Demonstrates **ReaxFF uptake in aramid fiber mechanics** adjacent to the group’s broader **reactive polymer / composite** interests (even though Penn State authors are not listed on this PDF).

## Citations and evidence anchors

- Abstract and introduction in `papers/ReaxFF_others/dyilmaz.pdf` (dated **Feb 3, 2016** in the extract).

## Related topics

- [[reaxff-family]]
