---
id: paper:2023musaelian-nat-learning-local
type: paper
title: "Learning local equivariant representations for large-scale atomistic dynamics"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ml-atomistic
  - domain:methods-software
  - method:ml-potential
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1038/s41467-023-36329-y"
year: 2023
authors:
  - "Albert Musaelian"
  - "Simon Batzner"
  - "Anders Johansson"
  - "Lixin Sun"
  - "Cameron J. Owen"
  - "Mordecai Kornbluth"
  - "Boris Kozinsky"
venue: "Nat. Commun. 14, 579 (2023)"
pdf_sha256: "c20c1c4fb543ce9994d45c2ef56059508c9f8d95289f3c00f01e73459518e2ab"
pdf_path: "papers/Others/Allegro_ML_2023.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023musaelian-nat-learning-local -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Machine-learned interatomic potentials (MLIPs) now compete with empirical force fields and tight-binding models for **large-scale molecular dynamics**, but many graph neural network architectures rely on **multi-hop message passing** that complicates **massive parallelization**. **Allegro**, introduced in this **Nature Communications** article (**Musaelian**, **Batzner**, **Johansson**, **Sun**, **Owen**, **Kornbluth**, **Kozinsky**), is a **strictly local**, **E(3)-equivariant** model that builds **iterated tensor products** of learned features without propagating information beyond a fixed **local neighborhood**. The design targets **GPU-friendly** parallelism and very long trajectories for **condensed-phase** systems. Reported evaluations span **QM9** and **rMD17** benchmarks, claims of **out-of-distribution** robustness on selected splits, and an **amorphous electrolyte** example where Allegro-driven MD tracks **ab initio** references; a scaling study highlights simulations approaching **100 million atoms** in the abstract’s headline demonstration.

## Methods

### Supervised training on QM data (C)

**E/F** labels from **electronic-structure** calculations; **atomic numbers** + **positions** mapped to **E(3)-equivariant** features (**irreps**).

### Architecture (Allegro)

**Local** **tensor-product** iterations replace deep **message-passing** while preserving **symmetry** (details in article/SI).

### Validation suite

**QM9** / **rMD17** benchmarks; **OOD** splits; **amorphous electrolyte** **MD** stability; **strong-scaling** to ~**100M atoms** (headline HPC demo).

## Findings

### Accuracy vs baselines

Competitive or better than **MPNN**/**transformer** potentials on reported tasks with improved **large-cell** scaling due to **strict locality**.

### Electrolyte case study

Matches **ab initio** **structure/dynamics** when training covers the chemistry.

### Scalability vs coverage

**100M-atom** run demonstrates **throughput**; **generalization** still depends on **training corpus** breadth and **UQ**. The main text emphasizes that **strict locality** avoids **multi-hop** graph propagation costs and improves **GPU** strong scaling relative to deeper **message-passing** graph networks on large **condensed-phase** cells.

**Compared** to **MPNN** baselines on the **rMD17**-style **reaction** **surfaces** and the **amorphous** **electrolyte** case, **Allegro** **reproduces** **ab initio** **forces** within the **published** **tolerances** while **reducing** **cost** at **extreme** **NVT**-style **sampling**—a **sensitivity** to **out-of-distribution** **chemistry** remains, which the **authors** **frame** as a **limitation** for **reactive** **interfaces**; **outlook** toward **battery** **kinetics** requires **broader** **datasets** than the **showcase** **alloys**; **citations** should use the **peer-reviewed** **DOI** `pdf_path` (not this **wiki** for **new** **numbers**).



## Limitations

Transfer to reactive, multi-species battery interfaces still depends on dataset breadth and uncertainty quantification—architecture choices alone do not guarantee chemistry coverage.

## Relevance to group

Provides MLIP context adjacent to corpus work on **Li systems** and **ReaxFF**; useful cross-reference for hybrid **QM/ML/FF** workflows.

## Citations and evidence anchors

https://doi.org/10.1038/s41467-023-36329-y — Main text (~pp. 1–2) states architecture premise and benchmark claims.

## Reader notes (navigation)

- **Cluster:** [[theme-ml-atomistic-potentials]]; **debate:** [[reaxff-vs-mlip-accuracy]].  
- **Frozen eval:** ML1 gold in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).

## Related topics

- [[2023li-venue-paper]]
- [[theme-ml-atomistic-potentials]]
