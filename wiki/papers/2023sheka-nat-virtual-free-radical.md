---
id: paper:2023sheka-nat-virtual-free-radical
type: paper
title: "Virtual Free-Radical Polymerization of Vinyl Monomers in View of Digital Twins"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:semiempirical-tightbinding
  - task:application
paper_keywords:
  - keyword:polymer
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.3390/polym15142999"
year: 2023
authors:
  - "Elena F. Sheka"
venue: "Polymers"
pdf_sha256: "30bfdd37a1c60c8a015e98861fd0e444eafbb0cda718302a939b60053e32ddc9"
pdf_path: "papers/Others/Sheka_MDPI Polymers 2023.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2023sheka-nat-virtual-free-radical -->

## Summary

This open-access *Polymers* article presents what the author describes as a first “virtual polymerization” framework organized around **digital twins (DTs)** for elementary steps in **vinyl free-radical polymerization**. The scientific goal is to move beyond picturing polymers only as sequences of points in three-dimensional space and instead treat each elementary reaction class—**initiation**, **propagation**, and **termination** of chain growth—as a structured family of DT structures whose electronic properties can be computed and compared systematically. The paper is explicitly **not** a reactive force field or classical MD study; it is a quantum-chemistry-style workflow based on a semi-empirical unrestricted Hartree–Fock model used to obtain ground-state energies and spin-density characteristics for roughly **sixty** DTs spanning the three reaction types. From barrier profiles computed for selected DT pairs, the author constructs **Evans–Polanyi–Semenov (EPS)**-type linear relations intended to estimate activation energies for initiation- and propagation-class reactions across vinyl monomers without running a separate high-level barrier calculation for every monomer-specific case.

## Methods

### Electronic structure model (C)

**Semi-empirical unrestricted Hartree–Fock** on **digital-twin (DT)** geometries for **vinyl** **free-radical** steps (**initiation**, **propagation**, **termination** classes; ~**60** DTs in the paper’s scope statement).

### Barriers and EPS construction

**Barrier profiles** for representative DT pairs feed **Evans–Polanyi–Semenov**-type linear relations for categories **(1)/(2)** (**initiation/propagation**).

### Interpretive focus

**Spin-density** features used to rationalize **TS** structure in **radical** elementary reactions.

**Workflow shape (as described).** The paper organizes **digital twins** into **initiation**, **propagation**, and **termination** classes, then compares **electronic** properties across families to justify **EPS** linear relations. This structure is **not** a **ReaxFF** or **classical MD** pipeline; it is a **semi-empirical QC** survey intended to compress barrier estimation effort for **vinyl** monomer libraries.

**N/A (atomistic RMD, ReaxFF, NPT, E-field).** The study does not report **LAMMPS**/**ReaxFF** **trajectories** or **periodic** **cells**; **N/A** for **NPT** **barostats**, **timestep** **fs** **values**, or **E-field** **workflows**—all **N/A** by design for this **semi-empirical** **UHF** **barrier**+**EPS** **paper**.

## Findings

### EPS utility claim

**EPS** fits from barrier scans are presented as **practical** **E\(_a\)** estimates for **initiation/proagation** across **vinyl monomers** in the semi-empirical framework.

### Conceptual point

**Spin** structure of **TS**s is argued to be as important as **ground-state** energetics for **barrier** rationalization.

### Scope caveat

**Gas-phase**/**semiempirical** barriers are **internally consistent** within the model—not drop-in replacements for **condensed-phase** **ReaxFF**/**DFT** without calibration.

### Evidence routing (comparisons, parameters, future work)

The **EPS** **lines** are **compared** to **per-monomer** **barrier** **scans** **(versus** running an **NEB**-style point every time) so library chemistry can be **explored** at **low** **cost**—**sensitivity** of the **E\(_a\)** **estimates** to monomer **coverage** of the **scanned** **twin** **set** and to **field**-free, **0 K**-leaning **electronic** **structure** is **inherent** to the model. **Limitation** (authored in spirit): the **twin** set does **not** **yet** **mesh** a **laboratory** **polymerization** **bench**; **open** **questions** include how **temperature**-**broadening** and **solvent** should enter **if** a **ReaxFF**-class **kinetic** **map** is **sought** later. **Corpus** **honesty**: the **citable** **numerical** **barriers** live in the *Polymers* **PDF**; this **page** is a **navigation** **summary** of the **workflow** only.

## Limitations

The model omits explicit **solvent**, **temperature** distributions beyond static electronic structure, and **molecular dynamics** sampling of chain growth; comparisons to **ReaxFF** or high-level **DFT** require separate calibration. The corpus PDF is filed under **`papers/Others/`** as a contrast case to the group’s primary **ReaxFF** reactive workflows.

## Relevance to group

Included in **`papers/Others/`**; useful contrast case for **polymer radical chemistry** workflows outside the group’s primary **ReaxFF** line.

## Citations and evidence anchors

- DOI: [10.3390/polym15142999](https://doi.org/10.3390/polym15142999)

## Related topics

- [[reaxff-family]]
