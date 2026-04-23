---
id: paper:2021dong-hyun-kim-acs-molecular-dynamics
type: paper
title: "Molecular Dynamics Simulation of Silicon Dioxide Etching by Hydrogen Fluoride Using the Reactive Force Field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - material:oxide
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:dft-static
source_refs: []
doi: "10.1021/acsomega.1c01824"
year: 2021
authors:
  - "Dong Hyun Kim, Seung Jae Kwak, Jae Hun Jeong, Suyoung Yoo, Sang Ki Nam, YongJoo Kim, Won Bo Lee"
venue: "ACS Omega 2021, 6, 16009-16015"
pdf_sha256: "c3d27a6cdb26826a0338b2e4f364cb381580f9aeff55e9a5e541befaea08f3a3"
pdf_path: "papers/ReaxFF_others/kim-et-al-2021-molecular-dynamics-simulation-of-silicon-dioxide-etching-by-hydrogen-fluoride-using-the-reactive-force.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021dong-hyun-kim-acs-molecular-dynamics -->

## Summary

Dry etching of silicon dioxide with hydrogen fluoride is central to semiconductor patterning, and atomistic models that capture bond formation and cleavage are needed to complement continuum reactor models. Kim et al. develop a Si/O/H/F reactive force field in the ReaxFF formalism specifically to study HF etching of SiO₂ surfaces. Quantum training data come from density functional theory and include reactant and product clusters, bond dissociation scans, valence-angle distortions, and reactions between SiO₂ clusters and slabs with HF. After optimization, ReaxFF energies and structures are reported to match the QM training sets well enough to proceed to production molecular dynamics. The authors then bombard SiO₂ substrates with energetic HF molecules and analyze how etching yield and counts of reaction products depend on the incident energy of HF, aiming to expose atomistic surface reaction sequences during etching. The introduction motivates the work by noting that many prior plasma and etching MD studies used specialized empirical potentials for subsets of halogen chemistry, whereas ReaxFF’s bond-order plus electronegativity-equalization framework is intended to treat concurrent covalent and ionic contributions in Si/O/H/F environments relevant when fluorine participates as reactive anionic species at surfaces.

## Methods

### Force-field training (ReaxFF for Si–O–H–F)

Parameterization follows the standard ReaxFF workflow: assemble DFT reference data for Si–O–H–F chemistry including dissociation and angular distortions; optimize bond, angle, and higher-order ReaxFF terms against those references; and validate on held-out configurations described in the article and Supporting Information. The published workflow states that prior Si/O/H/F parameterizations existed for systems such as silica and fluoropolymers but required reoptimization of Si/O/F bond terms and Si–F and H–F bond parameters together with F–Si–F and F–Si–O angle terms against QM training sets, optimized in their implementation using a covariance-matrix adaptation evolution strategy (CMA-ES) as referenced in the Methods section. Quantum training sets include reactant and product **structures**, **bond** dissociation, valence-angle distortions, and reactions of SiO₂ **clusters** and a SiO₂ **slab** with **HF** (as summarized in the abstract in `pdf_path`).

### MD application (reactive etching of α-cristobalite SiO₂)

- **Engine / code:** **Reactive molecular dynamics** with the fitted **ReaxFF**; implementation in `pdf_path` (LAMMPS/PuReMD-style workflows are common for this literature but the indexed extract does not name the code).
- **System & composition:** **α-cristobalite** SiO₂ **slab** substrate and incident **HF**; total **atoms**, surface termination, and beam composition: in `pdf_path` (see §2 of *ACS Omega* 2021, 6, 16009–16015, DOI 10.1021/acsomega.1c01824).
- **Boundaries / periodicity:** **3D** **periodic** supercells are typical for such slab studies; use **boundary** conditions, fixed layers, and any vacuum gaps exactly as the article defines in `pdf_path` (**N/A** in the short extract here for full detail).
- **Ensemble, thermostat, barostat, pressure:** authors vary HF incident **energy** while following the MD stage described in the article; the indexed extract does not spell out **NVT** vs **NVE** (both appear in the Methods/SI in `pdf_path` where a thermostat or dissipation model is used). If the beam segment is effectively **NVE**-like with separate **temperature** control, record that as written. Isotropic **NPT** **pressure** *control*: **N/A** unless the main text says otherwise; **N/A** for hydrostatic **barostat** in gas-beam **bombardment** as typically posed.
- **Time step, duration, stages:** integration **time step** in **fs** and **simulation** **length**s per **HF** **energy** window are in `pdf_path` (not in the p1-2 index snippet; confirm **ps** total **trajectory** when reproducing). **Equilibration** and **production** **run** lengths for each case: `pdf_path`.
- **Shear, electric field, MSST, umbrella, enhanced sampling:** **N/A** in the published summary unless `pdf_path` names them; gas-phase etchant **bombardment** is the stated driver.

### Static QM (DFT training) — supplement

**DFT** training sets, functionals, basis/cutoff conventions, and the CMA-ES optimization of ReaxFF parameters are in §2.1 and SI of the article (`pdf_path`).


## Findings

The fitted ReaxFF reproduces the QM training-set structures and energies within the accuracy reported in the paper, which the authors take as justification for moving to large-scale etching simulations. In the MD stage, simulations show how etching yield and the inventory of reaction products vary with HF incident energy, supporting a picture in which impact energy modulates reaction branching on the oxide surface. The authors state that the developed ReaxFF offers mechanistic insight into atomistic SiO₂ etching by HF under the modeled conditions. The Results discussion ties observed product channels and surface stoichiometry evolution to the atomistic pathways accessible at each impact energy, providing a simulation counterpart to phenomenological etch-rate models used in process engineering.


## Relevance to group

Semiconductor processing–oriented ReaxFF development and application aligned with oxide etching literature.

## Citations and evidence anchors

- DOI: [10.1021/acsomega.1c01824](https://doi.org/10.1021/acsomega.1c01824)

## Related topics

- [[reaxff-family]]
