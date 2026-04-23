---
id: paper:2022annurev-physchem-082-venue-paper
type: paper
title: "Neural Network Potentials: A Concise Overview of Methods"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:ml-atomistic
  - method:ml-potential
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:machine-learning-potential
  - keyword:review-or-perspective
candidate_tags: []
source_refs: []
doi: "10.1146/annurev-physchem-082720-034254"
year: 2022
authors:
  - "Emir Kocer"
  - "Tsz Wai Ko"
  - "Jörg Behler"
venue: "Annu. Rev. Phys. Chem."
pdf_sha256: "ebacdcc448bf96445e67f8490c15bd8595acf9d7d93aa50492f7229587708118"
pdf_path: "papers/Others/annurev-physchem-082720-034254.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2022annurev-physchem-082-venue-paper -->

## Summary

Machine-learning potentials, especially neural-network models, now enable large-scale atomistic simulations across molecular liquids, condensed phases, and extended materials with accuracy approaching density-functional theory when training data are adequate. Kocer, Ko, and Behler contribute an Annual Review of Physical Chemistry chapter that surveys neural-network potentials mapping atomic environments—encoded by handcrafted or learned descriptors—to potential energies and analytic forces for molecular dynamics. The narrative stresses that sharing a neural-network headline still hides major design forks: local versus global representations, explicit long-range electrostatics versus implicit embedding of polarization, and the treatment of charge transfer or multi-center electronic effects that break strict locality assumptions.

## Methods

This entry is a **methods review** (Annual Review of Physical Chemistry), not a primary simulation paper.

### A — Machine-learned interatomic potentials (training data)

- How **DFT** databases, **incremental** learning, and **active** learning loops feed **neural** potential training.

### B — Model architectures

- **Feedforward** nets vs **equivariant message-passing** networks; descriptor choices and symmetry constraints.

### C — MD engine integration

- **PBC**, **stress** tensors, **finite timestep** stability, coupling to **enhanced sampling**.

### D — Long-range electrostatics / polar systems

- **Local** covalent potentials vs **hybrid** schemes with **long-range** kernels or **charge-equilibration** submodels for **ionic** environments (parallel vocabulary to **ReaxFF** / **eReaxFF** discussions elsewhere in the corpus).

The chapter does **not** publish one new unified benchmark suite; cite **primary** studies for numerical performance claims.

## Findings

The authors conclude that neural potentials can reach near-DFT accuracy for energies and forces when training coverage spans the chemistry encountered in production simulations, but transferability remains limited by descriptor completeness and by how electronic long-range interactions are represented. Open challenges include data efficiency for rare elements, robust extrapolation outside training manifolds, and consistent coupling to enhanced sampling and rare-event methods that rely on accurate free-energy surfaces. For groups using empirical reactive fields such as ReaxFF, the chapter supplies parallel vocabulary—symmetry-adapted descriptors, learned equivariant layers, charge equilibration—useful when comparing hybrid QM–ML workflows to fully empirical reactive models.

Readers building retrieval systems around this wiki should treat the review as a map to primary literature rather than as a standalone benchmark of model accuracy. Section cross-references in the PDF remain the authoritative outline for follow-up reading lists.

## Limitations

No new numerical experiments appear in the review; performance numbers must be traced to cited primary studies. Corpus metadata marks PDF extraction quality as partial—use `papers/Others/annurev-physchem-082720-034254.pdf` for authoritative section boundaries and bibliography.

## Relevance to group

Provides taxonomy and vocabulary for neural MLPs alongside ReaxFF-focused work in the corpus.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
