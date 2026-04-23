---
id: paper:2018lotfi-journal-of-m-comparative-study
type: paper
title: "A comparative study on the oxidation of two-dimensional Ti3C2 MXene structures in different environments"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - domain:oxides-ceramics
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/C8TA01468J"
year: 2018
authors:
  - "Roghayyeh Lotfi"
  - "Michael Naguib"
  - "Dundar E. Yilmaz"
  - "Jagjit Nanda"
  - "Adri C. T. van Duin"
venue: "J. Mater. Chem. A"
pdf_sha256: "914c69bf385f9349479f617b3409bba40406584d3f462e790f2b071848e7bf8d"
pdf_path: "papers/Lotfi_Materials_A_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018lotfi-journal-of-m-comparative-study -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Two-dimensional Ti\(_3\)C\(_2\) MXene oxidizes rapidly in ambient air, complicating storage, processing, and integration into electronic or catalytic devices where surface chemistry must remain controlled. Lotfi et al. compare ReaxFF reactive molecular dynamics of MXene oxidation in dry air (O\(_2\)), wet air (O\(_2\) + H\(_2\)O), and hydrogen peroxide (H\(_2\)O\(_2\)) between 1000 K and 3000 K to separate the roles of oxidant strength, water-assisted oxygen transport, and temperature-driven titanium segregation toward surfaces. Companion X-ray diffraction and Raman measurements on heated samples corroborate qualitative simulation trends, especially the contrast between wet and dry air protocols that matter for laboratory handling strategies.

## Methods

### MD application (atomistic dynamics)

Reactive **molecular dynamics** with **ReaxFF** (Ti–C–O–H parameterization cited in *J. Mater. Chem. A*, `papers/Lotfi_Materials_A_2018.pdf`) compares oxidation of **Ti\(_3\)C\(_2\)** MXene in **dry air** (O\(_2\)), **wet air** (O\(_2\)+H\(_2\)O), and **H\(_2\)O\(_2\)**, plus **vacuum** heating as a no-oxidant baseline. The abstract reports temperature **series at 1000, 1500, 2000, 2500, and 3000 K** to accelerate chemistry within accessible MD windows; **time-resolved bond orders** track **Ti–C**, **C–C**, and **Ti–O** connectivity as oxidation proceeds. **Engine / code:** **N/A — MD package name** not stated on the indexed excerpt (`normalized/extracts/2018lotfi-journal-of-m-comparative-study_p1-2.txt`); confirm in the full **Methods**. **System size & composition, PBC vs open boundaries, ensemble (NVE/NVT/NPT), timestep, thermostat/barostat types, and pressure targets** are given in the article **Methods**/tables—**N/A — not transcribed** in this excerpt-based note. **Duration / stages:** **multi-stage** heating across the **1000–3000 K** program with **production** trajectory lengths in **ps**/**ns** tabulated in **Methods** (not duplicated here). **Electric field:** **N/A — not used** in the abstract-level protocol description. **Replica / enhanced sampling:** **N/A — not indicated** for this oxidation study in the indexed text.

### Experiments (validation)

Heating **MXene** in **wet vs dry air** followed by **X-ray diffraction** and **Raman** characterization is reported in the abstract as qualitative validation of the simulated oxidant ordering.
## Findings

**Outcomes and mechanism.** Oxidation rates follow **H\(_2\)O\(_2\) > wet air > dry air** at comparable temperatures in the simulations summarized in the abstract, consistent with stronger oxidant delivery for peroxide and humid air. **Raising temperature** increases oxidation rate and drives **Ti** toward surfaces while **Ti–C** connectivity drops and **Ti–O** / **C–C** bond-order metrics evolve as the MXene oxidizes. **Vacuum** heating converts the MXene toward **cubic TiC** with **little change** in the cited **Ti–C / Ti–O / C–C** bond-order picture aside from **topotactic** rearrangement—i.e., oxidants, not heat alone, gate the chemistry in that branch.

**Comparisons.** **XRD** and **Raman** on **heated MXene** in **wet vs dry air** are reported as supporting the simulated oxidant ordering at the qualitative level described in the abstract.

**Sensitivity.** Clear **temperature** and **oxidizing-environment** levers appear in the abstract’s multi-**K** program and three-gas-matrix design.

**Authored limitations / outlook.** ReaxFF supplies **qualitative** kinetics; **quantitative** ambient-time extrapolation is not claimed in the abstract-level summary used here (see **## Limitations** below and the article Discussion).

**Corpus honesty.** This page is grounded in **`pdf_path`** and the indexed extract; numerical supercell sizes and MD integrator settings should be taken from the **peer-reviewed PDF** if not duplicated above.
## Limitations

ReaxFF supplies qualitative kinetics; absolute rates require calibration to experiment. Elevated simulation temperatures accelerate chemistry within nanosecond windows and do not represent ambient oxidation timescales directly, so quantitative extrapolation to room-temperature storage requires separate modeling or experiment. Experimental XRD/Raman trends summarized in the article remain qualitative benchmarks for simulation.

## Relevance to group

Core **MXene + ReaxFF** application paper from the **group parameterization line**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1039/C8TA01468J` (`papers/Lotfi_Materials_A_2018.pdf`).

## Related topics

- [[reaxff-family]]
