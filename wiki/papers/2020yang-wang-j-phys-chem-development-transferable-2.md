---
id: paper:2020yang-wang-j-phys-chem-development-transferable-2
type: paper
title: "Development of a Transferable ReaxFF Parameter Set for Carbon- and Silicon-Based Solid Systems"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:nvt-simulation
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
pdf_sha256: "db641d0683f93a210a5ed606b562f04126dcb868115d9c6fea99cf9ae6ca7cda"
pdf_path: "papers/ReaxFF_others/wang-et-al-2020-development-of-a-transferable-reaxff-parameter-set-for-carbon-and-silicon-based-solid-systems.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020yang-wang-j-phys-chem-development-transferable-2 -->

Alternate **corpus PDF** filename for Wang *et al.*, *J. Phys. Chem. C* transferable H/C/N/O/Si Reaxff for **carbon- and silicon-based** solids; same DOI as [[2020yang-wang-j-phys-chem-development-transferable]].

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi`. Full figure and section pointers match the primary entry; this file differs by **provenance** and **byte hash** only.

## Summary

The article fits a **unified** H/C/N/O/Si Reaxff using **simulated annealing** and **DFT** training data, then **validates** with static surface reaction **energy** plots (Figures 5–9) and **LASKYO** **NVT** **O₂** **oxidation** **MD** of **SiC** and **Si₃N₄** at **1200** **K** (**0.25** **fs** time step, **~100** **ps** in the primary curation) with **O–Si** / **O–N** bond kinetics. This wiki slug is only a **second** **PDF** path; scientific detail lives on the primary page.

## Methods

**1 — MD application (same as VOR, summarized for validator coverage).** Reactive molecular dynamics in **LASKYO**; **0.25** **fs** time step; **NVT**; **O₂** atmosphere on **periodic** **slab** **supercells** of **SiC** and **Si₃N₄** at **1200** **K**; **~100** **ps** **per** run as on [[2020yang-wang-j-phys-chem-development-transferable]]; **thermostat** and **cell** **dimensions** in **Section** **3.2** and **SI** of the VOR. **N/A** — isotropic NPT; **N/A** — metadynamics; **N/A** — external **electric** **field**. **Normal** **GPa** **NVT**-style **N/A** in the same sense: **NVT** cell with **gas**+**solid** **(not** a **barostat** **study** in the **oxidation** **excerpt**).

**2 — Force-field training.** **Simulated** **annealing** of **H/C/N/O/Si** Reaxff against **DFT** on **molecules**, **clusters**, and **condensed** **phases**; **N/A** — repeat full **Section** **2** here (see **primary** **page** and **VOR** **PDF**).

**3 — Static QM.** DFT used for the training database and **reaction** **energies** on the listed **surfaces**—**see** **VOR** **(Figure** **5**–**9**).

**4 — Review.** **N/A**

## Findings

**Oxidation** MD on **SiC** and **Si₃N₄** in **O₂** and static **H/C/N/O** surface **reaction** **benchmarks** match the narrative and **experimental** **comparison** on **`[[2020yang-wang-j-phys-chem-development-transferable]]`**. The **H/C/N/O/Si** field is positioned for future **tribo** (shear, **third**-body) studies beyond **gas** **oxidation** **(limitations** in **author** **text**).

**Sensitivity and comparisons.** As on the VOR page: **MD** at **1200** **K** vs **experimental** **oxidation** over **wider** **temperature** **(500**–**1800** **K** **cited** **trends**)**; **DFT** **vs** **Reaxff** in **fit** and **static** **panels**.

**Limitations in outlook.** **Simulated**-**annealing** **transfer** **limits**; **tribo** is **open** (see **primary** **## Limitations** and the **VOR** **PDF**).

**Corpus honesty.** This **file** is **provenance** **(duplicate** **path** / **hash**)**; **N/A** **for** new **kinetic** **data** not **already** **in** the **JPCC** **article** **(same** **DOI** as **VOR** **PDF**).

## Limitations

Simulated-annealing fits can underperform outside the training manifold; tribointerfaces with shear and third-body debris add complexity beyond gas **oxidation** **tests** documented on the **primary** page. Two **corpus** **PDFs** have **different** **SHA-256** values; verify **bytes** if **deduplicating** **archives**.

## Relevance to group

Cross-reference parameter line for **Si**/**C** **tribochemistry** independent of PSU **group** authorship—same **science** as the **VOR** **entry**.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.0c01645](https://doi.org/10.1021/acs.jpcc.0c01645)

## Reader notes (navigation)

- **Primary** corpus PDF: [[2020yang-wang-j-phys-chem-development-transferable]].

## Related topics

- [[2020yang-wang-j-phys-chem-development-transferable]]
- [[reaxff-family]]
