---
id: paper:2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake
type: paper
title: "Deuterium uptake and sputtering of simultaneous lithiated, boronized, and oxidized carbon surfaces irradiated by low-energy deuterium"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - material:graphene-carbon-nano
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:validation-experiment
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1063/1.5026415"
year: 2018
authors:
  - "F. J. Domínguez-Gutiérrez"
  - "P. S. Krstić"
  - "J. P. Allain"
  - "F. Bedoya"
  - "M. M. Islam"
  - "R. Lotfi"
  - "A. C. T. van Duin"
venue: "Journal of Applied Physics 123, 195901 (2018)"
pdf_sha256: "b6b85e51855e6b971461fcc827ebe0b2db0b48ea345a404536133fbf8d2ac73c"
pdf_path: "papers/Dominguez_Gutierrez_JAP_2018_deuterium.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018f-j-dom-nguez-guti-r-journal-of-a-deuterium-uptake -->

## Summary

**Molecular dynamics** with **ReaxFF** potentials extended to treat **B** and **Li** on **carbon** surfaces quantifies **D retention** and **sputtering yields** for **Li–C–B–O** mixtures exposed to **low-energy D**, comparing selected results to **new experiments** on **B–C–O–D** systems to interpret how **oxygen** modulates **fueling/recombination**-relevant **D** behavior in **plasma-facing** **carbon** scenarios. The study is positioned as a **composition-resolved** complement to single-species carbon erosion benchmarks, emphasizing how **mixed conditioning** layers reorganize under sequential deuterium impact.

## Methods

From the **J. Appl. Phys.** PDF (`pdf_path`); **Sec. II** gives the simulation recipe.

- **Potentials / code:** **ReaxFF** for **Li-B-C-O-D** with **EEM** charges, implemented in **LAMMPS**. **Li-B** parameters trained vs **NWChem** **PBE0/** **6-31G*** **DFT** (bond/angle/binding benchmarks in **Fig. 1**).
- **Surface cell:** **~400** atoms, lateral **~1.8 nm**, depth **~2.0 nm** (**z**); amorphous **B/Li/C/O** mixtures prepared by melt/quench + **300 K** **Langevin** thermalization for each composition (**Sec. II B**).
- **D irradiation:** Projectiles **5 eV** (retention) and **5 eV** / **30 eV** (sputtering, as stated). **Sequential** bombardment: **D** launched **0.7 nm** above the surface every **50 ps** at random **x,y**; **20 ps** **NVE**-like cascade evolution, **20 ps** rethermalization to **300 K**, **10 ps** relaxation before the next impact (**Sec. II B**). **Saturation** preparation continues until **D_acc** plateaus (**<0.5%** change). Production statistics use **N = 15000** independent impacts on a prepared surface (**embarrassingly parallel** as described).
- **Observables:** Reported quantities connect **time-accumulated** retained deuterium, **sputtered** species yields, and **surface composition** evolution so that simulation outputs can be read alongside experimental surface-analysis channels discussed in the article.
- **Boundaries / pressure / timestep:** **3D PBC** on the amorphous **slab** cells as in Sec. II. Impact cycling alternates short **NVE** cascade segments with **rethermalization** toward **300 K**; **N/A — NPT barostat** and **N/A — imposed bulk pressure** in the quoted bombardment workflow. Integration **timestep** values are given numerically in Sec. II of the **Journal of Applied Physics** **PDF** (`pdf_path`).

## Findings

- **Oxygen** participates strongly in **D** bonding pathways across the explored compositions; comparative **experiment + simulation** highlights mechanisms for **D** retention in **B–Li–C–O** mixtures relevant to **conditioned** **PFC** chemistry.
- **Boron** can **suppress carbon erosion** relative to reference surfaces; **lithium** increases **oxygen** surface content under **D** bombardment in regimes discussed in the paper, modulating retention.
- The study positions **mixed conditioning** (**Li + B + O**) as a knob for **erosion** vs **retention** trade-offs in **fusion** **PFC** applications.
- **Comparisons and sensitivity:** Computational **retention** and **sputtering** metrics are read against **new experiments** on **B–C–O–D** surfaces and related datasets discussed in the article; trends depend on **impact energy** (**5 eV** versus **30 eV** channels) and on **B/Li/O** **composition** of the prepared films.
- **Limitations / corpus:** Classical **ReaxFF** omits explicit **electronic** sputtering; absolute yields should be taken from tables in the **PDF** rather than this wiki summary. **Proof** duplicate ingest: [[2018dominguez-venue-paper]].

## Limitations

- **Classical reactive** models omit **electronic** sputtering channels explicit in higher theory; energies focus on the **low-energy** experimental window emphasized in the article.
- **Surface heterogeneity** in real tokamak tiles (roughness, mixed materials) exceeds the idealized **flat** **B/Li/C/O** mixtures simulated here, so absolute retention numbers should be extrapolated to devices only with experimental anchoring.

## Reader notes (navigation)

- Proof duplicate PDF: [[2018dominguez-venue-paper]]. Maintainer catalog: [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (proof/galley duplicate handling).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
