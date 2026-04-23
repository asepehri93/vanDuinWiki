---
id: paper:2016senftle-npj-computat-reaxff-reactive
type: paper
title: "The ReaxFF reactive force-field: development, applications and future directions"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:methods-software
  - method:reaxff
  - task:review
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1038/npjcompumats.2015.11"
year: 2016
authors:
  - "Thomas P. Senftle"
  - "Sungwook Hong"
  - "Md Mahbubul Islam"
  - "Sudhir B. Kylasa"
  - "Yuanxia Zheng"
  - "Yun Kyung Shin"
  - "Chad Junkermeier"
  - "Roman Engel-Herbert"
  - "Michael J. Janik"
  - "Hasan Metin Aktulga"
  - "Toon Verstraelen"
  - "Ananth Grama"
  - "Adri C. T. van Duin"
venue: "npj Computational Materials (2016) 2, 15011"
pdf_sha256: "695bd87b0c35860c9b56f84487d6f05fe8cb8004592b92b366950fbe380abc4a"
pdf_path: "papers/Senftle_npjcompumats201511.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
---
<!-- id:paper:2016senftle-npj-computat-reaxff-reactive -->

## Summary

This open-access **npj Computational Materials** article is a broad **review** of the **ReaxFF** reactive force-field framework: a bond-order-based empirical approach intended to capture **bond breaking and formation** in large atomistic simulations without on-the-fly quantum chemistry. The manuscript situates ReaxFF historically, explains the conceptual structure of the energy model (including how **charge equilibration** and variable charge treatments enter practice), and surveys representative **application areas** spanning organic and inorganic chemistry, interfaces, and multicomponent systems where fixed-bond classical models are inadequate. The review also discusses **parameterization culture** (QM-driven training sets, optimization workflows, and software ecosystems) and outlines **future directions** as reactive simulations scale to larger machines and more complex chemistries. For readers building a knowledge base, the paper functions as a **terminology spine** and pointer graph toward primary parameterization and validation studies rather than a single benchmark paper.

## Methods

As a **review**, the article’s “methods” are bibliographic and conceptual: it synthesizes literature on ReaxFF’s functional form, typical **QM** reference data used in fits, and implementation considerations relevant to practitioners (including coupling to MD engines and charge models). It compares ReaxFF qualitatively to other **reactive empirical** strategies and highlights recurring workflows for extending parameters to new elements and chemistries. Readers should treat any numerical examples as **illustrative**; reproducible protocols for a specific material system must be taken from the cited primary studies and their SI tables.

## Findings

The review presents ReaxFF as a pragmatic bridge between **DFT-like local chemistry** and **classical MD reach** for reactive trajectories in complex geometries. It emphasizes that practical success depends on **training-set coverage** and **validation scope**, because empirical reactivity can be accurate within a trained domain yet fragile outside it. The article synthesizes **development milestones** and a wide span of **application motifs** (including metal-containing and heterogeneous environments discussed in later sections), while candidly noting **outstanding challenges**: transferability, electronic-structure limitations inherent to empirical forms, and the need for disciplined benchmarking when models are used predictively. Publication metadata in the PDF records **npj Computational Materials (2016) 2, 15011** with **DOI 10.1038/npjcompumats.2015.11** (online/publication timing may differ from print-year labeling). As a field guide, the review stresses that ReaxFF’s practical value comes from disciplined workflows: expand training data when moving across **oxidation states** and **coordination environments**, validate on **held-out** configurations that resemble the target application, and treat **charge models** and **boundary conditions** as part of the scientific hypothesis—not incidental details. Readers building citation networks should treat each application chapter as a map to **primary** studies rather than a substitute for the underlying datasets.

## Limitations

Review articles aggregate secondary sources; quantitative claims about a specific material should be traced to the underlying **primary** papers and their data tables.

## Relevance to group

Landmark **group-authored** ReaxFF overview (**van Duin** *et al.*); useful entry point for **terminology**, **capability boundaries**, and **literature pointers** for downstream wiki linking.

## Citations and evidence anchors

- DOI: [10.1038/npjcompumats.2015.11](https://doi.org/10.1038/npjcompumats.2015.11)
- Text-aligned pointers: `normalized/extracts/2016senftle-npj-computat-reaxff-reactive_p1-2.txt`

## Related topics

- [[reaxff-family]]
