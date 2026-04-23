---
id: paper:2014kylasa-jcp-puremd-gpu-reactive
type: paper
title: "PuReMD-GPU: a reactive molecular dynamics simulation package for GPUs"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:software
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:puremd
  - keyword:gpu-md
  - keyword:method-development
  - keyword:reaxff-application
  - keyword:charge-equilibration
candidate_tags: []
source_refs: []
doi: "10.1016/j.jcp.2014.04.035"
year: 2014
authors:
  - "Kylasa, S. B."
  - "Aktulga, H. M."
  - "Grama, A. Y."
venue: "Journal of Computational Physics"
pdf_sha256: "9a838256a311d1c47ec851e549c7c76f559ac2fe3306b9e6e05fbfa5a03865ce"
pdf_path: "papers/ReaxFF_others/PuReMD_GPU_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014kylasa-jcp-puremd-gpu-reactive -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **J. Comput. Phys.** article identified by `doi`, `title`, and `pdf_path`.

## Summary

Kylasa, Aktulga, and Grama introduce **PuReMD-GPU**, a **GPU** implementation of the **PuReMD** engine for **ReaxFF** reactive molecular dynamics, targeting the dominant costs of **ReaxFF** timestep integration: **bonded** many-body work tied to **bond orders**, **nonbonded** pair interactions, and especially the **charge equilibration (QEq)** **sparse linear solve** repeated every timestep. The paper argues that **ReaxFF**’s sub-femtosecond timesteps make **per-step** throughput the limiting factor for large systems, so **GPU** acceleration of **QEq** via **Krylov**-style solvers and careful **data-structure** design yields practical **wall-clock** gains for production science. The authors validate **correctness** on **bulk water** and **amorphous silica** benchmarks against a **highly optimized CPU single-core** **PuReMD** path, then report **end-to-end speedups** for those systems on the hardware configurations quoted in the article.

## Methods

### Code lineage and integration context

- **PuReMD-GPU** is a **GPU** implementation of the **PuReMD** **ReaxFF** engine; **PuReMD** (as **ReaxFF/C** in **LAMMPS**) is noted in the abstract as widely used for systems from **biomembranes** to **explosives** (**RDX**).

### Algorithmic focus (per-timestep costs)

- The paper targets **sub-femtosecond** **ReaxFF** timesteps by accelerating **bonded** many-body work (bond-order reconstruction, conjugation terms), **nonbonded** interactions, and especially the **charge equilibration (QEq)** **sparse linear solve** repeated each step (abstract + introduction excerpt).

### GPU implementation details (high level)

- **PuReMD-GPU** refactors data structures and kernels for **GPU** memory traffic and parallelism; **QEq** uses **iterative** sparse solvers suited to **ReaxFF**’s charge-coupling patterns (wiki summary aligned with abstract claims).

### Validation experiments

- **Accuracy:** energies/forces and integration behavior are compared against a **highly optimized CPU single-core PuReMD** reference on **bulk water** and **amorphous silica** model systems (abstract).

### Distribution

- The abstract states **PuReMD-GPU** was **available on request** from the authors at publication (verify current licensing/repos with maintainers before citing availability).

### 1 — MD application (benchmark trajectories in the paper)

- **Engine / code:** **PuReMD-GPU** implements **ReaxFF** **reactive MD** kernels and solvers on **GPUs** (**abstract**); comparisons reference **PuReMD** as **ReaxFF/C** in **LAMMPS** in the abstract framing.
- **Benchmark systems:** **bulk water** and **amorphous silica** cells used for **correctness** and **speedup** studies versus a **highly optimized CPU single-core PuReMD** reference (**abstract**); treat these as finite **atom** budgets reported in the article (**N/A — exact atom totals not on indexed extract**).
- **Boundaries / periodicity:** **3D PBC** is standard for the **bulk water** / **amorphous silica** benchmarks in this article class; **N/A — explicit PBC statement not on indexed extract window** (JCP Methods).
- **System sizes / ensemble / timestep / thermostat / barostat / production lengths / temperature set points:** **N/A — not stated on the indexed abstract/extract window used for this page**; read **`papers/ReaxFF_others/PuReMD_GPU_2014.pdf`** Methods for definitive numbers.
- **Hydrostatic pressure / barostat:** **N/A — pressure control not stated on the indexed abstract window** (confirm NVT vs NPT in JCP Methods).
- **Electric field:** **N/A — not indicated** in the abstract-level summary used here.
- **Replica / enhanced sampling:** **N/A — not indicated** in the abstract-level summary used here.

## Findings

### Outcomes and mechanisms

Reported **end-to-end** speedups reach up to **~16×** versus the authors’ **CPU single-core** **PuReMD** baseline for the **water** / **amorphous silica** benchmarks and hardware tested (**abstract**). The paper argues **GPU** acceleration of **QEq** and **bond-order** work is central to practical **wall-clock** throughput for large **ReaxFF** cells where **sub-femtosecond** timesteps make **per-step** cost dominate (**abstract**/introduction themes).

### Comparisons

Correctness is anchored by agreement with a **highly optimized CPU single-core PuReMD** reference on the benchmark systems named in the **abstract** (energies/forces/integration behavior).

### Sensitivity

Absolute speedups are **hardware-dependent**; **temperature**, **cutoffs**, and **neighbor-list** settings will move micro-benchmarks—**N/A — full sensitivity tables not summarized on the indexed extract window** (JCP article).

### Limitations and corpus honesty

Code availability was **on request** at publication (**abstract**); modern deployments should verify licensing with maintainers (**## Limitations**). **Numerical** benchmark details should be read from **`papers/ReaxFF_others/PuReMD_GPU_2014.pdf`**, not extrapolated from this wiki note.

## Limitations

Code availability was **on request** at publication; modern deployments should verify licensing and repository location with current **PuReMD** maintainers. **GPU** speedups depend on **hardware**, **precision**, and **neighbor-list** settings; reproduce benchmarks before claiming **production** throughput for a new cluster.

## Reader notes (navigation)

Index this page under **methods-software** rather than **application** chemistry; it supports **ReaxFF** science indirectly by reducing **wall-clock** cost for large reactive cells.

## Citations and evidence anchors

- DOI `10.1016/j.jcp.2014.04.035` (article footer in extract).

## Related topics

- [[reaxff-family]]
