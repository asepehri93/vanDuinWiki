---
id: paper:2019chapter9-venue-paper
type: paper
title: "Molecular dynamics simulations of MXenes: ab initio, reactive, and non-reactive empirical force fields"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - material:tmd
  - method:reaxff
  - method:classical-md
  - method:aimd
  - task:review
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:review-or-perspective
  - keyword:2d-materials
  - keyword:aimd
  - keyword:reaxff-application
  - keyword:batteries-interfaces
source_refs: []
doi: "10.1007/978-3-030-19026-2_9"
year: 2019
authors:
  - "Roghayyeh Lotfi"
  - "Dundar E. Yilmaz"
  - "Lukas Vlcek"
  - "Adri van Duin"
venue: "In: 2D Metal Carbides and Nitrides (MXenes), Springer (2019)"
pdf_sha256: "67189b7ad93953442949931eb8c92ac278c0a845a21e4e17a5756beb598cfbc8"
pdf_path: "papers/Chapter9_MXenes Book_Final.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2019chapter9-venue-paper -->

## Summary

Springer’s *2D Metal Carbides and Nitrides (MXenes)* volume synthesizes synthesis, properties, and applications of MXenes; Chapter 9 focuses on how molecular simulation methods have been applied to MXene systems. Lotfi, Yilmaz, Vlcek, and van Duin review three modeling tiers: ab initio molecular dynamics for short-time electronic-structure fidelity, reactive empirical potentials such as ReaxFF for bond-breaking chemistry at larger scales, and non-reactive classical force fields for elastic and charging dynamics where chemistry is frozen. The chapter surveys literature uses of these tiers across energy storage, ion and molecule adsorption, catalysis, exfoliation, and water-related phenomena, explaining when each level is appropriate and what tradeoffs arise in cost versus accuracy. Readers approaching MXenes from experiment receive a roadmap for selecting models that match the phenomenon’s timescale and electronic requirements.

## Methods

The chapter is organized as a methods taxonomy plus literature survey. It defines AIMD, reactive MD, and classical MD assumptions, compares computational cost scaling, and walks through representative applications with citations to primary studies rather than presenting new simulations in the chapter text available here. Worked examples reference community codes and typical ensemble choices without replacing primary sources. Reproducibility for any specific numerical claim requires the original paper cited in the chapter; this PDF should be read as a guided bibliography and conceptual framework.

## Findings

The narrative states that non-reactive MD is often used for large systems or slow ionic charging where bonds remain intact, whereas ReaxFF-class models become necessary when electrolyte decomposition or surface redox chemistry matters. AIMD is positioned as a validator for structures and short-time stability. The chapter ties these capabilities to application clusters such as intercalation thermodynamics, diffusion, friction, and electrochemical interfaces, emphasizing that parameter sets continue to evolve after 2019. The overarching conclusion is methodological: MXene simulation success depends on aligning model fidelity with the chemistry question, not on using the most expensive method everywhere. Students new to the field can read the chapter as a decision tree: start from the phenomenon (intercalation versus bond-breaking versus elasticity), then pick AIMD, ReaxFF, or fixed-bond FF accordingly, citing primary studies for parameters. Practitioners updating MXene models after 2019 should layer newer interatomic potentials and DFT benchmarks on top of this chapter rather than discarding it, because the organizational structure—what questions each method class can answer—remains stable even as parameters evolve. The chapter also pairs naturally with the Springer TOC fragment `paper:2019mxenes-venue-paper` for bibliographic completeness.

## Limitations

Review coverage is bounded by publication date and cited corpus; MXene parameterizations and DFT functionals have advanced since printing.

## Relevance to group

van Duin co-authored the MXene simulation review in the Springer MXenes volume.

## Citations and evidence anchors

https://doi.org/10.1007/978-3-030-19026-2_9

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
