---
id: paper:2014zhou-physical-che-reaxff-reactive
type: paper
title: "ReaxFF reactive molecular dynamics on silicon pentaerythritol tetranitrate crystal validates the mechanism for the colossal sensitivity"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - domain:reaxff-lineage
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nve-simulation
  - keyword:energetic-materials
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1039/C4CP03781B"
year: 2014
authors:
  - "Tingting Zhou"
  - "Lianchi Liu"
  - "William A. Goddard III"
  - "Sergey V. Zybin"
  - "Fenglei Huang"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "31a1d4ffd58a9c30c5b348473c29a4f868c4d6d59bfa726783e162efec8b24a4"
pdf_path: "papers/ReaxFF_others/TingTingZou_Goddard_PETN_SI_PCCP2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014zhou-physical-che-reaxff-reactive -->

## Summary

**Silicon pentaerythritol tetranitrate (Si-PETN)** is known experimentally for **extreme sensitivity**, motivating mechanistic hypotheses beyond those typical of **PETN** alone. This **PCCP** article extends **ReaxFF** for **Si–C–H–O–N** energetic chemistry using **QM** training data, then applies **LAMMPS** reactive MD to contrast **thermal decomposition** of solid **Si-PETN** versus **PETN** and interpret Si-PETN’s exceptional sensitivity. The narrative ties **bulk** simulations to a previously proposed **unimolecular** **carbon–silyl nitro-ester** rearrangement that creates **Si–O** linkages not available to PETN in the same way, arguing that **exothermic** Si–O formation can couple to early **NO\(_2\)** release under conditions where PETN follows more conventional pathways. The contrast illustrates how **heteroatom** chemistry reroutes **decomposition** within the same nitrate-ester motif class—supporting the paper’s conclusion that colossal sensitivity can follow a **low-barrier unimolecular** route rather than dominant **multi-body** initiation.

## Methods

**Force-field training (ReaxFF, Si–C–H–O–N).** The authors extend ReaxFF for silicon-containing nitrate-ester chemistry so bulk simulations use the same reactive manifold as prior single-molecule QM work on Si-PETN. The Electronic supplementary information bundled with `papers/ReaxFF_others/TingTingZou_Goddard_PETN_SI_PCCP2014.pdf` documents QM versus ReaxFF comparisons for Si–C, Si–O, and Si–N bond dissociations (Fig. S1), bending energies for Si–O–C, O–Si–C, C–Si–C, and Si–O–N angles (Fig. S2), bond-order cutoffs for fragment analysis (Table S1), and the parameter file `ESI-ffield.txt`.

**MD application (ReaxFF-RMD in LAMMPS).** Solid Si-PETN is modeled in a \(2\times2\times3\) supercell (**696 atoms**) after lattice optimization with **three-dimensional periodic boundary conditions (PBC)** on all axes. Equilibration uses **0.2 fs** timesteps with **Nose–Hoover** thermostat (**100 fs** damping) and **Parrinello–Rahman** barostat (**1000 fs** damping) to relax lattice parameters at **5 K** and **300 K** (as stated in the PCCP/SI text), targeting **atmospheric pressure** during those **NPT**-style lattice-relaxation segments. Thermal-decomposition studies heat each crystal rapidly in **NVT** from **300 K** to one of **1000, 1200, 1400, 1600, 1800, or 2000 K** (example cited: **300 K → 1600 K** in **0.1 ps**), then continue **NVT** sampling at the target temperature for **at least 20 ps** before analyzing chemistry. To probe how exothermic reactions feed back on temperature and kinetics, additional **microcanonical (NVE)** RMD runs are started at **1200, 1400, 1600, and 1800 K** and run for **at least 100 ps** with **0.1 fs** timesteps. PETN crystals are simulated under parallel protocols for direct comparison. **Pressure control:** **N/A —** the high-temperature **NVT/NVE** decomposition stages use fixed-volume cells without hydrostatic barostat control; mechanical **pressure**/stress evolves only as a consequence of shear-free heating and chemistry, whereas the earlier lattice equilibration employs a barostat targeting **1 atm** as quoted above.

**Static QM / DFT-only:** **N/A —** this publication’s new electronic-structure training data are referenced through the ReaxFF fitting and literature QM on Si-PETN; the PCCP/SI text should be consulted for any explicit DFT functional/basis details tied to those prior QM benchmarks.

**Electric field / replica sampling / shear-shock:** **N/A —** not used in the thermal RMD protocol described above.

## Findings

At lower simulated temperatures, Si-PETN decomposition begins with the Liu carbon–silyl nitro-ester rearrangement that forms Si–O linkages—steps the authors state are absent for PETN under the same low-temperature regimes. As chemistry progresses, they argue that exothermic Si–O formation promotes earlier NO\(_2\) release from N–O/C-type cleavage channels that do not appear for PETN at comparable conditions. At higher temperatures PETN reacts by conventional NO\(_2\) loss and HONO elimination, yet Si-PETN remains markedly more reactive in their comparison. The bulk RMD results are presented as validating prior single-molecule QM arguments that Si-PETN’s extreme sensitivity follows a low-barrier unimolecular pathway rather than requiring dominant multi-body collision initiation. The PETN–Si-PETN contrast highlights how replacing the central C with Si reroutes early NO\(_x\) chemistry while preserving the overall nitrate-ester motif class. Reactive force fields inherit QM-training approximations; finite cells, rapid heating ramps, and nanosecond-scale sampling influence quantitative branching and timing, so barrier heights and product distributions should be read as model-dependent relative trends unless cross-checked against additional experiments or higher-level theory.

## Limitations

Reactive FF energetics for **energetic materials** require ongoing validation; simulation **heating rates** and **finite-size** effects can influence branching ratios.

## Relevance to group

**Energetic materials** **ReaxFF** reference from the **Goddard/Zybin** line, adjacent to **EM** initiation and **shock** chemistry topics in the corpus.

## Citations and evidence anchors

- DOI: [10.1039/C4CP03781B](https://doi.org/10.1039/C4CP03781B)

## Related topics

- [[reaxff-family]]
