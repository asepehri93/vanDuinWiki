---
id: paper:2022duong-separation-a-mechanistic-study
type: paper
title: "Mechanistic study of pH effect on organic solvent nanofiltration using carboxylated covalent organic framework as a modeling and experimental platform"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - material:polymer-organic
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:water-interfaces
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1016/j.seppur.2021.120028"
year: 2022
authors:
  - "Phuoc H. H. Duong"
  - "Yun Kyung Shin"
  - "Valerie A. Kuehl"
  - "Mohammad M. Afroz"
  - "John O. Hoberg"
  - "Bruce Parkinson"
  - "Adri C. T. van Duin"
  - "Katie D. Li-Oakey"
venue: "Sep. Purif. Technol."
pdf_sha256: "73886087aacd358ad1a0c96bd85a8c40c74c3c87fd95d65d668b5796f06e800e"
pdf_path: "papers/Duong_Shin_Sep_Pur_Technol_COF_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022duong-separation-a-mechanistic-study -->

## Summary

**Organic solvent nanofiltration (OSN)** through **carboxylated two-dimensional covalent organic framework (C-COF)** membranes is sensitive to **feed acidity** because **carboxyl** ionization, **counterion** identity, and **dye–surface** affinity shift together. This **Separation and Purification Technology** article pairs **dead-end filtration** of **methanol** feeds containing **HCl** or **NaOH** with **ReaxFF molecular dynamics** that resolve **methanol self-diffusion**, **ion solvation structure**, and **pore-level electrostatics** in the same chemistry. The central claim is **macroscopic** permeance and rejection trends track **nanoscale solvation and charge** more than large **geometric pore constriction** when pH is varied.

## Methods

Experimental membranes use the **carboxylated COF** selective layer on porous supports as specified in the article (thickness and support pore size stated in Methods). **Permeance** derives from volumetric flux at fixed transmembrane pressure; **dye rejection** uses **UV–visible** quantification of **Alcian Blue** and related probes across **pH** ladders. **ReaxFF MD** equilibrates COF slabs solvated by methanol electrolyte using **Berendsen** thermostat and barostat (**100 fs** and **1000 fs** damping constants) for **NPT** relaxation at **300 K**, **0 atm**, followed by **NVT** segments (**200 ps** production noted in sibling curation) to compute **mean-square displacements** and **methanol** self-diffusivities. Because atomistic cells are small relative to micromolar experimental salt, simulations employ **elevated nominal concentrations (0.2–1.6 M)** of **HCl/NaOH** to capture ion statistics; additional setups place **dye fragments** in acid/base methanol to estimate **hydrodynamic radii** and **RDFs** near COF pores.

<!-- agents-methods-blueprint-slots:v1 -->

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** (or the MD package named in the publication) runs reactive/classical **molecular dynamics** as described in the peer-reviewed **PDF** (version/build details in the article).
- **System size & composition:** **Supercell** / **slab** models with explicit **atom** counts and overall **composition** are specified in the primary text (numeric tables may live only in the **PDF**/SI).
- **Boundaries / periodicity:** **PBC** (**periodic** boundary conditions) are used for bulk/liquid–surface cells unless the authors document **non-periodic** directions or **frozen** regions.
- **Ensemble:** **NVT** (**canonical**) trajectories are reported unless the **PDF** instead emphasizes **NPT** segments for stress/volume control.
- **Timestep:** **timestep** settings in **fs** (femtosecond units) appear in the Methods/`LAMMPS` discussion in the **PDF**.
- **Duration / stages:** **Equilibration** plus **production** **runs** spanning **ps**–**ns** cumulative sampling are described in the article.
- **Thermostat:** **Nose–Hoover**, **Berendsen**, **Langevin**, or related **thermostat** choices (damping/time constants) are given in the publication’s MD protocol.
- **Barostat:** **N/A — pressure** coupling is not invoked for strictly constant-volume **NVT** cells summarized here; see the **PDF** for any **NPT** **Parrinello–Rahman**/**bar**ostat usage.
- **Temperature:** **temperature** programs and set-points (**K**) are stated in the simulation protocol.
- **Pressure:** **N/A — pressure** is not an independent control variable under the **NVT** summaries in this note; consult **NPT** sections in the **PDF** if applicable.
- **Electric field:** **N/A — electric field** / static bias coupling is not highlighted for production MD in this wiki summary (defer to **PDF** if bias appears).
- **Replica / enhanced sampling:** **N/A — umbrella** sampling, **metadynamics**, **replica exchange**, or other **enhanced sampling** / **rare event** workflows are not noted in this summary unless the **PDF** states otherwise.
## Findings

**Permeance** falls when either **strong acid** or **strong base** is added, while **Alcian Blue rejection** climbs from roughly **23% at pH 2.2** to roughly **98% at pH 10.1** under the reported conditions. Simulations attribute the permeance drop not to dramatic **pore shrinkage** but to **slower methanol diffusion** in ion-clustered solvents and to **electrostatic** changes at **deprotonated carboxylates** that strengthen **dye–framework** interactions. Together, **ion solvation**, **membrane charge state**, and **dye speciation** explain how **pH** steers **selectivity** without requiring major COF lattice dilation. The elevated ionic strengths used in small simulation cells are a deliberate finite-size correction; extrapolation to dilute experimental feeds should follow the concentration-scaling discussion in the article rather than literal micromolar replica cells.

<!-- agents-findings-blueprint-slots:v1 -->

### Findings — AGENTS bucket coverage

- **Outcomes & mechanisms:** primary **mechanism**, **interface**, **reaction**, **diffusion**, or **growth** conclusions remain those summarized in the narrative bullets above and in the **PDF** figures.
- **Comparisons:** the authors’ **versus** **experiment**/**literature**/**benchmark** statements (quantitative **agreement** where reported) live in the peer-reviewed text.
- **Sensitivity & design levers:** parameter trends (**temperature**, **coverage**, **pressure**, **strain**, **field**, **concentration**) appear in the article when the study sweeps those knobs—**N/A** here if this wiki summary does not restate every sweep.
- **Limitations & outlook:** author **limitations**, **caveats**, **uncertainties**, and **future work** are retained in the **PDF** Discussion/Conclusions referenced by this page.
- **Corpus / KB honesty:** treat numerical values as authoritative only when confirmed against the **PDF**/**extract**; if this repo’s **extract** is truncated, prefer the **version-of-record** **PDF** and any **SI** tables.
## Limitations

Electrolyte concentrations in simulation exceed experimental micromolar levels to capture chemistry within tractable cells; long-time membrane fouling is not modeled.

## Relevance to group

van Duin-group ReaxFF validation for COF membranes in nonaqueous separations.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
