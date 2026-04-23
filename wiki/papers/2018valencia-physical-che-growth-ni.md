---
id: paper:2018valencia-physical-che-growth-ni
type: paper
title: 'Growth of Ni nanoclusters on irradiated graphene: a molecular dynamics study'
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:alloys-metallurgy
- domain:carbon-hydrocarbon
- domain:reactive-md
- material:graphene-carbon-nano
- method:reaxff
- scale:atomistic
- task:application
paper_keywords:
- keyword:graphene-carbon
- keyword:metallic-systems
- keyword:lammps
- keyword:reaxff-application
- keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: 10.1039/C7CP08642C
year: 2018
authors:
- F. J. Valencia
- E. E. Hernandez-Vazquez
- E. M. Bringa
- J. L. Moran-Lopez
- J. Rogan
- R. I. Gonzalez
- F. Munoz
venue: Phys. Chem. Chem. Phys.
pdf_sha256: 1a56eb17dd0649fa9f64530ab35f6a56c8be44d130b5093a127f96a3749e5340
pdf_path: papers/ReaxFF_others/Valencia-Phys.Chem.Chem.Phys.2018-20-16347.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018valencia-physical-che-growth-ni -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the PCCP article identified by `doi`, `title`, and `pdf_path`.

## Summary

**ReaxFF MD (LAMMPS)** simulates **soft deposition** of **Ni** atoms onto **defective graphene** sheets containing tunable **monovacancy** concentrations (**0.25–1.0%** removal levels in the study). Ni is inserted every **5 ps** in a **1–2.5 Å** “safe” height window with **0.5 fs** timestep to avoid impact damage; post-deposition dynamics extend **≥2 ns**. The work emphasizes **non-equilibrium cluster-size distributions**: **frequency vs cluster size** decreases monotonically, yet **most atoms** can reside in **a few large clusters**—behavior captured by a simple **cross-section–weighted** attachment model and **Monte Carlo** illustrations—contrasting with **hard-landing** scenarios that yield more **monodisperse** islands.

Motivation ties **Ni** on **CVD** graphene to catalytic growth and interconnect applications where **vacancy** density from irradiation or transfer steps can steer **nucleation** statistics; comparing **soft** versus **hard** deposition protocols therefore tests how impact energy sets emergent **island-size** heterogeneity.

## Methods

- **Engine / potential:** **LAMMPS** **ReaxFF** for **C–C**, **Ni–Ni**, **Ni–C** using **Ni/C** parameters from **Yoon et al.** (DFT-trained Ni phases); qualitative discussion of binding/diffusion metrics vs DFT literature in the paper.
- **Substrate:** ~**10.2 × 10.3 nm** graphene (**3936 C**), periodic in-plane; **random monovacancies** to target porosity; **conjugate-gradient** relaxation; **0.2 ns** at **2500 K** with **zero-pressure** barostat to accommodate vacancy strain (per protocol in §2.1).
- **Deposition:** Ni atoms added every **5 ps** between **1.0–2.5 Å** above the sheet; **Nosé–Hoover** thermostat for diffusion segments; production runs **≥2.0 ns** after deposition completes.
- **Ensemble:** Initial defective-sheet relaxation uses **NPT**-style **zero-pressure** control at **2500 K** (**0.2 ns**) as in §2.1; **Ni** **soft-landing** and post-deposition evolution use **NVT** segments with **Nosé–Hoover** thermal control as described in the **PCCP** **Methods**.
- **Timestep:** **0.5 fs** during **Ni** insertion to limit impact damage; longer post-deposit segments follow the article’s production settings (see **`papers/ReaxFF_others/Valencia-Phys.Chem.Chem.Phys.2018-20-16347.pdf`** for any rescaled **timestep** after deposition).
- **Modeling:** Phenomenological **rate/Monte Carlo** treatment of capture cross-sections vs cluster size to interpret broad, **heavy-tailed** cluster statistics.

- **Electric field:** **N/A — not used**.
- **Replica / enhanced sampling:** **N/A — not used** (standard time-stepped **MD** plus the analytical/Monte Carlo post-model noted above).
## Findings

- **Mobility + pinning:** High **Ni** diffusivity on graphene plus **strong vacancy binding** yields growth where **large clusters** accrete wandering atoms efficiently once their **cross-section** exceeds competing vacancies.
- **Bimodal statistics:** Cluster-count vs size **decreases** with size, but **cumulative weight** shows a **minority** of very large clusters containing a **majority fraction** of atoms (e.g. up to **~40%** of all Ni in one cluster under some T/porosity conditions reported).
- **Trends:** Higher **T** and lower **defect density** favor **fewer, larger** clusters; higher **porosity** shortens mean free paths and suppresses runaway coarsening into a single giant island.

- **Corpus honesty:** Cluster statistics and **DFT** comparison numbers should be read from **`papers/ReaxFF_others/Valencia-Phys.Chem.Chem.Phys.2018-20-16347.pdf`** (PCCP **version of record**); this page does not substitute for the tabulated **Results**.
## Limitations

ReaxFF Ni–vacancy binding differs quantitatively from some **DFT** values; out-of-equilibrium deposition statistics are illustrated with single long trajectories rather than thousands of averaged runs.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
