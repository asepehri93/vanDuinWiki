---
id: paper:2015lloyd-surface-scie-development-reaxff
type: paper
title: "Development of a ReaxFF potential for Ag/Zn/O and application to Ag deposition on ZnO"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - method:reaxff
  - task:parameterization
  - task:application
  - material:metal-surface
  - material:oxide
  - scale:atomistic
source_refs: []
doi: "10.1016/j.susc.2015.11.009"
year: 2015
authors:
  - "A. Lloyd"
  - "D. Cornil"
  - "A.C.T. van Duin"
  - "D. van Duin"
  - "R. Smith"
  - "S. D. Kenny"
  - "J. Cornil"
  - "D. Beljonne"
venue: "Surface Science 645 (2016) 67–73"
pdf_sha256: "abdd27650d9ba7f3773556390efc78066c5a7656376ecbbe0a54613d65fcb8dc"
pdf_path: "papers/Lloyd_AgZnO_SurfSci2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015lloyd-surface-scie-development-reaxff -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Lloyd *et al.* extend an existing **ZnO ReaxFF** parameterization with **Ag–Zn–O** terms fit to **DFT (SIESTA)** equations of state and **surface binding/work-of-separation** data for **Ag on ZnO**. The abstract reports good reproduction of **Ag**, **Ag–Zn alloy**, and **silver oxide** crystal EOS targets and reasonable agreement for **Ag adsorption energetics** on ZnO surfaces. The fitted potential is then applied to **single-impact Ag deposition** on **polar (0001)** and **nonpolar (10\(\bar{1}\)0)** **wurtzite ZnO** substrates across **0.1–30 eV** impact energies (motivated by **magnetron sputtering**-like conditions), concluding that **maximum adsorption** is achieved for **≤10 eV** deposition energies in the summarized simulation campaign.

## Methods

- **DFT** training via **SIESTA** for bulk + surface references.
- **ReaxFF** reparameterization constrained to prior ZnO functional form where possible.
- **MD** deposition trajectories at variable impact energy.

## Findings

- Demonstrates a pathway to model **Ag thin-film nucleation** on **ZnO seed layers** relevant to **low-emissivity** glazing stacks, with explicit attention to **interface adhesion** weaknesses noted in the introduction.


## Limitations

- High-energy impacts access **non-equilibrium** chemistry; users must validate **sputtering**-like outcomes against experiment for each **face chemistry** (O-terminated vs Zn-terminated) and defect population.

## Relevance to group

**A.C.T. van Duin** and **RxFF Consulting** contributors appear on the author list, reflecting **industry-facing** **ReaxFF** parameterization for **oxide/metal** interfaces.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.susc.2015.11.009](https://doi.org/10.1016/j.susc.2015.11.009)

## Related topics

- [[reaxff-family]]
