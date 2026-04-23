---
id: paper:2021bhamra-x-interfacial-bonding
type: paper
title: "Interfacial Bonding Controls Friction in Diamond-Rock Contacts"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - method:reaxff
  - material:oxide
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:oxide-surface
source_refs: []
doi: "10.1021/acs.jpcc.1c02857"
year: 2021
authors:
  - "Jagjeevan S. Bhamra, James P. Ewen, Carlos Ayestaran Latorre, John A. R. Bomidi, Marc W. Bird, Nabankur Dasgupta, Adri C. T. van Duin, Daniele Dini"
venue: "J. Phys. Chem. C"
pdf_sha256: "19e7aef925bb506ba62f0e6170ca0756ac1f00075bc694fe08cca415fa777a5d"
pdf_path: "papers/Bhamra_Ewen_Diamond_Rock_JPC_C_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021bhamra-x-interfacial-bonding -->

## Summary

Macroscale tribometry compares diamond tips on limestone (calcite-rich) versus granite (quartz-rich) in humid air and water, while nonequilibrium molecular dynamics with newly trained ReaxFF parameters for calcite-related chemistry links friction coefficients to rates and types of interfacial bond formation during sliding.

## Methods

### MD application (nonequilibrium LAMMPS)

- **Engine / code:** **NEMD** in **LAMMPS**; velocity **Verlet**; **0.25 fs** timestep.
- **System size & composition:** **Diamond** tip and **rock** (calcite- vs quartz-dominated) substrate models; interfacial **H₂O** content varied (**0 / 50 / 150** molecules) as reported in the figures. Maximum **Hertz**-scale contact **pressures** for the scanned loads span about **1.9–3.9 GPa** (**diamond**–**calcite**) and **2.0–4.1 GPa** (**diamond**–**quartz**).
- **Boundaries / periodicity:** **Periodic** in **x** and **y**; **bottom** **substrate** layer(s) **frozen**; a **reflective** boundary to retain desorbed species. **N/A**—full lateral cell vectors and atom counts: see `pdf_path` for the reported supercells.
- **Ensemble / control:** `fix langevin`-style **Langevin** **thermostat** at **300 K** (about **25 fs** damping) on selected **tip**/**substrate** layers, consistent with a driven **NEMD** (non-**NVE**) sliding setup. **N/A**—**NPT** **barostat**: inhomogeneous, load-controlled contact rather than bulk isotropic **pressure** control in the same sense as **NPT** bulk equilibration.
- **Equilibration / production:** **Minimization**; **0.1 ns** equilibration with **0.1 nN** normal **load** ramp, then the target **normal** load (about **2.5–40 nN**) and **vₓ = 10 m·s⁻¹** sliding in the main dataset (**1–10 m·s⁻¹** check shows similar friction trends in the text). **0.75 ns** sliding **trajectories**; time-averaged **steady** friction from the last **~200 ps**. Bond order tracked at **1.0 ps** intervals (cutoff **0.3** in the author protocol).
- **Sliding vs experiment:** **Shear** in MD at **m·s⁻¹** speeds, far above the **tribometry** order (**~0.1 m·s⁻¹**); the article discusses scaling/trends accordingly.
- **Long-range / electrostatics in MD:** **N/A**—full **cutoff**/**ReaxFF** QEq schedule in `pdf_path`/SI if needed for reproduction.

### Experiments (tribology)

- Point-contact **tribometry** on **granite** vs **limestone**; **diamond** indenter/flat-on-rock **geometry**; **humid** and **water**-immersed **conditions** with **friction** vs **load** reporting.

### Force-field training (ReaxFF and VASP for calcite)

- **Parent / scope:** ReaxFF extension for **calcite**-related O/Ca/O interactions combined with pre-existing **quartz**/**water** subsets in the ReaxFF formalism, as cross-referenced in the article.
- **QM / DFT (VASP):** **PBE** **pseudopotentials** (**PAW**), planewave **cutoff** about **520 eV**, **spin**-polarized, **k**-mesh for **calcite** and **equations of state** training points.
- **Training set and optimization:** **Bulk** and **reaction**-relevant data for **calcite**; targeted **ReaxFF** reoptimization of key **off-diagonal** and **valence** terms, then **condensed-phase** (equation of state, heats) checks as described in the paper. **CMA-ES**-style/standard ReaxFF **optimization** is referenced in the *J. Phys. Chem. C* text.

## Findings

**Experiments vs composition:** In **humid**/**water**-rich **conditions**, **limestone**-bearing contacts show **higher** **friction** than **granite**-bearing ones despite the lower **hardness** ranking—**K**-family roughness/phase identity in the *main text* is part of the experimental **comparison** picture (see *JPC C* and figures).

**NEMD trends:** In **dry** NEMD, the **diamond**–**calcite**/**quartz** **trend** can differ from the **humid** **experiment** ordering; with **interfacial water** in the simulation, **diamond**–**calcite** can recover **higher** **friction** than **diamond**–**quartz**, which the paper ties to more **persistent** interfacial **bonds** in the **calcite** system (**C–O–Ca**-like and **H-bond** networks).

**Kinetics and scaling:** **Bond-formation** rates are reported as **exponential** in the effective **contact stress/pressure** with small **activation volumes**, and **time-averaged** **friction** can scale about **linearly** with the **interfacial bond count** under **steady** sliding. At **>~2 GPa** contact **pressure** (both **MD** and **experiments** with water), the **friction**–**load** curve shows **superlinear** growth that the paper associates with a **bonding**-mediated **friction** regime. **Caveat:** the corpus `pdf_path` is a **galley**-style PDF; verify figure/page alignment against a **version-of-record** copy for citation-grade numbers (see **## Limitations**).

## Limitations

The corpus PDF is a galley proof (header shows placeholder page/volume in places). Simulation sliding speeds greatly exceed laboratory speeds; the rigid projectile-like tip model omits diamond wear chemistry.

## Relevance to group

A. C. T. van Duin and N. Dasgupta are co-authors; ReaxFF parameterization for calcite interfaces supports the tribology study.

## Citations and evidence anchors

## Related topics

- [[reaxff-family]]
