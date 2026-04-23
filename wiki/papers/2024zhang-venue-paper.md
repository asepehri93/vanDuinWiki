---
id: paper:2024zhang-venue-paper
type: paper
title: "Development and validation of a general-purpose ReaxFF reactive force field for earth material modeling"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - task:validation
  - material:silicate-glass
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:dft-static
  - keyword:enhanced-sampling
candidate_tags: []
source_refs: []
doi: "10.1063/5.0194486"
year: 2024
authors:
  - "Yingchun Zhang"
  - "Xiandong Liu"
  - "Adri C. T. van Duin"
  - "Xiancai Lu"
  - "Evert Jan Meijer"
venue: "J. Chem. Phys."
pdf_sha256: "9041562f14bece68769d4acad7b5eae2f78488f1e67021a1da4147e66fd6bb96"
pdf_path: "papers/Zhang_Earth_materials_JCP_2024.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2024zhang-venue-paper -->

Si/Al/O/H/Na/K ReaxFF parameterization against broad CP2K/Gaussian DFT training sets (charges, bond/angle curves, equations of state, ion migration, condensation reactions, Keggin isomer energies) with LAMMPS `reax/c` validation on minerals, melts, and interfaces; metadynamics via PLUMED appears for free-energy workflows in the Methods section of the article.

## Summary

The manuscript presents a crust-relevant ReaxFF covering Si, Al, O, H, Na, and K. H/O and general cross-terms start from ReaxFF2017-weak and remain fixed while Si/Al/Na/K parameters (atomic, bond, off-diagonal, angle) are optimized with the standalone ReaxFF trainer using weighted least squares against DFT reference data. Training includes: Mulliken-like atomic charges for diverse clusters (Al(OH)\(_n\), Si(OH)\(_4\), NaOH hydrates, Keggin ions, gibbsite/corundum/tetrahedral Al₂O₃ phases, quartz, NaOH/Na₂O crystals); bond dissociation and angle distortion curves for Al–O, K–O, Na–Si/Al, Al–Si linkages; condensation reaction energies for Si/Al oligomers up to high polymerization with multiple topologies; Keggin α/β/γ/δ/ε relative energies; equations of state for quartz, corundum, gibbsite, aluminosilicates, feldspars, muscovite, jadeite, etc.; Na⁺ and K⁺ migration paths in albite and orthoclase using restrained path energies (DFT reference via climbing-image NEB). Periodic DFT uses CP2K/QUICKSTEP PBE, DZVP-GTH, 360 Ry density cutoff, GTH pseudopotentials, DFT-D3; cluster benchmarks use Gaussian 09 B3LYP/6-31G(d,p). Validation compares ReaxFF to DFT on charges (RMSE ~0.17 e reported for an example), energy curves (Figs. 1–2), EOS (Fig. 3), condensation energies (Fig. 4, Table S1), and transport-related profiles; Pearson correlation \(R_p \approx 0.95\) between ReaxFF and DFT training data is reported in the abstract. MD settings in §II.D: LAMMPS `reax/c`, Δt = 0.25 fs, velocity-Verlet, NVT with Nosé–Hoover, PLUMED metadynamics for free energies where noted.

## Methods

- **Optimization:** Successive one-parameter search with weighted squared error; per-element extensibility: optimize Si/Al/Na/K with O/H first, then cross-interactions.
- **DFT training:** CP2K PBE + D3 for periodic systems; Gaussian B3LYP/6-31G(d,p) for clusters; CI-NEB in LAMMPS for migration curve reproduction after training.
- **Simulation:** LAMMPS production MD; PLUMED metadynamics for free-energy surfaces; static minimization by conjugate gradient with backtracking (max step 0.2 Å) as stated.

**MD application (§II.D and validation sections):** **Engine** — **LAMMPS** `reax/c`, velocity-Verlet, **Δt = 0.25 fs**; **ensemble** — **NVT** with **Nose-Hoover thermostat** for many validation trajectories. **System size** — **mineral / melt / interface** cells as defined in the paper (full **stoichiometry** in **PDF**; `extraction_quality: partial` here). **PBC** — **3D periodic** for bulk and interfaces where stated. **Duration** — **ns**-scale segments in application examples. **Barostat** — **N/A** for the quoted **NVT** validation runs unless a quoted block uses **NPT**. **Pressure** — **N/A** for those **NVT** blocks. **Replica / enhanced sampling** — **PLUMED metadynamics** for free-energy surfaces where §II.D notes it. **Electric field** — **N/A** in the training/validation protocol summarized here.
## Findings

1. The fitted force field tracks DFT charges, bond/angle curves, and migration barriers for Na⁺/K⁺ in feldspar frameworks with strong agreement on the plotted profiles.
2. Equations of state for multiple minerals match DFT compression/expansion curves; equilibrium cell lengths within ~1% for several aluminosilicates in the validation set.
3. Condensation reaction energies for Si–O–Si, Al–O–Al, and Si–O–Al linkages across oligomer sizes and Keggin isomer energies align with DFT references (Fig. 4, Fig. S5).
4. Aggregate training fit quality \(R_p = 0.95\) is reported; broader geological applications (interfaces, melts, fluids) are discussed as future uses.
## Limitations

`extraction_quality` for the corpus PDF is marked **partial** in normalized metadata—verify fine details against the full JCP PDF; parameter set scope is crustal major elements only (no transition metals).

## Relevance to group

van Duin-group ReaxFF for geochemical/mineral systems with extensive DFT training and LAMMPS validation.

## Citations and evidence anchors

- DOI: [10.1063/5.0194486](https://doi.org/10.1063/5.0194486)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
