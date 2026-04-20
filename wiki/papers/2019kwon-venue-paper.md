---
id: paper:2019kwon-venue-paper
type: paper
title: "Numerical simulations of yield-based sooting tendencies of aromatic fuels using ReaxFF molecular dynamics (uncorrected proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2019.116545"
year: 2019
authors:
  - "Hyunguk Kwon"
  - "Sharmin Shabnam"
  - "Adri C. T. van Duin"
  - "Yuan Xuan"
venue: "Fuel (uncorrected proof PDF in corpus)"
pdf_sha256: "b1287861455fc265637f719bb1545bd6eade01ad36580bb6a61a5df345b58acc"
pdf_path: "papers/Kwon_Fuel_2019_proof.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2019kwon-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Corpus note:** this slug registers an **uncorrected proof** (`papers/Kwon_Fuel_2019_proof.pdf`). The **same Fuel article** is curated on **`[[2019kwon-fuel-correct-numerical-simulations]]`** (`papers/Kwon_Fuel_2019_online.pdf`). The work develops a **ReaxFF MD** workflow to estimate **Yield Sooting Index (YSI)**-style sooting propensity for **aromatic** fuels using a **multi-stage** procedure intended to mirror experimental and continuum **YSI** definitions. **Toluene** and **phenol** serve as proof-of-concept aromatics with well-studied chemistry: simulations recover **ring-retaining vs carbon-loss** pathways (including **CO** release motifs for **phenol**) and assemble a quantitative **YSI** construction from trajectory chemistry with **reasonable agreement** to measured **YSI** for those cases.

## Methods

**Reactive MD** with **ReaxFF**; **multi-stage** protocol aligned with the **YSI** concept; benchmarks on **toluene** and **phenol** with comparison of **ReaxFF-derived** indices to **experimental YSI**—identical scientific content to **`[[2019kwon-fuel-correct-numerical-simulations]]`**.

## Findings

**ReaxFF** captures **qualitative** soot-relevant chemistry consistent with known pathways for the chosen fuels; the **YSI mapping** yields values in **reasonable agreement** with experiment for the demonstration set, supporting **relative ranking** of sooting tendency when detailed mechanisms are unavailable.

## Limitations

**Proof** layout and pagination differ from the **version of record**; cite **`[[2019kwon-fuel-correct-numerical-simulations]]`** for stable figure/table references.

## Relevance to group

Duplicate corpus path for **Penn State** / **van Duin** **sooting** workflow traceability.

## Citations and evidence anchors

Prefer **`[[2019kwon-fuel-correct-numerical-simulations]]`**. DOI: https://doi.org/10.1016/j.fuel.2019.116545

## Related topics

- [[2019kwon-fuel-correct-numerical-simulations]]
- [[reaxff-family]]
