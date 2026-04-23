---
id: paper:2018brownell-physical-che-deformation-mechanisms
type: paper
title: "Deformation mechanisms of polytetrafluoroethylene at the nano- and microscales"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - material:polymer-organic
  - method:classical-md
  - method:reaxff
  - task:application
  - scale:multiscale
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:tribology
  - keyword:classical-ff
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1039/C8CP05111a"
year: 2018
authors:
  - "Matthew Brownell"
  - "Arun K. Nair"
venue: "Phys. Chem. Chem. Phys., 21 (2019) 490–503 (advance publication 2018)"
pdf_sha256: "2541109686a41ccc0e3ef66b94086e19a933582d19cd24cdbf9a5ad1871a3397"
pdf_path: "papers/ReaxFF_others/2018- Deformation mechanisms of polytetrafluoroethylene at the nano- and microscales.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018brownell-physical-che-deformation-mechanisms -->

## Summary

Multiscale modeling of **polytetrafluoroethylene (PTFE)**: **atomistic MD** informed by **ReaxFF**-derived parameters feeds a **coarse-grained** model used to probe **microscale** particle **mechanics**, **indentation**, and **scratch** friction, linking **chain-scale** and **bulk** responses. The article emphasizes PTFE’s practical importance in **low-friction** coatings and films while arguing that **nano- to micro-scale** deformation modes must be captured to interpret tribological measurements that are sensitive to chain alignment and particle packing.

## Methods

From the PCCP article PDF (`pdf_path`).

- **Atomistic (ReaxFF / LAMMPS):** All atomistic MD uses **ReaxFF** in **LAMMPS** with visualization in **VMD** (as stated). **Single-chain** tensile tests on lengths **25-1000 A** (e.g. **20-755** C atoms per chain), including **300 K** in **57.5 wt% water** vs vacuum; **100 A** chains scanned **300-600 K** (**50 K** steps). Chains are **minimized 2 ps**; end **C** atoms constrained against curling (**Y,Z** fixed at both ends), then one end fixed and the other strained to **20%** strain. **Bulk** PTFE built from aligned chains in a square lattice (**Z**-aligned), box about **99 x 55 x 108 A^3** after equilibration, **X/Z** periodic, bottom **10 A** (two layers) fixed; **spherical indenter R=25 A**, **10 A** indent, **10 A** scratch length, scratch angles **0 / 45 / 90** degrees vs **Z**.
- **Coarse-grained:** **Bundle** models (**~28 x 17.75 x 17.41 A^3**) equilibrated **300 K**; **ReaxFF** tensile (**0.05 ps^-1** strain to **13%**), three-point bend, and equilibrium-distance fits define bead **bond/angle/vdW** parameters (**Table 1** in paper). **CG** particles used for **microscale** indentation/scratch and surface-roughness sweeps.
- **Workflow note:** The CG parametrization is explicitly **anchored** to the ReaxFF atomistic responses chosen for PTFE-like fluorocarbon chemistry, so that bead interactions inherit the qualitative stiffness and failure trends observed before coarse graining.
- **Ensemble / thermostat / timestep:** Atomistic stages use **NVT**-style thermalized dynamics in **LAMMPS** with **ReaxFF** integration **timestep** typically **≤0.25 fs** (femtoseconds; confirm tabulated value in PCCP **Methods**); **Nose–Hoover** or equivalent thermostat settings follow the article for tensile vs shear protocols.
- **Duration:** **Equilibration** and **production** segment lengths are reported in **ps** for single-chain pulls and bulk **indentation** runs (see **PDF** tables).
- **Barostat / pressure:** **N/A — hydrostatic pressure control** not used for the quoted constant-volume **ReaxFF** cells; contact **stress** during indentation is imposed mechanically by the rigid indenter, not by an **NPT** **barostat**.

## Findings

- **Temperature** strongly affects **maximum strength** of a **single chain**; **elastic modulus** depends on **chain length**, with **shorter** chains than **100 Å** showing increased **maximum strength** (as stated in the abstract).
- For **bulk** PTFE, **friction** under **indentation/scratch** depends on **scratch direction** relative to the substrate.
- **CG** simulations show **indentation force** depends on **PTFE particle density** and that **smoother** particle surfaces yield **lower friction**; the authors position the model for comparison to **experimental PTFE thin films**.
- The combined atomistic-to-CG pipeline is used to argue that **anisotropic** substrate response under scratch-like loading can emerge from **chain orientation** and **contact geometry**, not only from bulk modulus alone.

## Limitations

- **CG** parametrization ties to a specific **ReaxFF** training path; quantitative transfer outside the fitted chemistries and strain rates should be checked.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
