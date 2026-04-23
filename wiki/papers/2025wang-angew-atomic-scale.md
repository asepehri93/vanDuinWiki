---
id: paper:2025wang-angew-atomic-scale
type: paper
title: "Atomic-Scale Mechanistic Insights into the Ring-Opening Polymerization of Elemental Sulfur"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:lammps
  - keyword:thermal-decomposition
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1002/anie.202511640"
year: 2025
authors:
  - "Mengyi Wang"
  - "Saied Md Pratik"
  - "Nadire Nayir"
  - "Maliheh Shaban Tameh"
  - "Veaceslav Coropceanu"
  - "Jean-Luc Bredas"
  - "Jeffrey Pyun"
  - "Adri C. T. van Duin"
  - "Shamil Saiev"
venue: "Angewandte Chemie International Edition"
pdf_sha256: "3389a15fc5e9eb9adb9885c7dd6c343ae0a7c210125ed3ded481b8a779139fe1"
pdf_path: "papers/Wang_Angewandte_Sulfur_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025wang-angew-atomic-scale -->

## Summary

Molten elemental sulfur undergoes a viscosity jump near the λ-transition (~159 °C) associated with ring-opening polymerization (ROP), but experimental characterization of polymeric sulfur species is difficult. This paper introduces a **ReaxFF parameterization aimed specifically at sulfur’s ROP chemistry**, trained against extensive quantum-mechanical reference data, and applies it to **large-scale reactive MD** (systems exceeding **10,000 atoms**) at temperatures relevant to polymerization. The simulations provide an atomistic picture of liquid sulfur composition and mechanism, including the report that **very large macrocyclic sulfur rings** appear at the onset of polymerization—a motif contrasted with the long-standing “chain model” picture dominated by S₈ rings and linear chains.

## Methods

- **Reactive model:** ReaxFF reactive force field **reparameterized** for elemental sulfur and its polymerization chemistry, with parameters fit to **quantum mechanical datasets** spanning relevant sulfur bonding environments and reaction energetics (exact training sets and validation benchmarks are given in the article and Supporting Information).
- **Simulations:** Classical reactive molecular dynamics at molten-state temperatures bracketing the λ-transition region, using large systems (>10⁴ atoms) to sample polymerization kinetics and composition in the melt.
- **Software context:** Large-scale MD consistent with group practice (e.g. **LAMMPS**-class engines for ReaxFF); the article and SI list integrator, **thermostat**, **time step**, **equilibration** vs **production** segments, and **temperature** windows around the **λ** transition.

**1 — MD application (atomistic dynamics).** **Reactive MD** in the melt for **>10,000** **atom** **composition**; **N/A** in this short summary: exact **NPT**/**NVE**/**NVT** label, **fs** **time step** value, full **ps/ns** **production run** length, and **PBC** discussion—confirm in the version-of-record PDF. **N/A** — no **NPT** **barostat** parameters stated here. **N/A** — no **static electric field** protocol in the ROP survey as summarized. **N/A** — no **metadynamics** or **replica exchange**; **N/A** — **umbrella** sampling is not part of the stated ROP **production** plan on this page.

**2 — Force-field training.** **Parent:** **ReaxFF** **reparameterized** for **sulfur** **ROP** chemistry, extending prior S/O/H training where applicable. **QM reference:** **DFT** (and broader **QM**) **data sets** across relevant **S** bonding and **reaction** energetics, per the article. **Training set / optimization:** **structures**, **reaction** energetics, and related targets listed in the main text and **Supporting Information**; **parameters** reoptimized to match the **reference** set. **Validation** uses **DFT**/**QM** and literature comparisons as stated.

**3 — Static QM / DFT-only.** **N/A** as a stand-alone **DFT** production study—the paper centers on **reactive** MD with **QM**-trained **ReaxFF**.

**4 — Reviews / non-simulation** — **N/A.**
## Findings

- Reactive MD with the new sulfur-focused ReaxFF reproduces a temperature-dependent composition of the melt consistent with the view that small rings and polymeric species coexist across the λ-transition, going beyond prior classical models that cannot form/break bonds.
- Simulations report the emergence of **large macrocyclic sulfur rings** during early polymerization stages, challenging older mechanistic pictures that emphasize only small rings and linear chains.
- The work positions **reactive MD** as a route to **mechanism**-level insight in **molten sulfur** **Ring-opening polymerization** and related **chemistry** contexts, with **temperature** near the **λ** transition a key **lever** (see the article for the reported window).

- **Corpus honesty:** ROP **barriers** and exact **kinetic** **rates** in the melt must be quoted from the **PDF**/**SI**, not this summary.

## Limitations

Force-field fidelity is bounded by the QM training coverage and classical MD approximations; longest relaxation times and nucleation rare events may still require enhanced sampling or larger trajectories than reported. Local corpus text is extract-limited for every numerical MD setting—confirm timesteps and run lengths in the PDF/SI.

## Relevance to group

Led in part by Adri C. T. van Duin with Penn State and Arizona collaborators; foregrounds **purpose-built ReaxFF training** for polymerizing sulfur.

## Citations and evidence anchors

- DOI: [10.1002/anie.202511640](https://doi.org/10.1002/anie.202511640)

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
