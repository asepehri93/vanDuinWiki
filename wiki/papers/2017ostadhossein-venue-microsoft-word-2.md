---
id: paper:2017ostadhossein-venue-microsoft-word-2
type: paper
title: "Supporting information (part II): ReaxFF optimization tables for two-dimensional MoS₂"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:supporting-information
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors: []
venue: "Supporting information (ACS Publications)"
pdf_sha256: "aad05bf43b146fe375bcf1e467e9c1562953eb89efba4be8ee144a95432415f0"
pdf_path: "papers/Ostadhossein_MoS2_JPC_Letters_2017_SI_II.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017ostadhossein-venue-microsoft-word-2 -->

!!! abstract
SI text for Ostadhossein et al. MoS₂ JPCL: DFT training with Jaguar (B3LYP/LAV3P**) and VASP (PBE-PAW) plus tables of optimized ReaxFF parameters (Table S1) and molecular/periodic training sets (Table S2); references to bond/angle distortion figures vs DFT.

## Summary

This PDF is Supporting Information (Part II) for an ACS *Journal of Physical Chemistry Letters* communication on two-dimensional MoS₂ modeled with ReaxFF. Its primary knowledge-base function is reproducibility: it lists quantum-chemistry training data, optimizer outputs, and full parameter tables for the Mo–S reactive force field used in the parent letter. The document states that gas-phase and molecular training data were computed with Jaguar using B3LYP and the LAV3P** basis set (entries summarized in Table S1), while periodic MoS₂ and bilayer deformations were computed with VASP using GGA-PBE, projector-augmented-wave pseudopotentials, a 400 eV plane-wave cutoff, Γ-centered k-meshes, and a force convergence criterion of 0.02 eV/Å, including bilayer scans with constrained molybdenum layers and relaxed sulfur positions. Nudged elastic band calculations appear where barriers are reported. Table S1 records optimized ReaxFF parameters (Mo atom parameters, Mo–S bonds, off-diagonal couplings, angle terms), while Table S2 enumerates molecular and periodic structures used in the training set—equations of state, edges, vacancies, and related motifs. Figures S1–S2 compare ReaxFF and DFT bond and angle energy scans for selected deformations.

## Methods

**Force-field training / fitting.** **Table S1** lists the **optimized ReaxFF parameters** (Mo atom parameters, **Mo–S** bonds, off-diagonal couplings, angle terms). **Table S2** enumerates **molecular and periodic MoS₂** training structures (equations of state, **edges**, **vacancies**, related motifs). **Figures S1–S2** compare **ReaxFF** and **DFT** bond/angle **energy scans** for selected deformations.

**MD application (atomistic dynamics).** **N/A —** this SI documents **parameters** and **QM** benchmarks that feed **parent** **LAMMPS** workflows on **`[[2017ostadhossein-venue-research]]`**, not new production trajectories in the SI file itself.

**Static QM / DFT.** **Jaguar**: **B3LYP** with **LAV3P\*\*** basis for **gas-phase / molecular** training data. **VASP**: **GGA-PBE**, **PAW** pseudopotentials, **400 eV** plane-wave cutoff, **Γ-centered** k-meshes, force convergence **0.02 eV/Å**, including **bilayer** scans with constrained **Mo** planes and relaxed **S** positions; **nudged elastic band (NEB)** calculations appear where **barriers** are reported.

**Review / non-simulation framing.** **Supporting Information Part II** for the **MoS₂** **ReaxFF** **JPCL** letter (**non-primary**); interpret science on **`[[2017ostadhossein-venue-research]]`** (**DOI 10.1021/acs.jpclett.6b02902**).

## Findings

**Outcomes & mechanisms.** The SI package documents **which ReaxFF energy terms** were adjusted for **2017 MoS₂** and **which QM benchmarks** anchored each term, enabling auditors to trace discrepancies between later simulations and the published training pipeline.

**Comparisons.** **Figures S1–S2** (bond/angle distortion scans) provide direct **ReaxFF vs DFT** energy comparisons for selected deformations.

**Sensitivity & design levers.** **QM level** choices (**Jaguar** vs **VASP**) and **periodic vs molecular** training motifs determine where the reactive FF is stiffest or softest relative to **DFT**.

**Limitations & outlook.** This file is **SI-only**; it does not restate the parent letter’s full mechanistic narrative or main-text device figures.

**Corpus / PDF honesty.** Treat **Table S1/S2** numerics as **fitting artifacts** tied to the **2017** snapshot; for scientific conclusions about **growth**, **edges**, or **catalysis**, use **`[[2017ostadhossein-venue-research]]`**.


## Limitations

Readers seeking conclusions about lateral versus vertical growth kinetics must consult the parent letter; the SI does not restate the full mechanistic narrative or main-text figures.

## Relevance to group

This is the transparency backbone for MoS₂ ReaxFF parametrization in a major JPCL line coauthored by the van Duin group, and it should be linked whenever parameters are reused for LAMMPS input decks.

## MAS / retrieval notes

Automation should ingest Table S1/S2 directly for parameter files rather than paraphrasing numeric columns; link parent DOI `10.1021/acs.jpclett.6b02902` for bibliographic grounding. If a query asks for “MoS₂ ReaxFF parameters,” return the SI path `papers/Ostadhossein_MoS2_JPC_Letters_2017_SI_II.pdf` and the parent article slug for scientific interpretation.

## Citations and evidence anchors

- Parent DOI: `10.1021/acs.jpclett.6b02902`

## Related topics

- [[reaxff-family]]
- [[2017ostadhossein-venue-research]]
