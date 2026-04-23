---
id: paper:2015psofogiannakis-surface-scie-development-reaxff
type: paper
title: "Development of a ReaxFF reactive force field for Si/Ge/H systems and application to atomic hydrogen bombardment of Si, Ge, and SiGe (100) surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - material:widegap-semiconductor
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reaxff-application
  - keyword:catalysis-surface
candidate_tags: []
source_refs: []
doi: "10.1016/j.susc.2015.08.019"
year: 2015
authors:
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
venue: "Surface Science"
pdf_sha256: "53a56a5eec80c54c5a5cf1c766b97249a47a2dbb0c80b78b6813418ee1a6b511"
pdf_path: "papers/Psofogiannakis_SiGeH_SurfSci_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015psofogiannakis-surface-scie-development-reaxff -->

## Summary

Psofogiannakis and van Duin extend an established **Si/H ReaxFF** parameterization with **germanium** chemistry—**Ge–Ge**, **Si–Ge**, and **Ge–H** interactions—by training against **quantum chemistry** data that emphasize **relative** differences between **Ge** and **Si** analogs (*Surface Science*, DOI `10.1016/j.susc.2015.08.019`). The scientific target is **plasma-processing** and **surface** **hydrogenation** of **group-IV** semiconductors: **atomic hydrogen** bombardment of **(100)** **diamond-cubic** **Si**, **Ge**, and **SiGe** surfaces at technologically relevant **kinetic energies**. By preserving prior **Si** training while adding **Ge** terms through **difference fitting**, the authors aim to keep **compatibility** with existing **Si** **ReaxFF** datasets while enabling **alloy** and **Ge**-specific **etching** pathways that differ in **bond strength** and **lattice openness**.

The introduction also places this work in a process-engineering context: H-plasma treatment is used for passivation and cleaning, but can induce near-surface damage through hydrogenation-driven etching and subsurface defect formation. The ReaxFF extension is therefore motivated as a mesoscale bridge between expensive ab initio approaches and nonreactive empirical models, enabling trajectory-level comparisons of composition and incident-energy effects that matter for semiconductor process windows.

## Methods

### Force-field training

**Parent field:** established **Si/H ReaxFF** augmented with **Ge–Ge**, **Si–Ge**, and **Ge–H** interactions. **QM reference:** **Jaguar DFT** with **B3LYP** and **LAV3P\*\*** on clusters and related models. **Training set:** dissociation curves, angle/torsion scans, and geometries benchmarked in **Table 1**-style comparisons emphasizing **Ge–X** versus **Si–X** energetics. **Optimization:** parameters adjusted to match those **QM** targets while **not degrading** prior **Si** accuracy (difference-fitting philosophy described in *Surface Science*).

### MD application (atomistic dynamics)

**Reactive MD** with **ReaxFF** simulates **monoenergetic atomic H** bombardment of **diamond-cubic** **Si(100)**, **Ge(100)**, and **SiGe(100)** **slabs** in **NVT** cells with **in-plane periodic boundary conditions** and vacuum along the surface normal (**slab** geometry, *Surface Science*). **Engine, timestep, thermostat coupling, substrate temperature, slab sizes, equilibration versus bombardment staging, and the incident-energy grid** are specified in the article’s **Computational Methods**; they are **not** present on the short local extract used for curation.

**Barostat / hydrostatic pressure:** **N/A —** constant-volume **slab** bombardment.

**Electric field / enhanced sampling:** **N/A**.

## Findings

**Composition trends:** **Si(100)** shows more facile **surface and subsurface H uptake**, **H\(_2\)** formation, and **etching-related** responses than **Ge(100)** under comparable **atomic H** bombardment, consistent with **bond-strength** and **lattice openness** differences highlighted in the abstract. **SiGe** is **intermediate**, with **alloy**-specific **surface disordering** that changes how **H** interacts with the surface. **Sensitivity:** reaction propensity varies with **incident kinetic energy** and **composition** along the scanned conditions. **Limitations:** **monoenergetic atomic H** simplifies real **H-plasma** mixtures (**ions**, **molecules**, broad energy distributions); **ReaxFF** remains approximate relative to **DFT** for rare channels where the article provides cross-checks.

- **Comparative outcome framing:** The paper uses one force field across Si, Ge, and SiGe to isolate composition-driven differences without changing the reactive model family between cases.
- **Mechanistic emphasis from abstract/introduction:** Surface adsorption, subsurface incorporation, molecular hydrogen release, and etching are treated as coupled outcomes of bombardment chemistry rather than independent observables.
- **Corpus honesty:** The local p1-2 extract establishes the training philosophy and application scope, while full numeric bombardment protocol values and trajectory statistics should be read from the complete article text.

## Relevance to group

**van Duin**-group **ReaxFF** extension to **Ge** semiconductors with explicit **H-plasma**-relevant dynamics.

## Citations and evidence anchors

DOI `10.1016/j.susc.2015.08.019`.

## Related topics

- [[reaxff-family]]
