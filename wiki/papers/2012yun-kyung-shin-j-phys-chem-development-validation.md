---
id: paper:2012yun-kyung-shin-j-phys-chem-development-validation
type: paper
title: "Development and Validation of a ReaxFF Reactive Force Field for Fe/Al/Ni Alloys: Molecular Dynamics Study of Elastic Constants, Diffusion, and Segregation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - material:alloy-bulk
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp308507x"
year: 2012
authors:
  - "Yun Kyung Shin"
  - "Hyunwook Kwak"
  - "Chenyu Zou"
  - "Alex V. Vasenkov"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A 2012, 116, 12163–12174"
pdf_sha256: "ebcbf5fb6790677f20d471f9fae766ef65284e359d1b18578f1d0310d0cb274a"
pdf_path: "papers/Shin_FeAlNi_JPCA_2012.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2012yun-kyung-shin-j-phys-chem-development-validation -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A ReaxFF parameterization for **Fe–Al–Ni** alloys is derived from QM data on bulk phases and low-index surface energies and adatom binding. Validation MD computes temperature-dependent elastic constants for FeAl, FeNi3, and Ni3Al (300–1100 K), matching experimental trends of softening with temperature; diffusion simulations in compositionally graded Al/Ni layers show strong composition dependence of Al diffusivity near 1000 K; high-temperature surface segregation in L12-ordered clusters reveals composition-dependent segregation strengths (e.g., Al enriches most on Fe3Al surfaces among the cases studied), qualitatively consistent with older experimental reports.

## Methods

- **Fitting:** QM-derived bulk, surface, and adatom training sets for binary Fe–Al–Ni alloy interactions.
- **MD:** Elastic constant extraction, diffusion in layered geometries, segregation analysis in finite clusters at 2500 K.

## Findings

- Cohesive picture of mechanical and transport properties plus surface chemistry for model alloy systems under a single reactive FF.


## Limitations

- High segregation temperature and simplified geometries are modeling choices to access kinetics within MD timescales; direct quantitative match to all experimental conditions may require larger models and longer runs.

## Relevance to group

Canonical **metallic alloy ReaxFF** development paper used as a foundation for subsequent oxidation and materials mechanics studies.

## Citations and evidence anchors

- DOI: [10.1021/jp308507x](https://doi.org/10.1021/jp308507x)
- Abstract: `normalized/extracts/2012yun-kyung-shin-j-phys-chem-development-validation_p1-2.txt`

## Related topics

- [[reaxff-family]]
- ReaxFF for metals and alloys (Fe–Al–Ni)
- Surface segregation and diffusion in alloys