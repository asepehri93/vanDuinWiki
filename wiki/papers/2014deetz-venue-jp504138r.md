---
id: paper:2014deetz-venue-jp504138r
type: paper
title: "Parallel optimization of a ReaxFF reactive force field for polycondensation of alkoxysilanes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:silica-silicate
  - keyword:lammps
  - keyword:method-development
source_refs: []
doi: "10.1021/jp504138r"
year: 2014
authors:
  - "Deetz, Joshua D."
  - "Faller, Roland"
venue: "Journal of Physical Chemistry B"
pdf_sha256: "7e79916cd4d60b9e83e710685c31088d211205082d1b7126f22a20291db8cbc4"
pdf_path: "papers/ReaxFF_others/Deetz_JPC_B_alkoxysilanes_parallel_opt_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014deetz-venue-jp504138r -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

A ReaxFF parametrization workflow for alkoxysilane sol–gel chemistry uses a parallel local search: processors hold small parameter lists, parameters update together each iteration to speed optimization and reduce trapping in local minima. The fitted model reproduces hydrolysis and condensation reaction energies; MD of silicic acid condensation yields an activation energy for silane condensation and nanosecond-scale cluster growth consistent with gradual depletion of hydrolyzed silicon and silica cluster formation. A tetramethoxysilane–methanol–water mixture shows both hydrolysis and condensation in simulation (abstract; introduction, extract).

## Methods

### 2 — Force-field training (parallel ReaxFF optimization)

- **Parent FF / elements:** **ReaxFF** for **alkoxysilane** **sol–gel** chemistry; optimization extends an existing reactive description (see article introduction for lineage).
- **QM reference / training targets:** fit **QM** **hydrolysis**, **alcohol condensation**, and **water condensation** reaction energies for **Scheme 1** chemistries; **DFT** functional, basis, and **k**-mesh conventions are defined in **J. Phys. Chem. B** Methods (`pdf_path`).
- **Training set / observables:** **QM** reaction energies for specified **alkoxysilane** transformations; **LAMMPS** evaluates **ReaxFF** energies on trial parameter sets during optimization.
- **Optimization:** **Parallel local search**—parameter subsets are distributed across processors, evaluated **in parallel**, and the **full** parameter vector is **updated each iteration**, reducing wall time versus **serial one-parameter-at-a-time** steepest-descent updates and mitigating **local-minimum** trapping (article optimization section).
- **External reference data:** **QM** reaction energies as above; **MD validation** trajectories compare against expected **condensation** phenomenology (abstract; extract).

### 1 — MD application (LAMMPS validation trajectories)

- **Engine / code:** **LAMMPS** **ReaxFF** for **silicic acid** condensation and **TMOS/methanol/water** mixtures (article as summarized here).
- **System build:** **Packmol**-packed **TMOS / methanol / water** with **≥2 Å** minimum pair separation before dynamics.
- **Ensemble / thermostat / timestep:** **NVT**, **Nosé–Hoover** thermostat, **Δt = 0.25 fs** at **2000 K** for the **TMOS** mixture validation case (article).
- **Duration / stages:** **Silicic acid** condensation monitored over **~300 ps–ns** segments at several temperatures (article summary); full equilibration/production splits are in the PDF.
- **Boundaries / atom counts:** **N/A in this wiki summary**—confirm supercell sizes and **PBC** in **`pdf_path`**.
- **Barostat / pressure:** **N/A —** **NVT** cook-off framing for the summarized **2000 K** mixture runs.
- **Electric field / enhanced sampling:** **N/A —** not used in the summarized validation protocol.

### 3 — Static QM

**N/A as standalone block**—**QM** enters as **training** data for **ReaxFF** (see **Force-field training**).

## Findings

### 1 — Outcomes and mechanisms

The optimized ReaxFF reproduces the targeted **hydrolysis and condensation** energetics. Condensation MD shows the expected qualitative sequence: **gradual loss of hydrolyzed silicon** and **growth of condensed silica clusters** on few-nanosecond timescales. The TMOS–methanol–water system exhibits **concurrent hydrolysis and condensation**, supporting use of the model for precursor-solution early-stage chemistry (abstract; extract pages 1–2).

### 2 — Comparisons

- **ReaxFF** reaction energetics vs **QM** training targets (article).

### 3 — Sensitivity

- **Temperature** sweeps for **silicic acid** condensation track **cluster growth** and **activation** behavior (article summary).

### 4 — Limitations / outlook

- Empirical **ReaxFF** scope bounded by training sets; **nanosecond** segments capture early aggregation rather than full **gel** maturation (**## Limitations**).

### 5 — Corpus / KB honesty

- Numbers and **activation energies** quoted in the abstract should be checked against **`pdf_path`** and tables in the article.

## Limitations

Empirical reactive FF scope is bounded by training sets; nanosecond trajectories capture early aggregation rather than full gel maturation.

## Citations and evidence anchors

- DOI `10.1021/jp504138r` (extract footer).
- Abstract block (extract pages 1–2).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
