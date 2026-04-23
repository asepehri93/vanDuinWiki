---
id: paper:2017tomas-carbon-119-2-structural-prediction
type: paper
title: "Structural prediction of graphitization and porosity in carbide-derived carbons"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:thermal-decomposition
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.04.004"
year: 2017
authors:
  - "Carla de Tomas"
  - "Irene Suarez-Martinez"
  - "Fernando Vallejos-Burgos"
  - "María J. López"
  - "Katsumi Kaneko"
  - "Nigel A. Marks"
venue: "Carbon 119, 1–9 (2017)"
pdf_sha256: "b0eda28d65fa72bc4cf66ff4b2924876e2abcbe860df201affc4494b6cedf060"
pdf_path: "papers/Others/Prediction of CDC structure Marks 2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017tomas-carbon-119-2-structural-prediction -->

## Summary

Carbide-derived carbons (CDCs) are nanoporous materials formed by selectively etching non-carbon atoms from carbide precursors, yielding tunable pore size distributions and disordered graphitic domains. This paper presents a mimetic atomistic workflow that uses molecular dynamics with the environment-dependent interaction potential (EDIP) for carbon to build CDC-like networks after simulated removal of metal/metalloid species, then thermally processes the structures to follow graphitization trends. An Arrhenius-based time–temperature mapping relates simulation temperatures to experimental synthesis temperatures to bridge timescale gaps.

## Methods

### 1 — MD application (atomistic dynamics)

The authors develop a **mimetic MD workflow** for **carbide-derived carbon (CDC)**-like networks using **molecular dynamics** with the **environment-dependent interaction potential (EDIP)** for carbon (*Carbon* **119**, 1–9, **2017**). Starting from a **carbide-like** parent, **non-carbon** species are removed to mimic **etching**, then the **carbon skeleton** is **thermally annealed** to study **graphitization** vs **temperature** with **pore** metrics extracted from relaxed **amorphous** structures. An **Arrhenius-based** mapping relates **simulation temperature** to **experimental synthesis temperature** to bridge timescales.

- **Engine / code:** **EDIP** carbon potential in an **MD** code as reported in the article (**not** ReaxFF).
- **System size & composition:** **Amorphous carbon** networks with **nanoscale porosity** after mimetic etch + anneal; explicit atom counts per protocol step are in **`pdf_path`**.
- **Boundaries / periodicity:** **N/A** — **PBC** details not restated in `normalized/extracts/2017tomas-carbon-119-2-structural-prediction_p1-2.txt`; confirm in PDF.
- **Ensemble:** **N/A** — **NVT/NPT** labels not stated in the indexed excerpt.
- **Timestep:** **N/A** — **Δt** not stated in the indexed excerpt.
- **Duration / stages:** **N/A** — anneal schedule lengths not stated in the indexed excerpt.
- **Thermostat:** **N/A** — not stated in the indexed excerpt.
- **Barostat:** **N/A** — not stated in the indexed excerpt.
- **Temperature:** **Effective temperature** sweeps (mapped to experiment via **Arrhenius** scaling in the article) control **graphitization** extent.
- **Pressure:** **N/A** — not summarized on indexed pages.
- **Electric field:** **N/A** — not used.
- **Replica / enhanced sampling:** **N/A** — conventional **annealing MD**.

### 2 — Force-field training

**N/A** — **EDIP** is used as a **published** **fixed** carbon model; no new **QM** refit is reported as the headline contribution.

### 3 — Static QM / DFT-only

**N/A** for large **amorphous** generation—**EDIP MD** drives **covalent** **C–C** topology changes without explicit **oxidative** **etchant** chemistry.

### 4 — Comparison to experiment (literature)

The abstract states the mimetic **MD + EDIP** approach reproduces main **experimental CDC** motifs: **disorder** at lower effective **T**, progressive **graphitization** with increasing **T**, and **nanometre-scale porosity** consistent with **TEM/XRD/Raman** phenomenology cited in the introduction.

## Findings

### Outcomes and mechanisms

**Simulated CDC models** capture the **disordered** microstructure at lower effective temperatures, **graphitic** ordering that strengthens with increasing temperature, and **nanoscale pores** consistent with **CDC** literature trends described in the abstract.

### Comparisons

The workflow is positioned against purely **geometric** slit-pore models and **reconstructive** (**RMC/HRMC**) approaches: it is **predictive** (no experimental scattering input required) but must still be checked against **experiment** when claiming a specific **PSD**.

### Sensitivity / design levers

**Anneal temperature** (and the **Arrhenius** mapping to laboratory **synthesis T**) is the primary knob for **graphitization** vs **porosity** tradeoffs in the mimetic scheme.

### Limitations and corpus honesty

**Halogenation chemistry** and **heteroatom** removal are **idealized** relative to real **chlorine** **CDC** processing; **EDIP** cannot represent **oxidative** surface chemistry that **ReaxFF** might treat elsewhere in the corpus. Quantitative **pore size distributions** and **Raman**-comparable metrics should be taken from **`pdf_path`**, not this summary.


## Limitations

Etching chemistry is idealized relative to laboratory halogenation pathways; EDIP cannot capture oxidation chemistry treated by ReaxFF in related corpus entries.

## Corpus notes

Downstream adsorption studies should archive which EDIP-generated CDC snapshot was used as input, because pore metrics can shift with the random seed used during mimetic etching even when global thermodynamic trends match experiment.

For MAS retrieval, pair this entry with classical carbon potential discussions (`EDIP`, `AIREBO`, `ReaxFF`) so users understand which chemistry is explicitly modeled versus intentionally omitted.

If you need reactive oxygen chemistry on CDC surfaces, plan a follow-on ReaxFF study rather than stretching EDIP beyond its intended covalent carbon regime.

## Relevance to group

Complements **ReaxFF carbon** work by supplying classical nanoporous carbon frameworks for sorption and support modeling.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2017.04.004](https://doi.org/10.1016/j.carbon.2017.04.004)

## Related topics

- [[reaxff-family]]
