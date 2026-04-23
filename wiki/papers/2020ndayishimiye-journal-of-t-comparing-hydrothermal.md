---
id: paper:2020ndayishimiye-journal-of-t-comparing-hydrothermal
type: paper
title: "Comparing hydrothermal sintering and cold sintering process: mechanisms, microstructure, kinetics and chemistry"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - material:oxide
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.jeurceramsoc.2019.11.049"
year: 2020
authors:
  - "Arnaud Ndayishimiye"
  - "Mert Y. Sengul"
  - "Sun Hwi Bang"
  - "Kosuke Tsuji"
  - "Kenji Takashima"
  - "Thomas Hérisson de Beauvoir"
  - "Dominique Denux"
  - "Jean-Marc Thibaudeau"
  - "Adri C. T. van Duin"
  - "Catherine Elissalde"
  - "Graziella Goglio"
  - "Clive A. Randall"
venue: "Journal of the European Ceramic Society"
pdf_sha256: "3440ff87756302f082574b6ecbfcc2fc07a7a89b09ff0d62bfe33e69b10174a2"
pdf_path: "papers/Ndayishimiye_JECS_2019_sintering.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020ndayishimiye-journal-of-t-comparing-hydrothermal -->

## Summary

**ZnO** is densified by **hydrothermal sintering (HS, closed)** vs **cold sintering (CSP, open)** at **155 ± 5 °C** and **320 MPa** with dwell times **0–80 min**. Both routes reach very high relative density with similar ZnO structure, but differ in stabilized side phases, grain size evolution, and trapped solvent/organics. **Zinc acetate “bridges”** appear in HS samples. ReaxFF simulations compare HS-like vs CSP-like solvent environments and connect acetate clustering to observations (e.g., Zn–Zn pair correlations in clusters, pathways toward acetate crystals consistent with XRD/SEM).

## Methods

- **Sintering:** HS vs CSP as in the abstract—**155 ± 5 °C**, **320 MPa**, dwell **0, 20, 40, 80 min**; characterization includes XRD/Rietveld, electron microscopy, Raman, TG-MS, etc. (per section 2).
- **ReaxFF setup:** Nonpolar **ZnO (10̄10) wurtzite** slab (**14** layers, **3528** atoms); solvent with **100 Zn²⁺**, **50 H₂O** and **two acetates per Zn²⁺** (total **16500** atoms in solvent region) for interface equilibration at **300 K**; CSP-like boxes add vacuum normal to the surface while keeping liquid density; HS-like boxes heated toward **500 K** with **0.002 K/fs** ramp.
- **Potential & integrator:** ZnO/acetic-acid/water ReaxFF from cited prior work with reoptimization for sub/supercritical acetic-acid–water mixtures; MD in **ADF**; **0.25 fs** timestep; **velocity Verlet**; **Berendsen** thermostat (**0.1 ps** damping).
- **Extended clustering run:** Surface removed; **20100**-atom solvent (**100 Zn²⁺**, **200 acetate**, **6200 H₂O**) simulated **1 ns** to probe hydrothermal clustering.

**MD protocol (same ReaxFF runs, complementing the bench sintering above).** All trajectories are **3D** cells in **Amsterdam Density Functional (ADF)** using **ReaxFF-based reactive molecular dynamics** with **PBC** for the **wurtzite (10̄10) ZnO slab** and the bulk-solvent boxes. Integration uses **0.25 fs** timesteps, **velocity Verlet**, and a **Berendsen** thermostat (**0.1 ps** damping) under **NVT**-like control. **CSP-like** and **HS-like** solvent boxes differ by **vacuum** along the surface normal and, for HS-like cells, **ramped heating** (**0.002 K fs⁻¹** toward **500 K** in the paper). **Barostat / NPT: N/A —** these interfacial and clustering MD stages are not the **uniaxial** **NPT sintering** in the autoclave (**155 ± 5 °C**, **320 MPa**; dwell **0, 20, 40, 80 min**). **Electric field: N/A —** not used. **Shear / shock: N/A —** not used. **Replica or enhanced sampling: N/A —** not used. **2 — Force-field training: N/A —** a published ZnO–acetic-acid–water ReaxFF is reoptimized/used for sub/supercritical acetic–water conditions as cited, not a new full parameterization in this work. **3 — Static QM: N/A —** primary quantum benchmarks are via cited prior work and comparison to experiment, not a new DFT surface study here.

## Findings

Relative densities above **98%** are reported at **0 min** dwell for both hydrothermal sintering (HS, closed) and cold sintering (CSP, open), but **later** density trends are **not** **monotonic** in the same way for the two routes—so a single “best dwell” is **route**-dependent. XRD, microscopy, Raman, and TG-MS separate oxygen-related **defect** populations, **grain** structure, and **zinc** **acetate** signatures; **HS** samples show **bridging** / **zinc** **acetate** features that **CSP** does not reproduce under the same **T/P** path. The **ReaxFF** **MD** then connects **HS-like** solvent and temperature histories to **acetate**-mediated Zn **clustering** and pair-correlation behavior consistent with **larger** **zinc** **acetate** crystals in **HS**-processed **pellets**—a mechanistic **story** for **microstructure** divergence even when final **relative** **density** is high in both routes at **155 ± 5** **°C** and **320** **MPa** with dwells **0, 20, 40, 80** **min**. The authors’ comparison stresses **reactor** **path** (closed **hydrothermal** vs open **CSP**), **humidity**, and **trapped** organics, not just peak density. **As they frame it**, short **interfacial** and **1** **ns** **clustering** simulations do **not** stand in for full **autoclave** kinetics, **grain** growth, or **volatile** **escape** at the **reactor** scale.

## Limitations

Simulation sizes/times capture precursor clustering chemistry, not full pellet-scale sintering kinetics; ReaxFF for ZnO–acetate–water is specialized to this interface chemistry.

## Relevance to group

Penn State MRI/MSE/ME collaboration (Randall, van Duin, Ndayishimiye, Sengul, Bang, Tsuji) with international coauthors.

## Reader notes (navigation)

- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
