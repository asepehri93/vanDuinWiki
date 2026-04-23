---
id: paper:2018bauchy-computationa-deciphering-atomic
type: paper
title: "Deciphering the atomic genome of glasses by topological constraint theory and molecular dynamics: A review"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - material:silicate-glass
  - method:classical-md
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:silica-silicate
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2018.12.004"
year: 2018
authors:
  - "Mathieu Bauchy"
venue: "Computational Materials Science, 159 (2018) 95–102"
pdf_sha256: "a3eac7e396b8bfd0d23ff9ea3b7ebb5fd8ce8d6df108d02c6d662f3433e734c8"
pdf_path: "papers/Others/Topology-glass-review2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018bauchy-computationa-deciphering-atomic -->

## Summary

This short review frames glass discovery as decoding an “atomic genome”: identifying how local structural motifs and their connectivity determine macroscopic properties. The article synthesizes progress that couples molecular dynamics with topological constraint theory to navigate the vast compositional space of glasses, with emphasis on silicate chemistries. Themes include using constraints to rationalize glass-forming ability, predicting mechanical behavior, and connecting local topology to chemical reactivity trends. The review argues that combining MD-derived structural statistics with constraint-based bookkeeping offers a practical complement to trial-and-error materials exploration.

## Methods

As a review, the paper does not prescribe one MD protocol. Instead it summarizes case studies from the author’s prior work and collaborators where classical or reactive simulations supply radial distributions, coordination statistics, and mechanical moduli that feed into constraint-theory analyses. Readers should consult cited primary articles for ensembles, timesteps, and system sizes. Topological constraint theory enters as a coarse-grained accounting of rigid versus flexible modes in network glasses, adapted to simulation-derived structural inputs.

In practice, the review’s “MD + constraints” recipe means extracting coordination-based constraints from equilibrated glassy cells—often silicates—and comparing predicted rigidity transitions or composition windows for glass-forming ability against independent melting or processing data cited in the underlying papers. When reactive chemistry is not required, classical silica potentials suffice; when bond-making/breaking matters, reactive or ab initio data must augment the constraint bookkeeping.

## Findings

The review positions MD plus constraint theory as a scalable strategy for exploring composition–property relationships when exhaustive experimental screening is impractical. Reported examples (per abstract scope) include predicting mechanical responses and clarifying chemical reactivity trends in silicate glasses beyond Edisonian mapping. The narrative emphasizes that local motif statistics extracted from simulation can be tied to global constraints that control rigidity transitions and ductility.

Because glasses occupy a vast compositional space—including multicomponent oxides, chalcogenides, and oxycarbides—the review stresses computational filters: simulations propose plausible networks, constraints reduce the dimensionality of “what can be rigid,” and targeted experiments validate only the most promising islands in composition space. Readers should treat each cited case study as conditional on the potential model used to generate the underlying structures.

## Limitations

Specific numerical benchmarks are not centralized here; claims must be traced to referenced primary studies. Constraint theory assumptions may break down for highly ionic or nanosegregated glasses without careful parametrization.

## Corpus notes

When refreshing this page, verify that cited primary studies still match the review bibliography, because downstream tooling does not automatically track corrigenda to *Computational Materials Science* articles referenced here.

## Related topics

- [[theme-oxides-silica-ceramics]]
- [[reaxff-family]]
