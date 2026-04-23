---
id: paper:noyear-stack-stack-envichem10revised-metadynamics
type: paper
title: "Geochemical reaction mechanism discovery from molecular simulation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - task:review
  - method:enhanced-sampling
  - method:classical-md
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:review-or-perspective
  - keyword:enhanced-sampling
  - keyword:water-interfaces
  - keyword:monte-carlo-sampling
source_refs: []
doi: ""
year: 0
authors:
  - "Andrew G. Stack"
  - "Paul R. C. Kent"
venue: "Manuscript PDF (corpus; Environmental Chemistry context)"
pdf_sha256: "c3abc01722071bf63f55927f4489cb864d18fcdb91ce6fc721298cd3e0e0a7ca"
pdf_path: "papers/Others/stack_envichem10revised_Metadynamics.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:noyear-stack-stack-envichem10revised-metadynamics -->


## Summary

Review-style article arguing that molecular simulation can isolate elementary geochemical reactions, quantify their rates and mechanisms, and thereby improve macroscopic kinetic models beyond net rates inferred from bulk experiments. It surveys classical molecular dynamics and quantum chemical approaches, discusses enhanced sampling tools including umbrella sampling and metadynamics, and presents thematic case studies (water exchange and sorption, surface charging, crystal growth and dissolution, electron transfer). The pedagogical tone matches a manuscript-style review rather than a single experimental campaign with one dataset.

## Methods

Primary source: `papers/Others/stack_envichem10revised_Metadynamics.pdf` (28 pages; filename suggests Environmental Chemistry coursework or revised notes). No DOI is recorded in front matter.

The article is a **conceptual and literature synthesis**, not a single new simulation study. Methodological content compares strengths and limits of **classical MD** (force fields, fixed versus polarizable charges, harmonic bonds, long-range electrostatics) versus **quantum chemistry** for reaction mechanisms, and introduces **rare-event methods** such as umbrella sampling and metadynamics for barrier crossing and free-energy profiles. Case-study subsections reference published applications across aqueous species, mineral surfaces, growth and dissolution, and redox processes.

## Findings

- Macroscopic field-versus-laboratory rate discrepancies and qualitative failures of net-rate models motivate atomistic mechanism discovery rather than descriptive fitting alone.
- Classical MD scales to large systems and long times but depends on force-field validity; quantum methods improve electronic detail but constrain system size and sampling.
- Enhanced sampling (umbrella sampling, metadynamics) is presented as a practical route to explore reaction pathways and free energies that brute-force MD cannot reach.
- Illustrative applications show how simulations have clarified specific mechanisms (e.g., water exchange, sorption, surface charging, growth/dissolution, electron transfer) that bulk measurements average over.
- Outlook: molecular simulation should become more common for validating experiments and testing plausibility of kinetic models used in environmental and geochemical risk assessment.

## Limitations

Corpus PDF lacks standard bibliographic DOI in metadata; year and exact venue are not established from the file alone. Treat citations inside the PDF as **unverified** for this wiki until matched to a published version; operators should not assume page-level bibliographic completeness from the filename alone.

## Relevance to group

Peripheral reference for geochemical enhanced sampling and MD methodology; no van Duin authorship. Useful as a **methods vocabulary** pointer (**umbrella sampling**, **metadynamics**) adjacent to reactive workflows that still require rare-event treatment at interfaces.

## Citations and evidence anchors

<!-- No DOI in front matter; cite PDF path for local provenance. -->

- Local PDF path for operators: `papers/Others/stack_envichem10revised_Metadynamics.pdf`

## Related topics

- [[reaxff-family]]
