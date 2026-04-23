---
id: paper:2015ogo-venue-paper
type: paper
title: "Efficient global optimization of reactive force-field parameters (ogolem / serial ReaxFF preprint)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:software
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:method-development
  - keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: ""
year: 2015
authors:
  - "Mark Dittner"
  - "Julian Mueller"
  - "Hasan Metin Aktulga"
  - "Bernd Hartke"
venue: "Journal of Computational Chemistry (submitted/in-press preprint PDF in corpus)"
pdf_sha256: "822a216b2dc688e7eff51a8b46edaca471a52a1bcf2ee45dd80c3d4beb93ae74"
pdf_path: "papers/ReaxFF_others/ogo_serialreax_pre.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2015ogo-venue-paper -->

!!! abstract "Corpus note"
The local PDF is a **preprint / in-press** manuscript (**J. Comput. Chem.**, 2015 submission metadata on the cover page). The published article is curated as **`[[2015dittner-venue-efficient-global]]`** (DOI `10.1002/jcc.23966`); prefer that entry for authoritative pagination and final title.

## Summary

This ingested PDF corresponds to the same research line as the published Journal of Computational Chemistry paper on efficient global optimization of reactive force-field parameters: it presents **ogolem**, an evolutionary or genetic-algorithm framework with thread-level and MPI-level parallelism, extended to complex ReaxFF training sets that couple many structures and observables. The manuscript argues that global meta-heuristic search can reach high-quality ReaxFF parameter sets with less manual intervention and favorable parallel scaling compared with serial multistart local optimization workflows common in older practice. Conceptually, the code treats each fitness evaluation as an embarrassingly parallel task across candidate parameter vectors, which maps well to clusters running LAMMPS or PuReMD energy calls. The preprint therefore documents an engineering effort to industrialize reactive force-field fitting beyond ad hoc scripts.

## Methods

### Force-field training (global optimization workflow)

**Parent potential:** **ReaxFF** parameter vectors for reactive systems. **QM / reference data:** **DFT** (and related **QM**) **energies**/**forces** on **training structures** supply the objective, alongside **experimental benchmarks** where included in the manuscript’s **training set**. **Optimization:** **ogolem** implements **genetic-algorithm** / evolutionary **global parameter optimization** (selection, crossover, mutation) with **least-squares**-style fitness reductions versus the **reference data**. **Training set:** multi-structure **ReaxFF** **fitting** sets coupling many **geometries** and observables (Sec. 2.2 narrative in the preprint).

### MD application (benchmark energy evaluations)

The manuscript positions **ogolem** as driving repeated **energy** and **force** evaluations on **ReaxFF** systems—typically via **molecular dynamics** or energy **minimization** on **periodic supercells** whose **atom** counts and **stoichiometry** follow each benchmark’s **training** geometry (full tables only in the manuscript, not on the local one-page **abstract**). **Boundary conditions:** benchmarks use **three-dimensional periodic boundary conditions (PBC)** where the underlying reference structures are bulk-like. **Ensemble / thermostat / timestep (fs):** per-case **NVT** or **NVE** segments with documented **thermostat** settings and **timestep** appear in the full text—**N/A to list** from the ingested **abstract** alone. **Equilibration and production durations (ps/ns):** likewise **N/A** from the abstract; see **[[2015dittner-venue-efficient-global]]**. **Target temperature (K):** **N/A** on the abstract page; reproduction requires the **version-of-record**. **Barostat / NPT:** **N/A —** optimization is not framed as hydrostatic **pressure** control. **Hydrostatic pressure:** **N/A —** fitness benchmarks are not described as **GPa**-resolved **NPT** scans on the abstract page. **Electric field / metadynamics / replica exchange:** **N/A** for the global search workflow itself.

## Findings

The **abstract** claims that the implementation delivers **ReaxFF** parameter sets of comparable **quality** with **less human effort** and **shorter wall time** than prior practice, with **strong parallel scaling** as the number of **fitness evaluations** grows. **Workflow:** evolutionary / **genetic-algorithm** search explores parameter space more globally than **serial multistart** local optimization. **Sensitivity:** performance depends on **training-set** construction and stochastic **seeds**, as for any meta-heuristic optimizer. **Comparisons:** claims are relative to earlier **ReaxFF optimization** workflows cited in the text, not new **experiment**. **Limitations:** this **`pdf_path`** is a **submitted / in-press** preprint; for **pagination**, final wording, and benchmark tables, use the **version-of-record** entry **[[2015dittner-venue-efficient-global]]** (DOI `10.1002/jcc.23966`).

## Limitations

Stochastic search remains sensitive to training-set design and random seeds; global optimization does not remove chemistry judgment in selecting objectives and constraints.

## Relevance to group

Software pathway for ReaxFF parameterization alongside PuReMD and LAMMPS ecosystems; canonical reference: [[2015dittner-venue-efficient-global]].

## Citations and evidence anchors

- Published article: [[2015dittner-venue-efficient-global]] (DOI `10.1002/jcc.23966`).

## Related topics

- [[reaxff-family]]
- [[reaxff-parameterization-workflow]]
