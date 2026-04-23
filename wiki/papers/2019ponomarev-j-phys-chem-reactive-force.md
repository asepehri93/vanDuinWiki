---
id: paper:2019ponomarev-j-phys-chem-reactive-force
type: paper
title: "Reactive Force Field for Simulations of the Pyrolysis of Polysiloxanes into Silicon Oxycarbide Ceramics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - method:reaxff
  - task:parameterization
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.9b03810"
year: 2019
authors:
  - "Ilia Ponomarev"
  - "Adri C. T. van Duin"
  - "Peter Kroll"
venue: "J. Phys. Chem. C 123:16804-16812 (2019)"
pdf_sha256: "e6af92d9a7287a5e59ef1a77131bdc5b2e70694769246e4b9e89baaa81788599"
pdf_path: "papers/Ponomarev_JPCC_SiCO_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019ponomarev-j-phys-chem-reactive-force -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below are **curated summaries** of the **J. Phys. Chem. C** article identified by **`doi`** and **`pdf_path`**. Parameter counts and training-data sizes are quoted from the publication text; treat **SI** tables as authoritative for numerical **FF** entries.

## Summary

The article develops a **new ReaxFF** parameterization for **Si–C–O–H** chemistry aimed at **silicon oxycarbide (SiCO)** ceramics and **polymer-to-ceramic** synthesis routes starting from **cross-linked polysiloxane** precursors. The scientific motivation emphasizes that **SiCO** combines attractive **thermal** and **mechanical** properties for applications from **thermal protection** to **electronics** and **energy storage**, but that **atomistic** modeling has been limited either by **DFT** cost or by **insufficient** empirical reactive models for the **amorphous**, **hydrogen-bearing** networks formed during **pyrolysis**.

The authors position their work against prior **ReaxFF** sets (notably **Newsome et al.** for **Si–C–O** contexts and later **Soria et al.** extensions), arguing those parameterizations can miss key **SiCO** features and produce inadequate structures for some **glass** and **free-carbon** morphologies. The abstract claims **extensive** validation against **experimental** and **computational thermochemistry**, **ab initio molecular dynamics** benchmarks at elevated temperature, and an application to **simulated polymer pyrolysis** producing **amorphous SiCO** with **graphene-like carbon segregations** embedded in an **oxycarbide matrix**, in qualitative agreement with experimental observations.

## Methods

**1 — MD application (polysiloxane pyrolysis).** **Molecular** **dynamics** in **LAMMPS**-class **RMD** codes (as in the **J. Phys. Chem. C** **article**): **large**-**scale** **reactive** **MD** converts **cross**-**linked** **polysiloxane** precursors toward **amorphous** **SiCO**; **3D** **PBC** **supercells** with **10⁴**-scale **atom** counts in the **reported** **pyrolysis** **runs** ( **confirm** in **text** / **SI**). **NVT** **thermostat**-**mediated** **ramped**-**T** **(temperature in K)** **schedules** with **timestep** in **sub**-**1** **fs** and **long**-**ns**-class **cumulative** **durations** as in **Main**+**SI**; **N/A** to restate every **K**-**ramp** **and** **equilibration** here. **Barostat** / **NPT** **/ hydrostatic** **pressure** **: ** **N/A** for **T**-**ramped** **NVT** **stages** unless a **NPT** **block** is **in** the **SI**. **External** **E**-**field**, **shock**, **umbrella**: **N/A** in the **stated** **RMD** **path**.

**2 — Force-field training (ReaxFF, Si–C–O–H, SiCO).** **Parent** set builds from **Newsome et al.** **Si–C–O** data plus **Srinivasan**-class **C–C** updates. **DFT** **library**: **>10,000** crystalline **SiCO**-type **hypothetical** **cells** and **>1000** **amorphous** models from **network** construction and **melt**–**quench** **AIMD**, in a **self**-**learning** **retraining** **loop**. **QM** **targets** include **thermochemistry** and **high-**T **AIMD**-style **comparisons**; **functionals** / **cutoffs** in the **DFT** **protocol** are in the **main** / **SI**. **Optimization** follows standard **ReaxFF** **least-squares** / **ParReaxFF**-class workflows as stated.

**3 — Static QM alone.** The paper uses **extensive** **DFT** **training**; **N/A** as a **standalone** static **only** result section separate from the **RMD** **application** above.

## Findings

### Mechanisms and morphology

The new field passes **thermochemistry**/**AIMD** checks emphasized in the abstract more faithfully than earlier **SiCO** attempts, enabling **long** **reactive** runs at **large** sizes. **Pyrolysis** simulations produce **amorphous SiCO** with **graphene-like carbon segregations** in an **oxycarbide** matrix—**qualitatively** aligned with **experiment** (figures in **Results**).

### Limitations / future validation

**SiCO** space is broad; **H content**, **T**, and **O/C stoichiometry** shift microstructures—case-by-case validation remains necessary.

## Limitations

**SiCO** composition space is vast; **hydrogen** content, **processing temperature**, and **oxygen** stoichiometry can all shift microstructure. **ReaxFF** remains an **empirical** model: **quantitative** **NMR**-level predictions and **long-range** **carbon** ordering may require **cross-validation** against **DFT** or **experiment** for each target composition. Training emphasizes **SiCOH** chemistry relevant to **polysiloxane** routes; **transfer** to unrelated **organosilicon** chemistries needs explicit checks.

## Relevance to group

**UT Arlington / PSU** collaboration combining **Kroll** group **SiCO** modeling with **van Duin**-line **ReaxFF** development—central to **ceramic** **pyrolysis** and **nanocarbon-in-glass** microstructures in the group’s materials portfolio.

## Citations and evidence anchors

- DOI [10.1021/acs.jpcc.9b03810](https://doi.org/10.1021/acs.jpcc.9b03810); *J. Phys. Chem. C* **2019**, **123**, 16804–16812.
- Excerpt alignment: `normalized/extracts/2019ponomarev-j-phys-chem-reactive-force_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
