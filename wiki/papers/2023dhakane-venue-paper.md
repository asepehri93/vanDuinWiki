---
id: paper:2023dhakane-venue-paper
type: paper
title: "A Graph Dynamical neural network approach for decoding dynamical states in ferroelectrics (galley PDF)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:ml-atomistic
  - method:reaxff
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reactive-md
  - keyword:machine-learning-potential
candidate_tags: []
source_refs: []
doi: "10.1016/j.cartre.2023.100264"
year: 2023
authors:
  - "Abhijeet Dhakane"
venue: "Carbon Trends (galley / corrected proof in corpus)"
pdf_sha256: "2ad87f9a1a6b9a119c9271eb7d27b2c43c7f49e5192f2e7f75855633b8f70e36"
pdf_path: "papers/Dhakane_Ganesh_CarbonTrends_GraphNN_BaTiO3_2023_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023dhakane-venue-paper -->

## Summary

This slug records a **galley or corrected proof** PDF byte-identical ingest for the *Carbon Trends* article with DOI `10.1016/j.cartre.2023.100264`. Galley files often differ from the final journal XML in line breaks, figure resolution, and occasionally wording; for authoritative statements, readers should use the version-of-record wiki page **`[[2023dhakane-carbon-trend-graph-dynamical]]`**, which points at the non-galley PDF path in this corpus when available. Scientifically, the publication combines large-scale ReaxFF molecular dynamics of pristine and oxygen-vacancy-containing barium titanate with graph-based dynamical neural networks and Markov-state or Koopman-style analyses on local polarization features, aiming to separate slow and fast relaxation modes at domain walls and defects. The work sits at the intersection of reactive ferroelectric MD, machine learning, and reduced dynamical models for complex oxide interfaces. Ferroelectric domain walls are inherently heterogeneous; combining reactive trajectories with graph dynamical models is one route to compress wall motion into interpretable slow modes for device-scale reasoning.

## Methods

### Corpus role (duplicate ingest / non-primary PDF)

This slug tracks **`papers/Dhakane_Ganesh_CarbonTrends_GraphNN_BaTiO3_2023_galley.pdf`** bytes separately from the primary ingest for **hash** and **layout** provenance. It is **not** the canonical **Methods** source.

### Where the protocols live

**LAMMPS** system sizes (~**10⁴–10⁵** atoms), **PyTorch** **graph** model definitions, **thermostat**/**timestep** choices, and **local polarization** featurization are documented on **`[[2023dhakane-carbon-trend-graph-dynamical]]`** and the **peer-reviewed** PDF for **DOI** `10.1016/j.cartre.2023.100264`.

For retrieval-aligned detail (mirroring the **VOR** page): reactive trajectories use **ReaxFF** for **BaTiO₃** with **oxygen vacancies**, building on the authors’ prior **PCCP 2019** parametrization; cells reach roughly **tens of thousands** of atoms with **pristine** and **defective** **domain-wall** setups. **Local polarization** vectors distinguish **bulk-like**, **wall**, and **defect-adjacent** environments, then feed **graph dynamical networks** and **Koopman/Markov** analyses implemented in **PyTorch** to separate **fast** vs **slow** collective modes.

### MD application (N/A for duplicate slug)

**N/A** — this **galley** duplicate is **not** the canonical **Methods** source. **MD** protocol (engine, **LAMMPS** **ReaxFF** settings, **PBC**, **NVT/NPT**, **temperature** setpoints (e.g. **300 K** if used in the VOR), **ps/ns** run lengths, **barostat**, **field/wall strain**, **enhanced sampling**): use **`[[2023dhakane-carbon-trend-graph-dynamical]]`** and the **version-of-record** **PDF** for **DOI** `10.1016/j.cartre.2023.100264`.

## Findings

### Substance mirrored from the VOR page

**Oxygen vacancies** create **localized slow dipole relaxation** and **defect dipoles** that **impede** **domain-wall** motion; **wall segments** can differ by **~order-of-magnitude** **effective** dynamics in the **ReaxFF** + **graph-dynamical** analysis. The **VOR** discussion also highlights **spatial heterogeneity** along **rough** walls and cites **~10×** spreads between **fast** wall segments and **slow**, **high-curvature** segments relative to **mean** wall behavior—use **`[[2023dhakane-carbon-trend-graph-dynamical]]`** for the full quantitative discussion.

### What to cite for science

Use **`[[2023dhakane-carbon-trend-graph-dynamical]]`** (or the **VOR** PDF) for **figures**, **numbers**, and **quantitative** claims—this **galley** page exists for **manifest** alignment and **deduplication** by **DOI**. **Corpus honesty:** **duplicate** **PDF**; **sensitivity** to **temperature/field/strain** is **not** re-derived on this page.

## Limitations

Galley pagination does not match the final article; cite the DOI and primary wiki slug for quotations. ReaxFF accuracy for ferroelectric oxides is context-dependent and should be cross-checked against experiment for quantitative barriers. Downstream chunk builders should key embeddings to the VOR markdown body, not duplicate galley boilerplate. Graph-neural sections on the primary page list tensor shapes omitted here.

## Relevance to group

Duplicate ingest path for Dhakane–Ganesh ReaxFF plus ML ferroelectric work with van Duin-network co-authorship.

## Citations and evidence anchors

- DOI: [10.1016/j.cartre.2023.100264](https://doi.org/10.1016/j.cartre.2023.100264)

## Reader notes (navigation)

- Version-of-record page: [[2023dhakane-carbon-trend-graph-dynamical]]  
- Theme: [[theme-ferroelectrics-polar-oxides]], [[reaxff-family]]

## Related topics

- [[2023dhakane-carbon-trend-graph-dynamical]]
