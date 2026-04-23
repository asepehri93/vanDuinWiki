---
id: paper:2025amin-ahmadisharaf-acs-growth-hexagonal
type: paper
title: "Growth of hexagonal boron nitride from molten nickel solutions: a reactive molecular dynamics study"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reactive-md
  - domain:2d-layered
  - material:hexagonal-boron-nitride
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:gpu-md
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:parallel-tempering
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.4c16991"
year: 2025
authors:
  - "Amin Ahmadisharaf"
  - "Bin Liu"
  - "James H. Edgar"
  - "Jeffrey Comer"
venue: "ACS Appl. Mater. Interfaces 2025, 17, 11213−11226"
pdf_sha256: "883bc829693c016b43ecf3e0e2a8ef354bc89161c89a5683bd35d7dbeed610d1"
pdf_path: "papers/ReaxFF_others/Comer_Liu_ACSAMI_2025_growth-of-hexagonal-boron-nitride-from-molten-nickel-solutions-a-reactive-molecular-dynamics-study.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2025amin-ahmadisharaf-acs-growth-hexagonal -->

## Summary

**ReaxFF molecular dynamics in LAMMPS (GPU-accelerated)** is used to simulate **hBN nucleation and growth** from **liquid nickel** solvent exposed to **N\(_2\)** gas, over **~20–30 ns** trajectories and complementary **temperature replica exchange** equilibration of **Ni–B** melts. The work argues that chemistry localizes at the **metal–gas interface**, progresses through **N–N–B** and **B–N–B** intermediates, and that **boron concentration** and **temperature** strongly modulate **hBN** yield on accessible time scales.

## Methods

- **Engine and parameters:** **LAMMPS** **molecular dynamics** with **reactive ReaxFF** for **B/N/Ni** (parameters aligned with the authors’ prior work; **parameter files** and **Zenodo** bundle referenced in the article). **0.25 fs** integration timestep. **NVT** with **Langevin** thermostat (**200 ps** damping) for most constant-volume runs; **NVE** for **diffusion** estimates. **NPT** (later section) uses **Nosé–Hoover** barostat/thermostat as described (**Shinoda**-style barostat in **z** only for some cells).
- **Nickel slab / melt:** **fcc Ni** slab (**12×12** close-packed planes, **1520 atoms**), **3D PBC** **periodic** **27.89 × 32.20 × 220 Å\(^3\)**, **Ni(111)** surfaces, melted at **1800 K** in **NVT** to obtain a **liquid** slab.
- **Boron loading:** A **β-rhombohedral boron** nanocrystal (**208 B**) dissolves into molten Ni at **1900 K** (**13 ns** segment), then **temperature replica exchange** (**20 replicas**, **1800–2700 K**) equilibrates **Ni–B** melts, yielding among others a **~12 at.% B** solution (**2.5 wt%**) used as a starting point for growth studies.
- **N\(_2\) + Ni:** Pure liquid **Ni** slabs with **60 / 120 / 240** **N\(_2\)** molecules at **84 / 168 / 336 atm** effective pressures (**~200 Å** **z** extent), **5 ns** runs to survey **N\(_2\)** interaction with molten nickel.
- **hBN growth runs:** From equilibrated **Ni–B** melts, **88 N\(_2\)** molecules are placed **>12 Å** from the surface; simulations **20–30 ns** at **1750–2700 K** in the **fixed 27.89 × 32.20 × 220 Å\(^3\)** cell.
- **Constant-pressure variants:** **104 B** atoms, **208 N\(_2\)**, **1750 K**, **15 ns**, **25 / 50 / 100 atm** targets with **z**-only barostat and large **N\(_2\)** reservoirs (initial **z** chosen from ideal gas law).

**Slot summary:** **N/A — electric field**; **N/A — umbrella sampling**; **replica exchange** (temperature) used for **Ni–B** melt **equilibration** as above.
## Findings

- **Reaction localization:** Conversion to **BN** occurs primarily at the **liquid Ni surface** because **N** solubility in bulk Ni is low and intermediates favor the **interface**.
- **Mechanism:** **N\(_2\)** attacks **Ni-solvated B**, forming **N–N–B** species, then **B–N–B** motifs; species **ripen** between **hBN** crystallites (**Ostwald**-like transport of nitrogen).
- **Processing trends:** **hBN** production on **10² ns** scales is **strongly sensitive to B concentration** and **mildly sensitive** to **N\(_2\)** pressure in the **2.5–10 MPa**-class regime explored for some setups (**6–12 at.% B** family in the abstract framing). **1750 K** (just above Ni melting) gives the **highest** growth rate in the studied window; **≥2000 K** yields **no extended hBN sheets** within the simulated trajectories.
- **Kinetics:** Path sampling indicates **incorporation of small B–N motifs into large sheets** is often **rate-limiting**; at **>1900 K**, **sheet breakup** competes with growth, explaining loss of large sheets despite persistent intermediates.
## Limitations

- **Force-field** fidelity for **molten alloy–gas** chemistry and **long-range transport** is finite; **experimental** metal-flux reactors include **impurities** and **convective mixing** not modeled here.

## Relevance to group

Complements other **hBN** and **ReaxFF** corpus entries by focusing on **flux growth** from **molten Ni** with explicit **N\(_2\)** gas environments.

## Citations and evidence anchors

- DOI: [10.1021/acsami.4c16991](https://doi.org/10.1021/acsami.4c16991)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
