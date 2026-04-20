---
id: paper:2015hong-venue-research
type: paper
title: "Molecular dynamics simulations of the oxidation of aluminum nanoparticles using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - material:metal-surface
  - scale:atomistic
source_refs: []
doi: "10.1021/acs.jpcc.5b04650"
year: 2015
authors:
  - "Sungwook Hong"
  - "Adri C.T. van Duin"
venue: "Journal of Physical Chemistry C (ASAP PDF in corpus; see DOI)"
pdf_sha256: "6974038ec96656cf9e22642917f384bd696f2822abb69a6d6626a0a0612ad676"
pdf_path: "papers/Hong_AlOx_JPCA_2015_ASAP.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015hong-venue-research -->

## One-paragraph summary

Hong and van Duin report **ReaxFF MD** of **aluminium nanoparticle (ANP) oxidation** at **300, 500, and 900 K** with two **initial oxygen densities** (0.13 and 0.26 g/cm\(^3\)). The abstract lays out a mechanistic picture where **O\(_2\)** adsorption/dissociation creates **hot spots** and **voids**; voids are claimed to **lower oxygen diffusion barriers** dramatically (up to **~92%**) and make diffusion **exothermic**, accelerating **oxide shell** growth. Oxidation extent and **oxide density/thickness** are reported to depend jointly on **temperature** and **oxygen pressure**, with overall kinetics said to align with selected experimental literature on aluminium oxidation.

## Methods

- **Reactive MD** with **ReaxFF** for Al/O chemistry, including validation discussion referencing **bare Al** oxidation before ANP cases (per introduction/extract).

## Findings

- Mechanistic competition among **thermal activation**, **oxygen availability**, and **microstructural** evolution (voiding) is central to the predicted oxidation trajectory.
- The study explicitly categorizes **oxidation states** (metal, suboxide, oxide, superoxide) along the trajectory in the aims paragraph.

## Limitations

- Nanoscale MD still uses high **effective pressures/temperature ramps** compared to many experiments; quantitative burning rates require careful upscaling analysis.
- ASAP PDF may differ slightly in pagination from the final issue version.

## Relevance to group

**Adri C. T. van Duin** co-authorship; strengthens the **Al/Al\(_2\)O\(_3\)** **ReaxFF** storyline used across combustion, propellants, and corrosion-related modeling.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpcc.5b04650](https://doi.org/10.1021/acs.jpcc.5b04650)

## Related topics

- [[reaxff-family]]
