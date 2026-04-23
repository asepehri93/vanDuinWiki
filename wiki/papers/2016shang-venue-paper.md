---
id: paper:2016shang-venue-paper
type: paper
title: "Supporting Information: Lateral Versus Vertical Growth of Two-Dimensional Layered Transition-Metal Dichalcogenides (MoS2)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2016
authors:
  - "Shun-Li Shang"
  - "Greta Lindwall"
  - "Yi Wang"
  - "Joan M. Redwing"
  - "Tim Anderson"
  - "Zi-Kui Liu"
venue: "Supporting Information (Nano Letters companion)"
pdf_sha256: "50fce298d1ddc2bba66a8ffef370f1885780ab467aecb6df14fd53b99a9c83ca"
pdf_path: "papers/Others/Shang_Liu_MoS2_growth_NanoLetters2016_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
paper_keywords:
  - keyword:supporting-information
  - keyword:dft-static
  - keyword:2d-materials
---
<!-- id:paper:2016shang-venue-paper -->

## Summary

This Supporting Information PDF accompanies the *Nano Letters* thermodynamic analysis of MoS₂ chemical vapor deposition growth windows, focusing on competition between lateral monolayer extension and bilayer nucleation. Rather than introducing new reactive molecular dynamics models, the SI supplies the computational chemistry backbone: Vienna *Ab initio* Simulation Package–style density functional theory (DFT) settings, additional DFT energy surfaces, CALPHAD thermodynamic database construction for the molybdenum–sulfur subsystem, and multicomponent gas-phase analysis for Mo–S–O–H chemistry using the SGTE-SSUB database. The SI explicitly tests multiple exchange–correlation treatments beyond the PBE+D3 combination highlighted in the main text, including bare GGA-PBE, PBEsol, and PBEsol+D3, with Table S3 benchmarking equations of state for MoS₂, α-alumina, body-centered-cubic molybdenum, and graphite against experiments; the authors state that PBE+D3 offers a favorable balance of efficiency and agreement for the set of training structures used. Supplementary Table S5 bundles a complete thermodynamic database (TDB-style) for the Mo–S system, while supplementary figures extend main-text phase diagrams into broader ranges of temperature, pressure, and composition, clarifying partial pressures of relevant sulfur and oxygen carriers during growth. Operators should pair this file with **`[[2016shang-venue-nl-2016-02443v]]`** for scientific conclusions about growth modes.

## Methods

This SI documents **DFT** settings and **CALPHAD** database construction for the **MoS\(_2\)** growth thermodynamics in **`[[2016shang-venue-nl-2016-02443v]]`**. **Table S2** lists **supercell** sizes, **plane-wave** cutoffs, **k**-point meshes, and **convergence** thresholds for periodic **MoS\(_2\)** and related benchmarks, comparing **PBE**, **PBE+D3**, **PBEsol**, and **PBEsol+D3**. **Table S3** benchmarks **equations of state** for **MoS\(_2\)**, **α-alumina**, **bcc Mo**, and **graphite** against experiment to justify functional choices. **Tables S4–S6** and the bundled **Mo–S** thermodynamic database support the **CALPHAD** fit to experimental **phase equilibria**; supplementary **figures** extend **gas speciation**, **T–x** sections, and **P–T** diagrams for representative **CVD**-like gas mixtures.

**MD application / force-field training.** **N/A —** the SI is **QM + thermodynamics** documentation, not a reactive **MD** or **ReaxFF** protocol sheet.

**DFT documentation in the SI.** Tables summarize **PBE**/**PBEsol** **functionals** with and without **Grimme D3** **dispersion**, **plane-wave** cutoffs, **k-point** meshes, relaxed **geometry** benchmarks (equations of state reporting **energy** versus volume for **MoS\(_2\)**, **graphite**, **bcc Mo**, and **α-alumina**), and derived thermodynamic **properties** feeding **CALPHAD**. **N/A —** full numerical grids on this wiki page—read **`pdf_path`**.

## Findings

**Role of the SI.** The package makes **DFT training data** and **CALPHAD** optimization **auditable**—how **equation-of-state** benchmarks and **Mo–S** parameters constrain the **P–T–x** windows discussed in the **main letter**. It does **not** establish standalone **ReaxFF** or production **MD** benchmarks.

**Corpus honesty.** Headline conclusions on **lateral versus vertical** growth belong to **`[[2016shang-venue-nl-2016-02443v]]`**; use **`pdf_path`** for full tables (`extraction_quality: partial`).

## Limitations

Corpus extraction quality is flagged partial; rely on the PDF for complete tables. Any mismatch between DFT functionals must be resolved against the main article’s chosen reference treatment before porting numbers into other workflows.

## Relevance to group

The SI underpins a flagship Penn State–affiliated MoS₂ thermodynamics publication in the corpus, providing DFT and CALPHAD inputs that contextualize later ReaxFF studies of MoS₂ from separate papers.

## MAS / retrieval notes

Route growth-window questions to **`[[2016shang-venue-nl-2016-02443v]]`** for conclusions; use this SI page for DFT k-mesh/cutoff tables and CALPHAD TDB filenames. Extraction quality is `partial` in corpus metadata—verify critical numbers against the PDF bytes. When users ask for “MoS₂ phase diagrams,” distinguish gas-phase speciation figures in the SI from thin-film growth conclusions in the main letter.

## Citations and evidence anchors

- Primary PDF: `papers/Others/Shang_Liu_MoS2_growth_NanoLetters2016_SI.pdf`
- Text-aligned pointers: `normalized/extracts/2016shang-venue-paper_p1-2.txt`

## Related topics

- [[2016shang-venue-nl-2016-02443v]]
