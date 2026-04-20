---
id: paper:2014somers-applied-cata-interactions-plasma
type: paper
title: "Interactions of plasma species on nickel catalysts: a reactive molecular dynamics study on the influence of temperature and surface structure"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:catalysis-surfaces
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - material:metal-surface
  - scale:atomistic
source_refs: []
doi: "10.1016/j.apcatb.2014.01.061"
year: 2014
authors:
  - "W. Somers"
  - "A. Bogaerts"
  - "A.C.T. van Duin"
  - "E.C. Neyts"
venue: "Applied Catalysis B: Environmental 154–155 (2014) 1–8"
pdf_sha256: "73441b32cbe253d2eceb5ffa2b3d30f13dfb9af40de64dc861851304918879ab"
pdf_path: "papers/Somers-2014-ACBE-154-1.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014somers-applied-cata-interactions-plasma -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Somers *et al.* use **ReaxFF-based reactive MD** to study impacts of **CH\(_x\)** radicals (\(x=1{-}3\)) from plasma-relevant methane chemistry onto **Ni catalyst surfaces** over **400–1600 K**, motivated by **plasma-assisted methane reforming**. They report that **H\(_2\)** formation becomes substantial at **≥1400 K**, while early-stage **C–H bond breaking** after adsorption can depend on **surface structure**; at longer times, **carbon diffusion into Ni** erodes crystallinity and **reduces** the lasting influence of surface facet identity on **H\(_2\)** formation probability. The paper frames these simulations as building blocks toward understanding **plasma–catalyst** coupling in reforming, beyond single-temperature DBD-relevant conditions.

## Methods

- **Reactive MD** with **ReaxFF** for hydrocarbon/Ni chemistry.
- Temperature sweeps and multiple **Ni surface** models (facet-dependent comparisons referenced in abstract/introduction).

## Findings

- **Facet effects** matter initially for radical dehydrogenation pathways and intermediate speciation.
- **Carbon ingress** into Ni at high temperature homogenizes structural signatures, weakening facet-dependent differences in **H\(_2\)** yields at later stages in the trajectories described.

## Limitations

- Plasma chemistry in reactors involves **electrons, photons, and field effects** not fully captured by gas-surface MD alone; the contribution isolates **radical–surface** reactivity.
- Extract covers introduction and partial results narrative; quantitative yield curves require deeper reading.

## Relevance to group

**Adri C. T. van Duin** as co-author connects the work to **ReaxFF** applications in **plasma catalysis** and **Ni/CH\(_x\)** reactivity relevant to reforming and related hydrocarbon/surface modeling.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.apcatb.2014.01.061](https://doi.org/10.1016/j.apcatb.2014.01.061)

## Related topics

- [[reaxff-family]]
