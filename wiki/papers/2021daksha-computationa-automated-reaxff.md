---
id: paper:2021daksha-computationa-automated-reaxff
type: paper
title: "Automated ReaxFF parametrization using machine learning"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:ml-atomistic
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:machine-learning-potential
  - keyword:qm-training-data
  - keyword:monte-carlo-sampling
source_refs: []
doi: "10.1016/j.commatsci.2020.110107"
year: 2021
authors:
  - "Chaitanya M. Daksha"
  - "Jejoon Yeon"
  - "Sanjib C. Chowdhury"
  - "John W. Gillespie Jr."
venue: "Comput. Mater. Sci."
pdf_sha256: "e55631254c8ffdb24a93fff8ce60cbf50978df80a05e56cf3703ecbdb6445214"
pdf_path: "papers/ReaxFF_others/Daksha_Yeon_CompMatSci_2021_ReaxFF_ML_parameterization.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021daksha-computationa-automated-reaxff -->

## Summary

Daksha *et al.* address the high cost of ReaxFF parameter searches by pairing a **genetic algorithm (GA)** with an **artificial neural network (ANN)** that **surrogates** ReaxFF energy evaluations during much of the optimization, reverting to full ReaxFF calls where needed to limit surrogate drift. The paper benchmarks the workflow on a **zinc oxide** training case, comparing GA+ANN against GA alone and against manual parameterization narratives, and reports large **wall-time** savings in their tests while targeting comparable final error metrics.

## Methods

### MD application (production RMD)

**N/A —** the paper’s main deliverable is **ReaxFF parameter search** (GA + ANN), not a flagship **NVE**/**NVT**/**NPT** **molecular dynamics** application with fully tabulated **supercell** **stoichiometry**, **PBC** vectors, and **ps**/**ns** **production** runs. If the article/SI includes an illustrative **ZnO** **slab** RMD **validation** segment, **N/A —** treat **300 K**-class **temperature** setpoints, **thermostat** type, and **0.1–0.25 fs**-scale **timestep** as **N/A** here until copied from `pdf_path` (this note does not invent them). **Boundary / periodicity:** **N/A**—confirm **PBC** vs fixed layers in any MD snippet in the SI. **Barostat / pressure (MD):** **N/A** for a dedicated **NPT** application section unless the SI reports one. **Electric field, shock, enhanced sampling:** **N/A.**

### Force-field training (ReaxFF, GA+ANN)

- **Parent / scope:** ReaxFF reparameterization on a **ZnO** benchmark; GA uses **double-Pareto crossover** and **multi-standard-deviation Gaussian mutation** as reported in *Comput. Mater. Sci.*.
- **QM reference / training data:** **DFT** (or cluster/QM) **energies** and **geometries** for Zn–O **bonding** in the **training** **structures**—**exact** **functional**, **basis** set, **k**-**mesh**, and `VASP`/`Gaussian`-style program choices must be taken from the article/SI, not this wiki.
- **Surrogate:** An **ANN** approximates ReaxFF **energies** during many GA **fitness** calls; the workflow interleaves **full** ReaxFF evaluations to control **surrogate error** and search stability (per the paper’s strategy).
- **Optimization and metrics:** Compare **GA+ANN** vs **GA** without surrogate and vs **manual** ReaxFF training on aggregate error and optimization **time**; definitions of the objective and baselines are in `pdf_path`.

### Static QM / DFT in this work

**N/A —** standalone **property** DFT is not the paper’s headline; QM enters as **reference data** for the ReaxFF fit (see **Force-field training**). Copy DFT program, functional, and basis from the paper when reproducing the training set.

## Findings

- **Outcomes / optimization:** The **ANN**-accelerated GA reaches comparable aggregate **error** on the **ZnO** **training** set **versus** **GA** without the surrogate, with a large reduction in **wall** time **versus** **manual** ReaxFF fitting narratives in the paper’s **benchmarks** (hardware- and **implementation**-sensitive; **compared** figures in `pdf_path`).
- **Mechanism / search behavior:** Search can **stall** when the surrogate is poor in high-gradient regions of **parameter** space, which the paper mitigates with periodic **full** ReaxFF **re-evaluation** so fitness calls track the true **force field**.
- **Sensitivity & transfer:** **Performance** depends on ANN **architecture**, training coverage, and the GA **mutation**/**crossover** settings; **transfer** to new **chemistries** needs fresh **DFT** **reference** data and a retrained **ANN**, so **out-of-domain** use remains an **uncertainty** **limitation** the authors flag explicitly.
- **Corpus honesty:** All numerical **error** tables and time-to-convergence **metrics** are **in** the **PDF**/**SI**—**not** duplicated here to avoid **galley** vs **VOR** drift; confirm locators in `pdf_path` before **benchmark** reuse.

## Limitations

Surrogate quality and ANN architecture choices can bias the GA search if not monitored. Reported month-to-day speedup claims depend on machine count, parallel efficiency, and GA settings; treat them as order-of-magnitude guidance from the paper, not universal benchmarks.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1016/j.commatsci.2020.110107](https://doi.org/10.1016/j.commatsci.2020.110107) (`papers/ReaxFF_others/Daksha_Yeon_CompMatSci_2021_ReaxFF_ML_parameterization.pdf`).

## Related topics

- [[reaxff-family]]
