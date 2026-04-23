---
id: paper:2018vashisth-j-phys-chem-accelerated-reaxff
type: paper
title: Accelerated ReaxFF Simulations for Describing the Reactive Cross-Linking of
  Polymers
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:organics-polymers-pyrolysis
- domain:reaxff-lineage
- material:polymer-organic
- method:reaxff
- scale:atomistic
- task:method-development
paper_keywords:
- keyword:polymer
- keyword:reactive-md
- keyword:reaxff-application
- keyword:lammps
- keyword:qm-training-data
- keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpca.8b03826
year: 2018
authors:
- Aniruddh Vashisth
- Chowdhury Ashraf
- Weiwei Zhang
- Charles E. Bakis
- Adri C. T. van Duin
venue: J. Phys. Chem. A
pdf_sha256: 97d5875229a299b446770f6ea0c0fa1c1729d1296b82016f7736d14140a43259
pdf_path: papers/Vashisth_JPC_bondboost_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018vashisth-j-phys-chem-accelerated-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the J. Phys. Chem. A article identified by `doi`, `title`, and `pdf_path`.

## Summary

An **accelerated ReaxFF** workflow (distance **restraints** / **bond-boost**-inspired energy injection to surmount epoxy–amine **barriers** at **low temperature**) cross-links **bis F / DETDA** epoxy compositions. The **CHNO-2017_weak**-derived parameter set is **reoptimized** on **epoxide/amine** coupling data; **QM transition states** benchmark barrier heights. Multi-step **NVT** polymerization builds a **large atomistic network (~1872 atoms)**; **annealing**, **NPT** density runs, and **LAMMPS** tensile tests yield **density**, **\(T_g\)**, and **modulus** compared to **dogbone** experiments.

## Methods

- **FF reoptimization:** Start from **CHNO-2017_weak**; refine **C–O, C–N, N–H** bonds/angles and **N** hydrogen-bond terms against epoxide–amine reactions; full tables in **SI** (`[[2018vashisth-venue-microsoft-word]]`).
- **Acceleration:** **Restraint energy** \(E_\mathrm{rest}\) on selected atom pairs (functional form eq. 2 in paper) with tuned **\(F_1,F_2,R_{12}\)** to supply **≈barrier** energy; systematic **NVT** scans calibrate barriers vs **QM** for **noncatalyzed**, **water-catalyzed**, and **self-promoted** pathways; **Python** post-processing removes spurious imaginary modes in TS candidates.
- **Polymer build:** Stoichiometric **bis F : DETDA** packs at **~0.4–0.6 g/cm³**; iterative **doubling** of system size with **500 K** accelerated **NVT** cross-linking until a **continuous** network (e.g. **32 bis F + 16 DETDA** molecules in the largest system reported).
- **Property evaluation:** **Anneal** 300→600 K in **100 K** steps (**12.5 ps** per step) alternating **NVT/NPT**; **density** from final **NPT** at **300 K**; **\(T_g\)** from **density vs T** linear fits (**300–500 K**, **20 K** steps, **50k** steps × **0.25 fs** **NVT** + **200k** steps **NPT** per point); **tensile modulus** via **LAMMPS** `stress/atom` at **300 K**, high strain rates (**\(10^8\)–\(2×10^8\) s\(^{-1}\)**), **cubic** deformation with **Poisson** relaxation on lateral faces, averaged over **three** directions.
- **Experiment:** **Cure** protocol (**121 °C / 1 h + 177 °C / 3.5 h**), **MDSC** \(T_g\), **ASTM D792** density, **clip-gauge** modulus—procedures cross-referenced to prior work.

### MD application (LAMMPS, bis F / DETDA packs)

- **Engine / code:** **LAMMPS** with **ReaxFF** as in the article’s **Computational Details** (issue PDF on `pdf_path`).
- **System size & composition:** Reactive packs are built from stoichiometric **bis F : DETDA** stoichiometry, iteratively **doubled** to the **continuous-network** sizes reported (e.g. **32 bis F + 16 DETDA** in the largest illustrative system); initial densities **~0.4–0.6 g cm⁻³** before cross-linking.
- **Boundaries / periodicity:** Bulk **epoxy** cells use **three-dimensional periodic boundary conditions** in **LAMMPS** (standard **PBC** supercell for condensed-phase **ReaxFF**).
- **Ensemble:** **NVT** for **accelerated** cross-linking windows; alternating **NVT** / **NPT** for **annealing**, **densification**, and **\(T_g\)** sweeps; **NPT** for final **density** points and **modulus** deformation cells as quoted above.
- **Timestep:** **0.25 fs** integration for **\(T_g\)** / **NPT** segments tied to the **density-versus-temperature** protocol.
- **Duration / stages:** **Multi-stage** workflow—accelerated **NVT** polymerization, **300 → 600 K** **annealing** (**12.5 ps** per **100 K** step), long **NPT** / **NVT** blocks for **\(T_g\)** sampling (**50k**/**200k**-step segments per temperature), and **tensile** production at **300 K**.
- **Thermostat / barostat:** **N/A —** the **J. Phys. Chem. A** text does not spell out a named **thermostat** algorithm beyond specifying **NVT**/**NPT** segments; **pressure** for **NPT** portions follows the **barostat** usage implied by the **density** and **modulus** stages in the article.
- **Temperature:** **Cross-linking** at **500 K** (and cure-temperature-matched windows noted in the article); **annealing** ladder **300–600 K**; **\(T_g\)** scans **300–500 K** (**20 K** steps); **tensile** tests at **300 K**.
- **Pressure:** **NPT** segments for **density** / **\(T_g\)** / **modulus** as above; **N/A —** not applicable during pure **NVT** cross-linking windows.
- **Electric field:** **N/A — not used**.
- **Replica / enhanced sampling:** **N/A — not used** beyond the **restraint-energy** acceleration recipe (not umbrella / metadynamics / replica exchange).
## Findings

- **QM agreement:** ReaxFF barrier heights and TS geometries match **QM** literature data for the three **epoxide–amine** motif classes considered.
- **Cross-linking:** Accelerated runs achieve **~82%** of theoretical cross-linking extent in the large-system example discussed in the article.
- **Properties:** Simulated **density**, **\(T_g\)**, and **Young’s modulus** track **experimental** values within the uncertainties discussed; strain-rate scaling addressed via multi-rate simulation/experiment comparison.

## Limitations

High **strain-rate** MD vs quasi-static experiments; accelerated MD can **reject** events under high local strain; restraint parameters require calibration per chemistry.

## Reader notes (navigation)

- Parameter tables / tracking script: [[2018vashisth-venue-microsoft-word]]
- Related epoxy study (proof PDF in corpus): [[2018vashisth-venue-paper]]

## Related topics

- [[reaxff-family]]
