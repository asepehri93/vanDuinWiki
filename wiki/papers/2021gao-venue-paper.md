---
id: paper:2021gao-venue-paper
type: paper
title: "Molecular dynamics study of melting, diffusion, and sintering of cementite chromia core-shell particles"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - method:reaxff
  - material:alloy-bulk
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:metallic-systems
source_refs: []
doi: "10.1016/j.commatsci.2021.110721"
year: 2021
authors:
  - "Yawei Gao, Ana Paula Clares Pastrana, Guha Manogharan, Adri van Duin"
venue: "Comput. Mater. Sci. (Elsevier uncorrected proof in corpus)"
pdf_sha256: "137ce568eb4f219e699689f2087b89c7445990bd7084b61fbad7a24ca7299bfb"
pdf_path: "papers/Gao_CompSciMat_2021_Cementite_Chromia_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2021gao-venue-paper -->

## Summary

This slug tracks an **Elsevier uncorrected proof** (`papers/Gao_CompSciMat_2021_Cementite_Chromia_galley.pdf`) for the same *Comput. Mater. Sci.* article (DOI `10.1016/j.commatsci.2021.110721`) on ReaxFF MD of cementite (Fe\(_3\)C) with a Cr\(_2\)O\(_3\) shell, motivated by AM stainless powder. The peer-reviewed text, full simulation tables, and stable locators are on [[2021gao-computationa-molecular-dynamics]]; this file exists because the manifest registers **proof** bytes that may differ in **layout** from the journal PDF.

## Methods

### 1 — MD application (atomistic dynamics)

**Protocol class:** ReaxFF MD in LAMMPS, **NVT** ensemble, **0.25 fs** time step, **Berendsen** thermostat (damping **100 fs** in the article), **200** Å cubic cells with **3D periodic boundary conditions** on the simulation box, **900 K** and **2000 K** staging plus **1000–2600 K** melting sweeps, **0.5 ns** sintering windows as in Section 2 of the VOR—**not re-derived here** because the galley PDF is a non-primary duplicate. For reproducible **timestamps, equilibration lengths, and atom counts**, use [[2021gao-computationa-molecular-dynamics]] (full PDF) rather than this proof file alone.

**Barostat / pressure:** N/A — no barostat; **N/A — pressure** not set (constant-volume NVT). **E-field / enhanced sampling:** N/A. **Electrostatics:** ReaxFF QEq with charges updated each step in the VOR text.

### 2 — Force-field training

**N/A —** published Shin *et al.* C/H/O/Fe/Cr set with DFT/validation in Section 2.1; see the VOR page.

### 3 — Static QM

Validation DFT/BAND as cited on the VOR page; not re-summarized from the proof.

### 4 — Review

N/A.

## Findings

**Corpus / KB honesty:** The scientific conclusions (Lindemann melting comparison, O ingress, MSD, four-stage sintering, 900 K incomplete Stage 4) match the abstract and the curated **version-of-report** page [[2021gao-computationa-molecular-dynamics]]. This wiki note does **not** re-quote **figure** numbers or **page** ranges from the galley because **pagination may differ** from the typeset article.

**Comparisons / sensitivity / mechanisms:** as authored on the VOR entry—**melting locus** (core vs surface), **temperature** regime (900 vs 2000 K, and 1000–2600 K ramp). **Limitations of this slug:** `extraction_quality: partial` reflects the proof PDF path, not a separate result set.

## Limitations

**Uncorrected proofs** may carry watermarks and non-final editing. Prefer [[2021gao-computationa-molecular-dynamics]] for **citation-ready** reading and protocol detail.

## Relevance to group

**Adri C. T. van Duin** senior authorship; manifest linkage to a proof PDF for the Comp. Mater. Sci. article.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2021.110721](https://doi.org/10.1016/j.commatsci.2021.110721)

## Reader notes (navigation)

- Primary article: [[2021gao-computationa-molecular-dynamics]]  
- Themes: [[reaxff-family]], metallurgy / oxide ceramics clusters in paper indexes

## Related topics

- [[2021gao-computationa-molecular-dynamics]]
- [[reaxff-family]]
