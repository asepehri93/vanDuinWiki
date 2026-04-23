---
id: paper:2018hanson-venue-supporting-online
type: paper
title: 'Supporting information: First-principles-based reaction kinetics from reactive molecular dynamics (H\(_2\)O\(_2\) decomposition)'
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reactive-md
  - keyword:lammps
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: "10.1073/pnas.1701383115"
year: 2018
authors:
  - "Daniil V. Ilyin"
  - "William A. Goddard III"
  - "Julius J. Oppenheim"
  - "Tao Cheng"
venue: "Proc. Natl. Acad. Sci. U.S.A. (Supporting Information PDF)"
pdf_sha256: "8923c83740d940b6ed0b7e102c03a8991810abb5bd7980c142407259f9f22a60"
pdf_path: "papers/ReaxFF_others/pnas.1701383115.sapp.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018hanson-venue-supporting-online -->

## Evidence and attribution

!!! note "Authority of statements"

    This file lists **SI** contents for **PNAS** DOI `10.1073/pnas.1701383115`. Scientific claims belong to **`[[2018ilyn-venue-first-principles-based]]`**.

## Summary

This corpus PDF (`papers/ReaxFF_others/pnas.1701383115.sapp.pdf`) is the **Supporting Information** bundle for **Ilyin et al.**, *Proc. Natl. Acad. Sci. U.S.A.*, on extracting **first-principles-quality reaction kinetics** from **ReaxFF reactive MD** of **hydrogen peroxide** decomposition (**RMD2Kin / ReaxMD2Kin** pipeline). The SI assembles **supplementary discussion**, **nine supplementary figures**, **eight trajectory movies**, **Table S1** with **bond-order cutoffs** for species detection, and **SI references**. Figures document **temperature sweeps** for **OH-** vs **HOO-initiated** pathways, **NVT/NVE** sensitivity, **dominant reaction** histograms, **QM vs ReaxFF** **transition-state** comparisons for key propagation steps, and **B3LYP** **potential energy surfaces** for selected reactions. **Movies S1–S8** provide **3D animations** of **ReaxFF** **reactive trajectories** referenced in the main text. Together, the **SI** package is structured so readers can **audit** each **major** **initiation** and **propagation** channel claimed in the **PNAS** article, including **QM** **sanity checks** on **selected** **elementary** reactions that dominate **long-time** **kinetics** fits. **Movies** are particularly useful for **teaching** **reactive MD** **parsing** because they show **3D** **atomic** **motion** accompanying **bond-order** **events** that can be **opaque** in **tabular** **output** alone.

## Methods

### SI contents (reproducibility artifacts)

- **Table S1:** **bond-order** **cutoffs** and related **parsing** thresholds for **species** detection from **ReaxFF** trajectories (**reuse exactly** when replicating **RMD2Kin** outputs).
- **Figures S1–S9** (inventory in SI): **temperature** sweeps, **dominant reaction** **histograms**, **QM vs ReaxFF** **transition-state** overlays for selected **elementary** steps, and **B3LYP** potential-energy scans for key channels referenced in the **PNAS** text.
- **Movies S1–S8:** **3D** **trajectory** animations of **ReaxFF** **H\(_2\)O\(_2\)** decomposition pathways.

### RMD2Kin / kinetic extraction (from SI + main text)

- **Reactive MD:** **ReaxFF** **LAMMPS** trajectories spanning **temperature** ranges used for **Arrhenius** extraction (**initiation** vs **propagation** emphasis documented in figures).
- **Ensemble sensitivity:** **NVT** vs **NVE** comparisons in the SI probe **thermostat** effects on **inferred** **rates** (see SI discussion).
- **QM benchmarks:** **B3LYP** (and related) **QM** data for **selected** reactions to **validate** **ReaxFF** **barriers**/**geometries** before exporting **kinetic** parameters.
- **Boundaries / duration / timestep / pressure:** Published **reactive MD** trajectories for **H\(_2\)O\(_2\)** decomposition use **3D periodic boundary conditions** on homogeneous gas-phase cells as shown in the **PNAS** main text and SI figures. **Production run** lengths and the integration **timestep** in **fs** are specified there (not duplicated numerically on this SI-only page). **N/A — NPT barostat** / **N/A — imposed hydrostatic pressure** for the standard constant-volume **NVT**/**NVE** comparisons tabulated in the SI.

### Authority / navigation

- Integrated **scientific** narrative and **primary** kinetic claims: **`[[2018ilyn-venue-first-principles-based]]`** (main **PNAS** article).

## Findings

As **supporting** material, the SI **does not introduce** new **standalone** scientific conclusions; it **enables reproducibility** of the **main paper’s** **kinetic** and **mechanistic** claims by exposing **raw** **analysis** choices (bond-order cuts), **supplementary** **Arrhenius** plots, and **QM** **comparisons** for **propagation** chemistry.
- **Mechanisms / rates:** Supplementary figures group **dominant reaction** channels for **OH-** versus **HOO-initiated** pathways, clarifying how **decomposition** **kinetics** are partitioned before exporting Arrhenius parameters.
- **Comparisons / sensitivity:** **NVT** versus **NVE** sweeps in the SI quantify **thermostat** **sensitivity** on inferred rates; **QM vs ReaxFF** overlays show where the reactive FF tracks **B3LYP** **barriers** for selected steps.
- **Limitations / corpus:** This page is **SI-only**; cite **`[[2018ilyn-venue-first-principles-based]]`** for integrated **Results** and for any **timestep**/**duration** numbers not restated here. **PDF** figure labels in the SI may differ cosmetically from HTML supplements on the publisher site.

## Limitations

**SI-only** PDF—read **`[[2018ilyn-venue-first-principles-based]]`** for **abstract**, **motivation**, and **integrated** discussion. **File naming** uses **PNAS** convention (`pnas.*.sapp.pdf`), not author **Hanson** (historical corpus label). **Bond-order** **cutoffs** in **Table S1** are **analysis parameters**—small changes can **repartition** species counts in **complex** **H₂O₂** **decomposition** networks, so **reuse** **cutoffs** exactly when **replicating** **kinetic** fits. **PNAS** may issue **corrections**; check the **publisher** site for **updates** to **supplementary** **materials**.

## Relevance to group

Provides **artifact-level** documentation for a **high-profile** **ReaxFF → kinetics** workflow cited in **combustion** and **reactive MD** method discussions; always cross-link **`[[2018ilyn-venue-first-principles-based]]`** for **integrated** **scientific** claims. The SI’s **QM** **TS** comparisons exemplify how **operators** should **validate** **elementary steps** before exporting **Arrhenius** parameters to **downstream** **kinetics** tables.

## Citations and evidence anchors

- Parent DOI: `10.1073/pnas.1701383115`; SI: `papers/ReaxFF_others/pnas.1701383115.sapp.pdf`; extract `normalized/extracts/2018hanson-venue-supporting-online_p1-2.txt` (figure inventory).

## Related topics

- [[2018ilyn-venue-first-principles-based]]
- [[reaxff-family]]
