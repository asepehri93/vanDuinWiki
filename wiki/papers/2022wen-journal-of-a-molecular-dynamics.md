---
id: paper:2022wen-journal-of-a-molecular-dynamics
type: paper
title: "Molecular dynamics simulation of the shock response of materials: A tutorial"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:classical-md
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:shock-compression
  - keyword:msst
  - keyword:classical-ff
  - keyword:nve-simulation
candidate_tags: []
source_refs: []
doi: "10.1063/5.0076266"
year: 2022
authors:
  - "Peng Wen"
  - "Gang Tao"
  - "Douglas E. Spearot"
  - "Simon R. Phillpot"
venue: "Journal of Applied Physics 131, 051101 (2022)"
pdf_sha256: "6033cf137ad708441ce8c2d47a7c9f6b035dcf77835972994beba37ab1028940"
pdf_path: "papers/Others/Phillpot_et_al_shock_MD_SW_tutorial.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022wen-journal-of-a-molecular-dynamics -->

## Summary

This **Journal of Applied Physics** tutorial surveys how **molecular dynamics** is used to study **shock loading** of **crystalline and amorphous** materials. It distinguishes **non-equilibrium MD** approaches that **generate and track a propagating shock front** from **equilibrium MD** approaches that target the **post-shock state** **without** resolving full **wave propagation**, which matters for practitioners choosing between expensive wave-resolved simulations and cheaper Hugoniot-state estimates. It also points to **analysis** that extracts **thermodynamic information** and **defect** content from shock simulations, including how to relate one-dimensional wave profiles to continuum jump conditions when fluctuations are large.

## Methods

### Scope and genre (D — methods tutorial, not a single simulation study)

This **Journal of Applied Physics** piece is a **pedagogical survey** of **shock** **molecular dynamics**: it compares workflow families and analysis practices rather than reporting one **interatomic potential** or **material** benchmark.

### Nonequilibrium shock MD (NEMD) “wave-resolved” protocols (B)

- **Driver:** Impart a **planar compressive disturbance** (e.g. **piston**-like or **velocity rescaling** boundary conditions in common MD codes) so a **shock** propagates along a **single axis** in a **slab** or **filament** geometry.
- **Diagnostics:** Track **stress**, **energy density**, **mass density**, and **structure** (e.g. **local temperature**, **coordination**) **across the shock front** as it evolves.
- **Stability:** Discusses **timestep** constraints when **steep** gradients are present (tutorial guidance; **numerical values** are **material- and potential-dependent**—see full PDF).

### Hugoniot-state / constrained sampling routes (B)

- **Idea:** Access **post-shock thermodynamic states** by imposing constraints consistent with **Rankine–Hugoniot** **jump relations**, sometimes **without** fully resolving **steady shock structure**—useful when only the **end state** is needed.

### Post-processing and continuum linkage

- Extract **Hugoniot-related** quantities, **T/P profiles**, and **defect** or **melting** signatures; cautions include **finite-size** effects and **thermostat** artifacts in **shock-tube**-like setups.

### Potentials and numerical settings

**Interatomic model**, **timestep**, and **system size** are **not universal**—the tutorial directs readers to later sections of the **full PDF** (the short corpus extract covers **early pages only**).

## Findings

### Complementary workflows

**Front-resolved NEMD** and **Hugoniot-state / constrained** sampling are **complementary**: one emphasizes **propagating-wave** **mechanisms**, the other can target **thermodynamic states** behind shocks with different computational cost.

### Linking atomistics to continuum shock theory

When **diagnostics** are chosen carefully, MD results can be related to **Rankine–Hugoniot** analysis, but **thermostat** choices and **boundary** conditions must be validated for the **expected** **shock** structure of the **material** at hand.

### Reactive potentials

The overview notes extra bookkeeping and stability concerns for **reactive** models (e.g. **bond-order** schemes) under **shock** loading; readers should follow **software-specific** guidance beyond the generic **classical MD** checklist.

## Limitations

Tutorial scope: **not** tied to one **force field** or **material**; readers must map recommendations to their **potential**, **boundary conditions**, and **stability constraints**. Reactive potentials add timestep and bond-order bookkeeping costs that the overview mentions only at a high level, so practitioners coupling shock protocols to chemistry should consult software-specific stability guidance beyond the generic MD checklist summarized here.

## Relevance to group

Useful **cross-reference** for **reactive shock** or **MSST** studies in the corpus; **orthogonal** to **ReaxFF chemistry** unless explicitly coupled in a given paper.

## Citations and evidence anchors

- DOI: [10.1063/5.0076266](https://doi.org/10.1063/5.0076266)

## Reader notes (navigation)

- Methods companion to reactive shock studies in the corpus; cross-link [[reaxff-family]] when comparing MSST/NEMD setups to ReaxFF chemistry workflows.

## Related topics

- [[reaxff-family]]
