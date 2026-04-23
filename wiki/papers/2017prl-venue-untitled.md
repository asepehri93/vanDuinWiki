---
id: paper:2017prl-venue-untitled
type: paper
title: "Topological Control on the Structural Relaxation of Atomic Networks under Stress"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - method:enhanced-sampling
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:enhanced-sampling
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevLett.119.035502"
year: 2017
authors:
  - "Mathieu Bauchy"
  - "Mengyi Wang"
  - "Yingtian Yu"
  - "Bu Wang"
  - "N. M. Anoop Krishnan"
  - "Enrico Masoero"
  - "Franz-Joseph Ulm"
  - "Roland Pellenq"
venue: "Phys. Rev. Lett."
pdf_sha256: "8875a0ac435402f0184c086b7e74a440e66ec5467571ec47dee70e8f40669c82"
pdf_path: "papers/ReaxFF_others/PRL_relaxation2017_bauchy.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017prl-venue-untitled -->

!!! abstract
Accelerated MD on Pellenq C–S–H models with ReaxFF shows logarithmic shear creep under constant stress; relaxation propensity is minimized near isostatic networks without floppy modes or eigenstress—linking topology to aging.

## Summary

**Calcium–silicate–hydrate (C–S–H)** controls **creep**, **aging**, and **durability** in **cementitious** materials, but linking **atomistic** disorder to **macroscopic** **rheology** requires models that capture both **chemistry** and **long-time** relaxation. Bauchy *et al.* construct **Pellenq-type** **C–S–H** structures across a range of **Ca/Si** ratios, introduce **water** via **GCMC**, and relax with **ReaxFF**, including **reactive** **water–silicate** interactions as cited in the letter. They then apply **accelerated molecular dynamics** under **constant shear stress** to extract **creep** kinetics and interpret trends with **topological constraint theory (TCT)** using **floppy-mode** counts, **eigenstress**, and **isostaticity** labels.

## Methods

### 1 — MD application (atomistic dynamics)

**Pellenq-type calcium–silicate–hydrate (C–S–H)** models spanning **Ca/Si** from **~1.0 to 1.9** are prepared by defecting an **11 Å tobermorite** parent and **grand canonical Monte Carlo (GCMC)** addition of interlayer water at **room temperature** and **constant volume**, followed by **ReaxFF** relaxation that allows **water dissociation** to **hydroxyl** species (methodology pointer to Pellenq *et al.* as cited in the letter). Prepared samples are **stress-relaxed at 300 K** before creep loading. Production creep uses **ReaxFF molecular dynamics** with an integration **timestep of 0.25 fs** (stated in the letter text) and **accelerated molecular dynamics** to reach laboratory-relevant relaxation timescales under **constant shear stress** (acceleration variant and run lengths detailed in the letter + **Supplemental Material**).

- **Engine / code:** **ReaxFF** reactive molecular dynamics as cited in the letter (specific MD engine not named on the indexed pages).
- **System size & composition:** **Layered C–S–H** nanograin models with tunable **Ca/Si** and interlayer **H₂O/OH⁻** content as generated from the **tobermorite** defect + **GCMC** hydration protocol summarized above.
- **Boundaries / periodicity:** **3D periodic** supercells consistent with the Pellenq C–S–H construction workflow (see cited Refs. [27–28] in the letter).
- **Ensemble / stress:** Initial **zero-stress relaxation at 300 K**; subsequent **constant shear stress** creep protocol using **accelerated MD** (details in SI).
- **Timestep:** **0.25 fs** (explicitly stated in the indexed letter excerpt).
- **Duration / stages:** **N/A on this wiki page** — total accelerated-MD clock and equivalent real time are not reproduced here; use the **PRL** SI bundle.
- **Thermostat:** **N/A** — explicit thermostat name not in the indexed letter excerpt (likely embedded in the accelerated-MD prescription in the SI).
- **Barostat:** **N/A** for the quoted creep segment — **shear stress** control dominates; hydrostatic **NPT** usage, if any, is not restated on the indexed pages.
- **Temperature:** **300 K** for the systematic pre-creep relaxation noted in the letter.
- **Pressure:** **N/A** — creep narrative emphasizes **shear stress**; isotropic pressure targets are not summarized on the indexed excerpt.
- **Electric field:** **N/A** — not used.
- **Replica / enhanced sampling:** **Accelerated molecular dynamics** (hyperdynamics / parallel-replica class—exact flavor in **PRL**/**SI**) replaces brute-force integration for rare activated events.

### 2 — Force-field training

**N/A as a new fit in this letter** — the study **consumes** an established **ReaxFF** parametrization for **C–S–H** with reactive water chemistry (cited parameter lineage).

### 3 — Static QM / DFT-only

**N/A** — **DFT** is not the long-timescale creep engine; QM appears only via prior validation literature referenced for the parent models.

### 4 — Topology analysis (non-MD)

**Topological constraint theory (TCT)** metrics—**floppy-mode** counts, **eigenstress**, and **isostaticity** labels—are computed on the same atomic networks to interpret **shear creep** propensity.

## Findings

### Outcomes and mechanisms

Under **constant shear stress**, **C–S–H** exhibits **delayed logarithmic shear creep** analogous to glassy network relaxation. **Isostatic** compositions—simultaneously **lacking** soft **floppy modes** and large built-in **eigenstress**—show the **lowest** propensity for **stress-driven relaxation**, whereas **flexible** (**n_c < 3**) and **stressed-rigid** (**n_c > 3**) networks creep faster via **soft modes** or **internal stress release**, respectively.

### Comparisons

The letter contrasts these **TCT** states using the **Pellenq C–S–H** model family, which the cited prior work validates against **nanoindentation modulus/hardness** experiments—supporting the use of the same models for **creep** trends.

### Sensitivity / design levers

**Ca/Si** ratio (and the associated defect + hydration history) shifts the network between **flexible**, **isostatic**, and **stressed-rigid** regimes, which the authors map directly to **creep** propensity.

### Limitations, outlook, and corpus honesty

**PRL** brevity means **full accelerated-MD parameters**, statistical replication, and additional **sensitivity** sweeps live in the **Supplemental Material** and referenced longer papers—this wiki entry is **not** a substitute for those tables. **ReaxFF** omits explicit **electronic-structure** detail; the authors flag that limitation when extrapolating to observables dominated by **charge transfer** or **redox** chemistry.

## Limitations

PRL letter format—full simulation parameters in supplementary references; single potential landscape (ReaxFF) governs chemistry. Readers seeking **quantitative** **creep** rates should treat this page as an orientation summary and extract numbers from the **letter + SI** bundle referenced by the DOI. **C–S–H** **nanostructure** varies with **curing** history; the modeled **Ca/Si** sweeps should not be read as exhaustive coverage of **cement** chemistry space.

## Relevance to group

Uses **ReaxFF** cement parametrizations and TCT tools aligned with **C–S–H** modeling in the broader KB.

## Citations and evidence anchors

- DOI: `10.1103/PhysRevLett.119.035502`

## Related topics

- [[reaxff-family]]
- [[2017n-m-anoop-krishnan-acs-revealing-effect]]
