---
id: paper:2019ponomarev-j-phys-chem-reactive-force
type: paper
title: "Reactive Force Field for Simulations of the Pyrolysis of Polysiloxanes into Silicon Oxycarbide Ceramics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - method:reaxff
  - task:parameterization
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.9b03810"
year: 2019
authors:
  - "Ilia Ponomarev"
  - "Adri C. T. van Duin"
  - "Peter Kroll"
venue: "J. Phys. Chem. C 123:16804-16812 (2019)"
pdf_sha256: "e6af92d9a7287a5e59ef1a77131bdc5b2e70694769246e4b9e89baaa81788599"
pdf_path: "papers/Ponomarev_JPCC_SiCO_2019.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019ponomarev-j-phys-chem-reactive-force -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A ReaxFF parameterization for Si–C–O–H is reported for silicon oxycarbide (SiCO) ceramics and polymer-pyrolysis routes to them. The force field is tested against thermochemical reference data and AIMD checks at elevated temperature, then applied to simulated polymer pyrolysis forming amorphous SiCO. Simulations align with experimental observations and provide structural insight into carbon-rich regions and graphene-like segregations embedded in an oxycarbide matrix.

## Methods

ReaxFF fitting to QM and experimental thermochemistry; validation against AIMD; large-scale pyrolysis MD from polysiloxane-like precursors.

## Findings

Good agreement on targeted thermochemical metrics; pyrolysis trajectories reproduce key observations and help interpret “free carbon” and glassy SiCO morphology at the atomistic level.


## Limitations

Carbon-rich polymer-derived ceramics span wide composition space; transferability outside the fitted chemistry should be validated case by case.

## Relevance to group

Combines UT Arlington / PSU collaboration on advanced ceramics and ReaxFF for Si–C–O–H, relevant to high-temperature materials and composite microstructures.

## Citations and evidence anchors

`papers/Ponomarev_JPCC_SiCO_2019.pdf` — abstract (validation and pyrolysis application). https://doi.org/10.1021/acs.jpcc.9b03810

## Related topics

- [[reaxff-family]]