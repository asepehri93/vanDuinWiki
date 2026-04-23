---
id: paper:2018sang-nat-situ-atomistic
type: paper
title: In situ atomistic insight into the growth mechanisms of single layer 2D transition
  metal carbides
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:2d-layered
- domain:reactive-md
- method:reaxff
- method:dft-static
- task:experiment-integrated
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:2d-materials
- keyword:validation-experiment
- keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: 10.1038/s41467-018-04610-0
year: 2018
authors:
- Xiahan Sang
- Yu Xie
- Dundar E. Yilmaz
- Roghayyeh Lotfi
- Mohamed Alhabeb
- Alireza Ostadhossein
- Babak Anasori
- Weiwei Sun
- Xufan Li
- Kai Xiao
- Paul R.C. Kent
- Adri C.T. van Duin
- Yury Gogotsi
- Raymond R. Unocic
venue: Nature Communications
pdf_sha256: 3f65c75b57624527e94efb122fc49e6f1fde73d6c2a060c94c498bd2d549c53b
pdf_path: papers/Sang_Nature_Comm_MXene_defect_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018sang-nat-situ-atomistic -->

## Summary

Bottom-up growth of atomically thin transition metal carbides is motivated by applications from electronics to energy storage, yet experimental single-layer carbide synthesis on well-defined substrates had been scarce compared with theory. This Nature Communications work uses in situ aberration-corrected scanning transmission electron microscopy (STEM) to show homoepitaxial Frank–van der Merwe growth of hexagonal TiC single adlayers on defunctionalized Ti₃C₂ MXene. Thermal exposure combined with electron-beam irradiation activates growth near 500 °C, while purely thermal runs reach comparable chemistry near 1000 °C. The substrate itself supplies Ti and C adatoms that migrate onto hexagonal Ti planes of monolayer Ti₃C₂, producing compositions described in the paper as Ti₄C₃- and Ti₅C₄-like two-dimensional products. Electron energy loss spectroscopy (EELS) resolves elevated carbon signal in triangular adlayer islands relative to the matrix, favoring a hexagonal TiC adlayer over a pure Ti adlayer, and density functional theory (DFT) plus ReaxFF-based hybrid force-biased Monte Carlo and molecular dynamics (fbMC/MD) connect those observations to surface energies, diffusion barriers, and step costs.

## Methods
**1 — In situ microscopy (experiment).** **Nion UltraSTEM 100** at **~10⁻⁹ Torr** with a **Protochips Fusion** heater; **monolayer Ti₃C₂Tₓ** is **defunctionalized** above **~500 °C** for imaging/EELS of **triangular adlayers**; supplemental movies capture **beam-assisted** dynamics.

**2 — Static QM (DFT).** **VASP** **PBE-GGA** with **500 eV** cutoff and **k-meshes** per slab calculations (see article for **k** sampling); used for **formation energies**, **diffusion barriers**, and **step** penalties contrasting **h-TiC** adlayers vs **Ti** clustering.

**3 — MD application (ReaxFF fbMC/MD).** **Hybrid force-bias Monte Carlo / molecular dynamics (fbMC/MD)** with **ReaxFF** explores **bond-making/breaking** during **adlayer** evolution where rare events matter. **PBC:** **three-dimensional PBC** **Ti–C–O/H** slab supercells containing **hundreds to thousands of atoms** (exact counts in **SI**). **Ensemble / temperature:** **fbMC/MD** trajectories are reported as **NVT**-style reactive runs at **1500 K** and **2500 K** in the main-text figure discussion, with any **NPT** prerelaxation of slabs deferred to **SI** tables. **Duration:** trajectory segments are analyzed on **picosecond** timescales in the figure captions accompanying those **fbMC/MD** panels (see *Nat. Commun.* for exact **ps** totals). **Timestep / thermostat / barostat / pressure:** remaining integrator controls are specified in **SI**—this wiki does not transcribe every **LAMMPS** keyword. **Electric fields:** **N/A —** not applied in the reactive simulations beyond implicit **electron-beam** chemistry being separate from the **fbMC/MD** model.

**4 — Force-field training.** **N/A —** uses published **ReaxFF** for **Ti–C–O/H** environments.

**5 — Reactive MD generic note:** **fbMC** constitutes **Monte Carlo** acceleration coupled to **MD**.

## Findings
**Outcomes / mechanisms:** **STEM/EELS** at **~500 °C** (and hotter purely thermal routes near **~1000 °C** in the narrative) supports **homoepitaxial** growth of **hexagonal TiC**-like adlayers on **defunctionalized Ti₃C₂**, with **carbon-rich** triangles rather than **pure Ti** clusters. **DFT** shows **h-TiC** adlayers are strongly bound while **bare Ti** adatoms would **3D**-cluster without carbon. **fbMC/MD** illustrates kinetically accessible **growth** sequences consistent with those energetics.

**Comparisons:** **in situ** data are compared against **DFT** + **fbMC/MD** pathways.

**Sensitivity:** **temperature** and **electron-beam** dose couple strongly in experiment, whereas simulations separate **thermal** reactive pathways.

**Limitations:** **beam effects** complicate direct mapping to purely thermal **MD**; **ReaxFF** kinetics remain approximate.

**Corpus honesty:** **VASP** settings and **fbMC/MD** details should be checked in **`papers/Sang_Nature_Comm_MXene_defect_2018.pdf`** + **SI**; this summary mirrors main-text statements only.

## Limitations

Electron-beam effects couple to thermal driving forces; reactive FF kinetics remain approximate versus experiment.

## Relevance to group

Multiple van Duin group contributors (Yilmaz, Lotfi, Ostadhossein, van Duin) co-author; integrates ReaxFF with in situ microscopy for MXene synthesis.

## Citations and evidence anchors

- DOI: [10.1038/s41467-018-04610-0](https://doi.org/10.1038/s41467-018-04610-0)

## Related topics

- [[reaxff-family]]
