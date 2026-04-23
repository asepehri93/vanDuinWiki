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
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014senftle-venue-jp411015a -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **J. Phys. Chem. C** article develops a **ReaxFF Pd/H** interaction description fit to quantum data for **bulk and surface** properties, then applies a **hybrid grand-canonical Monte Carlo / MD (GC-MC/MD)** approach to compute **hydrogen absorption isotherms** for **Pd bulk** and **nanoclusters** (sizes about **1.0–2.0 nm**) over wide pressure and temperature ranges. Structural analysis emphasizes how **surface, subsurface, and bulk** regions contribute to the **size-dependent** transition between low-concentration **α**-like solid solution and higher-concentration **β**-like hydride regimes framed in terms of the **miscibility gap** behavior known from bulk Pd–H. Complementary **MD** studies address **dissociative adsorption kinetics**, **hydrogen diffusion coefficients**, barriers, and pre-exponentials in bulk Pd; the abstract claims **agreement with experimental literature** for both thermodynamic (GC-MC/MD) and kinetic observables.

Broader motivation highlights **Pd** as the canonical **H\(_2\)** storage and **membrane** metal where **nanoscale** confinement shifts **phase** boundaries; pairing **GC-MC/MD** thermodynamics with **MD** kinetics tests whether a single **ReaxFF** line can reproduce both **isotherm** shapes and **diffusivity** trends.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

### ReaxFF training / reference data (Section 2.1 in article)

- **Pd/H ReaxFF** is derived from an **extensive quantum-mechanical training set** covering **bulk and surface** properties (abstract and Methods introduction); bond-order ReaxFF form follows the standard **van Duin** reactive force-field framework cited in the paper.

### Grand-canonical hybrid sampling (thermodynamics)

- **GC-MC/MD:** A **hybrid grand-canonical Monte Carlo / molecular dynamics** method computes **theoretical hydrogen absorption isotherms** for **Pd bulk** and **nanoclusters** with diameters **~1.0–2.0 nm**, spanning **hydrogen pressures** from **10⁻¹ atm** to **10⁻¹⁴ atm** and **temperatures** **300–500 K** (abstract). Equilibrated structures are analyzed by **region** (**surface**, **subsurface**, **bulk**) to interpret the **size-dependent** transition between low-concentration **α**-like and higher-concentration **β**-like hydride regimes tied to the bulk **miscibility gap** picture.

### Molecular dynamics (kinetics and transport)

- **MD** studies address **dissociative adsorption** of **H₂** from the gas phase for **size-dependent** uptake kinetics in clusters, and **H diffusion** in **bulk Pd**, reporting **diffusion coefficients**, **apparent barriers**, and **pre-exponential factors** from trajectory analysis (abstract).
- **Integration / cutoffs / timestep:** not stated in the checked-in **p1–2** extract; use the **J. Phys. Chem. C** Methods section and **Supporting Information** for engine settings and sampling lengths.

**PBC / frozen layers, thermostat damping, barostat (NPT vs NVT), and any anisotropic stress control:** **N/A —** not retyped from **`pdf_path`** on this wiki page—confirm in **Methods/SI**.

## Findings

- **Thermodynamics:** GC-MC/MD **isotherms** and regional **H** partitioning are used to describe how **surface**, **subsurface**, and **bulk** sites contribute to the **α→β** transition in **nanoclusters** versus bulk; the abstract reports **agreement with experimental literature** for these thermodynamic results.
- **Kinetics and transport:** MD-derived **uptake** behavior and **bulk H diffusion** parameters (including **barriers** and **pre-exponentials**) are also reported to match **experimental** values in the authors’ comparison, supporting validation of the **Pd/H** potential.
- **Nanoscale miscibility gap:** The Introduction reviews literature on **narrowing** (and possible **closure**) of the **miscibility gap** with decreasing cluster size and emphasizes **stabilizer/support** effects as an open experimental variable; the simulation analysis is framed in that context rather than as a single definitive cluster-size cutoff.
- **Parameter transferability:** The **Pd/H** description is **fully transferable** with earlier **Pd/O** parameters, enabling planned extensions to **Pd/O/H** and **Pd/C/O/H** for **oxidation**, **hydrogenation**, and **combustion** on **Pd** catalysts (abstract closing statements).

## Limitations

- Cluster-stabilizer and support effects remain an active experimental variable; the extract emphasizes unresolved literature scatter on **miscibility gap** closure for small clusters.
- Proofing artifacts appear in some deposited text variants; quantitative isotherm plots require full PDF review.

## Relevance to group

**Adri C. T. van Duin** co-authorship ties this to the group’s **ReaxFF parameterization** program for **hydrogen-metal** systems underpinning many catalysis and storage simulations.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp411015a](https://doi.org/10.1021/jp411015a)

## Related topics

- [[reaxff-family]]
