---
id: paper:2012aktulga-parallel-com-parallel-reactive
type: paper
title: "Parallel reactive molecular dynamics: Numerical methods and algorithmic techniques"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:method-development
  - task:software
  - scale:atomistic
paper_keywords:
  - keyword:method-development
  - keyword:puremd
  - keyword:charge-equilibration
  - keyword:lammps
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.parco.2011.08.005"
year: 2012
authors:
  - "H. M. Aktulga"
  - "J. C. Fogarty"
  - "S. A. Pandit"
  - "A. Y. Grama"
venue: "Parallel Computing 38, 245–259 (2012)"
pdf_sha256: "707932f3d2d4d39c8a9dbca931ee4318a7c3c9e8036d0c4900f9e143bc14a393"
pdf_path: "papers/ReaxFF_others/Aktulga_parallelReaxFF_2012.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012aktulga-parallel-com-parallel-reactive -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF** couples **reactive bond dynamics** with **charge equilibration (QEq)**: partial charges follow from minimizing electrostatic energy via a **large sparse linear solve** each **sub-femtosecond** timestep, while **bond lists** and **many-body** terms rebuild as coordination changes. This paper presents **PuReMD** (**Purdue Reactive MD**), a parallel implementation optimized for these costs: **dynamic data structures** for evolving topology, algorithmic tuning of bonded/nonbonded work, and **Krylov** solvers for QEq. Reported scaling studies reach **thousands of cores** on a commodity cluster (**Hera** at LLNL-OCF, up to **3375 cores** in the abstract), extending accessible **time/size** for reactive systems by **over an order of magnitude** relative to prior capability described in the article.

## Methods

### 1 — MD application (atomistic dynamics)

**PuReMD** (**Purdue Reactive Molecular Dynamics**) implements **ReaxFF** as a **classical MD** method with **dynamic** neighbor lists and **bond/topology** reconstruction each timestep to follow **reactive** environments (`normalized/extracts/2012aktulga-parallel-com-parallel-reactive_p1-2.txt`).

- **Engine / code:** **PuReMD** / **ReaxFF** reactive MD (abstract + Sec. 1).
- **System size & composition:** The abstract lists representative applications (**Si–Ge** nanobar strain relaxation, **water–silica** interaction, **lipid bilayer** oxidative stress); **N/A —** atom counts are not stated on the indexed excerpt pages.
- **Boundaries / periodicity:** **N/A —** not stated on the indexed excerpt pages (examples include surfaces/bilayers but details are later in the PDF).
- **Ensemble / thermostat / barostat / pressure:** **N/A —** **NVT**/**NPT**/**NVE** labels, thermostat/barostat algorithms, and **pressure** control are not stated on the indexed excerpt pages.
- **Temperature:** **N/A —** explicit thermostat **temperature** setpoints for the benchmark trajectories are not stated on pp. 1–2 (the excerpt is methodological/scaling-focused).
- **Timestep:** **ReaxFF** timesteps are described as typically **an order of magnitude smaller** than conventional MD, **~0.1 fs** vs **~1 fs** (Sec. 1, extract).
- **Duration / stages:** The abstract states **nanosecond**-scale reactive simulations become feasible for large systems with PuReMD’s per-timestep performance; **N/A —** equilibration/production split is not on pp. 1–2.
- **Electric field:** **N/A —** not stated on the indexed excerpt pages.
- **Replica / enhanced sampling:** **N/A —** not stated on the indexed excerpt pages.

### 2 — Force-field training

**N/A —** software/methods paper; it assumes an existing **ReaxFF** formulation and focuses on **algorithms + scalability**.

### 3 — Static QM / DFT-only

**N/A —** not a DFT study.

**Algorithms (dominant cost):** **QEq** is posed as a **large sparse linear solve** each timestep with a **shielded electrostatic kernel**; **Krylov** methods are highlighted for scaling the QEq solve to thousands of cores (Sec. 1, extract).

## Findings

**Outcomes and mechanisms:** The article frames **ReaxFF**’s distinctive costs as **per-timestep bond reconstruction** and **complex bonded kernels** approaching nonbonded costs, plus an accurate **QEq** solve each timestep—contrasting with fixed-bond MD where charges are fixed (Sec. 1, extract).

**Comparisons / performance claims:** PuReMD is reported to extend reactive **spatiotemporal** capability by **over an order of magnitude** relative to prior capability discussed in the paper, with scaling/performance demonstrated up to **3375 cores** on **Hera** at **LLNL-OCF** (abstract, extract).

**Sensitivity and design levers:** The text emphasizes **timestep length** (sub-fs **ReaxFF** vs fs-scale conventional MD) as a driver of how often **QEq** must be solved and how bond/topology updates must track chemistry (Sec. 1, extract).

**Limitations / outlook:** The abstract notes analysis of **potential bottlenecks** beyond the demonstrated core counts; detailed hardware/network sensitivity is **N/A —** not excerpted on pp. 1–2.

**Corpus / KB honesty:** This summary is tied to **`pdf_path`** and `normalized/extracts/2012aktulga-parallel-com-parallel-reactive_p1-2.txt` (early article pages only).

## Limitations

- Performance is hardware and network dependent; **ReaxFF** parameter sets and integrator choices still govern scientific validity independent of code speed.

## Relevance to group

Infrastructure paper for **scalable ReaxFF MD** used across the community; essential context for runtime expectations on large **LAMMPS/PuReMD** jobs.

## Citations and evidence anchors

- DOI: [10.1016/j.parco.2011.08.005](https://doi.org/10.1016/j.parco.2011.08.005)
- Text-aligned pointer: `normalized/extracts/2012aktulga-parallel-com-parallel-reactive_p1-2.txt`

## Related topics

- [[reaxff-family]]
- LAMMPS reactive workflows and high-performance computing
