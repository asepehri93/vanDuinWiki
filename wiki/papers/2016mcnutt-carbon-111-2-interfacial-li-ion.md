---
id: paper:2016mcnutt-carbon-111-2-interfacial-li-ion
type: paper
title: "Interfacial Li-ion localization in hierarchical carbon anodes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reactive-md-generic
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2016.10.061"
year: 2016
authors:
  - "Nicholas W. McNutt"
venue: "Carbon, 111 (2017) 828-834"
pdf_sha256: "5e24841207ed5f3f4418e9c80e86d61607af563cee01f1b609a0bb88feacf153"
pdf_path: "papers/ReaxFF_others/mcnutt_Carbon_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016mcnutt-carbon-111-2-interfacial-li-ion -->

## Summary

The work studies lignin-derived hierarchical carbon anodes that combine nanoscale crystallites within an amorphous carbon matrix, motivated by low-cost energy storage. Using reactive molecular dynamics on an experimentally validated atomistic model, the authors characterize how Li\(^+\) is stored and show that storage is dominated by localization at interfaces between crystalline carbon domains rather than classical graphitic intercalation. The **hierarchical** microstructure is motivated by **experimental** carbons where **crystallites** are embedded in **disordered** carbon formed during **pyrolysis** of **lignin** precursors.

## Methods

The carbon composite structure varies with lignin pyrolysis temperature; the authors analyze one atomistic model from prior work matched to a composite pyrolyzed at **1500 °C**: mass density **1.51 g cm⁻³**, nanocrystallites about **7 Å** in radius, and equal volume fractions of crystalline and amorphous carbon. The lithiated supercell contains **75,795 C**, **32,353 H**, and **5,012 Li** atoms inside three-dimensional periodic boundaries to capture crystalline–amorphous interfaces.

After energy minimization, the parent unlithiated structure is re-equilibrated with **ReaxFF** in the **NVT** ensemble using a **Nosé–Hoover** thermostat, then lithiated and propagated in **LAMMPS** with **Δt = 0.25 fs** and charge equilibration every timestep to represent Li⁺ charge transfer in the carbonaceous environment (Section 2 of the *Carbon* article). One quoted equilibration segment holds **298 K** for **224 ps** before analyzing Li⁺ distributions. Barostat-driven **NPT** production, static external electric fields, and bias-based enhanced sampling are not highlighted in the protocol summary prepared for this page—confirm in the full PDF if extending the workflow.

**Force-field training.** **N/A** — applies cited ReaxFF parametrizations for C/H/Li.

**Static QM / DFT.** **N/A** — DFT is not the primary method for these large cells.

## Findings

Li⁺ localizes at interfaces between nanoscale crystalline carbon domains and the amorphous carbon matrix rather than by classical graphitic intercalation between extended basal stacks. The work positions hierarchical lignin-derived carbon storage relative to graphite-like intercalation narratives in the introduction. Results are tied to the **1500 °C**-matched descriptor set (density, crystallite size, crystalline volume fraction) in **Methods**. The discussion addresses idealized atomistic models, kinetic accessibility of binding sites, and chemisorption versus physisorption basins on MD timescales—see the *Carbon* PDF for the full argument.

## Limitations

Electrochemical potential control and explicit electrolyte species are outside the excerpts summarized here. When reproducing or extending the study, confirm ensemble choices, any **NPT** segments, and total trajectory budgets from the full *Carbon* article rather than this summary alone.

## Relevance to group

Illustrates reactive atomistic modeling of Li storage in complex carbon microstructures adjacent to battery interface and carbon materials themes.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2016.10.061](https://doi.org/10.1016/j.carbon.2016.10.061)

## Related topics

- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
