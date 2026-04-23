---
id: paper:2017tavazza-venue-untitled
type: paper
title: "Evaluation and comparison of classical interatomic potentials through a user-friendly interactive web-interface"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - method:classical-md
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:lammps
  - keyword:validation-experiment
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1038/sdata.2016.125"
year: 2017
authors:
  - "Kamal Choudhary"
  - "Faical Yannick P. Congo"
  - "Tao Liang"
  - "Chandler Becker"
  - "Richard G. Hennig"
  - "Francesca Tavazza"
venue: "Scientific Data 4, 160125 (2017)"
pdf_sha256: "9519a2a4bf3073c337c3dde8ecf78f18a6dace7c065a904b7bdbe1a7077968a9"
pdf_path: "papers/Others/Tavazza_Interatomic_potential_comparison_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017tavazza-venue-untitled -->

## Summary

This entry records a **Scientific Data** descriptor PDF path associated with Tavazza *et al.* (journal citation **4**, **160125**, **2017**) that is **bibliographically** the same **dataset release** as [[2016choudhary-venue-untitled]] (shared DOI `10.1038/sdata.2016.125`). The project publishes a **database** and **interactive web interface** comparing **0 K** **energetics** and **elastic** **properties** for a large panel of **materials** computed with many **classical** **interatomic potentials**—including **EAM**, **MEAM**, **Tersoff**, **Stillinger–Weber**, **AIREBO**, **COMB**, and **ReaxFF**—against **Materials Project** **DFT** references and available **experimental** **elastic** data. The purpose is **benchmarking at scale**: making **force-field** errors **auditable**, **versioned**, and **comparable** across potential families rather than reporting a single **application** study.

## Methods

This **Scientific Data** descriptor (**DOI** `10.1038/sdata.2016.125`, **2017** publication metadata) is bibliographically the **same dataset release** as **[[2016choudhary-venue-untitled]]**; this slug exists because the corpus ingested a **2017 PDF filename** variant (`papers/Others/Tavazza_Interatomic_potential_comparison_2017.pdf`).

### 1 — MD application (atomistic dynamics)

The project runs **high-throughput LAMMPS** workflows at **0 K** (structure relaxation / finite-difference strain) to compute **elastic tensors** and related **mechanical** diagnostics for **many materials** × **many classical interatomic potentials** (**EAM**, **MEAM**, **Tersoff**, **Stillinger–Weber**, **AIREBO**, **COMB**, **ReaxFF**, …) compared against **Materials Project (MP) DFT** references and **experimental elastic** data where available.

- **Engine / code:** **LAMMPS** for automated **0 K** **energy/strain** evaluations (descriptor text + **[[2016choudhary-venue-untitled]]**).
- **System size & composition:** **Crystalline** **MP**-consistent **unit/supercells** per material entry in the database (exact sizes live in dataset records).
- **Boundaries / periodicity:** **3D PBC** for bulk crystal **elastic** calculations (standard MP-style setups mirrored in the pipeline).
- **Ensemble:** **N/A** — **0 K** **static** limits; no finite-**T** **NVT** production **MD** in the benchmark core described for **elastic** scoring.
- **Timestep:** **N/A** — no finite-timestep **MD** time integration in the **0 K elastic** workflow summarized here.
- **Duration / stages:** **N/A** — not a **ps/ns** trajectory study; single-point / strain-step sequences instead.
- **Thermostat:** **N/A** — **0 K** **statics**.
- **Barostat:** **N/A** — **elastic** constants from **stress–strain** or energy–strain derivatives without **NPT** dynamics.
- **Temperature:** **0 K** **static** reference comparisons (explicitly flagged as the baseline scope).
- **Pressure:** **N/A** — hydrostatic **NPT** trajectories are **not** the headline workflow for the **elastic** database.
- **Electric field:** **N/A** — not used.
- **Replica / enhanced sampling:** **N/A** — high-throughput **grid** over potentials/materials, not enhanced sampling MD.

### 2 — Force-field training

**N/A** — the publication **benchmarks** existing **parameter files**; it does **not** introduce a new **ReaxFF** fit in this descriptor.

### 3 — Static QM / DFT-only

**Materials Project DFT** supplies **reference elastic tensors / hull** data used to **score** each classical potential’s **0 K** predictions against **QM** and, where present, **experiment**.

## Findings

Across **thousands** of **calculations**, the database makes clear that **elastic** **quality** is **multi-dimensional**: a potential may reproduce one **tensor** **component** while failing on another, and **PCA** highlights **structured** correlations among errors rather than **IID** noise. For **ReaxFF**, inclusion alongside **fixed-bond** models situates **reactive** potentials in the same **comparative** ecosystem—useful for **parameterization** QA even though **ReaxFF** is often deployed in **chemically** **reactive** contexts beyond the **0 K** **elastic** **benchmarks** emphasized here. **Limitations** include the **baseline** focus on **0 K** **elastic** properties; **temperature-dependent** **phonon**/**anelastic** effects are explicitly flagged as outside the first release’s scope. **Maintainers** should treat this PDF as **bibliographically** redundant with [[2016choudhary-venue-untitled]]: the **DOI** is the **stable** identifier, while **filename** differences track **publisher** packaging or **ingest** **duplicates** without implying a **second** **dataset**. When **citing** **elastic** **comparisons** from the **web** **portal**, record the **potential** **file** **version** and **LAMMPS** **build** metadata alongside **Materials Project** **MP** **IDs**, because **elastic** **tensors** for a given **crystal** can shift slightly as **MP** **DFT** **settings** evolve across **database** **generations**. **PCA** **plots** in the **descriptor** are **pedagogical**: they summarize **correlation** structure but are not a substitute for **inspecting** **raw** **error** **vectors** on **your** **material** **of** **interest**.

## Relevance to group

Provides a **benchmarking ecosystem** adjacent to **ReaxFF** development: the same comparative mindset (QM/experiment vs empirical models) used when curating reactive force fields.

## Citations and evidence anchors

- DOI: [10.1038/sdata.2016.125](https://doi.org/10.1038/sdata.2016.125)

## Related topics

- [[reaxff-family]]
- Classical force-field repositories and validation
