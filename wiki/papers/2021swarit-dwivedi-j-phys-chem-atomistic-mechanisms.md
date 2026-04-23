---
id: paper:2021swarit-dwivedi-j-phys-chem-atomistic-mechanisms
type: paper
title: "Atomistic Mechanisms of Thermal Transformation in a Zr-Metal Organic Framework, MIL-140C"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - domain:organics-polymers-pyrolysis
  - material:oxide
  - task:parameterization
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.0c02930"
year: 2021
authors:
  - "Swarit Dwivedi"
  - "Malgorzata Kowalik"
  - "Nilton Rosenbach"
  - "Dalal S. Alqarni"
  - "Yun Kyung Shin"
  - "Yongjian Yang"
  - "John C. Mauro"
  - "Akshat Tanksale"
  - "Alan L. Chaffee"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. Lett."
pdf_sha256: "81ea79b4a48cf9cebb54f8ead140712e9551dc953fb723e0a94f152c8534789d"
pdf_path: "papers/Dwivedi_MOF_thermal_JPC_letters_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2021swarit-dwivedi-j-phys-chem-atomistic-mechanisms -->

## Summary

Thermal collapse of the **Zr**-based metal–organic framework **MIL-140C** is studied with **ReaxFF molecular dynamics** alongside **transmission electron microscopy (TEM)** of **decomposed** material, connecting **atomistic** **pyrolysis** chemistry to **nanoscale** **oxide** **cluster** **morphologies**. A **Zr/C/H/O** **ReaxFF** description is assembled from prior **zirconia** (**YSZ**-related) **Zr/O/H** training and **glycine**-derived **C/H/O** chemistry, then **reoptimized** against **DFT** data on **Zr–oxo** cluster models with **truncated carboxylate** linkers (**formate**/**benzoate**/**BDC**-like motifs), including **charges**, **geometries**, and **reaction energies**. The simulations follow **heating-induced** **degradation**, propose molecular pathways for **carbon monoxide** as a dominant **gaseous** product, and characterize residual **ZrO\(_x\)**-like clusters within **disrupted** **organic** matter.

## Methods

**1 — MD application (MIL-140C).** **Reactive** **molecular dynamics** in **LAMMPS** on **3D** **PBC** **MIL-140C** **supercells** (order 10⁴ **atoms**; **cell** and **heating** schedule in *JPCL*) uses **NVT** **thermostat** control, **sub-fs** **timestep**, and **ps**–**ns** **equilibration**/**ramp**/**production** to follow **linker** **scission** and **cluster** **evolution** at elevated **temperature** (**K**). **Barostat / isotropic** **pressure** coupling: **N/A** in the **summarized** constant-volume **pyrolysis** runs. **N/A — external** **uniform** **electric** **field**; **N/A — umbrella** / **metadynamics** in the standard runs.

**2 — Force-field training.** **Zr/C/H/O** **ReaxFF** merges **parent** **Zr/O/H** **data** (YSZ-related **equation-of-state** and **surface** **energies** for **ZrO\(_2\)**, **Mulliken** **charges** in the source) with **C/H/O** organics, then **reoptimi**zes against **M06-2X/6-31G(d,p)+LANL2DZ** **DFT** on **Zr\(_6\)O\(_4\)(OH)\(_4\)** **cluster** **geometries** with **truncated** **linker** **models** (**formate**/**BDC**-type). **One-parameter** **parabolic** **extrapolation** in the **ReaxFF** **optimizer** implements the **fit**; **TEM** of **decomposed** **samples** provides **experimental** **validation** of **nanoscale** **morphology** **trends** after **heating** **comparable** to **simulation**.

**3 — Experiments (TEM).** **TEM** on **thermally** **treated** **MIL-140C** is **compared** to **MD** **snapshots** for **cluster** size and **texture** (not a full in situ correlative **benchmark** of every **trajectory**).
## Findings

**Simulations** and **experiment** both indicate **very small** **ZrO\(_x\)** clusters embedded in **disrupted organic** regions, consistent with **high catalytic activity** reported for **decomposed MOFs** in the discussion. The **mechanism** analysis highlights **sequential** loss of **cross-linkers** before **vertically stacked** linkers, **CO**-producing pathways, and **oxidation states** of evolved **ZrO\(_x\)** approaching **tetragonal ZrO\(_2\)**-like behavior in the **model** under aggressive **heating**.

**Comparisons and sensitivity.** **TEM** and **MD** are **compared** at the **morphology** level; **thermal** **ramp** **rate** and **hold** **temperature** are the main **levers** for which **reaction** channels are sampled. **Corpus / PDF** has full **protocols**.

## Limitations

**Cluster** models and **truncated linkers** in the training set approximate full **MIL-140C** complexity; **long-time** **mesoscale** **porosity** collapse and **gas** **transport** are only partially accessible in **nanosecond** **MD**.

## Relevance to group

Group co-authorship on **reactive MD** of **MOF** **thermal** chemistry with explicit **ReaxFF** **parameterization** to **Zr-organic** systems. **Training** **clusters** include **Gaussian** **DFT** **single-point** energies and **relaxed** **geometries** for **Zr–oxo** nodes with **truncated** **linkers**; reproduce those **clusters** before attempting **parameter** **merges** with unrelated **Zr/O** sets. **Thermal** **ramp** rates and **total** **simulation** times for **MIL-140C** degradation appear in the **JPCL** article and govern which **reaction** channels are sampled within **nanosecond** **MD** trajectories.

## Reader notes (navigation)

- [[reaxff-family]]

Cross-link **MOF** **thermal** **decomposition** questions to **`[[theme-pyrolysis-combustion-organics]]`** and **experimental** **TEM** **SI** in the **JPCL** article when users need **mesoscale** **morphology** beyond **atomistic** **snapshots** from **MD**.
