---
id: paper:2013vanduin-venue-untitled
type: paper
title: "A ReaxFF reactive force-field for proton transfer reactions in bulk water and its applications to heterogeneous catalysis (book chapter)"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reaxff-parameterization
  - keyword:water-interfaces
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:review
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/9781849734905-00223"
year: 2013
authors:
  - "Adri C. T. van Duin"
  - "Chenyu Zou"
  - "Kaushik Joshi"
  - "Vyascheslav Bryantsev"
  - "William A. Goddard"
venue: "Computational Catalysis (RSC Catalysis Series No. 14)"
pdf_sha256: "83244d0c79fc2655ecf77956a9824e4e885e39a328b26b4547c96a2dc5e92512"
pdf_path: "papers/vanDuin_ReaxFF_water_RoySoc_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013vanduin-venue-untitled -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **book chapter** identified by `doi`, `title`, and `pdf_path`.

## Summary

Chapter **6** surveys a **ReaxFF water** description aimed at **proton-transfer** chemistry in **bulk water** and selected **heterogeneous catalysis** contexts, situating ReaxFF among many empirical and polarizable water models. The narrative contrasts **pairwise** vs **polarizable** water force fields, discusses transferability trade-offs, and outlines how reactive MD with ReaxFF enables **bond-breaking/forming** simulations not accessible to fixed-bond water models—supporting mechanistic studies at interfaces relevant to catalysis when combined with appropriate parameter sets.

The chapter is written for catalysis practitioners comparing empirical options: it explains when a reactive water model is necessary instead of a rigid water model plus implicit assumptions about dissociation.

## Methods

**4 — Reviews / book chapter (literature scope).** **Chapter 6** in *Computational Catalysis* (RSC Catalysis Series **No. 14**, DOI **10.1039/9781849734905-00223**) is a **survey**: it contrasts **pairwise** vs **polarizable** water models, explains how **ReaxFF** encodes **bond-order** reactivity for **bulk** water and **proton-transfer** chemistry, and connects those modeling choices to **heterogeneous catalysis** questions (oxide/water interfaces, acid–base chemistry) where fixed-bond water is insufficient (`papers/vanDuin_ReaxFF_water_RoySoc_2013.pdf`; `normalized/extracts/2013vanduin-venue-untitled_p1-2.txt`). The chapter points to collaborative **parameter-development** context (Caltech/Goddard-group lineage as cited in the volume).

**1 — MD application (production protocols).** **N/A —** the chapter is not a standalone protocol paper; **timestep**, **ensemble**, **thermostat**, **barostat**, **system sizes**, and **DMS** settings for specific production runs belong to the **primary journal articles** referenced inside the chapter.

**2 — Force-field training.** The chapter discusses **ReaxFF** functional form and **philosophy** for reactive water; **N/A —** for a single enumerated **QM training set / optimizer / weights table** on this wiki layer—those details are paper-specific and should be copied from cited primary sources when needed.

**3 — Static QM / DFT-only.** **N/A —** not a **DFT** application note; **QM** enters comparatively when discussing accuracy relative to empirical reactive water models.

## Findings

**Outcomes & mechanisms (didactic).** The chapter argues that **ReaxFF water** enables **bond-breaking/forming** simulations inaccessible to **fixed-bond** water models at **cost** tractable for large condensed-phase cells, while remaining **approximate** relative to **QM** or **MS-EVB**-class proton treatments.

**Comparisons.** It situates **ReaxFF** among **pairwise** and **polarizable** alternatives for catalysis practitioners choosing empirical models.

**Sensitivity & transferability.** Accuracy trade-offs depend on the target **interface chemistry**; users are implicitly directed to validate **barriers** and **solvation** structures against higher-level benchmarks for each new system (as the chapter’s narrative implies).

**Limitations & outlook.** Quantitative **kinetics**, **pK\(_a\)**-level accuracy, and **spectroscopic** benchmarks are **not** asserted here as chapter-local results—defer to **cited primaries**.

**Corpus honesty.** Use this page for **historical framing** and **DOI-grounded** navigation; do not treat the book chapter as a substitute for the **parameter files** and **protocol tables** in underlying journal papers.

## Limitations

Book chapter scope is **didactic**; quantitative benchmarks should be taken from the underlying journal papers and parameter releases.

## Relevance to group

Canonical **group-authored** exposition of **reactive water** models and their catalytic applications alongside Caltech collaborators.

## Citations and evidence anchors

- DOI: [10.1039/9781849734905-00223](https://doi.org/10.1039/9781849734905-00223)
- Extract: `normalized/extracts/2013vanduin-venue-untitled_p1-2.txt`

## Reader notes (navigation)

- **RSC Catalysis Series** chapter; cite chapter DOI for the book contribution.

## Related topics

- [[reaxff-family]]
- Proton transport and aqueous interfacial catalysis
