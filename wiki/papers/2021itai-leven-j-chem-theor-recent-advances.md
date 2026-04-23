---
id: paper:2021itai-leven-j-chem-theor-recent-advances
type: paper
title: "Recent Advances for Improving the Accuracy, Transferability, and Efficiency of Reactive Force Fields"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:methods-software
  - method:reaxff
  - method:ereaxff
  - task:review
candidate_tags: []
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reaxff-parameterization
source_refs: []
doi: "10.1021/acs.jctc.1c00118"
year: 2021
authors:
  - "Itai Leven"
  - "Hongxia Hao"
  - "Songchen Tan"
  - "Xingyi Guan"
  - "Katheryn A. Penrod"
  - "Dooman Akbarian"
  - "Benjamin Evangelisti"
  - "Md Jamil Hossain"
  - "Md Mahbubul Islam"
  - "Jason P. Koski"
  - "Stan Moore"
  - "Hasan Metin Aktulga"
  - "Adri C. T. van Duin"
  - "Teresa Head-Gordon"
venue: "J. Chem. Theory Comput."
pdf_sha256: "90c26d661109de5d945af3318146c7f02306148742cc6aa1550afd86465f94a9"
pdf_path: "papers/Leven_JCTC_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021itai-leven-j-chem-theor-recent-advances -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *J. Chem. Theory Comput.* Perspective identified by `doi`, `title`, and `pdf_path`. Alternate **proof** PDF: **`[[2021leven-x-recent-advances]]`** (non-primary duplicate).

## Summary

Reactive force fields such as **ReaxFF** enable long-time reactive simulations on large atom counts, but accuracy, transferability, and cost remain active research fronts. This **JCTC Perspective** surveys recent improvements: reformulations of **charge equilibration** to reduce unphysical long-range charge transfer; **explicit-electron (eReaxFF)** routes; energy-conservation analysis for coupled charge dynamics; **hybrid** models that embed reactive subregions in fixed-bond regions; and **algorithmic** acceleration (extended-Lagrangian charge dynamics, preconditioned charge solvers, **LAMMPS** performance and **KOKKOS**-related integration paths). The text is a **citation map**, not a single new benchmark: readers must follow references for numerical settings, ensembles, and validation for each chemistry.

## Methods

The manuscript is a **Perspective** (synthetic review), not one unified simulation or fitting campaign. Blocks below follow `AGENTS.md` order; the substantive “methods” of the paper are the **review scope** in **block 4**.

### 1 — MD application (atomistic dynamics)

**N/A —** this publication does not define one canonical LAMMPS (or other) **production** protocol. It **cites and organizes** how reactive MD (including LAMMPS-centric workflows) is used across the field and discusses integration and throughput bottlenecks; for timesteps, cutoffs, ensembles, and system sizes, use each **primary** work referenced in the Perspective.

### 2 — Force-field training

**Survey content (not a new global fit).** The article summarizes strategies around **ReaxFF-class** and related **reactive** parameterizations: mitigations for classical **EEM/QEq** failure modes, routes toward **eReaxFF**, and **hybrid** Hamiltonians. Training objectives, QM levels, and optimization software appear **via citations** to original parametrization papers—not as a single new **ffield** file produced in the Perspective.

### 3 — Static QM / DFT

**N/A** as a standalone DFT “methods results” section. Referenced **DFT** and higher-level QM studies underpin **cited** force-field and MLIP training papers; the Perspective does not report a unified DFT protocol of its own.

### 4 — Reviews, perspectives, or non-simulation studies

**Literature scope and comparison stance:** the authors structure the field by **bottleneck type**—chemistry **vs** charge dynamics **vs** **sampling** or **wall-clock** limits—and point to **software** paths (**LAMMPS**, **ReactMD**, preconditioning, KOKKOS where discussed) for large electrochemical-like cells. **Reproducibility:** every quantitative protocol must be taken from a **cited** primary source. **Non-primary layout:** pagination may differ from a **proof** duplicate ([[`2021leven-x-recent-advances`]]); prefer this **VOR**-linked `pdf_path` for stable locators when citing page numbers.

## Findings

The Perspective attributes persistent weaknesses of classical **EEM/QEq** paired with ReaxFF (e.g. **over-delocalized** **charge** **transfer** in some long-range or metallic-like situations) to limitations of point-charge equilibration, and it summarizes **community** mitigations (modified charge schemes, **hybrid** **embeddings**). It positions **eReaxFF**-related ideas as **higher-fidelity** for selected **redox** problems while noting **calibration** cost. **Software** discussion ties to **practical** **LAMMPS**-family workflows, consistent with coauthor experience in **scalable** **reactive** **dynamics**.

**Comparisons:** the text contrasts **invariant** graph-style MLIPs and **symmetry-aware** architectures **referentially**, not with one table owned by the Perspective. **Practical guidance:** treat failures as **chemistry-limited**, **charge-limited**, or **sampling/throughput-limited**, then branch to the cited **tool** lines. **Limitations (authored stance):** the article ages as **MLIP** and charge models evolve; it is an **orientation** document, not a universal parameter recipe. **Corpus / KB honesty:** peer-reviewed content is in `pdf_path`; a **proof** **PDF** may exist as [[`2021leven-x-recent-advances`]]; **definitive** page **figures** for external **citation** should follow the **publisher** **copy**.

## Limitations

Perspective **scope**—**numerical** benchmarks, **parameter** domains, and post-publication **code** should be confirmed from **primary** studies. **Proof** **PDFs** can differ in **layout** from this file.

## Relevance to group

**van Duin** coauthored overview of the **ReaxFF / ReactMD** ecosystem; pairs with application pages on **batteries**, **oxides**, and **organics**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.jctc.1c00118](https://doi.org/10.1021/acs.jctc.1c00118) (`papers/Leven_JCTC_2021.pdf`).

## Reproducibility and corpus locators

This note documents where to find primary evidence in-repo; it does not add new scientific claims beyond the cited publication.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, **timestep**, ensembles, kinetics), use the peer-reviewed PDF and SI as authoritative; this wiki summarizes for navigation and retrieval.

## Related topics

- [[2021leven-x-recent-advances]]
- [[2019leven-j-phys-chem-gem-coarse-grained]]
- [[reaxff-family]]
