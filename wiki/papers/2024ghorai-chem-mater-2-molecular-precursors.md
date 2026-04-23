---
id: paper:2024ghorai-chem-mater-2-molecular-precursors
type: paper
title: "From Molecular Precursors to MoS2 Monolayers: Nanoscale Mechanism of Organometallic Chemical Vapor Deposition"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - method:dft-static
  - domain:catalysis-surfaces
  - task:application
paper_keywords:
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemmater.3c02675"
year: 2024
authors:
  - "Sagar Ghorai and Ananth Govind Rajan"
venue: "Chem. Mater. 2024, 36, 2698-2710"
pdf_sha256: "04cb720dfe872bca8aeecd9a491cec11455538221df06a87e841cd90ca113281"
pdf_path: "papers/Others/From Molecular Precursors to MoS2 Monolayers NanoscaleMechanism of Organometallic Chemical Vapor Deposition.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024ghorai-chem-mater-2-molecular-precursors -->

## Summary

Density functional theory is used to trace organometallic CVD of monolayer 2H MoS2 from Mo(CO)6 and H2S: cluster formation, 1T to 2H evolution, edge-growth competition, and the role of an amorphous SiO2 substrate in early nucleation.

## Methods

Structural motifs of small Mo_xS_y species were surveyed in the Cambridge Structural Database (ConQuest 2022.3.0) to inform coordination and oxidation-state patterns. Cluster reaction energetics and barriers from Mo(CO)6 and H2S were computed with **Gaussian 16 (rev. C)**: LANL2DZ on Mo and 6-31G(d,p) on C, O, S, and H; **B3LYP** for exchange-correlation; SCF criteria as in the paper; transition states located by bond/angle/dihedral scans and verified by imaginary-frequency following. Gas-phase thermal corrections and zero-point energies used the **Atomic Simulation Environment (ASE)** thermochemistry module with the ideal-gas approximation; **cclib** parsed Gaussian outputs for potential energy surfaces. Substrate-including work used **VASP** with **PBE** (GGA), **PAW** potentials, **Grimme D3** dispersion with Becke-Johnson damping, **500 eV** plane-wave cutoff, electronic convergence **1e-5 eV**, force threshold **0.03 eV/Angstrom**, **Gamma-only** sampling for a **21.39 x 21.39 Angstrom** amorphous silica slab (**~7.2 OH/nm^2** silanol density per Comas-Vives-type models), **0.01 eV** Gaussian smearing; adsorbates treated harmonically and gases as ideal gas in ASE free-energy analysis.

**MD application:** **N/A** — the study is **static QM** (cluster and periodic DFT) plus thermochemical analysis, not production atomistic trajectories. **Force-field training:** **N/A** — no classical or ReaxFF parametrization.

**Static QM / DFT (checklist).** The preceding paragraphs report **functionals** (**B3LYP** clusters; **PBE** with **PAW** in VASP), **D3** dispersion for the periodic slab work, **basis** (Gaussian sets above; **500 eV** plane-wave **cutoffs** in VASP as stated), **k-sampling** / **k-mesh** (**Gamma-only** **Brillouin** sampling for the amorphous silica **slab**), **geometries, TS search, and pathways** (cluster PES and slab adsorbates; TS verification by frequencies), and **target properties** (reaction energetics, adlayer and cluster free energies, frequencies, etc.). See the paper for any settings not restated on this page.
## Findings

**Outcomes and mechanism.** The authors report a stepwise mechanism from Mo(CO)6 through Mo(CO)3, sulfidation, metallic 1T Mo-S clusters, and transition to semiconducting 2H MoS2, including competition between Mo- and S-zigzag edges that yields triangular versus hexagonal flake shapes, with stated thermodynamic and kinetic control over those edge terminations. Hydrogen (H2) elimination is identified as the rate-determining step for growth in the studied pathway. Free energies for Mo-S clusters on amorphous SiO2 highlight substrate stabilization in early nucleation, and the work argues that clusters with more than two Mo atoms can form on the SiO2 surface. The authors position the study as a basis for ab initio CVD models and, more broadly, for extending similar treatments to other TMDs.

**Comparisons and sensitivity.** The discussion ties cluster and interface energetics to **edge-termination** competition and, where the paper gives values, to relative **kinetic** barriers; consult the article for any quantitative comparison to experiment beyond this summary. **Limitations and outlook (as framed in the work)** are developed under **`## Limitations`**; **corpus honesty** for this page: claims follow the **PDF**-indexed content—if a numerical detail in this note disagrees with the version-of-record article, treat the published paper as authoritative.
## Limitations

DFT cluster and periodic models omit full reactor flow, precursor partial pressures, and experimental temperature ramps; kinetic barriers are pathway-specific within the surveyed Gaussian/VASP setup. If this wiki note and the PDF disagree on numerical detail, treat the peer-reviewed article as authoritative.

## Relevance to group

DFT-level CVD nucleation study for MoS₂ adjacent to reactive MD and TMD work elsewhere in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.chemmater.3c02675](https://doi.org/10.1021/acs.chemmater.3c02675)

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
