---
id: paper:2019karalis-scientific-r-supercritical-water
type: paper
title: "Supercritical water anomalies in the vicinity of the Widom line"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:npt-simulation
  - keyword:nvt-simulation
  - keyword:polarizable-ff
  - keyword:validation-experiment
  - keyword:classical-ff
source_refs: []
doi: "10.1038/s41598-019-51843-0"
year: 2019
authors:
  - "Konstantinos Karalis"
  - "Christian Ludwig"
  - "Bojan Niceno"
venue: "Scientific Reports"
pdf_sha256: "d134688d51addfe89ae201c5f41d7b8fbff4214341bc4afe0f60efd2d1a98fc5"
pdf_path: "papers/Others/Karalis_Supercritical_Widom_SciRep_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019karalis-scientific-r-supercritical-water -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *Scientific Reports* article identified by `doi`, `title`, and `pdf_path`.

## Summary

Supercritical water exhibits nonclassical fluctuations and property anomalies near the **Widom line** (locus of response-function maxima extending from the critical point). Classical force fields mislocate the critical temperature and pressure, complicating direct comparison to experiment. This study performs **GROMACS 2016.4** molecular dynamics of **2048** **SPC/E**, **TIP4P/2005**, **BK3**, and **SWM4-NDP** water models along **four isobars** between **230 and 290 bar** with **5 K** temperature steps from **600 to 700 K**. The authors map **density**, **static dielectric constant**, **self-diffusion**, and **heat capacity** maxima, applying **temperature/pressure shifts** (for example mapping **TIP4P/2005** **640 K** to experimental **647.1 K**) to compare models whose critical points are offset from experiment.

The **Widom** region is where **response** functions **peak** and **local** **density** **fluctuations** are enhanced; capturing those features matters for **supercritical** **solvation** and **reaction** **kinetics** even when the fluid is nominally a single phase.

## Methods

**Integration.** Leap-frog, **1 fs** timestep; **Nosé–Hoover** thermostat (**1 ps** relaxation); **Parrinello–Rahman** isotropic barostat (**1 ps**); **PME** electrostatics with **1.4 nm** cutoff as stated.

**Sampling / thermodynamic paths.** **2048**-molecule **boxes**; **GROMACS 2016.4**; **5 K** **increments** on **T** (for example **600** **K** to **700** **K** along the **stated** **isobars**; **NPT** and **NVT** **stages** **per** **observable** in the **article**), **10 ns** **production** after **equilibration**.

**Analysis.** Locating **Widom**-associated extrema along isobars; extracting **activation energies** for self-diffusion on liquid-like versus gas-like sides (Table 1 in the paper).

**Boundaries:** **three-dimensional periodic** bulk **H\(_2\)O** cells (**PBC**); **N/A** — no fixed walls or open directions. **Electric field:** **N/A** — not applied. **Replica / enhanced sampling:** **N/A** — not used (standard **MD**).

**Reproducibility detail.** Match **GROMACS** **version**, **cutoff** scheme, **bond** **constraints** (if any), and **PME** settings to the article for dielectric properties; use **block** averaging as in the paper for **C\(_V\)** peaks.
## Findings

**Polarizable** and **non-polarizable** models all reproduce **Widom**-type anomalies and signatures of **nanoscale heterogeneity** in supercritical water under the explored conditions. **TIP4P/2005** provides the **best overall** agreement with experimental thermodynamic and transport data along the paths tested. **Activation energies** for **self-diffusion** differ between Widom sides as tabulated.

**Model-selection note.** The **shift** strategy (mapping simulated **T** to experimental **T** near the **critical** point) is a pragmatic way to compare **force fields** with different **critical** **temperatures** without re-parameterizing each model.

**Property bundle.** The paper jointly evaluates **density**, **dielectric** constant, **diffusion**, and **heat** **capacity** because **Widom** anomalies manifest differently in **thermodynamic** versus **transport** observables; a model can match **density** yet miss **C\(_V\)** peaks.

**Polarizability trade-offs.** **Polarizable** models (for example **SWM4-NDP**) increase **cost** but can improve **dielectric** response; the benchmark narrative is **holistic**, not **single-property**.

**Downstream coupling.** For **ReaxFF** workflows that need **supercritical** **water** as a **solvent**, treat this study as a **classical** **water** **benchmark** reference—not as a reactive **kinetics** model for **dissociation** at extreme **T**.

## Limitations

Classical models lack **reactive** chemistry; supercritical **electrolyte** speciation is out of scope.

## Relevance to group

Benchmark **H\(_2\)O** fluid properties for multiscale workflows that may couple to **ReaxFF** reactive solvation studies.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1038/s41598-019-51843-0](https://doi.org/10.1038/s41598-019-51843-0) (`papers/Others/Karalis_Supercritical_Widom_SciRep_2019.pdf`).
- Extract: `normalized/extracts/2019karalis-scientific-r-supercritical-water_p1-2.txt`.

## Related topics

- [[reaxff-family]]
