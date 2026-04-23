---
id: paper:2008cohen-venue-paper
type: paper
title: "Insights into current limitations of density functional theory"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:dft-static
  - keyword:review-or-perspective
  - keyword:method-development
canonical_tags:
  - domain:methods-software
  - method:dft-static
  - task:review
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2008
authors:
  - "Aron J. Cohen"
  - "Paula Mori-Sánchez"
  - "Weitao Yang"
venue: "Science 321, 792–794 (2008)"
pdf_sha256: "74f0c75c6653cecf2267307c5ab75b3b2a6fc969688b9e85e77b284d3ddd4d70"
pdf_path: "papers/Others/Cohen (2008) Insights into Current Limitations of Density Functional Theory.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2008cohen-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **Science Perspective** identified by bibliographic cues in the extract (`Science`, Vol. 321, Aug 2008). Add the **journal DOI** from the publisher landing page if you need a stable hyperlink—the normalized record has no DOI.

## Summary

This perspective argues that widely used approximate **exchange–correlation functionals** in **DFT** exhibit systematic errors traceable to **delocalization error** and **static correlation error**, framed using **fractional charge** and **fractional spin** perspectives. It summarizes major failure modes discussed in the text: underestimated **reaction barriers**, **band gaps**, energies of **dissociating molecular ions**, and **charge-transfer excitation energies**, together with overstated **charge-transfer complex binding**, and exaggerated **polarizability** under electric fields—linked to delocalization. Near-degenerate and strongly correlated regimes (e.g., transition metals, bond breaking) are tied to **static correlation** limitations.

## Methods


This *Science* Perspective does not report a single numerical simulation protocol; it develops a conceptual framework using fractional electron number and fractional spin constructions, illustrated with model dissociation curves (for example H\(_2^+\) and H\(_2\)) comparing Hartree–Fock, LDA, and B3LYP to exact or limiting behaviors. The argument ties systematic DFT failures to two classes of approximate exchange–correlation error framed in the text as delocalization error and static correlation error.

### Review scope and evidence style

This page summarizes Cohen, Mori-Sánchez, and Yang’s **Science** **Perspective** (`pdf_path`, `normalized/extracts/2008cohen-venue-paper_p1-2.txt`). **Literature scope:** **DFT** **approximate exchange–correlation** functionals across communities where **delocalization** and **static correlation** errors matter. **Comparison protocol:** illustrative **model** **dissociation** curves compare **Hartree–Fock**, **LDA**, and **B3LYP** to exact or reference limits—see the PDF for equations and citations. **Atomistic MD / force-field training:** **N/A —** not the subject of this article.

### Static QM / DFT (as used in the Perspective’s arguments)

**Functional:** **LDA**, **B3LYP**, and **Hartree–Fock** appear as exemplar methods in the dissociation-curve discussion (not a single production **DFT** protocol for one material). **Dispersion:** **N/A — explicit DFT-D / vdW correction** scheme not isolated in the short extract—verify the PDF if needed. **Basis:** **N/A — basis-set specification** for the tutorial curves not recovered from the excerpt. **k-sampling:** **N/A — Brillouin-zone mesh** (the Perspective is not a periodic solid benchmark study). **Structures / pathways:** **dissociation** coordinates for **H\(_2^+\)** and **H\(_2\)** model systems. **Properties computed / discussed:** **reaction barriers**, **band gaps**, **charge-transfer** energetics, **polarizability** under fields, and related **energy** errors tied to **fractional charge** / **fractional spin** reasoning.

## Findings

Common **approximate exchange–correlation** functionals show **delocalization error**: they tend to **underestimate** **reaction barriers**, **band gaps**, **energies of dissociating molecular ions**, and **charge-transfer excitation energies**, and to **overbind charge-transfer complexes** and **overpolarize** under electric fields. A second class of failure is **static correlation error** in **near-degenerate** / **strongly correlated** situations (e.g. **transition metals**, **bond breaking**), diagnosable with **fractional charge** and **fractional spin** constructions. Reducing these systematic errors is framed as the path to broader reliable **DFT** predictions. **Corpus honesty:** the normalized record lacks a **DOI**; cite **Science** **321**, 792–794 (2008) from the PDF imprint.

## Limitations

- This is a **perspective**, not a computational methods benchmark for a specific materials code.
- No DOI is present in `normalized/papers/2008cohen-venue-paper.json`; cite **Science** directly for archival linking. Repository automation maps this stable `paper_id` to `normalized/papers/2008cohen-venue-paper.json` and the repo-relative `pdf_path`. Where `extraction_quality` is partial, the tracked PDF and any publisher DOI you add later remain the quantitative authority over short local extracts.

## Relevance to group

Conceptual background for why **QM training data** and **validation** matter for **ReaxFF** fitting pipelines that ingest DFT references.

## Citations and evidence anchors

- PDF: `papers/Others/Cohen (2008) Insights into Current Limitations of Density Functional Theory.pdf`.
- Extract: `normalized/extracts/2008cohen-venue-paper_p1-2.txt`.

## Related topics

- [[themes-index]]
