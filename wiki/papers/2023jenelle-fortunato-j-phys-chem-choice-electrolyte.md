---
id: paper:2023jenelle-fortunato-j-phys-chem-choice-electrolyte
type: paper
title: "Choice of Electrolyte Impacts the Selectivity of Proton-Coupled Electrochemical Reactions on Hydrogen Titanate"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c01057"
year: 2023
authors:
  - "Jenelle Fortunato"
  - "Yun Kyung Shin"
  - "Michael A. Spencer"
  - "Adri C. T. van Duin"
  - "Veronica Augustyn"
venue: "J. Phys. Chem. C"
pdf_sha256: "77e12280bb30f8df5bd1867f1869af6c55463685616a7125116fb507694428e3"
pdf_path: "papers/Fortunato_Shin_JPCC_2023_titanate_H3PO4_H2SO4.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023jenelle-fortunato-j-phys-chem-choice-electrolyte -->

## Summary

Proton-coupled electrochemistry on layered oxides depends sensitively on electrolyte speciation because acids modulate both Faradaic selectivity and parasitic hydrogen evolution or dissolution. This *Journal of Physical Chemistry C* article examines hydrogen titanate H₂Ti₃O₇ electrodes in 1 M phosphoric acid versus 1 M sulfuric acid, combining cyclic voltammetry, galvanostatic cycling, and materials characterization with ReaxFF molecular dynamics of the electrode–electrolyte interface. Yun Kyung Shin and Adri C. T. van Duin contribute the reactive modeling leg alongside experimental collaborators led by Veronica Augustyn. A separate wiki slug may register an alternate proof PDF for the same DOI; this page tracks the issue-aligned PDF path in frontmatter for operators who attach the publisher file locally.

## Methods

### Electrode synthesis and electrochemical testing

**H\(_2\)Ti\(_3\)O\(_7\)** prepared from **Na\(_2\)Ti\(_3\)O\(_7\)** via **solid-state** + **ion-exchange** routes (**Experimental** section). **Aqueous** cells with **Ag/AgCl** reference; compare **1 M H\(_2\)SO\(_4\)** vs **buffered 1 M H\(_3\)PO\(_4\)** at matched protocol choices.

### Ex situ characterization

**XRD**, **SEM**, **Raman**, **XPS**, **ICP-OES** for **phase**, **morphology**, **surface chemistry**, and **Ti dissolution**.

### ReaxFF interfacial MD (B)

Explicit **electrolyte–surface** models resolving **water**, **acid anions**, and **protonation** motifs; **parameter** extension and **Ti(III)** surrogate details in **`[[2023fortunato-venue-paper]]`** (SI PDF).

### 1 — MD application (atomistic dynamics) — interfacial leg

**Engine / code:** **LAMMPS** with **ReaxFF** (extended parameterization for **H–Ti–O**/**acid** **chemistry** as in the SI / companion slug). **System & composition:** **H\(_2\)Ti\(_3\)O\(_7\)**-water–**electrolyte** **(H\(_2\)SO\(_4\)** or **H\(_3\)PO\(_4\))** interfacial cells. **Boundaries / periodicity:** in-plane **PBC** for **slab**/**surface** supercells. **Ensemble, timestep, thermostat, duration:** **N/A** on this page—**SI** simulation cells in **`[[2023fortunato-venue-paper]]`** document **NVT**-class **sampling** and numerical **controls**; the main text figures give qualitative structure. **Barostat, pressure, shear, shock:** **N/A** in this interfacial **NVT**-like summary. **Temperature:** near **ambient** **aqueous** **interface** (as in SI) unless otherwise stated. **External electric field in MD:** **N/A** — the experiment applies **galvanostatic**/**CV** **bias**; the **ReaxFF** work supports speciation/association at the **unbiased**-slab or **mild**-driving level described in the article/SI, not a full **device** **field** map. **Coulomb / ReaxFF QEq:** as implemented for the **FF** in use. **Enhanced sampling:** **N/A** here.

### 2 — Force-field training

**N/A** on this **issue-PDF** page; **new** or **reweighted** **terms** and **DFT** training data are in **`[[2023fortunato-venue-paper]]`** and related SI.

### 3 — Static QM

**N/A** in this work’s modeling core; **DFT** may appear in prior **HTO** literature elsewhere as cited, but the paper’s new atomistic **leg** is **ReaxFF** **MD**.

## Findings

### Electrochemical metrics (abstract)

**Average Coulombic efficiency** improves ~**48% → 71%** and **capacity** ~**83 → 90 mAh g\(^{-1}\)** when switching **H\(_2\)SO\(_4\)** → **H\(_3\)PO\(_4\)** at the stated concentrations.

### Experimental interpretation

**Phosphoric** media are argued to **buffer** interfacial **acidity** and reduce **HER**/**HTO dissolution** vs **strongly acidic sulfate**.

### Atomistic support (qualitative)

**ReaxFF** trajectories favor stronger **phosphate** **interfacial association** vs **sulfate**, altering **proton availability** and **surface** **passivation**—see main-text figures for structural detail.

## Limitations

Atomistic trajectories cannot span hour-scale dissolution or reprecipitation kinetics observed in cells, nor do they fully resolve porous-electrode transport and local pH gradients; conclusions are therefore mechanistic complements to experiment rather than digital twins of full devices.

## Relevance to group

The study is a primary archival reference for Shin and van Duin ReaxFF modeling of aqueous acid interfaces on titanate proton-storage hosts, linking electrochemistry tags to reactive MD in the corpus.

## MAS / retrieval notes

When this page appears alongside duplicate slugs for the same DOI, prefer the issue PDF path recorded in `normalized/papers` after sync; quote electrochemical metrics with units exactly as printed in the abstract (mAh g⁻¹, Coulombic efficiency) and point users to SI simulation cells for ReaxFF boundary conditions.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.3c01057](https://doi.org/10.1021/acs.jpcc.3c01057)

## Related topics

- [[2023fortunato-x-choice-electrolyte]]
- [[2023fortunato-venue-paper]]
- [[reaxff-family]]
