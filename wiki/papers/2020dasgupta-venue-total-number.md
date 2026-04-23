---
id: paper:2020dasgupta-venue-total-number
type: paper
title: "ReaxFF molecular dynamics simulations of electrolyte–water systems at supercritical temperature (AIP author proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1063/5.0006676"
year: 2020
authors:
  - "Nabankur Dasgupta"
  - "Yun Kyung Shin"
  - "Mark V. Fedkin"
  - "Adri van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "28933b48e22f89b37098f1efbad6acc857c342133231074ecb5cbfc3726b43d9"
pdf_path: "papers/Dasgupta_JCP_2020_supercritical_electrolyte_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020dasgupta-venue-total-number -->

## Evidence and attribution

!!! note "Authority of statements"

    This ingest is an **AIP author proof / query** PDF (`papers/Dasgupta_JCP_2020_supercritical_electrolyte_galley.pdf`) with **AUTHOR QUERY** markup and placeholder pagination. Definitive **Methods** tables and figures refer to [[2020dasgupta-j-chem-phys-reaxff-molecular]].

## Summary

**ReaxFF** molecular dynamics of **alkali chloride** salts in **water** at **700 K** maps **structure** and **dynamics** across **liquid-like to vapor-like** **densities**, reporting **RDFs/ADFs**, **ion diffusion**, **H-bond residence times**, **Voronoi voids**, and **clustering**. This slug is a **proof** duplicate; scientific intent matches [[2020dasgupta-j-chem-phys-reaxff-molecular]]. **Supercritical** **aqueous** **electrolytes** matter for **geochemistry**, **hydrothermal** **synthesis**, and **extreme** **process** **windows**; the **JCP** study emphasizes how **dielectric** **screening** and **void** **topology** change when **water** **density** drops far below **ambient** **liquid** values.

## Methods

- **Potential:** **ReaxFF** for **water** and **alkali/halide** interactions as cited in the article.
- **Integration:** **Velocity Verlet**, **timestep 0.25 fs**; **Berendsen** thermostat, **100 fs** damping on the **full system** (per Methods).
- **State points:** **700 K** at water densities **ρ = 1.00, 0.70, 0.35, and 0.15 g cm\(^{-3}\)** for each salt (**Table I** on the canonical page); salts **LiCl**, **NaCl**, **KCl**, **RbCl**, **CsCl** as reported.
- **Ion** **clustering** diagnostics complement **RDFs** so **contact** **ion-pair** populations can be tracked as **screening** weakens.
- **MD (same science as VOR, see [[2020dasgupta-j-chem-phys-reaxff-molecular]]):** ReaxFF molecular dynamics; **atom-resolved** periodic **supercells** for each **alkali chloride** + water **composition** with water densities ρ = 1.00, 0.70, 0.35, and 0.15 g cm⁻³ in Table I on the canonical page; 700 K; Berendsen thermostat, 0.25 fs timestep, 100 fs Berendsen damping. Equilibration/production lengths in **ps**/**ns**: see VOR (N/A to duplicate the full table in this proof note). Barostat: N/A for isochoric state-point grids. Pressure control: N/A in those NVT production segments. Electric field: N/A. Enhanced sampling: N/A.

## Findings

- **Coordination**, **diffusion**, **void** statistics, and **clustering** trends with **density** and **ion** identity are summarized on [[2020dasgupta-j-chem-phys-reaxff-molecular]]—including **larger void volumes** and altered **transport** at **low density**, and **salt clusters** when **dielectric screening** weakens.
- Readers should lift **quantitative** **diffusion** **coefficients** and **uncertainty** estimates from the **VOR** article text rather than from **query** **overlay** pages in the **proof** PDF.

## Limitations

**Proof** PDFs are **not** substitutes for the **version of record**; **figures** and **line numbers** may differ. **700 K** and **supercritical** conditions are outside ambient **electrolyte** regimes.

**Curation note:** the local file includes **AIP** **author** **query** markup—open **[[2020dasgupta-j-chem-phys-reaxff-molecular]]** for **clean** **Methods** tables when building **Phase 5** chunks or **benchmark** cards. **Supercritical** **density** sweeps are the distinguishing feature versus ambient **Fedkin** **validation** papers. **Alkali** **series** **Li→Cs** trends should be read alongside **void** **percolation** discussion on the **canonical** **JCP** page. **Berendsen** **thermostat** **damping** **100 fs** matches the **canonical** **Methods** paragraph for these **state** points.

## Relevance to group

**van Duin-group** **ReaxFF** on **supercritical** **aqueous electrolytes**; this entry records **galley** bytes only.

## Citations and evidence anchors

- DOI: [10.1063/5.0006676](https://doi.org/10.1063/5.0006676) — galley: `papers/Dasgupta_JCP_2020_supercritical_electrolyte_galley.pdf`; VOR: [[2020dasgupta-j-chem-phys-reaxff-molecular]].

## Reader notes (navigation)

- **Corpus catalog (galley duplicate):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (entry **2020dasgupta-venue-total-number**)
- **Canonical article page:** [[2020dasgupta-j-chem-phys-reaxff-molecular]]

## Related topics

- [[2020dasgupta-j-chem-phys-reaxff-molecular]]
- [[reaxff-family]]
