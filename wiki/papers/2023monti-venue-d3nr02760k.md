---
id: paper:2023monti-venue-d3nr02760k
type: paper
title: "Disclosing gate-opening/closing events inside a flexible metal–organic framework loaded with CO2 by reactive and essential dynamics"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:reactive-md
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1039/d3nr02760k"
year: 2023
authors:
  - "Susanna Monti"
  - "Cheherazade Trouki"
  - "Giovanni Barcaro"
venue: "Nanoscale"
pdf_sha256: "90741f48c62dab21b06febd2f440dcbf5c4b116bed15079be890420dc402d706"
pdf_path: "papers/ReaxFF_others/Monti_MOF_Nanoscale_2023.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023monti-venue-d3nr02760k -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *Nanoscale* article identified by `doi`, `title`, and `pdf_path`.

## Summary

**Reactive MD** of **CO\(_2\)** in a **flexible MOF** is combined with **principal component analysis (PCA)** and **essential dynamics** to resolve **gate opening/closing**, guest **diffusion**, and **linker motions** at **tens-of-nanometer** supercell scale. The study targets a thermally stable, flexible MOF where **CO\(_2\)** loading couples to **pore gating** and **linker rearrangements**. The authors use a **ReaxFF** parametrization suited to the **inorganic–organic** framework with **PCA** of trajectory variance to highlight collective motions that modulate **CO\(_2\)** storage, adsorption, and diffusion. **Large** **supercells** are used deliberately so **diffusive** **CO\(_2\)** **motion** and **framework** **flexibility** are not **artificially** **suppressed** by **periodic-image** **constraints** typical of **small** **unit-cell** **DFT** **studies** of the same **material** class.

## Methods

### ReaxFF MD (B)

Large-cell **ReaxFF** for **flexible MOF** + **CO\(_2\)**, enabling **guest–framework** bond rearrangements (**metal–organic** chemistry per parameterization).

### Supercell scale

**Tens-of-nm** cells to reduce **finite-size** bias on **diffusion**/**flexibility** vs small **DFT** cells.

### Trajectory reduction

**PCA** + **essential dynamics** isolate **gate** modes, **linker** motions, and correlated **CO\(_2\)** transport along channels (**ESI** for histograms/barrier checks).

The **Nanoscale** narrative also contrasts this **large-cell** **ReaxFF** approach with **static** **DFT** **adsorption** snapshots: **flexible** **MOFs** can undergo **concerted** **linker** motions that **DFT** **unit cells** may **constrain** away, so **dynamic** **ReaxFF** trajectories are used to **capture** **gating** as a **trajectory ensemble** property rather than a single **minimum-energy** **path**.

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** (or equivalent as stated) with a **MOF**-compatible **ReaxFF** for **framework** + **CO\(_2\)**. **System & composition:** **tens-of-nm** **supercells** with **guest** **CO\(_2\)** and a **flexible** **MOF** (see article for composition and loading). **Boundaries / periodicity:** **3D PBC** for large **supercells** to sample **diffusion** and **gating**. **Ensemble, timestep, thermostat, barostat, production time, temperature, pressure:** **MOF**+**CO\(_2\)** **ReaxFF** **NVT**/**NPT**-class **sampling** in **tens-of-nm** **cells** uses **fs** **timesteps** and **ns** **durations** as tabulated, with **bar**-scale or **NPT** **isotropic** **pressures** when the **framework** is **pressurized**; **N/A** on this page for the full **NVT**/**NPT** **narrative** (see *Nanoscale* and **ESI**). **Electric field, shear, shock:** **N/A** here. **Coulomb / ReaxFF QEq:** as in the **parameterization**. **Post-processing:** **PCA** and **essential dynamics** on **trajectories** (not **umbrella** **MD**).

### 2 — Force-field training

**N/A** — the study **deploys** a **ReaxFF** line for **inorganic–organic** **framework** **chemistry**; training scope is in the **primary** **paper**.

### 3 — Static QM

**N/A** — **DFT** appears as a **contrast** for **static** **snapshots**; **dynamics** are **ReaxFF**-based.

## Findings

### Gating and transport

Reports **gate open/close** events, **CO\(_2\)** coordination at **open metal** sites, **sequential diffusion**, and **linker** motions coupling to **local** **CO\(_2\)** flux.

### Interpretability layer

**PCA** compresses variance into **collective coordinates** aligned with **pore aperture** changes—useful for connecting **dynamic** **ReaxFF** to **static** **barrier** pictures from **QM**.

**Compared** to **DFT** **minima**, **gating** **dynamics** in **NVT** **trajectories** depend on **temperature** and **CO\(_2\)** **fugacity**; **sensitivity** of **local** **flux** to **pore** **dilation** is the **reaction**-**coordination** **insight** of the **paper**—a **ReaxFF**-level **kinetic** **uncertainty** remains, as does **rare**-**event** **sampling** **limitation** in **shorter** **ns** **runs**; **outlook** **sections** in *Nanoscale* and **ESI** discuss **hysteresis** **more** than this **note** can **summarize**—**confirm** on **version-of-record** `pdf_path`.

## Limitations

ReaxFF accuracy depends on the training set for this MOF chemistry; long timescales of rare gating events may still undersample within affordable trajectories. **Rare-event** **bias**: **gate** **opening** may require **microsecond** **scales** while **published** **trajectories** are **shorter**, so **qualitative** **mechanism** **maps** should be valued over **single** **barrier** **numbers** unless **converged** **sampling** is demonstrated.

## Relevance to group

Included in **ReaxFF_others** corpus; demonstrates **ReaxFF + enhanced trajectory analysis** for **MOF–CO\(_2\)** systems.

## Citations and evidence anchors

- DOI: [10.1039/d3nr02760k](https://doi.org/10.1039/d3nr02760k)

## Reader notes (navigation)

- **Flexible** **MOF** + **CO\(_2\)**: pairs with [[theme-reactive-md-corpus]] for **reactive** **FF** **method** context; **PCA** is a **post-processing** **layer** on **ReaxFF** **trajectories**, not a separate **QM** **method**.

## Related topics

- [[reaxff-family]]
