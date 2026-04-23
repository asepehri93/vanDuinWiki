---
id: paper:2019gao-venue-rsc-cp
type: paper
title: "A ReaxFF molecular dynamics study of molecular-level interactions during binder jetting 3D-printing (RSC proof)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
source_refs: []
doi: "10.1039/c9cp03585k"
year: 2019
authors:
  - "Yawei Gao"
  - "Yun Kyung Shin"
  - "Daniel Martinez"
  - "Guha Manogharan"
  - "Adri C. T. van Duin"
venue: "Physical Chemistry Chemical Physics (author proof)"
pdf_sha256: "4a701b0506ae25a1425d3badfe13b57526e27eaeb3cc2ffa069bda5e38afb044"
pdf_path: "papers/Gao_PCCP_2019_3D_printing_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019gao-venue-rsc-cp -->

## Evidence and attribution

!!! note "RSC proof / production PDF"

    **`[[2019gao-physical-che-reaxff-molecular]]`** hosts the **full PCCP article** PDF preferred for figures. This slug records the **galley/proof** packaging (`papers/Gao_PCCP_2019_3D_printing_galley.pdf`).

## Summary

The article models binder jetting three-dimensional printing of AISI 316L stainless steel using ReaxFF molecular dynamics of chromium-oxide nanoparticles with aqueous diethylene glycol (DEG) and water, following print, cure, burn-out, and sinter thermal stages. Simulations resolve hydrogen-bond networks between particles, DEG oxidation during heating, and Cr–O bridge formation after sintering. A restraint potential measures an effective breaking strength between nanoparticles as binder composition varies, and the authors compare DEG with related alcohols differing in hydroxyl content. The narrative matches **`[[2019gao-physical-che-reaxff-molecular]]`** in full; this page preserves proof-file provenance.

## Methods

The study adopts a Cr/C/H/O ReaxFF parametrization from Shin and coworkers for passivated Cr₂O₃-rich surfaces. Nanoparticles ~22 Å in diameter (~500 atoms) are annealed in H₂O + O₂ at 1273 K before stage-wise NVT simulations with a Berendsen thermostat (100 fs damping). Typical cells place two nanoparticles with controlled water and DEG counts in an 80 Å periodic cube for the 300 K “print” stage, expand to a larger cell for cure at 393 K with product removal, then heat to 900 K for burn-out and 1900 K for sintering. Breaking strength uses a bell-shaped restraint on 25 atom pairs per particle with strain-rate control as in Equation 3 of the article. Compositional sets A and B vary water versus DEG totals (Table 1).

**Engine and pressure control.** **Reactive molecular dynamics** with **ReaxFF** is executed in **LAMMPS** as in the **PCCP** article; **periodic** **supercells**, **NVT** **Berendsen** damping, and restraint **MD** parameters match [[2019gao-physical-che-reaxff-molecular]]. **Barostat / hydrostatic pressure:** **N/A** — no **GPa** **pressure** targets beyond **constant-volume** **NVT** in the summarized BJP protocol. **External electric field:** **N/A**. **Enhanced sampling:** **N/A**.

## Findings

Hydrogen bonds involving DEG and water link Cr-oxide particles during print and cure, increasing restraint-based strength when both species participate. Burn-out oxidizes DEG and disrupts the hydrogen-bond network; sintering forms Cr–O bridges. After high-temperature stages, water’s role in strength diminishes in the model, and an optimal binder content appears for post-sinter strength. More hydroxyl groups in the binder family (2-ethoxyethanol < DEG < triol) correlate with higher early-stage strength in the ReaxFF workflow.

The stage-wise thermal protocol (print at 300 K, cure at 393 K with expansion to a larger cell, burn-out at 900 K with volatile removal, sintering at 1900 K) is chosen to mirror BJP processing sections discussed in the PCCP article, with direct heating between stages as implemented in the simulations. The restraint potential separating two nanoparticles provides a scalar mechanical proxy for how binder chemistry survives each stage, even though it is not a full micromechanical finite-element model of a printed powder bed.

## Limitations

Proof PDFs may differ slightly in layout from the version of record; cite figures from **`[[2019gao-physical-che-reaxff-molecular]]`** when possible. Nanoparticle models and nanosecond trajectories provide mechanistic trends rather than part-scale engineering predictions.

## Relevance to group

van Duin-group **ReaxFF** application to **additive manufacturing** binders; this slug tracks **non-primary** proof bytes.

## Citations and evidence anchors

- DOI: [10.1039/c9cp03585k](https://doi.org/10.1039/c9cp03585k)

## Reader notes (navigation)

- VOR article: [[2019gao-physical-che-reaxff-molecular]]

## Related topics

- [[reaxff-family]]
