---
id: paper:2020wenbo-zhu-j-phys-chem-jp0c02573-2
type: paper
title: "Development of a Reactive Force Field for Simulations on the Catalytic Conversion of C/H/O Molecules on Cu-Metal and Cu-Oxide Surfaces and Application to Cu/CuO-Based Chemical Looping"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:berendsen-thermostat
  - keyword:catalysis-surface
  - keyword:combustion
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:qm-training-data
  - keyword:reaxff-parameterization
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.0c02573"
year: 2020
authors:
  - "Wenbo Zhu"
  - "Hao Gong"
  - "You Han"
  - "Minhua Zhang"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C (2020)"
pdf_sha256: "a6f3d932833266ad604392f2bd16edf4bcf4ff53c37ea22ce134452db56fb9c0"
pdf_path: "papers/Zhu_JPCC_CuCHO_2020_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020wenbo-zhu-j-phys-chem-jp0c02573-2 -->

## Summary

A **Cu/C/H/O Reaxff** is built by **re-optimizing** **Cu** on **cluster** data, **merging** with a **C/H/O** field, and **fitting** **Cu–(C/H/O)** **cross-terms** to **DFT** **binding** and **barriers** on **Cu(100)**, **(111)**, **(211)**. Custom **Reaxff**-based **transition-state** and **reaction-path** **utilities** are presented. **LAMMPS** **NVT** **reactive** **MD** ( **Berendsen** **thermostat**, **0.1** **ps** **damping**) at **600–1600** **K** and **0.25** **fs** covers **H** **dissociation**, **methoxy** **chemistry**, **glucose** **+** **Cu** at **1600** **K** ( **400** **ps** **gas** **leg**), and **CLC**-style **redox** **tours** (**Section 3**; **SI** for **cell** **sizes**).

This **slug** is an **alternate** **PDF** path (**online** file name) for the same **DOI** as **`[[2020wenbo-zhu-j-phys-chem-jp0c02573]]`**.

## Methods

**1 — MD application.** **LAMMPS**; **NVT**; **Berendsen** **thermostat**; **0.25** **fs** time step; **temperature** **setpoints** in **600–1600 K** (e.g. **600 K**, **1000 K**, **1400 K**, **1600 K** for the **illustrative** **cases** in **Section 3**); **trajectory** **durations** include **400** **ps** for the **glucose** **gas**-phase **leg** and other **ps**-scale **production** **segments** in **Section 3**; **PBC** **slabs** with **~10–20** **Å** **vacuum** **as** in **SI**. **N/A** — **NPT**; **N/A** — **umbrella**; **N/A** — **E-field**. **Hydrostatic** **pressure** **N/A** under **NVT** **sampling** in the **examples** **quoted** here.

**2 — Force-field training.** **Reoptimize** **Cu**; **merge** **C/H/O**; **fit** **cross-terms** to **DMol3** **rPBE** **data** (**energies**, **barriers**); see **`[[2020wenbo-zhu-j-phys-chem-jp0c02573]]`** for **full** **DFT** **convergence** **ladder**.

**3 — Static QM.** **DMol3** **rPBE**; **LST/QST/CG** for **TS**; **identical** **to** the **VOR** **curation** on the **primary** **wiki** **page**.

**4 — Review or non-simulation.** **N/A**

## Findings

**Outcomes and mechanisms.** **DFT**-consistent **surface** **chemistry** and **rich** **C/H/O** **MD** on **Cu**; **fuel-dependent** **CLC** **outcomes** when **O** **storage** **on** **CuO** **couples** to **fragmentation** on **Cu** **(facets)**, as **framed** in the **full** **text**.

**Comparisons and sensitivity.** **Reaxff** **vs** **DFT** on **adsorption**/**barriers**; **T** **sweeps**; **case**-by-**case** **chemistry** **(methoxy, glucose, hydrocarbons**).

**Authored limitations and outlook.** **Transferability** to **electrochemical** **interfaces** **with** **explicit** **electrolyte** **may** need **more** **training**—see **## Limitations** below.

**Corpus honesty.** **Provenance** **of** this **file** = **second** **PDF** **name**; **use** the **VOR** **file** for **page**-stable **citations** if **pagination** **drifts** **between** **preprint**/ **Just**-**Accepted**/ **VOR** **builds** **(confirm** in **PDF**).

## Limitations

**Transferability** to **electrolyte-covered** **Cu** under **electrochemical** control is not automatic; **explicit** **solvation** and **charged** interfaces may need **additional** training. **Corpus** operators should treat **combustion** and **CLC** **case** **studies** as **illustrative** **trajectories** whose **statistics** **(barrier** **sampling,** **long** **runtime** **needs**)** must be **read** from the **VOR** **PDF** and **SI** **tables**, not inferred from this **navigation** **slug** alone.

## Relevance to group

**van Duin** co-authorship; **parameterization** + **method** tooling (**TS** search) for **metal** **oxidation**/**catalysis**.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.0c02573`

## Reader notes (navigation)

- Primary curated PDF and full DFT/MD table alignment: [[2020wenbo-zhu-j-phys-chem-jp0c02573]]

## Related topics

- [[reaxff-family]]
