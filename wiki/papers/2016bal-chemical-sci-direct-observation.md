---
id: paper:2016bal-chemical-sci-direct-observation
type: paper
title: "Direct observation of realistic-temperature fuel combustion mechanisms in atomistic simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - method:reaxff
  - method:enhanced-sampling
  - domain:organics-polymers-pyrolysis
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:enhanced-sampling
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1039/C6SC00498A"
year: 2016
authors:
  - "Kristof M. Bal"
  - "Erik C. Neyts"
venue: "Chem. Sci."
pdf_sha256: "4681ba292eb3aef7329f8f0d594fbabe8b65b48cd9634a324ca342b354951380"
pdf_path: "papers/ReaxFF_others/Bal_Neyts_CVHD.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016bal-chemical-sci-direct-observation -->

## Summary

Reactive molecular dynamics with **ReaxFF** can follow bond rearrangements in fuel chemistry, but nanosecond horizons have historically forced **>2000 K** simulations for appreciable alkane reactivity. This **Chem. Sci.** article applies **CVHD + ReaxFF** in **LAMMPS** to extend **effective** timescales: **n-dodecane pyrolysis** is reported down to **1000 K** (long **~57 ms** effective trajectory in their Table 1 example), while **lean oxidation** reaches **700 K** with an **effective time up to ~39 s**. **CVHD** grows a history-dependent bias on bond-distortion collective variables (hyperdynamics-style acceleration with metadynamics-like hill deposition). The authors argue **product compositions** and **dominant pathways** are **strongly temperature-dependent** and **consistent with experiments and kinetic models** for the comparisons shown—see **`[[2016bal-2016-chemsci-doi-venue-direct-observation]]`** for the fully tabulated MD/CVHD protocol grounded on this same DOI.

## Methods

This ingested PDF (`Bal_Neyts_CVHD.pdf`) is a **DOI-identical sibling** of **`[[2016bal-2016-chemsci-doi-venue-direct-observation]]`** (different bytes on disk). The scientific protocol is the same **Chem. Sci.** **2016**, **7**, **5280–5286** article: **LAMMPS + colvars + CVHD**, **ReaxFF** (**Chenoweth *et al.*** with **QEq**), **Δt = 0.1 fs**, **Langevin thermostat** thermalization then **Nosé–Hoover-chain NVT** (**0.1 ps** relaxation) and **Martyna–Tobias–Klein barostat NPT** (**1 ps** relaxation) where used. **System composition & PBC:** **pyrolysis** = **912 atoms** (**24** n-dodecane) in a **50 × 50 × 50 Å³** **periodic** cell; **lean combustion** = **390 atoms** (**5** n-dodecane + **100** O₂) in a **40 × 40 × 40 Å³** **periodic** cell; **CVHD** uses the **C–C/C–H** strain collective variables and **Gaussian** hill schedules quoted on the sibling page, plus additional **NPT CVHD** at **1000 K** (**10–500 bar**) with a **0.5 ps** hill stride. **Electric field:** **N/A — not used.** **Replica / umbrella sampling:** **N/A —** acceleration is **CVHD** only.

For a reader-facing, line-by-line protocol narrative (including **CVHD** numerical knobs), use **`[[2016bal-2016-chemsci-doi-venue-direct-observation]]`**—this duplicate-ingest page stays short by design.

### Force-field training

**N/A —** application of literature **ReaxFF**, not a new parameterization (same as sibling).

### Static QM / DFT

**N/A —** same as sibling (no central DFT trajectory study for the CVHD runs).

## Findings

The **duplicate PDF** does not change the scientific conclusions summarized on **`[[2016bal-2016-chemsci-doi-venue-direct-observation]]`**: **CVHD** unlocks **low-T** chemistry on **second-scale effective times** for **oxidation** (**700 K**) and **millisecond-scale** windows for **pyrolysis** (**1000 K**), with **strong temperature dependence** of **products** and **mechanism** (**high-T β-scission / C₂-rich** vs **lower-T isomerization / heavier alkenes** in pyrolysis; **O₂-abstraction-driven** vs **pyrolysis-first** limiting cases in oxidation). Use the sibling page + **`pdf_path`** for figure-level detail.

## Limitations

CVHD introduces approximations distinct from brute-force MD; validation requires scrutiny of collective variables and time reconstruction. ReaxFF accuracy limits quantitative barrier heights and branching ratios for some channels.

## Relevance to group

Methodological reference for time-scale acceleration with reactive force fields in hydrocarbon oxidation networks.

## Citations and evidence anchors

- DOI: [10.1039/C6SC00498A](https://doi.org/10.1039/C6SC00498A)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
