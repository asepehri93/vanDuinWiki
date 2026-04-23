---
id: paper:2019song-liu-nanoscale-20-predicting-preferred
type: paper
title: "Predicting the preferred morphology of hexagonal boron nitride domain structure on nickel from ReaxFF-based molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:catalysis-surfaces
  - method:reaxff
  - method:dft-static
  - task:application
  - material:hexagonal-boron-nitride
  - material:metal-surface
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:2d-materials
  - keyword:enhanced-sampling
source_refs: []
doi: "10.1039/C8NR10291K"
year: 2019
authors:
  - "Song Liu"
  - "Jeffrey Comer"
  - "Adri C. T. van Duin"
  - "Diana M. van Duin"
  - "Bin Liu"
  - "James H. Edgar"
venue: "Nanoscale (2019), 11, 5607-5616"
pdf_sha256: "2b5cde94cfd67f6ecf72229ac67772827f4d12b7b3da7e3263881d3a45503d62"
pdf_path: "papers/Liu_Nanoscale_2019_BN_Nickel.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019song-liu-nanoscale-20-predicting-preferred -->

## Summary

ReaxFF MD in LAMMPS is used to simulate hBN island growth on Ni(111) by sequential B/N deposition at controlled B : N feed ratios, comparing emergent island shapes (triangular versus hexagonal, and edge terminations) with DFT-based expectations. Adaptive biasing force (ABF) calculations in LAMMPS/Colvars support the interpretation in terms of nitrogen chemical potential. The work targets MBE-like, hydrogen-free conditions where edge polarity and metal–adsorbate chemistry, rather than a single global thermodynamic minimum, can steer domain morphology of a 2D insulator on a transition-metal substrate.

## Methods

**MD setup (Ni/B/N ReaxFF).** **LAMMPS** with the **PuReMD/Aktulga**-style ReaxFF integration as cited; **5-layer FCC Ni(111)** slab (**12×12** surface cell, **720 Ni**), **periodic xy**, **~90 Å** vacuum; **bottom Ni layer** harmonically restrained (**10 kcal/mol/Å²**). **B** and **N** atoms deposited **sequentially** onto the bare surface at **0.25 ps** interval with **minimum initial separation 1.90 Å** to avoid premature **B–N** pairing.

**Integration.** **1500 K**, **Nosé–Hoover** thermostat; **velocity Verlet**; **≥10 ns** trajectories; **Δt = 0.25 fs**.

**Electronic structure reference.** **VASP PAW PBE** **Γ-only**, **350 eV** cutoff, **0.02 eV/Å** force tolerance for **DFT** benchmarks cited in the paper.

**Free energy.** **Adaptive biasing force (ABF)** via **Colvars** in **LAMMPS** for selected coordinates (see article).

**Barostat / target pressure:** **N/A** — deposition and production runs use **constant-volume** **NVT**-style control at **1500 K** as stated; no **NPT** servocontrol called out for the main growth protocol. **Electric field:** **N/A** — not used. **Replica / enhanced sampling:** **ABF** (above) is the only **enhanced sampling** noted; **umbrella** / **metadynamics** / **replica exchange:** **N/A** unless cited elsewhere in the article.
## Findings

**Domain morphology** depends strongly on **B : N ratio** and **N availability**: **B-rich** feeds yield **fragmented** / small **hBN** patches; **near-stoichiometric** feeds produce **triangular** islands with **B-terminated zigzag** edges; **N-rich** feeds grow **larger** domains and drive transitions toward **hexagonal** shapes with **N-terminated zigzag** edges at high **N** excess—trends aligned with **DFT**-based expectations discussed in the text. **Comparisons** to **DFT** **edge** energetics and **chemical potential** arguments (including **ABF**-supported interpretation) appear in the article for the **Ni(111)** **MBE**-like setup. **Sensitivity** to **deposition** **timing**, **B:N** **stoichiometry**, and **temperature** (**1500 K** in the MD protocol) is central to the **morphology** map. **Limitations** and **future** items the authors flag (e.g. **hydrogen**-containing **CVD**) are summarized under **## Limitations** and in the **Nanoscale** **Discussion**; **corpus honesty:** numbers not repeated here should be taken from the **VOR** PDF, not this note alone.
## Limitations

**Hydrogen-free** gas-phase picture matches **MBE**-like conditions; **CVD** with **hydrogen** is not fully replicated.

**ABF**/**Colvars** **free-energy** estimates depend on **collective variable** choice and **sampling** duration; confirm **barrier** **heights** against **independent** **DFT** **NEB** where **disagreement** matters for **mechanism** claims.

**Edge** **energetics** on **Ni** can shift with **adatom** **coverage** and **temperature** beyond the **deposition** **protocols** explored in any single **figure** panel—scan **conditions** in the **full** text before **generalizing** **morphology** rules.

**Nickel** **substrates** are common **catalyst** supports for **hBN** **CVD**; translating these **MBE**-like **simulation** **insights** to **H₂**-rich **CVD** requires explicit **hydrogen** **chemistry** not fully captured here (discussion caveat).

## Relevance to group

**Ni/B/N ReaxFF** application to **2D hBN** on **Ni**, co-authored by **van Duin**.

## Citations and evidence anchors

DOI: [10.1039/C8NR10291K](https://doi.org/10.1039/C8NR10291K)

## Related topics

- [[reaxff-family]]
