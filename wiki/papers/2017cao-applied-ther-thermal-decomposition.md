---
id: paper:2017cao-applied-ther-thermal-decomposition
type: paper
title: "Thermal decomposition of HFO-1234yf through ReaxFF molecular dynamics simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:reactive-md
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1016/j.applthermaleng.2017.07.104"
year: 2017
authors:
  - "Yu Cao"
  - "Chao Liu"
  - "Hao Zhang"
  - "Xiaoxiao Xu"
  - "Qibin Li"
venue: "Appl. Therm. Eng."
pdf_sha256: "dbada2a1911b9c5e2036b955cd57f07aed275d1ffe15ef2c4efea9224eecee45"
pdf_path: "papers/ReaxFF_others/Cao 2017 Thermal decomposition of HFO-1234yf through ReaxFF molecular dy....pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017cao-applied-ther-thermal-decomposition -->

## Summary

**Hydrofluoroolefin (HFO) refrigerants** such as **HFO-1234yf** are deployed for lower global-warming potential than legacy hydrochlorofluorocarbons, but **thermal stability** in compressors, heat exchangers, and fault scenarios remains an engineering concern. Cao *et al.* apply **ReaxFF molecular dynamics** to **HFO-1234yf** reacting in **molecular oxygen** over **1900–3500 K**, a regime where **pyrolysis** and **oxidation** compete. The abstract organizes results around sequential **bond activations**, emergence of oxygenated intermediates, terminal **HF/fluorocarbon oxide/CO₂** products, and a compact **pathway** accounting that highlights **radical chain carriers**.

## Methods

**MD application (ReaxFF).** The study uses **ReaxFF molecular dynamics** for **C/H/F/O** chemistry; the article ties its **parameterization** to prior **QM-trained** **combustion / organofluorine** **ReaxFF** work via the reference list and **Methods** (exact **force-field** identifier is given there).

**Systems and conditions** target **gas-phase** **thermal decomposition** of **HFO-1234yf** (**2,3,3,3-tetrafluoropropene**) with **molecular O₂** at **1900–3500 K** (range stated in the abstract). **Periodic (PBC)** supercell stoichiometry, **density**, **atom counts**, and **oxygen excess** are given in the journal **Methods**; this wiki page does **not** reproduce those tables from the short front-matter extract.

**Observables** are read from trajectories: **primary product formation pathways** (the abstract highlights **ten** channels at the level of their analysis), time-dependent **radical inventories** (**•CF₃**, **•F**, **•H**, **FCOO•**, **HOO•**, **•OH** among the named species), and **chain transfer** emphasized through **HOO• → •OH** interconversion during **oxidation**.

**Force-field training** is **N/A** (**off-the-shelf** parametrization). **Static QM** and **electric-field / enhanced-sampling** workflows are **N/A** for the core claim of the paper.

**Reproducibility detail** (**MD software**, **ensemble**, **timestep**, **thermostat/barostat**, **equilibration vs production time**, **PBC** lattice vectors, **pressure**) is specified in *Appl. Therm. Eng.* **§2–3** and any **SI**—consult the **PDF** rather than this excerpt-grounded note.

**MD blueprint honesty.** **Gas-phase** cells use **PBC** as described in the article. Explicit **NVT**/**NPT**/**NVE** labels, **MD engine** (**LAMMPS** is common for **ReaxFF**—confirm), **timestep**, **thermostat**/**barostat**, **equilibration**/**production** lengths (**ps**/**ns**), and whether **pressure** is controlled are **N/A** on this page because they are not recoverable from the short indexed extract—read *Appl. Therm. Eng.* **Methods**.

## Findings

**Pyrolytic** activation begins with **C–C**, **C–H**, and **C–F** scission near **2100 K**, populating small **fluorinated radicals** that seed downstream chemistry. **Oxidation chemistry** intensifies near **2500 K**, where oxygenated intermediates such as **H₂O**, **CF₃OH**, and **FCOOH** appear along routes that ultimately funnel to **HF**, **COF₂**, and **CO₂** as major **terminal** products in the ReaxFF trajectories—consistent with experimental product references cited in the paper. The authors summarize **ten** **primary-product formation pathways** resolved at the level of their analysis and argue that **radical concentrations**—not only temperature—control reactivity, with **HOO• → •OH** transfer acting as a principal **chain carrier** in their mechanism picture. For **engineering** readers, the study is best read as a **qualitative map** of **high-temperature** **HFO** chemistry: absolute **rates** will depend on **pressure**, **transport**, and **ReaxFF** parameter sensitivity analyses beyond the abstract-level summary captured here. The **Applied Thermal Engineering** venue signals interest in **heat-exchanger** and **compressor** fault temperatures where **refrigerant** **decomposition** can foul surfaces or alter **working-fluid** **composition**.

## Limitations

High-temperature ReaxFF chemistry can be **qualitative**; quantitative kinetics should be checked against experiment and sensitivity analysis in the paper. **Facility** studies of **HFO** decomposition should also account for **catalytic** **surfaces** absent in these **gas-phase** reactive MD cells. **Pressure** and **density** choices in the MD setup control **collision** frequencies; compare them carefully when mapping to **combustion** **reactor** conditions.

## Relevance to group

Applied **ReaxFF** study of **fluorocarbon refrigerant** decomposition relevant to **combustion/thermal stability** of working fluids.

## Citations and evidence anchors

- DOI: `10.1016/j.applthermaleng.2017.07.104`.

## Related topics

- [[reaxff-family]]
