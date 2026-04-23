---
id: paper:2016velegol-soft-matter-origins-concentration
type: paper
title: "Origins of concentration gradients for diffusiophoresis"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:continuum-or-mesoscale
  - task:review
  - scale:multiscale
candidate_tags: []
source_refs: []
doi: "10.1039/C6SM00052E"
year: 2016
authors:
  - "Darrell Velegol"
  - "Astha Garg"
  - "Rajarshi Guha"
  - "Abhishek Kar"
  - "Manish Kumar"
venue: "Soft Matter (2016) 12, 4686–4703"
pdf_sha256: "b7600c57d0ba837efbe96e0781e20e18dbcc3f9b7884565b8b83111aaf3d3ad5"
pdf_path: "papers/Others/Vallegol_et_al_diffusion_2016.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:review-or-perspective
  - keyword:water-interfaces
---
<!-- id:paper:2016velegol-soft-matter-origins-concentration -->

## Summary

Velegol *et al.* publish a tutorial-style **Soft Matter** article (DOI `10.1039/C6SM00052E`, **12**, **4686–4703**, **2016**) arguing that **diffusiophoresis**—the **phoretic** migration of **colloids** and **particles** along **solute** **concentration gradients**—and the companion phenomenon of **diffusio-osmosis** (**solvent** flow along **walls** driven by the same gradients) are far more ubiquitous than textbook presentations suggest. The central claim is not a new **microscopic** simulation but a **taxonomy**: **concentration gradients** arise spontaneously from **reaction** **asymmetry**, **dissolution**, **crystallization**, **evaporation**, **mixing**, **sedimentation**, **membrane** **selectivity**, and many other everyday transport processes, not only from deliberately **imposed** **boundary** **concentrations** in a **U-tube**. The authors survey **geophysical**, **physiological**, **drying**, **separations**, and **microfluidic** settings where **diffusiophoretic** transport may be **under-recognized** yet **engineering-relevant**.

## Methods

The article is a **tutorial-style *Soft Matter* review** (**12**, **4686–4703**, **2016**, DOI in front matter) that catalogs how **solute concentration gradients** arise in natural and engineered settings and how those gradients drive **diffusiophoresis** (colloid migration) and **diffusio-osmosis** (solvent slip along walls). Beyond deliberately imposed **U-tube** profiles, the authors treat **reaction asymmetry**, **dissolution**, **crystallization**, **evaporation**, **mixing**, **sedimentation**, **membrane selectivity**, and related transport as concrete **gradient sources**, then connect them qualitatively to **Navier–Stokes** channel physics (**pressure-driven** flow versus **chemically** driven slip) and to **electrokinetic** analogies (**diffusiophoresis** versus **electrophoresis**) when **local chemical potentials** persist even under screened **macroscopic** fields.

**1 — MD application.** **N/A —** not a molecular-dynamics methods paper.

**2 — Force-field training.** **N/A —** not applicable.

**3 — Static QM.** **N/A —** not applicable.

**4 — Experiments / continuum benchmarks.** **N/A —** no new **parameterized** continuum fits or **A/B** experiments are reported as a unified benchmark; the value is **taxonomy** plus literature pointers.

## Findings

**Outcomes / thesis.** **Concentration gradients** sufficient for **diffusiophoresis** are argued to be **common**, not esoteric, arising from the **process list** highlighted in the **abstract** (reaction asymmetry, dissolution, crystallization, evaporation, mixing, sedimentation, membrane selectivity, etc.).

**Design levers.** The narrative motivates **recognizing** phoretic transport when interpreting **microfluidic**, **drying**, **georeservoir**, **physiological**, and **separations** flows—so that **gradients** can be **engineered** for directed transport or diagnosed when they **bias** deposition.

**Relation to atomistic electrolyte work (corpus bridge).** vanDuinWiki **MD** papers that resolve **interfacial ion stratification** can inform the **boundary-layer** **chemical potential** shapes assumed in **continuum** phoresis models, but this review **does not** couple to a specific **force field** or **simulation protocol**.

**Limitations / outlook.** As a **2016** tutorial, quantitative **coefficient** tables and **modern** microfluidic datasets should be pulled from **primary** citations referenced inside the **PDF** rather than from this summary alone.

## Relevance to group

Penn State **colloid/electrokinetics** perspective complementary to atomistic **electrolyte interface** work; useful for placing **ionic gradient** phenomena that also appear in MD papers.

## Citations and evidence anchors

- DOI: [10.1039/C6SM00052E](https://doi.org/10.1039/C6SM00052E)
- Text-aligned pointers: `normalized/extracts/2016velegol-soft-matter-origins-concentration_p1-2.txt`

## Related topics

- Electrolyte transport and colloid dynamics (continuum framing)
