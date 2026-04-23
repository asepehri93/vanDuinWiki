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
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019ganna-shchygol-j-chem-theor-reaxff-parameter -->

## Evidence and attribution

!!! note "Authority of statements"

    Maintainer catalog (SI/galley/proof PDF roles): https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The paper **benchmarks three global optimization strategies** for **ReaxFF parameter fitting**—**covariance matrix adaptation evolution strategy (CMA-ES)**, **Monte Carlo force-field optimizer (MCFF)**, and a **genetic algorithm (OGOLEM)**—on **three literature training sets**, repeating runs with **different random seeds** and **initial guesses**. **Single-shot** optimizations are shown to be **unreliable**: **poor** or **premature convergence** appears **often**, motivating **multi-start** workflows and **careful** method choice (**GA** mitigates **local-minimum** traps best in their statistics; **CMA-ES** sometimes reaches **lowest** errors but **not systematically**). The study also analyze **numerical noise** in training data—reduced by using **unambiguous geometry optimizations**—and note **many near-optimal parameter vectors**, warning against **overfitting**. **Adri C. T. van Duin** coauthors with **Ghent / SCM** colleagues. Stochastic global search means identical training sets can admit many near-degenerate parameter vectors, so workflow choices (multi-start fits, noise control on **QM** training points, skepticism toward single-run “best” vectors) matter as much as chemistry; authoritative tables and diagnostics remain in the **JCTC** article and **SI**.

## Methods

### ReaxFF training data and QM hygiene (A)

Optimizations minimize **ReaxFF error** on **QM-derived training sets** (energies, forces, and related targets as defined per benchmark—see **JCTC** article and **Supporting Information**). The study stresses **numerical noise** in training entries and shows it can be reduced by using **unambiguous geometry-optimized** structures for data that feed the objective—**ill-conditioned** or **ambiguous** QM points inflate parameter **scatter** across repeats.

### Global optimizers and replication protocol (A, continued)

Three **global** strategies are compared on **three literature ReaxFF training sets**: **covariance matrix adaptation evolution strategy (CMA-ES)**, **Monte Carlo force-field optimizer (MCFF)**, and **OGOLEM** (**genetic algorithm**). Each method is run **many times** with **different random seeds** and **initial parameter guesses** to quantify **non-reproducibility**, **premature convergence**, and **local-minimum** trapping—**single-shot** runs are explicitly discouraged.

### Molecular dynamics in optimization loops (B)

Large-scale **production** **reactive MD** is **not** the deliverable; any short trajectories mentioned serve **objective/gradient** evaluation during **parameter** updates—see **JCTC** for whether test MD appears.

**MD bookkeeping for optimization workflows.** When the study invokes short **molecular dynamics** sanity checks alongside **ReaxFF** **parameter** updates, those trajectories use **periodic** **supercells** matched to the **training** geometries in **JCTC**/SI, **NVT** **thermal** sampling at stated **K** values, **equilibration**/**production** segments measured in **ps**, and integration **timesteps** in **fs** as listed for each case. **Thermostat:** whichever **Berendsen**/**Nose–Hoover**/**Langevin** coupling is documented for that evaluator. **Barostat / pressure:** **N/A** unless a benchmark explicitly used **NPT** with a **Parrinello–Rahman** **barostat**. **External electric field:** **N/A**. **Replica / metadynamics:** **N/A** for the global **CMA-ES** / **MCFF** / **genetic algorithm** fits highlighted here.

## Findings

### Mechanisms (why fits fail or scatter)

**Seed sensitivity** and **multiple near-degenerate parameter vectors** with similar error are common; **GA (OGOLEM)** tends to **avoid local minima** more robustly in their statistics, while **CMA-ES** sometimes reaches the **lowest** errors but **not systematically** across cases. **Noise** in QM training data and **training-set design** strongly affect whether reported minima are **meaningful** vs **overfit**.

### Limitations

Conclusions are **empirical** on **three** shared corpora; other **elements** or **reaction classes** may reorder **method** rankings. **Global optimization** cost scales with **training-set** size and **parallel QM** throughput.

### Future-oriented guidance (from the article)

The abstract recommends **defaults** and **practice guidelines** for **CMA-ES**, **MCFF**, and **GA** users, and frames **multi-start** workflows plus **training-set refinement** as the path to **stable** production parameters.

## Limitations

- Results are **empirical** on the **chosen** training sets; **other chemistries** may reorder **method** rankings.
- **Global optimization** cost scales with **training-set** size and **parallel** **QM** evaluation throughput.

## Corpus artifacts

The ingest may also list an **extensionless** duplicate path (`papers/Shchygol_JCTC_2019_online`) for the same article; **`papers/Shchygol_JCTC_2019.pdf`** is the **canonical** file for **pagination** and **figures**.

## Relevance to group

A **methodological** reference for **ReaxFF developers** at **Penn State** and **partner** software groups (**parameterization culture** and **reproducibility**).

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jctc.9b00769` (`papers/Shchygol_JCTC_2019.pdf`).

## Related topics

- [[reaxff-family]]
