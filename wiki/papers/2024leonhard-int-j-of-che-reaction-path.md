---
id: paper:2024leonhard-int-j-of-che-reaction-path
type: paper
title: "Reaction path identification and validation from molecular dynamics simulations of hydrocarbon pyrolysis"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - method:reaxff
  - method:dft-static
  - task:validation
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:reactive-md
  - keyword:lammps
  - keyword:neb
  - keyword:dft-static
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: "10.1002/kin.21719"
year: 2024
authors:
  - "Felix Schmalz"
  - "Wassja A. Kopp"
  - "Eirini Goudeli"
  - "Kai Leonhard"
venue: "Int. J. Chem. Kinet. 2024, 56, 501–512"
pdf_sha256: "79d18c75d796f6b50ff332388aef02374fe59d59065b7d3549f352297dfd5451"
pdf_path: "papers/ReaxFF_others/Leonhard_Group_Int J of Chemical Kinetics - 2024 - Schmalz - Reaction path identification and validation from molecular dynamics.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024leonhard-int-j-of-che-reaction-path -->

## Summary

The article combines **ChemTraYzer (CTY)** analysis of **ReaxFF CHO2016** **NVT** **RMD** trajectories from **LAMMPS** for **iso-octane** and **n-heptane** high-temperature pyrolysis with a **validation workflow**: **NEB** transition-state refinement (**GFN1-xTB** and **ReaxFF** in **AMS**, then **B3LYP-D3-BJ/6-31G(d′,p′)** in **Gaussian 16**) to test pathways, focusing on **benzene** formation routes relative to a **Langer et al.** mechanism. The work argues **CHO2016** can recover known routes while proposing many **novel** elementary steps, but also documents **large** errors vs **DFT** for some **hydrogen migration** barriers and problematic behavior for **spin-forbidden** channels—motivating **validation** and possible **reparameterization**.

## Methods

- **RMD setup:** **LAMMPS** with **ReaxFF CHO2016** (Ashraf *et al.* parametrization as cited); **3D PBC** **gas** cells; **NVT** at **2500 K**; **100** molecules **iso-octane** simulated **5 ns** and **100** molecules **n-heptane** **3 ns**; **>5000** **total atoms** in each cell (from cited molecule counts; exact **atomic** number per frame in **Table**/**Methods** in **kinetics** **PDF**); initial mass density **0.1 g cm\(^{-3}\)** (pressures **~182 bar** and **~207 bar** respectively); geometry/connectivity every **1 fs** for CTY.
- **CTY post-processing:** Bond-order-based connectivity changes; **recrossing** filtering; **long-lived** species threshold **~10 fs**; reaction lists compared to **Langer et al.** mechanism via **SMILES** (**RDKit**); **NetworkX** pathway search with user-guided intermediates and constraints excluding very small carbon/hydrogen species as described.
- **Path validation:** Extract **10** consecutive geometries spanning **50 fs** around an event (**5** frames before/**4** after); **NEB** in **AMS** with **10 Ha/Bohr\(^2\)** springs and **climbing image**; **CHO2016** NEB uses **tapered bond orders** option; end-point **B3LYP-D3-BJ/6-31G(d′,p′)** verification of TS.
- **Compute cost (reported):** Order **30 h/ns** (**iso-octane**) and **27 h/ns** (**n-heptane**) on **16 cores** for RMD; CTY analysis **~10 h/ns** (paper’s Section 2.4).

**1 — RMD (production pyrolysis).** **Engine:** **LAMMPS** + **ReaxFF CHO2016**. **System:** **100**-molecule **iso-octane** and **n-heptane** cells at **0.1 g cm\(^{-3}\)** (~**180–210 bar** internal **pressure** from ideal-gas-like density—see paper). **PBC**; **NVT** at **2500 K**; **output every 1 fs** to **CTY**; run lengths **5 ns** and **3 ns** as stated. **Timestep, thermostat, barostat, E-field, umbrella/MTD:** not expanded here beyond **NVT 2500 K**—if absent from the indexed summary, use the **kinetics** **PDF** **§2** for the exact **fs** step and **thermostat** parameters. **2 — DFT/TS for validation (Gaussian B3LYP, AMS NEB, GFN1-xTB in places).** Treated in the same workflow bullets. **3 — NEB** and **B3LYP** verification are **reaction-path** follow-ups, not a separate “production DFT” paper block.
## Findings

- CTY yields **very large** reaction sets (**21,495** reactions after **5 ns** **iso-octane**; **7,422** after **3 ns** **n-heptane**) compared to **~10,298** reactions in the reference mechanism, with **>90%** labeled **new** by strict **SMILES** matching—illustrating both **discovery** potential and the need for **screening**.
- A **benzene** formation pathway from **n-heptane** pyrolysis is extracted that connects toward **1,3-pentadiene** chemistry in the reference network but uses **non-mechanism** steps; **DFT** vs **ReaxFF** energetics along steps such as **1,3-pentadiene → 1,2,3-pentatriene** show **large** endothermicity, so such routes are **high-temperature**-biased.
- For pathways tested, **CHO2016** can align with **QM** for some channels but **underestimates hydrogen migration barriers** by up to **~40 kcal mol\(^{-1}\)** vs **DFT** in cases highlighted, and can **lower barriers** for **spin-forbidden** reactions—stressing **QM validation** for **RMD**-discovered steps. The discussion compares the **Langer** reference mechanism, **CTY** reaction sets, and **NEB+DFT** barriers. **Kinetic** claims here reference **~2500 K** **RMD**; low-temperature **kinetics** extrapolation is **caveated** in **`## Limitations`**.
## Limitations

**SMILES** matching marks many near-duplicate elementary processes as **new**; **RMD** at **2500 K** explores chemistry far from low-temperature kinetics; **GFN-xTB** / **ReaxFF** NEB barriers carry known error bars.

## Relevance to group

Benchmarks **ReaxFF** **hydrocarbon** chemistry discovery workflows relevant to combustion/soot contexts that intersect **reactive MD** practice in the broader community.

## Citations and evidence anchors

- DOI: [10.1002/kin.21719](https://doi.org/10.1002/kin.21719)

## Related topics

- [[reaxff-family]]
