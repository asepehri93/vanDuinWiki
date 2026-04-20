---
id: paper:2014zhang-venue-jp5054277
type: paper
title: "Development of a ReaxFF reactive force field for tetrabutylphosphonium glycinate/CO2 mixtures"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:classical-md
  - task:parameterization
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1021/jp5054277"
year: 2014
authors:
  - "Bo Zhang"
  - "Adri C. T. van Duin"
  - "J. Karl Johnson"
venue: "Journal of Physical Chemistry B 2014, 118, 12008–12016"
pdf_sha256: "afa01e785856fd907e673d7b40880bb3b4691aefae16f11dfa55a82e1354eb5f"
pdf_path: "papers/Zhang_JPC_B_IL_CO2_2014.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014zhang-venue-jp5054277 -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Zhang, van Duin, and Johnson develop a **ReaxFF** description for **\[P(C\(_4\))\(_4\)\]\[Gly\]** ionic liquid interacting with **CO\(_2\)**, targeting simultaneous **physical sorption**, **complexation**, and **chemisorption** channels that fixed-bond force fields cannot represent. The training set combines **periodic DFT** reaction pathways in the condensed phase, **condensed-phase MD** configurations, and **gas-phase cluster** interactions for intra-ion and ion–CO\(_2\) contacts. The abstract reports that optimized parameters reproduce key **DFT/experiment/classical** benchmarks and that **MD** distributions of **C(CO\(_2\))–N(anion)** distances and **CO\(_2\)** bending angles broadly match **DFT-MD**. A predicted **density increase** with CO\(_2\) loading up to at least **50 mol %** is attributed partly to the compact effective volume of **chemically bound** CO\(_2\).

## Methods

- **ReaxFF** optimization against **DFT** reaction and condensed-phase sampling.
- **MD** validation of structural distributions and mixture densities.

## Findings

- IL/CO\(_2\) systems exhibit **multiple interaction strengths**; reactive FF enables unified sampling without ad hoc mixing of pre/post-reacted phases.
- Demonstrates **CO\(_2\) capture** relevance for **ionic-liquid** screening workflows.


## Limitations

- Viscosity and transport of real supported-IL configurations (noted in related experimental literature in the introduction) remain partially outside the excerpted scope.
- Quantitative binding free energies and full reaction networks require full-text tables.

## Relevance to group

**Adri C. T. van Duin** co-authorship; extends **ReaxFF** to **CO\(_2\)+ionic-liquid** reactive sorption, connecting to separations and carbon-capture modeling use cases.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp5054277](https://doi.org/10.1021/jp5054277)

## Related topics

- [[reaxff-family]]
