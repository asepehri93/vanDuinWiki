---
id: paper:2013zheng-journal-of-m-algorithms-gpu-enabled
type: paper
title: "Algorithms of GPU-enabled reactive force field (ReaxFF) molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:method-development
  - task:software
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:gpu-md
  - keyword:lammps
  - keyword:method-development
  - keyword:thermal-decomposition
source_refs: []
doi: "10.1016/j.jmgm.2013.02.001"
year: 2013
authors:
  - "Mo Zheng"
  - "Xiaoxia Li"
  - "Li Guo"
venue: "J. Mol. Graphics Modell."
pdf_sha256: "a2b242b9101cb182a8e6c3fa732698b1113ae3e41e063e975d936ad51b4e4056"
pdf_path: "papers/ReaxFF_others/Zheng_ReaxFF_CPU_JMolGraphModel_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013zheng-journal-of-m-algorithms-gpu-enabled -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Benchmark numbers (speedups, system sizes) must be taken from the article.

## Summary

The paper introduces **GMD-Reax**, described as an early **GPU-accelerated ReaxFF MD** implementation. It positions **ReaxFF MD** as far more costly than **classical MD** (bond order updates, **charge equilibration**, smaller time steps) and reports **benchmarks** on an **NVIDIA C2050** for **coal pyrolysis**-style systems from **~1.4k** to **~27k** atoms. Claimed **speedups** in the abstract reach roughly **12×** vs **LAMMPS** **Fortran** ReaxFF on **8 CPU cores** and **6×** vs a **PuReMD**-related **C** path “in terms of simulation time per time-step” over **100** steps (exact comparison details are in the text). The motivation is **throughput**: enabling **desktop** **GPU** runs for **nanosecond-scale** reactive trajectories that were previously **cluster-limited** on **CPU-only** paths.

## Methods

### Software scope (GMD-Reax)

- **GMD-Reax** is presented as an early **GPU-enabled ReaxFF MD** program targeting the dominant CPU costs of **bond-order updates**, **per-timestep charge equilibration (QEq)**, and the **smaller integration timestep** required versus non-reactive classical MD (abstract and introduction excerpt).

### Baselines and hardware

- **CPU comparators** include **LAMMPS** **Fortran** ReaxFF (**eight CPU cores**) and **LAMMPS** **C** code based on **PuReMD**, matching the abstract’s naming.
- **Hardware:** benchmarks are reported on a PC with an **NVIDIA C2050** **Fermi**-class GPU (introduction).

### Benchmark systems and metric

- **Systems:** **coal pyrolysis**-like **C/H/O** trajectories with **1378–27,283 atoms** (abstract).
- **Metric:** **simulation time per time step** averaged over **100 steps** to compare implementations on an equal footing (abstract).

### Chemistry validation scope

- The manuscript focuses on **algorithmic performance** and **desktop throughput** for reactive MD; **QM validation** of the underlying **ReaxFF** parameterization is referenced to prior **ReaxFF** literature rather than re-derived here—see article discussion for scope.

**1 — MD application (atomistic dynamics).** **Engine / code:** **GMD-Reax** on **GPU** compared with **LAMMPS** **ReaxFF** **CPU** paths (abstract / introduction in `papers/ReaxFF_others/Zheng_ReaxFF_CPU_JMolGraphModel_2013.pdf`). **System:** **C/H/O** benchmark cells of **1378–27,283 atoms** (coal-pyrolysis-like chemistry, abstract). **Boundaries:** **N/A — explicit PBC and box details not summarized on this page** (confirm in article if reproducing). **Ensemble / thermostat / barostat:** **N/A —** reported metric is **wall time per timestep**, not a single production **NVT/NPT** protocol. **Timestep:** **N/A — not stated** in the p1–2 extract; cite the paper for benchmark **Δt** rather than generic literature defaults. **Duration:** averages over **100 timesteps** for timing (abstract). **Temperature / pressure / electric field / replica sampling:** **N/A —** not the controlled variables in the headline benchmarks summarized here.

## Findings

- The authors report **speedups up to ~12×** versus **LAMMPS Fortran ReaxFF on eight CPU cores** and **~6×** versus the **PuReMD-style C** implementation for the **per-timestep** cost in their benchmarks.
- The stated intent is to make **large reactive systems** tractable on **single desktop GPUs**, reducing reliance on **cluster-scale** CPU hours for **nanosecond-scale** ReaxFF trajectories.
- **Coal pyrolysis**-style benchmarks stress **heterogeneous** **C/H/O** chemistry with frequent **bond-order** updates—representative of the **worst-case** CPU costs **GMD-Reax** targets.
- **Compared to baselines:** headline **~12×** vs **LAMMPS Fortran** on **8 cores** and **~6×** vs **PuReMD-style C** (**Summary** / **Findings**).
- **Sensitivity:** reported **speedup** depends on **system size** (**1378–27,283 atoms**) and **hardware** (**C2050** era).
- **Limitations / outlook:** **GPU** **kernels** and **CPU** **ReaxFF** codes evolved since **2013**; treat numbers as **historical benchmarks** (**## Limitations**).
- **Corpus note:** this page is **not** a **parameterization** source—**QM validation** of any **FF** used in downstream work must trace to **primary** **ReaxFF** **publications**.

## Limitations

- **Hardware-specific** results (**NVIDIA C2050** era); newer GPUs and kernels change absolute throughput; the paper’s focus is **implementation speed**, not re-parameterizing **ReaxFF** chemistry.
- When porting **QEq**-heavy decks between **CPU** and **GPU** codes, operators should still regression-check **energy drift** and **charge neutrality**—the manuscript motivates throughput but does not replace code-specific validation.

## Relevance to group

**Ecosystem** paper for **ReaxFF** **throughput**; relevant when comparing **CPU/GPU** paths for **large** reactive simulations.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.jmgm.2013.02.001` (`papers/ReaxFF_others/Zheng_ReaxFF_CPU_JMolGraphModel_2013.pdf`).

## Related topics

- [[reaxff-family]]
