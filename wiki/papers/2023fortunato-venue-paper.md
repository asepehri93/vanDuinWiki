---
id: paper:2023fortunato-venue-paper
type: paper
title: "Supporting Information: Choice of Electrolyte Impacts the Selectivity of Proton-Coupled Electrochemical Reactions on Hydrogen Titanate"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:oxides-ceramics
  - method:reaxff
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:batteries-interfaces
  - keyword:reaxff-application
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c01057"
year: 2023
authors:
  - "Jenelle Fortunato"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Veronica Augustyn"
venue: "J. Phys. Chem. C (Supporting Information PDF in corpus)"
pdf_sha256: "aefac80324eeadf5af07f1ca18530c9528fd39630844aba5250d75f4bc4d3235"
pdf_path: "papers/Fortunato_Shin_JPCC_2023_titanate_H3PO4_H2SO4_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023fortunato-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    This corpus PDF is **Supporting Information** for a **JPCC** article (**DOI** in front matter). **Electrochemical conclusions** belong to the **main article**; this page documents **SI** **ReaxFF** development content excerpted in the SI text.

## Summary

The SI accompanies Fortunato, Shin, Spencer, van Duin, and Augustyn’s study of **proton-coupled electrochemical reactions** on **hydrogen titanate (H₂Ti₃O₇)** in **acidic** media, contrasting electrolytes such as **phosphoric acid** versus **sulfuric acid** (full experimental narrative on the main article page). The SI’s **“ReaxFF method”** section restates the standard **ReaxFF** energy partitioning and notes **EEM**-type **charge** models for **Coulomb** interactions, emphasizing that parameters are fit to **QM** and/or **experimental** targets.

The SI’s **force-field development** discussion explains how the team extends a **TiO/H ReaxFF** suitable for **Ti(IV)** oxides and **water** chemistry on **anatase**, **rutile**, **brookite**, and high-pressure **TiO₂** phases, and then introduces **Sc–O–H** parameters so that **Sc(III)** acts as a **surrogate** for **Ti(III)** on **reduced hydrogen titanate** surfaces—an expedient when direct **Ti(III)** training data are difficult to fold into the optimization cleanly. Training sets cited in the SI include **equations of state** and **heats of formation** for **Sc₂O₃**, **ScO**, **ScO₂**, **hcp Sc**, and **molecular fragment** distortion curves (**Figure S1** in the SI). Additional **Ti/Sc** ternary oxide fits reference **Ti₂ScO₅** and **Ti₂Sc₂O₇** crystal phases (**Figure S2**). The SI also compares **oxygen vacancy** formation energetics on **rutile** with **Sc** substitution scenarios (**Figure S3**), supporting the qualitative point that **vacancies** near **Sc** analogues are stabilized differently than those near **Ti(IV)** sites.

## Methods

### Genre (supporting information, not standalone experiment)

This PDF is **Supporting Information** for **DOI** `10.1021/acs.jpcc.3c01057`, containing **ReaxFF** development detail, **QM** comparison figures (**S1–S3** etc.), and parameter tables—**not** the full **electrochemical** results narrative.

### Force-field development content (A)

- **Baseline:** Extension of a **Ti/O/H ReaxFF** for **Ti(IV)** oxides and **water** chemistry across **TiO\(_2\)** polymorphs (as cited in the SI).
- **Surrogate strategy:** **Sc–O–H** parameters introduced so **Sc(III)** can mimic **Ti(III)** on **reduced hydrogen titanate** surfaces when direct **Ti(III)** fitting is unwieldy.
- **Training sets:** **Equations of state**, **heats of formation**, and **distortion curves** for **Sc** oxides/metal and selected **Ti–Sc** ternary oxides (**figures** referenced in SI text).

### Where full cells and electrochemistry live

**Interfacial MD** benchmarks tying **anion** identity to **PCET** selectivity, plus **CV**/**capacity** metrics, are reported in the **main article**—see **`[[2023jenelle-fortunato-j-phys-chem-choice-electrolyte]]`** / **`[[2023fortunato-x-choice-electrolyte]]`**.

### MD application (SI page — delegate to main text)

**N/A** — this **SI** file documents **ReaxFF** **development** (**Ti/O/H**, **Sc–O–H**), **not** a standalone **MD** **protocol** sheet for **interfacial** **production** runs. For **LAMMPS**+**ReaxFF**, **PBC** **slab** cells, **NVT/NPT** choices, **thermostat** (e.g. **Nosé–Hoover** in the **main** **text**), **target** **temperature** (e.g. **~300 K** **room-temperature** **MD** in typical **interfacial** **setups**), **timestep**, **ps/ns**, **barostat/pressure**, **E-field**, and **sampling** used in the **H\(_2\)SO\(_4\)** vs **H\(_3\)PO\(_4\)** **interface** study, use **`[[2023fortunato-x-choice-electrolyte]]`** and the **main** **JPCC** **article** **PDF** at **DOI** `10.1021/acs.jpcc.3c01057`.

## Findings

### What the SI establishes

Reproducible documentation of the **ReaxFF** extension and **Sc-for-Ti(III)** surrogate with **QM** comparisons for **vacancy** energetics and related benchmarks.

### What requires the main text

**H\(_3\)PO\(_4\)** vs **H\(_2\)SO\(_4\)** **selectivity**, **Coulombic efficiency**, and **capacity** trends must be taken from **main-text** figures/discussion—**not** inferred from **SI** fragments alone. **Mechanistic role of the SI:** the **ReaxFF** **extension** is meant to make **reduced** **H\(_2\)Ti\(_3\)O\(_7\)** **surfaces** and **anion**-**competitive** **adsorption** **comparable** to **QM** on **key** **training** **geometries**—a **prerequisite** for **interpreting** **interfacial** **MD** in the **main** paper. **Comparisons** to **DFT** in **Figure S1–S3** are **internal** **validation** of the **force field**, **not** **cell** **polarization** **experiments** by themselves. **Sensitivity** of **PCET** **selectivity** to **pH**/**buffer**/**anion** is an **electrochemical** **lever** reported on the **VOR** page, **not** re-derived here. **Limitations & outlook:** **Sc** as a **Ti(III)** **surrogate** can **fail** if **electronic** **state** **space** drifts outside the **fitted** **set**; **however** the **SI** still gives **reproducible** **QM/FF** **gaps** for **main-text** **claims**. **Corpus honesty:** **SI-only** **PDF**; **electrochemistry** “**findings**” live on the **VOR** **main** page.

## Limitations

**SI** PDFs can be hard to interpret without the **main** article; **figures** are numbered separately (**S1**, **S2**, …). **Surrogate** elements increase **risk** if simulations wander outside the **fitted** **Sc/Ti** substitution regime.

## Relevance to group

Stores **Shin**/**van Duin** **ReaxFF** development detail for **titanate** **aqueous interfaces**, relevant to **energy storage** and **PCET** mechanistic studies.

## Citations and evidence anchors

- Article DOI [10.1021/acs.jpcc.3c01057](https://doi.org/10.1021/acs.jpcc.3c01057); SI PDF: `papers/Fortunato_Shin_JPCC_2023_titanate_H3PO4_H2SO4_SI.pdf`.
- Excerpt alignment: `normalized/extracts/2023fortunato-venue-paper_p1-2.txt`.

## Reader notes (navigation)

- Main article (slug may vary): [[2023jenelle-fortunato-j-phys-chem-choice-electrolyte]]

## Related topics

- [[reaxff-family]]
