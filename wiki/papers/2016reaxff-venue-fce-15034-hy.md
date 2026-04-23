---
id: paper:2016reaxff-venue-fce-15034-hy
type: paper
title: "Development, applications and challenges of ReaxFF reactive force field in molecular simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:review
  - scale:multiscale
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reaxff-application
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: ""
year: 2016
authors:
  - "You Han"
  - "Dandan Jiang"
  - "Jinli Zhang"
  - "Wei Li"
  - "Zhongxue Gan"
  - "Junjie Gu"
venue: "Front. Chem. Eng. (Springer/Higher Education Press offprint; FCE-0016-15034-HY)"
pdf_sha256: "191bbd81515714657052e30fd8f9cd99006c670f585e910a59589150112a9526"
pdf_path: "papers/ReaxFF_others/ReaxFF_review_FCE-0016-15034-HY-offprint.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016reaxff-venue-fce-15034-hy -->

## Summary

This **review** (Chinese–English) surveys **ReaxFF** **development**, **parameterization philosophy**, and **applications** across multiple domains: **high-energy organics**, **hydrocarbons** and **coal chemistry**, **nanostructured carbons** and **silicon**, **solid–liquid** and **biological interfaces**, **catalysis** on **metals** and **oxides**, and **electrochemistry** including **fuel cells** and **lithium batteries**. It also enumerates **limitations**: **parameter transferability**, **accuracy** relative to **QM** for selected observables, and challenges representing **electronically excited states** within a classical **reactive** framework.

The article is written as a **bibliographic synthesis** rather than a single benchmark study: it explains the **ReaxFF** energy decomposition (**bond**, **over/undercoordination**, **valence**, **torsion**, **conjugation**, **van der Waals**, **Coulomb**) following **van Duin**-style formulations and uses representative citations to illustrate where **reactive MD** has been impactful.

## Methods

As a **review**, the manuscript does not define one new production trajectory; **methods** are the **literature scope** and **comparison axes**. The text walks through **ReaxFF** **energy decomposition** (bonded and **nonbonded** contributions and **variable charge** practice in the **van Duin**-line formulation as cited), typical **QM-derived** training data used in **parameterization**, and **application clusters** such as oxidation, **pyrolysis**, **solid–liquid** interfaces, **mechanical** loading with bond rupture, and **electrochemical**-adjacent problems. It points readers to **primary** **parameterization** studies, **software** contexts such as **LAMMPS** where discussed, and common **validation** strategies. **Canonical DOI** for bibliography should be taken from **publisher metadata** if needed; the corpus **`doi`** field may be empty because this ingest is a named **offprint** file (**FCE-0016-15034-HY**).

## Findings

The review positions **ReaxFF** as a pragmatic bridge between **DFT-level** training data (within covered **reaction** and **phase** spaces) and **large-cell** **classical MD** timelines. It summarizes **success domains** (e.g., oxidation, catalysis, battery- and fuel-related interfaces in cited work) while stressing **limitations**: **transferability** outside training **stoichiometries**, **accuracy** for **barriers** and **excited states**, and the need to treat **parameter files** as **application-specific** contracts rather than universal physics. Readers should extract any **numerical** performance claim only from the **cited primary** study, not from this survey’s prose alone.

## Limitations

**Review** articles age quickly; **software** defaults, **best practices**, and **parameter** databases evolve. Any quantitative claim about a specific **material** must be traced to **primary** sources. The corpus copy is a **publisher offprint**; pagination may differ from other editions.

As a **bilingual** survey, it can help **non-English** readers find entry points into **ReaxFF** literature, but it should not be used as a **canonical** description of any single **parameter** file’s **validation** status.

## Relevance to group

High-level **entry** for **ReaxFF** **scope** and **limitations**, complementary to **group-specific** **parameterization** notes and **theme** hubs.

## Citations and evidence anchors

- Corpus PDF: `papers/ReaxFF_others/ReaxFF_review_FCE-0016-15034-HY-offprint.pdf`.
- Excerpt alignment: `normalized/extracts/2016reaxff-venue-fce-15034-hy_p1-2.txt`.

## Reader notes (extended)

If your goal is **citation** for a **formal bibliography**, resolve the **journal DOI** from the publisher metadata; the corpus retains the **offprint** PDF chiefly as a **stable** file path for **MANIFEST** provenance.

## Related topics

- [[reaxff-family]]
