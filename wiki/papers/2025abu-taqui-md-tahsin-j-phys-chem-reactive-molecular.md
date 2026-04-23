---
id: paper:2025abu-taqui-md-tahsin-j-phys-chem-reactive-molecular
type: paper
title: "Reactive molecular dynamics modeling of collision-induced dissociation of 1-ethyl-3-methylimidazolium tetrafluoroborate ionic liquid ions"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:nve-simulation
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.5c05157"
year: 2025
authors:
  - "Abu Taqui Md Tahsin"
  - "Stefan J. Bell"
  - "Elaine M. Petro"
venue: "J. Phys. Chem. A"
pdf_sha256: "e8eb8c6a729fd40a7ab1874e1411f8cfc06082a454b1d5d24156e991937d232d"
pdf_path: "papers/ReaxFF_others/Reactive Molecular Dynamics Modeling of Collision-Induced Dissociation of 1‑Ethyl-3-methylimidazolium Tetrafluoroborate Ionic Liquid Ions[97].pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2025abu-taqui-md-tahsin-j-phys-chem-reactive-molecular -->

## Summary

The paper models **collision-induced dissociation (CID)** of gas-phase ions of the ionic liquid **EMIM–BF\(_4\)** ([EMIM]\(^+\), [BF\(_4\)]\(^-\), and **2:1** and **1:2** clusters) colliding with **N\(_2\)** using **ReaxFF in LAMMPS**, spanning **10–100 eV** laboratory-frame collision energies. **B3LYP/6-31G** **GAMESS** calculations supply relaxed precursor structures and supplementary thermochemistry on selected pathways; **tandem mass spectrometry (MS/MS)** on an **electrospray** platform provides experimental product distributions for comparison.

## Methods

- **Quantum chemistry:** Geometries for precursor ions/clusters use **DFT B3LYP/6-31G** in **GAMESS**. **Cluster conformers** are explored with **CHARMM MD in LAMMPS** (annealing cycles) before returning minima to DFT. Selected pathways are evaluated for **ΔH\(_{0\,\mathrm{K}}\)** and **ΔG\(_{298\,\mathrm{K}}\)** to compare dissociation favorability.
- **Reactive MD:** **LAMMPS** **ReaxFF** parameters follow **Medina-Ramos et al.** with **EMIM–BF\(_4\)** refinements from **Tahsin & Petro**. Each collision starts from **300 K** **NVT** thermalization with **Nosé–Hoover** thermostats as implemented for canonical sampling, then switches to **NVE** while assigning an approach velocity for the target **lab-frame** collision energy (**10–100 eV** in **10 eV** steps). **Angular sampling** uses a grid of **y**-angles (**0–300°**, six values) and **z**-angles (**0–180°**, seven values). **Impact parameters** span **0–4 Å** relative to **N\(_2\)**. Nonbonded **N\(_2\)–ion** interactions use a **4 Å** cutoff. Each trajectory uses a **0.1 fs** timestep and **2 ps** total integration time.
- **Experiments:** **SCIEX ZenoTOF 7600** **MS2** on **~100 μM** EMIM–BF\(_4\) in methanol infusion, **N\(_2\)** collision gas, **0–100 eV** collision energy in **10 eV** steps (positive and negative modes).

**MD application (head-on collisions):** Isolated **ion** + **N\(_2\)** pairs in a gas-phase **molecular dynamics** cell; **N/A** — full **3D PBC** **periodic** **supercell** for a condensed solid (**non-periodic** / minimal box in **LAMMPS**-style **collision** setups, per article); after **300 K** **NVT** with **Nose-Hoover thermostat**, **NVE** **microcanonical** **production** for **2 ps** at **0.1 fs** **timestep**; **N/A — barostat**; **N/A** — hydrostatic **pressure** coupling; **N/A — electric field**; **N/A — metadynamics**; **N/A** — **umbrella** bias.
## Findings

- MD predicts **[EMIM]\(^+\)** **onset** near **~20 eV** (lab frame) and **[BF\(_4\)]\(^-\)** remains intact below **~40 eV**, with **[BF\(_4\)]\(^-\)** fragmenting to **[F]\(^-\)** + **BF\(_3\)** and **[BF\(_2\)]\(^+\)** at higher energies (**≥60 eV** features discussed), including **reaction** **pathways** the authors highlight.
- **[EMIM]\(^+\)** fragmentation is dominated by **3-methylimidazolium** at lower **collision** **energies**; **cyanide** becomes prominent at **higher** **eV**; **2:1** and **1:2** clusters fragment at **10 eV**, showing **sensitivity** to **cluster** **concentration**-like stoichiometry. **Outcomes** are **compared** to **electrospray** **MS2** **experiments** with **agreement** described in the main text, although **internal energy** distributions in **experiment** limit exact matching (**limitation** noted in the article).
- **Simulated** spectra align **versus** the **ZenoTOF** **measurements**; **caveat**—**short** (2 **ps**) gas-phase **trajectories** miss slow rearrangements. **Version-of-record** **PDF** governs all **quantities**; this page is a **curated** **extract**-aligned summary.
## Limitations

- **Short (2 ps)** gas-phase trajectories and a **specific ReaxFF fit** may miss slow rearrangements or electronic effects important at some energies.
- **Electrospray** experiments probe **soft ionized** ensembles; high-energy **CID** modeling omits **solvent** and **internal energy distributions** of the experimental ion population beyond the stated protocol.

## Relevance to group

Demonstrates **benchmarked ReaxFF CID** workflows for **ionic-liquid ions** in **LAMMPS**, relevant to **mass-spectrometry** and **low-pressure plasma** fragmentation contexts.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.5c05157](https://doi.org/10.1021/acs.jpca.5c05157)

## Related topics

- [[reaxff-family]]
