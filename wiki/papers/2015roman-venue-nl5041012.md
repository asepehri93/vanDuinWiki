---
id: paper:2015roman-venue-nl5041012
type: paper
title: "Mechanical properties and defect sensitivity of diamond nanothreads"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - method:reaxff
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1021/nl5041012"
year: 2015
authors:
  - "Ruth E. Roman"
  - "Kenny Kwan"
  - "Steven W. Cranford"
venue: "Nano Letters"
pdf_sha256: "2d0e96ea1c7642051157fb27a64b17ae7f297e2d2a6597c9183facf02017de2f"
pdf_path: "papers/ReaxFF_others/Roman_Kwan_Cranford__Carbon_Nanothreads_NanoLetters_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015roman-venue-nl5041012 -->

## Summary

**Diamond nanothreads** are hydrogen-saturated, **sp³** one-dimensional carbon structures synthesized from benzene under high pressure. Roman, Kwan, and Cranford (*Nano Lett.* **2015**, DOI `10.1021/nl5041012`) use **ReaxFF** molecular dynamics to estimate **Young’s modulus (~850 GPa)**, **tensile strength (26.4 nN when expressed as a 1D force metric)**, **strain at failure (~14.9%)**, and **bending rigidity (~5.35×10⁻²⁸ N·m²)**, and highlight a **tenacity (~4.1×10⁷ N·m/kg)** tied to the **1D architecture**. The modeled thread is described as a hydrogenated **(3,0)**-like nanotube variant with distributed **Stone–Wales** (**C–C dimer 90° rotation**) defects. **Steered molecular dynamics (SMD)** sweeps **1–4** defects to probe how **defect density** modulates strength, stiffness, and extensibility.

## Methods

**MD application (mechanical testing).** **Interaction model:** **ReaxFF** for **C/H** with bond-order-dependent reactivity suitable for bond rupture (letter + SI references to the ReaxFF literature). **Engine:** **LAMMPS** is used in the Supporting Information workflow referenced by the article (see `pdf_path`). **Structural validation:** a **~8 nm** periodic thread segment is equilibrated at **300 K** for **~1 ns**; the **radial distribution function** shows a nearest-neighbor **C–C** peak near **~1.52 Å** (sp³ character) and a dominant **~1.1 Å** peak consistent with **1:1 C:H** stoichiometry (extract). **Mechanical protocols:** (i) **quasi-static** cycles of incremental axial strain with energy minimization between steps; (ii) **dynamic SMD** tensile tests; **stress** from a **virial** formulation, with an equivalent **1D stress in force units** reported to reduce cross-section ambiguity (letter). **Representative failure point (two-defect model):** maximum stress **134.3 GPa** or **26.4 nN** and strain **14.9%** at failure in the quasi-static analysis quoted in the extract; stiffness taken from a **linear fit up to 4%** strain. **Bending rigidity** via **energy-minimization molecular mechanics** (letter). **Stone–Wales sensitivity:** additional SMD on models with **1–4** defects; energetic penalty **~12 kcal/mol per added defect** in the quoted analysis. **Boundaries:** **1D periodic** boundary along the thread axis with vacuum padding transverse to the axis (standard nanowire setup; confirm cell vectors in **`pdf_path`**). **Ensemble:** **NVT** thermalization at **300 K** for the RDF validation segment; SMD segments impose mechanical driving—**thermostat coupling during SMD** as specified in SI. **Timestep:** **fs**-scale value in **SI** (not duplicated numerically here). **Barostat:** **N/A** — uniaxial mechanical tests, not hydrostatic **NPT** production. **Pressure / electric field / replica enhanced sampling:** **N/A** for the headline tensile workflow (SMD is steered MD, not umbrella sampling).

**Force-field training:** **N/A** — the study **uses** published **ReaxFF** carbon/hydrogen parametrization; it does not report a new global refit.

**Static QM / DFT:** **N/A** — QM benchmarks are cited comparatively but are not the paper’s primary numerical engine.

## Findings

**Benchmark moduli/strength:** The abstract quotes **Young’s modulus ~850 GPa**, **strength 26.4 nN**, **extension 14.9%**, **bending rigidity 5.35×10⁻²⁸ N·m²**, and **tenacity 4.1×10⁷ N·m/kg**, tied to the **1D** architecture relative to nanotube/graphene literature comparisons in the letter.

**Energetic reference:** Potential energy per atom differs from a **graphane** sheet reference by **<~1%**, argued as evidence the constructed thread is a **stable allotrope** relative to that baseline (extract).

**RDF vs experiment:** Simulated **RDF** peaks are **sharper** than bundled experimental threads because the analysis uses a **single** periodic strand without inter-thread correlations (extract).

**Defect sensitivity:** **Stone–Wales** defect count (**1–4**) modulates **strength**, **stiffness**, and **extensibility** in SMD; adding a defect raises thread energy by about **12 kcal/mol** in the quoted estimate.

**Limitations (model scope):** Idealized **periodic** threads omit experimental **twist**, **terminations**, and **bundle** disorder; **SMD strain rates** exceed laboratory rates.

## Limitations

**ReaxFF** accuracy for ultrahigh-strength carbon phases remains application-dependent. **SMD** strain rates and **idealized** periodic threads omit surfaces, **twist**, and experimental **bundle** disorder beyond what the letter benchmarks explicitly claim.

## Relevance to group

Reference-quality **reactive carbon nanomechanics** example parallel to group **ReaxFF** work on **sp²/sp³** carbon systems.

## Reader notes (navigation)

- Alternate ingest: [[2015mechanical-venue-research]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1021/nl5041012](https://doi.org/10.1021/nl5041012)
