---
id: paper:2007chenoweth-venue-propene-combust-details-fig1
type: paper
title: "Propene oxidation pathways from ReaxFF NVT-MD (Scheme A, supporting information)"
updated: "2026-04-20"
confidence: med
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:nvt-simulation
  - keyword:supporting-information
  - keyword:reactive-md
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - method:reactive-md-generic
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2007
authors:
  - "Kimberly Chenoweth"
  - "Adri C. T. van Duin"
  - "William A. Goddard III"
venue: "Supporting information (manuscript supplement)"
pdf_sha256: "1bf1f59c244e7a8980860ab13e057fd437be1880b6315748a3ad239dd5632492"
pdf_path: "papers/CHO_supplements/ReaxFF_CHO_pathways.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2007chenoweth-venue-propene-combust-details-fig1 -->

## Evidence and attribution

!!! note "Authority of statements"

    This page summarizes the **supporting figure/scheme** PDF. Time labels in the extract are reproduced as **printed in the source**; interpret chemistry with the **figure** in the PDF.

## Summary

This supporting-information PDF presents **Scheme A: propene oxidation pathways** observed during **ReaxFF NVT molecular dynamics** simulations, for the manuscript “A ReaxFF Reactive Force Field for Molecular Dynamics Simulations of Hydrocarbon Oxidation” (Chenoweth, van Duin, Goddard). The extract records a sequence of species and time tags along the scheme as extracted from the figure text (formatting is dense in plain text).

## Methods


The supporting figure records oxidation pathways observed in ReaxFF molecular dynamics in the NVT ensemble using the C/H/O combustion parameterization developed for the parent manuscript on hydrocarbon oxidation. Species along each pathway are tagged with times in picoseconds as printed on Scheme A (for example the extract lists steps such as O\(_2\) at 194.74 ps, subsequent adducts at 202.30 ps and 215.66 ps, and later events past 500 ps, with dense concatenation in plain text). Pathways are reconstructed from simulation trajectories and laid out as a reaction graph rather than as a single scalar rate measurement.

**MD protocol (scheme-level only):** **molecular dynamics** with **ReaxFF** in the **NVT** ensemble (as captioned on Scheme A). **N/A — MD package name**; **N/A — atom counts / box vectors** on this one-page SI; **N/A — PBC** details; **Timestep:** **N/A — \(\Delta t\)** not printed on Scheme A; **Duration / stages:** pathway labels include **picosecond** timestamps (**194.74 ps**, **202.30 ps**, **215.66 ps**, events past **500–1400 ps** in the figure text) without a single continuous **production** segment length; **N/A — thermostat** parameters; **Barostat:** **N/A — NPT** (not stated for this scheme); **Temperature:** **N/A — canonical T** on the figure page—see parent article; **Pressure / stress:** **N/A**; **Electric field:** **N/A**; **Replica / enhanced sampling:** **N/A**. Grounding: `papers/CHO_supplements/ReaxFF_CHO_pathways.pdf`, `normalized/extracts/2007chenoweth-venue-propene-combust-details-fig1_p1-2.txt`.

## Findings

Scheme A maps a **multi-step** propene oxidation network with **species tagged at picosecond times** along the path (e.g. O\(_2\) at **194.74 ps**, later oxygenated adducts through **500+ ps**, and late **CO\(_2\)** / **H\(_2\)O**-related steps past **500–1400 ps** in the figure text). The diagram is evidence that **NVT** ReaxFF trajectories sample a rich sequence of intermediates for propene **combustion** chemistry under the parent CHO parameterization. **Temperature, density, timestep, and quantitative branching** are not specified on this one-page scheme; they appear in the **main paper** and full SI. **Corpus honesty:** plain-text extraction merges labels; use the **PDF** figure for authoritative connectivity.

## Limitations

- Plain-text extraction merges labels; use the **vector/text PDF** for unambiguous reading of species and arrows.
- Quantitative rates and branching fractions are in the **main paper** and full SI, not inferred here.

## Relevance to group

**Adri C. T. van Duin** is a named co-author on the parent manuscript; this artifact captures **observed reaction topology** for propene oxidation under ReaxFF—central to combustion-chemistry applications of the group’s reactive workflows.

## Citations and evidence anchors

- PDF: `papers/CHO_supplements/ReaxFF_CHO_pathways.pdf`.
- Extract: `normalized/extracts/2007chenoweth-venue-propene-combust-details-fig1_p1-2.txt`.

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
