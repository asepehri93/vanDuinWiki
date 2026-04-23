---
id: paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based
type: paper
title: "JAX-ReaxFF: A Gradient-Based Framework for Fast Optimization of Reactive Force Fields"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:methods-software
  - domain:ml-atomistic
  - method:reaxff
  - task:method-development
  - task:software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.2c00363"
year: 2022
authors:
  - "Mehmet Cagri Kaymak"
  - "Ali Rahnamoun"
  - "Kurt A. O’Hearn"
  - "Adri C. T. van Duin"
  - "Kenneth M. Merz Jr."
  - "Hasan Metin Aktulga"
venue: "J. Chem. Theory Comput. 18, 5181–5194 (2022)"
pdf_sha256: "b88485f0e074898eed5df2acca339046a27e660593fe7cfdae585048954813e9"
pdf_path: "papers/Kaymak_JAX_JCTC_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022mehmet-cagri-kaymak-j-chem-theor-jax-reaxff-gradient-based -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**JAX-ReaxFF** replaces slow, heavily stochastic ReaxFF parameter searches (genetic algorithms / Monte Carlo style workflows that can require millions of error evaluations) with **differentiable loss landscapes**: gradients of the training objective are computed via **JAX**, enabling **local optimizers** launched from **multiple initial guesses** in high-dimensional parameter space. The implementation targets **CPU/GPU/TPU** execution and reports dramatic wall-clock reductions for complex fits—positioned as enabling rapid iteration when both **training data** and **functional forms** must be refined jointly. The paper also frames the stack as a **sandbox** to explore ReaxFF functional customization guided by fast, gradient-based search.

Because parameter vectors can contain hundreds or thousands of terms, the authors stress that classical global search becomes a throughput bottleneck: each proposed parameter update may require enormous sampling, whereas automatic differentiation supplies directional information that can shrink the number of objective evaluations needed for comparable training-error reduction when the landscape is locally smooth enough.

## Methods

### 1 — MD application (atomistic dynamics)

- **Scope note:** MD protocol reporting is not the primary contribution here; the paper focuses on gradient-based ReaxFF parameter optimization, with downstream MD validation delegated to benchmark-specific setups in the article/SI.
- **Engine / code:** N/A for one canonical production trajectory in this page; parameter sets are exported to LAMMPS/PuReMD-style workflows for validation runs.
- **System size & composition:** N/A in this summary-level page because no single validation cell is the central protocol.
- **Boundaries / periodicity:** N/A (benchmark dependent; consult article/SI when reproducing a specific validation case).
- **Ensemble:** N/A (depends on the downstream validation benchmark, not one unified protocol in this methods paper).
- **Timestep:** N/A (benchmark dependent in validation runs).
- **Duration / stages:** N/A (equilibration/production lengths are benchmark dependent in article/SI validation setups).
- **Thermostat:** N/A (if used, it is reported within specific downstream validation protocols rather than a single study-wide trajectory).
- **Barostat:** N/A (no single NPT protocol is defined as the core method contribution).
- **Temperature:** N/A in the optimizer framework itself; temperatures belong to specific post-fit validation trajectories described per benchmark in the article/SI.
- **Pressure:** N/A in the core optimization method.
- **Electric field:** N/A unless a downstream validation benchmark explicitly applies one.
- **Replica / enhanced sampling:** N/A (not presented as part of the core optimization workflow).

### 2 — Force-field training (JAX–ReaxFF)

- **Parent / functional form:** Standard **ReaxFF** energy decompositions; **JAX** implements **vectorized** terms so **backprop** through the **ReaxFF** **loss** is feasible, including the usual **bond**, **angle**, **torsion**, **vdW**, **Coulomb**/**QEq**-class contributions detailed in the article.
- **QM reference:** **Training** **errors** are against **DFT**/**QM**-style **reference** **targets** in the same spirit as existing **ReaxFF** **fits** (data sets in *J. Chem. Theory Comput.*; **weighting** and **reaction** subsets in **SI**).
- **Training set / objectives:** The **loss** is assembled from the authors’ **QM** data partitions (molecules and solids as listed); the paper contrasts **stochastic** **genetic**/**Monte** **Carlo** **searches** that can require order **10⁶+** **evaluations** with **gradient**-based **updates** on comparable tasks.
- **Optimization:** **Multi-start** **local** **BFGS**-type or related **JAX**-driven **optimizers** from many **initial** **ReaxFF** **vectors**; **wall-clock** and **iteration** **counts** reported vs **genetic**/**MC** **baselines** in **tables/figures** of the **PDF**.
- **Software / hardware:** **JAX**-compiled kernels run on **CPU**/**GPU**/**TPU**; package produces **exportable** **parameter** **decks** for **LAMMPS**-compatible **workflows** as described in the **PDF**.

### 3 — Static QM / DFT and experiments

- **DFT (reference only):** **QM** **energies/structures** enter the **objective**; the paper is **not** a standalone **PES** or **kinetics** DFT application paper.
- **Experiments: N/A.**
## Findings

**Performance:** In representative **ReaxFF** **fitting** tasks, **JAX-ReaxFF** with **gradients** plus **accelerators** reduces **optimization** **time** from **order-of-days** to **order-of-minutes** in the **cases** **tabulated** in the article, compared with **stochastic** **search** that scales poorly when **error** **evaluations** dominate. **Comparisons** vs **genetic**/**MC** also stress that **gradients** can **improve** **convergence** when the **landscape** is **locally** **smooth**, while **multi-start** remains necessary when **objectives** are **rugged**—single **local** **runs** are **not** **globally** **guaranteed**.

**Method outlook:** The framework is positioned both as a **faster** **tuner** of **ReaxFF** and as a **sandbox** to test **proposed** **ReaxFF** **function** **edits** while **re-optimizing** **parameters** in **tight** **iterations** with **QM** **data**.
## Limitations

Quality still depends on **training set curation** and physics of the ReaxFF model class; global optimality is not guaranteed—multi-start mitigates but does not remove ruggedness of parameter spaces.

## Relevance to group

Core **infrastructure** paper for **PSU/MSU collaborators** on **accelerated ReaxFF development**, directly supporting the group’s large parameterization agenda.

## Citations and evidence anchors

https://doi.org/10.1021/acs.jctc.2c00363 — Abstract (~p. 1) states goals and performance claims; later sections document methodology and benchmarks.

## Related topics

- [[reaxff-family]]
- [[2021itai-leven-j-chem-theor-recent-advances]]
