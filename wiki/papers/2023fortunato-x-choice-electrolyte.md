---
id: paper:2023fortunato-x-choice-electrolyte
type: paper
title: "Choice of Electrolyte Impacts the Selectivity of Proton-Coupled Electrochemical Reactions on Hydrogen Titanate"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:reaxff-application
  - keyword:galley-or-proof-pdf
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c01057"
year: 2023
authors:
  - "Jenelle Fortunato"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Veronica Augustyn"
venue: "J. Phys. Chem. C"
pdf_sha256: "221aee963e32f97d48f29e08100e5ca82cb7106780b734e31be8a855aa308580"
pdf_path: "papers/Fortunato_JPCC_Titanate_H2SO4_H3PO4_2023_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023fortunato-x-choice-electrolyte -->

## Summary

**Proton-coupled electrochemistry** on **metal oxides** in **acid** competes **intercalation**, **hydrogen evolution (HER)**, and **dissolution**, so **electrolyte choice** can dominate **Coulombic efficiency** even when the **active oxide** is unchanged. Layered **hydrogen titanates** are **proton** **hosts** for **pseudocapacitive** **energy** **storage**, making **side reactions** especially visible in **galvanostatic** **cycling** metrics that integrate **Faradaic** **charge** with **parasitic** **currents**. **Fortunato**, **Shin**, **van Duin**, and **Augustyn** study **layered hydrogen titanate H₂Ti₃O₇ (HTO)** in **1 M sulfuric acid** versus **buffered 1 M phosphoric acid**, pairing **cyclic voltammetry** with **ReaxFF molecular dynamics** of **electrolyte–surface** contacts. The **electrochemical** **comparison** is intentionally **isothermal** and **isoconcentrated** on a **molarity** basis so that **anion** **identity** remains the dominant **variable** between **cells**, simplifying **interpretation** of **Coulombic efficiency** shifts. The **J. Phys. Chem. C** abstract reports **average Coulombic efficiency** improving from roughly **48% to 71%** and **specific capacity** from roughly **83 to 90 mAh g⁻¹** when moving from **H₂SO₄** to **H₃PO₄**, motivating atomistic explanations for **HER suppression** and **dissolution** mitigation.

## Methods

### Material synthesis

**Layered hydrogen titanate H\(_2\)Ti\(_3\)O\(_7\)** prepared from **Na\(_2\)Ti\(_3\)O\(_7\)** via **solid-state** + **ion-exchange** steps in the article.

### Electrochemical experiments

- **Electrolytes:** **1 M H\(_2\)SO\(_4\)** vs **buffered 1 M H\(_3\)PO\(_4\)** at comparable **molarity** and **potential windows** vs **Ag/AgCl**.
- **Metrics:** **Cyclic voltammetry**, **capacity**, and **Coulombic efficiency** (abstract quotes ~**48% → 71%** CE and ~**83 → 90 mAh g\(^{-1}\)** capacity improvement for **H\(_3\)PO\(_4\)** vs **H\(_2\)SO\(_4\)**—confirm exact conditions in the PDF).

### Ex situ characterization

**XRD**, **SEM**, **Raman**, **XPS**, **ICP-OES** for **phase**, **morphology**, **Ti** oxidation states, and **Ti dissolution** after cycling.

### ReaxFF interfacial MD (B)

**Explicit water** + **acid anions** at **HTO** surfaces; **Ti(III)** chemistry via parameter lineage documented in **`[[2023fortunato-venue-paper]]`** (SI PDF).

### MD application (integrated; proof-PDF copy)

**Engine / code:** **LAMMPS**+**ReaxFF** (group practice for **aqueous** **oxide** interfaces; exact **build** in **JPCC** *Computational* / **SI**). **System & composition:** **H\(_2\)Ti\(_3\)O\(_7\)** **(001)**-class **slabs** with **1 M** **H\(_2\)SO\(_4\)** vs **buffered 1 M** **H\(_3\)PO\(_4\)** **solutions** (cell sizes and **ion** counts: **N/A in wiki copy**). **3D PBC** **slab** **+** **reservoir**-style **electrolyte** model as in the **article**; **N/A** — exact fixed layers, timestep (fs), ps/ns, thermostat/barostat, NPT vs NVT, temperature setpoints (e.g. ~300 K isotropic MD in many interfacial aqueous setups), pressure, long-range **Coulomb**/ReaxFF **QEq** in this short note—see proof/VOR **Methods**. **N/A** — no **replica exchange** in the interfacial **MD** described in the abstract. **E-field:** **N/A** — no **static** field **bias** in the same sense as a **gated** device; **comparisons** to **CV** in **[[2023jenelle-fortunato-j-phys-chem-choice-electrolyte]]** if a **VOR** slug is curated.

## Findings

### Electrochemical performance shift

**Phosphoric** electrolyte yields **higher Coulombic efficiency** and **specific capacity** than **sulfuric** acid under the authors’ matched protocols (see abstract numbers).

### Atomistic interpretation (qualitative)

**Phosphate** **adsorbs** more strongly than **sulfate**, **buffering** interfacial **acidity** and **passivating** **reactive Ti** sites—consistent with **suppressed HER**/**dissolution** in MD and improved **electrochemical** metrics.

### Experimental corroboration

**Spectroscopy**/**ICP** data link **Ti loss** and **phase** retention to **electrolyte** choice, separating **dissolution**-driven fade from other effects.

### Caveat

**ReaxFF** supports **mechanistic** hypotheses, not fitted **elementary rates**; **proof PDF** path in corpus—prefer **VOR** pagination when citing **`[[2023jenelle-fortunato-j-phys-chem-choice-electrolyte]]`** for final figures.

## Limitations

The corpus PDF (`papers/Fortunato_JPCC_Titanate_H2SO4_H3PO4_2023_proof.pdf`) is an **ACS proof**; cite **`[[2023jenelle-fortunato-j-phys-chem-choice-electrolyte]]`** for **VOR** pagination. Maintainer catalog (GitHub): [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Relevance to group

Showcases **ReaxFF interface MD** (**Shin**, **van Duin**) paired with **aqueous oxide electrochemistry** (Augustyn group).

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.3c01057](https://doi.org/10.1021/acs.jpcc.3c01057)

## Related topics

- [[2023jenelle-fortunato-j-phys-chem-choice-electrolyte]]
- [[2023fortunato-venue-paper]]
- [[reaxff-family]]
