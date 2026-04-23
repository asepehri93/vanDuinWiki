---
id: paper:2012khalilov-venue-c2nr32387g
type: paper
title: "Reactive molecular dynamics simulations on SiO2-coated ultra-small Si nanowires"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:metallic-systems
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1039/c2nr32387g"
year: 2013
authors:
  - "Umedjon Khalilov"
  - "Geoffrey Pourtois"
  - "Annemie Bogaerts"
  - "Adri C. T. van Duin"
  - "Erik C. Neyts"
venue: "Nanoscale 5, 719–725 (2013)"
pdf_sha256: "8bbe9d4d6553b3d183146d34333fe6ae6394dd2cb6f2c1c15731f0ade4089ecf"
pdf_path: "papers/Khalilov_Nanoscale-2013-5-719.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012khalilov-venue-c2nr32387g -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Ultra-small Si nanowires (Si-NWs)** with **oxide shells** are important for **quantum-confined** **Si** optoelectronics, but **dry oxidation** pathways and **self-limiting** thicknesses are hard to control at the **nanometer** scale. This study uses **ReaxFF MD** to follow **oxidation** of **(100)** **Si-NWs** with initial diameters **1.0–3.0 nm** from **300–1200 K**. Two **temperature-dependent** regimes are reported: at **high T**, **ultrathin SiO\(_2\)** **nanowires** (fully oxidized structures in the classification used in the paper); at **low T**, **Si core** | **ultrathin SiO\(_2\)** **core–shell** morphologies. The **crossover temperature** **decreases linearly** with **increasing curvature** (smaller diameter). **Interfacial stress** drives **self-limiting oxidation**, depending on **initial radius** and **temperature**—linking mechanics to **process windows** for **morphology control**.

## Methods

### Force-field training (ReaxFF)

**Parent FF / elements:** **ReaxFF** with the **Si/SiO\(_2\)** parameter set employed by **Buehler et al.** (as cited in the article), trained extensively against **Si** and **SiO\(_2\)** phases. **SiO\(_x\)** suboxides with **\(x < 2\)** were not explicit training targets; the authors note prior **planar Si\|SiO\(_2\)** work still gave reasonable agreement with **DFT** and experiment for suboxide species.

**QM reference, training set, optimization, reference data:** **N/A —** this publication applies an existing **Si/SiO\(_2\)** **ReaxFF** parametrization to nanowire oxidation rather than reporting a new fit workflow; any additional QM benchmarks are in the cited **ReaxFF** references (see **`pdf_path`**).

### MD application (atomistic oxidation)

**Engine / code:** **Reactive molecular dynamics** with **ReaxFF** (indexed excerpt and abstract); **N/A —** standalone MD program name not recovered from `normalized/extracts/2012khalilov-venue-c2nr32387g_p1-2.txt`—confirm in **`pdf_path`**.

**System size & composition:** **(100)** **Si nanowires** with initial diameters **1.0–3.0 nm** under **dry thermal oxidation** in the **300–1200 K** window; the indexed text describes diameter via averaged radial positions of **surface atoms** (exact stoichiometries and gas-phase **O\(_2\)** loading per case are in **`pdf_path`**).

**Boundaries / periodicity:** **Periodic boundary conditions** along the **wire (z) axis** with a **1 nm** unit-cell repeat to mimic an infinitely long nanowire (Computational details in the article; excerpt p. 2).

**Ensemble:** **N/A —** **NVE/NVT/NPT** label not recovered from the indexed excerpt (verify **`pdf_path`**).

**Timestep:** **N/A —** not recovered from the indexed excerpt (verify **`pdf_path`**).

**Duration / stages:** **N/A —** equilibration/production schedule not recovered from the indexed excerpt; reactive trajectories are discussed on **ps** accessible timescales in line with typical **ReaxFF** oxidation surveys—verify staging in **`pdf_path`**.

**Thermostat:** **N/A —** thermostat type and coupling constants not recovered from the indexed excerpt (verify **`pdf_path`**).

**Barostat / pressure control:** **N/A —** **NPT** barostat not stated in the indexed excerpt for these nanowire runs.

**Temperature:** **300–1200 K** oxidation window; individual production temperatures follow the paper’s parameter sweep.

**Pressure / stress:** **Interfacial stress** is analyzed in the article as part of the self-limiting oxidation argument; **N/A —** externally imposed hydrostatic pressure control is not described in the indexed excerpt.

**Electric field:** **N/A —** not used for the oxidation MD in the indexed excerpt.

**Replica / enhanced sampling:** **N/A —** not indicated in the indexed excerpt.

### Static QM / DFT-only

**N/A —** central results are **ReaxFF MD** on nanowires, not a standalone static **DFT** study (DFT appears as validation context in the **ReaxFF** literature cited by the authors).

## Findings

The simulations report **two temperature regimes** for **ultra-small** wires: **high temperature** yields **fully oxidized ultrathin SiO₂ nanowire**-like products (terminology as used in the paper), whereas **lower temperature** yields **Si core | ultrathin SiO₂ shell** **core–shell** morphologies. The **crossover temperature** **decreases approximately linearly** with increasing **curvature** (smaller diameter), linking **nanoscale** effects to **process windows**. **Interfacial stress** is identified as driving **self-limiting oxidation**, depending on **initial Si-NW radius** and **oxidation temperature**, consistent with stress-gated oxidation arguments discussed in the introduction. The work positions **ReaxFF** as an atomistic bridge between **mechanics** and **oxidation** for **sub-3 nm** **(100)** Si wires under **dry** conditions.

## Limitations

- **1 nm** axial periodicity approximates an **infinitely long** wire; real wires have **length**, **facets**, and **defects** not fully captured.
- **Dry** oxidation only; **wet** chemistry pathways differ.

## Relevance to group

**van Duin-group** coauthored **ReaxFF** on **Si oxidation** at **nanowire** scale—ties to **electronics** **Si/SiO\(_2\)** processing literature.

## Citations and evidence anchors

- DOI: [10.1039/c2nr32387g](https://doi.org/10.1039/c2nr32387g)
- Text-aligned pointer: `normalized/extracts/2012khalilov-venue-c2nr32387g_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
- Silicon nanowire oxidation
