---
id: paper:2009vanduin-venue-reactive-force
type: paper
title: "Reactive force fields: Concepts of ReaxFF"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:method-development
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:review
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2009
authors:
  - "Adri van Duin"
venue: "Computational Methods in Catalysis and Materials Science (Wiley-VCH, 2009), Chapter 9"
pdf_sha256: "1d6a5f9ac1dd66495401f0ef7879737bf2e55584c176474df5c8e801b396f44a"
pdf_path: "papers/vanDuin_ReaxFF_vanSanten_chapter_2009.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2009vanduin-venue-reactive-force -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **edited volume chapter** identified by `pdf_path` and imprint lines in the extract (ISBN **978-3-527-32032-5**). Assign a **chapter DOI** only if you add it from the publisher record—the normalized JSON has none.

## Summary

This pedagogical chapter introduces **ReaxFF** as a **QM/FF bridge** for **bond making and breaking** in large MD simulations. It contrasts accurate QM length/time scales (order **100–1000 atoms**) with engineering needs (example: **~10\(^6\)** atoms in a **20 nm** cube), motivating **QM-fitted reactive force fields** and higher-scale coarse graining. The text outlines how ReaxFF extends classical FF ideas via **distance-derived bond orders**, coupling to **multibody** terms, and **charge delocalization** treatments, and positions ReaxFF among alternatives (e.g., tight-binding) emphasizing **empirical flexibility** vs. **transferability challenges** validated by extrapolation to new conditions.

## Methods


**Pedagogical chapter (checklist D)**—no single **benchmark** **MD** protocol; instead a **literature/scale** survey.

### Multiscale placement

- Contrasts **QM** reach (**~10\(^2\)–10\(^3\)** atoms as a typical order-of-magnitude classroom statement) with **FF MD** for far larger cells (illustrative **~10\(^6\)** atoms in a **~20 nm** cube; mentions **billion-atom** parallelism as an upper-end aspiration in the narrative).
- Discusses **coarse graining** from atomistic **MD** toward **mesoscale** descriptions (conceptual only—no specific CG mapping implemented in the chapter).

### ReaxFF formalism overview (as presented)

- **Distance-derived bond orders** feeding **valence** and **multibody** energy terms; **over/undercoordination** corrections; **charge** treatment via **electronegativity equilibration**-style schemes as described in the chapter text (see also dedicated **ReaxFF** primary papers cited in the bibliography).
- **Comparisons:** positions **ReaxFF** relative to **tight-binding** / more **QM-like** approximations, emphasizing **empirical** flexibility vs **transferability** risk.

### Not included

- No **timestep**, **thermostat**, **cutoff**, or **software** settings—readers must go to application papers + parameter files for executable protocols.

## Findings

**Positioning vs QM and classical FFs.** The chapter frames **ReaxFF** as a **QM/FF bridge** aimed at **bond making and breaking** in large **MD** simulations where accurate **QM** is limited to roughly **\(10^2\)–\(10^3)\) atoms** (order-of-magnitude classroom statement in the excerpt), while engineering-scale examples motivate **much larger** cells (illustrative **\(\sim 10^6\)** atoms in a **\(\sim 20\) nm** cube narrative) enabled by force-field **MD** acceleration.

**Formalism hooks (conceptual).** The indexed introduction lists core extensions relative to nonreactive FFs: **distance-derived bond orders**, coupling to **multibody** terms, and **charge delocalization / electronegativity equilibration-style** treatments as part of the ReaxFF picture.

**Comparisons to alternatives.** ReaxFF is contrasted with more **QM-linked** approximations such as **tight-binding** routes, emphasizing **empirical flexibility** versus **transferability** challenges.

**Limitations / validation stance.** The excerpt stresses that without first-principles closure, **empirical** methods rely on **extrapolation validation** against **QM** and **experiment** for scoped conditions—**caution** is implied when pushing **new** chemistries or states.

**Corpus honesty.** This page summarizes the **handbook chapter** at `pdf_path` plus `normalized/extracts/2009vanduin-venue-reactive-force_p1-2.txt` (intro pages). **Equations, citations, and parameter-file details** require the **full PDF**; there is **no chapter DOI** in the front matter.

## Limitations

A handbook chapter cannot replace parameter files or primary application papers for specific chemistries. Illustrative system-size numbers depend on hardware, parallel algorithms, and implementation details.

## Relevance to group

Authored by **Adri van Duin**, this is a **canonical pedagogical entry point** for ReaxFF concepts used in teaching and onboarding for MAS retrieval.

## Citations and evidence anchors

- PDF: `papers/vanDuin_ReaxFF_vanSanten_chapter_2009.pdf`.
- Extract: `normalized/extracts/2009vanduin-venue-reactive-force_p1-2.txt`.
- Book: *Computational Methods in Catalysis and Materials Science*, Wiley-VCH (see title page in PDF).

## Related topics

- [[reaxff-family]]
- [[themes-index]]
