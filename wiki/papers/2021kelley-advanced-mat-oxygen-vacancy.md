---
id: paper:2021kelley-advanced-mat-oxygen-vacancy
type: paper
title: "Oxygen vacancy injection as a pathway to enhancing electromechanical response in ferroelectrics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - material:perovskite-oxide
  - method:reaxff
  - method:dft-static
  - method:continuum-or-mesoscale
  - task:experiment-integrated
  - scale:multiscale
paper_keywords:
  - keyword:oxide-surface
  - keyword:dft-static
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1002/adma.202106426"
year: 2022
authors:
  - "Kyle P. Kelley"
  - "Anna N. Morozovska"
  - "Eugene A. Eliseev"
  - "Vinit Sharma"
  - "Dundar E. Yilmaz"
  - "Adri C. T. van Duin"
  - "Panchapakesan Ganesh"
  - "Albina Borisevich"
  - "Stephen Jesse"
  - "Peter Maksymovych"
  - "Nina Balke"
  - "Sergei V. Kalinin"
  - "Rama K. Vasudevan"
venue: "Adv. Mater. 2022, 34, 2106426 (published online Oct 2021)"
pdf_sha256: "ac1628d8cd2db6e355e064a9abe2c3715c6ddc56229d6d0f7ed851082ca59c88"
pdf_path: "papers/Kelley_AdvMaterials_2022_BaTiO3.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021kelley-advanced-mat-oxygen-vacancy -->

## Summary

Piezoresponse force microscopy (PFM) on pulsed-laser-deposited BaTiO\(_3\) thin films shows large enhancement of electromechanical response when oxygen vacancies are injected and mobilized by the biased tip, including persistence of piezoresponse above the bulk Curie temperature. The authors combine temperature-dependent band-excitation PFM in UHV and air with Ginzburg–Landau–type continuum modeling, finite-element elasticity, ReaxFF molecular dynamics, and DFT to connect mobile oxygen vacancies, built-in fields, and renormalized elastic and polar response to the observed stiffening and enhanced effective \(d_{33}\)-like signal.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** ReaxFF molecular dynamics with **velocity–Verlet** integration for the BaTiO\(_3\) film models. **N/A** — if a specific program (e.g. LAMMPS) is required, confirm the Methods / SI in `pdf_path`.
- **System & composition:** ab initio–trained BaTiO\(_3\) ReaxFF; uniform vs layered oxygen-vacancy arrangements in a 0–3 at.% range as in the *Adv. Mater.* modeling (Fig. 7d–e and discussion).
- **Boundaries / periodicity:** 3D PBC supercells for the film/slab ReaxFF models as in the article. **N/A** — edge/facet construction is not re-derived on this page.
- **Ensemble / field / stages:** static field protocol: 50 ps per field step, with the last 12.5 ps of each segment time-averaged for Ba displacements and local thickness; \(d_{33}\) from linear thickness–field slopes for static fields along +z and −z (Fig. 7d–e in `pdf_path`).
- **Timestep (fs):** **N/A** in this note—read the *Adv. Mater.* Methods or SI.
- **Duration / stages / thermostat / barostat:** 50 ps per field step as above. Thermostat, barostat, and pre-field equilibration: **N/A** in this short summary; **N/A** for using bulk isotropic NPT as the main pressure story in the ReaxFF thread. The work targets **E**-field response, not bulk hydrostatic P control in the ReaxFF summary.
- **Temperature:** PFM vs T in UHV and ambient. **N/A** for a single ReaxFF thermostat setpoint in this stub—see the article.
- **Electric field:** yes—stepwise static fields along +z/−z in the ReaxFF \(d_{33}\) analysis (as described in the main text and Fig. 7).
- **Replica / enhanced sampling:** N/A.
- **Shear / shock:** N/A in the ReaxFF section summarized here.

**Experiment (film + PFM):** ~80 nm BaTiO\(_3\) on SrRuO\(_3\)/SrTiO\(_3\); band-excitation PFM, UHV and ambient; poling and cycling in Figs. 1–6 and related Methods.

**Continuum / FEM:** LGD-style models with vacancy-dependent coefficients; FEM for elastic subproblems tied to tip fields (see article).

### 2 — Force-field training

N/A — the paper **uses** a **cited** ab initio–tuned BaTiO\(_3\) ReaxFF; it does not report a new full refit. Provenance is in the article and its references.

### 3 — Static QM / DFT

Charged oxygen-vacancy DFT supercells; elastic moduli (Voigt–Reuss–Hill) vs \(V_\mathrm{O}\) concentration up to ~7.5%; **N/A** here to quote the full DFT level (functional, basis, k-sampling, convergence)—see *Adv. Mater.* and SI. Authors note phase-stability caveats for high defect load (~5% and above).

### 4 — Reviews, perspectives, or non-simulation studies

N/A.

## Findings

- **Experiment:** Large enhancement of electromechanical response (the abstract uses a ~4.8× enhancement framing) with vacancy injection; response order depends on bias-pulse order and can saturate with cycling. PFM maps T-dependent response, including features discussed past bulk \(T_\mathrm{C}\) in the main text.
- **ReaxFF on \(d_{33}\):** Pristine effective \(d_{33}\) ~7.1–7.2 pm/V; 3% uniform \(V_\mathrm{O}\) increases \(d_{33}\) by ~21–23% depending on field sign; 3% layered profiles raise \(d_{33}\) by up to ~39% in at least one field orientation, matching the trend of defect-enhanced response in the same modeling block.
- **DFT moduli vs \(V_\mathrm{O}\):** stiffen in the few-percent range, then weaken at high concentration where BaTiO\(_3\) becomes unstable—qualitatively aligned with PFM stiffening at intermediate defect filling before saturation.

**Comparisons** tie SPM, ReaxFF, and DFT on one system class. **Sensitivity:** uniform vs layered vacancy profiles, field sign, and T. **Limitations (as framed in the article):** simplified charge-state and supercell treatment for defects; the wiki does not re-copy the SI. **Corpus / KB honesty:** for citation-quality protocol numbers, use the VOR and SI in `pdf_path` with DOI 10.1002/adma.202106426.

## Limitations

Defects under strong fields involve multiple charge states; ReaxFF and DFT are simplified as stated in the article/SI. This page does not substitute for the full Methods.

## Relevance to group

ReaxFF coauthored by van Duin, integrated with SPM and continuum work on ferroelectric perovskite films.

## Citations and evidence anchors

*Adv. Mater.* **2022,** **34,** 2106426, DOI [10.1002/adma.202106426](https://doi.org/10.1002/adma.202106426) — PFM, continuum/FEM, ReaxFF, and DFT in `pdf_path` (Figs. 1–6, 7, modeling sections).

## Related topics

- [[reaxff-family]]
- [[ferroelectric-domain-wall-md]]
