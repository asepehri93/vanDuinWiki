---
id: paper:2016choudhary-venue-untitled
type: paper
title: "Evaluation and comparison of classical interatomic potentials through a user-friendly interactive web interface"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - task:validation
  - task:software
  - scale:atomistic
paper_keywords:
  - keyword:method-development
  - keyword:validation-experiment
  - keyword:lammps
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1038/sdata.2016.125"
year: 2016
authors:
  - "Kamal Choudhary"
  - "Faical Yannick P. Congo"
  - "Tao Liang"
  - "Chandler Becker"
  - "Richard G. Hennig"
  - "Francesca Tavazza"
venue: "Sci. Data"
pdf_sha256: "3d725d5b6b99b4b8658ae1f0c602b1220ae71ff36a1d15cbfbaff18b7bb5e976"
pdf_path: "papers/ReaxFF_others/Choudhary_Convex_Hull_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016choudhary-venue-untitled -->

## Summary

Choudhary *et al.* present a **Scientific Data** descriptor (DOI `10.1038/sdata.2016.125`) that releases a **high-throughput database** and **interactive web interface** for comparing a broad library of **classical interatomic potentials**—spanning **EAM**, **MEAM**, **Tersoff**, **Stillinger–Weber**, **AIREBO**, **COMB**, **ReaxFF**, and related families—against **Materials Project** **density functional theory** references and selected **experimental** benchmarks. The published descriptor reports **3248** tabulated calculations covering **1471** materials and **116** force fields (with the database continuing to grow), with emphasis on **0 K** **energetics** (including **convex hull** placement relative to DFT) and **elastic constants** extracted from standardized **LAMMPS** workflows. By packaging both **tabular data** and **visual analytics**, the authors aim to make **force-field quality** a **reproducible**, **versioned** community exercise rather than an ad hoc literature comparison, which is particularly relevant for **reactive** potentials such as **ReaxFF** where transferability claims are often system-specific.

## Methods

### High-throughput benchmarking workflow (as described)

- **Code path:** **LAMMPS**-driven **static** lattice workflows at **0 K** to compute **elastic tensors** and related **energetics** for many **crystal prototypes** × **force-field** parameterizations.
- **Reference QM:** Compare to **Materials Project** **DFT** entries for the same chemistries/structures where available; optionally compare selected elastic data to **experiment** when present in the dataset.
- **Convex hulls:** Provide **convex-hull** comparisons between **FF** and **DFT** to summarize **relative phase stability** predictions across competing structures.
- **Dissemination:** Release **tabular data**, **plots**, and **open scripts** via the **Scientific Data** descriptor (including the **interactive** website URL printed in the article PDF).

### MD application (atomistic dynamics)

**N/A — finite-temperature production MD** is not the dataset’s core; the descriptor emphasizes **0 K** **static** evaluations and standardized elastic scripts.

### Force-field training

**N/A — not a parameterization paper**; it is a **comparative evaluation** of many existing parameter files.

### Static QM / DFT

**N/A as a new QM methods contribution**; the work **consumes** **Materials Project**-style **DFT** reference energies/structures as benchmarks.

## Findings

Across the compiled landscape, **no single potential family** uniformly dominates all materials or properties: systematic **under- and over-stabilization** patterns appear in both **energetics** and **elasticity**, and **PCA** reveals structured correlations among tensor components that would be invisible in scalar error averages. For **ReaxFF** specifically, inclusion in the same comparative framework situates **reactive** models alongside **fixed-bond** alternatives, reinforcing that **benchmarks** must be interpreted with chemistry- and phase-specific context. The open release is positioned as enabling **continuous integration**-style testing as parameter files evolve, supporting both **method developers** and **application** groups who need traceable decisions when selecting **FF** classes for production simulations. For **vanDuinWiki** workflows, the database is most valuable as a **sanity-check** companion when judging whether a **ReaxFF** **parameterization** is an outlier relative to other **reactive** or **classical** models on the same **crystal** **prototype**.

## Limitations

Temperature-dependent properties are flagged as future extensions; elastic constants come from a specific LAMMPS elastic script—users should validate for their symmetry and stress conventions.

## Relevance to group

PSU (Liang) co-authorship; directly references **ReaxFF** within a multi-FF benchmarking ecosystem useful for parameterization QA.

## Citations and evidence anchors

- DOI: [10.1038/sdata.2016.125](https://doi.org/10.1038/sdata.2016.125)

## Related topics

- [[reaxff-family]]
