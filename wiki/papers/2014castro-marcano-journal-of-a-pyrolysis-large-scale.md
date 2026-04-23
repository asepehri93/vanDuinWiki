---
id: paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale
type: paper
title: "Pyrolysis of a large-scale molecular model for Illinois no. 6 coal using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.jaap.2014.07.011"
year: 2014
authors:
  - "Fidel Castro-Marcano"
  - "Michael F. Russo Jr."
  - "Adri C. T. van Duin"
  - "Jonathan P. Mathews"
venue: "Journal of Analytical and Applied Pyrolysis 109 (2014) 79–89"
pdf_sha256: "bfcc61364bbeb8c3fd66c2504a560a29c305dae5ea4842ff988aa838fef56eaa"
pdf_path: "papers/Castro_JAAP_3246_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014castro-marcano-journal-of-a-pyrolysis-large-scale -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study uses large-scale MD to run high-temperature (2000 K) ReaxFF MD on a **>50,000 atom** molecular structural model of Illinois No. 6 coal—728 molecule diversity—over 250 ps to accelerate bond-breaking chemistry. Roughly 60% of cross-links break primarily by thermolysis in the simulation window, enabling analysis of devolatilization and structural transformation pathways for a complex organic geopolymer model relevant to utilization and emissions chemistry.

By retaining thousands of distinct molecular fragments rather than a single representative oligomer, the simulation exposes how heteroatom-bearing bridges and aliphatic links contribute unevenly to early volatile release.

## Methods

### Structural model (Illinois No. 6 coal)

- The simulation uses a previously constructed **large-scale molecular model** of **Illinois No. 6 coal** composed of **728 chemically diverse molecules** (abstract).

### Reactive MD protocol (ReaxFF)

- **ReaxFF** **reactive MD** is run on a **>50,000 atom** assembly at **2000 K** for **250 ps** so that bond-breaking chemistry occurs within accessible nanosecond-scale wall times (abstract).
- The authors continue the trajectory until **~60%** of **cross-links** are disrupted, **primarily by thermolysis**, enabling analysis of **fragment** populations and **heteroatom**-mediated scission (abstract).

### Sulfur-free control

- The **ReaxFF** run is **repeated on a sulfur-free** variant of the model to isolate how **organic sulfur** forms influence **gas/tar** generation rates (abstract).

### Analysis

- Post-trajectory analysis tracks **molecular-weight distributions**, **sulfur form** populations (**aliphatic vs thiophenic**), **heterocycle** decomposition extents (**pyrrolic**, **thiophenic**, **furanic** rings), and qualitative agreement of **tar** motifs with literature (abstract).

### 1 — MD application (ReaxFF reactive MD)

- **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** as stated in the abstract; **specific software** (e.g. LAMMPS) and integrator labels are **N/A in the pages 1–2 extract**—see the **JAAP** article body at `pdf_path`.
- **System size & composition:** **>50,000 atoms**; **728** diverse molecules representing **Illinois No. 6 coal** (abstract; `normalized/extracts/2014castro-marcano-journal-of-a-pyrolysis-large-scale_p1-2.txt`).
- **Boundaries / periodicity:** **N/A —** not stated in the indexed extract; confirm **PBC** and cell vectors in the PDF.
- **Ensemble:** **N/A —** not stated in the indexed extract (typical cook-off framing is often **NVT**—confirm in PDF).
- **Timestep:** **N/A —** not stated in the indexed extract.
- **Duration / stages:** **250 ps** at **2000 K**, run until **~60%** of **cross-links** are disrupted **primarily by thermolysis** (abstract).
- **Thermostat / barostat:** **N/A —** not stated in the indexed extract.
- **Temperature:** isothermal **2000 K** for the pyrolysis segment summarized above (abstract).
- **Pressure / electric field / enhanced sampling:** **N/A —** not invoked in the abstract-level protocol summary.

### 2 — Force-field training

**N/A —** the abstract describes **application** of **ReaxFF** to a large coal model, not a new parameterization in the indexed excerpt (parent parameterization should be cited in the article introduction—see PDF).

### 3 — Static QM / DFT-only

**N/A —** central claims are from **ReaxFF MD** trajectories in the abstract framing.

## Findings

### 1 — Outcomes and mechanisms

- **Cross-link disruption:** roughly **60%** of **cross-links** break within the simulated window, dominated by **thermolysis**, enabling detailed inspection of **devolatilization** chemistry (abstract).
- **Initiation chemistry:** pyrolysis is reported to begin via **hydroxyl release**, **hydroaromatic dehydrogenation**, and cleavage of **heteroatom-bearing cross-links** (abstract).
- **Major products** include **H₂**, **CH\(_4\)**, **C\(_2\)H\(_4\)**, **C\(_2\)H\(_2\)**, **H\(_2\)CO**, **ethynol**, **alkylphenols**, **alkylnaphthalenes**, and **alkylnaphthols**, described as **consistent with experiments** at a qualitative level (abstract).
- **Heteroatoms:** **S- and O-bearing bridges** degrade faster than **alkyl** linkages; **aliphatic sulfur** decomposes faster than **thiophenic sulfur** in the authors’ analysis (abstract).
- **Heterocycles:** decomposition extents reported as **~57% pyrrolic**, **~47% thiophenic**, and **~29% furanic** motifs (abstract).
- **Sulfur role:** the **sulfur-containing** model generates **inorganic gases** and **tars** faster than the **sulfur-free** counterpart; **C–S** bonds are found **weaker** than analogous **C–C** bonds, increasing fragmentation (abstract).

### 2 — Comparisons

- **Volatile and tar motifs** are described as **qualitatively consistent with experimental data** and **literature** expectations for **sulfur forms** (**aliphatic** vs **thiophenic**) in the abstract.

### 3 — Sensitivity and design levers

- **Sulfur-free vs sulfur-bearing models** isolate how **organic sulfur** accelerates **gas/tar** generation in this structural representation (abstract).

### 4 — Limitations and outlook (as authored in abstract framing)

- The abstract emphasizes **high temperature** (**2000 K**) to access chemistry within **250 ps**; **laboratory heating rates** and **long-time** secondary chemistry are outside this window (see **## Limitations**).

### 5 — Corpus / KB honesty

- **Timestep**, **thermostat**, and **nonbond settings** are **not** recoverable from the checked-in **`_p1–2` extract**; use **`pdf_path`** for the full **JAAP** protocol narrative.

## Limitations

- Short simulated time vs laboratory heating rates; temperatures are elevated to access reactions within nanoseconds.
- Model fidelity depends on the underlying structural model and force-field transferability for sulfur/nitrogen/oxygen moieties present in coal.

## Relevance to group

Flagship **large-system ReaxFF pyrolysis** study tying geochemical/energy engineering (EMS Energy Institute) to reactive MD capabilities.

## Citations and evidence anchors

- DOI: [10.1016/j.jaap.2014.07.011](https://doi.org/10.1016/j.jaap.2014.07.011)
- Abstract: `normalized/extracts/2014castro-marcano-journal-of-a-pyrolysis-large-scale_p1-2.txt`

## Reader notes (navigation)

- **Cluster:** [[theme-pyrolysis-combustion-organics]]; cross-link to [[graphene-nanocarbon]] for sp² carbon themes.  
- **Frozen eval:** PYR1 gold in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
- Coal devolatilization and reactive MD at mesoscale atom counts
- ReaxFF for complex CHONS organics
