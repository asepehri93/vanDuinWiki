---
id: paper:2025sowise-venue-paper
type: paper
title: "Molecular adsorbate effects on graphite–silica superlubricity: A ReaxFF investigation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - domain:carbon-hydrocarbon
  - material:graphite
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:graphene-carbon
  - keyword:oxide-surface
  - keyword:water-interfaces
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.26599/FRICT.2025.9441055"
year: 2025
authors:
  - "Marcus C. Perovich"
  - "Luis E. Paniagua-Guerra"
  - "Qian Mao"
  - "Seong H. Kim"
  - "Adri C. T. van Duin"
  - "Bladimir Ramos-Alvarado"
venue: "Friction"
pdf_sha256: "7d0d20380d4e1fb8ce59d786d7e74087de68d7a304d39ef3ef7c02ebd5e8fd25"
pdf_path: "papers/Perovich_Friction_2025_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2025sowise-venue-paper -->

## Summary

Graphite exhibits ultra-low friction on the basal plane, but ambient adsorbates are known to degrade superlubricity. This study uses ReaxFF-based reactive molecular dynamics of a graphite basal surface sliding against silica to compare phenol, pentanol, and water as interfacial adsorbates. Three different ReaxFF parameter sets—each trained with emphasis on friction-related observables—are compared to show that the optimization objective strongly affects predicted tribological behavior. Beyond sliding simulations, adsorption and binding-energy analyses are combined with a quantitative measure of interfacial roughness to test whether friction tracks interfacial structure more closely than binding energy or adsorbate commensuration with graphene.

Local corpus text is a short front-matter extract; load, velocity, thermostat, and cell construction details should be confirmed from the full PDF or supporting information.

## Methods

- **Interactions:** ReaxFF (bond-order reactive force field) with **three** distinct parameterizations optimized using friction-relevant training targets.
- **System:** Graphite–silica sliding interface with **phenol**, **pentanol**, or **water** as adsorbates.
- **Simulations:** **LAMMPS** **reactive** **Molecular** **dynamics** of **sliding** **friction** at set **temperature** in **K** (value in **SI**); **normal** **load** and **sliding** **directionality** (relative to the **graphite** **lattice**) **sweeps** in **PBC** **in-plane** **periodic** **slab** **supercells** for **graphite**–**silica** **contact** (full **lattice** **vectors** in **SI**).
- **Analysis:** Adsorption and binding-energy calculations; quantitative **interfacial roughness** metric for each adsorbate, related to computed friction coefficients. **N/A** on this page: **LAMMPS** (or other) **version**, **NVE**/**NVT** label, **time step** (**fs**), **ps**/**ns** **sliding** **duration**, **PBC** **cell** **vectors** and **atom** counts, **thermostat**/**barostat** details, and **GPa**/**bar** **normal** **pressure** protocol (see **Friction** **article**/**SI**). **N/A** — **replica** **exchange** in the **rare**-**event** **sense**; **N/A** — external **E**-**field** beyond the **load**/**contact** **pressure** already noted in the **normal** **load** **sweeps**.

## Findings

- The choice of ReaxFF training objective materially changes predicted coefficients of friction and overall tribological response for the same nominal interface chemistry.
- Normal load and sliding directionality modulate friction in ways consistent with the parameter-set comparison.
- Friction trends align more directly with the inferred **interfacial molecular structure / roughness** than with binding energy or simple commensuration arguments alone; the roughness-based interpretation accounts for the calculated friction coefficients across adsorbates. **Comparisons** across the **three** **ReaxFF** **parameter** **lines** are internal to the **manuscript**; use the **PDF** for **absolute** **μ** **values**.

## Limitations

Galley PDF in corpus; extract does not preserve full simulation protocol tables. ReaxFF accuracy remains tied to the chosen training data and may not capture all long-range polarization or quantum effects relevant to some oxide–carbon contacts.

## Relevance to group

Adri C. T. van Duin is a co-author; work demonstrates ReaxFF parameter sensitivity in tribology and environment-dependent superlubricity on graphitic carbon.

## Citations and evidence anchors

- DOI: [10.26599/FRICT.2025.9441055](https://doi.org/10.26599/FRICT.2025.9441055)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

## Reader notes (navigation)

- The corpus uses a **galley** `pdf_path`; prefer the final **Friction** **layout** **PDF** for exact **figure** and **parameter** **tables** when available.
- [[paper-index-by-domain]]
