---
id: paper:2018shin-venue-rsc-cp
type: paper
title: "Development of a ReaxFF reactive force field for lithium ion conducting solid electrolyte Li1+xAlxTi2−x(PO4)3 (LATP)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - material:ceramic-electrolyte
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/C8CP03586E"
year: 2018
authors:
  - "Yun Kyung Shin"
  - "Mert Y. Sengul"
  - "A. S. M. Jonayat"
  - "Wonho Lee"
  - "Enrique D. Gomez"
  - "Clive A. Randall"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "2488af5d342f16b0454b5963f66e3b234357643ae98b9a61d280d53371f5c552"
pdf_path: "papers/Shin_LATP_PCCP_2018_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018shin-venue-rsc-cp -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **PCCP** article develops a **ReaxFF description** for **NASICON-type LATP** (**Li₁₊ₓAlₓTi₂₋ₓ(PO₄)₃**) to study **composition-dependent Li⁺ transport** and **local structural** response in a **solid electrolyte** relevant to **all-solid-state batteries**. **Reactive MD** enables **bond rearrangement** at **interfaces** and **defective** regions beyond harmonic **fixed-bond** models, supporting analysis of **migration mechanisms** across **x** (Al substitution) space. **Adri C. T. van Duin** is corresponding author together with the **Shin**-led parameterization effort. The corpus PDF is an **RSC proof** (`c8cp03586e`).

## Methods

- **ReaxFF parameterization** against **QM / crystallographic** references for **Li–P–O–Ti–Al** chemistry (see article training sets).
- **MD simulations** of **ionic conductivity** metrics and **Li migration** pathways reported in **PCCP**.

## Findings

- **ReaxFF** reproduces key **structural** and **transport** trends for **LATP** compositions explored in the paper.
- Highlights **mechanistic** insight into **Li** motion coupling to **local phosphate** framework distortions.

## Limitations

- **Long-time** **DC conductivity** extraction from **MD** requires **careful finite-size / statistical** analysis.
- **Electrode–electrolyte** interfaces at **operating voltages** may need **additional** validation beyond bulk **electrolyte** fits.

## Relevance to group

A flagship **solid-electrolyte ReaxFF** reference from the **group’s battery materials** line.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1039/C8CP03586E` (manuscript id **C8CP03586E** on the proof header).

## Related topics

- [[reaxff-family]]
