---
id: paper:2012castro-marcano-combustion-a-combustion-illinois
type: paper
title: "Combustion of an Illinois No. 6 coal char simulated using an atomistic char representation and the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:thermal-decomposition
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.combustflame.2011.10.022"
year: 2012
authors:
  - "Fidel Castro-Marcano"
  - "Amar M. Kamat"
  - "Michael F. Russo Jr."
  - "Adri C. T. van Duin"
  - "Jonathan P. Mathews"
venue: "Combustion and Flame 159, 1272–1285 (2012)"
pdf_sha256: "31ec3343a0bf9156a7fe121bf555a2b2e6f74b25153aaa0cc6766169cd8aa5eb"
pdf_path: "papers/Castro_CombFlame_coal_2012.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012castro-marcano-combustion-a-combustion-illinois -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Coal char** is a **disordered polyaromatic** solid whose **combustion** chemistry is hard to probe atomistically. This work builds a **devolatilized Illinois No. 6** char **atomistic** model using **Fringe3D** (from **HRTEM** lattice-fringe statistics) plus **Perl** scripts to place **heteroatoms** and **aliphatic** motifs with reduced investigator bias, constrained by **elemental** and **NMR** literature targets. **ReaxFF** for **hydrocarbon combustion** drives **reactive MD** at very high temperature (**3000–4000 K**) under **stoichiometric**, **fuel-lean**, and **fuel-rich** conditions to force chemistry to complete on accessible simulation times. **Oxidation** initiates by **thermal fragmentation** of aromatic moieties and/or **H abstraction** by **O\(_2\)**, **O**, and **OH**; **fuel-lean** conditions yield **faster** oxidation of polyaromatic frameworks than **fuel-rich**. **Ring** transformations include **6-membered** rings converting to **5-** and **7-membered** rings that further react or decompose.

## Methods

### 1 — MD application (atomistic dynamics)

**Reactive MD** uses **ReaxFF** for **hydrocarbon combustion** chemistry applied to an atomistic **devolatilized Illinois No. 6 coal char** model (`pdf_path`; `normalized/extracts/2012castro-marcano-combustion-a-combustion-illinois_p1-2.txt`).

- **Engine / code:** **ReaxFF** **reactive molecular dynamics** (abstract/Introduction class wording on extract); **N/A —** MD engine/package not named on the indexed excerpt pages.
- **System size & composition:** **Coal char** structural model built via **Fringe3D** (**HRTEM** fringe statistics) plus **Perl** scripts adding **heteroatoms** and **aliphatic** motifs with reduced investigator bias, constrained to literature **elemental** and **NMR** targets (abstract framing on extract).
- **Boundaries / periodicity:** **N/A —** not stated on the indexed excerpt pages.
- **Ensemble / timestep / duration / thermostat / barostat:** **N/A —** **NVT**/**NPT**/**NVE** labels, timestep sizes, **production run** segment reporting, and thermostat/barostat algorithms are not stated on the indexed excerpt pages.
- **Temperature:** **3000–4000 K** window stated for the high-temperature combustion MD campaign (indexed excerpt; verify exact sub-ranges per condition in **`pdf_path`**).
- **Pressure / stress:** **N/A —** not stated on the indexed excerpt pages.
- **Electric field:** **N/A —** not stated on the indexed excerpt pages.
- **Replica / enhanced sampling:** **N/A —** not stated on the indexed excerpt pages.

**Oxygen stoichiometry conditions:** **Stoichiometric**, **fuel-lean (oxygen-rich)**, and **fuel-rich** environments are used to accelerate chemistry to completable timescales at these temperatures (abstract, extract).

### 2 — Force-field training

**N/A —** the study **uses** an established **ReaxFF** **hydrocarbon combustion** parameterization associated with the van Duin-group ecosystem rather than reporting a new fit in the indexed excerpt.

### 3 — Static QM / DFT-only

**N/A —** not the primary methodology beyond structural model construction context (verify **`pdf_path`** for any DFT benchmarks).

## Findings

The analyses indicate **char oxidation** initiates either by **thermal fragmentation** of aromatic moieties into smaller pieces that subsequently oxidize, or by **H abstraction** by **O₂**, atomic **O**, and **OH**. **Fuel-lean (oxygen-rich)** conditions produce **faster** oxidation/consumption of **polyaromatic** frameworks than **fuel-rich** runs in their comparison. **Six-membered** aromatic rings transform into **five-** and **seven-membered** rings that further react or decompose, predominantly with **O** and **OH**. The work is presented as demonstrating integration of a **representative char structural model** with **ReaxFF** for high-temperature **combustion** chemistry (with **inorganics/ash** explicitly deferred as future work in the abstract framing).

## Limitations

- **Inorganics/ash** omitted in this “initial work”; temperatures are **far above** practical burners but chosen for **ReaxFF** timescale accessibility.
- Extrapolation to **engineering** burners requires bridging scales and lower-temperature kinetics not directly sampled.

## Relevance to group

**van Duin-group** **ReaxFF** on **coal char** combustion with **PSU** coal modeling collaborators—key corpus link between **reactive MD** and **energy** **carbonaceous** solids.

## Citations and evidence anchors

- DOI: [10.1016/j.combustflame.2011.10.022](https://doi.org/10.1016/j.combustflame.2011.10.022)
- Text-aligned pointer: `normalized/extracts/2012castro-marcano-combustion-a-combustion-illinois_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
- Coal char and reactive MD
