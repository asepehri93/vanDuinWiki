---
id: paper:2019ganeshan-molecular-si-multiply-accelerated
type: paper
title: "Multiply accelerated ReaxFF molecular dynamics: coupling parallel replica dynamics with collective variable hyper dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - domain:fuel-combustion
  - domain:batteries-electrochemistry
  - method:reaxff
  - method:enhanced-sampling
  - task:method-development
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:enhanced-sampling
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:lammps
source_refs: []
doi: "10.1080/08927022.2019.1646911"
year: 2019
authors:
  - "Karthik Ganeshan"
  - "Md. Jamil Hossain"
  - "Adri C. T. van Duin"
venue: "Molecular Simulation (2019)"
pdf_sha256: "69195252811561bf512082e80f19559beb684024c0117fbfc242d44e3078cc06"
pdf_path: "papers/Ganeshan_Hossain_MolSym_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019ganeshan-molecular-si-multiply-accelerated -->

## Summary

Rare-event **reactive molecular dynamics** with **ReaxFF** still faces a **time-scale gap** even on large clusters because **sub-femtosecond** timesteps are required for stable **bond-order** dynamics. The article therefore examines **synergistic acceleration** by coupling **parallel replica dynamics (PRD)** with **collective-variable hyperdynamics (CVHD)** within the **ReaxFF** workflow. **PRD** exploits **ergodicity**-style arguments to replace one long trajectory with **M** shorter replicas that explore independent escape routes from a basin, shortening **wall-clock** time to the first **reactive transition**. **CVHD** instead **biases** the **potential** landscape along selected **collective variables** to lower **barriers**. The authors benchmark the combined scheme on **n-dodecane pyrolysis** and on a more aggressively reacting **ethylene carbonate / lithium** system representative of **battery-electrolyte** chemistry.

## Methods

### ReaxFF model and collective variables (A)

Reactive interactions use **ReaxFF** as implemented in the authors’ **LAMMPS** / **PuReMD** workflow; **n-dodecane pyrolysis** benchmarks adopt the **C/H/O** parameterization of **Chenoweth et al.** (cited in the article). **CVHD** requires **collective variables** and **bias** deposition parameters (Gaussian height/width, deposition interval, event wait—values stated in **Molecular Simulation** Methods); **PRD** requires **replica** counts, **correlation**/**dephasing** times, and **bond-order**-based **event** detection (e.g. **bond-order cutoff ~0.3** for intact **n-dodecane**).

### Parallel replica dynamics and hyperdynamics (B)

**PRD:** broadcast/minimize a configuration across **M** replicas, assign independent **Maxwell–Boltzmann** velocities, **dephase**, then run reactive **MD** until a **first reaction** criterion triggers (merge policy for wall-clock acceleration as in the paper). **CVHD:** history-dependent **bias** along collective variables to accelerate **rare** escapes. **Combined PRD+CVHD:** effective hypertime from **CVHD** combined with **PRD** sampling; the article gives **n-dodecane** cell geometry (**24** molecules, **50 Å** cubic cell, **1200 K** and **1500 K**), **CVHD** parameters following **Bal and Neyts**, and **PRD** parameters (**t_corr**, **t_dephase**). **EC/Li** uses the **organic carbonate / lithium** **ReaxFF** line appropriate to that chemistry.

### DFT / static QM (C)

**Not applicable** to the method demonstration beyond **prior ReaxFF** training literature.

**Reactive MD integration.** Production **molecular dynamics** uses **LAMMPS** / **PuReMD** with **ReaxFF** bond-order updates on **periodic** cubic **cells** (**50 Å** side for **n-dodecane** benchmarks) containing **24** molecules (order **10³ atoms** total). **Temperature:** **1200 K** and **1500 K** **thermal** setpoints as reported. **Timestep:** sub-**femtosecond** **timestep** values appropriate to **ReaxFF** stability are quoted in the article’s **Computational Methods** (see `pdf_path`). **Duration:** **CVHD** bias deposits on **0.2 ps** intervals with **1 ps** event waits; **PRD** uses **t_corr = 10 ps** and **t_dephase = 5 ps** as stated above. **Ensemble:** **NVT**-style **thermal** control during biased production (details in article). **Thermostat:** specified with the **CVHD** implementation in **Molecular Simulation** (see **PDF**). **Barostat / pressure:** **N/A** — constant-volume **supercells** without **GPa** **pressure** coupling in the summarized benchmarks. **External electric field:** **N/A**. **Enhanced sampling:** **parallel replica dynamics** plus **collective-variable hyperdynamics** are the core **accelerated dynamics** workflow.

## Findings

### Mechanisms (when stacking helps)

For **n-dodecane pyrolysis**, **PRD** on top of **CVHD** yields **extra wall-clock speedup** vs **CVHD** alone when **replica** parallelism harvests **first-passage** events effectively. For **EC/Li**, **CVHD** already **strongly accelerates** reactions, so **PRD** adds **diminishing** incremental benefit—consistent with **PRD** scaling **inversely** with **transition rate** when **CVHD** has already raised rates.

### Limitations

**Biased** dynamics alter **kinetics**; **PRD** assumptions break if **memoryless** transition statistics fail. Absolute **rates** need **reweighting** or **unbiased** checks where feasible.

### Future outlook

The abstract argues the **qualitative** **non-additivity** pattern should **generalize** across many reactive systems; **absolute** **kinetic** constants remain **validation**-limited.

## Limitations

**Hyperdynamics** introduces **bias potentials** that alter **dynamics**; **PRD** assumes transitions are **memoryless** enough for **parallel** harvesting. Combining both methods complicates **interpretation** of **absolute** **kinetic** constants compared to **direct** **MD**.

## Relevance to group

van Duin-group **methods** paper on **rare-event** **acceleration** for **ReaxFF**, relevant to **combustion** pyrolysis and **electrolyte** decomposition workflows that share **stiff** chemistry and **long** waiting times.

## Reader notes (navigation)

- [[reaxff-family]]
- Compare acceleration metrics here with other **CVHD** / **PRD** studies in the corpus when tuning **bias** parameters.

## Citations and evidence anchors

https://doi.org/10.1080/08927022.2019.1646911

## Related topics

- [[reaxff-family]]
