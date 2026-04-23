---
id: paper:2024zhu-progress-in-advances-developing
type: paper
title: "Advances in developing cost-effective carbon fibers by coupling multiscale modeling and experiments: A critical review"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:ml-atomistic
  - method:reaxff
  - scale:multiscale
  - task:review
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reaxff-application
  - keyword:machine-learning-potential
candidate_tags: []
source_refs: []
doi: "10.1016/j.pmatsci.2024.101329"
year: 2024
authors:
  - "Jiadeng Zhu"
  - "Zan Gao"
  - "Qian Mao"
  - "Yawei Gao"
  - "Ya Li"
  - "Xin Zhang"
  - "Qiang Gao"
  - "Mengjin Jiang"
  - "Sungho Lee"
  - "Adri C. T. van Duin"
venue: "Prog. Mater. Sci. 146 (2024) 101329"
pdf_sha256: "df9c4ad6ad107124ec3eca0b5633e84ba68b116d6fbf795bf4640fab31cde248"
pdf_path: "papers/Zhu_Mao_Progress_MatSci_Carbon_Fibers_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2024zhu-progress-in-advances-developing -->

## Summary

This is a **critical review** of strategies to lower the cost of **carbon fibers (CFs)** while meeting property targets, emphasizing how **experiments** are combined with **multiscale computational modeling** (from **density functional theory** and **reactive molecular dynamics** such as **ReaxFF**, to **coarse-grained MD**, **finite-element** style continuum models, and **machine learning**). The article surveys precursor families, spinning and conversion routes (stabilization, carbonization, graphitization), and how computation is used to rationalize reaction pathways, structure evolution, and structure–property links.

## Methods

The article is a **literature synthesis**, not a single primary modeling study. It organizes prior work by **precursor chemistry** (e.g., PAN- and pitch-based routes, cellulosic and lignin-based alternatives, and related biopolymer approaches discussed in the review), **processing levers** (spinning modality, draw ratio, thermal schedules, tension), and **computational methodology** categories: **DFT** for electronic-level insight where applicable; **atomistic MD** with **reactive force fields (ReaxFF)** for bond-breaking chemistry during oxidative stabilization and carbonization; **multiscale coupling** (e.g., feeding atomistic data into continuum or FEA representations); and **ML** for mapping high-dimensional process–structure–property relationships when large datasets exist.

## Findings

- Final CF **mechanical and transport properties** (tensile modulus/strength, thermal and electrical conductivity, etc.) depend jointly on **precursor architecture**, **processing history**, **carbon crystallinity** and **defect content**, as summarized in the review’s conclusions.
- **Multiscale modeling** (explicitly including **DFT**, **ReaxFF MD**, **CGMD**, etc., in the review’s framing) is presented as a way to connect **atomistic chemistry and microstructure** to **engineering-scale** behavior when paired with experiments.
- The outlook highlights **remaining cost barriers** for commodity-scale CF use, and points to **integrated experimental–computational** workflows—including **ReaxFF** developments for **C/H/O/N/S polymer chemistry** and examples such as **lignin chemistry** and **ML-oriented training data**—as routes to screen precursors and processes more efficiently.

## Limitations

- As a **review**, quantitative benchmarks are **second-hand** from cited primary sources; readers should consult the original studies for parameters and validation.
- Coverage is **corpus- and field-scoped** (cost-focused CF research), not an exhaustive global market or manufacturing survey.

## Relevance to group

Adri C. T. van Duin is a co-author; the review foregrounds **ReaxFF** and related **reactive MD** as tools for **carbonization chemistry** alongside broader multiscale and ML threads relevant to materials informatics.

## Citations and evidence anchors

- DOI: [10.1016/j.pmatsci.2024.101329](https://doi.org/10.1016/j.pmatsci.2024.101329)

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
