---
id: paper:2017motevalian-venue-research
type: paper
title: "Kinetics of Silane Decomposition in High-Pressure Confined Chemical Vapor Deposition of Hydrogenated Amorphous Silicon"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:thermal-decomposition
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:lammps
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.iecr.7b03515"
year: 2017
authors:
  - "Seyed Pouria Motevalian"
  - "Stephen C. Aro"
  - "Hiu Y. Cheng"
  - "Todd D. Day"
  - "Adri C. T. van Duin"
  - "John V. Badding"
  - "Ali Borhan"
venue: "Ind. Eng. Chem. Res."
pdf_sha256: "dc3c0d636716df99a877e9e96de1af7b43b6e12577d79fe5b7faeecc17b844c0"
pdf_path: "papers/Motevalian_Si_H_I&EC_2017_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017motevalian-venue-research -->

!!! abstract
Confined HPCVD measures silane pyrolysis kinetics (20–33 MPa, 5.9 µm capillary); ReaxFF NVT MD on clean vs H-terminated c-Si shows heterogeneous decomposition and supports H-desorption-limited growth.

## Summary

**Experiments:** **Silane** pyrolysis in **confined high-pressure CVD** at **20–33 MPa** in a **5.9 µm** inner-diameter microcapillary yields **first-order** kinetics in silane with **Ea = 53.7 ± 2.9 kcal/mol** and **A = 1.5×10¹⁰ m/s**, aligning activation energies with **H desorption** from crystalline silicon surfaces—suggesting **H desorption** limits film growth. **Simulations:** **ReaxFF** MD of **silane** interacting with **clean vs H-passivated c-Si** slabs (**15 SiH₄** molecules, **7 MPa**, **400 °C** equivalent conditions in a **22×22×50 Å** cell with a **256-atom Si slab**; minimization and slab prep per SI). **NVT** production runs monitor unreacted silane. **No homogeneous gas-phase reactions** appear in the ReaxFF trajectories; **clean surfaces** consume silane into **silicon hydrides** within ~**10 ps**, while **H-terminated** surfaces show **no reaction** in the same protocol—supporting **heterogeneous** control and **dangling-bond availability** as rate-limiting in confined HPCVD.

Microcapillary confinement raises pressure without large reactor volume, letting kinetics be measured where gas-phase chain growth is suppressed—matching the simulation emphasis on surface-limited chemistry.

## Methods

**Force-field training / fitting.** **ReaxFF** parametrizations for **Si/H** chemistry (including **silane** and **silicon hydrides**) are used as published; additional **force-field testing** notes appear in the **Supporting Information**. **No** new QM refit is reported in the main article text summarized here.

**MD application (atomistic dynamics).** **Engine / code:** **ReaxFF** **molecular dynamics** as implemented in the authors’ workflow; **specific MD package** **N/A —** not named in the **main-text proof PDF** excerpt used here (confirm software/version in **Supporting Information** if required for reproduction). **System size & composition:** **15 silane** molecules with a **256-atom** **c-Si** slab in a **22 × 22 × 50 Å** periodic cell, comparing **clean** vs **hydrogen-passivated** surfaces (**Figure 4**). **Boundaries / periodicity:** **Three-dimensional periodic** supercell (standard for this slab–gas setup). **Target conditions:** **~400 °C** (**~673 K**) and **~7 MPa** silane pressure as stated for the reactive cell. **Ensemble:** **canonical ensemble** (**NVT-class**) production trajectories after separate **NVT** minimization/pretreatment of the slab and gas regions described in the **SI**. **Timestep / femtosecond integration:** explicit **Δt** **N/A —** not printed in the main proof excerpt; **SI** lists minimization and slab-preparation settings. **Duration / stages:** separate **NVT** pretreatments of **surface** and **gas** regions (**SI**), then combined runs long enough to resolve **~10 ps** **clean-surface** consumption kinetics reported in **Figure 4**; total production **nanoseconds** **N/A —** confirm in **SI** tables. **Thermostat:** coupling details for the **canonical ensemble** runs are **N/A —** beyond the ensemble label in the main proof excerpt—see **SI**. **Barostat:** **N/A —** constant-volume **canonical** runs without hydrostatic **barostat** control in the excerpted protocol. **Pressure:** initial/target **silane** pressure **~7 MPa** (as stated); thermodynamic pressure evolves during reactive events but is not tabulated further on this page. **Electric field:** **N/A —** not applied. **Enhanced sampling:** **N/A —** brute-force **MD**.

**Static QM / DFT.** **N/A —** **DFT** is **not** the time integrator for the **ReaxFF** decomposition trajectories summarized here.

**Review / non-simulation framing.** **Confined high-pressure CVD** experiments (**20–33 MPa**, **5.9 µm** capillary) provide **Arrhenius** parameters (**Ea = 53.7 ± 2.9 kcal mol⁻¹**, **A = 1.5×10¹⁰ m s⁻¹** as reported) compared against the **heterogeneous** mechanism suggested by simulation. **Corpus note:** `pdf_path` points to a **proof** PDF.

## Findings

**Outcomes and mechanisms.** **Confined HPCVD** measurements give **first-order** **silane** kinetics with **Ea = 53.7 ± 2.9 kcal/mol** and **A = 1.5×10¹⁰ m/s**, with **Ea** in the range reported for **H desorption** from **c-Si** surfaces—supporting **H-desorption-limited** growth. **ReaxFF** trajectories on **clean** **c-Si** show rapid **heterogeneous** consumption of **SiH₄** into **silicon hydrides** (**~10 ps** scale in **Figure 4**), whereas **H-terminated** surfaces show **no reaction** under the same protocol, implicating **dangling-bond availability** after **H removal** as **rate-limiting**. **No homogeneous gas-phase reactions** are observed in those simulations.

**Comparisons.** The authors relate the **activation energy** story to **prior** **CVD** literature on **heterogeneous** vs **homogeneous** pathways under conditions where **silane adsorption** outcompetes **oligomer** adsorption.

**Sensitivity and design levers.** **Pressure** (**20–33 MPa** experiments vs **~7 MPa** simulation cell), **temperature** (**400 °C**-class conditions in simulation), and **surface termination** (**clean** vs **H-passivated**) are the primary levers discussed.

**Limitations and outlook (as authored).** **Proof** PDF; full **reactor** dimensions, **flow**, and **SI** **MD** settings exceed this short summary—use the **article/SI** for reproduction.

**Corpus honesty.** Simulation cell parameters are abbreviated here; **`pdf_path`** is a **proof** duplicate—confirm final values on the **version-of-record** when available.

## Limitations

Proof PDF; ReaxFF system size and timescales are illustrative of mechanism, not full reactor chemistry.

## Relevance to group

Adri C. T. van Duin is a co-author; connects ReaxFF to semiconductor CVD kinetics.

## Citations and evidence anchors

- DOI: `10.1021/acs.iecr.7b03515`

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Corpus file is a **proof** PDF.
