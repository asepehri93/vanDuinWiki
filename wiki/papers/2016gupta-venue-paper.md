---
id: paper:2016gupta-venue-paper
type: paper
title: "Carbonization with misfusion: Fundamental limits of carbon fiber strength revisited"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - method:reaxff
  - method:classical-md
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1002/adma.201603009"
year: 2016
authors:
  - "Nitant Gupta"
  - "Vasilii I. Artyukhov"
  - "Evgeni S. Penev"
  - "Boris I. Yakobson"
venue: "Advanced Materials"
pdf_sha256: "83556ece6335ef3428a50149939f2a1c23e3406f9f3f05ab883b823e65a2bf1c"
pdf_path: "papers/ReaxFF_others/Gupta_D_Loops_AdvMat_2016.pdf"
extraction_quality: "partial"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:reactive-md
  - keyword:2d-materials
---
<!-- id:paper:2016gupta-venue-paper -->

## Summary

The paper introduces **D-loops**, a **topological defect** proposed to arise naturally from **PAN carbonization** misfusion of **graphene nanoribbon** segments, and uses **molecular dynamics** to quantify how D-loops reduce **tensile strength** in graphitic models relative to ideal graphite expectations. The narrative connects **topological** constraints in the carbon network to **stress concentration** patterns that are difficult to capture with purely **misalignment**-based fiber-strength models.

## Methods

- **MD engine:** **LAMMPS**; visualization with **VMD** and **Ovito** (as stated).
- **Potentials:** **ReaxFF** for **mechanical fracture / stress** calculations on **sp² carbon** nanostructures; **AIREBO** used to **build/prepare D-loop geometries**; a **nitrogen-extended ReaxFF** is noted for **length-contraction** simulations (per main text / SI reference).
- **Loading / analysis:** **Uniaxial tensile** tests on periodic and non-periodic D-loop supercells; **von Mises stress** via **per-atom stress** with **atomic volumes from Voronoi tessellation** (Ovito).
- **Parameter sweeps:** Variation of **D-loop spacing**, **Burger’s vector magnitude**, and **loading orientation** with multiple independent runs (median/quartiles reported for strength statistics).

**Boundary conditions**, **strain rate**, **ensemble** (**NVT**/**NVE** segments in tensile pulls), **timestep**, **thermostat** parameters, and **supercell** dimensions are tabulated in the **Adv. Mater.** article and **SI** (**numerical values N/A — not copied into this wiki page**). **Equilibration / production segment lengths (ps/ns) for each tensile or heating leg:** **N/A — not copied into this wiki page**; see *Adv. Mater.* and **SI** tables. **Barostat / hydrostatic pressure:** **N/A — not the focus** of the uniaxial fracture protocols summarized here. **Temperature** setpoints for main-text pulls vs **SI** ribbon-contraction studies: **see PDF**.

## Findings

- D-loops can **strongly reduce breaking strength** (reported up to **~4×** reduction vs idealized expectations in the study’s models), motivating them as a **new practical strength ceiling** for carbon fibers beyond older **Reynolds–Sharp** misalignment pictures alone.
- At small separations, paired D-loops behave similarly to an **equivalent hole**; at larger separations the defects enter a **dilute** regime where **orientation-dependent** strength follows a **cosine/sine angular fit** (Eq. (1) in the paper).
- **Length contraction** of **N-terminated nanoribbons** upon heating (supporting information simulations) ties D-loop formation to **carbonization**-relevant **ribbon shrinkage** behavior.

The **Adv. Mater.** discussion frames D-loops as a **practical** upper bound on **fiber strength** when **misfusion** is unavoidable during **pyrolysis**, motivating process routes that limit **topological** defect density rather than only **crystallite orientation**.

**Compared** to idealized graphite strength targets, the **simulation** models show large **reductions** once **D-loops** are embedded. **Sensitivity** to **D-loop** spacing, **Burger’s vector** magnitude, and load **orientation** is summarized by the cosine/sine angular law in the dilute regime. **Limitations** include idealized **ribbon** supercells vs industrial fiber texture; see **Limitations** below and the **PDF** for author-stated caveats. **Experimental** validation is discussed at the literature level in *Adv. Mater.* rather than through new measurements on this wiki page.

## Limitations

- Fiber **real microstructures** are more complex than isolated ribbon models; **kinetic pathways** to D-loops in industrial carbonization are discussed qualitatively.
- Strength numbers are **simulation-model dependent** (force-field choice, strain rate, defect placement).

## Relevance to group

**ReaxFF + LAMMPS** fracture study on **carbon** defects; useful cross-reference for **mechanical failure** of **sp²** systems (distinct from van Duin-group parameterization line, Rice authors).

## Citations and evidence anchors

- DOI: [10.1002/adma.201603009](https://doi.org/10.1002/adma.201603009) — *Adv. Mater.* **28**, 7323–7331 (2016).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
