---
id: paper:2014botari-physical-che-mechanical-properties
type: paper
title: "Mechanical properties and fracture dynamics of silicene membranes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/c4cp02902j"
year: 2014
authors:
  - "Botari, T."
  - "Perim, E."
  - "Autreto, P. A. S."
  - "van Duin, A. C. T."
  - "Paupitz, R."
  - "Galvao, D. S."
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "144b48f19727aaabd3ead272afa194171a5b0499e65fe4bd1819e4e10f9e9d2a"
pdf_path: "papers/Botari_Silicene_PCCP_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014botari-physical-che-mechanical-properties -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Suspended single-layer silicene is studied with DFTB and ReaxFF reactive MD alongside higher-level DFT for equilibrium properties. The work reports elastic constants, fracture patterns, edge reconstructions, stress distributions, unbuckling under strain, temperature effects, and zigzag versus armchair edge differences, motivated by silicene’s buckled structure versus graphene (abstract; introduction, extract).

Silicene’s mixed sp\(^2\)/sp\(^3\)-like buckling makes failure pathways richer than planar graphene: the paper uses multi-method MD to separate elastic response from bond rearrangements that create holes and linear-chain debris during fracture.

## Methods

### Static benchmarks (equilibrium properties)

- **DFT:** **DMol³** calculations supply higher-level reference data for selected **equilibrium** properties used to anchor lower-cost models (methodology opening in extract).
- **DFTB+:** tight-binding calculations provide intermediate-cost **equilibrium** benchmarks for **silicene** sheets.
- **ReaxFF:** reactive force-field evaluations compare against the above for **equilibrium** diagnostics where reported in the article.

### Dynamics (fracture and large cells)

- **DFTB+ MD** enables **large-cell** simulations of **mechanical** response at lower cost than full **DFT** dynamics.
- **ReaxFF MD** extends to **bond-breaking** regimes where **edge reconstructions** and **defect-mediated** failure occur; the abstract positions **DFTB+** and **ReaxFF** as complementary for **elastic** versus **reactive** stages.

### Observables tracked (per abstract)

- **Elastic constants**, **fracture patterns**, **edge reconstructions**, **stress distributions**, **unbuckling** under strain, **temperature** dependence, and **zigzag vs armchair** edge differences (abstract bullets echoed on this page).

### Coverage note

- **Supercell sizes, strain rates, and thermostats** are specified in the **PCCP** Methods section; the checked-in extract truncates mid-methodology.

**1 — MD application (atomistic dynamics).** **Engine / code:** **DFTB+** for large-cell **molecular dynamics** and **ReaxFF** **reactive molecular dynamics** for bond-breaking regimes (`papers/Botari_Silicene_PCCP_2014.pdf`; extract `normalized/extracts/2014botari-physical-che-mechanical-properties_p1-2.txt` names **DFTB+** and **ReaxFF**). **System:** **suspended single-layer silicene** membranes, including **zigzag** vs **armchair** edges and varying sizes up to **~1600 atoms** in the **DFT** validation discussion (extract). **Boundaries:** **in-plane periodic** membrane supercells with vacuum padding (**N/A — exact PBC vectors and vacuum thickness not in the p1–2 extract**). **Ensemble / thermostat / timestep / duration / barostat:** **N/A — full production MD settings** (e.g., **NVT** coupling, **Δt**, **ps/ns** windows, strain-rate protocol) lie **after** the clipped extract—use **PCCP** Methods. **Temperature:** finite-**T** **MD** is part of the study design (abstract), but the numerical **K** schedule is **PDF-grounded**. **Pressure:** **N/A —** mechanical **strain**/`stress` tests rather than quoted **NPT** hydrostatic targets in this summary. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training:** **N/A —** applies existing **ReaxFF** and **DFTB+** models; the article uses **DFT (PBE, DNP, DMol³)** to **validate** equilibrium predictions (extract), not to fit new parameters on-page.

**3 — Static QM / DFT-only.** **DMol³**, **PBE-GGA**, **DNP** basis, stated **convergence** criteria, and **full cell** relaxations for **equilibrium** benchmarks (extract, **Methodology**).

## Findings

**Outcomes and mechanisms.** **DFTB+** and **ReaxFF MD** on **suspended silicene** report **elastic** response, **fracture** morphologies, **edge reconstructions**, **stress** fields, **unbuckling** under strain, and **temperature**-dependent failure, with explicit comparison of **zigzag** vs **armchair** edges and membrane **size** effects (abstract; introduction in extract frames **buckling** and possible **linear-chain** debris versus graphene).

**Comparisons.** **DFT (PBE / DMol³)** and **SCC-DFTB+** are used to **benchmark** lower-cost models on **equilibrium** properties before large-scale rupture **MD** (extract); quantitative **moduli** and **critical stresses** are **table/figure** content in the **PCCP** PDF, not duplicated here.

**Sensitivity and design levers.** Trends depend on **edge termination**, **membrane size**, and **temperature** as independent variables called out in the abstract.

**Limitations and outlook.** **DFT** dynamics are **precluded** at the largest sizes in the extract’s argument; **ReaxFF** accuracy for **Si** **mechanochemistry** should be judged against the paper’s own **DFT/DFTB** checks. **Corpus honesty:** `normalized/extracts/2014botari-physical-che-mechanical-properties_p1-2.txt` ends early in **Methodology**; this page does not invent **thermostat** constants or **strain rates** absent from the checked extract—consult `papers/Botari_Silicene_PCCP_2014.pdf` for full protocols.

## Limitations

Extract stops early in methodology; quantitative moduli and fracture stress tables are later in the PDF.

## Relevance to group

van Duin coauthor on ReaxFF for 2D silicon mechanics, adjacent to graphene and nanocarbon materials programs.

## Citations and evidence anchors

- PCCP 2014, 16, 19417–19423; DOI `10.1039/c4cp02902j` (extract page 1).
- Abstract + introduction paragraphs (extract pages 1–2).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
