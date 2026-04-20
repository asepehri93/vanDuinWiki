---
id: paper:2015psofogiannakis-venue-jp5b00699
type: paper
title: "ReaxFF reactive molecular dynamics simulation of the hydration of Cu-SSZ-13 zeolite and the formation of Cu dimers"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - material:zeolite-porous
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b00699"
year: 2015
authors:
  - "George M. Psofogiannakis"
  - "John F. McCleerey"
  - "Eugenio Jaramillo"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "18feeef1f056fe0036c3209080ba474780c732df7289a731b4575f231b600d2c"
pdf_path: "papers/Psofogiannakis_JPCC_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015psofogiannakis-venue-jp5b00699 -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This study develops a **Cu/Si/Al/O/H ReaxFF** parameterization and applies it in reactive MD to follow **hydration and speciation of Cu in Cu-SSZ-13**, a zeolite central to selective catalytic reduction (SCR) of NOx. Simulations report that near-room-temperature water drives **framework-detached, fully hydrated Cu** that can migrate through pore windows, while at higher temperature the work highlights **OH-bridged Cu dimers** (for example Cu2OH and Cu2(OH)2) whose stability and pore-blocking placement are tied to framework composition (Cu/Al loading and stabilization of [CuOH]+). The discussion connects these atomistic pathways to **SCR and NO oxidation** phenomenology where extra-framework Cu speciation and transport matter.

## Methods

- **Reactive MD** with a newly trained **ReaxFF** description for Cu in aluminosilicate zeolite chemistry including water.
- **Training and validation** are framed against quantum-mechanical reference data in the original article (see PDF “Computational Methods” and supporting information).

## Findings

- A **Cu/Si/Al/O/H ReaxFF** enables nanosecond-scale trajectories that resolve **hydration-driven detachment** of Cu from the zeolite framework and **intra-pore diffusion** of hydrated cations.
- **Elevated temperature** promotes **cationic OH-bridged dimers** inside cages; dimerization temperature shifts with composition in a way consistent with higher-Cu, lower-Al materials stabilizing **[CuOH]+** precursors.
- **Stable dimers** associate with **8-member-ring** regions adjacent to large cages in geometries that can **obstruct pore openings**, with implications for diffusion-limited steps in catalytic cycles.


## Limitations

- Force-field accuracy is bounded by the **QM training set** and by ReaxFF’s empirical bond-order approximations; quantitative rates and spectroscopic observables require cross-checks against experiment and higher-level electronic structure where available.
- **Finite system sizes and simulation times** may undersample rare dimerization events or long-range cooperative effects in real crystallites.

## Relevance to group

Direct **ReaxFF parameterization for microporous Cu zeolites** with Penn State authorship; connects reactive FF development to **environmental catalysis** problems (NOx abatement) that motivate much of the group’s heterogeneous catalysis portfolio.

## Citations and evidence anchors

- Abstract and introduction in the PDF (`papers/Psofogiannakis_JPCC_2015.pdf`) state the force-field scope, hydration/detachment behavior, dimer chemistry, and SCR framing; **DOI:** `10.1021/acs.jpcc.5b00699`.

## Related topics

- [[reaxff-family]]
- Zeolite / Cu-zeolite themes: no dedicated `materials/zeolite-porous.md` page yet; search paper notes for *zeolite*.
