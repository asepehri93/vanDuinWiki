---
id: paper:2023zhang-venue-manuscript
type: paper
title: "Joint theoretical and experimental study of stress graphitization in aligned carbon nanotube/carbon matrix composites"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - material:graphene-carbon-nano
  - task:experiment-integrated
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.3c03209"
year: 2023
authors:
  - "Liwen Zhang"
  - "Małgorzata Kowalik"
  - "Qian Mao"
  - "Behzad Damirchi"
  - "Yongyi Zhang"
  - "Philip D. Bradford"
  - "Qingwen Li"
  - "Adri C. T. van Duin"
  - "Yuntian T. Zhu"
venue: "ACS Appl. Mater. Interfaces (galley PDF in corpus)"
pdf_sha256: "9987263d138902934676625649648f1d40a6d4b5fd82fce9bea363ba3ff38ea9"
pdf_path: "papers/Zhang_Kowalik_Mao_CNT_Matrix_ACS_AMI_2023_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023zhang-venue-manuscript -->

!!! note "Corpus note"
    The repository contains a **galley** PDF; cite the **version of record** using the DOI below for bibliographic permanence. Maintainer catalog entries for **SI/galley/proof** roles: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Summary

The work combines **ReaxFF-based reactive molecular dynamics (RMD)** with **experiments** on **aligned carbon nanotube (CNT) / polyacrylonitrile (PAN)-derived carbon matrix** composites to explain **stress graphitization** at **CNT–matrix interfaces** during high-temperature treatment. The motivation is that **graphitic** domains around CNTs can strengthen the matrix, but the atomistic drivers of **stress-assisted** carbonization during pyrolysis are not obvious from continuum descriptions alone. **Adri C. T. van Duin** is a corresponding author on the computational line of the study. The abstract contrasts **CNT-free** versus **CNT-reinforced** models and reports that simulations at **1500 K** reproduce a **stress concentration** pattern that promotes **nitrile** orientation, **dehydrogenation**, and **carbon six-membered ring** formation near CNT surfaces, paralleling **TEM**-visible **graphitic** layers in processed films.

## Methods

**Corpus note:** The checked-in file is a **galley** **PDF**; **DOI** `10.1021/acsami.3c03209` is the **bibliographic** **anchor** for **pagination**-sensitive **citations**.

### 1 — MD application (ReaxFF in LAMMPS, CNT / oxidized-PAN, stress graphitization)

- **Engine / code:** **ReaxFF** **RMD** in **LAMMPS**; **VMD** for **snapshots** (*ACS Appl. Mater. Interfaces* Methods).
- **Ensemble, timestep, PBC, thermostat:** **NPT** and **NVT** **stages** use **3D** **PBC**; **time** **step** **0.25** **fs**; **Nose**–**Hoover**-style **coupling** (article reports **100** **fs** **temperature/pressure** **coupling** **constants** for the **NPT** **preequilibration** of the **orthorhombic** **box**); **bond** **order** **0.3** for **chemistry** **parsing** in the **RMD** **setups** (see the *AMI* **Methods** in the corpus **galley** **PDF**).
- **Heating / graphitization:** **Three** **CNT**-**loading** **cases** (**0**, **20**, **80** **wt%** in the **abstract**-level **narrative**) with **1D** **aligned** **tubes**; from **separate** **preequilibrated** **NPT** **snapshots** the **authors** **take** **three** **independent** **seeds** each and **heat/****carbonize** at **1500** **K** in **NVT** for **5** **ns** to study **stress**-**driven** **local** **graphitization** (**Methods**; **align** to **the** **galley** for **all** **stage** **lengths** and **NPT** **T**).
- **Analysis:** **Local** **stress** **(von** **Mises-****type,** as **defined** **in**-**text)** and **chemical** **order** **parameters** tie **higher** **CNT** **loading** to **larger** **peripheral** **stress** and **faster** **dehydrogenation/****ring-****formation** in the **PAN-****derived** **carbon** **(see** **main** **text** **+** **SI** **for** **all** **definitions**). **N/A** in this **short** **note** for a **reprint** of **every** **NPT** **stage** not shown **above**—**see** the **VOR** **+** **SI** when **galley** **line** **wrap** **differs**.

- **Barostat, electric field, rare-event sampling:** **NPT** **preequilibration** and **NVT** **1500** **K** **carbonization** as **quoted**; **N/A** for **E-field**; **N/A** for **metadynamics**; **N/A** for a **separate** **NPT** **barostat** during the **5** **ns** **NVT** **1500** **K** **carbonize** (constant-**T** **MD** in **NVT**).

### 2 — Experiments (CNT array / PAN, mechanical testing, TEM)

**CNTs** (multiwall, **~2–3** **walls**, **4–7** **nm** **diameters**, per *Methods*), **PAN** **precursor**, **film** **infiltration/****pyrolysis** **routes** as **reported**; **tensile** **tests** **(82%**/**144%** **gains** **in** **tensile** **strength**/**Young’s** **modulus** **vs** a **control** in the **abstract**); **TEM** of **graphitic** **layers** **on** **CNTs** (see *AMI* for **sample** **history**).


## Findings

The simulations relate **higher CNT loading** to **stronger stress concentration** near CNT surfaces, which biases **nitrile alignment** and accelerates **local carbonization/graphitization** pathways relative to lower-loading or CNT-free models in the same thermal window. Experimental films show **additional graphitic layers** forming from the **PAN-derived matrix** around CNTs, with large **improvements** in **tensile strength** and **Young’s modulus** (reported at **82%** and **144%**, respectively, in the abstract relative to the chosen baseline). Together, the computational and laboratory results support a **stress-mediated graphitization** mechanism for engineering **CNT/carbon-matrix** interfaces in high-temperature processing.

## Limitations

Process details (exact reactor schedules, full mechanical test statistics, and all imaging conditions) should be taken from the **full PDF/SI** beyond the first-page extract.

## Relevance to group

Demonstrates **ReaxFF** applied to **polymer-derived carbon** and **nanocarbon composite** processing with **experimental validation**, consistent with the group’s **reactive carbonization** portfolio.

## Citations and evidence anchors

- DOI: `10.1021/acsami.3c03209`

## Related topics

- [[reaxff-family]]
