---
id: paper:2018aussems-carbon-137-2-mechanisms-elementary
type: paper
title: "Mechanisms of elementary hydrogen ion-surface interactions during multilayer graphene etching at high surface temperature as a function of flux"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:classical-md
  - method:enhanced-sampling
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:enhanced-sampling
  - keyword:lammps
  - keyword:reaxff-application
  - keyword:nve-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2018.05.051"
year: 2018
authors:
  - "D. U. B. Aussems"
  - "K. M. Bal"
  - "T. W. Morgan"
  - "M. C. M. van de Sanden"
  - "E. C. Neyts"
venue: "Carbon, 137 (2018) 527–532"
pdf_sha256: "9c88f66552b9cc0b06f9288c7095deede1a5d3aeec41fa7c3d4648c8b3dfa662"
pdf_path: "papers/ReaxFF_others/Bal_H_plasma_graphene_Carbon_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018aussems-carbon-137-2-mechanisms-elementary -->

## Summary

Atomistic **molecular dynamics** study of **multilayer graphene** etched by **5 eV H⁺** impacts at **1000 K** surface temperature, addressing the **time-scale gap** between fast ion-impact chemistry and slower thermal processes (diffusion, desorption) by **collective variable–driven hyperdynamics (CVHD)**, extending the **inter-impact time** to a more experimentally relevant **ion flux**.

Plasma–surface modeling motivation is that laboratory **ion fluxes** are far lower than affordable **direct MD** inter-impact intervals, so **CVHD** accelerates rare thermal events between **H** impacts without assuming a fixed **effective** temperature path that misses barrier crossings.

## Methods

From the article PDF (`pdf_path`).

- **Interactions:** **ReaxFF** with the parameter set of **Mueller et al.** (as cited in the paper). **5 eV** **H** projectiles impact the surface at normal incidence at random in-plane positions.
- **Substrate and temperature:** **Four** **ABAB-stacked** graphene layers, lateral size **20 A x 20 A**, periodic in **x,y**; initial surface temperature **1000 K**. After each impact, dynamics run **1 ps** in the **NVE** ensemble, then **1 ps NVT** with a **Nose-Hoover-style** thermostat to re-cool the substrate.
- **Inter-impact (CVHD):** The waiting time before the next impact is advanced with **collective-variable hyperdynamics (CVHD)** using **0.1 fs** MD steps, Gaussian bias updates every **100 fs**, and bond-range biasing on **C-C** and **C-H** distances (ranges given in the article). The long inter-impact segment reaches **~1 ms** physical time (flux **~10^23 m^-2 s^-1** in the abstract), giving roughly **six orders of magnitude** extension vs short inter-impact baselines; **3000** impacts (**3 ps** and **1 ns** cases) or **1700** impacts (**1 ms** case) as stated.
- **Software:** **LAMMPS** with a modified **Colvars** module (references in the paper).
- **System size:** Four-layer **ABAB** graphene stack in a **20 Å × 20 Å** lateral cell (thousands of **carbon atoms** plus adsorbed **hydrogen**; exact counts in the *Carbon* **Methods**).
- **Boundaries:** In-plane **periodic boundary conditions** with open or fixed out-of-plane conventions as in the article for the ion-bombarded stack.
- **Barostat / pressure:** **N/A — hydrostatic pressure control** is not used for the quoted CVHD / post-impact segments; cell volume follows the fixed lateral supercell described in the **PDF**.
- **Electric field:** **N/A —** no applied **electric field** in the summarized protocol.
- **Enhanced sampling:** **Collective-variable hyperdynamics (CVHD)** accelerates rare bond events between impacts (distinct from umbrella sampling / metadynamics).

**2 — Force-field training:** **N/A —** this work applies a published **ReaxFF** parameterization (**Mueller et al.**, as cited in *Carbon*) to **H** on multilayer graphene; it does not report a new **QM**-driven refit or updated **ReaxFF** parameter table.

**3 — Static QM / DFT-only:** **N/A —** the ion-bombardment study is **classical reactive MD** with optional semi-empirical modeling of flux–temperature regimes in the **Introduction**; any **DFT** references are contextual literature, not the paper’s central **AIMD** protocol.

## Findings

- **Mechanism / outcomes:** Without reaching **long inter-impact times**, MD tends to probe only very **fast** reflection/adsorption channels; with **CVHD**, **thermal** processes such as **surface diffusion**, **recombinative desorption**, and related **relaxation** become accessible at **ms–µs**-scale effective spacing, changing **hydrogen uptake** and **surface evolution** (per *Carbon* **Results**).
- **Comparisons:** The introduction contrasts prior **MD** studies at unrealistically high **ion flux** with fusion / ion-beam **experiments** at much lower flux; extending inter-impact time is argued to better overlap with those **experimental** regimes.
- **Sensitivity:** **Surface temperature** (**1000 K** in the abstracted setup) and effective **ion flux** (down to **~10²³ m⁻² s⁻¹** in the long CVHD case) strongly shift the balance of **ion-induced** versus **thermally induced** chemistry.
- **Limitations / outlook:** The abstract stresses that **long time scales** are required alongside accurate elementary **ion–surface** physics—remaining uncertainties about specific **desorption** channels are discussed in the **PDF** Discussion.
- **Corpus honesty:** Numbers here follow the peer-reviewed **PDF** at `pdf_path` and the indexed **extract**; verify final **timestep** ranges and bias-update cadence in the journal text before reuse in MAS pipelines.

## Limitations

- Quantitative cross-validation against a specific experimental beam/plasma setup depends on matching **flux**, **surface temperature**, and **defect** structure; the extract does not restate all simulation sizes or force-field details here.

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
