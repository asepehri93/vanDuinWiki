---
id: paper:2015han-venue-paper
type: paper
title: "Development, applications and challenges of ReaxFF reactive force field in molecular simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:review
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
source_refs: []
doi: "10.1007/s11705-015-1545-z"
year: 2015
authors:
  - "You Han"
  - "Dandan Jiang"
  - "Jinli Zhang"
  - "Wei Li"
  - "Zhongxue Gan"
  - "Junjie Gu"
venue: "Frontiers of Chemical Science and Engineering"
pdf_sha256: "d623c3b35b5587be7777def61b41a7bf18cc1a7e910fc79f106690994931912e"
pdf_path: "papers/ReaxFF_others/Han_ReaxFF_review_FrontChemSciEng_2015.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2015han-venue-paper -->

## Summary

This Frontiers of Chemical Science and Engineering review surveys roughly two decades of ReaxFF development and application as an approach that bridges quantum chemistry and non-reactive empirical force-field molecular simulation when bond making and breaking matter. The abstract states that ReaxFF aims to supply a transferable potential capable of describing many reactions with bond formation and cleavage. The article organizes applications into several clusters: organic reactions under extreme conditions tied to high-energy materials, hydrocarbons, and coals; nanomaterials such as graphene oxides, carbon nanotubes, silicon nanowires, and metal nanoparticles; solid–solid, solid–liquid, and biological or inorganic interfaces; catalysis on metals and metal oxides; and electrochemical mechanisms in fuel cells and lithium batteries. The review also lists limitations and challenges that the authors argue illuminate future directions for applying ReaxFF across a wider range of chemical environments.

## Methods

This article is a **literature review** (Frontiers of Chemical Science and Engineering), not a laboratory or simulation study with a single numerical protocol.

**Review scope and organization.** The introduction contrasts quantum chemistry cost with non-reactive force fields, then reproduces the standard ReaxFF energy decomposition (bond, over- and under-coordination, lone-pair, valence angle, penalty, torsion, conjugation, van der Waals, and Coulomb terms). Later sections summarize milestone parameter lines and application clusters by citation: organics and high-energy-materials-related chemistry, extensions toward many elements, and representative application areas called out in the abstract (e.g., nanocarbon and metal nanoparticles, interfaces, catalysis on metals/oxides, and electrochemical settings discussed in the cited primary literature).

Because the article is a **survey**, it does **not** anchor a single numerical MD protocol (timestep, barostat, production length) or a standalone QM convergence table for one project; those quantities are **N/A here** and must be taken from each **cited primary** study. Likewise, **new ReaxFF parameter fits** are not reported as a unified training exercise in this review—development milestones are described **by citation** rather than as one reproducible optimization log on these pages.

## Findings

The abstract frames ReaxFF as filling the gap between quantum chemistry and non-reactive empirical simulations for systems where connectivity changes. The early sections quoted in the extract describe progressive broadening of ReaxFF from organics to many elements and application areas, with illustrative references to silicon oxide benchmarks, aluminum phases, magnesium hydride equations of state, multi-metal carbon training sets, lithium parameter development, and large QM training sets for vanadium oxide catalysis. The review’s stated intent is to summarize development trajectories and application clusters while flagging limitations and open challenges named in the closing sections of the paper.

## Limitations

As with any broad review, fidelity to any specific application depends on the cited primary literature rather than this summary alone. The corpus extract covers the opening pages; specialized numerical claims should be checked against the cited originals.

## Relevance to group

Pedagogical survey of ReaxFF scope and milestones, including van Duin-line references in the bibliography, useful as a high-level map alongside group-specific parameterization notes.

## Reader notes (navigation)

- [[reaxff-family]]
- [[protocols/reaxff-parameterization-workflow]]
