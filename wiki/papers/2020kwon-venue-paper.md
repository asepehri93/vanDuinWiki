---
id: paper:2020kwon-venue-paper
type: paper
title: "ReaxFF-based molecular dynamics study of bio-derived polycyclic alkanes as potential alternative jet fuels"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:reactive-md
  - keyword:combustion
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2020.118548"
year: 2020
authors:
  - "Hyunguk Kwon"
  - "Aditya Lele"
  - "Junqing Zhu"
  - "Charles S. McEnally"
  - "Lisa D. Pfefferle"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Fuel (Elsevier galley proof PDF in corpus; see sibling page for version-of-record PDF)"
pdf_sha256: "66e95f3921e086b434a93d2f98fcac411a9004dc1e1c03288b3dbec359e0c0be"
pdf_path: "papers/Kwon_Lele_Fuel_2020_Jetfuel_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2020kwon-venue-paper -->

## Summary

ReaxFF reactive molecular dynamics is used to study the initial stages of pyrolysis of two bio-derived head-to-head polycyclic alkanes (HtH-1 and HtH-2) proposed as high energy-density aviation fuels, including mixture effects and comparison to conventional jet-fuel chemistry. The work examines thermal decomposition of HtH-1 (C18H32) and HtH-2 (C18H34) with ReaxFF MD. Global Arrhenius parameters characterize overall kinetics; a systematic reaction-analysis framework extracts temperature-dependent pathways. HtH-1 decomposes faster than HtH-2 under matched temperature and density, and faster than JP-10 in the same framework. Dominant bond-breaking channels shift from central inter-ring C–C scission at lower temperature toward C–CH3 cleavage at higher temperature. Major product distributions differ between fuels and are discussed in relation to sooting tendency and experiments. Binary mixtures show largely unimolecular chemistry with weak cross-talk between components.

!!! note "Corpus note"
    The corpus holds an **uncorrected proof** PDF. For the version-of-record file path, see [[2020kwon-fuel-279-202-reaxff-based-molecular]].

## Methods

**Note:** `pdf_path` is the **Elsevier galley**; for final tables, use [[2020kwon-fuel-279-202-reaxff-based-molecular]] if values differ.

**1 — MD application (ReaxFF pyrolysis).** **Engine / code:** **ReaxFF** reactive **MD** in **LAMMPS** (as in the **Fuel** **galley** / **VOR**). **System size & composition:** **3D** **periodic** **vapor** **boxes** with **40** **fuel** **molecules** per **single-**-**component** **case** at **mass** **densities** **0.1–0.3** **kg** **dm⁻³**; **binary** **mixtures** keep **40** **molecules** **total** with **HtH-1** **mole** **fractions** **α** = **0.9,** **0.7,** **0.5**. **Boundaries / PBC:** **3D** **periodic**. **Ensemble:** **NVT** at **fixed** **box** **volume** **(ρ** **set** **by** **loading**)**—** **N/A** for **NPT** **1** **atm** **barostat**-**style** **pressure** **servicing** **(constant-**-**V** **heating** **of** **vapor**)**. **Timestep:** **0.1** **fs** **production**; **0.05** **fs** **at** **3000** **K** **for** **convergence** **checks** **(article** **/ SI)**. **Duration / stages:** **equilibration** **NVT** **1500** **K** **for** **2.5** **ps** **(designed** **to** **limit** **decomposition**); **production** **NVT** **1500–3000** **K** **(full** **ns**-**scale** **windows** in **source**)**. **Thermostat:** **Berendsen** **with** **100** **fs** **damping**. **Barostat / hydrostatic pressure:** **N/A** **(NVT** **only** **in** the **cited** **stages**)**. **Temperature (K):** **1500–3000** **K** **as** **above**; **1500** **K** **also** **used** **with** **CVHD** **(below)**. **Electric field / shock / shear:** **N/A**. **Replica / enhanced sampling:** **control-**-**variable**-**driven** **hyperdynamics** **(CVHD)** **at** **1500** **K** **to** **accelerate** **rare** **reaction** **events** **(per** **article**); **umbrella** **/ metadynamics:** **N/A** **(not** **stated** **in** **the** **galley** **bullets** **used** **here**)**. **Analysis:** **in-**-**house** **reaction**-**analysis** **code** **on** **trajectories**; **global** **Arrhenius** **fits**; **optional** **ReaxFF** **PES** **sampling** **for** **selected** **channels** **(see** **article**)**.

**2 — Force-field training.** **N/A**—uses a **published** **C/H** **ReaxFF** **(cited** **in** the **article**), **not** a **de** **novo** **fit** **in** this **manuscript**.

**3 — Static QM / DFT-only.** **N/A**—**ReaxFF** **MD** **is** the **sampling** **method** **for** **the** **reported** **kinetics** **(QM** **only** **as** **reference,** **if** **any,** **per** **VOR**)**.**

## Findings

- HtH-1 shows faster decomposition than HtH-2 at the same conditions and faster kinetics than JP-10 in the same simulation setup.
- Mechanisms are temperature-dependent: central C–C inter-ring breaking dominates at lower temperature; **C–CH3** bond breaking becomes increasingly important at higher temperature due to entropic effects.
- Major products reported include **C5H8** and **C4H8** from HtH-1 and **C4H8** and **C2H4** from HtH-2; the authors relate product slate to **sooting tendency**, consistent with measurements for HtH-1 vs HtH-2.
- In **binary mixtures**, HtH-1 and HtH-2 react primarily through **unimolecular** channels with **little mutual interaction** during pyrolysis at the conditions sampled.
- The study is framed as demonstrating ReaxFF-MD plus automated reaction analysis for complex fuel chemistries **without pre-specified reaction networks**.

## Limitations

Proof-stage PDF; kinetic parameters and product statistics are simulation-level and depend on the ReaxFF parameterization and the elevated temperatures used to sample reactions in nanosecond-scale MD.

## Relevance to group

Penn State co-authorship (van Duin, Kwon, Lele, Xuan); extends ReaxFF pyrolysis workflows to new bio-derived polycyclic fuels.

## Reader notes (navigation)

- [[2020kwon-fuel-279-202-reaxff-based-molecular]]
- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
