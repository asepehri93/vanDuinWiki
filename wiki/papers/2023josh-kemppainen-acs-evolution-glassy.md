---
id: paper:2023josh-kemppainen-acs-evolution-glassy
type: paper
title: "Evolution of Glassy Carbon Derived from Pyrolysis of Furan Resin"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:carbon-hydrocarbon
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
doi: "10.1021/acsaenm.3c00360"
year: 2023
authors:
  - "Josh Kemppainen"
  - "Ivan Gallegos"
  - "Aaron S. Krieg"
  - "Jacob R. Gissinger"
  - "Kristopher E. Wise"
  - "Margaret Kowalik"
  - "Julia A. King"
  - "S. Gowtham"
  - "Adri van Duin"
  - "Gregory M. Odegard"
venue: "ACS Appl. Eng. Mater. 2023, 1, 2555–2566"
pdf_sha256: "7e958c4c525d34ba53ca990200dcca584ca0dcf37bf325c60e97c99c08b73c7d"
pdf_path: "papers/Kemppainen_furan_pyrolysis_ACS_Appl_Eng_Mater_2023_2555.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023josh-kemppainen-acs-evolution-glassy -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **ACS Appl. Eng. Mater.** (**DOI** in front matter). Numerical metrics (**density**, **modulus**, **sp² fraction**, **XRD**-derived lengths) must match the **article tables**; this page summarizes the workflow at narrative level.

## Summary

The study couples **ReaxFF-based reactive molecular dynamics** with **new experimental measurements** to trace how **poly(furfuryl alcohol)**—a **furan resin** precursor—**polymerizes** into a **cured** network and then **pyrolyzes** toward **glassy carbon**. The motivation is **renewable-precursor** **carbon** materials relevant to **C/C composites** and related applications where **pyrolysis** controls **microstructure** and **mechanical** properties. The authors position **furan-derived** glassy carbon as a distinct branch of the broader **polymer-derived carbon** literature and seek **quantitative** alignment between simulation and experiment across **density**, **elastic modulus**, **char yield**, **sp² carbon fraction**, and **XRD-derived** descriptors such as **interlayer spacing** (**d₀₀₂**), **in-plane crystallite size** (**Lₐ**), and **stacking height** (**L꜀**).

## Methods

### Software and numerics (B)

**LAMMPS** **ReaxFF** **reactive MD** per **Computational Methods** (**timestep**, **thermostat/barostat**, **system size**—read the **PDF**).

### Curing / polymerization

**Poly(furfuryl alcohol)** **polycondensation** initialized using **Table 1** product **mole** fractions and pathways summarized around **Figure 1**; compare simulated **density** and **Young’s modulus** of **cured** resin to **experiment**.

### Pyrolysis

**High-T** reactive MD with **inert** heating schedules and **volatile** handling (including **mass-loss** algorithms referenced in the article).

### Structural diagnostics

Track **mass loss**, **C content**, **sp²** fraction, **d₀₀₂**, **Lₐ**, **L꜀** vs **experiment**/**literature** for **furan-derived** glassy carbon.

The article’s **Computational Methods** narrative (see **PDF**) specifies **LAMMPS** integration parameters, **thermostat/barostat** choices, and **system sizes** for **cured** vs **pyrolyzed** cells; this wiki page does **not** duplicate those tables—use **`pdf_path`** when reproducing trajectories or comparing to other **furan**/**phenolic** pyrolysis studies in the corpus.

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** with **ReaxFF** (see **Computational Methods** in `pdf_path`). **System & composition:** **cured** poly(furfuryl alcohol) and **pyrolyzed** glassy-carbon cells; sizes follow **Table 1** and **Figure 1** pathways in the article. **Boundaries / periodicity:** **3D PBC** for bulk **resin**/**carbon** as in the published protocol. **Ensemble, timestep, temperature schedules, barostat, production length:** the **cured**-resin and **pyrolysis** **protocols** use **NVT**/**NPT** **stages** with **fs** **timesteps** and **multi-ns**-scale **trajectories** as tabulated; **N/A** on this page for full **NVT**/**NPT** **narratives** and **per-stage** **ns** **durations**—read the **ACS Appl. Eng. Mater.** **tables**. **Pressure:** as reported if **NPT** stages are used. **Electric field, shear, shock, enhanced-sampling:** **N/A** — not part of the summarized workflow.

### 2 — Force-field training

**N/A** — the paper **applies** a **ReaxFF** model to **furan** **curing** and **pyrolysis** for validation against **experiment** and literature **XRD** metrics, rather than reporting a new fit.

### 3 — Static QM

**N/A** — the publication is **reactive MD** + **experiment**; DFT is not the central protocol block.

## Findings

### Agreement claims (abstract-level)

**Cured** models match **experimental** **ρ** and **E** within uncertainties; **pyrolyzed** models align with **literature** glassy-carbon metrics for **furan** routes—supporting **precursor screening** for **C/C** applications.

### Mechanistic detail

Radical pathways and **turbostratic** evolution are in **Results**/**figures**—not duplicated here.

At abstract level, the authors report agreement between **simulated** and **measured** **cured** **density**/**modulus** and show that **pyrolyzed** **ReaxFF** models reproduce **literature** **glassy-carbon** **XRD** metrics for **furan** routes—supporting the use of **atomistic** pyrolysis models as **qualitative** **precursor** screeners for **renewable** **C/C** routes.

**Compared** to **laboratory** **pyrolysis**, the **kinetic** **reaction** network in **furan** **char** (e.g. **turbostratic** **reorganization**) is only partially captured, and the **sensitivity** of final **L\(_a\)**, **L\(_c\)**, and **sp²** **carbon** **fraction** to **furnace** **temperature** **ramps** may exceed what **short** **ns** **NVT**/**NPT** **stages** resolve; the **Limitations** section (below) notes time-scale and **ReaxFF** **approximations**, and the **definitive** **numbers** remain the **version-of-record** **PDF** at `pdf_path`.

## Limitations

**MD pyrolysis** uses **high heating rates** and **nanoscale** cells relative to laboratory **furnace** runs; **kinetic** pathways and **mesoscale** **porosity** may differ. **ReaxFF** accuracy for **oxygenated** intermediates and **aromatic** growth should be checked when extending to different **additives** or **mineral** fillers.

## Relevance to group

**van Duin**-affiliated **ReaxFF pyrolysis** pipeline for **renewable furan** precursors—complements **phenolic** and other **carbonization** studies such as **`paper:2023gallegos-carbon-trend-establishing-physical`**.

## Citations and evidence anchors

- DOI [10.1021/acsaenm.3c00360](https://doi.org/10.1021/acsaenm.3c00360).
- Excerpt alignment: `normalized/extracts/2023josh-kemppainen-acs-evolution-glassy_p1-2.txt`.

## Related topics

- [[2023gallegos-carbon-trend-establishing-physical]]
- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
