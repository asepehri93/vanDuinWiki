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
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015lloyd-surface-scie-development-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Lloyd *et al.* derive **Ag–Zn–O** interactions for **ReaxFF** by extending an established **ZnO** parameter set, fitting new terms to **density functional theory (DFT)** data from **SIESTA** for **bulk** references (elemental **silver**, **Ag–Zn** alloy, **silver oxides**) and for **Ag on ZnO** **surface** configurations, including **equations of state**, **binding energies**, and **works of separation**. The reported fits reproduce the DFT bulk benchmarks and track **Ag–ZnO** surface energetics with useful accuracy for the training scope. The work is motivated by **low-emissivity (Low-E)** glazing, where **Ag** films are sputtered onto **ZnO seed layers** but the **Ag/ZnO** junction is mechanically weak (**large lattice mismatch**, order **10%**). The parametrized field is exercised in **reactive MD** using **single-atom Ag deposition** onto **wurtzite ZnO**, comparing **O-terminated polar (0001)** and **nonpolar (1010)** orientations for impact energies from **0.1 eV to 30 eV**, bracketing **magnetron sputtering**-like conditions. Over that campaign, **adsorption is strongest when deposition energies stay at or below ~10 eV**, whereas higher energies favor reflection or subsurface behavior (per the article’s summarized trajectories).

## Methods

**DFT (SIESTA)** supplies energies and structures for bulk and surface training sets. The **ReaxFF** functional form follows the standard bond-order formulation used in prior ZnO work (total energy as sums of bonded, van der Waals, Coulomb, over/undercoordination, and related terms—see the article’s methodology section). **Ag–Zn–O** parameters augment the existing oxide description. **Molecular dynamics** uses **single-point Ag impacts** with controlled kinetic energy on the selected **ZnO** facets across the stated energy window to compare **polar** versus **nonpolar** growth contexts relevant to collaborators’ experiments.

## Findings

The **ReaxFF** parametrization **matches DFT equations of state** for the **Ag**, **Ag–Zn**, and **silver oxide** crystals used in training and **reproduces the intended trends** for **Ag adsorption** on **ZnO** slabs versus DFT. **Deposition simulations** link **impact energy** to **Ag retention**: the study reports that **maximum Ag adsorption on ZnO** occurs for **deposition energies ≤ ~10 eV**, with higher energies reducing sticking in the summarized runs—giving a practical processing-energy window for seed-layer **Ag** nucleation relative to **sputtering**-like conditions.

## Limitations

- High-energy impacts access **non-equilibrium** chemistry; users must validate **sputtering**-like outcomes against experiment for each **face chemistry** (O-terminated vs Zn-terminated) and defect population.

## Relevance to group

**A.C.T. van Duin** and **RxFF Consulting** contributors appear on the author list, reflecting **industry-facing** **ReaxFF** parameterization for **oxide/metal** interfaces.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.susc.2015.11.009](https://doi.org/10.1016/j.susc.2015.11.009)

## Related topics

- [[reaxff-family]]
