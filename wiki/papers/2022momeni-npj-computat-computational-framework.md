---
id: paper:2022momeni-npj-computat-computational-framework
type: paper
title: "A computational framework for guiding the MOCVD-growth of wafer-scale 2D materials"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - method:continuum-or-mesoscale
  - material:tmd
  - task:experiment-integrated
  - scale:multiscale
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:validation-experiment
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-022-00936-y"
year: 2022
authors:
  - "Kasra Momeni"
  - "Yanzhou Ji"
  - "Nadire Nayir"
  - "Nuruzzaman Sakib"
  - "Haoyue Zhu"
  - "Shiddartha Paul"
  - "Tanushree H. Choudhury"
  - "Sara Neshani"
  - "Adri C. T. van Duin"
  - "Joan M. Redwing"
  - "Long-Qing Chen"
venue: "npj Computational Materials"
pdf_sha256: "6ea427a14e94369d9285dfe652f69a10ec51c059428269bd0abfa4278e180090"
pdf_path: "papers/Momeni_MOCVD_2D_npjCompMat_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2022momeni-npj-computat-computational-framework -->

!!! abstract "Scope"

The **CPM** model couples CFD, phase-field growth, and reactive MD (including ReaxFF chemistry for WSe\(_2\)) to MOCVD experiments for wafer-scale 2D materials.

## Summary

Wafer-scale metal–organic chemical vapor deposition (MOCVD) of 2D materials is sensitive to flow, temperature, and precursor distribution. The authors build a multiscale framework (CPM: continuum fluid and heat transport linked to mesoscale phase-field island growth and nanoscale reactive MD) and benchmark it against detailed MOCVD experiments on WSe\(_2\) as a model TMD, including substrate rotation effects on uniformity. The **computational** **goal** is **not** a single **MD** **trajectory**, but a **coupled** **decision** **tool**: **reactor** **CFD** narrows **feasible** **window** **conditions**, **phase-field** **island** **models** translate those **conditions** into **morphology** **metrics**, and **ReaxFF** **segments** supply **surface** **reaction** **inputs** where **empirical** **rates** are uncertain.

## Methods

### A — ReaxFF / reactive MD (nanoscale chemistry)

- **Precursor–surface** reactions for **WSe\(_2\)**-relevant **MOCVD** chemistry: ReaxFF segments supply rates or barriers where empirical kinetics are uncertain (**full** species list and protocols in *npj Comput. Mater.* / **[[2022momeni-venue-paper]]** SI).

### B — Continuum reactor (CFD)

- **Navier–Stokes**, **continuity**, **species** **transport** (**convection–diffusion**), and **energy** equation; **boundary** **conditions** matched to the **experimental** **furnace** geometry (rotation, flow inlets, etc.).

### C — Phase-field (mesoscale growth)

- **Island** morphology, **edge** energies, **deposition** fluxes, **edge** diffusion, **temperature**-dependent shapes—fed by **CFD** **precursor** fields.

### D — Experiments

- **MOCVD** **WSe\(_2\)** **wafer** maps (**coverage**, **uniformity**) benchmark the coupled **CPM** framework.

**Coupling:** **CFD** → **phase-field** → comparison to experiment; **ReaxFF** **nanoscale** **segments** inform **kinetic** or **reaction** **inputs** for **MOCVD** **WSe\(_2\)** **(full** **species/thermal** **protocols** in **the** **article** + **[[2022momeni-venue-paper]]** **SI)**.

### 1a — ReaxFF / MD slot (for applicable MD blocks)

- **Engine, slab sizes, NVT timesteps, run lengths, long-range** **QEq/DFT** **kinetic** **bridges: N/A** in this **short** **wiki** **narrative** — the **definitive** **reactive**-**MD** **reactor**-**side** **protocol** **(LAMMPS**-style) **lives** in the **version-of-read** text + **SI**; **import** from **`[[2022momeni-venue-paper]]`** for **PBC,** **timestep,** and **thermostat** when **reproducing** the **WSe\(_2\)** **MOCVD**-**chemistry** **tether** **to** the **field**-**level** model. **Equilibration** **/ **production** **durations** **(ps** **/ **ns** **in** **ReaxFF** **or** **PF** **stages)** are **in** those **sources** **—** **N/A** here to **quote** **ns**-long **trajectory** **lengths** without **re-opening** the **full** **SI.**

### 1b — Continuum / multiscale (this paper’s emphasis)

- **N/A** **MD**-**as**-**entire** **paper** — the **work** is **not** a **stand-alone** **WSe\(_2\)** **RMD** **kinetics** **traj** **repo**; the **MOCVD**-**tethered** **reactor** **(CFD)**, **mesoscale** **phase**-**field** **morphology**, and **2DCC** **experiments** **drive** the **narrative**. **NPT** /**pressure** /**E**-**field** /**rare**-**event** **sampling: N/A** in the **summarized** **ReaxFF** **hitch**—see **1a** **(SI)**.
## Findings

**Outcomes and comparisons:** The 2DCC MOCVD experiments and the CPM (CFD + phase-field + ReaxFF-benchmarked WSe\(_2\) surface kinetics) report how inlet flow, rotation, and local temperature/precursor fields from the reactor model map to WSe\(_2\) coverage and island morphology. Quantitative agreement is in the VOR and SI, not re-tabulated here.

**Sensitivity levers:** Inlet flow, furnace geometry, and wafer rotation (plus the CFD-mapped T and C fields in the main text). N/A in this short summary: every precursor partial pressure; see VOR and `[[2022momeni-venue-paper]]` SI.
## Limitations

Reactive MD segments remain costly; continuum and phase-field parameters require calibration for each new material stack. The **CPM** coupling is presented as a **closed loop**: **CFD** supplies **precursor** **fluxes** and **thermal** maps that feed **phase-field** **island** **growth**, while **nanoscale** **ReaxFF** segments benchmark **surface** **reaction** **propensities** for **WSe\(_2\)**-relevant **precursors** under the **MOCVD** conditions explored experimentally. **Substrate** **rotation** enters both **flow** **uniformity** and **coverage** maps, so retrieval users should cite **figure** panels that tie **simulated** **uniformity** to **measured** **wafer** maps rather than quoting a single **scalar** **growth** rate in isolation.

## Relevance to group

Van Duin-group reactive MD is embedded in a multiscale pipeline with 2DCC MOCVD experiments.

## Reader notes (navigation)

- [[reaxff-family]]
- SI detail: [[2022momeni-venue-paper]]
- Hub: [[theme-2d-epitaxy-growth]]

## Citations and evidence anchors

- DOI: [10.1038/s41524-022-00936-y](https://doi.org/10.1038/s41524-022-00936-y)

## Related topics

- [[reaxff-family]]
