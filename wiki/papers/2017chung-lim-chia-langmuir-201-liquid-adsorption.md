---
id: paper:2017chung-lim-chia-langmuir-201-liquid-adsorption
type: paper
title: "Liquid Adsorption of Organic Compounds on Hematite α-Fe2O3 Using ReaxFF"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.7b02374"
year: 2017
authors:
  - "Chung-Lim Chia"
  - "Carlos Avendaño"
  - "Flor R. Siperstein"
  - "Sorin Filip"
venue: "Langmuir"
pdf_sha256: "f31ad95a27db2f3985f474765798777e46f6aa78f9ea595b945f59dfcf376090"
pdf_path: "papers/ReaxFF_others/Chia_Langmuir_Fe2O3_organic_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017chung-lim-chia-langmuir-201-liquid-adsorption -->

## Summary

**ReaxFF-based MD** studies **organic liquids** on **hematite α-Fe2O3**, contrasting a **frozen** surface with a **flexible** surface where **partial charges** can evolve. **Polarity** of the solvent (ethanol vs toluene vs iso-octane) affects **surface atom displacements** and **surface polarization**. Flexible-surface runs show **stronger electrostatic coupling** and **better-defined yet less ordered** adsorbed layers than the rigid case, with implications for **transferable FF parametrization** from vacuum slabs. The **Langmuir** study targets **industrial** **solvent**–**oxide** contacts where **interfacial** **electrostatics** can dominate **adsorption** **structure** even without **strong** **chemisorption**.

## Methods

**MD application (ReaxFF).** **Reactive MD** builds **Fe-terminated α-Fe₂O₃ (0001)** slabs with **in-plane PBC** and **liquid** overlayers of **ethanol**, **toluene**, or **iso-octane** spanning a **polarity** ladder. **ReaxFF** parameters and **surface** **crystallography** follow the references cited in *Langmuir*. Two **substrate treatments** are compared: a **frozen** oxide lattice versus a **flexible** lattice where **partial charges** evolve during dynamics (**QEq**-class coupling as described in the article), intended to capture **metal–oxygen** **relaxation** and **interfacial polarization** absent in rigid-ion **clay-FF** workflows tuned on **non-reactive** oxides.

**Atom counts**, **cell vectors**, **liquid film thickness**, **temperature**, **ensemble**, **timestep**, **thermostat/barostat**, and **equilibration/production schedules** are specified in *Langmuir* **Methods**/**SI** and are **not transcribed** from the short indexed extract used here.

**Force-field training** is **N/A** (**literature** **Fe–O–C/H** set). **Static QM** is **N/A** as the primary methodology in the indexed introduction.

**MD blueprint honesty.** **Reactive molecular dynamics** on **PBC** **α-Fe₂O₃** **slabs** with **liquid** films is the workflow class. **LAMMPS** (or the code named in *Langmuir*) should be confirmed in the **PDF**. **NVT**/**NPT**/**NVE** assignment, **timestep**, **thermostat**, **barostat**/**pressure** control for interfacial cells, and **equilibration**/**production** durations (**ps**/**ns**) are **N/A** on this page—read *Langmuir* **Methods**/**SI**.

## Findings

**Outcomes:** on **flexible** hematite, **surface atom displacements** and **surface polarization** grow with **adsorbate polarity** (**ethanol > toluene > iso-octane** in the polarity ordering used by the authors). **Layering:** **flexible** models give **sharper yet less ordered** interfacial layers than **rigid** slabs because **charge rearrangement** strengthens **electrostatic** coupling across the outermost **Fe–O** layers. **Comparisons:** **rigid** vs **flexible** substrate models are contrasted directly; authors also position **ReaxFF** against **classical** oxide **force fields** tuned on **non-reactive** surfaces. **Sensitivity:** **polarity** of the solvent is the main lever discussed for **interface** structure. **Limitations / outlook:** authors caution that **vacuum-fitted** **oxide charges** can misrepresent **polar liquid** contacts—**transferable** parametrization must include **interfacial polarization**. ## Limitations

Only **three solvents** and one **termination** of **(0001)**; broader **coverage**, **defects**, and **reactive** chemistry are outside the stated scope. **Numerical protocol and plots** should be read from the **VOR PDF**/**SI**.

## Relevance to group

Demonstrates **ReaxFF** for **oxide–organic liquid interfaces** and **electrostatically active** surfaces—relevant to **corrosion, lubrication, and interfacial** simulation practice.

## Citations and evidence anchors

- DOI: [10.1021/acs.langmuir.7b02374](https://doi.org/10.1021/acs.langmuir.7b02374)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
