---
id: paper:2011rebo-venue-paper
type: paper
title: "Reparameterization of the REBO-CHO potential for graphene oxide molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:classical-ff-specialized
  - material:graphene-carbon-nano
  - method:classical-md
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:qm-training-data
  - keyword:graphene-carbon
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.84.075460"
year: 2011
authors:
  - "Alexandre F. Fonseca"
  - "Geunsik Lee"
  - "Tammie L. Borders"
  - "Hengji Zhang"
  - "Travis W. Kemper"
  - "Tzu-Ray Shan"
  - "Susan B. Sinnott"
  - "Kyeongjae Cho"
venue: "Physical Review B 84, 075460 (2011)"
pdf_sha256: "666c1efb612884057d3f35f114c83c1ce6e25bef7e9bcff8704d644a075987f3"
pdf_path: "papers/Others/REBO_CHO_PhysRevB.84.075460.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2011rebo-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The **second-generation reactive empirical bond order (REBO)** potential for hydrocarbons, extended to **C/H/O** by **Ni et al.** as **REBO-CHO**, is **reoptimized** for **graphene oxide (GO)**. Using **density functional theory (DFT)** reference data, the authors adjust primarily the **bond-order** contribution so that **oxygen binding energies** to graphene and **equilibrium C–O distances** match DFT more closely, while preserving behavior for which the original **REBO-CHO** was trained. The modified potential is then applied to sample **GO** configurations to probe structural and energetic trends accessible to large **classical MD**.

## Methods

### 1 — MD application (atomistic dynamics)

The paper motivates **equilibrium molecular dynamics** studies of **GO** thermal transport as a downstream consumer of an accurate **C/O/H** reactive model (Introduction), and reports **classical MD** exercises of the modified **REBO-CHO** on representative **GO** samples (abstract/Introduction framing on `normalized/extracts/2011rebo-venue-paper_p1-2.txt`).

- **Engine / code:** **Classical molecular dynamics** is the stated application class; **N/A —** specific MD software is not named on the indexed excerpt pages.
- **System size & composition:** **Graphene oxide (GO)**-related test configurations are discussed qualitatively; **N/A —** atom counts / supercell stoichiometry are not restated on the indexed excerpt pages.
- **Boundaries / periodicity:** **N/A —** PBC vs cluster details for the MD demonstrations are not stated on the indexed excerpt pages.
- **Ensemble / timestep / duration / thermostat / barostat:** **N/A —** **NVT**/**NPT**/**NVE** integrator schedules, timestep sizes, trajectory segment lengths, and thermostat/barostat algorithms are not stated on the indexed excerpt pages.
- **Temperature / pressure / electric field / enhanced sampling:** **N/A —** not stated on the indexed excerpt pages.

### 2 — Force-field training

- **Parent FF / elements:** **Second-generation REBO** for hydrocarbons (**Brenner et al.** lineage), extended to **C/H/O** as **REBO-CHO** by **Ni et al.** (Introduction, extract).
- **QM reference:** **DFT** calculations supply reference **oxygen binding energies to graphene**, **equilibrium C–O distances**, and other **GO**-related benchmarks compared to **REBO-CHO** (abstract + Introduction, extract). **N/A —** DFT program/functional/basis/k-mesh details are not recovered from the indexed pp. 1–2 excerpt—verify **`pdf_path`**.
- **Training set / optimization target:** The modification focuses on the **bond-order term** so that **O binding** and **C–O distances** match **DFT** more closely while preserving behaviors for which the original **REBO-CHO** parameterization was deemed adequate (abstract, extract).
- **Optimization / software:** **N/A —** optimizer workflow details are not stated on the indexed excerpt pages beyond “optimized” language tied to **DFT** comparisons—verify **`pdf_path`**.
- **Reference data used:** **DFT** reference data for **GO**-relevant quantities; contextual discussion compares **REBO/AIREBO** practice (including **AIREBO**-style **vdW** switching) versus **COMB**/**ReaxFF** families for broader chemistry coverage (Introduction, extract).

### 3 — Static QM / DFT-only

**N/A —** DFT is used as **reference data** for fitting targets, but the publication is not a standalone static-QM discovery study framed as block 3.

## Findings

**Outcomes and mechanisms:** The abstract states that **REBO-CHO** “was **not suitable** to simulate **GO**” in the authors’ preliminary tests, motivating a **bond-order** modification that improves **oxygen binding to graphene** and **C–O equilibrium distances** versus **DFT** while aiming not to disturb regions where the original parameterization was adequate (extract).

**Comparisons:** Head-to-head **REBO-CHO vs DFT** comparisons are the central evidence anchors for the reparameterization claims on the indexed excerpt pages (abstract + Sec. I narrative, extract).

**Sensitivity and design levers:** The key lever emphasized is **which part of the REBO-CHO functional form is adjusted**—the article argues the issues “can be solved by recalculating **only the bond order term**” (Sec. I closing, extract).

**Limitations and outlook (authored tone):** The Introduction contrasts **REBO** efficiency (no explicit **charge** like **ReaxFF**) against limitations in **ionic/polar** environments—relevant to how far **GO** models can be pushed (Introduction, extract).

**Corpus / KB honesty:** Indexed text is **partial** (`extraction_quality: partial`); quantitative MD protocol lines and later-section benchmarks are not guaranteed to appear on pp. 1–2 of `normalized/extracts/2011rebo-venue-paper_p1-2.txt`—verify **`pdf_path`** for definitive tables.

## Limitations

- **REBO** remains a classical reactive model; **charge** is not treated like **ReaxFF QEq**, limiting transferability to highly ionic or polar environments.
- Parameter scope is **CHO** graphitic oxides; other heteroatoms and highly oxidized regimes may need separate validation.

## Relevance to group

Complements **ReaxFF** GO work by showing **REBO**-line tuning for **graphene oxide**—useful when comparing **speed vs polarizability** trade-offs.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.84.075460](https://doi.org/10.1103/PhysRevB.84.075460)
- Text-aligned pointer: `normalized/extracts/2011rebo-venue-paper_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
- Graphene oxide classical potentials
