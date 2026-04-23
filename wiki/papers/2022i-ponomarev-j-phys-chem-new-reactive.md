---
id: paper:2022i-ponomarev-j-phys-chem-new-reactive
type: paper
title: "New Reactive Force Field for Simulations of MoS2 Crystallization"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - material:tmd
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:2d-materials
  - keyword:lammps
  - keyword:dft-static
source_refs: []
doi: "10.1021/acs.jpcc.2c01075"
year: 2022
authors:
  - "I. Ponomarev"
  - "T. Polcar"
  - "P. Nicolini"
venue: "J. Phys. Chem. C"
pdf_sha256: "e1bee4c7f41c739b041690c90ff2794b05d56268b67f18bb8b360463d676f33c"
pdf_path: "papers/ReaxFF_others/Ponomarev_MoS2_NaCl_JPC_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022i-ponomarev-j-phys-chem-new-reactive -->

## Summary

Ponomarev *et al.* present a **Mo–S ReaxFF** parametrization targeted at **crystallization** behavior of **molybdenum sulfide**, a problem where older reactive fields can produce **rock-salt**-like **Mo–S** motifs that conflict with the **layered 2H** structure observed experimentally for **MoS\(_2\)**. The authors fit **ReaxFF** parameters against **VASP** **DFT** references using **PAW** potentials, the **PBE** functional, **DFT-D2** dispersion corrections, and optional **Hubbard +U** tests for select cases, emphasizing reproduction of **energies**, **forces**, **cell parameters**, and **geometry descriptors** across **Mo\(_x\)S\(_y\)** crystals used in the training corpus. Optimization uses a **Monte-Carlo-like** random walk in parameter space with **Metropolis-style** acceptance based on weighted error reduction, starting from a related parameter block discussed in the paper (including **V–O** heritage in the fitting narrative). **LAMMPS** `reax/c` simulations with **0.5 fs** timesteps and tight **conjugate-gradient** tolerances perform **melt–quench** crystallization tests to see whether the new field recovers **layered** **MoS\(_2\)** ordering from disordered melts.

## Methods

### A — ReaxFF training / fitting (Mo–S)

- **QM reference:** **VASP** **PAW**, **PBE** + **DFT-D2**, **500 eV** cutoff; optional **+U** tests; stress/force convergence per article.
- **Optimization:** **Monte Carlo**/**Metropolis** walk in parameter space minimizing weighted multi-objective error over **Mo\(_x\)S\(_y\)** **crystal** training sets.
- **Goal:** Avoid **rock-salt**-like **dense** **Mo–S** minima; favor **layered 2H-MoS\(_2\)**-like physics.

### B — Molecular dynamics (melt–quench validation)

- **LAMMPS** **`reax/c`**, **Δt = 0.5 fs**; **CG** minimization threshold **10⁻¹²** (reported protocol).
- **Melt–quench** from disordered **Mo–S** melts to test **crystallization** to **layered** vs incorrect packings.

### C — Quantum chemistry

- Same **VASP** **PBE-D2** settings as training reference for benchmarks tabulated in the paper.

### D — Experiments

- None.

**SI-only tables / extra panels:** **`[[2022ponomarev-venue-paper]]`**.

**Integrated MD validation:** **LAMMPS** `reax/c`, **Δt = 0.5 fs** (article); **3D** **PBC** **Mo–S** **supercells** (full **stoichiometry** and **atom** **counts** in the **PDF**); **NVT** **melt–quench** with **Nose-Hoover** **thermostat** (**temperature** **program** in **K** in *J. Phys. Chem. C*); **equilibration** and **anneal**/**quench** **stages** over **ps**–**ns**; **barostat** **N/A** if **volume** **fixed**; **hydrostatic** **pressure** **N/A** unless **NPT** **stated**; **external** **electric** **field** **N/A**; **umbrella**/**replica** **exchange** **N/A**.

## Findings

**Outcomes / mechanisms:** The new parametrization tracks **VASP** **PBE-D2** **DFT** **benchmarks** more closely than prior **ReaxFF** **sets** in the paper, and **melt–quench** runs favor **layered** **2H-MoS\(_2\)**-like **order** over **rock-salt**-like **dense** **packings** tied to older **fields**. **Comparisons:** **versus** **other** **ReaxFF** **parameter** **blocks** on **energy/force** **tables**; **not** a direct **experiment** **fit**. **Sensitivity:** **Monte** **Carlo** **fitting** **objectives** and **training** **crystal** **sets** drive the **improvement**; **melt–quench** **temperature** **schedule** selects **layered** **vs** **spurious** **minima**. **Outlook:** extension to **O, C, N, H** for **tribology**/**catalysis**-type **chemistry**. **Corpus / KB:** rank **fields** only from **tabulated** **errors** in the **version-of-record** **PDF**—this **note** does **not** copy **numerical** **RMSE** **rows**.


## Limitations

Multi-element **reactive** environments beyond the fitted **Mo–S** scope require additional training; users should validate for their **chemistry** and **conditions**. When this page is used for **retrieval** benchmarks, prefer quoting **paper_id** and **DOI** together so automation can disambiguate the corpus filename (**`Ponomarev_MoS2_NaCl_JPC_2022.pdf`**) from unrelated **NaCl** tokens in other projects.

## Reader notes (navigation)

This entry is frequently retrieved alongside other **TMD** parameterization notes in **Phase 5** reports.

## Relevance to group

Benchmark reference for **TMD** **ReaxFF** development and **crystallization** testing—useful when comparing **MoS\(_2\)** simulations across parameter generations.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.2c01075](https://doi.org/10.1021/acs.jpcc.2c01075)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
