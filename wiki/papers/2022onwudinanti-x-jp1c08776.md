---
id: paper:2022onwudinanti-x-jp1c08776
type: paper
title: "A ReaxFF Molecular Dynamics Study of Hydrogen Diffusion in Ruthenium—The Role of Grain Boundaries"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - method:reaxff
  - material:alloy-bulk
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.1c08776"
year: 2022
authors:
  - "Chidozie Onwudinanti"
  - "Mike Pols"
  - "Geert Brocks"
  - "Vianney Koelman"
  - "Adri C. T. van Duin"
  - "Thomas Morgan"
  - "Shuxia Tao"
venue: "J. Phys. Chem. C"
pdf_sha256: "f89c7a9b246240c1533b2ef00dc4c0baf28735ce3539d23dd3f59196bbc7a25d"
pdf_path: "papers/Onwudinanti_RuH_JPCC_2022_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2022onwudinanti-x-jp1c08776 -->

!!! abstract "Scope"

New ReaxFF for Ru/H with MD of hydrogen in pristine hcp Ru versus Σ7 tilt and twist grain boundaries—GBs trap H and redirect diffusion anisotropically, informing EUV mirror capping layers.

## Summary

Ruthenium caps on EUV multilayer mirrors must limit hydrogen uptake that drives blistering. Prior DFT indicated low bulk H solubility; this work parametrizes a ReaxFF model against quantum data for Ru/H and runs reactive MD on nanocrystalline motifs to isolate grain-boundary effects on H transport.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** ReaxFF molecular dynamics was run with the AMS2020 reactive MD package; trajectory analysis (including hydrogen MSD) used MDAnalysis.
- **System size and composition:** Three Ru/H cells were simulated: pristine hcp Ru (40.6 x 37.5 x 34.3 A, 3840 Ru + 40 H), Sigma7 tilt GB (27.0 x 46.8 x 42.8 A, 3690 Ru + 40 H), and Sigma7 twist GB (36.1 x 36.1 x 34.8 A, 2800 Ru + 28 H).
- **Boundaries / periodicity:** 3D periodic boundary conditions for all cells.
- **Ensemble:** Pre-equilibration in NpT, then diffusion production in NVT.
- **Timestep:** 0.25 fs (velocity-Verlet integration).
- **Duration / stages:** At least 0.1 ns pre-equilibration before NVT diffusion sampling; configurations saved every 1000 steps.
- **Thermostat:** Nose-Hoover chain thermostat (chain length 10; damping 25 fs).
- **Barostat:** Berendsen barostat during NpT pre-equilibration.
- **Temperature:** Maxwell-Boltzmann initialization at target temperature; 700 K is explicitly shown in GB snapshots.
- **Pressure:** 1 atm during NpT pre-equilibration; N/A for pressure control in the NVT diffusion stage.
- **Electric field:** N/A - no external field protocol reported.
- **Replica / enhanced sampling:** N/A - no umbrella, metadynamics, or replica exchange reported.

### 2 — Force-field training (Ru/H ReaxFF)

- **Parent FF / elements:** New Ru/H ReaxFF parameterization targeting ruthenium with dissolved/interstitial hydrogen.
- **QM reference:** BAND calculations using a PBE + TS + SOC + ZORA style reference level as described in the paper/SI.
- **Training set:** Bulk hcp Ru structural and elastic targets (a, c/a, cell volume, bulk modulus) plus hydrogen site energetics in Ru (tetrahedral and octahedral environments).
- **Optimization:** ReaxFF parameter fitting workflow is reported in the article and SI; exact optimizer weighting details are not fully expanded in this page text.
- **Reference data used:** DFT-derived quantities above were used for fit/validation, and the paper compares H site energetics to earlier reported values.

### 3 — Experiments

- **EUV** **lithography** is **cited** **as** **motivation**; **N/A** **in-house** **H**-**in**-**Ru** **measurement** in this **computational** **paper** **(indirect** **H**-**in**-**Y** **H**-**proxy** only in **ref** [13] **cited** **in** the **intro** per **JPCC** text)**.

## Findings

### 1 — Outcomes and mechanisms

The simulations indicate that Sigma7 tilt and twist grain boundaries in Ru are hydrogen-favoring regions relative to pristine hcp Ru. Hydrogen diffusion is anisotropic in GB-containing models: transport along the boundary plane is faster, while crossing the boundary plane is more hindered, which produces effective trapping/accumulation at the boundary environment.

### 2 — Comparisons

Compared with the pristine Ru cell, both GB models show stronger hydrogen localization at interfacial regions and altered diffusion pathways. The fitted Ru/H ReaxFF also reproduces key Ru bulk structural/mechanical quantities reported in the study benchmark set, supporting use of the potential for this GB-versus-bulk transport comparison.

### 3 — Sensitivity and design levers

Microstructure is the key design lever highlighted by this paper: introducing specific GB motifs changes both preferred hydrogen residence sites and directional mobility. The article framing links this to Ru cap performance in EUV systems, where reducing adverse hydrogen uptake/transport pathways is a practical objective.

### 4 — Limitations and outlook (as authored)

The reported conclusions are based on selected Sigma7 GB archetypes rather than a full grain-boundary character distribution. The paper positions the model as a step toward broader microstructure-aware assessments, not as a final map of all Ru film textures and service conditions.

### 5 — Corpus / KB honesty

This page is grounded in the on-file DOI-matched galley PDF plus linked SI context. It supports claims about relative GB-vs-bulk hydrogen behavior and anisotropic diffusion trends in the modeled cells; it does not establish universal trapping strengths for all Ru grain-boundary types or direct one-to-one operating-pressure equivalence for deployed EUV mirror stacks.

## Limitations

The study samples specific Σ7 boundaries; other misorientation distributions could show different trapping strengths. **Ru** **microstructure** in **EUV** **mirrors** includes **texture**, **grain-size** **gradients**, and **interlayers** not represented in the **idealized** **bicrystal** **cells** used to isolate **GB** **H** **partitioning**. **Hydrogen** **chemical** **potential** in **service** may differ from **simulation** **reservoirs**; map **MD** **chemical** **potentials** cautiously to **operating** **partial** **pressures**. **Ru/H** **parameter** **sets** should be versioned alongside the **AMS**/**ReaxFF** **or** **LAMMPS** **ReaxFF** **build** used in **downstream** **runs** (this **article** **states** **AMS2020** for the **reported** **MD**).

## Relevance to group

Co-authored ReaxFF development and application for hydrogen in technologically relevant Ru films.

## Reader notes (navigation)

- PDF on file is labeled galley in manifest; science matches the DOI version. **Corpus catalog (galley-style PDF):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) for general proof/galley handling.
- [[reaxff-family]]

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.1c08776](https://doi.org/10.1021/acs.jpcc.1c08776)

## Related topics

- [[reaxff-family]]
