---
id: paper:2020yuan-nat-effects-pressure
type: paper
title: "Effects of pressure and velocity on the interface friction behavior of diamond utilizing ReaxFF simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:berendsen-thermostat
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.ijmecsci.2020.106096"
year: 2020
authors:
  - "Song Yuan"
  - "Xiaoguang Guo"
  - "Qian Mao"
  - "Jiang Guo"
  - "Adri C. T. van Duin"
  - "Zhuji Jin"
  - "Renke Kang"
  - "Dongming Guo"
venue: "International Journal of Mechanical Sciences 191 (2021) 106096"
pdf_sha256: "2f8f0b3ebffe114dec089c7bb2e871498ad7878fd034479398be555e733d0df1"
pdf_path: "papers/Yuan_Mao_etal_InJMechSci2020_diamond_friction.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020yuan-nat-effects-pressure -->

**Reaxff** **MD** models **chemical** **mechanical** **polishing**-style **diamond** **friction** with varying **normal** **load** (pressures in the **~10** **GPa** **class** in the **figures**) and **sliding** **velocity** (**20, 50, 100** **m** **s⁻¹** **along** **x** for **~500** **ps** in the **stated** **setup**), monitoring **friction** **force**, **C–C** / **C–O–C** **bond** **populations**, and **amorphous** **carbon** **formation**.

## Summary

The study couples **rigid** **top** **diamond** on **hydroxylated** **diamond** **+** **H₂O₂** **slurry** in **LAMMPS** **NVT** at 300 K with **Berendsen** **thermostat** (**25** **fs** **damping**), **0.25** **fs** time step, and **~12–14** **GPa**-class **normal** **pressures** in the **cited** **figures**; **friction** **trends** **vs** **C–C**/**C–O–C** **bonds** and **amorphous** **C** **fraction** **evolve** in **two** **regimes** with **pressure** and **sliding** **velocity**.

## Methods

**1 — MD application.** **LAMMPS**; **combustion**-class **C/H/O** **Reaxff** for **diamond** **+** **aqueous** **CMP**-like **chemistry** (**Section** **2**). **NVT** at 300 K; **Berendsen** **thermostat**; **25** **fs** **damping**; **velocity** **Verlet**; **0.25** **fs** **time** **step**; **rigid** **top** **layer** **+** **shear** over **hydroxylated** **diamond** **+** **H₂O₂** **slurry** **(Section** **2**). **Normal** **pressures** **~12–14** **GPa** **(figures)**; **sliding** **20, 50, 100** **m** **s⁻¹** **+x**; **~500** **ps** after **load** **ramp** (**Section** **2–3**). **PBC** in **x,y** in the **in-plane** **slab** **geometry**; **N/A** — **NPT** **(constant**-**T** **NVT** **with** **mechanical** **load** **control** **instead** **of** **barostat** **in** **excerpt**). **N/A** — **metadynamics**; **N/A** — **E-field** **(no** **external** **field** **in** **excerpt**). **N/A** — **replica** **exchange** **(not** **used**).

**2 — Force-field training.** **N/A** — **Reaxff** **from** **cited** **combustion** **CH/O** **line**; **not** **refit** **in**-**manuscript**.

**3 — Static QM.** **N/A**

**4 — Review or non-simulation.** **N/A**

## Findings

**Outcomes and mechanisms.** **Early** **friction** **rises** with **C–C** and **C–O–C** **interfacial** **bonds** and with **higher** **normal** **pressure** and **sliding** **velocity** in the **first** **regime** **described**. **Later** **friction** **correlates** with **amorphous** **carbon** and can **drop** with **increasing** **pressure**/**velocity** in the **second** **regime** **(interpretation** **in** **article**). **Removal** **mechanisms** **shift** from **dominant** **C–C** **single**-**bond** **formation** at **low** **pressure** to **more** **single** and **multi**-**C–C** **bonds** at **higher** **pressure** **(wear** **+** **subsurface** **damage** **narrative** **in** **text**).

**Comparisons and sensitivity.** **Pressure** and **sliding** **velocity** **sweeps**; **friction** **vs** **bond** **counts** **vs** **a**-**C** **fraction** **(figure**-**based** **parameter** **study**).

**Authored limitations and outlook.** **Reaxff** **slurry** **chemistry** is **simplified** **vs** full **electrochemistry**; **see** **## Limitations** **on** this **page**.

**Corpus honesty.** **Manuscript** **2020** **vs** **IJMS** **2021** **issue**—**DOI** is **authoritative**; **slugs** may **retain** **“2020”** **naming** **(see** **## Citations** **below**).

## Limitations

**Reaxff** **C/O/H** chemistry for **CMP slurry** may omit **full** **electrochemical** detail; **simulation** **speeds**/**pressures** map to **idealized** **interface** models.

## Relevance to group

**van Duin** co-authorship; **Reaxff** **tribology** on **diamond** **manufacturing** interfaces.

## Citations and evidence anchors

- DOI: `10.1016/j.ijmecsci.2020.106096` (published **IJMS** **191**, **2021**; manuscript numbering may differ from **2020** slug)

## Related topics

- [[reaxff-family]]
