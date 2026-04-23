---
id: paper:2022xu-x-manuscript
type: paper
title: "How Polytetrafluoroethylene Lubricates Iron: An Atomistic View by Reactive Molecular Dynamics"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:tribology
  - keyword:polymer
  - keyword:reactive-md
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.1c23950"
year: 2022
authors:
  - "Qiang Xu"
  - "Jie Zhang"
  - "Xin Li"
  - "Diana M. van Duin"
  - "Yuanzhong Hu"
  - "Adri C. T. van Duin"
  - "Tianbao Ma"
venue: "ACS Applied Materials & Interfaces"
pdf_sha256: "b600bd9f5f70ff9153e803b4e72f2cb4bf84e05c4c043a29472806ff8f46188b"
pdf_path: "papers/Xu_PTFE_Iron_lubrication_RxFF_Tianbao_ACS_AMI_2022_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022xu-x-manuscript -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **ACS Appl. Mater. Interfaces** DOI `10.1021/acsami.1c23950` and `normalized/extracts/2022xu-x-manuscript_p1-2.txt`. This slug uses a **galley** PDF path.

## Summary

**PTFE** lubricates **steel** in many systems, yet **atomistic** mechanisms coupling **shear**, **oxidation**, and **polymer scission** remain debated. The authors **extend ReaxFF** to **Fe–O–C–H–F** chemistry covering **iron oxides**, **water**, and **fluoropolymer** fragments trained against **QM** data, then simulate **single-asperity** **shear** of **PTFE** on **iron/oxide** countersurfaces from **10–300 K**. The work emphasizes **radicals** from **C–C scission**, **oxidation/hydroxylation**, **Fe–C** and **Fe–F** **bonding** that **anchor** **transfer films**, and **chain orientation** effects on **friction**. **Friction** is reported **nonmonotonic** in **T** with a **peak near 100 K**, interpreted via **reduced mobility** and **stiffer**, **less oriented** chains at **cryogenic** conditions. The framing aligns with **experimental** evidence that **tribofilms** can involve **strong** **chemical** attachment of **fluorinated** fragments to **iron oxides**, motivating an **explicitly reactive** treatment rather than **purely nonreactive** **contact** models. **For operators**, the **galley** path recorded here is primarily a **manifest** convenience; **all** **quantitative** **tables** should be **reconciled** against the **ACS** **version of record** during **bibliography** **hygiene** passes.

## Methods

### Reactive force-field development (A)

- **Elements / chemistry:** Extended **ReaxFF** for **Fe–O–C–H–F** covering **iron oxides**, **water**, and **fluoropolymer** fragments; merges prior **Fe/O/H** and **fluorocarbon** databases with **new QM training data** (structures, reactions, and energetics enumerated in the article/SI).
- **Optimization:** Parameters adjusted to reproduce selected **QM** benchmarks relevant to **tribochemical** bond formation/cleavage (see paper for functional/basis details of the **DFT** reference data).

### Reactive MD tribology protocol (B)

- **Geometry:** **Single-asperity**-style **shear** of **PTFE** against **iron/oxide** counter-surfaces (exact surface models in the publication).
- **Conditions:** **Temperature** range **10–300 K**; **normal load**, **sliding velocity**, **ensemble**, and **thermostat** settings are listed in the **article/SI**—**not duplicated** on this wiki.
- **Observables:** **Friction** / **shear stress** traces, **radical** formation, **oxidation/hydroxylation**, and **transfer-film** chemistry.
- **Electrostatics:** Standard **ReaxFF** **QEq** treatment as implemented in the authors’ **LAMMPS** workflow (see primary text for **cutoffs** and **output interval**).

### Corpus / versioning note

This slug’s **`pdf_path`** is a **galley**; reconcile **figures, pagination, and SI tables** with the **ACS** **version of record** when available.

### MD application (tribology) and ReaxFF training (pointer)

**FF training (A):** **DFT** **reference** **energies** and **reaction** **sets** for **Fe–O–C–H–F** are in the *ACS Appl. Mater. Interfaces* **Methods**/**SI**; see subsections above. **RMD (B):** **LAMMPS** with the fitted **ReaxFF**; **PTFE**/**iron**/**oxide** **slab** models under **10–300 K** **single-asperity** **shear** with **normal** **load** and **sliding** **rate** in the **article** (not re-tabulated here). **3D** **PBC** where used; **ensemble**, **timestep**, **ps**/**ns** segments, and **thermostat** for **deformation**/**shear**; **Coulomb** and **QEq** **per** primary text. **N/A** — no static **interfacial electric field**; **N/A** — no **metadynamics**/**replica** **sampling** beyond the reported **shear** **MD**; **N/A** for **NVT**-style **constant** **volume**, no **NPT** **barostat** unless the **VOR** states it.

## Findings

### Tribochemical mechanism

**Shear** generates **radicals** and promotes **oxidation/hydroxylation**, consistent with **experimental** **tribochemistry** references cited in the paper.

### Transfer film and interfacial bonding

**Transfer films** include **Fe–C** and **Fe–F** connectivity and **strong** **Fe\(_2\)O\(_3\)–hydroxyl** interactions described in the article as **chelation-like** in character.

### Temperature-dependent friction

**Friction** is **nonmonotonic** in **T**, with a **peak** near **100 K** in the authors’ analysis—linked to **reduced chain mobility** and **interfacial orientation** effects at **cryogenic** conditions versus **room temperature**.

## Limitations

**Galley** bytes may differ slightly from **VOR**; **asperity** models omit **multi-contact** statistics at **engineering** scales. **Friction** **extracts** from **MD** require consistent **normal load** and **shear velocity** reporting—confirm **SI** tables for **exact** **protocol** values before **benchmarking** against **macroscopic** **tribometer** data. **Galley** **pagination** can differ from **VOR**, so **figure** **labels** used in **downstream** **notes** should be **checked** against the **final** **ACS** **PDF** when available locally.

## Relevance to group

Direct **van Duin-group** **ReaxFF tribochemistry** on **metal–polymer** contacts, co-authored with **Tianbao Ma**’s laboratory collaborators. The work is a **paired** entry with **`[[2022qiang-xu-acs-how-polytetrafluoroethylene]]`** documenting an alternate **PDF** variant in **`papers/`** for **manifest** completeness.

## Citations and evidence anchors

- DOI: [10.1021/acsami.1c23950](https://doi.org/10.1021/acsami.1c23950) — galley `papers/Xu_PTFE_Iron_lubrication_RxFF_Tianbao_ACS_AMI_2022_galley.pdf`; extract `normalized/extracts/2022xu-x-manuscript_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[2022qiang-xu-acs-how-polytetrafluoroethylene]]
