---
id: paper:2020kirchhoff-small-2020-1-simulations-oxidation
type: paper
title: "Simulations of the oxidation and degradation of platinum electrocatalysts"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - method:monte-carlo
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:batteries-interfaces
  - keyword:monte-carlo-sampling
source_refs: []
doi: "10.1002/smll.201905159"
year: 2020
authors:
  - "Björn Kirchhoff"
  - "Laura Braunwarth"
  - "Christoph Jung"
  - "Hannes Jónsson"
  - "Donato Fantauzzi"
  - "Timo Jacob"
venue: "Small 16, 1905159 (2020)"
pdf_sha256: "39f3b7d62a620c0e499f1b8198eba6126dbe7b9c2ac3f08adfdef20ae5dfd614"
pdf_path: "papers/ReaxFF_others/Kirchhoff_Small_PtO_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020kirchhoff-small-2020-1-simulations-oxidation -->

## Summary

**Grand-canonical Monte Carlo (GCMC)** sampling with a **ReaxFF** description of **Pt–O–H** chemistry is used to explore **oxidation** and **degradation** pathways for **2–4 nm cuboctahedral Pt nanoparticles** as a function of **electrochemical potential**, including **solvation** and **thermochemical** corrections in the constructed **phase diagrams**. **DFT** checks support unusual **fragmentation products** found at highly oxidizing conditions. **PEMFC** **cathodes** operate **Pt** near **oxygen** **reduction** potentials where **surface** **oxide** **films** can be **thermodynamically** favored even if **kinetic** **hysteresis** keeps **metallic** **Pt(111)**-like **domains** visible in some **operando** probes.

## Methods

**Model (Pt nanoparticles in an electrochemical picture).** **Cuboctahedral Pt** **nanoparticles** of **~2–4 nm** **diameter** stand in for **PEMFC**-relevant **Pt** **catalyst** **particles** (as in the **Small** **article**).

**ReaxFF + grand-canonical Monte Carlo (thermodynamic sampling).** **O** and **H** are **exchanged** with **reservoirs** in a **GCMC** **framework** using **ReaxFF** **energies** for **Pt–O–H** **chemistry**, **plus** **solvation** and **thermochemical** **corrections** to build **phase**-**like** **diagrams** **vs** **electrochemical** **potential** (**V** **vs** **SHE** in the **manuscript**). This is **not** a long **NVE/NVT** **production** **MD** **trajectory** as the **main** **result**; it is **Monte** **Carlo** **sampling** of **oxidized** **configurations** on a **fixed** **nanoparticle** **graph** with **grand**-**canonical** **O/H** **insertion**/**removal** **moves**.

**1 — MD application (atomistic dynamics) vs this paper’s sampling.** The **headline** method is **ReaxFF**-based **grand-canonical Monte Carlo** on **cuboctahedral Pt** nanoparticles (~2–4 nm), not long NVE/NVT/NPT reactive molecular dynamics trajectories. For **AGENTS** slot mapping: **MD engine (LAMMPS-style):** **N/A —** **GCMC** is the main loop, not an MD time integrator (reactive molecular dynamics is not the headline production mode here). **System size & composition:** **nanoparticle** as above, with **O/H** **inserted/removed** by **GCMC** **moves**. **PBC / boundaries:** finite **nanoparticle** cluster; periodic boundary conditions for a bulk **MD** supercell are **N/A** for this headline **GCMC**-on-nanoparticle story (any auxiliary periodic cell must be read in the **PDF**). **Ensemble / timestep / barostat / pressure / E-field / enhanced MD:** **N/A** in the sense of conventional time-stepped **MD** (sampling is **MC** at fixed thermodynamic state per the paper’s construction). **Duration (trajectory):** **N/A** for **ps**/**ns**-long **reactive** **MD**; **MC** **passes** and **sampling** **lengths** are defined in the **article** (not a **production** **run** in the **MD** **sense**). **Thermostat / barostat in MD:** **N/A**—there is no **Berendsen**/**Nose–Hoover**-style **NVT** **reactive** **molecular** **dynamics** **to** **thermostat** here; **Grand**-**canonical** **statistics** are **at** the **state** **point** **used** in the **thermodynamic** **model**. **Target temperature:** the electrochemical/thermodynamic construction is carried out at the temperature used in the **Small** **article** (use the **version-of-record** for explicit **K**; not transcribed in this note). **Shear, shock, long-range / QEq notes:** **N/A** — not the focus here.

**3 — Static QM / DFT (validation).** **DFT** is used on **selected** **cluster** **products** (e.g. **[Pt₆O₈]⁴⁻**-**type** **fragments** at **strongly** **oxidizing** **conditions**) to **check** **stability** and **hydrophilicity** **claims** **against** **ReaxFF**-**found** **motifs** (**N/A** to **fully** **list** **functional**/**basis** here—**per** **SI**/**Methods** in **PDF**).

**2 — Force-field training.** **N/A —** the **article** **applies** an **existing** **ReaxFF** **Pt–O–H** **line** to **GCMC**; it is **not** a **new** **ReaxFF** **fit** **paper** (see **Small** for **which** **parameterization** **is** **used**).

## Findings

- **Surface oxide** motifs become **thermodynamically stable** around **0.80–0.85 V vs. SHE**, overlapping **typical fuel-cell cathode** operating windows—highlighting that **oxidized Pt surfaces** may matter even when often neglected in simplified catalyst models.
- Beyond **~1.1 V**, simulations show **particle fragmentation** into **[Pt₆O₈]⁴⁻**-like **clusters**, hypothesized to participate in **Pt dissolution/transport** pathways.
- **DFT** supports the **stability** of **[Pt₆O₈]⁴⁻** and its **hydrophilic** character, reinforcing a mechanistic link to **degradation** and **Pt ion** transport scenarios discussed in the paper.

The **Small** article situates **thermodynamic** **oxide** **stability** windows alongside **PEMFC** **relevant** **potentials**, motivating **multiscale** models that connect **atomistic** **oxide** **coverages** to **continuum** **dissolution** **fluxes**.

## Limitations

Nanoparticle models omit full **support interactions**, **electrolyte** dynamics, and **kinetic barriers** for dissolution; potentials are **thermodynamic** constructs subject to the ReaxFF fit.

**Retrieval** note: contrast this **Pt** **electrocatalyst** **oxidation** study with **Bi** **cathodic** **corrosion** in **[[2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion]]** when questions span **anodic** versus **cathodic** **metal** **stability** at **electrified** **interfaces**.

**Curation note:** **GCMC** + **ReaxFF** **phase** **diagrams** are **static**; pair with **kinetic** **experiments** cited in **Small** when translating **onset** potentials to **degradation** rates. **Particle** **size** effects enter through **surface** **oxide** **capacities** that scale differently than **bulk** **Pt** **thermodynamics**. **ORNL** coauthors anchor the work in **electron** **microscopy**-informed **catalyst** **degradation** debates.

## Relevance to group

Shows **ReaxFF + GCMC** applied to **electrochemical Pt oxidation**—a useful contrast to **oxide glass** and **battery electrolyte** ReaxFF studies elsewhere in the corpus.

## Citations and evidence anchors

- DOI: [10.1002/smll.201905159](https://doi.org/10.1002/smll.201905159)

## Related topics

- [[2020hossain-j-chem-phys-lithium-electrolyte-solvation]]
- [[reaxff-family]]
