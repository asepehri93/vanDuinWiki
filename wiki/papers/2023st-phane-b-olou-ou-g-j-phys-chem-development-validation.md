---
id: paper:2023st-phane-b-olou-ou-g-j-phys-chem-development-validation
type: paper
title: "Development and Validation of a ReaxFF Reactive Force Field for Modeling Silicon–Carbon Composite Anode Materials in Lithium-Ion Batteries"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - method:monte-carlo
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:batteries-interfaces
  - keyword:lammps
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.2c07773"
year: 2023
authors:
  - "Stéphane B. Olou'ou Guifo"
  - "Jonathan E. Mueller"
  - "Diana van Duin"
  - "Mahdi K. Talkhoncheh"
  - "Adri C. T. van Duin"
  - "David Henriques"
  - "Torsten Markus"
venue: "J. Phys. Chem. C"
pdf_sha256: "9b18195b307c67706003d1dde128a868b273232319f944cbe27af4825ac17943"
pdf_path: "papers/Guifo_LiSiC_JPCC_2023_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023st-phane-b-olou-ou-g-j-phys-chem-development-validation -->

## Summary

Silicon–carbon nanocomposites are widely discussed as next-generation **Li-ion anodes** because **sp\(^2\)** carbon can supply electronic percolation while **Si** phases contribute very high **gravimetric capacity**, and **covalent SiC**-related regions can add mechanical stiffness. The paper develops a **Li–Si–C** **ReaxFF** model intended to connect **atomistic** chemistry—within individual phases and especially at **interfaces**—to **macroscopic** responses such as **volume expansion**, **stress**, and **voltage** during **lithiation**. The parametrization is trained and tested against a **large, diverse** **density functional theory** reference set, then coupled to **molecular dynamics** and **Monte Carlo** sampling so that hybrid **Si–C** architectures can be explored beyond the size limits of routine **DFT** cells.

## Methods

### 1 — MD application (LAMMPS in MedeA, ReaxFF for Li–Si–C)

Simulations use **LAMMPS** as driven from the **MedeA** **environment** with the **new** **Li**–**Si**–**C** **ReaxFF** in the *J. Phys. Chem. C* **Methods**. **Velocity** **Verlet** integration: **0.5 fs** for general **MD** and **0.1 fs** when the authors need finer time resolution for **Li-ion** kinetics. **Nosé** **thermostat** and **Hoover** **barostat** (each **100 fs** damping) control **NPT** runs near **1 atm** and **298.15 K** (STP) in the stated workflows; small-strain **elastic** properties use a **NVT** **strain** scan around a relaxed state as described. **N/A** in this short summary for every **supercell** and **lithiation**-stage **duration**—see the paper and **SI** Section F.

A **hybrid** **GCMC** + **local** **geometry** **optimization** scheme (as in **Senftle** *et al.*) equilibrates interfacial **Si**–**C** structures against a **Li** **reservoir**; **Nernst**-style **corrections** to the reservoir chemical potential appear in the **SI** so model cells mimic **open-circuit**-like anode **patches** when **Li** **diffusion** is fast on the simulation **length** **scale**. **N/A** for **E-field** **MD**; **N/A** for umbrella/ metadynamics (sampling is **ReaxFF** **MD** + **GCMC**-style **Li** exchange). Bulk and interface **supercells** in the *JPCC* text use **3D** **periodic** **boundary** conditions (PBC) **unless** a free-surface model is **explicitly** **noted** in the **primary** **PDF**/**SI**.

### 2 — Force-field training (ReaxFF)

**Li**–**Si**–**C** **ReaxFF** is fit to a **large, diverse** **ab initio** database covering **lithiation**-relevant **Li–Si**, **Li–C**, **Si–C**, and related structures; coauthors with **BASF** affiliations help frame **industrial** validation. Full **objectives** and **error** **metrics** are in the *JPCC* **Methods**/**SI**.

### 3 — DFT (QM reference for training and spot checks)

**N/A** as a standalone DFT-**only** “results” thread—the paper documents **PBE-**class and **hybrid** **QM** used to assemble and test the **ReaxFF**; copy **k**-meshes, **cutoffs**, and any **NEB** **details** from the **VOR** **PDF**/**SI**, not from this wiki.


## Findings

For **SiC**-rich scenarios, the abstract reports a very high **theoretical capacity** (**5882 mA h g\(^{-1}\)**) associated with formation of **amorphous lithium carbide** species such as **a-Li\(_{4.4}\)C** within an **a-Li\(_{4.4}\)(SiC)\(_{0.5}\)**-like assembly; these **Li–C**-rich regions **soften** the composite mechanically while driving **volumetric swelling** up to about **668%** in the illustrated example. For **Si** bonded to **sp\(^2\) carbon**, simulations show **stepwise lithiation** and **distinct volume changes** in each subdomain across the lithiation window. The force field also resolves a **Li-rich interphase** at **grain boundaries** between **Si** and **sp\(^2\) C** that enhances **adhesion** between domains and raises the **local Li (de)insertion voltage** by up to about **1 V** relative to the bulk-like regions, which the authors frame as actionable for **atomistic design** of **Si–C** microstructures.

**Comparisons, sensitivity, and corpus note.** The *JPCC* work **compares** **lithiation**-driven **voltage** and **mechanical** response across **Si**-rich and **C**-rich **domains** **(versus** single-phase hosts) and links **interface** **adhesion** to **(de)lithiation** stages in the **MD**+**MC** **illustrations**; **sensitivity** to **temperature** (≈**298** **K**-class **NPT**/**NVT** in the **setup** they **report**) and to **Li** **chemical** **potential** in the **GCMC** **reservoir** **drives** local **structure**–**property** **trends** summarized in the **abstract**. **Limitations** **(authored)**: ReaxFF omits full **electronic** **polarization** and **electrolyte** decomposition (see the Limitations section). **Corpus** **honesty**: **reproduce** **voltage**/**capacity** **numbers** from the **VOR** **PDF**/**SI**—**not** from this **wiki** if **settings** differ between **sections** of the **JPCC** text.



## Limitations

ReaxFF cannot capture full **electronic** polarization or **electrolyte** decomposition chemistry without extensions; DFT training limits transferability outside covered chemistries.

## Relevance to group

Core **van Duin**-group **battery anode** ReaxFF with **BASF**-affiliated co-authors (industrial validation context in the article).

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.2c07773](https://doi.org/10.1021/acs.jpcc.2c07773)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
