---
id: paper:2018chen-nat-hydroxide-diffuses
type: paper
title: "Hydroxide diffuses slower than hydronium in water because its solvated structure inhibits correlated proton transfer"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:aimd
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:aimd
  - keyword:water-interfaces
  - keyword:dft-static
  - keyword:nose-hoover
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1038/s41557-018-0010-2"
year: 2018
authors:
  - "Mohan Chen"
  - "Lixin Zheng"
  - "Biswajit Santra"
  - "Hsin-Yu Ko"
  - "Robert A. DiStasio Jr"
  - "Michael L. Klein"
  - "Roberto Car"
  - "Xifan Wu"
venue: "Nature Chemistry (2018)"
pdf_sha256: "ee34f3e5ab5f362656ccfabb4f74678fda5fd2af41337abbd3572115f97e4d26"
pdf_path: "papers/Others/Nature-chem-OH-H-diffusion-2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018chen-nat-hydroxide-diffuses -->

## Summary

**Ab initio molecular dynamics** at **hybrid DFT** quality with **van der Waals (Tkatchenko–Scheffler)** and **self-interaction** corrections compares **hydronium** vs **hydroxide** structural diffusion in **bulk water**, focusing on **temporal correlations** of **proton transfers** and the **solvation** motifs that gate **OH⁻** mobility. The study addresses why **OH⁻** and **H₃O⁺** can show different macroscopic transport signatures even though both participate in **Grotthuss-style** shuttling: the analysis emphasizes **when** successive transfers occur together versus independently, not only average hopping rates.

## Methods

From the Nature Chemistry article PDF (`pdf_path`); values follow the **Methods** section there. The authors compare multiple **DFT** flavors (**PBE**, **PBE-TS**, **PBE0-TS**) to separate **dispersion** and **hybrid** effects on solvation structure and dynamics.

- **DFT / AIMD code:** **Quantum ESPRESSO**; exact exchange for **PBE0** via **Wannier**-based formulation; **Tkatchenko-Scheffler (TS)** vdW treated self-consistently (**PBE0-TS**). **Plane-wave cutoff 72 Ry**; **Troullier-Martins** norm-conserving pseudopotentials; **gamma-only** Brillouin sampling.
- **Cells:** Pure water **128 H2O**, cubic edge **15.7 A**; **H3O+(aq)** (**63 H2O** + one excess proton: **127 H**, **63 O**), edge **12.4 A**; **OH-(aq)** (**63 H2O** + **OH-**: **127 H**, **64 O**), edge **12.4 A** (targets ambient liquid density as stated). **Periodic boundary conditions** on cubic supercells for each composition.
- **Car-Parrinello MD:** Fictitious electronic mass **150 a.u.**; electronic mass preconditioning cutoff **6 Ry**; **NVT** at **330 K**; **Nose-Hoover chain** thermostats (**one chain per atom**, **four** thermostats per chain). **Timestep 3.5 a.u. (~0.08 fs)**. **Hydrogen** masses set to **deuterium (2.0135 amu)** for sampling; **oxygen 15.9995 amu**. Trajectory lengths: **H3O+** **28 / 45 / 32 ps** (**PBE / PBE-TS / PBE0-TS**); **OH-** **54 / 55 / 38 ps**; bulk water **14 / 14 / 25 ps** (**PBE / PBE-TS / PBE0-TS**). **H-bond** definition: **O-O < 3.5 A**, **H-O-O angle < 30 deg**; **O-H** covalent cutoff **1.24 A**.
- **Barostat / pressure:** **N/A —** fixed-volume **NVT** **Car–Parrinello** trajectories without **NPT** **barostat** coupling to a **pressure** target.

## Findings

- **Mechanism / outcomes:** **Hydronium** diffusion remains associated with **correlated**, relatively **frequent** **Grotthuss** hopping among **Eigen-** and **Zundel**-like motifs, whereas **hydroxide** shows **less temporally correlated** transfers gated by a **hypercoordinated** solvation shell (**Nature Chemistry** **Results**).
- **Comparisons:** The study **compares** **PBE**, **PBE-TS**, and **PBE0-TS** **DFT** flavors to isolate **dispersion** and **hybrid** effects on both structure and dynamics, relating trends to **experimentally** inferred **OH⁻** versus **H₃O⁺** transport asymmetry.
- **Sensitivity:** **Functional** choice shifts solvation motifs and hopping **kinetics**; **330 K** **NVT** sampling and heavy-hydrogen masses modify absolute **diffusion** numbers relative to **298 K** laboratory **NMR**.
- **Limitations / outlook:** **AIMD** cost limits **system size** and trajectory length; the **Discussion** cites literature on **nuclear quantum** effects that are not the headline correction here.
- **Corpus honesty:** Numerical settings mirror the **Methods** section of the **PDF** at `pdf_path`; confirm **Ry** cutoffs and thermostat chain depth if reproducing with newer **Quantum ESPRESSO** builds.

## Limitations

- **AIMD** cost limits **system size** and **sampling** depth; nuclear **quantum** effects are discussed in the literature cited by the paper but are not the central headline here.

## Related topics

- [[2018dengpan-dong-j-phys-chem-grotthuss-versus]]
- [[theme-water-silica-geo]]
