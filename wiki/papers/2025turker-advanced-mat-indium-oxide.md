---
id: paper:2025turker-advanced-mat-indium-oxide
type: paper
title: "2D Indium Oxide at the Epitaxial Graphene/SiC Interface: Synthesis, Structure, Properties, and Devices"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:oxides-ceramics
  - material:oxide
  - method:dft-static
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:oxide-surface
  - keyword:dft-static
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1002/adma.202516133"
year: 2025
authors:
  - "Furkan Turker"
  - "Bohan Xu"
  - "Chengye Dong"
  - "Michael Labella III"
  - "Nadire Nayir"
  - "Natalya Sheremetyeva"
  - "Zachary J. Trdinich"
  - "Duanchen Zhang"
  - "Gokay Adabasi"
  - "Bita Pourbahari"
  - "Li-Syuan Lu"
  - "Wesley E. Auker"
  - "Ke Wang"
  - "Mehmet Baykara"
  - "Vincent Meunier"
  - "Nabil Bassim"
  - "Adri C. T. van Duin"
  - "Vincent H. Crespi"
  - "Joshua A. Robinson"
venue: "Advanced Materials"
pdf_sha256: "347b641468ffcdfab319a4ff025391e863bedb813b7320171519875dabd6ca6d"
pdf_path: "papers/Turker_Nayir_2D_InO2_GrapheneSiC_AdvancedMaterials2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025turker-advanced-mat-indium-oxide -->

## Summary

The work reports synthesis of a monolayer indium oxide (InO₂) phase—distinct in stoichiometry from bulk indium oxides—intercalated under epitaxial graphene on SiC over large patterned areas (reported as >300 μm²). Graphene is patterned by optical lithography before intercalation so that the lateral extent of graphene patches tunes how thick the InO₂ film grows, with roughly 85% of the film described as monolayer. Complementary **molecular dynamics** and **density functional theory** calculations are used to rationalize the preference for monolayer InO₂ under these confinement conditions. Electronic-structure calculations assign a **4.1 eV** bandgap to monolayer InO₂, compared with **2.7 eV** for bulk reference values quoted in the paper. Metal–oxide–semiconductor Schottky diodes built on InO₂-intercalated epitaxial graphene on n-type SiC show the junction evolving from ohmic toward Schottky behavior, with a reported barrier height of **0.87 eV** and rectification ratio on the order of **10⁵**.

## Methods

- **Synthesis / processing:** Indium-oxide intercalation at the epitaxial graphene / SiC interface; **selective-area confinement heteroepitaxy (SA-CHet)** using optical lithography to pattern graphene before intercalation to improve lateral uniformity and control thickness.
- **Microscopy / fabrication:** Structural and device steps leading to MOS Schottky test structures on intercalated stacks; lithography, contacts, and measurement geometry are in the version-of-record PDF and SI.

**1 — MD application (atomistic dynamics).** The paper couples **molecular dynamics** to interpret **InO₂** monolayer preference under confinement (abstract). **N/A** — the checked-in `normalized/extracts/2025turker-advanced-mat-indium-oxide_p1-2.txt` and this note do not restate the MD **engine (e.g. LAMMPS)**, **atom** counts, **slab**/**supercell** **stoichiometry**, **PBC**/**periodic** cell setup, **ensemble** (**NVE**/**NVT**/**NPT**), **fs**-scale **time step**, **ps/ns** run lengths, **thermostat** type, or **NPT** **barostat** parameters. **N/A** — no **metadynamics**, **umbrella** sampling, or **replica exchange** in the short summary. **N/A** — no **static external electric field** in the modeling description on this page. **N/A** — this summary does not quote a **bar** or **GPa** target; see the PDF for any **NPT** or **stress**-controlled leg.

**2 — Force-field training.** **N/A** — the publication is not a new **ReaxFF** (or other FF) **parameterization** report.

**3 — Static QM / DFT-only.** DFT (with **molecular dynamics**) is reported for **InO₂** and bulk-like references to assign a **4.1 eV** monolayer **band gap** vs **2.7 eV** for bulk in the main text. **N/A** — the front-page extract does not restate **exchange–correlation functional**, **dispersion** treatment, **plane-wave/PAW** (or other) **basis** conventions, **k-mesh** density, or which **structures/relaxations** underlie the gap comparison; the article’s computational section must be read for that detail.

**4 — Experiment–simulation link.** Synthesis, **STEM**/**diffraction**-class characterization, and **MOS** electrical characterization are described in the main article; modeling supports **thickness**/**phase** interpretation and **barrier** discussion.

## Findings

- Large-area, largely monolayer InO₂ can be formed under epitaxial graphene on SiC, with thickness tuned via prepatterned graphene patch size.
- Theory supports a thermodynamic or kinetic preference for monolayer InO₂ under the intercalation constraints studied.
- Calculated monolayer InO₂ bandgap (4.1 eV) differs substantially from the bulk-like value (2.7 eV) quoted for comparison.
- Electrical devices show a strong Schottky-like rectification behavior with barrier height 0.87 eV and rectification ratio ≈10⁵ under the reported measurement configuration.

- **Corpus honesty:** Quantitative **MD/DFT** settings beyond the abstract on this page require the full PDF; do not extrapolate **taper**, **QEq** frequency, or DFT level from group defaults.

## Limitations

Computational modeling in the extract is summarized at a high level; readers should rely on the article’s methods for DFT functionals, MD force field choice, and convergence settings. Experimental device metrics depend on specific stack processing and contact geometry.

## Relevance to group

Adri C. T. van Duin contributes to modeling aspects of 2D oxide formation at epitaxial graphene / SiC interfaces within a broader experimental collaboration.

## Citations and evidence anchors

- DOI: [10.1002/adma.202516133](https://doi.org/10.1002/adma.202516133)

## Related topics

- [[graphene-nanocarbon]]
- [[theme-oxides-silica-ceramics]]
