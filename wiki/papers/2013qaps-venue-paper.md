---
id: paper:2013qaps-venue-paper
type: paper
title: "Computational modeling of structure and OH-anion diffusion in quaternary ammonium polysulfone hydroxide – Polymer electrolyte for application in electrochemical devices"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:classical-md
  - material:polymer-organic
  - task:application
  - scale:atomistic
  - domain:methods-software
candidate_tags: []
source_refs: []
doi: "10.1016/j.memsci.2012.12.010"
year: 2013
authors:
  - "Merinov, Boris V."
  - "Goddard, William A., III"
venue: "Journal of Membrane Science"
pdf_sha256: "ab24968fe6d08ad62c2b817f9ea91103abfd671167c21cded18f08c9ea22833a"
pdf_path: "papers/Others/QAPS_OH_JMS-2013.pdf"
extraction_quality: partial
group_affiliation: false
---

<!-- id:paper:2013qaps-venue-paper -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Classical molecular dynamics predicts microstructure and hydroxide transport in quaternary ammonium polysulfone hydroxide (QAPS-OH) alkaline membranes, dry and with ~14 wt% water. The model describes hydrophobic backbone with interconnected hydrophilic channels hosting mobile OH⁻; computed diffusion coefficients and activation energies are compared to experiment, with discussion of diffusion mechanisms (abstract; introduction; journal header, extract).

## Methods

Amorphous membrane construction (Cerius2 Amorphous Builder / Monte Carlo build protocol referenced), MD over temperature for QAPS-OH with and without water uptake (section “Simulation details”, extract).

## Findings

The abstract reports three-dimensional interconnected hydrophilic channels, OH⁻ residing in channels, and MD-derived diffusion coefficients and activation energies consistent with available experimental data, with qualitative mechanism discussion.


## Limitations

Normalized `extraction_quality` is partial (publisher cover page occupies part of the extract). Force field and water model details beyond the first pages are not visible in the p1–2 extract.

## Relevance to group

Alkaline polymer electrolytes adjacent to battery/fuel-cell interface topics in the broader corpus; not a ReaxFF paper but relevant electrochemical device modeling context.

## Citations and evidence anchors

- Abstract and keywords: modeling scope, water content, diffusion/activation energy claims (extract).
- Journal of Membrane Science 431 (2013) 79–85 and DOI line in extract.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]