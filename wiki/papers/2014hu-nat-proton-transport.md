---
id: paper:2014hu-nat-proton-transport
type: paper
title: "Proton transport through one-atom-thick crystals"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - material:hexagonal-boron-nitride
  - material:tmd
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:graphene-carbon
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/nature14015"
year: 2014
authors:
  - "Hu, S."
  - "Lozada-Hidalgo, M."
  - "Wang, F. C."
  - "Mishchenko, A."
  - "Schedin, F."
  - "Nair, R. R."
  - "Hill, E. W."
  - "Boukhvalov, D. W."
  - "Katsnelson, M. I."
  - "Dryfe, R. A. W."
  - "Grigorieva, I. V."
  - "Wu, H. A."
  - "Geim, A. K."
venue: "Nature"
pdf_sha256: "1773ade35ae210fabc1d1dbfa9f811fd36f4e71b7638ff9d4e2c8fadaf26cf95"
pdf_path: "papers/Others/Nature_graphene_protons_I.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014hu-nat-proton-transport -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

Electrical transport through micromembranes separates proton-injecting Nafion/PdHₓ stacks with suspended monolayer graphene, hexagonal BN, or MoS₂ barriers in humid hydrogen/argon. Monolayer graphene and hBN show measurable proton conductance under ambient conditions, whereas monolayer MoS₂, bilayer graphene, and few-layer hBN do not within the same protocol. Monolayer hBN exhibits the highest room-temperature proton conductance in the study, with a low activation energy ~0.3 eV reported for that barrier; graphene’s areal resistivity is estimated to fall below ~10⁻³ Ω cm² above ~250 °C. Catalytic metal decoration enhances throughput. Results position atomically thin crystals as selectively proton-conducting versus heavier species (abstract; extract pages 1–2).

## Methods

### Sample fabrication (2D membranes)

- **Micromechanically cleaved** **graphene**, **hBN**, and **MoS\(_2\)** flakes are **transferred** and **suspended** over **micrometre-scale** apertures in **Si** substrates; samples are screened to minimize **pinholes** before measurement (**Letter**; extract).

### Proton-injection contacts and electrolyte environment

- Membranes are **coated on both sides with Nafion** and electrically contacted using **PdH\(_x\)** stacks that inject **protons** into the measurement path (**extract**).
- **Gas-phase** measurements use **H₂/Ar** mixtures at **100% relative humidity**; **Extended Data** includes a **liquid HCl** control reporting **consistent** conductivities (**extract**).

### Transport measurements

- **Current–voltage (I–V)** sweeps quantify **proton conductance** through the suspended **2D** films, comparing **monolayer** vs **few-layer** stacks (**bilayer graphene**, **few-layer hBN**, **monolayer MoS\(_2\)**, etc.) (**extract**).

### Analysis metrics

- **Arrhenius** **activation energies** and **areal resistivity** estimates are extracted from temperature-dependent datasets as reported in the **Letter** (numbers in **Summary** above).

### Atomistic simulation and electronic-structure protocols

**N/A — atomistic MD / DFT production:** the **Letter** summarized here reports **electrical transport** through **micromembranes** with **gas-phase** **H₂/Ar** **humidity** control and **I–V** characterization, not **LAMMPS**-class trajectories or **plane-wave DFT** workflows. Timestep, thermostat, and PBC items from the MD-application checklist therefore do **not** apply to the primary evidence chain in `papers/Others/Nature_graphene_protons_I.pdf` (corroborate any secondary modeling citations in the full PDF if present).

## Findings

**Monolayer graphene** and **monolayer hBN** show **measurable proton conduction** under ambient conditions, whereas **no proton current** is resolved through **monolayer MoS\(_2\)**, **bilayer graphene**, or **thicker hBN** within the same protocol (parasitic leakage discussed). **Monolayer hBN** exhibits the **highest room-temperature proton conductance** among the barriers tested; the Letter reports a **low activation energy of ~0.3 eV** for monolayer hBN and estimates **graphene**’s areal resistivity falls **below ~10⁻³ Ω cm²** **above ~250 °C**. **Catalytic metal decoration** increases proton throughput. The discussion ties differences in permeation to **integrated valence electron density** patterns for **graphene** versus **hBN** versus the **thicker MoS\(_2\)** stack (Letter; extract pages 1–2).

## Limitations

Device architecture relies on Nafion-mediated proton supply; interpretation connects macroscopic currents to monolayer barrier physics as detailed in the full Methods.

## Citations and evidence anchors

- DOI `10.1038/nature14015` (extract header).
- Abstract-level claims (extract pages 1–2).

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[graphene-nanocarbon]]
