---
id: paper:2020jiang-proceedings-reactive-electron
type: paper
title: "Reactive and electron force field molecular dynamics simulations of electric field assisted ethanol oxidation reactions"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:combustion
  - keyword:reactive-md
  - keyword:reaxff-application
  - keyword:lammps
source_refs: []
doi: "10.1016/j.proci.2020.06.318"
year: 2020
authors:
  - "Xi Zhuo Jiang"
  - "Kai Hong Luo"
venue: "Proc. Combust. Inst. (2020); open access"
pdf_sha256: "e6632ede5725844fa71a4c7f8e579ec28b8e09372bdcc9ef6aa594a8abe0fcbb"
pdf_path: "papers/ReaxFF_others/Jiang_Luo_ReaxFF_efield_ProcCombInst_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020jiang-proceedings-reactive-electron -->

## Summary

The authors couple **ReaxFF molecular dynamics** with **electron force field (eFF) molecular dynamics** to study how **external electric fields** influence **ethanol oxidation** at **atomistic** and **subatomic (electronic)** levels. **ReaxFF** simulations (21 runs reported in the abstract) show a **two-stage** oxidation picture where fields alter **decomposition** kinetics and later steer **O₂-involving** pathways; **eFF** simulations (35 runs) estimate **electron energy** shifts on **10–100 kJ/mol** scales, extending the interpretation beyond classical bond order. The motivation section ties **electric-field-assisted combustion** to practical **plasma-assisted** and **low-temperature** ignition contexts where fields may couple to chemistry through both **collisional** heating and **electronic** effects—motivating a **dual-level** simulation strategy (introduction themes; abstract).

## Methods

**1 — MD application (ReaxFF and eFF).** The work combines **ReaxFF** reactive MD and **electron force field (eFF)** MD for **gas-phase ethanol oxidation** with an **external static electric field** in the **x** direction. The **abstract** reports **21** ReaxFF and **35** eFF runs in total. **ReaxFF** uses a **C/H/O parameter set** for ethanol oxidation as introduced in the article’s **Sec. 2.1** (standard ReaxFF energy decomposition; refs. [20–23] in the **PDF**). **Field strengths** along **x** include **2×10⁴**, **5×10⁴**, **2×10⁵**, **5×10⁵**, **2×10⁶**, and **5×10⁶** **V m⁻¹** plus a **no-field** baseline (indexed **Proc. Combust. Inst.** PDF, Sec. 2.1). **N/A —** this wiki does not copy **ensemble**, **timestep (fs)**, **thermostat**, **barostat**, **cell composition**, and **PBC** details (see full **PDF** for setup tables). **Duration / production run length** in **ps** or **ns** per case: use the **article** (not transcribed here). If the primary text uses only **NVT** / fixed volume for these gas systems, **barostat / hydrostatic pressure control: N/A** for the corresponding stages. **Target temperature (K):** follow **Sec. 2** of the **version-of-record** (combustion-relevant **K**; not tabulated in this note). **Static/oscillating field:** the manuscript applies the **E-field in MD** as described in Sec. 2. **Electric field in MD: yes** (listed strengths above), not an **N/A** “no field” case. **Enhanced sampling:** **N/A —** not called out in the **indexed excerpt** (no umbrella / metadynamics in the short extract).

**2 — Force-field training.** **N/A —** the paper **uses** published ReaxFF and eFF models; it is not a new parameterization study.

**3 — Static QM / DFT-only.** **N/A —** main results are from **ReaxFF** and **eFF** MD, not a standalone DFT static study.

## Findings

**Outcomes and mechanisms.** ReaxFF data are interpreted as a **two-stage** ethanol oxidation: **(i)** **decomposition** of ethanol, then **(ii)** chemistry involving **O₂**. In **stage 1**, the field is said to influence the decomposition rate by changing **kinetic energies** of C-containing species on **~100–1000 kJ mol⁻¹** scales and by altering **conformations** that modulate **bond dissociation**. In **stage 2**, the field is said to affect **reaction pathways** as well as energies. **eFF** results give **order-of-magnitude ~10–100 kJ mol⁻¹** changes in **electron** energy, extending the story to subatomic (electronic) response (see **abstract** and **PDF** **sections/figures**).

**Comparisons, outlook, corpus honesty.** The text connects to debates on **ionic wind** (momentum transport) vs **chemistry**-driven field effects; the **abstract** states the work can support both views in different regimes. For **replicability**, **E-field** schedules, **densities**, and **any** time-step/ensemble choices must follow the **version-of-record** at `pdf_path` (**Proc. Combust. Inst.**, open access), not this short wiki alone.

## Limitations

Coupling **ReaxFF** and **eFF** involves different approximations; quantitative agreement with experiment requires careful calibration of **field strengths**, **densities**, and **boundary conditions**.

## Relevance to group

Demonstrates **multi-physics** reactive modeling (**ReaxFF + eFF**) for **field-assisted** oxidation—conceptually adjacent to **plasma–chemistry** and **combustion** themes.

## Citations and evidence anchors

- DOI: [10.1016/j.proci.2020.06.318](https://doi.org/10.1016/j.proci.2020.06.318)

## Related topics

- [[2020huang-combustion-a-enhancing-combustion]]
- [[reaxff-family]]
