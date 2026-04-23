---
id: paper:2022dasgupta-venue-paper
type: paper
title: "Development and application of ReaxFF methodology for understanding the chemical dynamics of metal carbonates in aqueous solutions"
updated: "2026-04-23"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:water-interfaces
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/d1cp04790f"
year: 2022
authors:
  - "Nabankur Dasgupta"
  - "Chen Chen"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "8889b438a6fdb286bc16d71ebfc6119b92488b1bd86643e06490b8445e082792"
pdf_path: "papers/Dasgupta_PCCP_carbonates_2022_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2022dasgupta-venue-paper -->

## Summary

Aqueous **carbonate** chemistry controls **pH**, **mineral dissolution**, and **electrolyte speciation** in geochemistry and in energy devices where **CO₂** interfaces with **brines** or **hydroxides**. Dasgupta, Chen, and van Duin extend **ReaxFF** to **metal carbonates** by adding **Na⁺**, **Ca²⁺**, **Mg²⁺**, and **CO₃²⁻** interactions consistent with existing **ReaxFF water** and **electrolyte** building blocks. The parameterization targets **DFT** data on **equations of state**, **formation and reaction enthalpies**, **angular distortions**, and **vibrational** benchmarks for condensed **carbonates/oxides** and selected **gas-phase clusters**. Subsequent **molecular dynamics** at **300 K** and **700 K** examines **solvation shells**, **ion diffusion**, and **speciation** between **carbonate** and **bicarbonate** forms in explicit water.

## Methods

**1 — MD application (atomistic dynamics).**
- **Engine / code:** LAMMPS with ReaxFF.
- **System size & composition:** Aqueous carbonate systems with Na/Ca/Mg carbonate chemistry in explicit water; atom counts and exact box compositions are not stated in the indexed extract.
- **Boundaries / periodicity:** N/A — boundary condition details are not stated in the indexed extract/galley text.
- **Ensemble:** NVT is reported for the validation trajectories.
- **Timestep:** N/A — timestep value is not stated in the indexed extract/galley text.
- **Duration / stages:** N/A — equilibration/production durations are not stated in the indexed extract/galley text.
- **Thermostat:** N/A — thermostat type and damping constants are not stated in the indexed extract/galley text.
- **Barostat:** N/A — NVT validation is described; no pressure-coupling/barostat setup is reported in the indexed extract.
- **Temperature:** 300 K and 700 K are the reported simulation temperatures (ambient vs supercritical-condition comparison).
- **Pressure:** N/A — pressure target/control is not stated in the indexed extract/galley text.
- **Electric field:** N/A — no applied electric field is reported.
- **Replica / enhanced sampling:** N/A — no umbrella sampling, metadynamics, or replica-exchange method is reported.
- **Electrostatics / cutoffs / QEq:** ReaxFF charge equilibration and nonbonded settings follow the LAMMPS ReaxFF implementation used in the study; numeric settings are not stated in the indexed extract.

**2 — Force-field training.**
- **Parent FF / elements:** ReaxFF parameterization extended for carbonate aqueous chemistry with C/H/O/Na/Ca/Mg interactions, built to be compatible with existing ReaxFF water/electrolyte descriptions.
- **QM reference:** VASP with PBE and PAW; plane-wave cutoff reported as 520 eV, with per-structure `k`-point meshes.
- **Training set:** Condensed-phase carbonate/oxide structures and gas-phase clusters, with targets including equations of state, reaction/formation enthalpies, angular distortions, and vibrational benchmarks.
- **Optimization:** Weighted ReaxFF fitting/optimization against the QM target set; exact optimizer settings/weights are not stated in the indexed extract.
- **Reference data used:** Comparisons to published computational/experimental references are used for validation context; no separate in-house experimental campaign is reported.

**3 — Static QM / DFT-only (as training data, not a standalone DFT application study).**
- **Functional:** PBE.
- **Dispersion:** N/A — dispersion correction details are not stated in the indexed extract.
- **Basis:** Plane-wave PAW framework (520 eV cutoff reported).
- **k-sampling:** Structure-dependent `k` meshes are reported.
- **Structures / pathways:** Carbonate/oxide condensed phases and selected gas-phase clusters for force-field fitting targets.
- **Properties computed:** EOS, reaction/formation energetics, angular distortions, and vibrational observables used to train/evaluate the ReaxFF parameterization.

## Findings

**1 — Outcomes and mechanisms.** The reported parameterization reproduces the targeted QM training observables for carbonate-related chemistries and enables aqueous reactive-MD analysis at ambient and supercritical-condition temperatures. Validation analyses emphasize solvation/coordination structure, ionic mobility trends, and carbonate/bicarbonate-sensitive local chemistry for Na/Ca/Mg systems.

**2 — Comparisons.** The paper compares fitted ReaxFF predictions against the underlying DFT reference set and against literature comparators used for RDF, coordination, and diffusivity-level behavior checks.

**3 — Sensitivity and design levers.** Temperature (300 K vs 700 K) is the explicit reported lever used to probe changes in aqueous carbonate dynamics and speciation behavior.

**4 — Limitations and outlook (as reported).** Applicability is bounded by the trained element/chemistry space (C/H/O/Na/Ca/Mg carbonate systems); extension to additional ion chemistries or conditions requires new parameterization/validation beyond this study.

**5 — Corpus / KB honesty.** The local source is a galley PDF with partial extract coverage, so this page avoids claiming numeric MD durations, pressure controls, or detailed thermostat/barostat constants that are not present in the indexed text; those should be copied from a local version-of-record PDF when available.
## Limitations

The corpus includes a **galley** PDF that may differ cosmetically from the final issue. Scientific scope is limited to chemistries represented in the training set; transfer to **transition metals**, **sulfates**, or **extreme pH** regimes requires additional validation. **Car–Parrinello** comparisons in the article are useful sanity checks for **proton-transfer** motifs but do not replace systematic **benchmarks** for every **mineral** **surface** of interest.

## Relevance to group

Foundational **ReaxFF** extension for **geochemical** and **electrolyte** carbonate systems led from the **van Duin** group.

## Citations and evidence anchors

- DOI: [10.1039/d1cp04790f](https://doi.org/10.1039/d1cp04790f)

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
