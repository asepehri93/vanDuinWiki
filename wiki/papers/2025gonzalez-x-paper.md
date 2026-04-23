---
id: paper:2025gonzalez-x-paper
type: paper
title: "Methanol-to-hydrocarbon initiation reactions over a zeolite catalyst: reactive molecular dynamics simulations"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - material:zeolite-porous
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:catalysis-surface
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1039/D5CP02704G"
year: 2025
authors:
  - "E. Grajales-González"
  - "Adri C. T. van Duin"
  - "S. Mani Sarathy"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "f1048cbba8de50926032528038b3ea15676d884d08cf214b0f1426499a78a635"
pdf_path: "papers/Gonzalez_zeolite_HCO_PCCP_2025_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025gonzalez-x-paper -->

!!! note "Corpus note"
    Maintainer catalog (SI/galley/proof PDF roles): https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md
    The ingested file is an RSC **Accepted Manuscript** PDF (`Gonzalez_zeolite_HCO_PCCP_2025_galley.pdf`); formatting and pagination may differ from the final issue.

## Summary

The authors develop a **ReaxFF** parameterization—starting from the **Pitman–van Duin C/Si/O/Al/Ca** zeolite–clay line and adding **C/O** training relevant to **methanol-to-hydrocarbons (MTH)** initiation—and apply **LAMMPS** **NPT** dynamics on an **H-ZSM-5** model spanning **600–1200 K** to capture **dynamic acidity**, **water-assisted** chemistry, and **cation mobility** during early **methanol** conversion, beyond static **DFT** pictures.

## Methods

- **Force-field basis:** **Pitman–van Duin** **C/Si/O/Al/Ca** ReaxFF with documented **H/O/Si**, **H/O/Al**, **Ca/O**, **Ca/H** sub-blocks; additional **C/O** bond/angle/torsion training against **DFT** profiles of first **methanol** conversion steps (full specification in Section 2 of the paper).
- **MD protocol (LAMMPS):** All stages in **LAMMPS**; simulations begin with **energy minimization**, **100 ps NPT** at **1 atm**, then heating at **10 K s\(^{-1}\)** under **NPT**; production **NPT** segments at target temperatures; **time step 0.1 fs**; **Nosé–Hoover** thermostats/barostats for **NVT/NPT** stages as listed in the manuscript. **Zeolite flexibility** handled via variable cell **NPT** (see Computational Methodology §2.2 in the paper). **PBC** / **periodic** **supercell** for the **H-ZSM-5** model (full **cell** vectors and **atom** counts in the article).
- **System chemistry:** **Methanol** conversion to **water**, **DME**, and **surface methoxy (SMS)** species monitored in the **H-ZSM-5** framework; optional humidity cases at **800 K** described in the Results/Abstract.

**Zeolite model and mobility checks.** The **H-ZSM-5** framework is treated as **flexible** under **NPT** so **Al** sites, **Brønsted** **protons**, and **extra-framework** species can redistribute during **high-temperature** **MTH** chemistry—contrasting with static **DFT** cells that freeze **lattice** **atoms**. Production segments record **framework** **Al–O** **stretch**-like proxies and **cation**/**proton** **hopping** statistics discussed in the article as **entropy**-relevant **degrees of freedom**. **N/A** — no external **electric field**; **N/A** — **umbrella sampling** / **metadynamics** / **replica exchange** (not used in the workflow summarized here).

## Findings

- **Methanol** conversion rises from **800 K** to **1000 K**, producing **water** and **SMS**; **SMS** yields fall by **1200 K** as **methane** becomes more prevalent.
- **Humidity** at **800 K** shifts **Brønsted** acidity toward **dynamic** **H\(_3\)O\(^+\)**-like behavior, enhancing **hydrogen-transfer** pathways and framework activation relative to the drier case described.
- **Cation diffusion** is common in the reactive **MD** trajectories; authors argue this alleviates entropic bottlenecks relative to static **DFT** studies that fix framework **Al/H** positions.

Quantitative **rates** and **mechanism** details should be checked against the **version-of-record** (or the sibling **VOR** at `paper:2025grajales-gonz-xe1-physical-che-methanol-to-hydrocarbon-initiation`) if pagination matters; this page uses the **galley** PDF in `pdf_path` as catalogued.

## Limitations

High-temperature **ReaxFF** sampling can favor entropically dominated channels; the authors flag **>1200 K** regimes as potentially unreliable for chemistry. Full limitations are discussed in the PCCP text.

## Relevance to group

**Grajales-González**, **van Duin**, and **Sarathy**: **ReaxFF** **MTH** initiation on **H-ZSM-5** with **temperature-dependent** **framework** dynamics—complements **zeolite**/**catalysis** threads in the corpus.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1039/D5CP02704G](https://doi.org/10.1039/D5CP02704G)

## Related topics

- [[reaxff-family]]
