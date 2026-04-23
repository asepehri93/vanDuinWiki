---
id: paper:2019kwon-fuel-262-201-numerical-simulations
type: paper
title: "Numerical simulations of yield-based sooting tendencies of aromatic fuels using ReaxFF molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:reactive-md
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2019.116545"
year: 2019
authors:
  - "Hyunguk Kwon"
  - "Sharmin Shabnam"
  - "Adri C. T. van Duin"
  - "Yuan Xuan"
venue: "Fuel"
pdf_sha256: "7dfac75a53d3b1162e73ff2d89d4a8f5dce85270c8b8d7a518670d17d31060a0"
pdf_path: "papers/Kwon_Fuel_2020_Sooting_Tendencies.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019kwon-fuel-262-201-numerical-simulations -->

## Summary

Soot formation from combustion is often ranked experimentally using **yield-based** metrics such as the **Yield Sooting Index (YSI)**, which connects **fuel molecular structure** to **soot yield** in standardized flame configurations. Prior **ReaxFF** work explored **soot precursor chemistry** and **reaction networks**, but had not, before this study, adopted the **experimental YSI measurement concept** inside a reactive MD workflow. This **Fuel** article presents a **multi-stage ReaxFF simulation procedure** designed to mirror the YSI definition’s reliance on **soot volume fraction** trends under a **nitrogen-diluted methane/air** diffusion-flame surrogate, enabling **quantitative** ReaxFF-derived YSI values to be compared against tabulated measurements. The motivation is pragmatic: many **oxygenated** or **bio-derived** fuels lack complete **detailed kinetics**, yet engineers still need **relative sooting** rankings; a ReaxFF-based YSI framework could support screening when trustworthy kinetic models are unavailable. Conceptually, the paper’s advance is **metric alignment**: instead of inventing an ad hoc soot proxy, it adapts the **YSI** definition’s emphasis on **soot volume fraction** trends in a standardized flame surrogate, then shows how ReaxFF observables can be mapped onto that construct for **toluene** and **phenol** benchmarks.

## Methods

### Experimental YSI concept (for readers)

**YSI** (as used in experiment and in CFD) is a **linear** function of the **maximum** **soot** **volume** **fraction** **\(f_{v,\max}\)** on the **centerline** of a **nitrogen**-**diluted** **CH₄**/**air** **co-flow** **laminar** **diffusion** **flame** when a **~1000** **ppm** (mole) **dopant** is added to the **fuel** stream (intro and **Sec. 1** in the *Fuel* article). The **ReaxFF** **work** **mirrors** that **construct** in a **reactive** **MD** **post-processing** **framework** **(Sec. 2–3)**.

### 1 — MD application (ReaxFF, multi-stage NVT)

**Engine / platform name:** **N/A** — the *Fuel* **PDF** **text** does **not** name a **LAMMPS**-style **integrator** in the **sections** **checked**; all **operational** **settings** are **in** the **article** **body**. **ReaxFF** **parameterization:** **CHO-2016** **(Sec. 2,** **cited** as **[39])**. **PBC** **3D** **cubic** **~38.6** **Å** **cell** with **ρ** **=** **0.28** **kg/dm³** **(fuel**-**rich** **CH₄**/**O₂,** **equivalence** **ratio** **3.5** per **the** **paper**)**. **Minimization** then **NVT** **25** **ps** **at** **1500** **K** **(Sec. 2** **text**)**. **Second** **NVT** **at** **3000** **K** **with** **Berendsen** **thermostat** **(damping** **100** **fs**)**; **run** **until** **maximum** **reactivity** **(radical** **count**)**; **intermediate** **pool** **composition** **Table** **1** **(Sec. 2** **and** **Table** **1**)**. **Doping:** **add** **42** **“test”** **molecules** as **benzyl** (toluene) **or** **phenoxy** (phenol) **(Sec. 2–3)**, **systems** **~2308** or **~2224** **atoms,** **ρ** **~0.39** **kg/dm³**; **dopant** **mole** **fraction** **>1000** **ppm** in **RMD** **(authors** **justify** **per** **Sec. 2**)**. **Final** **NVT-MD** at **2200 K, 2400 K, 2600 K** **(five** **independent** **replica** **seeds,** **random** **dopant** **placements**)**. **Durations** **(Sec. 4.1,** **Fig.** **2):** **e.g. ~6** **ns** **(2200** **K)**, **~3.5** **ns** **(2400** **K)**, **~2** **ns** **(2600** **K)**, **terminated** when **key** **species** **(CO,** **H₂O,** **C₂H₄,** **…)** **reach** **plateau** **(Sec. 4.1** **text**)**. **Time** **step** **(fs):** **N/A** — not **reliably** **recovered** from the **text**-**extracted** **PDF** **here**; **read** the **VOR** **/Methods** for **reproduction**. **Barostat / isotropic** **pressure** **servocontrol:** **N/A** **—** **NVT** **stages** **only** in **the** **stated** **protocol**. **Electric** **field** / **replica** **/metadynamics:** **N/A**.

### 2 — Force-field training

**N/A** — **adopts** the **published** **CHO-2016** **field** **([39]**, **improving** on **CHO-2008** **for** **C₁** **chemistry** per **Sec. 2**); **no** **in-paper** **reoptimization**.

### 3 — Static QM / DFT

**N/A** — the **kinetic** **pictures** **(toluene** **vs** **phenol**)** are **grounded** in **prior** **chemical** **kinetics** **literature**; **ReaxFF** **(CHO-2016)** is **the** **quantitative** **reactive** **engine**.
## Findings

### Mechanisms (soot-relevant chemistry)

**Toluene:** simulations emphasize **ring-retaining** growth to **larger aromatics**. **Phenol:** aromatic growth couples to **carbon-loss** channels with **CO** release—consistent with the article’s comparison to established **kinetic** pictures.

### Quantitative YSI

**ReaxFF-derived YSI** values show **reasonable agreement** with **measured** YSI for the **benchmark** fuels, supporting **relative** sooting rankings when **detailed** mechanisms are unknown.

### Limitations and future scope

Demonstration is for **two** aromatics; extending to **oxygenated**/**blend** fuels and quantifying **uncertainty** needs further validation. The approach complements—not replaces—**detailed kinetics** **CFD** YSI workflows where **mechanisms** are mature.

## Limitations

Corpus `pdf_path` may reflect **pre-final** **volume**/**pagination**; use the **VOR** **at** the **DOI** for **authoritative** **Table** / **figure** **numbering** and any **line**-**edits** not present in a **local** **“Fuel xxx”** **preprint** **file**.

## Relevance to group

Demonstrates quantitative coupling of **ReaxFF** chemistry to an experimentally rooted **sooting metric (YSI)** for **aromatic fuels**.

## Citations and evidence anchors

- DOI: [10.1016/j.fuel.2019.116545](https://doi.org/10.1016/j.fuel.2019.116545)

## Related topics

- [[reaxff-family]]
