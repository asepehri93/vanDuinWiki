---
id: paper:2025amin-ahmadisharaf-j-phys-chem-reaxff-parameter
type: paper
title: "ReaxFF parameter set for boron clusters and icosahedral boron crystals: comparison with density functional theory and machine-learning potentials"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:machine-learning-potential
  - keyword:lammps
  - keyword:dft-static
  - keyword:nvt-simulation
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5c04822"
year: 2025
authors:
  - "Amin Ahmadisharaf"
  - "Adri C. T. van Duin"
  - "Bin Liu"
  - "Dylan Evans"
  - "Sadra Sabouri"
  - "Jeffrey Comer"
venue: "J. Phys. Chem. C 2025, 129, 22319−22333"
pdf_sha256: "95c0e89077924548e1a2c8787abac815908e10ea5e80fbf98880a414d75456f1"
pdf_path: "papers/Ahmadisharaf_Boron_clusters_JPCC_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025amin-ahmadisharaf-j-phys-chem-reaxff-parameter -->

## Summary

The authors **reoptimize ReaxFF parameters** for **elemental boron** (clusters and condensed phases) using **VASP PAW GGA-PBE** training data for **B/O/Ni-related** sets (iteratively adding **B\(_{80}\)** cluster motifs, including a low-energy **core–shell** structure and a high-energy **“Pouch”** structure from early ReaxFF runs). The new parameter set is compared against **DFT** (also **GPAW PBE** for a **58-cluster** test set) and several **machine-learning interatomic potentials** (**MACE**, **PFP**, **SevenNet**, etc.) on **relative cluster stabilities**, **icosahedral character** in melt/crystal simulations, and **B solubility** in **molten Ni**.

## Methods

- **Training DFT (VASP):** **PAW GGA-PBE**, **520 eV** cutoff, **Γ-centered k-meshes** at **0.03 Å\(^{-1}\)**-type density for periodic systems; **Γ-only** for **20 Å** cubic boxes of isolated clusters; **spin-polarized** treatment for **Ni-containing** cells; electronic/ionic convergence thresholds as stated (**10\(^{-6}\) eV** SCF, **−0.02 eV/Å** ionic for bulk).
- **Test-set DFT (GPAW):** **PBE**, **520 eV**, **Γ** sampling, **0.2 eV Fermi smearing**, **BFGS** relaxation (**0.02 eV/Å** force threshold) for **58 clusters** spanning **8–103 atoms**.
- **ReaxFF optimization:** Iterative **Versions 1–3** expand training with **B\(_{80}\)** data from **Li et al.** and internal ReaxFF-generated isomers; energies are compared after **ReaxFF-side geometry relaxation** (RMSD bounds and bond-network checks reported).
- **MD (LAMMPS, Jun 2022):** **ReaxFF** with **GPU** kernels; **0.25 fs** timestep; **NVT** (**Langevin**, **200 ps** damping) for clusters; **NPT** (**Nosé–Hoover**, **100 fs** time constants) for melts/crystals; **CG** minimization to **1×10\(^{-8}\)** kcal mol\(^{-1}\) Å\(^{-1}\) force tolerance; analysis/visualization in **VMD** with **Tcl** scripts (Zenodo).

**N/A (add-on protocol notes for this reparameterization paper):** **External electric field**; **umbrella / metadynamics** (not used in the training workflow summarized above). **MD** **validation** **temperatures** follow the **K** **schedules** in the melt and **NPT** blocks (e.g. **1300–3600 K** **anneal** / **quench** windows in the **PDF**), with **Langevin** or **Nose-Hoover** **thermostat** selection as written for each **stage**.
## Findings

- Among **prior ReaxFF** sets and the **MLIPs** tested for ranking **B\(_{80}\)** isomers, **only the new ReaxFF** and **PFP v7.0.0** reproduce the **DFT ordering** for the two **B\(_{80}\)** reference morphologies highlighted.
- On the **58-cluster** test set, the refined parameters improve **energy agreement** versus earlier boron ReaxFF and compare competitively with several **MLIPs** in aggregate metrics reported in the paper.
- Larger **supercooled liquid boron** simulations show **higher icosahedral content** with the new field than the older boron parameterization.
- **Solid B | molten Ni** interface simulations yield **boron solubility** closer to **experimental expectation**, whereas the **previous** boron parameter set **underestimated** solubility strongly.
## Limitations

- **Transferability** to **boron-rich compounds** beyond the training/test sets (e.g., complex borides/hetero-systems) still requires **separate validation**.
- **Cluster DFT** references mix **VASP** and **GPAW** pipelines; users should follow **SI** for exact **cluster-by-cluster** handling.

## Relevance to group

Adri C. T. van Duin is a co-author; the paper is a **core ReaxFF parameterization** reference for **icosahedral boron** and **Ni–B** processing contexts aligned with other **boron/hBN** work in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.5c04822](https://doi.org/10.1021/acs.jpcc.5c04822)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
