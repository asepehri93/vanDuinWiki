---
id: paper:2014cheng-venue-ja5037258
type: paper
title: "Adaptive accelerated ReaxFF reactive dynamics with validation from simulating hydrogen combustion"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:methods-software
  - domain:reaxff-lineage
  - method:reaxff
  - task:method-development
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:method-development
  - keyword:combustion
  - keyword:reactive-md
  - keyword:qm-training-data
source_refs: []
doi: "10.1021/ja5037258"
year: 2014
authors:
  - "Tao Cheng"
  - "Andrés Jaramillo-Botero"
  - "William A. Goddard III"
  - "Huai Sun"
venue: "J. Am. Chem. Soc."
pdf_sha256: "a1197d04028bf07abe1c63ef06cf2415bb9cb78a4dc344cb9b3521619f7f8369"
pdf_path: "papers/ReaxFF_others/Cheng_Jaramillo_JACS_BondBoost.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014cheng-venue-ja5037258 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Acceleration factors and temperature endpoints must be taken from the article.

## Summary

The paper introduces **adaptive accelerated ReaxFF reactive dynamics (aARRDyn)** using a **bond boost (BB)** that **targets** likely **reactive** events while leveraging **ReaxFF** bond-order and **coordination** concepts to **avoid** unphysical boosts. **H₂ combustion** serves as validation: **mechanistic sequences** and **kinetics** at **2498 K** are compared **with** vs **without** boosting. The abstract then claims **good agreement** across a **broad temperature window** down to **ignition-relevant** **798 K**, with **enormous** wall-clock **speedups** (e.g., **half-reaction** time **~538 s** physical vs **~1289 ps** simulated at **798 K** in their example). Because **ReaxFF-COH2008** mishandles some **oxonium** intermediates, the authors report **reoptimization** to **QM**, yielding **ReaxFF-OH2014** used in the study.

## Methods

### Accelerated dynamics framework (aARRDyn)

- **Adaptive accelerated ReaxFF reactive dynamics (aARRDyn)** employs an **adaptive bond boost (BB)** that uses **ReaxFF bond orders** and **coordination** metrics to **restrict** boosting to **likely reactive** pairs, avoiding globally unphysical acceleration (abstract).

### Brute-force reference trajectories

- **Validation** compares **unaccelerated (brute-force) ReaxFF reactive MD** to **aARRDyn** for **H\(_2\)/O\(_2\)** combustion at **2498 K**, checking **mechanistic sequences** and **kinetics** (abstract).

### Force-field revision for oxygenated intermediates

- Legacy **ReaxFF-COH2008** is reported to mishandle certain **oxonium** intermediates; the authors **reoptimize** **O/H** parameters against **QM** data, producing **ReaxFF-OH2014** used in the accelerated and reference runs (abstract).

### Broader temperature testing

- Additional comparisons span **798–2998 K** to probe **ignition-relevant** low-temperature behavior versus high-temperature chemistry (abstract).

### 1 — MD application (ReaxFF reactive MD)

- **Engine / code:** **Reactive MD** with **ReaxFF** as implemented for these benchmarks; **LAMMPS**-class integration, **timestep**, and **thermostat** choices are in **JACS** Methods/SI (`pdf_path`)—the introduction quotes **1 fs** as a representative **RMD** step for rare-event cost arguments (`normalized/extracts/2014cheng-venue-ja5037258_p1-2.txt`).
- **System size & composition:** **H\(_2\)/O\(_2\)** combustion cells for **BF-RMD** vs **aARRDyn** benchmarks; **atom** counts and stoichiometries are specified in the article/SI (abstract points to detailed **H\(_2\)** oxidation validation).
- **Boundaries / duration / thermostat / barostat:** **N/A in the indexed abstract** for full **PBC** vectors, production segment lengths, and thermostat labels—see **`pdf_path`**.
- **Ensemble:** **NVT** is the common framing for these **gas-phase** **ReaxFF** combustion benchmarks; confirm the exact ensemble statement in **JACS** Methods.
- **Timestep:** **1 fs** is discussed in the introduction as a representative **RMD** integration step for rare-event cost arguments (extract).
- **Duration / stages:** illustrative **aARRDyn** run at **798 K** reports **~1289 ps** of accelerated dynamics for the quoted half-reaction benchmark; **2498 K** **BF-RMD** reference segments are defined in the article (abstract).
- **Thermostat:** **N/A in the indexed abstract**—see **`pdf_path`** Methods/SI.
- **Temperature:** **2498 K** brute-force reference window; extended **798–2998 K** comparisons including **798 K** ignition-relevant case (abstract).
- **Barostat / pressure / electric field / umbrella or metadynamics:** **N/A —** not stated in the abstract excerpt used here; confirm in PDF/SI.

### 2 — Force-field training (ReaxFF-OH2014)

- **Parent FF / elements:** starts from **ReaxFF-COH2008**; authors report inaccuracies for **H\(_3\)O⁺**-class intermediates in combustion sequences (abstract).
- **QM reference / training target:** **reoptimization** of **O/H** parameters to **QM** data, yielding **ReaxFF-OH2014** used in subsequent **RMD** (abstract); full **DFT** level and basis are in the article/SI.
- **Optimization workflow:** **N/A in the abstract line** beyond “reoptimized the fit to a quantum mechanics (QM) level” (abstract)—see **Methods**/**SI** for algorithm details.
- **Reference data for validation:** **Brute-force RMD** (**BF-RMD**) at **2498 K** supplies the reference **mechanistic sequences** and **kinetics** for **H\(_2\)** oxidation (abstract).

### 3 — Method development (adaptive bond boost)

- **aARRDyn** couples an **adaptive bond boost** to **ReaxFF** bond-order and coordination metrics so boosts track **likely** reactive pairs (abstract).

## Findings

### 1 — Outcomes and mechanisms

- At **2498 K**, **aARRDyn** reproduces the **BF-RMD** **mechanistic sequence** and **rate-like behavior** for the **H₂ oxidation** validation case described in the abstract.
- Across **798–2998 K**, **aARRDyn** tracks **BF-RMD**-based **extrapolations** for **reaction rates** in their tests, enabling **ignition-relevant** **798 K** sampling that would be **intractable** brute-force.
- For **798 K**, the manuscript quotes a **half-reaction time ~538 s** (physical) realized in **~1289 ps** of **accelerated** dynamics, i.e. a **~4.2×10¹¹×** wall-time reduction vs naive integration for that illustrative benchmark.

### 2 — Comparisons

- **aARRDyn** vs **BF-RMD** at **2498 K** and extrapolated **BF-RMD**-consistent rates across **798–2998 K** (abstract).

### 3 — Sensitivity

- **Temperature** dependence of **H\(_2\)** oxidation **rates** and **mechanistic** detail across the **798–2998 K** window (abstract).

### 4 — Limitations / outlook

- **Boost** correctness depends on **parameterization** and **reaction** coverage; new chemistries require **revalidation** (**## Limitations**).

### 5 — Corpus / KB honesty

- Full **protocol tables** and **SI** diagnostics are authoritative over this abstract-grounded summary (`pdf_path`).

## Limitations

- **Boost** **correctness** depends on **parameterization** and **reaction** **space**; **new chemistries** require **revalidation**.

## Relevance to group

**Method** reference for **accelerated** **ReaxFF** **RMD** adjacent to **combustion** and **kinetics** workflows.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/ja5037258` (`papers/ReaxFF_others/Cheng_Jaramillo_JACS_BondBoost.pdf`).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
