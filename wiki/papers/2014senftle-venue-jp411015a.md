---
id: paper:2014senftle-venue-jp411015a
type: paper
title: "A ReaxFF investigation of hydride formation in palladium nanoclusters via Monte Carlo and molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:catalysis-surfaces
  - method:reaxff
  - method:monte-carlo
  - task:parameterization
  - task:validation
  - material:metal-surface
  - scale:atomistic
source_refs: []
doi: "10.1021/jp411015a"
year: 2014
authors:
  - "Thomas P. Senftle"
  - "Michael J. Janik"
  - "Adri C. T. van Duin"
venue: "Journal of Physical Chemistry C 2014, 118, 4967–4981"
pdf_sha256: "6d34e358a2852ca044810c0f835d8cdb5b5fa25587a44302b20f64fb4bc1118b"
pdf_path: "papers/Senftle_PdH_JPCC_2014.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2014senftle-venue-jp411015a -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **J. Phys. Chem. C** article develops a **ReaxFF Pd/H** interaction description fit to quantum data for **bulk and surface** properties, then applies a **hybrid grand-canonical Monte Carlo / MD (GC-MC/MD)** approach to compute **hydrogen absorption isotherms** for **Pd bulk** and **nanoclusters** (sizes about **1.0–2.0 nm**) over wide pressure and temperature ranges. Structural analysis emphasizes how **surface, subsurface, and bulk** regions contribute to the **size-dependent** transition between low-concentration **α**-like solid solution and higher-concentration **β**-like hydride regimes framed in terms of the **miscibility gap** behavior known from bulk Pd–H. Complementary **MD** studies address **dissociative adsorption kinetics**, **hydrogen diffusion coefficients**, barriers, and pre-exponentials in bulk Pd; the abstract claims **agreement with experimental literature** for both thermodynamic (GC-MC/MD) and kinetic observables.

## Methods

- **ReaxFF** parametrization for **Pd/H** with extensive **QM training** data.
- **GC-MC/MD** for isotherm-style equilibration of hydrogen content in clusters and bulk.
- **Classical MD** for uptake kinetics and diffusion analysis.

## Findings

- Nanoscale clusters are discussed in the context of a **narrowed miscibility gap** versus bulk, with literature comparisons on whether the gap can close at small sizes depending on stabilization/support.
- The Pd/H parameters are noted as **transferable** with prior **Pd/O** parameters, enabling future **Pd/O/H** and **Pd/C/O/H** extensions for catalytic oxidation/hydrogenation/combustion studies.

## Limitations

- Cluster-stabilizer and support effects remain an active experimental variable; the extract emphasizes unresolved literature scatter on **miscibility gap** closure for small clusters.
- Proofing artifacts appear in some deposited text variants; quantitative isotherm plots require full PDF review.

## Relevance to group

**Adri C. T. van Duin** co-authorship ties this to the group’s **ReaxFF parameterization** program for **hydrogen-metal** systems underpinning many catalysis and storage simulations.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp411015a](https://doi.org/10.1021/jp411015a)

## Related topics

- [[reaxff-family]]
