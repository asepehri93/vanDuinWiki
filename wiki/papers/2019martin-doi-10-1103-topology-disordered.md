---
id: paper:2019martin-doi-10-1103-topology-disordered
type: paper
title: "Topology of Disordered 3D Graphene Networks"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevLett.123.116105"
year: 2019
authors:
  - "Jacob W. Martin"
  - "Carla de Tomas"
  - "Irene Suarez-Martinez"
  - "Markus Kraft"
  - "Nigel A. Marks"
venue: "Phys. Rev. Lett."
pdf_sha256: "4eb6692c680de31a3ea711c58709660be9f024903434280468131bc7742c372d"
pdf_path: "papers/Others/PhysRevLett.123.116105.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019martin-doi-10-1103-topology-disordered -->

## Summary

Disordered carbons are frequently conceptualized as **three-dimensional networks of graphene fragments**, but the prevailing **local curvature motif**—**fullerene-like** positive Gaussian curvature from pentagons, **schwarzite-like** negative curvature from heptagons/octagons, or **ribbon-like** nearly flat segments—has remained controversial. This *Physical Review Letters* article analyzes **nanoporous and glassy carbon** atomistic models that were previously shown to reproduce a broad suite of experimental observables (imaging, diffraction, porosity, mechanics, and thermal transport in the cited prior work). Rather than relying only on ring statistics, the authors apply a **surface mesh** construction to classify topology and **global curvature contributions**, then connect mesh-level features to **local bonding environments** including **sp-** and **sp\(^3\)**-rich defects.

## Methods

**4 — PRL post-processing of imported atomistic models (not a new MD “production” study in this Letter).** The *Physical Review Letters* **reuses** disordered-carbon **atomistic** **networks** (~**32,000** **atoms**, **0.5–1.5 g cm⁻³**) **made** **earlier** with **self-assembly** / **annealed** **molecular** **dynamics** and **already** **benchmarked** against **HRTEM**, **diffraction**, **porosimetry**, **mechanics**, and **transport** in **cited** **prior** work. This **Letter** then applies a **triangular** **surface** **mesh** to each **structure** (after **Franzblau**-style **ring** detection to **nonagons** in the main text) and **maps** **angular** **defects** to **signed** **Gaussian** **curvature** **patches** on the **mesh**, separately **treating** **sp**- and **sp³**-**tagged** **perimeter**/**tetrahedral** **sites** **off** the **sp²** **surface** **graph**. **ReaxFF**-specific **force-field** **development** in this **file**:** **N/A**; **the** **interatomic** **model** **lives** in the **earlier** **MD** **publications** **cited** **as** the **source** of the **networks**. **A** **fresh** **blueprint**-**style** **LAMMPS** **table** **(timestep,** **NVT,** **thermostat**)** for** **this** **PRL** **is** **N/A** because **no** **new** **time**-**marching** **trajectory** **is** **reported** **here**—**only** **geometric** **post-processing** **on** **static** **frames** **imported** from **those** **studies**. **Shear** / **shock** / **E-field** **in** a **pristine** **MD** **sense**:** **N/A** for **this** **Letter**’s **evidence** **chain**. **DFT** in this **PRL** as a **primary** **result**:** **N/A**—**the** **mesh** **analysis** is **classical** **geometry** on **classical** **carbon** **models**.

## Findings

**1 — Outcomes & mechanisms (mesh-level topology).** **Negative** **Gaussian** **curvature** **(saddle**-**like** **patches**)** **dominates** the **global** **curvature** **budget** **in** the **analyzed** **disordered** **3D** **graphene** **networks**, **whereas** **fullerene**-**like** **positive** **curvature** **and** **near**-**flat** **ribbon** **segments** **are** **present** **but** **subdominant** **in** the **mesh** **histograms** **reported** in the **PRL** **(see** **main**-**text** **figures**)**. **sp**-**rich** and **sp³**-**rich** **defect** **atoms** **track** to **line**-**like** and **screw**-**like** **junctions** that **terminate** **free** **edges** and **stitch** **low**-**curvature** **ribbons** into **3D** **porous** **morphology**. **2 — Comparisons.** The **work** **contrasts** with **classical** **ring**-**counting** / **Euler**-**style** **arguments** **alone** by **showing** that **all** **three** **curvature** **classes** **coexist** in **the** **same** **self**-**consistent** **disordered** **carbon** **morphology** at **laboratory**-**relevant** **densities** **(per** the **PRL** **and** the **cited** **model**-**vs**-**experiment** **agreement** **in** **earlier** **work**)**. **3 — Sensitivity & levers.** **Curvature** **partitions** **at** **fixed** **mass** **density** **are** **expected** to **depend** on **the** **generative** **(anneal)** **protocol** **(temperature** **path,** **quench** **rate,** **and** **similar** **kinetic** **levers** **in** the **source** **MD**)**; **this** **Letter** **flags** that **pathway** **as** a **sensitivity** **axis** for **comparing** **future** **models**. **4 — Authored** **limitations** **/ outlook** are **tied** to **which** **3D** **graphene**-**like** **networks** are **admitted** **into** the **test** **set**; **if** a **synthesis** **pathway** **favors** **one** **topological** **element** over **another**, the **curvature** **mix** **shifts** **(see** **PRL** ** discussion** and **our** **##** **Limitations**)**. **5 —** **Corpus** **/ KB** **honesty** — the **PRL** **reuses** **imported** **configurations**; **do** **not** **treat** **this** **wiki** **as** a **source** of **independent** **synthetic** **carbon** **dynamics** **without** **consulting** the **generator** **papers** **cited** **in** the **PRL** **bibliography**.

## Limitations

Conclusions are conditioned on the **specific generative MD protocol** used to build the model carbons; different formation pathways could yield different curvature partitions even if bulk densities match.

## Reproducibility notes

The Letter explicitly ties conclusions to **large** disordered networks (~**32,000** atoms) spanning **0.5–1.5 g cm\(^{-3}\)**; smaller soot-like clusters may not exhibit the same curvature statistics. When coupling these diagnostics to **ReaxFF** pyrolysis trajectories, treat mesh extraction as a **post-processing** step that depends on robust **surface** identification from noisy atomistic configurations—implementation details (smoothing, mesh density) can shift measured curvature histograms. If reproducing figures, track the mesh **resolution** and any **smoothing** radius applied before computing Gaussian curvature histograms, because discretization can artificially broaden peaks.

## Relevance to group

Provides structural diagnostics for disordered carbon morphologies that may complement reactive MD studies of carbonization or pyrolysis.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevLett.123.116105](https://doi.org/10.1103/PhysRevLett.123.116105)

