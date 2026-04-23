---
id: paper:2023gallegos-carbon-trend-establishing-physical
type: paper
title: "Establishing Physical and Chemical Mechanisms of Polymerization and Pyrolysis of Phenolic Resins for Carbon-Carbon Composites"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:validation-experiment
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1016/j.cartre.2023.100290"
year: 2023
authors:
  - "Ivan Gallegos"
  - "Adri van Duin"
  - "Gregory M. Odegard"
venue: "Carbon Trends"
pdf_sha256: "e790f170bada93459f9a0b129440b87aecd0a1a7247a385ba3f2ea2946ae16c4"
pdf_path: "papers/Gallegos_Carbon_Trends_2023_100290.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023gallegos-carbon-trend-establishing-physical -->

## Summary

**Reactive MD (ReaxFF)** workflows model **full phenolic-resin polymerization** and subsequent **high-temperature pyrolysis** toward **carbon–carbon composite** matrices, with **mass density**, **elastic moduli**, and **carbon microstructure metrics** compared to **experiment** and **X-ray**-derived **graphitic** parameters. The study is positioned as a **materials-by-design** bridge between **atomistic** reaction pathways during curing and pyrolysis and **engineering** figures of merit (density, modulus, graphitic stacking metrics) that can be compared directly to **laboratory** measurements on phenolic-derived carbons used in **thermal protection** and **structural** composite applications.

The *Carbon Trends* framing also stresses **phenolic** chemistry as a **heritage** route to **C/C** components where **processing** controls **matrix** **density**, **stiffness**, and **graphitization**, motivating a workflow where **ReaxFF** supplies **bond-resolved** **polymerization** and **pyrolysis** pathways that can be checked against **NASA**/**MTU**-style **experimental** benchmarks cited in the article.

## Methods

### ReaxFF workflow (A/B)

**ReaxFF** in **LAMMPS** for **bond-making/breaking** during **curing** and **pyrolysis** (parameter lineage in article).

### Polymerization stage

**Condensation/crosslinking** to **3D** phenolic networks; extract **mass density** and **Young’s modulus** from relaxed cells.

### Pyrolysis stage

**High-T** reactive MD with **volatile removal**; characterize **amorphous/nanographitic** carbon via **RDFs**, **ring statistics**, **interlayer spacing**, **crystallite height**—aligned with **XRD** metrics.

### Validation

Compare to **experimental** **density/modulus** and **X-ray**-derived **graphitic** parameters for **phenolic-derived** carbons.

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** with **ReaxFF** for bond making and bond breaking during phenolic **polymerization** and **pyrolysis** (parameter set cited in the paper). **System & composition:** crosslinked **phenolic** supercells and high-temperature **pyrolysis** products; atom counts and stoichiometry are in the article, not restated on this page. **Boundaries / periodicity:** three-dimensional **PBC** for bulk condensed phases. **Ensemble, timestep, thermostat, barostat, equilibration/production length:** the **published** **protocol** uses **NVT** and/or **NPT**-style **stages** with **ps**–**ns**-scale **equilibration** and **production** as tabulated; **N/A** for duplicating every **NVT**/**NPT** block on this page—the *Carbon Trends* **Computational** section and tables in `pdf_path` are authoritative. **Temperature:** high-T **pyrolysis** and property-evaluation setpoints as defined there. **Pressure / stress control:** **N/A** in this short summary (use the article if isobaric equilibration is reported). **Electric field, shear, shock, enhanced-sampling MD:** **N/A** — not part of the described protocol.

### 2 — Force-field training

**N/A** — the study **applies** a ReaxFF description to phenolic **polymerization**/**pyrolysis** and carbon microstructure; **de novo** reparameterization in this paper is not the abstract’s emphasis (see article for lineage and any adjustments).

### 3 — Static QM

**N/A** — not a DFT benchmark paper; the introduction cites DFT in prior literature on related chemistries for context only.

## Findings

### Cured polymer models

**ρ ≈ 1.24 ± 0.01 g cm\(^{-3}\)**, **E ≈ 3.50 ± 0.64 GPa**, matching experimental ranges in the abstract.

### Pyrolyzed carbon structure

**d-spacing ≈ 3.81 ± 0.06 Å**, **crystallite height ≈ 10.94 ± 0.37 Å** vs **X-ray** references; **skeletal density ≈ 2.01 ± 0.03 g cm\(^{-3}\)** (per paper’s pore-exclusion definition).

### Mechanical benchmark gap

**E ≈ 122 ± 16 GPa** for pyrolyzed carbon **underpredicts** experimental **~146–256 GPa** ranges cited for comparable **nanoscale** amorphous carbons.

Taken together, the **cured**-resin and **pyrolyzed**-carbon **ReaxFF** **trajectories** link **condensation**/**crosslinking** to **turbostratic** **graphitic** order parameters **compared** with **X-ray** references; the **sensitivity** of this property set to **anneal** **temperature** and to **kinetic** under-sampling is a **limitation** the **authors** acknowledge when contrasting **modulus** to **laboratory** amorphous carbons. **Numerical** values and **uncertainties** on this page follow the **abstract** and **tables** in the **PDF** at `pdf_path`—**not** a substitute for pagination when citing externally.

## Limitations

ReaxFF errors for **reaction barriers** and **carbon reactivity** can be substantial; long annealing times and experimental microstructures may not be fully captured. **Sample sizes** and **simulation duration** in the article should be read alongside the **experimental** uncertainty bands when interpreting modulus or graphitization metrics; **continuum** fiber architectures and **interfiber** porosity in real composites are not represented at full engineering scale in the atomistic models. When citing **numerical** values from this wiki page, prefer the **tables** and **error bars** in the **peer-reviewed** PDF because **rounding** here is for readability only.

## Relevance to group

**van Duin**-affiliated **ReaxFF pyrolysis** study for **C/C composites** and **TPS** materials, paired with **NASA Langley** / **MTU** experimental validation.

## Citations and evidence anchors

- DOI: [10.1016/j.cartre.2023.100290](https://doi.org/10.1016/j.cartre.2023.100290)

## Related topics

- [[2023josh-kemppainen-acs-evolution-glassy]]
- [[reaxff-family]]
