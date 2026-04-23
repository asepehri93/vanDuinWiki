---
id: paper:2020islam-journal-of-e-enhancement-wse2
type: paper
title: "Enhancement of WSe2 FET performance using low-temperature annealing"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - method:classical-md
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:2d-materials
  - keyword:classical-ff
  - keyword:validation-experiment
source_refs: []
doi: "10.1007/s11664-020-08087-w"
year: 2020
authors:
  - "Zahabul Islam"
  - "Azimkhan Kozhakhmetov"
  - "Joshua Robinson"
  - "Aman Haque"
venue: "J. Electron. Mater. 49, 3770– (2020)"
pdf_sha256: "5f2d56e56bb6e6a31c32f7d18986abc90cdcd70e5a5ab8764335f68719f4ea1c"
pdf_path: "papers/Others/Islam_Haque_J_Elec_Mat_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020islam-journal-of-e-enhancement-wse2 -->

## Summary

Defects in transition metal dichalcogenides reduce carrier mobility and device performance; thermal annealing is a common repair strategy but often requires temperatures that stress interfaces or incompatible substrates. This Journal of Electronic Materials article investigates a **non-thermal annealing** process based on the **electron wind force**: current driven through a back-gated tungsten diselenide field-effect transistor channel while **Joule heating is actively mitigated**, keeping the process near room temperature. The authors argue that the electron wind force acts preferentially in defective regions, supplying atomic-scale mechanical drive that enhances defect mobility and enables defect annihilation without furnace-like temperatures. They report roughly **one order of magnitude** increase in drain current after treatment, which they present as experimental support for the hypothesis. The study situates WSe\(_2\) within the broader two-dimensional electronics effort at Penn State, where thickness and electrode engineering already tune ambipolar transport; improving channel crystallinity without high-temperature steps addresses integration constraints stated in the introduction.

## Methods

**Experiment (back-gated WSe\(_2\) FETs).** **WSe\(_2\)** is grown by **MOCVD** and integrated into **back-gated** field-effect transistors on **Si/SiO\(_2\)**. **Electron wind force (EWF) annealing** runs current through the channel while **actively mitigating Joule heating** so the process remains near **room temperature**; **transfer** characteristics and drain current are recorded **before and after** the treatment (deposition, contacts, and bias are specified in the article’s experimental section).

**1 — MD application (supplementary atomistic view).** The study reports **classical molecular dynamics** to probe **defect annihilation** and **local metallic phase transformation** alongside the **electrical** gains. **N/A —** simulation **code** (e.g. LAMMPS), **cell size** and **stoichiometry**, **PBC** details, **ensemble** (NVE/NVT/NPT), **timestep** and **trajectory length**, and **thermostat/barostat** parameters are **not** present in the short `normalized/extracts` snippet on disk; take these from the **version-of-record PDF** for replication. **Barostat / pressure control:** **N/A —** not specified in the extract for the MD block. **External electric field in the MD cell:** **N/A —** not described in the indexed text (the *experiment* is current-driven, not a separate MD e-field table here). **Enhanced sampling:** **N/A —** not mentioned in the extract.

**2 — Force-field training.** **N/A —** this work does not fit a new reactive or classical **force field**.

**3 — Static QM / DFT-only.** **N/A —** not a DFT study.

## Findings

**Outcomes and mechanisms.** After EWF annealing, the authors report about **an order of magnitude** increase in **drain current**, supporting the hypothesis that **momentum transfer** at **defects** raises **defect mobility** and enables **defect annihilation** at **near-room** conditions. **MD** is used to argue for **defect annihilation** and **local metallic** structural change as **consistent** with improved transport, framed as **illustrative** atomistic support rather than a full **device** model (see abstract and discussion in the **PDF**).

**Comparisons and outlook.** The introduction contrasts this route with **high-temperature** annealing (e.g. **>800 °C** in their literature context) that can be incompatible with some **substrates** or stacks; the selling point is **decoupling** annealing from **Joule**-dominated heating via **active cooling**—as stated in the text. **Corpus honesty:** **MD** **numerical** **protocol** details and any **error bars** on currents should be read from the **primary PDF** at `pdf_path`, not from this note alone.

## Limitations

Device variability, contact resistance, and long-term bias stress are not fully addressed in a single processing study. MD models use idealized defect distributions and classical potentials that may omit electronic-structure effects central to TMDCs. Electron-wind magnitudes depend on current density profiles that simplified MD cells do not reproduce.

## Relevance to group

Connects 2D defect engineering with atomistic interpretation adjacent to carbon and oxide simulation themes in the wiki.

## Citations and evidence anchors

- DOI: [10.1007/s11664-020-08087-w](https://doi.org/10.1007/s11664-020-08087-w)

## Related topics

- [[2020hu-npj-computat-predicting-synthesizable]]
- [[graphene-nanocarbon]]
