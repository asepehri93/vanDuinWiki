---
id: paper:2017osti-venue-paper
type: paper
title: "Influence of metal ions intercalation on the vibrational dynamics of water confined between MXene layers"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - domain:methods-software
  - method:classical-md
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:2d-materials
  - keyword:validation-experiment
  - keyword:oxide-surface
source_refs: []
doi: "10.1103/PhysRevMaterials.1.065406"
year: 2017
authors:
  - "Naresh C. Osti"
  - "Michael Naguib"
  - "Karthik Ganeshan"
  - "Yun K. Shin"
  - "Alireza Ostadhossein"
  - "Adri C. T. van Duin"
  - "Yongqiang Cheng"
  - "Luke L. Daemen"
  - "Yury Gogotsi"
  - "Eugene Mamontov"
  - "Alexander I. Kolesnikov"
venue: "Phys. Rev. Mater."
pdf_sha256: "ac3c800f9e3657c9bf13a8469ed13eb21980cbe3856a33c5728903acb13c1045"
pdf_path: "papers/Osti_PhysicsMat_2017.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2017osti-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Two-dimensional MXenes such as Ti\(_3\)C\(_2\)T\(_x\) combine metallic conductivity with hydrophilic, tunable surfaces, motivating applications in electrochemical storage, electrocatalysis, and water treatment. Intercalation of ions and molecules alters interlayer spacing and electrochemical response, but how metal-ion intercalation changes the vibrational behavior of water confined between MXene sheets was not fully established. This work combines inelastic neutron scattering (INS) on Ti\(_3\)C\(_2\)T\(_x\) samples that are pristine or intercalated with Li\(^+\), Na\(^+\), or K\(^+\) with molecular dynamics simulations (including contributions from Pennsylvania State University collaborators) to characterize confined water. The neutron measurements detect water in all samples, but intercalated materials retain only a small amount of water between layers compared to the pristine case. Water in pristine Ti\(_3\)C\(_2\)T\(_x\) appears comparatively disordered and bulk-like in its INS signature, whereas in ion-intercalated MXenes the confined water is more ordered. The degree of ordering increases with the size of the intercalated alkali cation. Molecular dynamics reproduce the trend that larger ions interfere more strongly with water motion, reducing mobility and reinforcing the picture that ion identity can be used to tune interlayer water dynamics for energy and environmental applications.

## Methods

### 1 — MD application (atomistic dynamics)

The publication pairs **inelastic neutron scattering** with **molecular dynamics simulations** to interpret how intercalated alkali ions modify vibrational signatures and mobility of water confined in Ti\(_3\)C\(_2\)T\(_x\) MXene galleries. The early-page extract `normalized/extracts/2017osti-venue-paper_p1-2.txt` states the MD conclusions (larger ions correlate with stronger interference and lower water mobility) but does **not** locally reproduce the full numerical protocol table; use `pdf_path` for engine naming, supercell construction, timestep, thermostat, and trajectory schedule.

- **Engine / code:** Molecular dynamics with a **ReaxFF** description for MXene–water–ion interactions as reported in *Phys. Rev. Mater.* (implementation details on the journal PDF).
- **System size & composition:** Atomistic models of **Ti\(_3\)C\(_2\)T\(_x\)** with confined water and **Li\(^+\)/Na\(^+\)/K\(^+\)** environments matching the INS sample chemistries; explicit atom counts and stoichiometries are **N/A** in the indexed excerpt—confirm in the PDF.
- **Boundaries / periodicity:** **N/A** — three-dimensional **PBC** usage for the reactive supercell is not stated in the indexed p1–2 text.
- **Ensemble:** **N/A** — NVE/NVT/NPT staging for production sampling is not stated in the indexed excerpt.
- **Timestep:** **N/A** — integration timestep (fs) is not stated in the indexed excerpt.
- **Duration / stages:** **N/A** — equilibration vs production segment lengths are not stated in the indexed excerpt.
- **Thermostat:** **N/A** — thermostat type and coupling constants are not stated in the indexed excerpt.
- **Barostat:** **N/A** — pressure-control algorithm not stated in the indexed excerpt for the MD trajectories used against INS.
- **Temperature (MD):** **N/A** — target MD temperature(s) are not stated in the indexed excerpt (sample drying/annealing temperatures for INS specimens **are** given below).
- **Pressure:** **N/A** — hydrostatic pressure control is not stated for the MD portion in the indexed excerpt.
- **Electric field:** **N/A** — not part of the summarized MD/INS comparison.
- **Replica / enhanced sampling:** **N/A** — not described on the indexed pages.
- **Electrostatics / cutoffs / QEq cadence:** **N/A** — not restated in the indexed excerpt; expect standard ReaxFF charge protocols in the article text.

### 2 — Force-field training

The study **uses** an established **ReaxFF** parametrization for MXene–water–ion interactions cited from prior work; it does **not** report a new global refit of ReaxFF as the primary outcome.

### 3 — Static QM / DFT-only

**N/A** — DFT is not the spectroscopic engine for the INS measurements.

### 4 — Experiment (INS) and sample handling

**Sample chemistry:** Ti\(_3\)AlC\(_2\) powder (≤45 μm) etched in **48% HF**, washed until **pH > 4**, yielding Ti\(_3\)C\(_2\)T\(_x\). **LiOH / NaOH / KOH** (each **2 M**, 1 g solid : 10 mL solution) intercalation used repeated stirring, centrifugation, and fresh hydroxide contact as described in Sec. II.A. Powders were **air-dried 18 h**, **XRD**-characterized, then **vacuum annealed 110 °C for 4 h** to remove bulk water; pristine material received an additional **150 °C, 4 h vacuum** step to remove trapped molecular hydrogen.

**INS:** **SEQUOIA** (SNS, ORNL) with incident energies **E\(_i\) = 50, 160, 250, and 600 meV** for MXene samples; **VISION** (inverse geometry) measured reference spectra for liquid water and **2 M** Li/Na/K hydroxide solutions.

## Findings

### Outcomes and mechanisms

INS detects a hydrogen-bearing (water) signal in **pristine** and **Li-, Na-, and K-intercalated** Ti\(_3\)C\(_2\)T\(_x\), but intercalated hosts retain **only a small amount** of interlayer water relative to pristine material. Confined water in pristine Ti\(_3\)C\(_2\)T\(_x\) appears **more disordered** and comparatively **bulk-like**, whereas intercalated systems show **increased ordering** of confined water, with ordering that **increases with cation size** in the sense defined in the article.

### Comparisons and simulation cross-check

**Molecular dynamics** reproduce the experimental trend that **larger intercalated ions** correlate with **greater interference** among water molecules and a **concomitant decrease in water mobility**, aligning with prior **quasielastic** work on K\(^+\)-intercalated MXenes that linked reduced mobility to **partial water removal** and stronger bonding to **surface terminating groups** and intercalants (as summarized in the introduction of the indexed extract).

### Sensitivity and design levers

The study contrasts **pristine vs. Li/Na/K-intercalated** galleries and ties spectral changes to **ion identity** and **residual water content** after hydroxide processing—parameters operators should keep aligned when comparing simulation cells to INS specimens.

### Limitations and corpus honesty

`extraction_quality` is **partial** because the checked extract ends early in Sec. II; **numerical MD settings**, figure-level spectral assignments, and extended discussion live on the **version-of-record PDF** (`pdf_path`). This wiki does not substitute for those tables when reproducing simulations.


## Limitations

`extraction_quality` is marked partial in corpus profiling because full-section extraction may be incomplete; cite the **Phys. Rev. Mater.** PDF for spectral assignments, additional figures, and complete simulation protocols.

## Relevance to group

Connects Penn State reactive MD expertise to ORNL neutron data on 2D electrode materials and confined aqueous electrolytes.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1103/PhysRevMaterials.1.065406](https://doi.org/10.1103/PhysRevMaterials.1.065406) (`papers/Osti_PhysicsMat_2017.pdf`).
- Extract pointer: `normalized/extracts/2017osti-venue-paper_p1-2.txt`.

## Reproducibility and corpus locators

This note documents **where** to find primary evidence in-repo; it does **not** add new scientific claims beyond the cited publication.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, timesteps, ensembles, kinetics), use the peer-reviewed PDF (and publisher Supporting Information) as the authoritative source; this wiki summarizes for navigation and retrieval.

## Related topics

- [[reaxff-family]]
- [[theme-2d-epitaxy-growth]]
