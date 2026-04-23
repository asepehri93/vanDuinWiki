---
id: paper:2021verma-physical-che-reaxff-reactive
type: paper
title: "ReaxFF reactive molecular dynamics simulations to study the interfacial dynamics between defective h-BN nanosheets and water nanodroplets"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - domain:water-silica-geo
  - material:hexagonal-boron-nitride
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/D1CP00546D"
year: 2021
authors:
  - "Akarsh Verma"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys. 23, 10822–10834 (2021)"
pdf_sha256: "2c28fde33824b6e0b14ababd17f9b23037b1dff24d8c7ad7b50ef5abb5edd63c"
pdf_path: "papers/Verma_PCCP_BN_water_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021verma-physical-che-reaxff-reactive -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The work develops a B/N/O/H **ReaxFF** description to study **vacancy-defective hexagonal boron nitride (h-BN)** in contact with **water**: interfacial structure, water dissociation near vacancies, layered water under confinement, fracture initiation at defects, temperature-dependent droplet behavior (including contact angle trends vs. temperature and pore size), and hydrogen-bond-driven water organization near functionalized pores. The work positions defective h-BN/water interfaces as relevant to filtration, desalination, and nanofluidic device contexts where both chemistry and mechanical failure matter.

## Methods

**1 — MD application.** **ReaxFF** **molecular dynamics** in **LAMMPS** models **h-BN** **nanosheets** with **boron**/**nitrogen** **vacancies** plus **water** as **nanodroplets** or under **confinement** between sheets; **3D** **PBC** **slabs** of order 10³+ **atoms**; **NVT** **thermostat**; **sub-fs** **timestep**; **ps**–**ns** **equilibration** and **ramped** or **cooled** **stages** at controlled **temperature** (**K**). Cases include **contact-angle** **measurements** vs **pore** **diameter** and **T**; **compressive** **loading** between sheets; and **reactive** **H₂O** **dynamics** at **defects**. **Barostat / hydrostatic** **pressure** control: **N/A** in the excerpted droplet/confined protocols. **N/A — external** **macroscopic** **electric** **field**; **N/A — umbrella** in the main **trajectories** highlighted.

**2 — Force-field training (B/N/O/H).** A **B/N/O/H** **ReaxFF** is **fit** to **DFT**/**QM** **reaction** and **energetic** **benchmarks** for **defect** **h-BN** and **water**-mediated **bond** rearrangement (details, **k-mesh** where relevant, and **optimization** weights in *PCCP*).

**3 — Experiments. N/A.**
## Findings

Pristine h-BN nanosheets are treated as structurally stable and hydrophobic in the validation-style discussion; near **boron/nitrogen vacancies**, water can dissociate with terminal N/B sites participating in H- and OH-containing products. Under compression between sheets, water **layers**; fracture can **nucleate from vacancy defects**. The abstract further states that the **terminal** **N** and **B** at vacancies bind **H** and **OH**, respectively, that **layered** water forms under **compression** between two sheets, and that **fracture** **nucleation** is tied to **defects**—all framed in the **PCCP** context of **desalination**- and **underwater**-device relevance. **Contact angle** trends **decrease** with **higher** **temperature** and **larger** **pores** in the nanodroplet studies.

**Comparisons, sensitivity, PDF.** The paper relates **trends** in **wetting** to **T** and **pore** **geometry**; absolute **kinetics** and **angle** **values** must follow the **VOR** **PCCP** file.

## Limitations

Parameter set is specific to B/N/O/H chemistry in this application window; quantitative agreement with experiment for contact angles and kinetics requires cross-checking against measurements and higher-level electronic structure where polarization and long-ranged electrostatics dominate.

## Relevance to group

Extends the group’s ReaxFF line to **2D BN defects + aqueous interfaces**, linking reactivity, mechanics, and nanoconfined water behavior relevant to collaborative work on BN-related synthesis and devices.

## Citations and evidence anchors

https://doi.org/10.1039/D1CP00546D — Abstract and Introduction (~pp. 1–2) frame motivation and ReaxFF validation stance; Results sections detail interfacial chemistry and droplet/contact-angle behavior.

## Related topics

- [[reaxff-family]]
- [[20220000-0002-1558-1560-x-reaxff-force]]
