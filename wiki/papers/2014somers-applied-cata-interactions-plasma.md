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
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014somers-applied-cata-interactions-plasma -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Somers *et al.* use **ReaxFF-based reactive MD** to study impacts of **CH\(_x\)** radicals (\(x=1{-}3\)) from plasma-relevant methane chemistry onto **Ni catalyst surfaces** over **400–1600 K**, motivated by **plasma-assisted methane reforming**. They report that **H\(_2\)** formation becomes substantial at **≥1400 K**, while early-stage **C–H bond breaking** after adsorption can depend on **surface structure**; at longer times, **carbon diffusion into Ni** erodes crystallinity and **reduces** the lasting influence of surface facet identity on **H\(_2\)** formation probability. The paper frames these simulations as building blocks toward understanding **plasma–catalyst** coupling in reforming, beyond single-temperature DBD-relevant conditions.

The radical-flux picture abstracts the plasma as a source of hyperthermal hydrocarbon fragments impinging on a catalytic Ni surface, isolating surface chemistry from gas-phase electron impact chemistry.

## Methods

**Force-field training.** **N/A** for a new fit: the study uses an existing **ReaxFF** parametrization for **C/H** on **Ni** as cited in the article, rather than reporting a fresh **QM**-driven reparameterization in the indexed front matter.

**MD application (CH\(_x\) + Ni surfaces).** The authors perform **ReaxFF reactive MD** for **CH\(_x\)** (**\(x=1,2,3\)**) interacting with **Ni** catalyst surfaces, motivated by **plasma-assisted methane reforming** (abstract). Simulations span **400–1600 K**; **1600 K** is explicitly tied in the introduction to temperatures reachable in the **transitional regime of a gliding arc** discharge, while **400 K** matches typical **DBD** conditions. Prior work cited on **Ni(111)** over **400–1600 K** motivates the **H\(_2\)**-formation focus. **Engine**, supercell construction, **periodic** (**PBC**) boundaries, ensemble (**NVT**/**NVE**/**NPT**), timestep, **equilibration**/**production** **durations** (**ps**/**ns**), thermostat, and **barostat**/**pressure** control (if any **NPT** segments) are **N/A** on the short **p1–2** extract and must be read from **`papers/Somers-2014-ACBE-154-1.pdf`**.

**Static QM.** **N/A** as a headline method: the introduction cites **DFT** on **CH\(_4\)**/**Ni** for context, but reported results are **ReaxFF MD**.

## Findings

**H\(_2\)** becomes substantial at **≥1400 K** (abstract). **Surface structure** matters mainly in the **initial stage**, where **Ni** facet type influences **C–H** bond-breaking after adsorption of radicals—consistent with the authors’ prior **400 K** facet study in the introduction—but **continuous carbon diffusion** into **Ni** gradually erodes **crystallinity** and **reduces** the lasting influence of facet identity on **H\(_2\)** formation probability (abstract). The abstract closes by positioning these trajectories as building blocks for broader **plasma–catalyst** surface-reactivity questions across structures and temperature. Quantitative yield curves and impingement protocols are in the journal PDF/SI.

## Limitations

- Plasma chemistry in reactors involves **electrons, photons, and field effects** not fully captured by gas-surface MD alone; the contribution isolates **radical–surface** reactivity.
- Extract covers introduction and partial results narrative; quantitative yield curves require deeper reading.

## Relevance to group

**Adri C. T. van Duin** as co-author connects the work to **ReaxFF** applications in **plasma catalysis** and **Ni/CH\(_x\)** reactivity relevant to reforming and related hydrocarbon/surface modeling.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.apcatb.2014.01.061](https://doi.org/10.1016/j.apcatb.2014.01.061)

## Related topics

- [[reaxff-family]]
