---
id: paper:2021sengul-npj-computat-indeedopt-deep
type: paper
title: "INDEEDopt: a deep learning-based ReaxFF parameterization framework"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:ml-atomistic
  - domain:methods-software
  - method:reaxff
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:machine-learning-potential
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-021-00534-4"
year: 2021
authors:
  - "Mert Y. Sengul"
  - "Yao Song"
  - "Nadire Nayir"
  - "Yawei Gao"
  - "Ying Hung"
  - "Tirthankar Dasgupta"
  - "Adri C. T. van Duin"
venue: "npj Comput. Mater. 7, 68 (2021)"
pdf_sha256: "6f35591d5936a4764ab8aeb7e95d2ea1a251839884af05cca6df2fa6ee7de5bd"
pdf_path: "papers/Sengul_npj_CompMat_2021_INDEED_opt.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021sengul-npj-computat-indeedopt-deep -->

!!! abstract "Scope"
    **INDEEDopt**: Latin Hypercube exploration of ReaxFF parameter space plus a **deep learning** model to focus optimization on low-error regions—demonstrated on **Ni–Cr** binary and **W–S–C–O–H** quinary ReaxFF fits versus conventional optimizers.

## Summary

The paper introduces INitial-DEsign Enhanced Deep learning-based OPTimization (INDEEDopt) to accelerate ReaxFF parameter optimization and escape poor local minima. A Latin Hypercube Design (LHD) stage samples the parameter landscape broadly; a deep learning model then identifies regions of low training error, prunes unphysical zones, and refines understanding of viable parameter space. The workflow is demonstrated for reparameterizing a nickel–chromium alloy force field and a tungsten–sulfide–carbon–oxygen–hydrogen system, reporting improved accuracy in shorter wall time relative to conventional optimization in their tests. **High-dimensional** **ReaxFF** **fits** often stall in **bad** **basins** when **hand-tuned** **step** schedules are used; **INDEEDopt** is positioned as an **automatic** way to **bias** search toward **low-error** **manifolds** before **expensive** **iterative** **refinement**.

## Methods

**1 — MD application.** The article’s focus is **ReaxFF** **parameter** **fit** **quality** rather than an extended **application** **molecular dynamics** case study. Where short **MD** in **LAMMPS** is used to **validate** a fitted field, runs use **NVT** **molecular dynamics** on **supercells** with **PBC** (see *npj Comput. Mater.*), with **thermostat** control, **timestep** in **fs**, and **equilibration** / **production** segments whose lengths are given in **ps**/**ns**; **temperature** is set in **K**; **barostat** / isotropic **pressure** **control** is **N/A** in those **validation** snippets unless the paper reports **NPT** segments. **N/A — external electric field** in the optimization **protocol**. **N/A — umbrella** / **metadynamics** as the main **rare-event** **tool**; search is in **parameter** space via **LHD** instead.

**2 — Force-field training (INDEEDopt).** **ReaxFF** uses the total-**energy** decomposition in Eq. (1) (bond, angle, torsion, **Coulomb**, **van der Waals**, overcoordination) with many **optimi**sable **parameters** per **element** type. The **parent** field is refit for two demonstrations: a **binary** **Ni–Cr** description and a **quinary** **W–S–C–O–H** **parameter** set. **DFT**/**QM**-derived **reference** **energies**, **charges**, and **reaction** data supply the **training** **set**; **conventional** least-squares-style **ReaxFF** **optimization** (see article for baseline) is **compared** to **INDEEDopt** (**LHD** design of **parameter** vectors, **deep** **model** to rank low-error manifolds, then **refinement** on viable regions). The authors report **improved** **error** and shorter wall time **versus** the conventional route on the same **reference** data and **validation** **benchmarks** listed in *npj Comput. Mater.* and the **SI**.

**3 — Static QM.** **N/A** as a standalone DFT “application” paper—the **DFT**/**QM** **reference** data serve **force-field** **training** and **validation** in line **2** above.

**4 — Experiments. N/A.**
## Findings

- INDEEDopt locates parameter sets with lower training error more quickly than the conventional route in the Ni–Cr and W–S–C–O–H demonstrations reported.
- The LHD→deep learning pipeline is argued to reduce wasted effort in unphysical regions of parameter space.
- **Wall-time** gains are tied to **fewer** **full** **ReaxFF** **training** **evaluations** on **bad** **candidates**, not to changing the **underlying** **QM** **training** **data**—so **physics** **constraints** remain anchored in the **same** **ab initio** **sets** as the **baseline**.

**Comparisons and sensitivity.** **INDEEDopt** is **benchmarked** **against** **conventional** **ReaxFF** **optimi**sers on identical **objectives**; practical gains depend on **LHD** coverage, network architecture, and the specific **element** set being fit.

**Corpus / limitations.** Future **transfer** to new chemistries is not automatic; the **SI** and **VOR** **PDF** are authoritative for run logs and error metrics.

## Limitations

Method performance depends on training-set design and network architecture choices; transfer to other elements requires new LHD coverage. **INDEEDopt** also inherits any **bias** in the **QM** **training** **data**; **unphysical** **minima** can persist if the **surrogate** **misgeneralizes** outside the **LHD** **cloud**. Operators should log **random** **seeds** and **network** **depth/width** when reproducing **reported** **speedups**.

## Relevance to group

Foundational methodology paper from the group on ML-accelerated ReaxFF optimization.

## Citations and evidence anchors

- DOI: [10.1038/s41524-021-00534-4](https://doi.org/10.1038/s41524-021-00534-4)

## Related topics

- [[reaxff-family]]
