---
id: paper:2016bal-2016-chemsci-doi-venue-direct-observation
type: paper
title: "Direct observation of realistic-temperature fuel combustion mechanisms in atomistic simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - method:reaxff
  - method:enhanced-sampling
  - domain:organics-polymers-pyrolysis
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:enhanced-sampling
  - keyword:reactive-md
candidate_tags:
  - "duplicate-ingest-see-2016bal-chemical-sci-direct-observation"
source_refs: []
doi: "10.1039/C6SC00498A"
year: 2016
authors:
  - "Kristof M. Bal"
  - "Erik C. Neyts"
venue: "Chem. Sci."
pdf_sha256: "87df50386504fa357c5c4d41e74641e8656a29fafb83301bedc4c23c42852429"
pdf_path: "papers/ReaxFF_others/Bal-2016-ChemSci-DOIversion.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016bal-2016-chemsci-doi-venue-direct-observation -->

## Summary

Atomistic simulation can in principle enumerate mechanisms, intermediates, and products of complex reacting flows without embedding a fixed reaction network, but conventional molecular dynamics is limited to nanoseconds, which has forced prior reactive simulations of fuel chemistry to use very high temperatures that poorly represent many practical low-temperature regimes. Bal and Neyts apply **collective-variable-driven hyperdynamics (CVHD)**—a self-learning scheme that grows a bias on bond-distortion collective variables—together with **ReaxFF** (Chenoweth *et al.* parameter set with **QEq** charges in **LAMMPS**). Their headline result is that **CVHD + ReaxFF** reaches **effective physical times** far beyond brute-force MD: **n-dodecane pyrolysis** is observed down to **1000 K** (up to **~57 ms** effective time in their Table 1 example), while **fuel-lean oxidation** of **n-dodecane** is pushed down to **700 K** with an **effective time up to ~39 s** and a very large boost factor. Product compositions and dominant pathways are reported to be **strongly temperature-dependent** and **consistent with experiments and kinetic models** in the comparisons they present.

## Methods

### MD application (atomistic dynamics)

Bal and Neyts implement **CVHD** in **LAMMPS** with the **colvars** module, using **ReaxFF** with the **Chenoweth *et al.*** hydrocarbon parameter set and **QEq** charge equilibration as distributed in **LAMMPS**. The equations of motion use **Δt = 0.1 fs**. Initial thermalization uses a **Langevin-type thermostat**, followed by **NVT** sampling with a **Nosé–Hoover chain** (**0.1 ps** relaxation time quoted in the article) and, where isotropic **NPT** is required, **Martyna–Tobias–Klein barostat** dynamics integrated with the **Tuckerman *et al.*** scheme (**1 ps** relaxation time quoted).

**System size & composition (approx. atom counts from stoichiometry):** **Pyrolysis:** **24** n-dodecane molecules (**912 atoms**) in a **50 × 50 × 50 Å³** **three-dimensional periodic** box (**~0.05 g cm⁻³**). **CVHD** biases **C–C** and **C–H** bond strains with **r_min/r_max** windows (**1.55–2.20 Å** for C–C; **1.05–1.65 Å** for C–H) chosen so high-barrier bond-breaking transition states remain unbiased. **Gaussian hills** (**w = 0.25 kcal mol⁻¹**, **d = 0.025**) are deposited every **0.2 ps**; the transition detector uses a waiting time **t_w = 1 ps**. **CVHD** pyrolysis runs span **1000–1800 K**; **unbiased** comparison MD is reported at **2500 K**.

**Lean combustion cells:** **5 n-dodecane + 100 O₂** (**390 atoms** as counted from the explicit molecular formula in the article) in a **40 × 40 × 40 Å³** **periodic** box (**~0.1 g cm⁻³**), with **oxygen** interactions mapped to the **same CV strain parameters as carbon** (as stated in the article). **CVHD** oxidation runs span **700–1800 K** at the reported high densities; average pressures rise from **~200 bar** at **700 K** to **~500 bar** at **1800 K** in their constant-volume oxidation setup. Additional **constant-pressure** **CVHD** sets at **1000 K** (**10–500 bar**) use a **longer Gaussian deposition stride (0.5 ps)** in **NPT** to limit bias buildup when collision frequency drops.

**Electric field:** **N/A — not used.** **Replica / parallel tempering / umbrella sampling:** **N/A —** acceleration is **CVHD**, not replica exchange or umbrella sampling.

### Force-field training

**N/A — not a ReaxFF refit paper**; the work applies an established **ReaxFF** description for hydrocarbon chemistry together with **CVHD**.

### Static QM / DFT

**N/A — not a DFT production study** for the reported accelerated trajectories; higher-level QM enters as literature context on reactive potential accuracy.

## Findings

- **Accessible timescales:** Table 1 in the article summarizes the **lowest temperatures** reached for **pyrolysis** (**1000 K**, **~57 ms** longest effective time, large boost) versus **combustion** (**700 K**, **~39 s** longest effective time, **~1.3×10⁹** boost vs prior long **ParRep** alkane work they cite). The abstract’s “**700 K**” headline refers primarily to the **oxidation** demonstration; **pyrolysis** at **1000 K** still constitutes a large departure from prior **>2000 K** brute-force reactive MD practice.
- **Pyrolysis chemistry trends:** At **high T**, **β-scission**-like channels dominate (**C₂**-rich products, similar to prior **>2000 K** MD). At **lower T**, **low-barrier isomerizations** occur more often, producing **more stable secondary radicals** and, after eventual **β-scission**, **heavier 1-alkene** products (**C₃+** fractions much larger at **1000 K** than at **2500 K** in their Fig. 2 narrative). **Propagation** by **H/CH₃/C₂H₅** abstraction becomes more central at lower temperatures, while **unimolecular C–C fission** gains weight at high temperature.
- **Oxidation mechanism regimes:** The authors contrast **low-T** oxidation initiated by **O₂ hydrogen abstraction** and downstream **peroxy / hydroperoxyalkyl (•QOOH)** radical chemistry with a **high-T** regime where chemistry begins like **pyrolysis** (**C–C fission** / **β-scission**, **C₂H₄** formation) followed by later oxidation—plus **intermediate-T** mixed behavior they discuss with pathway figures.
- **Validation stance:** They report **qualitative consistency** with **experimental** product trends and **kinetic-model** expectations for the staged comparisons they show, while emphasizing **CVHD** design choices (stride vs pressure, collective variables) that must be validated when porting the method to other gas-phase reactive systems.

## Limitations

Second corpus PDF (`2016bal-chemical-sci-direct-observation`) duplicates the article with a different file hash; cite one consistent PDF for pagination. Acceleration artifacts and bias potential design choices must be validated case by case; CVHD parameters are not universal.

## Relevance to group

Demonstrates accelerated reactive MD with ReaxFF for combustion-relevant chemistry—adjacent to group interests in reactive hydrocarbon systems.

## Citations and evidence anchors

- DOI: [10.1039/C6SC00498A](https://doi.org/10.1039/C6SC00498A)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
