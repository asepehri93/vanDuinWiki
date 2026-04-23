---
id: paper:2015wood-venue-jp5b05362
type: paper
title: "Ultrafast Chemistry under Nonequilibrium Conditions and the Shock to Deflagration Transition at the Nanoscale"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reactive-md-generic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:shock-compression
  - keyword:energetic-materials
  - keyword:reactive-md
  - keyword:nve-simulation
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b05362"
year: 2015
authors:
  - "Mitchell A. Wood"
  - "Mathew J. Cherukara"
  - "Edward M. Kober"
  - "Alejandro Strachan"
venue: "J. Phys. Chem. C"
pdf_sha256: "f98642f2e00075af30929dace3681dc04fd115eee1b01aa3ae4e2b6753baa8f2"
pdf_path: "papers/ReaxFF_others/Wood_Cherukara_Strachan_RDX_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2015wood-venue-jp5b05362 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **J. Phys. Chem. C** article identified by `doi` and `pdf_path`. It is not new primary claims by this wiki.

## Summary

Energetic materials often initiate from localized “hot spots” where mechanical work concentrates into nanoscale regions of extreme pressure and temperature. This *J. Phys. Chem. C* article uses large-scale **reactive molecular dynamics** to follow chemistry after **shock-induced collapse** of a **cylindrical nanopore** in crystalline **RDX**, focusing on a shock with **particle velocity ~2 km/s**. The central scientific question is how **nonequilibrium molecular collisions** during pore collapse couple to **exothermic chemistry** on picosecond time scales, and whether that chemistry can seed a self-sustaining reaction front rather than merely heating and quenching a nanoscale hot spot. The framing contrasts **dynamical** loading with **static** thermal hot spots of comparable size and thermodynamic conditions, because continuum-style initiation models frequently bake in assumptions about local equilibration that may fail when gradients are ultrasteep and chemistry is collisionally driven.

## Methods

**LAMMPS ReaxFF** (`papers/ReaxFF_others/Wood_Cherukara_Strachan_RDX_JPCC_2015.pdf`, §2.2) merges **nitramine** and **combustion** ReaxFF lines with **RDX**-reaction training data from prior work. **α-RDX** crystals contain one **cylindrical void** (**10–40 nm** diameter) from replicated **8-molecule** cells; the **40 nm** example extends **~243 nm** along the shock axis with the pore **60 nm** from the impact face. **3D PBC** and a **piston (momentum mirror)** launch shocks. Preparation: minimization, **5 ps** **NPT** (**isobaric–isothermal**) equilibration at **300 K** with a **barostat** active, then **10 ps** **NVT** (**isochoric–isothermal**) equilibration at **300 K**; production is **NVE** after piston impact with **0.1 fs** timestep and **self-consistent ReaxFF charges** (conjugate-gradient to **10⁻⁶** tolerance each step). No thermostat during **NVE** shock propagation. **U_p ≈ 2 km s⁻¹** is tied to **~11 GPa** shock pressure in the defect-free reference discussion. A **static hot spot** at matched thermodynamic state but **without** shock history serves as a control (§2). No electric field or enhanced sampling is used.

**Force-field training:** **N/A —** merged parametrization is taken from cited prior training literature.

**Static QM / DFT:** **N/A —** not the reported primary modality beyond validation references in the ReaxFF section.

## Findings

For **U_p ≈ 2 km s⁻¹**, collapse of a **40 nm** pore drives **deflagration-like** behavior: **collisional**, **multistep** chemistry on **picosecond** scales yields **exothermic** products that sustain heating rather than immediate quench. By **~30 ps** the authors report a **~0.25 km s⁻¹** reaction front **~5 nm** thick emanating from the hot spot (abstract-level numbers). The **static** control does **not** reproduce that **deflagration wave**, underscoring **nonequilibrium shock loading** versus purely **thermal** hot-spot pictures. **Pore size** and **U_p** control localization versus sustained fronts. Discussion notes simplification of real microstructures and ReaxFF limits on quantitative barriers. External **Purdue / LANL** work—reference for **shock** + **energetic-material** reactive MD.

## Limitations

Nanoscale single-pore models simplify real microstructures (defect statistics, polycrystallinity, mesoscale transport). ReaxFF chemistry for energetic materials requires independent validation for quantitative barrier and product distributions.

## Relevance to group

Reference for **shock** and **EM** **reactive MD** adjacent to combustion and initiation mechanics in the wider corpus.

## Citations and evidence anchors

- **DOI:** [10.1021/acs.jpcc.5b05362](https://doi.org/10.1021/acs.jpcc.5b05362) — `papers/ReaxFF_others/Wood_Cherukara_Strachan_RDX_JPCC_2015.pdf`.

## Related topics

- [[reaxff-family]]
