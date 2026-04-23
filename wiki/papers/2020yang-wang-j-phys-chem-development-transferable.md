---
id: paper:2020yang-wang-j-phys-chem-development-transferable
type: paper
title: "Development of a Transferable ReaxFF Parameter Set for Carbon- and Silicon-Based Solid Systems"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - material:widegap-semiconductor
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:nvt-simulation
  - keyword:oxide-surface
  - keyword:qm-training-data
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:tribology
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.0c01645"
year: 2020
authors:
  - "Yang Wang"
  - "Yuqing Shi"
  - "Qiang Sun"
  - "Kang Lu"
  - "Momoji Kubo"
  - "Jingxiang Xu"
venue: "J. Phys. Chem. C 2020, 124, 10007–10015"
pdf_sha256: "738807b94e515f0d8c446e9585fddff24d3cf236369c6b35844286a2cbbb3c62"
pdf_path: "papers/ReaxFF_others/Wang_SiCNO_JPCC_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020yang-wang-j-phys-chem-development-transferable -->

A **H/C/N/O/Si Reaxff** parameter set is **fitted** to **first-principles** data using **simulated annealing** to support **tribochemistry** of **carbon-** and **silicon-based** solid lubricants with **H₂O**, **H₂**, and **O₂**. **Oxidation** **MD** of **SiC** and **Si₃N₄** in **O₂** is **compared** to **experiments** on **high-temperature** **oxidation**.

## Summary

The authors **unify** **H/C/N/O/Si** **chemistry** for **graphite**/**DLC**/**SiC**/**Si₃N₄**/**SiO₂**-**class** **environments** under **tribo**-relevant **molecules**. **Simulated** **annealing** **Reaxff** **optimization** on **DFT** **training** data is **followed** by **static** **reaction** **energy** **tests** and **~100** **ps** **NVT** **oxidation** **MD** at **1200** **K** with **0.25** **fs** in **LASKYO** (in-house) **on** **SiC** and **Si₃N₄** with **O₂** **(Section** **3.2**). The **DFT** **database** **(Section** **2**)** covers **molecules**, **clusters**, and **condensed** **phases** so the **parameter** **set** can **bridge** **gas**-**phase** **oxidants** and **covalent** **ceramics** in one **framework**.

## Methods

**1 — MD application.** The authors run reactive molecular dynamics in **LASKYO** (in-house integrator); **0.25** **fs** **time** **step**; **NVT**; **~100** **ps** **O₂** **atmosphere** **SiC** and **Si₃N₄** **cells** at **1200** **K**; **O–Si**/**O–N** **bond** **counts** **vs** **time**; **N/A** — full **thermostat** **label** if the **wiki** **omits** it—**confirm** **PDF**; **N/A** — **NPT**; **N/A** — **E-field**; **N/A** — **metadynamics**. **PBC** **supercells** for **gas**+**solid** as in **Section** **3.2**. **Normal** **hydrostatic** **pressure** **N/A**—**NVT** **constant**-**volume** **oxidation** **cells** **(not** **NPT** **pressurization** **in** **excerpt**).

**2 — Force-field training.** **H/C/N/O/Si** **Reaxff**; **DFT** **reference** on **clusters**, **molecules**, and **condensed** **phases** (**SiO₂**, **Si₃N₄**, **Si**, **diamond**); **simulated** **annealing** **global** **search** of **parameters** (**Section** **2**). **Validation** on **H₂**, **H₂O**, **H₂O₂**, **O₂** **reaction** **energies** on **diamond(111)**, **Si(111)**, **SiC(111)**, **Si₃N₄(100)**, **SiO₂(001)** (**Figures** **5–9**). **Reference** data: **DFT**; **MD** **oxidation** **vs** **experiments** (**500–1800** **K** **trends**).

**3 — Static QM.** The **DFT** **level** and **k**-**sampling** are **in** **Section** **2**; **N/A** for a **separate** **k**-**point** **paragraph** in this **short** **wiki** **note**—**see** `pdf_path`.

**4 — Review or non-simulation.** **N/A**

## Findings

**Outcomes and mechanisms.** The **H/C/N/O/Si** set **reproduces** **qualitatively** **correct** **environmental** **molecule** **+** **surface** **chemistry** in the **static** and **MD** **tests** **selected**. **SiC** and **Si₃N₄** **O₂** **MD** **tracks** **experimental** **high-T** **oxidation** **behavior** **(thicknesses**/ **rates** as **cited**).

**Comparisons and sensitivity.** **MD**+**kinetics** **vs** **experiments**; **T** **(1200** **K** **MD** **window** **vs** **wider** **expt** **range**).

**Authored limitations and outlook.** **Gas** **oxidation** **is** an **intermediate** **test**; **tribo** with **shear**/**third-body** is **harder**—**see** **## Limitations**.

**Corpus honesty.** **JPCC** **VOR** **tables** **favor** `pdf_path`.

## Limitations

**Simulated annealing** fits can **underperform** on **states** outside the **training** **manifold**; **tribointerfaces** with **shear** and **third-body** **particles** add complexity beyond **gas** **oxidation** **tests**.

## Relevance to group

Independent **Reaxff** **parameterization** line for **SiC/Si₃N₄**/**carbon** **tribology**—useful cross-reference for **group** **Si/O/C** **models**.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcc.0c01645`

## Related topics

- [[reaxff-family]]
- [[2020yang-wang-j-phys-chem-development-transferable-2]]
