---
id: paper:2013shan-venue-jp310473h
type: paper
title: "Atomistic simulation of orientation dependence in shock-induced initiation of pentaerythritol tetranitrate"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:msst
  - keyword:shock-compression
  - keyword:energetic-materials
  - keyword:lammps
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp310473h"
year: 2013
authors:
  - "Tzu-Ray Shan"
  - "Ryan R. Wixom"
  - "Ann E. Mattsson"
  - "Aidan P. Thompson"
venue: "The Journal of Physical Chemistry B"
pdf_sha256: "231f632686d95255471fa978e80195fa7fece8d92e46c7618bb2335fa39dd813"
pdf_path: "papers/ReaxFF_others/Shan_PETN_JPCB_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013shan-venue-jp310473h -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Authors are **Sandia National Laboratories**; no van Duin-group affiliation.

## Summary

ReaxFF MD with the **multiscale shock technique (MSST)** shocks PETN single crystals along [110], [001], and [100] with shock speeds **3–10 km/s**. Chemistry turns on at **≥ ~6 km/s**, initiated by nitro/nitrate-group cleavage. **Sensitivity ranks** [110] most sensitive, [100] least; for [001], nitro loss dominates initiation, whereas [110] and [100] show mixed nitro/nitrate pathways. Energy partitioning into C–NO\(_2\) vs C–ONO\(_2\) modes differs by orientation, matching the trend that orientations with stronger steric hindrance to shear localize more plastic work and heat.

## Methods

Grounding: `papers/ReaxFF_others/Shan_PETN_JPCB_2013.pdf`; `normalized/extracts/2013shan-venue-jp310473h_p1-2.txt` (abstract + Theoretical Methods opening).

### 1 — MD application (shock-driven reactive MD with MSST)

- **Engine / code:** **Molecular dynamics** simulations using **ReaxFF** with shocks driven by the **multiscale shock technique (MSST)** (abstract). **LAMMPS** is **not named** on the indexed excerpt pages.
- **System size & composition:** **PETN** **single crystal** simulated as a **4 × 4 × 4 supercell** containing **several thousand atoms** (abstract / Methods excerpt).
- **Shock / strain rate:** Shocks propagate along **[110], [001], and [100]** with shock speeds **3–10 km/s** (abstract).
- **Boundaries / periodicity:** **Bulk PETN** supercell shock setup (abstract framing); **exact boundary conditions** of MSST implementation are **not restated** on p1–2 beyond standard MSST usage—confirm in `pdf_path`.
- **Ensemble / thermostat (pre-shock equilibration excerpt):** Prior to compression/shock work, the excerpted protocol includes **NVT** relaxation at **300 K** using a **Nosé–Hoover** thermostat for **up to 6 ps (DFT-MD)** and **10 ps (ReaxFF-MD)** (`papers/ReaxFF_others/Shan_PETN_JPCB_2013.pdf`, Sec. 2 excerpt).
- **Timestep / duration (MSST production):** N/A — full **MSST production** timestep/duration tables are **not on p1–2**; read `pdf_path` shock Methods.
- **Temperature:** N/A — explicit **thermodynamic temperature protocol** for shocked states is **not stated** separately from **MSST shock strength** on p1–2.
- **Pressure / stress:** Shock loading implies **uniaxial compression** along selected orientations; **stress tensor reporting** is **not stated** on p1–2.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A — **not stated** beyond MSST-driven shocks.

### 2 — Force-field training

N/A — uses the **ReaxFF parametrization of Budzien et al.** as cited (abstract / Methods excerpt).

### 3 — Static QM / AIMD (supporting EOS context)

**DFT-based molecular dynamics (DFT-MD)** on the **unreacted Hugoniot** uses **AM05** in **VASP 5.2** with **800 eV** cutoff and **k-point sampling** at mean-value point **(1/4,1/4,1/4)**, ionic timestep **0.4 fs**, referencing experimental PETN lattice parameters (Methods excerpt).

## Findings

- **Outcomes & mechanisms:** For shocks **≥ ~6 km/s**, chemistry initiates via **dissociation of nitro and nitrate groups** (abstract). **Steric hindrance** arguments tie **slip-system** constraints to **localized plastic heating** and orientation-dependent sensitivity (abstract + introduction excerpt).
- **Comparisons:** The introduction contrasts prior **small-cell / pair-collision** studies with this work’s larger supercell shocks intended to capture **local deformation mechanisms** (abstract/intro excerpt).
- **Sensitivity / design levers:** **Shock orientation** and **shock speed (3–10 km/s)** are the primary knobs; **sensitivity order** is reported as **[110] most sensitive**, **[001] intermediate**, **[100] least sensitive** (abstract).
- **Limitations & outlook:** The abstract distinguishes **dominant initiation channels** by orientation (**[001]** nitro-loss-dominated vs **[110]/[100]** mixed nitro/nitrate pathways) and discusses **kinetic energy partitioning** among **C–NO\(_2\)** vs **C–ONO\(_2\)** modes (abstract).
- **Corpus honesty:** Indexed excerpt includes **DFT-MD settings** for the **unreacted Hugoniot** but does not include full **MSST parameter tables**; read **`pdf_path`** for complete shock MD protocol.

## Limitations

Ideal crystal blocks omit defects, porosity, and continuum-scale hydrodynamics. MSST is an approximate **shock-driving** framework; quantitative initiation thresholds should be cross-checked against the paper’s full shock protocol and any continuum/hydro validation literature cited there.

## Relevance to group

Corpus **energetic materials / shock** example using ReaxFF (external to van Duin group) for MST benchmarking.

## Citations and evidence anchors

- DOI: [10.1021/jp310473h](https://doi.org/10.1021/jp310473h)
- Extract: `normalized/extracts/2013shan-venue-jp310473h_p1-2.txt`

## Related topics

- Shock-to-chemistry coupling in condensed explosives
- [[reaxff-family]]
