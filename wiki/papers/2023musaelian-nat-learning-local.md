---
id: paper:2023musaelian-nat-learning-local
type: paper
title: "Learning local equivariant representations for large-scale atomistic dynamics"
updated: "2026-04-20"
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
extraction_quality: good
group_affiliation: false
---

<!-- id:paper:2023musaelian-nat-learning-local -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Introduces **Allegro**, a **strictly local**, **equivariant** deep interatomic potential architecture aimed at **accuracy without atom-centered message passing**—targeting **scalable parallelization** and very large systems. The model composes **iterated tensor products** of learned equivariant features (no MPNN-style propagation beyond locality). Reported benchmarks include strong performance on **QM9** and **rMD17**, claims of **out-of-distribution generalization**, and MD of an **amorphous electrolyte** matching **ab initio** behavior; a headline scalability demo reaches **~100 million atoms** (per abstract).

## Methods

Neural potential architecture design; training on quantum-chemistry datasets; MD validation cases including disordered electrolyte; parallel strong-scaling demonstration.

## Findings

Local Allegro models can match or exceed prior **MPNN**/transformer baselines on standard sets while improving **scalability**; large-scale demo illustrates HPC headroom when locality is preserved by construction.


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
