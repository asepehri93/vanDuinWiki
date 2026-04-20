---
id: paper:2016islam-venue-ct6b00432
type: paper
title: "eReaxFF: a pseudoclassical treatment of explicit electrons within reactive force field simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:ereaxff
  - method:reaxff
  - task:method-development
  - domain:methods-software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.6b00432"
year: 2016
authors:
  - "Md Mahbubul Islam"
  - "Grigory Kolesov"
  - "Toon Verstraelen"
  - "Efthimios Kaxiras"
  - "Adri C. T. van Duin"
venue: "J. Chem. Theory Comput."
pdf_sha256: "785eb9c8dcbbf11351c7d9a2752ab2578ebc90aafd32285836069df87d45b0c8"
pdf_path: "papers/Islam_JCTC_eReaxFF_2016.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2016islam-venue-ct6b00432 -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

The article introduces **eReaxFF**, an extension of **ReaxFF** that treats **electrons explicitly** in a **pseudoclassical** formulation integrated with **ACKS2-derived** charge/electronic-structure approximations, targeting **orders-of-magnitude** speedups over conventional **quantum chemistry dynamics**. Training emphasizes **electron affinities** for representative **hydrocarbon radicals**, with **MD demonstrations** comparing **eReaxFF** to **Ehrenfest**-style references for selected cases. The authors argue that **literature ReaxFF parameters** remain largely **transferable** into the new framework, lowering adoption friction.

## Methods

- **Formulation + integration** of explicit electronic degrees of freedom with **ReaxFF** energy expressions.
- **ACKS2** coupling for charge-related quantities as described in the paper.
- **Proof-of-principle MD** on radical systems with **EA benchmarks**.

## Findings

- **Qualitative EA trends** align with **experiment** for multiple species in the benchmark suite presented.
- **eReaxFF MD** tracks **Ehrenfest** references more closely than naïve classical alternatives in the tests highlighted in the abstract.
- Positions the method as a bridge toward **large-scale redox, polarization, and battery-interface** problems that strain implicit-charge reactive models.

## Limitations

- **Pseudoclassical electrons** are not a full **quantum electronic** solution; accuracy limits near **conical intersections** and **strongly correlated** states must be monitored.
- **Parameter portability** still requires systematic validation per **chemically distinct** subsystem.

## Relevance to group

Landmark **method paper** from the **van Duin + Harvard + Ghent** collaboration defining **eReaxFF**, a cornerstone of the group’s **next-generation reactive FF** roadmap.

## Citations and evidence anchors

- Abstract and Sec. I in `papers/Islam_JCTC_eReaxFF_2016.pdf`; **DOI:** `10.1021/acs.jctc.6b00432`.

## Related topics

- [[reaxff-family]]
