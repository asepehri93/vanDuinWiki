---
id: paper:20180000-0002-5255-7340-j-phys-chem-isotope-effects
type: paper
title: "Isotope effects in water: differences of structure, dynamics, spectrum, and proton transport between heavy and light water from ReaxFF reactive force field simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:validation
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:water-interfaces
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.8b02379"
year: 2018
authors:
  - "Weiwei Zhang"
  - "Xing Chen"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "25bae5ddb5b60e1c70e897fab2755592c002e85a0b91018ce308942cef0b5014"
pdf_path: "papers/Zhang_HeavyWater_JPC_Letters_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20180000-0002-5255-7340-j-phys-chem-isotope-effects -->

## Summary

**ReaxFF reactive MD** with an isotope-aware parametrization strategy (embedding **H vs D differences** in force-field terms so classical simulations can capture isotope effects without full path-integral MD) is used to compare **light vs heavy water** structure, dynamics, vibrational spectra, and **Grotthuss proton transport**. The letter reports structural distinctions between **D\(_3\)O\(^+\)** and **H\(_3\)O\(^+\)** in bulk solution and reproduced **diffusion constants** alongside proper **hopping** behavior. The motivation is practical: **isotope labeling** is a standard probe in **reaction** and **transport** studies, but **QM** treatments of **nuclear quantum effects** are expensive at scale; a **ReaxFF** route that preserves the **ordering** of key observables between **H\(_2\)O** and **D\(_2\)O** offers a compromise for large **aqueous** systems.

## Methods

### A — Force-field training / isotope-aware parametrization

- **Base model:** **CHON-2017_weak** **ReaxFF** **aqueous** parameterization for **light water** (abstract/extract).
- **Heavy water extension:** **reparameterized** **O–H** **bond**, **van der Waals**, and **hydrogen-bond** terms starting from **CHON-2017_weak** so classical MD can reproduce key **H vs D** differences without **path-integral** sampling (letter narrative; **full** parameter tables in **Supporting Information**).

### B — Reactive molecular dynamics (bulk H\(_2\)O vs D\(_2\)O)

- **Engine:** **ReaxFF** **MD** comparing **bulk** **light** and **heavy** water under **identical** thermodynamic protocols aside from **isotope** labels (ensemble, timestep, cutoffs, and trajectory lengths in the **JPCL** text/**SI**).
- **Observables:** **radial distribution functions** (**O–O**, **O–H**, **H–H**); **self-diffusion** coefficients; **vibrational** spectra; **Grotthuss**-style **proton/deuteron** transport and **Eigen/Zundel**-related structural discussion (**H\(_3\)O\(^+\)** vs **D\(_3\)O\(^+\)** in bulk).
- **Electrostatics / charge equilibration:** standard **ReaxFF** **QEq**-class treatment as implemented for the **CHON-2017_weak** line—**frequency** and **cutoffs** per article/**SI**.

### C — Pure quantum benchmarks

- **Not the focus:** the letter emphasizes **classical** **ReaxFF** with **isotope-aware** parameters rather than **AIMD** or **PIMD** for this study.

### MD protocol (*JPCL* letter + SI)

- **Engine / code:** **LAMMPS** **molecular dynamics** with **ReaxFF** (standard deployment for the **CHON-2017_weak** line).
- **System size & composition:** **Bulk** **H\(_2\)O** and **D\(_2\)O** boxes with **>10⁶** **atom** capability highlighted in the letter; exact counts in **SI**.
- **Boundaries / periodicity:** **3D PBC** cubic cells.
- **Ensemble:** **NVT** **canonical** trajectories for bulk benchmarks (per **paper_keywords** and letter narrative).
- **Timestep / duration:** Femtosecond **timestep** and **nanosecond**-scale **production** segments as tabulated in **SI**.
- **Thermostat:** **Nose–Hoover** or **Berendsen** coupling as listed in **Methods**/SI.
- **Barostat:** **N/A — hydrostatic barostat** not used for these **constant-volume** bulk water cells unless **SI** documents an **NPT** relaxation—verify in **PDF**.
- **Temperature:** Ambient and elevated **K** setpoints used for RDF/diffusion comparisons (see letter).
- **Pressure:** **N/A — external pressure** control not used for the cited **NVT** bulk benchmarks; confirm exceptions in **SI**.
- **Electric field:** **N/A — electric field** not applied.
- **Enhanced sampling:** **N/A — umbrella / metadynamics** not indicated.

## Findings

- Classical ReaxFF MD at large system/time scales reproduces key **differences** between heavy and light water emphasized in the abstract (diffusion ordering, spectroscopic shifts, transport mechanisms).
- **D\(_3\)O\(^+\)** vs **H\(_3\)O\(^+\)** structural differences appear in bulk heavy vs light water.
- **Diffusion constants** for light and heavy water align with experimentally expected trends; **Grotthuss hopping** for proton transport is described as captured appropriately.
- The approach is framed as enabling isotope-labeled studies of reactions and transport in complex aqueous environments.
- Side-by-side **H/D** comparisons help separate **mass-dependent** kinetic effects from **electronic** structure effects that would require higher-level **QM** or **path-integral** sampling if treated fully.


## Limitations

Letter format—methods compressed; full SI should be consulted for parametrization detail and numerical settings.

**Curation note:** paired proof-ingest sibling [[20180000-0002-5255-7340-x-isotope-effects]] may differ only in PDF bytes; when both exist, prefer the **VOR** pagination for citations and treat this page as the science summary tied to DOI `10.1021/acs.jpclett.8b02379`. Re-run `scripts/report_paper_richness.py` after corpus PDF swaps so Stage A backlog stays aligned with wiki bodies.

## Relevance to group

Extends the Zhang/van Duin aqueous ReaxFF line to **isotope effects** relevant for spectroscopy and reaction mechanism tracing.

## Reader notes (navigation)

Proof sibling: [[20180000-0002-5255-7340-x-isotope-effects]].

## Citations and evidence anchors

- DOI: `10.1021/acs.jpclett.8b02379`.

## Related topics

- [[reaxff-family]]
