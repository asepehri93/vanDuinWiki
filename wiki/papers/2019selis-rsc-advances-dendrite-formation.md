---
id: paper:2019selis-rsc-advances-dendrite-formation
type: paper
title: "Dendrite formation in Li-metal anodes: an atomistic molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reactive-md
  - method:classical-md
  - method:reaxff
  - task:application
  - material:li-metal-anode
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:eam-potential
  - keyword:reaxff-application
  - keyword:batteries-interfaces
source_refs: []
doi: "10.1039/C9RA05067A"
year: 2019
authors:
  - "Luis A. Selis"
  - "Jorge M. Seminario"
venue: "RSC Advances (2019), 9, 27835-27848"
pdf_sha256: "710984a5001fdeaa4b3e3418dc998d6de2c76006003b4637d2d6287a60684b88"
pdf_path: "papers/ReaxFF_others/Selis_Seminario_RSC_Advances_2019_dendrite.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019selis-rsc-advances-dendrite-formation -->

## Summary

**Hybrid MD** of a **model nanobattery** examines **Li dendrite** growth at a **Li metal anode** covered by a **cracked LiF SEI** against **1 M LiPF₆ in ethylene carbonate** electrolyte in **LAMMPS**. **2NN MEAM** treats **Li⁰ / Li⁺** (short-range) interactions; **LiF** uses a **Born–Mayer** form; **EC / PF₆⁻ / ions** bond-order chemistry uses an **updated ReaxFF** parametrization (**Mahbubul et al.**); **nonbonded** **electrolyte–electrode** couplings use **Lennard-Jones + Coulomb** (tables in the article). **NPT** lithiation with three charging protocols at **325 K** and **410.7 K**. The **RSC Advances** study is positioned as a **mechanistic** **cartoon** for how **SEI** **defects** **focus** **Li** **deposition** **flux** at **atomistic** **resolution**.

## Methods

**Engine and ensemble.** **LAMMPS**; **NPT** for equilibration and lithiation; initial box **40.8 × 54.0 × 40.8 Å³** with **640 LiF** formula units, **936 Li** metal atoms, **424 EC** molecules, **28 LiPF₆** ion pairs; **pseudo-atom** cathode reservoir to supply **Li⁺** with prescribed charging modes.

**Force fields.** **2NN MEAM** for **Li metal** and **Li⁺** within **2.5 Å** of metal (partitioning as in the article’s **Force fields** section); **Born–Mayer** for **LiF**; **ReaxFF** (Mahbubul et al. update) for **bonded** **electrolyte** species; **LJ + Coulomb** for **nonbonded** cross-terms between **solvent/SEI/metal** subsystems (**Tables 2–3**).

**Charging protocols.** (1) **~1 Li⁺ / 0.4 ps** constant-current-like insertion; (2) **pulse train** **10 Li⁺ / 4 ps**; (3) **exchange** protocol maintaining constant electrolyte Li⁺ count.

**Parameter** **files**, **cutoffs**, and **neighbor** **skin** settings for the **MEAM**/**ReaxFF**/**LJ** partitioning appear in `papers/ReaxFF_others/Selis_Seminario_RSC_Advances_2019_dendrite.pdf` alongside **Movies**/**figure** captions describing **dendrite** **morphology** **metrics**.

**Grid / boundary / timestep / thermostat (consolidated).** **3D** **PBC** **nanocell** **(40.8** **×** **54.0** **×** **40.8** **Å³** as **above**); **timestep** and **Nose**-**Hoover** (or **other** **thermostat**) **details** in **RSC** **Advances** **full** **text** / **SI**; **N/A** to **re**-**list** here if **not** in the **local** **excerpt**. **Lithiation** **NPT** **runs** at 325 K and 410.7 K in the **abstract**-level **summary**; **Hydrostatic** **pressure** in **NPT** **(bar)** **/ stress** as in **RSC** **text**; **temperature** **thermostat** setpoints follow these **K** **targets**. **Shear, shock, applied** **E**-**field, umbrella** **sampling:** **N/A** unless the **SI** **states** them.

**2 — Force-field training.** **N/A** as a **new** **ReaxFF** **fit**—the study **uses** a **published** **ReaxFF** **electrolyte** **update** ( **Mahbubul** **et** **al.** ) **with** **MEAM**-**class** **Li** **metal** and **LiF** **SEI** **forms** as **partitioned** in the **article** **force**-**field** **section** and **tables** (see **RSC** **Advances** **PDF**).
## Findings

The **SEI crack** **does not block lithiation** but **focuses and promotes** dendrite growth versus a crack-free case. Dendrite formation is **more favorable at 325 K than at 410.7 K** under the explored conditions. **Higher C-rate** (**2.2C** vs **1.6C** in the reported comparison) **favors** dendrites, implying **lower-rate** operation can be **safer** for energy storage in this model.

The **authors** relate **temperature** and **rate** **trends** to **local** **Li** **supersaturation** near the **crack** **mouth** as **Li⁺** **flux** is **channeled** through the **gap**.

## Limitations

Idealized **nanoscale** cell, fixed **SEI chemistry** (**LiF** only), and **classical** potentials omit **electron transfer** and detailed **electrolyte decomposition**.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

**Atomistic battery-interface** morphology study using **LAMMPS** with **MEAM + ReaxFF + ionic** potentials; useful **hybrid FF** reference for **Li dendrites**.

## Citations and evidence anchors

DOI: [10.1039/C9RA05067A](https://doi.org/10.1039/C9RA05067A)

## Related topics

- [[batteries-interfaces-reaxff]]
