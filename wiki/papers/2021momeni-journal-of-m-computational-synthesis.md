---
id: paper:2021momeni-journal-of-m-computational-synthesis
type: paper
title: "Computational synthesis of 2D materials grown by chemical vapor deposition"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:continuum-or-mesoscale
  - task:application
  - scale:multiscale
paper_keywords:
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1557/s43578-021-00384-2"
year: 2021
authors:
  - "Kasra Momeni"
  - "Yanzhou Ji"
  - "Long-Qing Chen"
venue: "J. Mater. Res. 2021 (invited feature; Focus Issue routing as printed)"
pdf_sha256: "5c01bc199ac447ab5feea23e8e4c8c0a3f6390b251a7208a27a5335a997e23ea"
pdf_path: "papers/ReaxFF_others/Momeni2021_Article_ComputationalSynthesisOf2DMate.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021momeni-journal-of-m-computational-synthesis -->

## Summary

Two-dimensional semiconductors are promising for flexible electronics, energy technologies, and quantum-adjacent device concepts, yet industrial adoption hinges on controllable, reproducible wafer-scale growth. Chemical vapor deposition is versatile but couples fluid mechanics, heat transfer, and surface kinetics across scales; subtle changes in inlet velocity, temperature, or precursor stoichiometry can flip morphology from contiguous monolayers to islanded films. Momeni, Ji, and Chen introduce a multiscale multiphysics model that couples continuum Navier–Stokes transport in a reactor to a phase-field description of two-dimensional film evolution on the substrate. They use WSe\(_2\) as a model material to relate macroscopic knobs that experimentalists control to mesoscale quantities such as surface diffusion and effective deposition rates, then to coverage of the as-grown film.

## Methods

**Continuum and mesoscale (CVD + phase field).** This is **not** an atomistic MD or ReaxFF study. Momeni, Ji, and Chen present a **multiphysics** model for **2D** film growth: **Navier–Stokes** (plus heat and **mass** transport) in a **hot-wall** **CVD** reactor with stated **inlet**, **wall**, and **outflow** **boundary** conditions, coupled to a **phase-field** description of **2D** film evolution on the **substrate**. The gas-phase **solution** supplies local **supersaturation** to **kinetic** and **order-parameter** equations on the surface, with **coefficients** and **WSe\(_2\)**-relevant **parameters** taken from the cited kinetics/continuum literature. The implementation details, **mesh/discretization** choices, and case-study **boundary** values are in the *J. Mater. Res.* full text (`pdf_path`).

**MD, force-field training, and standalone DFT.** **N/A —** not part of this publication.

**Reviews / non-simulation content.** **N/A** as a “methods review” paper: it is a feature article with model equations and a **WSe\(_2\)** benchmark, not a literature **survey** without equations.

## Findings

**Outcomes.** The **coupled** model shows that small changes in **reactor** operating parameters (e.g. **inlet** **velocity** and **temperature** in the case studies illustrated) can substantially change **WSe\(_2\)** **film** **coverage** and **morphology**, motivating **simulation**-informed process windows instead of only **trial-and-error** tuning. **Synthesis** **rate** and **morphology** in this level of theory are limited by **gas**-phase **transport** and the **continuum** **kinetics** that the **phase field** encodes, not by atomistic **RMD** in this manuscript.

**Corpus positioning.** The authors contrast this **reactor+mesoscale** framework with **ab initio** / **reactive** **MD**: the former is affordable at **furnace** scales, while **defect** incorporation and **elementary** **barriers** require **DFT** or **ReaxFF**-class studies elsewhere.

## Limitations

Phase-field coefficients are effective fits; absolute growth rates should be validated against in situ probes such as reflectometry or Raman thermometry. This article does not use ReaxFF or other reactive force fields.

Coupled continuum–phase-field models also inherit uncertainties from precursor chemistry and surface reaction subsets that are not resolved atomistically; sensitivity studies in the paper should be reproduced from the primary text before using the model for quantitative reactor optimization. Mesh resolution and boundary-layer treatments can shift predicted supersaturation fields near the substrate.

## Relevance to group

Peripheral to the ReaxFF corpus but relevant to **2D materials synthesis** context at Penn State collaborators (L.-Q. Chen group).

## Citations and evidence anchors

- J. Mater. Res. DOI **10.1557/s43578-021-00384-2** — model formulation and WSe\(_2\) case study.

## Related topics

- [[reaxff-family]]
