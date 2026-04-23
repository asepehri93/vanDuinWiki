---
id: paper:2019jensen-carbon-journ-toward-ultralight
type: paper
title: "Toward Ultralight High Strength Structural Materials via Collapsed Carbon Nanotube Bonding"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nose-hoover
source_refs: []
doi: "10.1016/j.carbon.2019.09.090"
year: 2019
authors:
  - "Benjamin D. Jensen"
  - "Jae-Woo Kim"
  - "Godfrey Sauti"
  - "Kristopher E. Wise"
  - "Liang Dong"
  - "Haydn N. G. Wadley"
  - "Jin Gyu Park"
  - "Richard Liang"
  - "Emilie J. Siochi"
venue: "Carbon"
pdf_sha256: "4649d2e23a813eacb17d316f1b8ba69c9017699b7d4423d69216ce751aaa73eb"
pdf_path: "papers/ReaxFF_others/Jensen_Carbon_2019_CNT_pressure_preprint.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019jensen-carbon-journ-toward-ultralight -->

!!! note "Journal pre-proof"
  Corpus PDF is an **Elsevier Journal Pre-proof** (not guaranteed identical to final **pagination/typesetting**).

## Summary

**LAMMPS** **ReaxFF** (**C-2013**) simulations pressurize **parallel** and **perpendicular** arrangements of **double-walled CNT** stacks (~**120k** atoms, **~8 nm** inner diameter, mixed **armchair/zigzag** chirality) to induce **covalent bonding** across **collapsed** tubes—mirroring **spark plasma sintering** experiments on **CNT sheets**. **Pressure–structure** snapshots inform **processing** conditions for **ultralight** **high-strength** solids. The **NASA**/**aerospace** motivation is **structural** **nanocarbon** **preforms** where **vdW** **cohesion** alone limits **strength**; **pressure-induced** **crosslinking** is explored as a **processing** route analogous to **SPS** **densification** observed in **buckypaper**-like **samples**.

## Methods

### Force field (A)

**ReaxFF** **C-2013** parameterization for **carbon** **condensed-phase** chemistry (**LAMMPS** implementation); used to capture **pressure-induced** **C–C** bond formation between **CNT** walls without a **predefined** bond topology.

### Reactive MD and processing mimic (B)

**Engine / analysis:** **LAMMPS**; **OVITO** for visualization; coordination / **diamond** identification with **~0.18 nm** cutoff.

**Systems:** **Periodic** cells with **parallel** **bundles** (**4** tubes) vs **perpendicular** **junction** (**2** tubes); **double-walled** stack geometry and dimensions as in *Carbon* **Methods**.

**Thermodynamics / loading:** **Isothermal** **pressure ramps** at **300 K, 1000 K, 2000 K, 3000 K** (default **50 GPa/ns**; portions at **500 GPa/ns** where response is flat). **Ensemble:** **NPT**-style anisotropic stress control: **Langevin** **thermostat** with **Nose–Hoover** **anisotropic** **barostat**; **parallel** geometry fixes **axial** stress **0** and loads **transverse**; **perpendicular** geometry loads normal to junction (overlap-area correction **~17%** as stated).

**Integration:** **0.2 fs** timestep (some **high-T** repeats at **0.1 fs**).

**Post-processing:** snapshots each **5 GPa**; optional **quench** (**10 ps** to **300 K**, hold **10 ps**) to interrogate **bonding** snapshots.

**Electric field:** **N/A** — not applied. **Replica / enhanced sampling:** **N/A** — not used (direct **MD** only).

### DFT (C)

**Not reported** as primary—**ReaxFF** drives the **large-scale** **welding** study.
## Findings

### Mechanisms

Reactive **C–C crosslinking** under **pressure** yields **load-bearing** networks beyond **vdW** **sheet** cohesion; **parallel** **collapse** vs **perpendicular** **junction** **welding** produce distinct **microstructures**. **Pre-strained** experimental **sheets** show larger gains after **SPS**, consistent with improved **tube–tube** contact.

### Processing guidance

Simulations bracket **P–T** windows where **bonding** activates without **excessive** **damage**—useful for **textile** **preform** design.

### Limitations and future constraints

**C-2013** omits **catalyst** chemistry (**Fe** in experiments); **disorder**, **sp/sp²** mixing, **oxygen** functionality, **solvent/binder** effects, and **non-ideal** contacts can shift real **yields** vs idealized cells.

## Limitations

**ReaxFF C-2013** omits **explicit** **metallic** **catalyst** chemistry (**Fe** particles in experimental sheets are not fully modeled). **Turbostratic** **disorder**, **sp**/**sp²** **mixing**, and **oxygen** **functionalities** on **real** **CNT** **surfaces** may shift **crosslink** **yields** relative to the **idealized** **bundles** simulated. **Residual** **solvent** and **polymer** **binders** in **experimental** **preforms** can change **effective** **contact** **area** and **local** **heating** during **SPS** compared to **pristine** **simulation** **cells**.

## Relevance to group

Demonstrates **large-scale** **ReaxFF** **CNT** **mechanochemistry** tied to **processing** of **nanocarbon** **preforms**.

## Citations and evidence anchors

- `papers/ReaxFF_others/Jensen_Carbon_2019_CNT_pressure_preprint.pdf`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

## Reader notes (navigation)

The **preprint** filename in `pdf_path` signals **Elsevier** **pre-proof** status—confirm **pagination** against the **final** **Carbon** issue when citing **figure** numbers.
