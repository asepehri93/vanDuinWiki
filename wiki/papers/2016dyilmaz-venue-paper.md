---
id: paper:2016dyilmaz-venue-paper
type: paper
title: "Investigating structure–property relations of poly(p-phenylene terephthalamide) fibers via reactive molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2016
authors:
  - "Dündar E. Yilmaz"
  - "Nebahat Bulut"
venue: "Preprint / institutional manuscript (see PDF)"
pdf_sha256: "e1ee05134713e2eaf6b0e3040833fdc1603fab0c945f1d96568533436b809fa2"
pdf_path: "papers/ReaxFF_others/dyilmaz.pdf"
extraction_quality: "partial"
group_affiliation: false
---
<!-- id:paper:2016dyilmaz-venue-paper -->

## Summary

**Reactive MD with ReaxFF** is applied to **poly(p-phenylene terephthalamide) (PPTA, Kevlar-class)** fiber models with varying **radius**, **crystallinity**, and **core–shell** arrangements, motivated by **aramid** fibers’ **high** **specific** **stiffness** and the need to connect **atomic** **texture** to **macroscopic** **modulus**. **Quasi-static tensile deformation** up to **~15% strain** extracts **Young’s moduli** and follows how **crystalline** versus **disordered** fractions and **domain boundaries** control **failure initiation**. The manuscript introduces an **order parameter** based on the **cross-sectional area fraction** of **crystalline** domains to rationalize **modulus** trends in **core–shell** geometries where **skin** and **core** **order** differ by construction.

## Methods

**MD application (ReaxFF, quasi-static tension):** **Reactive MD with ReaxFF** pulls **PPTA** fiber supercells in **quasi-static tension** to **~15% strain** along the fiber axis; **step size and relaxation between strain increments** are specified in **`papers/ReaxFF_others/dyilmaz.pdf`**. **Stress–strain** curves give **Young’s modulus** at small strain and mark **bond-scission**. **Crystalline** and **disordered** domains are labeled so a **cross-sectional area fraction** of ordered material can define an **order parameter** for **core–shell** geometries. **Engine / timestep / thermostat / total trajectory time:** **N/A — not recoverable from the short corpus text available here** (read the **PDF** for **LAMMPS** or other engine keywords and control parameters). **Ensemble label during tension ramps:** **N/A — not stated in the indexed extract** (likely quasi-static energy relaxation between strain steps rather than long **NVT** production segments; confirm in PDF). **Barostat / hydrostatic pressure control:** **N/A — not used** for the quasi-static uniaxial protocol summarized here. **Imposed pressure (GPa/MPa):** **N/A — tensile load along fiber axis**, not a pressure-driven study. **Electric field / enhanced sampling:** **N/A — not used.**

**Target temperature (K) during tension / relaxation segments:** **N/A — not stated in the indexed extract**; confirm whether runs are **0 K** energy minimization steps vs finite-**T** **MD** in **`papers/ReaxFF_others/dyilmaz.pdf`**.

**Force-field training:** **N/A — applies an existing organics-capable ReaxFF** cited in the manuscript rather than reporting a new fit.

**Static QM / DFT:** **N/A — not the primary method** in the summarized framing.

**PBC / supercell:** **3D PBC** fiber supercells as in standard bulk fiber models; **cell vectors and equilibration/production durations:** **N/A — see PDF** if not tabulated in your local extract.

## Findings

The abstract reports **Young’s moduli** of about **226 GPa** (**disordered** chains) versus **311 GPa** (**crystalline** chains) for the illustrated models, attributing the gap to **order**. For **core–shell** fibers where **core** and **shell** swap **crystalline** vs **underordered** assignments, effective moduli scale approximately **linearly** with the **cross-sectional area fraction** of the **crystalline** section; the authors introduce an **order parameter** to capture this trend. **Failure** initiates at **domain boundaries** between **ordered** regions rather than through uniform bulk **chain** rupture, so **strain** up to **~15%** probes how **texture** concentrates load. **Bibliography:** this corpus copy is a **dated manuscript PDF** without a recorded **DOI**; reconcile with any **journal** version before citing pagination. **ReaxFF** organics models may not reproduce macroscopic **Kevlar** tests quantitatively—use the **PDF** for tables and failure sequences.

## Limitations

- **DOI not recorded** in normalized metadata; treat bibliographic details as **manuscript-stage** until reconciled with a published version.
- **Strain rate**, **system size**, and **ReaxFF** **organics** parameter scope imply **qualitative** trends for **ultimate** **properties** more than quantitative agreement with **macroscopic** fiber tests.

## Relevance to group

Demonstrates **ReaxFF uptake in aramid fiber mechanics** adjacent to the group’s broader **reactive polymer / composite** interests (even though Penn State authors are not listed on this PDF). Operators curating **PPTA** should cross-check any future **DOI** assignment against the **published** record if this **manuscript** PDF is superseded by a **journal** version with identical **science**.

## Citations and evidence anchors

- Abstract and introduction in `papers/ReaxFF_others/dyilmaz.pdf` (dated **Feb 3, 2016** in the extract).

## Related topics

- [[reaxff-family]]
