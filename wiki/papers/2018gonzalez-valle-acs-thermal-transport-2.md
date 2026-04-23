---
id: paper:2018gonzalez-valle-acs-thermal-transport-2
type: paper
title: "Thermal Transport across SiC–Water Interfaces"
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
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.8b10307"
year: 2018
authors:
  - "C. Ulises Gonzalez-Valle"
  - "Satish Kumar"
  - "Bladimir Ramos-Alvarado"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "5fd46a416419aaa216d62ec0a605629700bb6253a21ea65c0a72548dbec3620e"
pdf_path: "papers/Others/Gonzalez_Valle_water_SiC_acsami.8b10307.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018gonzalez-valle-acs-thermal-transport-2 -->

## Summary

Nonequilibrium classical molecular dynamics (NEMD) was used to study thermal transport across interfaces between 3C–SiC and water, including crystallographic plane, surface termination (C vs Si), and hydrophilic versus hydrophobic solid–liquid coupling tuned via Lennard-Jones cross-terms. The work relates thermal boundary conductance (TBC) to interfacial liquid structuring and reconciles anisotropic TBC behavior across terminations using the density depletion length as a descriptor.

## Methods

- **Engine and ensemble:** Simulations used **LAMMPS** with a staged protocol: energy minimization; **NVT** equilibration at 300 K for 1 ns (Nosé–Hoover thermostat, 100 fs time constant); **NVE** for 1 ns to check stability; then imposed heat addition/removal in 1.5 nm-thick slabs for 5 ns; production sampling of kinetic energy and coordinates every 10 ps over 7.5 ns. **Time step 1 fs** (SHAKE on rigid water).
- **Water model:** **SPC/E**; long-range electrostatics via **PPPM** (accuracy \(10^{-6}\)); rigid water enforced with **SHAKE**.
- **SiC:** **MEAM** potential for the solid; bulk SiC thermal conductivity estimated by extrapolation from finite slabs (reported ~368 W/m·K, ~5% above experiment), supporting use of the parametrization for the present analysis.
- **Solid–liquid coupling:** 12–6 **Lennard-Jones** Si–O and C–O only; **ε**\(_{Si–O}\) varied to span wetting while **σ**\(_{Si–O}\) = 2.63 Å and C–O parameters fixed (e.g. **σ**\(_{C–O}\) = 3.19 Å, **ε**\(_{C–O}\) = 0.005 eV, 13 Å cutoff) to match reference wetting behavior.
- **Geometry:** Two SiC slabs with water between; **(100)** and **(111)** orientations; periodic in **x,y**; fixed outer layers in **z**; slab dimensions ~10 nm length, transverse areas ~2.62×2.62 nm\(^2\) (100) and ~2.78×2.67 nm\(^2\) (111); ~6 nm water gap; **~1000–1100** molecules to keep bulk pressure consistent across wetting states.
- **TBC:** Imposed heat flux 5–15 nW; **TBC** \(G\) from **J = G ΔT\(_\mathrm{int}\)** using linear response of temperature profiles; interface **ΔT** from extrapolation of liquid and solid temperature profiles.

## Findings

- **Interface**-level **TBC** depends on **plane, termination, and wetting**, but **does not universally track wettability** alone; **interfacial liquid structuring** (layering, high-density zones) must be considered alongside bonding strength.
- **Density depletion length** reconciles anisotropic TBC and termination-dependent behavior; the **TBC–depletion scaling differs between Si and SiC**, so a single universal TBC–depletion fit across materials is not supported.
- For pristine planes, **G ∼ 1 + cos(θ)**-type scaling can hold **per atomic plane**, with **anisotropic** heat transfer between planes; **icelike** or ordered water regions can enhance TBC when present.
- **Mechanisms and comparisons:** **Interfacial** **heat** flow is dissected relative to **liquid layering** and **wetting** strength; bulk **MEAM** SiC thermal conductivity is checked against **experiment** (~5% deviation noted in **Methods**) as a sanity check before interpreting **interface** **TBC**.
- **Sensitivity and outlook:** **TBC** shifts with **ε**\(_{Si–O}\) wetting scans, **termination**, and **plane**; authors discuss how **contact-angle**-like metrics alone mis-rank interfaces. **Limitations** of classical **MEAM + SPC/E + LJ** coupling are summarized under **Limitations** below. Numbers and figures should be verified in the **ACS Appl. Mater. Interfaces** **PDF** (`pdf_path`).

## Limitations

Empirical **MEAM + SPC/E + LJ** coupling limits transferability to reactive or charged interfaces; NEMD flux and finite-size choices affect extracted **G** and profiles.

## Relevance to group

Classical **solid–liquid thermal transport** workflow comparable in spirit to interface studies in reactive systems; no ReaxFF parameterization in this paper.

## Citations and evidence anchors

- DOI: `10.1021/acsami.8b10307` (ACS Appl. Mater. Interfaces).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
