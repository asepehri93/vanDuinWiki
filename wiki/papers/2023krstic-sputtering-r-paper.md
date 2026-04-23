---
id: paper:2023krstic-sputtering-r-paper
type: paper
title: "Processes at lithium-hydride/deuteride surfaces upon low energy impact of H/D"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.3389/fphy.2023.1105194"
year: 2023
authors:
  - "P. S. Krstic"
  - "E. T. Ostrowski"
  - "S. Dwivedi"
  - "A. Maan"
  - "S. Abe"
  - "A. C. T. van Duin"
  - "B. E. Koel"
venue: "Front. Phys."
pdf_sha256: "49eef4b993ef6ff439dd1a3509d8d96f7931afed58270f19742b06d1a9de5d5e"
pdf_path: "papers/Krstic_FrontInPhysics_LiH_2023_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023krstic-sputtering-r-paper -->

## Summary

**Plasma-facing components** in **magnetic fusion** devices may use **liquid** or **condensed lithium** coatings to control **impurity** influx and **hydrogen** **recycling**. When **hydrogen isotopes** **implant** into **lithium**, **near-surface** regions approach **lithium hydride** stoichiometries that differ sharply from **clean Li** metal in their **bonding**, **sputtering**, and **reflection** response. This **Frontiers in Physics** article presents **classical molecular dynamics** with an **extended ReaxFF** model—including **long-range polarization** physics—to study **sputtering**, **reflection**, and **particle retention** when **H** and **D** impact **crystalline** and **amorphous LiH** surfaces. The **abstract**-level framing stresses comparison to earlier **Li**, **Li\(_2\)O**, and **LiOH** irradiation studies from the same collaboration so readers can interpret how **hydride** formation modifies **low-energy** **collision** outcomes relevant to **divertor** and **first-wall** modeling.

Within the fusion **PMI** storyline, **near-surface** **LiH** is a plausible **hydrogen-rich** endpoint when **fuel** **implantation** accumulates in **lithium** layers; treating **LiH** as distinct from **bare Li** matters because **bonding**, **stopping**, and **erosion** channels shift when **H** is chemically incorporated rather than only physisorbed. The **galley** path in the corpus mainly changes **layout**—**primary** **statistics** should still be taken from the **published** **Frontiers** PDF for **DOI** `10.3389/fphy.2023.1105194`.

## Methods

### Interaction model (B)

**ReaxFF**-class **reactive MD** with **long-range polarization** extensions (see article).

### Impact grid

**H** and **D** on **LiH** at **300 K**; **E = 1–100 eV**; **polar angles 0°–85°** (**near-normal** to **grazing**).

### Surface variants

**Crystalline** vs **amorphous** **LiH** terminations.

### Analysis

**Probabilities** for **reflection**, **sputtering**, **retention**; **energy/angle** distributions of ejecta.

### Corpus note

**Galley** path in-repo—confirm **cells**, **Δt**, and **statistics** vs **VOR** (**DOI** `10.3389/fphy.2023.1105194`).

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** with an **extended** **ReaxFF** and **long-range** **polarization** treatment (see *Front. Phys.*). **System & composition:** **H** and **D** on **crystalline** and **amorphous** **LiH** **surfaces**; **E = 1–100** eV, **300** K, **0°–85°** **polar** **angle** grid. **Boundaries / periodicity:** **slab**-style **surface** models with PBC in-plane as in the paper. **Ensemble, timestep, run length, thermostat, barostat:** **H/D** **impacts** are **integrated** with **0.25**-**fs**-order **ReaxFF** **timestep** over **4**–**10** k **steps** per event and **NVT**-**prepared** **300** **K** **surfaces**; **N/A** in this page for the full **NVT** **bath** **damping** and per-run **ps** **duration** (see *Front. Phys.* **VOR**). **Pressure, electric field in MD, enhanced sampling:** **N/A** here; **E** in this study is **beam** **kinetic** **energy** (eV), not a macroscopic **E**-field.

### 2 — Force-field training

**N/A** — the article **applies** an **extended** **LiH**-compatible **ReaxFF** **+** **polarization** framework; **re-fit** **protocols** are described in the article rather than on this stub.

### 3 — Static QM

**N/A** — **MD**-centric **bombardment** and **sputtering** statistics.

## Findings

### LiH vs bare Li

**LiH** surfaces differ from **bare Li** in **reflection**, **stopping**, and **sputtering** under matched impacts—**hydride** bonding matters for **recycling** models.

### PMI implication

**Lithium conditioning** can yield **hydrided** near-surface regions; **LiH** should be included when interpreting **fuel** recycling/**impurity** release.

### Cross-reference

Connects to prior **Li**, **Li\(_2\)O**, **LiOH** bombardment work from the same collaboration—**numbers** in **journal** tables.

Readers building **recycling** models should treat these **LiH** results as complementary to **`[[2023krstic-j-appl-phys-detailed-studies]]`**: together they span **oxide/hydroxide**-rich versus **hydride**-rich **lithium** chemistries that can coexist depending on **oxygen** exposure and **implanted** **H** inventory.

## Limitations

**Galley** PDFs may differ in **figure** numbering from **final** layout; **proof** boilerplate in some **extracts** is **not** scientific content. **`extraction_quality`** is **partial** for some pipeline rows—prefer **`papers/`** **PDF** for **primary** numbers.

## Relevance to group

**A. C. T. van Duin** is a co-author; ReaxFF parametrization for Li/H systems supports fusion and energy-storage adjacent lithium chemistry.

## Citations and evidence anchors

- DOI: [10.3389/fphy.2023.1105194](https://doi.org/10.3389/fphy.2023.1105194)

## Related topics

- [[reaxff-family]]
