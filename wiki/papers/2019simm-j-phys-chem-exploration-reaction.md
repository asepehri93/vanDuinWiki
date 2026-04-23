---
id: paper:2019simm-j-phys-chem-exploration-reaction
type: paper
title: "Exploration of Reaction Pathways and Chemical Transformation Networks"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:dft-static
  - method:enhanced-sampling
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:neb
  - keyword:dft-static
  - keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.8b10007"
year: 2019
authors:
  - "Gregor N. Simm"
  - "Alain C. Vaucher"
  - "Markus Reiher"
venue: "J. Phys. Chem. A (2019), 123, 385-399"
pdf_sha256: "f199e3b913bb23acb1e3fac5ad3e8c8e25198a6504dfc6b736f453d57f0f8ae8"
pdf_path: "papers/Others/Reaction_path_analysis_JPC_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019simm-j-phys-chem-exploration-reaction -->

## Summary

This open-access *J. Phys. Chem. A* feature article (ACS AuthorChoice) classifies algorithms for mapping potential energy surfaces (PES) and chemical reaction networks. It is not a ReaxFF or classical-MD application paper: the focus is quantum-chemical PES exploration and how different workflows trade completeness, computational cost, and human input.

Simm, Vaucher, and Reiher frame complex mechanisms as a search for relevant intermediates and elementary steps. Automated tools are grouped into three classes (see Figure 1 in the version-of-record PDF). Class 1 starts from a point on the PES and uses local curvature to discover new transition states and minima, iterating until a useful set of stationary points is found. Class 2 starts from a minimum and uses heuristics (graph-based transformation rules, artificial forces to bring moieties together, network expansion) to propose new PES points, then follows minimum-energy paths. Class 3 is interactive, combining human chemical intuition with fast resimulation. The article also argues that conformational space for each intermediate is part of the thermodynamic picture, so conformer search intersects with bond-making/breaking discovery.

## Methods

**Literature scope (review; no single new benchmark simulation).** The feature article is a conceptual taxonomy with literature examples. Class 1 covers curvature- or gradient-based explorers (e.g. ADDF/Maeda–Morokuma-type schemes) and similar paths toward transition-state structures; artificial-force (AFIR-style) approaches to biased intermolecular contact appear here when the paper classifies them as curvature- or local-search-driven. Class 2 collects heuristic network generators: graph transformation rules, artificial driving forces, and network expansion. Class 3 is interactive, pairing human choices with quick electronic-structure checks. The authors compare how much automation, heuristic encoding, and expert steering each class requires, and what coverage and cost profiles follow.

**Force-field training and large-scale production MD (blocks 1–2 in a reactive-FF workflow).** **N/A** — no new force-field parameterization and no new production reactive MD dataset are central results; the work is PES- and network-discovery methodology at the QM (and occasionally semiempirical) level, upstream of kMC or ReaxFF-scale dynamics.

## Findings

No single algorithm family universally dominates: curvature-based, heuristic, and interactive approaches are positioned as complementary, with hybrid workflows (rules + human curation + reoptimization of found stationary points) as a practical direction. Comparisons to experiment and to prior computational studies are organized per cited primary work rather than a unified benchmark. Sensitivity to temperature, pressure, and composition enters through selected examples, not a single end-to-end protocol. Limitations the review stresses include field coverage in a fast-moving area and the difficulty of guaranteeing complete networks for large systems. Open directions in the text include better integration of conformer search with bond-making/breaking network expansion, and clearer human–automation trade-offs. **Corpus honesty:** cite figure and equation numbers from the *J. Phys. Chem. A* PDF, not this note alone.
## Limitations

**Not** a benchmarking study for **ReaxFF** or **classical MD**; **reactive MD** practitioners should treat this as **upstream methodology** for **pathway** and **network** discovery. Detailed **algorithm** parameters appear in the **original** references cited within the **review**.

## Relevance to group

Methodological context for **automated pathway** analysis and **reaction network** construction adjacent to **reactive MD** and **kinetic Monte Carlo** workflows discussed elsewhere in computational chemistry notes.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.8b10007](https://doi.org/10.1021/acs.jpca.8b10007) — PDF: `papers/Others/Reaction_path_analysis_JPC_2019.pdf`.

## Related topics

- [[reaxff-family]]
