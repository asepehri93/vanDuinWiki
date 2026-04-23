---
id: paper:2023meng-journal-of-t-exploring-depolymerization
type: paper
title: "Exploring depolymerization mechanism and complex reaction networks of aromatic structures in chemical looping combustion via ReaxFF MD simulations"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:fuel-combustion
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:thermal-decomposition
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: "10.1016/j.joei.2023.101180"
year: 2023
authors:
  - "Liangliang Meng"
  - "Ying Zhu"
  - "Meilin Zhu"
  - "Ge Wu"
  - "Wenqian Guo"
  - "Chang Geng"
  - "Na Li"
  - "Rou Feng"
  - "Hui Zhang"
  - "Qingjie Guo"
  - "Hongcun Bai"
venue: "J. Energy Inst."
pdf_sha256: "94ee974ca9345435e66bc87be2997be9e00bb810068ff88533f1d51ce2cefb50"
pdf_path: "papers/ReaxFF_others/Meng_depolymerizationJEnInst_2023.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023meng-journal-of-t-exploring-depolymerization -->

## Summary

**Chemical looping combustion (CLC)** oxidizes fuels using a solid **oxygen carrier** (here **Fe\(_2\)O\(_3\)**) to yield **CO\(_2\)**-ready flue streams while avoiding direct air–fuel mixing. Solid fuels such as coal and biomass contain **aromatic moieties** whose **depolymerization** governs early **volatiles** release and subsequent **gas-phase** chemistry; understanding those steps at **atomistic** resolution can clarify **temperature** and **carrier** effects that bulk reactor models parameterize only indirectly. This **Journal of the Energy Institute** article applies **ReaxFF molecular dynamics** to **aromatic model compounds** reacting with **Fe\(_2\)O\(_3\)** in a CLC fuel-reactor setting, emphasizing **staged conversion**, **intermediate** populations, and **reaction-network** structure extracted from trajectories. The scientific goal is not a full reactor simulation, but a chemically explicit map of how **lattice oxygen** participates in **fragmentation** and **oxidation** for representative aromatic scaffolds. Within **CLC** framing, the paper is best read as a **mechanism library** for **solid-fuel** aromatics: it classifies **staged** chemistry and highlights when **pyrolysis** dominates early events versus when **oxide**-mediated **oxidation** accelerates **CO\(_2\)** formation later. That distinction is what later **continuum** models would need to preserve if they coarse-grain these atomistic pathways.

## Methods

### Systems and protocol (B)

**ReaxFF MD** of **aromatic** models + **Fe\(_2\)O\(_3\)** (**oxygen carrier**) under **CLC**-relevant **temperature** sweeps; compare **multiple** aromatic sizes.

The **Computational details** section of the PDF describes how **aromatic** **models** are interfaced with **Fe\(_2\)O\(_3\)** as a solid **oxygen carrier** so **lattice oxygen** can participate in **fragmentation**/**oxidation** across **staged** **temperature** protocols; that **oxide-contact** setup is what lets the authors separate **oxide-mediated** pathways from **pure** **pyrolysis** in the **network** analysis.

### Analysis

Time traces of **CO**, **H\(_2\)O**, **CO\(_2\)**, and fragments; separate **pyrolytic cracking** vs **oxide-mediated oxidation**; build **reaction-network graphs** from trajectories.

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** with **ReaxFF** for **aromatic** models in contact with **Fe\(_2\)O\(_3\)** **oxygen-carrier** regions under **CLC**-motivated **temperature** protocols. **System & composition:** **multiple** **aromatic** **sizes** plus **oxide** **surface**/bulk **motifs** as in **Computational details**. **Boundaries / periodicity:** **3D PBC** supercells for **solid**/**interface** models. **Ensemble, timestep, thermostat, barostat, run length:** the **aromatic**+**Fe\(_2\)O\(_3\)** **NVT** **MD** in the **paper** uses **fs** **timesteps** and **ns**-class **sampling** to extract **reaction** **events**; **N/A** here to tabulate every **NVT** **damping** and **production** **ns** **window** (see *J. Energy Inst.* `pdf_path`). **Pressure, electric field, shear, shock, enhanced-sampling MD:** **N/A** in this CLC **ReaxFF** **mechanism** summary.

### 2 — Force-field training

**N/A** — the paper **uses** a **ReaxFF** description for **hydrocarbon**/**oxide** **chemistry** as documented in the article; **reparameterization** is not the focus of the abstracted **Methods** here.

### 3 — Static QM

**N/A** — **reactive** **MD**-forward **network** analysis.

## Findings

### Four-stage qualitative picture

Staged **conversion** of aromatics over **Fe\(_2\)O\(_3\)**: **higher T** and **smaller** aromatics **accelerate** conversion in summarized trends.

### Species trends

**CO** and **H\(_2\)O** rise then fall in later stages as oxidation advances; **higher T** favors **lattice oxygen** release and **CO\(_2\)**-leaning completion.

### Mechanistic competition

Early **pyrolytic ring opening** competes with **oxidation**; larger **PAHs** yield **richer intermediate** manifolds and **denser** reaction graphs.

### Modeling export

Provides a **mechanistic graph** for **coarse-graining**, not a single **Arrhenius** rate—**lattice O** coupling distinguishes **CLC** from **inert pyrolysis**.

**Compared** to a **laboratory** **CLC** **reactor**, the **trends** in **intermediate** **concentration** and **lattice-oxygen** **reaction** **kinetics** are only **as good** as the **ReaxFF** **database**; **higher** **temperature** in the **NVT** **sweeps** accelerates **oxidation**-leaning **channels**, which is a key **sensitivity** **lever** in the **plots**—read the **J. Energy Inst.** **figure** **captions** in `pdf_path` and note **kinetic** **uncertainty** as a **limitation** when **coarse**-graining. **Open** **future** work would couple these **networks** to **continuum** **mass** **transfer** (not in this **atomistic** **study**).

## Limitations

ReaxFF kinetics are empirical; CLC **reactor** realism (flow, mass transfer, ash, full coal macromolecular structure) is not atomistically resolved.

## Relevance to group

Demonstrates **ReaxFF** for **CLC** and **solid-fuel** depolymerization networks adjacent to group **combustion** interests.

## Citations and evidence anchors

- DOI: [10.1016/j.joei.2023.101180](https://doi.org/10.1016/j.joei.2023.101180)

## Related topics

- [[reaxff-family]]
