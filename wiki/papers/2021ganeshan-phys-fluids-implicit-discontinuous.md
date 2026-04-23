---
id: paper:2021ganeshan-phys-fluids-implicit-discontinuous
type: paper
title: "An implicit discontinuous Galerkin finite element discrete Boltzmann method for high Knudsen number flows"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - method:continuum-or-mesoscale
  - task:method-development
  - scale:multiscale
candidate_tags: []
paper_keywords:
  - keyword:method-development
source_refs: []
doi: "10.1063/5.0041636"
year: 2021
authors:
  - "Karthik Ganeshan, David M. Williams"
venue: "Phys. Fluids 33, 032019 (2021)"
pdf_sha256: "1c270ff97eb5acf5dc693acdef8cc3d3611f3a584e6ca65a3a9da30b344a6652"
pdf_path: "papers/Others/Ganeshan_Williams_PhysicsofFluids_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021ganeshan-phys-fluids-implicit-discontinuous -->

## Summary

This *Physics of Fluids* article develops a **high-order** numerical method for **rarefied gas flows** where the **Navier–Stokes** equations break down and **kinetic** descriptions become necessary. The authors formulate an **implicit** **discontinuous Galerkin finite-element** discretization of the **discrete Boltzmann** **Bhatnagar–Gross–Krook (BGK)** equation for **isothermal** conditions, coupled with **Runge–Kutta** time integration, aiming for **high-order accuracy** in both space and time while retaining compact stencils suitable for complex geometries. The motivating applications include **high Knudsen number** microflows and porous-media regimes where continuum closures are unreliable.

## Methods

This is a **continuum / discrete-velocity Boltzmann** method paper, not atomistic **molecular dynamics**, **ReaxFF**, or **DFT**.

- **Governing model:** **Implicit** **discontinuous Galerkin** **(DG-FEM)** discretization of the **discrete Boltzmann** **Bhatnagar–Gross–Krook (BGK)** equation under **isothermal** conditions, with **Runge–Kutta** time integration (see *Phys. Fluids* for stage counts and stability).
- **Velocity discretization:** Validation uses a **D2Q16** discrete-velocity set; the paper compares **Gauss–Hermite** vs **Newton–Cotes** **quadratures** in the lid-cavity study.
- **Benchmarks:** 2D **Couette** flow at **Kn = 1** to assess spatial order; **lid-driven** **micro-cavity** at **Kn = 1, 2, and 8** to study quadrature choice vs **ray** **effects** at high **Kn** (see `pdf_path`).
- **N/A (by design):** **LAMMPS**/**ReaxFF**, **NVE**/**NVT** **molecular dynamics**, **barostat**, **DFT** — not part of this **kinetic-theory** solver formulation.

## Findings

The method achieves the demonstrated **spatial** order on the **Couette** test. **Micro-cavity** results show how **quadrature** choice affects solutions under strong **nonlinearity** at moderate-to-high **Kn**. The authors motivate **high-order** **Boltzmann** solvers for **porous-media** and **microflow** problems noted in the introduction. **Corpus honesty:** tabulated norms, **Kn**, and **boundary** models should be read from the **version-of-record** **PDF** at `pdf_path`, not this summary alone; see **## Limitations** for isothermal and 3D cost caveats.

## Limitations

The formulation is **isothermal**; extending to thermal flows and industrially relevant **three-dimensional** domains increases cost due to high-order DG and large velocity sets.

## Reproducibility notes

Discrete-velocity Boltzmann implementations require careful reporting of **quadrature** rules, **collision time** scaling with Kn, and **boundary** conditions for microcavity lids; small changes in lid-wall treatment can dominate error at high Kn. When coupling to porous media applications mentioned in the paper, document **grid resolution** relative to mean free path to avoid numerical diffusion masquerading as physical slip.

For the **lid-driven cavity** benchmarks, reproduce the **lid speed**, **Reynolds-like** scaling implied by discrete-velocity parameters, and whether **slip** or **diffuse** wall models are used—continuum analogies break down quickly as Kn rises, and boundary models dominate the solution character. When reporting convergence tables, include **mesh** polynomial degree and **time-step** restrictions imposed by stiffness at high Kn to separate stability limits from modeling error. Finally, archive the **discrete velocity set** definition (D2Q16) and any **normalization** conventions used for distribution functions so independent reimplementations can match reported norms.

## Relevance to group

Co-author Karthik Ganeshan appears on the birnessite Nature Materials paper in this corpus; this entry is continuum Boltzmann methodology rather than ReaxFF atomistics.

## Citations and evidence anchors

## Related topics

- [[2021boyd-nat-effects-interlayer]]
