---
id: paper:2021zhang-npj-computat-multi-objective-parametrization
type: paper
title: "Multi-objective parametrization of interatomic potentials for large deformation pathways and fracture of two-dimensional materials"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:ml-atomistic
  - method:classical-md
  - material:tmd
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:2d-materials
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-021-00573-x"
year: 2021
authors:
  - "Xu Zhang"
  - "Hoang Nguyen"
  - "Jeffrey T. Paci"
  - "Subramanian K. R. S. Sankaranarayanan"
  - "Jose L. Mendoza-Cortes"
  - "Horacio D. Espinosa"
venue: "npj Computational Materials"
pdf_sha256: "1ffe124100cdbe1129f71d140f6868f98807a713980dcb7edc014e2a32467f84"
pdf_path: "papers/Others/Zhang_Paci_Mendoza_npjCompMat_2D_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2021zhang-npj-computat-multi-objective-parametrization -->

## Summary

Zhang et al. present a multi-objective genetic-algorithm framework for fitting interatomic potentials when large-strain and fracture behavior matters, not only harmonic elastic properties. The abstract explains that the workflow combines training and screening property sets with correlation and principal-component analysis to decide which observables should enter optimization, enabling iterative refinement of objectives. Potentials compared include Buckingham, Stillinger–Weber, Tersoff, and a modified reactive empirical bond-order form for transition-metal dichalcogenides (REBO-TMDC). Using monolayer MoSe₂ as a case study, the authors report strong reproduction of training and screening metrics and favorable transferability tests, concluding that Tersoff performs best overall because of greater functional flexibility embedded in its form. The introduction further states that the evolutionary NSGA-III optimizer avoids dependence on gradient computation, so it can be applied to arbitrary potential functional forms while searching Pareto fronts in the criterion space.

## Methods

**1 — MD application (validation trajectories in this study).**
- Engine/code: LAMMPS is used for classical molecular dynamics validation of fitted potentials.
- System size and composition: monolayer TMDC test systems centered on MoSe2 are used for deformation and fracture-oriented evaluation; the exact atom counts/supercell dimensions are not specified in this note.
- Boundaries/periodicity: N/A — explicit periodic boundary condition setup and constrained directions are not stated in the indexed text used for this page; see the version-of-record PDF for the exact boundary specification.
- Ensemble: N/A — explicit NVE/NVT/NPT assignment is not stated in the indexed text used for this page.
- Timestep: N/A — the MD timestep value is not stated in the indexed text used for this page.
- Duration/stages: N/A — equilibration and production run durations are not stated in the indexed text used for this page.
- Thermostat: N/A — thermostat algorithm and damping constants are not stated in the indexed text used for this page.
- Barostat: N/A — pressure-control algorithm is not stated in the indexed text used for this page.
- Temperature: N/A — absolute simulation temperature or ramp schedule is not stated in the indexed text used for this page.
- Pressure: N/A — pressure target/stress-control details are not stated in the indexed text used for this page.
- Electric field: N/A — no external electric field protocol is described for this parameterization workflow.
- Replica/enhanced sampling: N/A — no umbrella/metadynamics/replica-exchange protocol is described for this workflow.

**2 — Force-field training.**
- Parent FF/elements: the paper compares Buckingham, Stillinger-Weber, Tersoff, and modified REBO-TMDC style interatomic forms for TMDC materials.
- QM reference: DFT-derived reference energetics/structures are used as fitting targets for the MoSe2-centered case study.
- Training set: the objective set includes both training and screening properties selected to cover elastic response plus large-deformation/fracture-relevant behavior.
- Optimization: a multi-objective NSGA-III genetic algorithm is used to search Pareto-optimal parameter sets; objective reduction uses correlation and principal-component analysis.
- Reference data used: the fit and screening process is benchmarked against DFT and literature-reported property targets discussed in the article.

**3 — Static QM/DFT-only block.**
N/A — this page summarizes an interatomic potential parameterization workflow rather than a standalone new DFT study.

## Findings

- **Outcomes and mechanisms:** For monolayer MoSe2, the calibrated potentials reproduce the chosen training and screening targets with good fidelity and retain transfer behavior in deformation-oriented tests. The proposed mechanism-level claim is methodological: large-strain/fracture behavior is captured better when optimization includes properties beyond near-equilibrium elastic data, so parameter sets are selected for broader response rather than only harmonic agreement.
- **Comparisons:** Across Buckingham, Stillinger-Weber, Tersoff, and modified REBO-TMDC candidates, the study reports the strongest overall performance for Tersoff in this benchmark. The multi-objective Pareto workflow is also compared against weighted-sum and unweighted-sum scalarizations, with the paper arguing Pareto selection better preserves non-dominated tradeoff solutions.
- **Sensitivity and design levers:** The most important lever is objective-set design. Correlation/PCA-guided pruning of candidate metrics reduces redundant objectives, and the resulting parameter ranking depends on which deformation/fracture-relevant targets are retained in the optimization and screening pool.
- **Limitations and outlook (as authored):** Conclusions are tied to the tested 2D TMDC benchmark domain and to the selected empirical functional families; transfer to unrelated chemistries or reactive event classes is not established here. The workflow is positioned as reusable for other materials, but each new system still requires system-specific objective construction and re-optimization.
- **Corpus honesty:** This wiki page is grounded in the indexed article-level content and does not restate every numeric validation table or MD control parameter; readers should consult the version-of-record PDF for full protocol constants and figure-by-figure values.

## Limitations

The work focuses on classical empirical forms for mechanical properties; explicit chemistry, charge transfer, and ReaxFF-scale reactivity are outside the primary scope even though a modified REBO-TMDC potential is discussed.

The discussion of weighted-sum scalarizations versus Pareto-front methods is relevant whenever force fields are fit to multiple objectives, including reactive parameterizations, even though this article’s benchmarks are classical. Readers should not confuse the REBO-TMDC acronym here with CHO ReaxFF combustion databases: the paper’s REBO variant targets TMDC mechanics rather than organometallic reaction pathways.

## Relevance to group

Northwestern/Argonne/MSU collaboration on classical potential fitting for 2D mechanics—useful corpus context next to ReaxFF-centric fracture and TMD notes, though not a van Duin-group publication.

## Reader notes (navigation)

- [[theme-2d-epitaxy-growth]]
- Classical MD and TMD mechanics concepts adjacent to [[reaxff-family]] applications

## Citations and evidence anchors

DOI: [10.1038/s41524-021-00573-x](https://doi.org/10.1038/s41524-021-00573-x)
