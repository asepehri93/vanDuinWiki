---
id: paper:2013newsome-venue-jp307680t
type: paper
title: "High-Temperature Oxidation of SiC-Based Composite: Rate Constant Calculation from ReaxFF MD Simulations, Part II"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp307680t"
year: 2013
authors:
  - "Newsome, David A."
  - "Sengupta, Debasis"
  - "van Duin, Adri C. T."
venue: "Journal of Physical Chemistry C"
pdf_sha256: "a794e37e8e48bca3182364ad0f9a84af35d75324f2c2fb28c97b1ce290917790"
pdf_path: "papers/Newsome_JPCC_2013.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2013newsome-venue-jp307680t -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

Part II of a two-part study uses ReaxFF reactive molecular dynamics trajectories to build rate models for thermal protection system (TPS) chemistry: oxidation of silicon carbide by O₂ and H₂O and combustion/pyrolysis of an EPDM polymer model. The work connects atomistic transport and reaction events to Arrhenius parameters for comparison with experiment and with phenomenological multiscale models (abstract and introduction, pages 1–2 of the extract).

## Methods

Reactive MD with a Si/C/H/O ReaxFF parameterization trained to quantum data (Part I referenced in the text). Rate-theory fits extend a Deal–Grove style picture of oxidizer transport through developing SiO₂ and interface reaction. Separate trajectory sets target EPDM combustion versus pyrolysis for Arrhenius extraction (abstract; Introduction; “Details of computational approach”, extract pages 1–2).

## Findings

O₂ oxidizes SiC more efficiently than H₂O in the simulations; transport activation barriers are reported roughly in the 40–70 kJ/mol range for O₂ and 125–150 kJ/mol for H₂O. Oxidizer attack produces a growing SiO₂-rich surface and carbon migration into a carbonaceous region. EPDM simulations yield activation barriers near 183 kJ/mol (combustion) and 213 kJ/mol (pyrolysis), bracketed against experimental polymer literature near ~100–250 kJ/mol (abstract).

## Limitations

Part II depends on Part I force-field validation and trajectory ensembles; Arrhenius extraction from short MD windows can be sensitive to model and sampling. The extract covers early pages only; full temperature/pressure matrices and uncertainty quantification appear later in the PDF.

## Relevance to group

Co-authored with Adri van Duin; demonstrates ReaxFF for aerospace ablation/oxidation chemistry and quantitative kinetics extraction aligned with the group’s reactive MD and parameterization line.

## Citations and evidence anchors

- Abstract and introduction: contribution statement, barrier ranges, EPDM Arrhenius values, J. Phys. Chem. C framing (extract pages 1–2).
- DOI: `10.1021/jp307680t` (footer of extract).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
