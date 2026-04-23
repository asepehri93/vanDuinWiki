---
id: paper:2015broqvist-venue-jp5b01597
type: paper
title: "ReaxFF force-field for ceria bulk, surfaces, and nanoparticles"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - domain:catalysis-surfaces
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - task:validation
  - material:oxide
  - scale:atomistic
source_refs: []
doi: "10.1021/acs.jpcc.5b01597"
year: 2015
authors:
  - "Peter Broqvist"
  - "Jolla Kullgren"
  - "Matthew J. Wolf"
  - "Adri C. T. van Duin"
  - "Kersti Hermansson"
venue: "Journal of Physical Chemistry C 2015, 119, 13598–13609"
pdf_sha256: "f47c87db7068a1d0d403e819f072d9267d392a7103a197374904810083b05744"
pdf_path: "papers/Broqvist_Ceria_JPC_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015broqvist-venue-jp5b01597 -->

## Summary

Broqvist *et al.* introduce a **ReaxFF** parametrization for **CeO\(_2\)** and **CeO\(_{2-x}\)** trained predominantly from **PBE+U** reference data, targeting **oxygen chemistry** in **bulk**, **extended surfaces**, **surface steps**, and **nanoparticles** where **Ce** **redox** and **vacancy** ordering drive **catalytic** response. Validation claims in the abstract include reproduction of **bulk moduli**, **lattice parameters**, and **surface energies** for stoichiometric systems; **step energies** on **(111)**; **vacancy formation energies** and their **depth dependence** from **(110)** and **(111)** surfaces upon **reduction**; and **energy orderings** among stoichiometric **tetrahedral**, **octahedral**, and **cubic** nanoparticle motifs plus partially reduced **octahedra**. The study positions the model as a practical complement to costly **QM dynamics** for **redox** problems on **ceria** where **bond-order**-based **oxygen** rearrangements matter.

## Methods

### Force-field training (primary contribution)

- **Parent FF / elements:** new **ReaxFF** description for **Ce/O** spanning **stoichiometric CeO₂** and **reduced CeO\(_{2-x}\)**, including **bulk**, **extended surfaces**, **steps**, and **nanoparticle** motifs (J. Phys. Chem. C **2015**, **119**, 13598–13609).
- **QM reference:** **VASP** **PBE+U** training/validation set with **PAW** pseudopotentials; **Hubbard U = 5 eV** on **Ce 4f** (guided by prior ceria literature); **PBE+U** used as consistently as possible across the training set. **Special cases:** **O–O** interactions reuse the established **ReaxFF “water branch” O–O** parameters (B3LYP-fitted reference data cited in the paper); **Ce metal** uses **experimental** lattice constant and bulk modulus in fitting; **EEM charge parameters** are trained to **B3LYP Mulliken charges** on small ceria clusters (Gaussian09; **Ce(RSC97)/ECP** and **O aug-cc-pVTZ** basis).
- **DFT numerical settings (PBE+U reference):** **30 Ry** kinetic-energy cutoff for plane-wave expansions; **Γ-only** sampling for clusters/molecules; **Monkhorst–Pack** meshes for bulk/surfaces chosen so total energies converge within **0.02 eV**; relaxations until max force **< 0.02 eV Å⁻¹**.
- **Training set / targets:** energies and structural data for ceria **bulk**, **surfaces**, **vacancy** arrangements, **step** motifs, and **nanoparticle** shape series used to reproduce **PBE+U** ordering/energetics within the ReaxFF functional form (Eq. (1) energy partitioning in the article).
- **Optimization:** **ReaxFF** parameter optimization performed with the **standard ReaxFF optimization software** using a **successive one-parameter parabolic search** strategy (as referenced in the article).

### ReaxFF “application” calculations reported in the parameterization paper

- **Engine / code:** **LAMMPS** with the authors’ new **ceria ReaxFF** implementation is used for **geometry relaxations** and validation examples (section **2.3**).
- **MD production trajectories:** **N/A —** the manuscript’s core validation is **energy/structure** benchmarking and nanoparticle stability trends, not long finite-temperature production MD with reported timesteps/thermostats. Reported ReaxFF work instead uses **0 K conjugate-gradient** relaxations in **PBC supercells** (hundreds to thousands of atoms for bulk, slabs, steps, and nanoparticle motifs; exact counts in the PDF). **N/A —** finite-**T** **NVT/NVE/NPT** trajectories, barostat/stress control, and applied fields or enhanced sampling are not part of these validation segments. **Duration in ps/ns:** **N/A —** relaxations terminate at convergence rather than a fixed **ns**/**ps** production schedule.

### Static QM / DFT

Covered under the **PBE+U VASP** workflow above (this is the authoritative reference layer for training).

## Findings

- **Stoichiometric ceria:** the fitted field reproduces key **bulk moduli**, **lattice parameters**, and **surface energies** for **CeO₂** within the accuracy bands shown in the paper’s tables/figures.
- **Reduction / vacancies:** **vacancy formation energies** and **depth dependence** from **(110)** and **(111)** surfaces track the **PBE+U** references sufficiently well to discuss **subsurface vs surface** reduction preferences at the force-field level.
- **Morphology / nanoparticles:** relative stabilities among **tetrahedral**, **octahedral**, and **cubic** nanoparticle motifs (including **partially reduced octahedra**) follow the **DFT** ordering closely enough that the authors use them to discuss **shape-dependent** ceria stability trends.
- **Comparisons / limitations (authored):** remaining discrepancies are discussed in-context (e.g., cases where **Ce metal** or **strong correlation** effects are hardest for a bond-order model); users are implicitly cautioned to validate outside the training envelope.
- **Comparisons vs experiment / literature:** the article benchmarks against **PBE+U** and selected **experimental** lattice/bulk data where used in fitting (see tables).
- **Sensitivity / transfer levers:** accuracy depends strongly on **coverage**, **oxidation state**, and **morphology** class (bulk vs surface vs nanoparticle) within the training envelope.
- **Corpus honesty:** for numerical **barriers** not explicitly included in training, treat this page as navigation prose and use the **PDF** (`papers/Broqvist_Ceria_JPC_2015.pdf`) as the **version-of-record** source.

## Limitations

**Ce 4f** physics is only captured **empirically** within the **training** set; users must validate for each new **surface orientation** or **dopant** scenario beyond the training envelope. **Strongly correlated** **electron** errors may appear for **non-training** **Ce** environments, so **quantitative** **barriers** for **reactions** not included in fitting should be treated cautiously.

## Relevance to group

**Adri C. T. van Duin** co-authorship; expands the **ReaxFF oxide/redox** portfolio for **ceria**, widely used in **catalysis** and **energy** materials simulations.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpcc.5b01597](https://doi.org/10.1021/acs.jpcc.5b01597)

## Related topics

- [[reaxff-family]]
