---
id: paper:2018gonzalez-valle-nat-spectral-mapping
type: paper
title: "Spectral mapping of thermal transport across SiC-water interfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - task:application
  - material:widegap-semiconductor
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nve-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.ijheatmasstransfer.2018.11.101"
year: 2018
authors:
  - "C. Ulises Gonzalez-Valle"
  - "Bladimir Ramos-Alvarado"
venue: "Int. J. Heat Mass Transfer"
pdf_sha256: "4f747427c69eb3ce0ad694a18a5d415eb79fc2b8cb5d7c48d07996bab3e62d3a"
pdf_path: "papers/Others/21. Spectral mapping of thermal transport across SiC-water interfaces.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018gonzalez-valle-nat-spectral-mapping -->

## Summary

NEMD simulations of 3C–SiC–water interfaces are combined with **spectral mapping**: interfacial heat flux is decomposed using a **spectral heat flux** built from solid–liquid force–velocity correlations, and **phonon density of states (DOS)** from velocity autocorrelations for interface vs bulk regions. The analysis ties mode-resolved contributions to TBC, crystallographic plane, termination, and wetting.

Motivation in the article is that **thermal boundary conductance** at semiconductor–water interfaces controls heat removal in power electronics and related technologies, yet macroscopic **TBC** metrics alone obscure which phonon polarizations and frequencies carry heat across chemically distinct terminations and wetting states.

## Methods

- **MD setup:** **SPC/E** water; **SHAKE**; **PPPM** electrostatics; **MEAM** for SiC; **LJ** Si–O and C–O cross-interactions with **ε**\(_{Si–O}\) varied by plane and wetting (**σ**\(_{Si–O}\) fixed at 2.63 Å; C–O parameters as in the companion ACS study).
- **NEMD:** Two SiC slabs, ~**10 nm** slab length, transverse areas **2.62×2.62** nm\(^2\) (100) and **2.78×2.67** nm\(^2\) (111); **6 nm** water; periodic **x,y**; fixed outer **z** layers; **1.5 nm** heat add/remove regions; **LAMMPS** + **VMD** visualization.
- **Protocol:** Minimization; **NVT** 300 K for **1 ns** (**Nosé–Hoover thermostat**, **0.1 ps** damping time constant); **NVE** **1 ns**; **5 ns** heating; production **5 ns** with KE, coordinates, and velocities sampled every **25 ps** (spectral post-processing uses stored forces/velocities at that cadence; see article for the integration **timestep** in **fs**).
- **Pressure / barostat:** **N/A — NEMD** applies fixed heat flux in slab regions rather than a global **NPT** target; bulk liquid is not barostatted to a stated **GPa** value in the protocol summarized here (constant-volume segments only).
- **Spectral mapping:** **Spectral heat flux** \(q(\omega)\) from real part of Fourier transform of **F**\(_{ij}\)·**v**\(_i\) correlations (solid→liquid forces); **DOS** \(\propto\) FT of **VACF** for interface (**~3 Å** interfacial slice) vs bulk solid atoms; DOS overlap related to TBC and liquid structure.
- **Pressure:** **NEMD** cells are treated at effectively **constant volume** in the summarized protocol; **N/A — NPT barostat** / **N/A — imposed hydrostatic pressure** targets beyond maintaining bulk-like water density between slabs.

## Findings

- **DOS at the interface** shifts with **termination**, **plane**, and **wetting**; **low-frequency** modes dominate TBC for **C- and Si-terminated (100)** and **C-terminated (111)**; **Si-terminated (111)** shows more **high-frequency** contribution.
- **Out-of-plane** modes contribute strongly to interfacial heat flux; **in-plane** flux composition is smaller, especially on **(111)**, linked to **bonding strength** and **liquid layering**.
- **TBC vs DOS overlap** aligns with **interfacial liquid structure**; **interfacial bonding strength alone** does not fully predict thermal transport across the studied SiC–water interfaces.
- **Mechanisms / comparisons / sensitivity / limitations / PDF:** Mode-resolved **heat** flux **mechanisms** are **compared** to macroscopic **TBC** from the same **NEMD** setups, showing how **phonon** **frequency** content shifts with **wetting** and **termination**. Sampling (**25 ps**) and classical **potentials** are **limitations** for quantitative **experiment** matching; see discussion in the **Int. J. Heat Mass Transfer** **PDF** (`pdf_path`).

## Limitations

Spectral analysis depends on **force decomposition**, sampling interval (**25 ps**), and classical potentials; results are for **non-reactive** SiC–water models.

## Relevance to group

Complements **[[2018gonzalez-valle-acs-thermal-transport-2]]** with **mode-resolved** analysis of the same physical system class.

## Citations and evidence anchors

- DOI: `10.1016/j.ijheatmasstransfer.2018.11.101`.

## Related topics

- [[2018gonzalez-valle-acs-thermal-transport-2]]
- [[reaxff-family]]
