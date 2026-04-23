---
id: paper:2026ul-venue-manuscript
type: paper
title: "Atomistic-scale simulations of the high-temperature chemistry of Si/C/O/H-based polymers and their conversion to Si/C solid materials"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - material:polymer-organic
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1021/acs.jpcc.5c05359"
year: 2026
authors:
  - "Asma Ul Hosna"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "9b196254fb84098e357b3b825830df47e6ebd515c42dfabe72bf5151cc5d7575"
pdf_path: "papers/Ul_Hosna_JPC_C_SiCOH_polymers_2026_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2026ul-venue-manuscript -->

## Summary

ReaxFF molecular dynamics simulates high-temperature pyrolysis of polydimethylsiloxane (PDMS) and carbon-enriched analogs (PTMS, PETMS, PDETMS) in small periodic cells and a larger PETMS system, focusing on silicon clustering versus small-molecule products at 2000 and 3000 K, RDF-based amorphous structure of large clusters, and supporting validation runs (density, time length, replicate trajectories).

## Methods

Primary source: `papers/Ul_Hosna_JPC_C_SiCOH_polymers_2026_galley.pdf` (JPCC; galley watermark).

**Systems.** Five dimers per cell in a 25 x 25 x 25 Angstrom^3 cube at initial density 0.1 g/cm^3 (Table 1 gives formula and density per polymer); eight-fold larger PETMS systems at the same density. Additional PDMS validation at experimental-like density 0.96515 g/cm^3, extended 2 ns duration, and four replicate trajectories for PDMS at the dilute density.

**Integration and thermostat.** Energy minimization; NVT heating/equilibration at 2000 and 3000 K with Berendsen thermostat (weak coupling, damping constant 100 fs) and timestep 0.05 fs. Production MD 1 ns with coordinates saved every 100 steps (as stated).

**Force field.** ReaxFF Si/C/O/H parametrization of Soria et al. trained to DFT data for alkyl-grafted Si surfaces; energy decomposition follows standard ReaxFF bonded and nonbonded terms (equation (1) in the article, referencing Chenoweth et al. SI).

**Analysis.** Bond-order cutoff 0.3 for connectivity; large clusters defined as silicon-containing species with mass greater than 50 amu, small molecules below 50 amu; mass ratio of large clusters to small molecules versus time; radial distribution functions for large clusters after pyrolysis and cooling protocols described in the paper.

**1 — MD application (atomistic dynamics).** **Reactive** **Molecular** **dynamics** (**LAMMPS**-class **ReaxFF** **implementation** in the **article**): **Five** **dimers** per **25**×**25**×**25** **Å³** **periodic** **cell** at **0.1** **g**/**cm³** (Table 1) and **8×** **larger** **PETMS** **supercell**; **NVT** **heating** **and** **pyrolysis** at **2000** **K** and **3000** **K**; **0.05** **fs** **time** **step**; **Berendsen** **thermostat** (damping **100** **fs**); **1** **ns** **production** (coordinates every **100** **steps**); **PDMS** **validation** at **0.96515** **g**/**cm³**, **2** **ns** **duration**, **four** **replicate** **trajectories** at the **dilute** **density**. **N/A** — no **NPT** **barostat**; **N/A** — no **static** **external** **electric** **field**; **N/A** — no **replica**/**metadynamics**; **N/A** — **isotropic** **GPa** **hydrostatic** **pressure** not used in the **NVT** **pyrolysis** **(constant**-**volume** **cells**).

**2 — Force-field training** — **N/A** (uses **Soria**-class **Si**/**C**/**O**/**H** **ReaxFF** from **DFT**-**trained** **alkyl**-**Si** **data**; not a new **fit** **paper** in isolation).

**3 — Static QM / DFT as standalone study** — **N/A** (DFT only underpins the Soria ReaxFF training).

**4 — Review** — **N/A.**
## Findings

- Pyrolysis at 2000 K yields a higher large-cluster-to-small-molecule mass ratio than at 3000 K for the conditions surveyed; PTMS at 2000 K reaches a maximum reported ratio of 5.4 in the abstract.
- Simulations produce SiC-rich nanoparticles and silica-type clusters plus small-molecule byproducts including hydrocarbons, aldehydes, and CO depending on temperature and precursor.
- Eight-fold larger PETMS runs show similar qualitative patterns in small-molecule formation and cluster distributions relative to smaller cells.
- RDFs of large clusters indicate amorphous Si/C/H/O networks without crystallization on the cooling protocol described; clusters described as high-viscosity, glass-like.
- PDMS time-extension to 2 ns and alternate density conditions support that 1 ns captures the main compositional trends for the dilute systems used, while high-density PDMS shows slower fragmentation and persistent siloxane aggregates as detailed in the Results section.

- **Corpus honesty:** **Galley** `Ul_Hosna_JPC_C_SiCOH_polymers_2026_galley.pdf`; **Berendsen** under **exothermic** **reaction** **(see** `## Limitations`).

## Limitations

Galley PDF; Berendsen thermostat chosen for stability under exothermic chemistry rather than Nose-Hoover; single trajectories for PTMS, PETMS, and PDETMS at main conditions with multi-trajectory statistics for PDMS only.

## Relevance to group

Adri van Duin senior author on ReaxFF pyrolysis modeling of organosilicon precursors toward SiC-related ceramics.

## Citations and evidence anchors

DOI: `10.1021/acs.jpcc.5c05359`.

## Related topics

- [[reaxff-family]]
