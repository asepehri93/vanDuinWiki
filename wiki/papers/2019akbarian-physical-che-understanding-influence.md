---
id: paper:2019akbarian-physical-che-understanding-influence
type: paper
title: "Understanding the influence of defects and surface chemistry on ferroelectric switching: a ReaxFF investigation of BaTiO3"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:ferroelectrics-polar
  - material:perovskite-oxide
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/C9CP02955A"
year: 2019
authors:
  - "Dooman Akbarian"
  - "Dundar E. Yilmaz"
  - "Ye Cao"
  - "P. Ganesh"
  - "Ismaila Dabo"
  - "Jason Munro"
  - "Renee Van Ginhoven"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys. 2019, 21, 18240–18249"
pdf_sha256: "4e189e8d7a502e133c6b71b0515a1f32eb49a9ad3ed94883212e916fe53ebc6e"
pdf_path: "papers/Akbarian_PCCP_BaTiO3_2019.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019akbarian-physical-che-understanding-influence -->

## One-paragraph summary

An extensible atomistic ReaxFF for **BaTiO3** is constructed to capture field- and temperature-driven ferroelectric hysteresis together with modifications from **surface chemistry** and **bulk oxygen vacancies**. The authors connect simulations to several experimental observations: a critical thickness near **4.8 nm** below which ferroelectricity is suppressed; oxygen vacancy migration/clustering reducing polarization and Curie temperature; and domain-wall interactions with surfaces that alter switching pathways and polarization magnitude—positioning the model for interface-heavy ferroelectric device scenarios.

## Methods

- **Reactive FF:** ReaxFF parametrization targeting BaTiO3 ferroelectric response and defect energetics.
- **MD:** Polarization switching protocols under electric fields and temperature; defect and surface models.

## Findings

- Mechanistic coupling between vacancies, domain walls, and surface termination in setting switching behavior.
- Demonstrates ReaxFF as a practical bridge between DFT-scale insight and larger nanostructure samples for ferroelectrics.

## Limitations

- Quantitative accuracy for all observables depends on training scope; complex heterointerfaces and dynamical band-gap effects are not fully captured in a classical reactive model.

## Relevance to group

Primary wiki anchor for **ferroelectric perovskites + ReaxFF** within the corpus.

## Citations and evidence anchors

- DOI: [10.1039/C9CP02955A](https://doi.org/10.1039/C9CP02955A)
- Opening summary: `normalized/extracts/2019akbarian-physical-che-understanding-influence_p1-2.txt`

## Related topics

- [[reaxff-family]]
- BaTiO3 ferroelectric switching and oxygen vacancies
- Domain walls and surface termination in perovskites
