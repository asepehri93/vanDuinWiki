---
id: paper:2017chowdhury-venue-jp6b12429
type: paper
title: "Extension of the ReaxFF combustion force field toward syngas combustion and initial oxidation kinetics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.6b12429"
year: 2017
authors:
  - "Chowdhury Ashraf"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A"
pdf_sha256: "fe1467aed0c35b8887920ebee84765b86c64dd6afa5badeea0753b2c9365c125"
pdf_path: "papers/Chowdhury_CHO_2017_JPCA.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:combustion
  - keyword:lammps
  - keyword:nvt-simulation
---

<!-- id:paper:2017chowdhury-venue-jp6b12429 -->

## Summary

This Journal of Physical Chemistry A article retrains the widely used Chenoweth et al. CHO-2008 ReaxFF combustion parameter set into an updated CHO-2016 description, coauthored by Chowdhury Ashraf and Adri C. T. van Duin. The authors identify two limitations in CHO-2008 for their targets: inaccurate small-molecule oxidation chemistry relevant to syngas, especially conversion between CO and CO\(_2\), and an overly fast hydrogen abstraction by molecular oxygen from hydrocarbons, which depresses predicted oxidation initiation temperatures relative to expectations. The manuscript expands the DFT-based training set with additional reactions and transition-state geometries along syngas oxidation routes and oxidation initiation pathways, then reoptimizes parameters while aiming to preserve CHO-2008 quality for large hydrocarbon chemistry such as jet-fuel surrogates.

## Methods

**Force-field training (ReaxFF).** Starting from **CHO-2008** (**Chenoweth et al.**), the authors **expand** the **DFT-backed training set** with **reaction energies** and **transition-state geometries** along **syngas oxidation** routes and **hydrocarbon oxidation-initiation** pathways where **CHO-2008** is known to fail—especially **CO ↔ CO₂** interconversion for **small-molecule** oxidation and an **overly facile O₂ hydrogen abstraction** that **suppresses** predicted **oxidation initiation temperatures**. **Reoptimization** yields **CHO-2016** while the manuscript states an explicit goal to **preserve** **CHO-2008**-level behavior for **large-molecule** / **jet-surrogate** chemistry. **QM level**, **weighting**, and **optimizer** details (**least-squares** / **CMA-ES**-style workflows) are documented in the **main text** and **Supporting Information**.

**MD application (validation).** **High-temperature gas-phase** **NVT** **reactive MD** exercises **CHO-2016** on **syngas**, **methane**, **JP-10**, and **n-butylbenzene** for both **oxidation** and **pyrolysis** scenarios (fuel list and qualitative outcomes summarized in the **abstract**). **Supercell compositions**, **initial stoichiometries**, **target temperatures**, **timestep**, **thermostat**, **total simulated times**, and **MD software** are tabulated in the **article + SI**; this wiki page does **not** copy those run cards from the short front-matter extract.

**Static QM** underpins the **fit** and selected **spot checks** rather than serving as a standalone production method. **Electric-field** drives and **enhanced sampling** are **N/A** in the indexed framing of this parametrization paper.

**FF-training blueprint honesty.** **Parent** **CHO-2008** **ReaxFF**; **QM** (**DFT**) **training** structures/energies; **optimization** language (**least-squares** / **CMA-ES**) and **reference** **QM**/**experimental** benchmarks are all in the **article + SI**—this page summarizes intent only.

**MD validation blueprint honesty.** **High-temperature** **reactive molecular dynamics** on **gas-phase** **PBC** supercells uses **NVT** in the abstract’s wording; **LAMMPS** is the usual engine for published **CHO-2016** workflows—confirm in **SI**. **Timestep**, **thermostat**, **equilibration**/**production** durations (**ps**/**ns**), **barostat**/**pressure** if any **NPT** segments exist, and **boundary** conditions beyond **PBC** are **N/A** on this page—copy from the **PDF/SI**.

## Findings

Syngas and methane oxidation simulations with CHO-2016 show substantially improved C\(_1\) chemistry relative to CHO-2008 and resolve the low-temperature oxidation initiation problem attributed to overly facile O\(_2\) abstraction in the older parametrization. For JP-10, Arrhenius parameters for decomposition obtained with CHO-2016 agree with experiment and with CHO-2008 simulation results within the scope claimed in the abstract. For n-butylbenzene, initiation mechanism pathways from CHO-2016 remain in good agreement with both experiment and CHO-2008 outcomes, supporting transferability across fuel classes in the authors’ tests. The article nonetheless acknowledges the vast size of combustion reaction networks and the need for case-by-case assessment beyond the validation suite.

The introduction also contrasts detailed kinetic models for small hydrocarbons with the practical need to simulate complex fuels and fuel mixtures at elevated pressures and in condensed phases where hand-built mechanisms become incomplete, motivating ReaxFF as a reaction-discovery tool that does not require prespecifying every elementary step, while acknowledging that quantum accuracy still limits affordable system sizes and timescales. The article cites enormous computational costs for illustrative ab initio nanoreactor studies as a contrast point for why ReaxFF remains attractive for statistically meaningful reactive sampling despite its empirical approximations.

## Limitations

- Combustion **networks** remain enormous; **transferability** must be assessed case-by-case beyond tested fuels.

## Relevance to group

Landmark **group** publication extending the widely used **CHO ReaxFF** line.

## Citations and evidence anchors

- **DOI:** [10.1021/acs.jpca.6b12429](https://doi.org/10.1021/acs.jpca.6b12429) (`papers/Chowdhury_CHO_2017_JPCA.pdf`).
- Text-aligned pointers: `normalized/extracts/2017chowdhury-venue-jp6b12429_p1-2.txt`

## Reader notes (navigation)

- Same article as proof PDF slug [[2017ashraf-venue-research]]; combustion hub: [[theme-pyrolysis-combustion-organics]], [[reaxff-family]].

## Related topics

- [[2017ashraf-venue-research]]
- [[reaxff-family]]
