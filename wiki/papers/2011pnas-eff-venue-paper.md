---
id: paper:2011pnas-eff-venue-paper
type: paper
title: "High-temperature high-pressure phases of lithium from electron force field (eFF) quantum electron dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:methods-software
  - method:reactive-md-generic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reactive-md
  - keyword:metallic-systems
  - keyword:shock-compression
  - keyword:hugoniot
candidate_tags: []
source_refs: []
doi: "10.1073/pnas.1110322108"
year: 2011
authors:
  - "Hyungjun Kim"
  - "Julius T. Su"
  - "William A. Goddard III"
venue: "Proceedings of the National Academy of Sciences 108 (37), 15101–15105 (2011)"
pdf_sha256: "f116c77b01122bd0d5dabbda5bf9d85c6530f049571b70fd918957ae8f8c2319"
pdf_path: "papers/Others/PNAS-eFF_2011-Kim-15101-5.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2011pnas-eff-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The **electron force field (eFF)** approximates **nonadiabatic** electronic dynamics using **Gaussian wave packets** for electrons at cost comparable to classical MD. Applied here to **lithium** under **shock**-like **warm dense** conditions, eFF reproduces a **kink** in the **shock Hugoniot** seen experimentally and explains it with **two consecutive** structural transitions: an **fcc → cI16** transition (connected to low-temperature high-pressure work) and a further transition to a distinct **amorphous** Li phase (“amor”) at high \(T\), characterized by **localized** valence electrons in **interstitial**-like regions and disrupted connectivity relative to molten Li.

## Methods

### 1 — MD application (eFF dynamics)

The **electron force field (eFF)** propagates **Gaussian** electronic wave packets together with **classical nuclei** using a **Hartree-product**-like wavefunction (with approximate **exchange**), enabling **nonadiabatic** dynamics without assuming a precomputed **ground-state** electronic surface—emphasized as important when electronic kinetic energy becomes substantial above roughly **10,000 K** (introduction, `pdf_path`). For **lithium**, the article frames simulations across **warm dense** conditions up to about **20,000 K** and **100 GPa** to interpret the **shock Hugoniot** (abstract/introduction).

- **Engine / code:** **eFF** time propagation framed as costing comparably to **classical molecular dynamics** in the introduction; **N/A —** a specific MD software package name is not emphasized on the indexed pp. 1–2 text in `normalized/extracts/2011pnas-eff-venue-paper_p1-2.txt`.
- **System size & composition:** **Bulk lithium** phases; validation compares **fcc** vs **cI16** **lithium** lattices across densities **ρ = 0.53–1.5 g/cm³** at **300 K** (Results opening, extract).
- **Boundaries / periodicity:** **Three-dimensional bulk lattices** for the **fcc/cI16** validation discussion; **N/A —** explicit supercell vectors / shock-wave boundary modeling for Hugoniot sampling are not recovered from the short excerpt—verify **`pdf_path`**.
- **Ensemble:** **Isothermal** sampling at **300 K** for the **fcc/cI16** comparison; **N/A —** whether an explicit stochastic thermostat vs energy rescaling is used is not stated on the indexed excerpt pages.
- **Timestep:** **N/A —** not stated on the indexed excerpt pages.
- **Duration / stages:** **N/A —** segment lengths beyond “isothermal dynamics” are not stated on the indexed excerpt pages.
- **Thermostat:** **N/A —** thermostat type/damping not stated on the indexed excerpt pages (only **300 K** isothermal control is named).
- **Barostat:** **N/A —** validation scans **density** at fixed **ρ** values rather than reporting an **NPT** barostat protocol on the indexed excerpt pages.
- **Temperature:** **300 K** (solid-state validation); broader **shock** study framed up to **~20,000 K** in the introduction (extract).
- **Pressure / stress:** **Up to ~100 GPa** appears in the introduction scope statement for the Li study; **N/A —** how pressure/stress is imposed in the Hugoniot calculations is not detailed on the indexed excerpt pages.
- **Electric field:** **N/A —** not used in the indexed excerpt discussion.
- **Replica / enhanced sampling:** **N/A —** not indicated in the indexed excerpt.

### 2 — Force-field training

**N/A —** this publication develops/applies **eFF** as an explicit electronic wavepacket model, not a **ReaxFF/classical bond-order** refit in the sense of AGENTS block 2.

### 3 — Static QM / DFT-only

**N/A —** the central electronic structure treatment here is **eFF** (Gaussian wave packets + Hartree-product-like wavefunction), not a conventional **DFT** static campaign; the text explicitly contrasts **eFF** with **ground-state DFT** limitations for highly excited electronic dynamics (introduction, extract).

## Findings

**Outcomes and mechanisms:** For **lithium** under **shock**-like **warm dense** conditions, the authors report **two consecutive** structural transitions that produce a **kink** in the **shock Hugoniot** seen experimentally: (**i**) an **fcc → cI16** transition connected to prior **low-temperature high-pressure** diamond-anvil work, and (**ii**) a second transition to a distinct **amorphous** Li phase (“**amor**”) at high **\(T\)**, characterized by **localized** valence electrons in **interstitial**-like regions and disrupted connectivity versus molten Li (abstract + Results opening, extract).

**Comparisons:** The **Hugoniot kink** is tied to experimental observation “previously … not explained” in the abstract framing; **fcc/cI16** validation includes predicted **X-ray diffraction** behavior at **300 K** across **ρ = 0.53–1.5 g/cm³** (extract).

**Sensitivity and design levers:** The validation discussion is organized as a **density** sweep at **300 K** between competing **fcc** and **cI16** lattices; broader **\(T,P\)** scope is stated qualitatively in the introduction (**up to ~20,000 K** and **~100 GPa**).

**Limitations and outlook (authored tone):** The introduction emphasizes limitations of **DFT** and classical **FFs** in **warm dense** regimes where **nonadiabatic** electronic dynamics matter; **eFF** uses a **Hartree-product**-like treatment with approximate **exchange**, so accuracy is method- and system-dependent (introduction + discussion context on **`pdf_path`**).

**Corpus / KB honesty:** This page is grounded in **`pdf_path`** and `normalized/extracts/2011pnas-eff-venue-paper_p1-2.txt` (pp. 1–2 text only); **Hugoniot** numerical tables, full shock protocols, and later-section diagnostics are **not** excerpted here.

## Limitations

- eFF uses **Hartree-product**-like wavefunctions with **exchange** handled approximately; accuracy is method-dependent, especially for **core + valence** partitioning in heavier systems.
- Normalized record title in `normalized/papers/` is a placeholder string; the **PNAS** title and DOI above are taken from the article text.

## Relevance to group

Complements **ReaxFF** ecosystem papers by documenting **eFF** for **extreme** metallic systems—useful contrast when discussing when **explicit electrons** vs **bond-order reactive FF** are appropriate.

## Citations and evidence anchors

- DOI: [10.1073/pnas.1110322108](https://doi.org/10.1073/pnas.1110322108)
- Text-aligned pointer: `normalized/extracts/2011pnas-eff-venue-paper_p1-2.txt`

## Related topics

- Warm dense matter and alkali metal phase behavior
- [[reaxff-family]] (methodological contrast)
