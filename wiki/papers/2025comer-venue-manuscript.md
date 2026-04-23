---
id: paper:2025comer-venue-manuscript
type: paper
title: "ReaxFF Parameter Set for Boron Clusters and Icosahedral Boron Crystals: Comparison with Density Functional Theory and Machine Learning Potentials"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:machine-learning-potential
  - keyword:lammps
  - keyword:gpu-md
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1021/acs.jpcc.5c04822"
year: 2025
authors:
  - "Amin Ahmadisharaf"
  - "Adri van Duin"
  - "Bin Liu"
  - "Dylan Evans"
  - "Sadra Sabouri"
  - "Jeffrey Comer"
venue: "J. Phys. Chem. C"
pdf_sha256: "f780f5d63fdf43301adba475d4494b798e4e2573578d743cf76e86544a513708"
pdf_path: "papers/Comer_Liu_Boron_JPC_2025_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025comer-venue-manuscript -->

!!! note "Corpus note"
    The ingested PDF is an ACS **galley/manuscript** proof (`Comer_Liu_Boron_JPC_2025_galley.pdf`), not necessarily the final version-of-record layout.

## Summary

The work refits a boron-focused **ReaxFF** parameter set so cluster relative energies align better with **DFT**, using a training set centered on **B\(_{80}\)** motifs (including core–shell and “Pouch” structures from earlier simulations). The refined set improves agreement on a broader test set of boron clusters (8–103 atoms), compares favorably to several **machine-learning interatomic potentials** on the same B\(_{80}\) ranking task, and is exercised in larger-scale **LAMMPS** simulations of crystallization from supercooled liquid boron and of boron solubility at a boron–molten nickel interface.

## Methods

- **DFT reference data:** Periodic cluster calculations used **VASP** with **PBE** (and related setups described in the article); plane-wave cutoff **520 eV**, **Γ-only** *k*-point sampling, **Fermi–Dirac** smearing (**0.2 eV**), **BFGS** optimization with force threshold **0.02 eV/Å**. Cluster coordinates were prepared with **ASE** in **20×20×20 Å\(^3\)** cells with **10 Å** vacuum padding.
- **ReaxFF training and versions:** An initial “Version 1” set was refit to penalize spurious low-energy boron cluster motifs, leading to **Version 2** and a final **Version 3 (B-v3)** trained with explicit handling of the “Pouch” geometry and its DFT energetics. Relative energies reported for B\(_{80}\) structures use **geometry optimization under each model** before comparing cluster energies.
- **Reactive MD (LAMMPS):** Simulations used **LAMMPS (23 Jun 2022)** with **ReaxFF** and **GPU-accelerated** routines. **Time step 0.25 fs.** Isolated clusters: **NVT** with **Langevin** thermostat (**200 fs** damping). Melts and continuous solid systems: **NPT** with **Nosé–Hoover** thermostat and barostat (**100 fs** time constant). Trajectories saved as **DCD every 1000 steps**; visualization and analysis used **VMD** and in-house **Tcl** scripts (deposited as noted in the paper).
- **Seed-crystal growth tests:** β-rhombohedral boron supercells with restrained seeds were melted (**3600 K**), then cooled to **1300–1700 K** at **1 atm** for **10–30 ns**; additional runs explored **~10 and ~24 GPa** and larger supercells as described in the article.
- **Boron–Ni solubility estimate:** Canonical (**NVT**) simulations placed solid boron against a molten **Ni(111)**-derived slab; boron fraction was estimated in a slab-centered region (\(|z-z_{\mathrm{Ni,COM}}|<5\) Å) versus time.

## Findings

- The final **B-v3** parameter set reproduces the **correct relative ranking** of the key **B\(_{80}\)** training structures compared to **DFT**, including a large penalty for the spurious “Pouch” motif that earlier parameter sets favored.
- On the training trio of B\(_{80}\) structures, **B-v3** and **PFP v7.0.0** were among the few models that matched **DFT** ranking; **B-v3** achieved the **lowest RMS error** versus DFT among the empirical and MLIPs surveyed in the comparison table.
- Extended **melts and growth** simulations show **more icosahedral character** with the refined parameters than with the prior boron ReaxFF parameterization.
- **Boron solubility** in contact with **molten nickel** from the refined parameters is **closer to experimental expectations** than the older boron parameter set, which underestimated solubility strongly.

## Limitations

**Boron** parameterization is **cluster- and B\(_{80}\)**-centric; transfer to **all** bulk **allotropes** and **impurity** chemistries is not guaranteed. **Proof/galley** PDF pagination may differ from the **journal** version. **GPU** **LAMMPS** timings and **thermostat** choices affect observable **nucleation** pathways in long melts.

## Relevance to group

**Jeffrey Comer**, **Adri van Duin**, **Bin Liu**, and collaborators refine **boron** **ReaxFF** for **icosahedral** **boron** **crystallization** and **metal** **contact** scenarios—adjacent to **materials** **synthesis** modeling in the corpus.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpcc.5c04822](https://doi.org/10.1021/acs.jpcc.5c04822)

## Related topics

- [[reaxff-family]]
