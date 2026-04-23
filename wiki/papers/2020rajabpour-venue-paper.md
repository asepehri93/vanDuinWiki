---
id: paper:2020rajabpour-venue-paper
type: paper
title: "Low-temperature carbonization of polyacrylonitrile/graphene carbon fibers: a combined ReaxFF molecular dynamics and experimental study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:experiment-integrated
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:validation-experiment
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1016/j.carbon.2020.12.038"
year: 2020
authors:
  - "Siavash Rajabpour"
  - "Qian Mao"
  - "Zan Gao"
  - "Mahdi Khajeh Talkhoncheh"
  - "Jiadeng Zhu"
  - "Yosyp Schwab"
  - "Malgorzata Kowalik"
  - "Xiaodong Li"
  - "Adri C. T. van Duin"
venue: "Carbon (Elsevier uncorrected proof PDF in corpus)"
pdf_sha256: "dc68f6f76f3290a419a4f729a9bb44fa37753cdc133b5a8ed367540f14e0a3e0"
pdf_path: "papers/Rajabpour_Carbon_2020_lowT_carbonization_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2020rajabpour-venue-paper -->

!!! note "Corpus PDF role"
    **Uncorrected proof** PDF (`Rajabpour_Carbon_2020_lowT_carbonization_galley.pdf`). The **version-of-record** PDF and primary curation: **[[2020rajabpour-carbon-174-2-low-temperature-carbonization]]**.

## Summary

**Polyacrylonitrile (PAN)**-derived **carbon fibers** are workhorse structural materials; **graphene** additives are explored to **catalyze** **carbonization** chemistry so that **high** mechanical properties can be achieved at **lower furnace temperatures**, saving **energy** and **processing** cost. This *Carbon* article couples **ReaxFF** reactive MD of **oxidized PAN** models with **graphene** inclusions to **accelerated**-temperature trajectories with **experimental** carbonization of **PAN** versus **PAN/graphene** fibers at **1250 °C** versus **1500 °C** setpoints. The simulation narrative emphasizes **graphene edges** and **heteroatom** (**N/O**) functionality as **nucleation** sites that promote **ring alignment** and **graphitic** cluster formation relative to **oxidized PAN** alone. Experiments report large gains in **tensile strength** and **Young’s modulus** for **graphene-containing** fibers carbonized at **1250 °C** compared with **neat PAN** at **1500 °C**, framing the **low-temperature** processing advantage.

## Methods

**ReaxFF MD** constructs **oxidized PAN** systems with **graphene**; **NVT** equilibration **60 ps** at **300 K** precedes snapshot selection (**five** frames from the last **5 ps** at **1 ps** spacing). Snapshots are heated to **2200**, **2500**, or **2800 K** at **10 K/ps**, then held **1 ns** per target temperature to sample **high-temperature** chemistry on accessible MD timescales. Integration uses **0.25 fs** timesteps (validated vs **0.10 fs** at **2800 K** in **SI**) and a **Berendsen** thermostat (**100 fs** damping). **Experiments** carbonize fibers and report mechanical properties (abstract values). The **Carbon** abstract states explicitly that **graphene edges** together with **N** and **O** heteroatoms act as **catalytic seeds** that expedite **all-carbon ring alignment** as precursors to **graphitic** structure growth—this is the MD mechanism paired with the **1250 °C** vs **1500 °C** mechanical comparison.

**MD application (ReaxFF).** Same **reactive molecular dynamics** protocol as on **`[[2020rajabpour-carbon-174-2-low-temperature-carbonization]]`**: **NVT** **60 ps** at **300 K**; **five** snapshots; **10 K/ps** ramp to **2200–2800 K**; **1 ns** at each **T**; **0.25 fs**; **Berendsen** **thermostat** (**100 fs** damping). **PBC** **3D** **supercells** of **oxidized** **PAN** + **graphene** (atom **counts** in **VOR** **PDF** if **galley** text is **thin**). **Barostat / NPT: N/A —** as in the **summarized** **protocol**. **Electric field: N/A —** **Replica / metadynamics: N/A —** not used.

## Findings

**MD** supports a mechanism in which **graphene edges** plus **N/O** groups **seed** **graphitic** growth and **alignment** pathways faster than **oxidized PAN** without graphene under the modeled conditions. **Experiments** quote **~91%** higher **tensile strength** (**632 → 1207 MPa**) and **~101%** higher **Young’s modulus** (**88 → 177 GPa**) for **PAN/graphene** at **1250 °C** versus **PAN-only** at **1500 °C** (abstract numbers). Together, the **simulation** story and **mechanical** data motivate **graphene** as a **processing aid** that can partially decouple **ultimate fiber properties** from the **maximum** **furnace** temperature, subject to **microstructure** and **precursor** chemistry details outside the MD cells.

**Sensitivity and corpus honesty:** **MD** uses **2200–2800 K** as **kinetic** **acceleration**; **furnace** **temperatures** in **experiment** differ. This **uncorrected** **proof** may lack final **pagination**; use **`[[2020rajabpour-carbon-174-2-low-temperature-carbonization]]`** for **VOR** **citation** **and** **stable** **mechanical** **table**.

## Limitations

Simulations use **elevated** temperatures to **accelerate** chemistry relative to **furnace** schedules; **quantitative** mapping to **factory** protocols requires caution. **Proof-PDF** lacks final **pagination/typesetting**; cite **[[2020rajabpour-carbon-174-2-low-temperature-carbonization]]** for stable locators.

## Reader notes (navigation)

- Version-of-record page: **[[2020rajabpour-carbon-174-2-low-temperature-carbonization]]**
- [[reaxff-family]]
