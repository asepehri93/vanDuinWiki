---
id: paper:2018cu-venue-microsoft-word
type: paper
title: "Supplemental material: What drives metal surface step-bunching in graphene chemical vapor deposition?"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - material:metal-surface
  - method:classical-md
  - task:application
paper_keywords:
  - keyword:supporting-information
  - keyword:graphene-carbon
  - keyword:classical-ff
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevLett.120.246101"
year: 2018
authors:
  - "Yi Ding"
  - "Da Luo"
  - "Zhu-Jun Wang"
  - "Jichen Dong"
  - "Xu Zhang"
  - "Marc-Georg Willinger"
  - "Rodney S. Ruoff"
  - "Feng Ding"
venue: "Supporting information, Phys. Rev. Lett. 120, 246101 (2018)"
pdf_sha256: "ab5e45f8f225b1907308920f953c5f3ff4e1b41f4006c0041ef12292fb1b9a3c"
pdf_path: "papers/Others/Cu_Graphene_Ding_PhysRevLett_SI.120.246101.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018cu-venue-microsoft-word -->

## Summary

This corpus entry stores the **Supplemental Material** PDF for **Physical Review Letters** **120**, **246101** (**DOI `10.1103/PhysRevLett.120.246101`**), which investigates **Cu** surface **step bunching** during **graphene chemical vapor deposition (CVD)**. The SI bundles **additional experiments** (for example **AFM** measurements and tabulated growth conditions) and **theory / molecular dynamics** sections that quantify energetics of **adatom** diffusion, **step** interactions, and **graphene-covered** **Cu** geometries used in **step-bunching** simulations. The filename in `papers/` reflects a **Microsoft Word** export artifact, but the registered bytes are the journal supplemental PDF. Scientific interpretation of **why** steps bunch and under which growth conditions should be taken from the **main PRL letter**; this page documents what the SI contains for **reproducibility** and retrieval.

## Methods

The supplemental text details **DFT (VASP)** calculations using **PBE** with **PAW** potentials, a **400 eV** cutoff, **DFT-D2** dispersion correction, and **climbing-image nudged elastic band (cNEB)** barriers for selected diffusion processes, with force thresholds on the order of **1e-2 eV/Å** as stated. Adatom diffusion beneath graphene is modeled with supercells cited in the SI (for example **2×2** graphene on **2×2 Cu(111)** with **five** Cu layers in one referenced setup). **Classical MD** in **LAMMPS** uses **EAM** for **Cu–Cu**, **AIREBO** for **graphene C–C**, and a **Lennard-Jones** cross-term for **Cu–C** with parameters compared against **VASP** binding energies (**Table S2** in the SI). Larger cells (**10×10** graphene on **10×10 Cu(111)** with **10** Cu layers, **1000** Cu atoms) support energy-tracking simulations of **step bunching** under **NVT** conditions at **1250 K** with a **Nose–Hoover** thermostat, **timestep 1.0 fs**, and **velocity-Verlet** integration, as summarized in the computational details section. **Periodic boundary conditions** apply in-plane for the **Cu(111)** **slab** supercells described. **Production** **MD** segment lengths (cumulative **ns** or **µs** totals) appear in the SI figures tracking **step** energetics. **Barostat / hydrostatic pressure:** **N/A —** the excerpted **NVT** **LAMMPS** protocol does not impose bulk **NPT** **pressure** targets. The SI’s role is to show that the **LJ** **Cu–C** cross-term is not arbitrary: it is anchored to **DFT** binding trends for adspecies relevant to **CVD**-like conditions, which matters because step energetics can be dominated by subtle **metal–carbon** interactions under graphene coverages.

## Findings

**Mechanism / outcomes:** This ingest is **SI-only**; atomistic **diffusion** / **step-bunching** **kinetics** are illustrated with extended **LAMMPS** setups, but headline **mechanism** claims remain in the **main PRL** text.

**Comparisons:** **DFT** **cNEB** barriers and **EAM**/**AIREBO**/**LJ** **MD** energies are **compared** to justify the **Cu–C** cross-term used in large-cell **benchmarks** relative to **VASP** references.

**Sensitivity:** **Temperature** (**1250 K** in the quoted **NVT** **MD**), **graphene** supercell size, and **Cu** layer count influence extracted **step** interaction **energies**.

**Limitations / outlook:** Quantitative conclusions about **CVD** window mapping belong to the **letter** plus any updated corrigenda; this **PDF** can lag figure numbering.

**Corpus honesty:** **SI-only** — cite **Phys. Rev. Lett.** **120**, **246101** for assertions; use this slug for **parameters** and **extended** **simulation** traces (`pdf_path`).

## Limitations

**SI-only** pages must be paired with the **primary PRL** text; the wiki filename does not affect DOI resolution.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevLett.120.246101](https://doi.org/10.1103/PhysRevLett.120.246101) — primary letter; this PDF is supplemental material only.

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
