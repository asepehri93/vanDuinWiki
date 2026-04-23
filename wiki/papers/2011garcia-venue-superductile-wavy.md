---
id: paper:2011garcia-venue-superductile-wavy
type: paper
title: "Superductile, Wavy Silica Nanostructures Inspired by Diatom Algae"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - method:classical-md
  - material:silicate-glass
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:silica-silicate
  - keyword:lammps
  - keyword:berendsen-thermostat
candidate_tags: []
source_refs: []
doi: "10.1002/adem.201080113"
year: 2011
authors:
  - "Andre P. Garcia"
  - "Nicola Pugno"
  - "Markus J. Buehler"
venue: "Advanced Engineering Materials 13 (10), 2011"
pdf_sha256: "49684a19e1cf61872fa6b07d677231bc9ded4c147d4af4ee0b4878fdb42294cb"
pdf_path: "papers/ReaxFF_others/Garcia_Buehler_WavySilica_ABM_2011.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2011garcia-venue-superductile-wavy -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Diatom frustules combine nanoporous, hierarchical silica with corrugated and wavy geometries that are far tougher and more extensible than bulk silica. This work uses ReaxFF-based molecular dynamics to relate **wavy silica nanostructure** to **unfolding-dominated deformation** and large tensile ductility. For increasing corrugation amplitude, an unfolding mechanism is reported that raises ductility up to roughly **270% strain**, interpreted by analogy to “hidden length” in proteins and linked to energy dissipation and toughness. An analytical continuum model is developed to reproduce trends from the atomistic simulations and to support multiscale modeling from nanoscale structure toward larger scales.

## Methods


**Reactive MD** uses a validated **ReaxFF** parameterization for **silica** implemented in **LAMMPS**. Models are **alpha-quartz**-based corrugated **foils** (periodic in-plane waves) inspired by *Ellerbeckia arenaria* side-wall waviness: fixed wavelength **63.5 Å**, **width** \(w\) **20–120 Å**, **amplitude** \(A\) **0–60 Å**, with **~2650–7000 atoms** depending on geometry; the largest cell is about **177 x 63.5 x 8.5 Å**. After **NVT** equilibration at **300 K** for **10 ps** (**Berendsen** thermostat), structures are loaded in **uniaxial strain** along **[120]** at **300 K** at **\(10^{-10}\) s\(^{-1}\)** by expanding the periodic cell in the load direction only (**PBC** in all directions); **timestep 0.2 fs**. **Virial stress** is reported from standard LAMMPS-style sums (Eq. (1) in the article). The paper also cites **AFM** nanoindentation moduli on frustules (**~3.4–15.6 GPa** vs **~100–300 GPa** depending on hierarchical layer) for experimental context. A **continuum analytical model** is fit to reproduce atomistic stress-strain trends for multiscale use.

## Findings

The ReaxFF simulations report that **increasing corrugation amplitude** promotes an **unfolding** mechanism that raises **ductility** to about **270% strain** for the wavy silica nanostructures studied—far beyond brittle bulk silica—by analogy to **“hidden length”** uncoiling in proteins and associated **energy dissipation**. The authors argue that **tuning amplitude and width** of wavy silica nanostructures can improve mechanical performance despite silica’s intrinsic bulk brittleness. They further report a **continuum analytical model** that captures the atomistic trends and can serve as a bridge to larger-scale descriptions. The abstract also notes diatom frustules combine **hierarchical, porous silica** with **honeycomb/wavy** morphologies that are mechanically protective relative to bulk silica’s brittleness.

## Limitations

- Classical reactive potentials trade accuracy for scale; quantitative agreement with experiment depends on the ReaxFF parameterization and the idealized wavy models versus real frustule chemistry and defects.
- Continuum models summarize atomistic trends but require calibration when extended to different sizes and boundary conditions.

## Relevance to group

Illustrates **ReaxFF** applied to **silica mechanics** and bio-inspired geometry—adjacent to the group’s silica/water and reactive MD themes, though not a van Duin-group publication.

## Citations and evidence anchors

- DOI: [10.1002/adem.201080113](https://doi.org/10.1002/adem.201080113)
- Text-aligned pointer: `normalized/extracts/2011garcia-venue-superductile-wavy_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
- Bio-inspired silica and mechanical design of nanostructures
