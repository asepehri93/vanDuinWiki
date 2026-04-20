---
id: paper:2016kumar-j-phys-chem-jz6b00091
type: paper
title: "Interface-induced renormalization of electrolyte energy levels in magnesium batteries"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:dft-static
  - task:application
  - material:metal-surface
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.6b00091"
year: 2016
authors:
  - "Nitin Kumar"
  - "Donald J. Siegel"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "42a78b311ad96dfef6f4c5780a74930ffe54559ba8a15c1825335d72bf1cbad4"
pdf_path: "papers/Others/Mg_Kumar.pdf"
extraction_quality: good
group_affiliation: false
---

<!-- id:paper:2016kumar-j-phys-chem-jz6b00091 -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **JPCL** study uses **many-body perturbation theory (G0W0)** to quantify how **electrode–electrolyte interfaces** shift **HOMO/LUMO levels** of **common organic solvents** on **model Mg-battery-relevant electrodes**, arguing that **interfacial electrostatics** can **narrow HOMO–LUMO gaps** by up to **~25%** for **high-dipole** molecules relative to gas-phase references. The central implication is that **high-throughput electrolyte screening** based on **isolated-molecule windows** may **overestimate stability**, because **electrode-induced renormalization** accelerates **reductive/oxidative decomposition** pathways when gaps shrink.

## Methods

- **DFT + G0W0** calculations on **surface–solvent** configurations representative of Mg anode materials discussed in the paper.

## Findings

- **Interface interactions** materially **shift frontier orbital energies** vs vacuum/PCM benchmarks in the reported datasets.
- **Large dipole solvents** show the strongest **gap narrowing** under the interaction models used.
- Authors recommend incorporating **interfacial corrections** into **electrolyte screening** workflows for **multivalent** chemistries.


## Limitations

- **Idealized surfaces** and **static electronic structure** omit **explicit dynamics**, **SEI chemistry**, and **entropic** contributions.
- Not a **ReaxFF** paper; it complements reactive MD studies by supplying **QM-level** electronic benchmarks.

## Relevance to group

Provides **QM context** for **electrolyte stability** adjacent to the corpus’s many **battery-interface ReaxFF** efforts.

## Citations and evidence anchors

- Abstract in `papers/Others/Mg_Kumar.pdf`; **DOI:** `10.1021/acs.jpclett.6b00091`.

## Related topics

- [[reaxff-family]]