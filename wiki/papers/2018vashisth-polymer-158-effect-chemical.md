---
id: paper:2018vashisth-polymer-158-effect-chemical
type: paper
title: "Effect of chemical structure on thermo-mechanical properties of epoxy polymers: Comparison of accelerated ReaxFF simulations and experiments"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - material:polymer-organic
  - method:reaxff
  - task:experiment-integrated
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.polymer.2018.11.005"
year: 2018
authors:
  - "Aniruddh Vashisth"
  - "Chowdhury Ashraf"
  - "Charles E. Bakis"
  - "Adri C. T. van Duin"
venue: "Polymer"
pdf_sha256: "1e523d319a9ee43282c071af159e307f727f4d78bf2f2ade50d74598c7b503be"
pdf_path: "papers/Vashisth_Polymer_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018vashisth-polymer-158-effect-chemical -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

The authors apply an **accelerated ReaxFF** workflow—supplying energy comparable to **reaction barriers** so that **slow epoxy crosslinking** events occur on **MD-accessible** timescales—to build **atomistic networks** from **bisphenol-A epoxide** cured with **three classes of amines** (aromatic, cycloaliphatic, aliphatic). **Simulated thermo-mechanical** properties are compared with **experiments**, highlighting how **curing-agent chemistry** shapes **local heterogeneity** (notably for **cyclic** amines) and **strain-rate sensitivity** (stronger for **aliphatic** systems). **Adri C. T. van Duin** is a corresponding author with **Penn State** engineering coauthors.

## Methods

- **Accelerated ReaxFF MD** to achieve **C–N crosslinking** between **epoxide** and **amine** moieties in finite cells.
- **Virtual mechanical testing** and **thermal** protocols paired with **experimental** benchmarks (see **Polymer** article for metrics).

## Findings

- **Good correlation** between **simulation** and **experiment** for the **thermo-mechanical** trends compared in the study.
- **Cyclic** curing agents yield **heterogeneous** local structure that **annealing** can partly homogenize; **aliphatic** networks show more **strain-rate** dependence than **aromatic**-cured analogs in the simulations reported.

## Limitations

- **Accelerated dynamics** changes **pathway competition** relative to **room-temperature** processing; **quantitative** cure kinetics remain **illustrative**.
- **Force-field** scope limits **transfer** to other **epoxide/amine** chemistries without **re-parameterization**.

## Relevance to group

Demonstrates **group ReaxFF** on **thermoset cure** with **side-by-side validation**, relevant to **polymer composites** and **industrial** processing questions.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.polymer.2018.11.005` (`papers/Vashisth_Polymer_2018.pdf`).

## Related topics

- [[reaxff-family]]
