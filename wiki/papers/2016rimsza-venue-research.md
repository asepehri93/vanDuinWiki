---
id: paper:2016rimsza-venue-research
type: paper
title: "Water Interactions with Nanoporous Silica: Comparison of ReaxFF and ab Initio Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - method:aimd
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b07939"
year: 2016
authors:
  - "J. M. Rimsza"
  - "Jejoon Yeon"
  - "A. C. T. van Duin"
  - "Jincheng Du"
venue: "J. Phys. Chem. C"
pdf_sha256: "2bfb535ed1eaf78b6b63de345b20d3f311c0a0d45d18d41de16d802b65e47286"
pdf_path: "papers/Rimsza_JPCC-water-silica-proof.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:aimd
  - keyword:water-interfaces
  - keyword:silica-silicate
  - keyword:oxide-surface
---
<!-- id:paper:2016rimsza-venue-research -->

## Summary

Nanoporous silica exposes strained siloxane and defect-rich surfaces to water. The study compares **two published ReaxFF Si/O/H parameterizations** (Yeon *et al.*, J. Phys. Chem. C **2016** and Fogarty *et al.*, J. Chem. Phys. **2010**) against **DFT-based ab initio molecular dynamics (AIMD)** for the same nanoporous models, emphasizing local structure, water dissociation paths, barriers, and diffusion—including nanoconfined water inside pores.

The corpus PDF is a **journal proof/galley-style** file (`Rimsza_JPCC-water-silica-proof.pdf`); treat the **version of record** DOI as authoritative for pagination and final wording.

## Methods

**1 — MD application (ReaxFF and AIMD).** **Nanoporous silica** models with internal surfaces rich in **strained siloxane** and **two-membered ring (2-ring)** defects are equilibrated and sampled with **ReaxFF** using the **Yeon *et al.*** and **Fogarty *et al.*** **Si/O/H** parameterizations named in the abstract, and with **DFT-based AIMD** on the same structural classes. Compared observables include **local hydration**, **water dissociation** paths and barriers where reported, **defect** populations and lifetimes, and **H** versus **O diffusion** under **nanoconfinement**. Full **protocol tables** (atom counts, **PBC**, ensemble, timestep, thermostats, barostats, run lengths, electrostatics) are **N/A —** not transcribed from this **proof/galley** PDF; use **`pdf_path`** and cross-check the **version-of-record** page **`[[2016rimsza-venue-jp6b07939]]`**. **Electric fields** and **enhanced sampling** beyond standard **MD** are **N/A —** not summarized here.

**2 — Force-field training.** **N/A —** applies published **ReaxFF** sets in a **validation** study.

**3 — Static QM / DFT.** **AIMD** provides the **QM** reference; detailed **DFT** settings are in the article/SI, **N/A —** not duplicated on this note.

**PBC** supercells host explicit water in **nanoporous Si/O/H** frameworks. **Molecular dynamics** with **ReaxFF** and **AIMD** follows **`[[2016rimsza-venue-jp6b07939]]`** for engine (**LAMMPS** where applicable), **NVT**/**NPT** staging, **timestep** (fs), **equilibration**/**production run** lengths (ps/ns), **thermostat** and **barostat**/**pressure** control, and **temperature** (K); this **proof/galley** **PDF** should not be used alone for those numbers. **Electric field** driving and **umbrella**/**metadynamics**/**replica-exchange** sampling are **N/A —** unless the published SI states otherwise.

## Findings

**Outcomes.** Pathways that **eliminate high-energy 2-ring defects** involve **two distinct intermediate** geometries whose **lifetimes** influence **hydroxylation** and **2-ring removal** rates. **Nanoconfinement** lowers **water diffusion** and yields **nanoconfined** water behavior distinct from bulk-like water. **Hydrogen** diffuses about **10–30%** faster than **oxygen**, consistent with **H-hopping** contributions under confinement.

**Comparisons.** Against **AIMD**, the **Yeon *et al.*** **ReaxFF** parametrization is reported to agree more closely on **mechanisms**, **hydroxylation rates**, **defect concentrations**, and **activation energies** in this benchmark; the authors **recommend** that parametrization for **high-defect**, **highly strained** water–silica interfaces such as complex **nanoporous** motifs.

Both **ReaxFF** sets reproduce parts of the **AIMD** picture, but **defect-rich** pores amplify differences; confirm numbers against **`[[2016rimsza-venue-jp6b07939]]`** and the publisher PDF when citing tables.

## Limitations

- Proof PDFs can differ slightly from the final typeset article; cite and read the **VOR** for exact numerical tables and supplementary cross-references.
- Transferability of the recommended FF is stated for **defect-rich, strained** silica motifs; bulk-like silica or different chemistries may require separate validation.

## Relevance to group

Co-authored by **A. C. T. van Duin**; directly benchmarks **ReaxFF water–silica** chemistry against AIMD for **nanoporous, defective** silica—an important validation setting for reactive silica simulations.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b07939](https://doi.org/10.1021/acs.jpcc.6b07939)
- Text-aligned pointers: `normalized/extracts/2016rimsza-venue-research_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
