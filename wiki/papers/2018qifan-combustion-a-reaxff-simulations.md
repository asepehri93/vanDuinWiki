---
id: paper:2018qifan-combustion-a-reaxff-simulations
type: paper
title: "ReaxFF simulations of petroleum coke sulfur removal mechanisms during pyrolysis and combustion"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.combustflame.2018.09.005"
year: 2018
authors:
  - "Qifan Zhong"
  - "Qiuyun Mao"
  - "Jin Xiao"
  - "Adri C. T. van Duin"
  - "Jonathan P. Mathews"
venue: "Combust. Flame"
pdf_sha256: "b5a319b4d56e0c8b2d9fdba93ebaedc8e17f44b5b5d73426a8a6a16afadd73cb"
pdf_path: "papers/Zhong_CombFlame_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018qifan-combustion-a-reaxff-simulations -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF reactive MD** is applied to **petroleum coke** models to probe **sulfur removal** chemistry during **pyrolysis** and **combustion** scenarios, connecting **atomistic pathways** to the **high-temperature** **S** release problem relevant to **emissions** and **coke utilization**. The work sits at the intersection of **fuel chemistry**, **heteroatom (S) elimination**, and **reactive simulation** of **carbonaceous** matrices. **Adri C. T. van Duin** is a coauthor alongside **Mathews** group **combustion** expertise.

## Methods

- **ReaxFF MD** with **elevated-temperature** protocols to accelerate **C–S** and **S–O/H** reaction events within tractable timescales.
- **Structural / species** tracking for **S-containing** fragments and **gas-phase** products as defined in the article.

## Findings

- Identifies **mechanistic families** for **sulfur elimination** under **pyrolysis vs combustion** conditions (see paper figures for species timelines).
- Provides **ReaxFF-based** interpretation complementary to **TG-MS**-style experimental narratives referenced in the title/abstract framing.


## Limitations

- **Petroleum coke** structural diversity means **model carbon** matrices are **simplified**; **quantitative** yields are **illustrative**.
- **High-T MD** requires careful reading of **temperature** and **heating** protocols when comparing to **experiment**.

## Relevance to group

Extends **ReaxFF** into **heavy fuel / coke** **S chemistry** relevant to **combustion** and **environmental** impacts.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.combustflame.2018.09.005` (`papers/Zhong_CombFlame_2018.pdf`).

## Related topics

- [[reaxff-family]]
