---
id: paper:2019ganna-shchygol-j-chem-theor-reaxff-parameter
type: paper
title: "ReaxFF Parameter Optimization with Monte-Carlo and Evolutionary Algorithms: Guidelines and Insights"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:monte-carlo
  - method:reaxff
  - task:parameterization
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.9b00769"
year: 2019
authors:
  - "Ganna Shchygol"
  - "Alexei Yakovlev"
  - "Tomáš Trnka"
  - "Adri C. T. van Duin"
  - "Toon Verstraelen"
venue: "J. Chem. Theory Comput."
pdf_sha256: "18acd9bfa94d26e0924b0a4777ff8c4d7a5b4295b343422f66905110bb49090f"
pdf_path: "papers/Shchygol_JCTC_2019.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019ganna-shchygol-j-chem-theor-reaxff-parameter -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

The paper **benchmarks three global optimization strategies** for **ReaxFF parameter fitting**—**covariance matrix adaptation evolution strategy (CMA-ES)**, **Monte Carlo force-field optimizer (MCFF)**, and a **genetic algorithm (OGOLEM)**—on **three literature training sets**, repeating runs with **different random seeds** and **initial guesses**. **Single-shot** optimizations are shown to be **unreliable**: **poor** or **premature convergence** appears **often**, motivating **multi-start** workflows and **careful** method choice (**GA** mitigates **local-minimum** traps best in their statistics; **CMA-ES** sometimes reaches **lowest** errors but **not systematically**). The authors also analyze **numerical noise** in training data—reduced by using **unambiguous geometry optimizations**—and note **many near-optimal parameter vectors**, warning against **overfitting**. **Adri C. T. van Duin** coauthors with **Ghent / SCM** colleagues.

## Methods

- **Systematic comparisons** of **CMA-ES**, **MCFF**, and **OGOLEM** on shared **ReaxFF** training corpora.
- **Replication study** across **seeds** and **initial parameters**; **noise** analysis on **training** entries.

## Findings

- **Optimization** outcomes are **seed-sensitive**; **best practices** and **default settings** per method are recommended in the article.
- **Training-set design** and **noise control** materially affect **stability** of fitted **parameters** and **interpretability** of **error** metrics.

## Limitations

- Results are **empirical** on the **chosen** training sets; **other chemistries** may reorder **method** rankings.
- **Global optimization** cost scales with **training-set** size and **parallel** **QM** evaluation throughput.

## Relevance to group

A **methodological** reference for **ReaxFF developers** at **Penn State** and **partner** software groups (**parameterization culture** and **reproducibility**).

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jctc.9b00769` (`papers/Shchygol_JCTC_2019.pdf`).

## Related topics

- [[reaxff-family]]
