---
id: paper:2013lee-venue-untitled
type: paper
title: "Peel-and-stick: Mechanism study for efficient fabrication of flexible/transparent thin-film electronics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:tribology
  - keyword:oxide-surface
  - keyword:water-interfaces
  - keyword:validation-experiment
source_refs: []
doi: "10.1038/srep02917"
year: 2013
authors:
  - "Chi Hwan Lee"
  - "Jae-Han Kim"
  - "Chenyu Zou"
  - "In Sun Cho"
  - "Jeffery M. Weisse"
  - "William Nemeth"
  - "Qi Wang"
  - "Adri C. T. van Duin"
  - "Taek-Soo Kim"
  - "Xiaolin Zheng"
venue: "Scientific Reports"
pdf_sha256: "950cdddfdf02a831036e97f33ac3409daf1edd24f4c3be9faf5b60dde35eedf7"
pdf_path: "papers/Lee_Sci_Rep_2013_NiO_SiOx_stick_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013lee-venue-untitled -->

## Evidence and attribution

!!! note "Evidence"

    Prose below summarizes the **peer-reviewed article** (**DOI `10.1038/srep02917`**). The corpus filename references **NiO/SiO\(_x\)**-related processing; the abstract centers on **water-assisted transfer printing** mechanics.

## Summary

The **peel-and-stick / water-assisted transfer printing (WTP)** process transfers **thin-film devices** from **metal/SiO\(_2\)/Si** donors to flexible substrates. **Critical adhesion energy** measurements show **water** reduces **metal–SiO\(_2\)** adhesion sharply (abstract: **~70–80%** reduction), enabling **subcritical debonding**. **ReaxFF MD** supports the interfacial picture of **water** interacting with **strained Si–O** networks at the crack tip, consistent with **environment-assisted** debonding concepts. The introduction positions WTP as a **room-temperature water** route to weaken donor adhesion—after devices are fabricated on a **metal-coated** oxide wafer, the metal film plus devices can be peeled in **water** and then laminated to arbitrary receivers—so understanding **metal–oxide** **G\(_c\)** in **air vs water** is central to reproducible yield.

## Methods

**Critical adhesion energy** \(G_c\) was measured with **double-cantilever-beam (DCB)** tests comparing **Ni/SiO\(_2\)** debonding in **air** (~**20% RH**) versus **liquid water** at **21 °C**, tracking **debond growth rate** \(da/dt\) versus applied **debond driving energy** \(G\) (micromechanical test geometry described in the article and **Supplementary** figures). The DCB specimen stacks a **~300 nm** **electron-beam-evaporated Ni** film on **thermal SiO\(_2\)** on **Si**, caps the exposed **Ni** with a second wafer via **epoxy**, and records **da/dt** curves whose endpoints mark **G\(_c\)**.

**1 — MD application (ReaxFF, supporting mechanism):** The article reports **molecular dynamics** using the **ReaxFF** reactive force field to connect **water** with **strained Si–O**-type species at the **metal–SiO\(_2\)** interface in an **environment-assisted subcritical debonding** picture (indexed text and `papers/Lee_Sci_Rep_2013_NiO_SiOx_stick_proof.pdf`). **Ensemble / duration:** **N/A —** whether production legs use **NVE**, **NVT**, or **NPT**, and the **picosecond**/**nanosecond** **production run** lengths, are **not stated** on **`normalized/extracts/2013lee-venue-untitled_p1-2.txt`**. **System / PBC / timestep / thermostat:** **N/A —** **supercell** **atom** counts, **periodic** boundary treatment, **fs** **timestep**, and **thermostat** damping are likewise **not** in the indexed excerpt. **Barostat / pressure:** **N/A —** no **hydrostatic pressure** target or **barostat** is quoted for the supporting **MD** on those pages—confirm in the full **PDF** **Methods**.

**2 — Force-field training:** **N/A —** this work **applies** ReaxFF to an interfacial debonding question rather than reporting a **new** ReaxFF parameterization in the abstract-level material indexed here.

**3 — Static QM / DFT-only:** **N/A —** central evidence for adhesion is **micromechanical \(G_c\)** measurement plus **reactive MD**, not a standalone static **QM** study in the opening pages summarized here.

## Findings

**Outcomes and mechanisms:** For the **Ni** on **thermal SiO\(_2\)** DCB stack, the measured **critical adhesion energy** **\(G_c\)** falls from about **1.37 J m\(^{-2}\)** in air (**~20% RH**, **21 °C**) to about **0.31 J m\(^{-2}\)** in **liquid water**—about an **80%** reduction—so debonding can run at **\(G\)** **well below** the dry **\(G_c\)**, matching **water-assisted subcritical** debonding invoked for **peel-and-stick**. **ReaxFF MD** is cited as supporting **stress-accelerated** interaction of **H\(_2\)O** with **strained Si–O**-type species at the **crack tip** (indexed abstract/introduction, `normalized/extracts/2013lee-venue-untitled_p1-2.txt`).

**Comparisons:** The text contrasts the **ultra-low** **Ni/SiO\(_2\)** **\(G_c\)** in water with a literature **graphene–Cu** **\(G_c\)** near **0.72 ± 0.07 J m\(^{-2}\)** to highlight how **chemically assisted** debonding can undercut even **weak** van der Waals–like metal–carbon interfaces for transfer yield.

**Sensitivity / design levers:** **Humidity** (air **RH** vs liquid water), **metal–SiO\(_2\)** chemistry, and **donor-stack** design are the implied **knobs** for **adhesion** and **transfer** in the peel-and-stick framing (abstract-level summary).

**Limitations and outlook (authored / implied):** The indexed text emphasizes **environment-assisted subcritical debonding** as the **working principle**; detailed **device-yield** limits, **other metals**, and **full MD validation** scope appear later in the **PDF** than the **p1–2** extract.

**Corpus honesty:** Corpus PDF `papers/Lee_Sci_Rep_2013_NiO_SiOx_stick_proof.pdf` is a **Scientific Reports** production file (filename contains **“proof”**); compare pagination to the **version-of-record** **DOI `10.1038/srep02917`** if teaching from specific figures.

## Limitations

MD covers idealized interfaces vs real polycrystalline metals and complex device stacks. Industrial peel-and-stick stacks may also include **adhesion promoters**, **passivation** layers, and **roughness** not represented in the DCB coupon geometry; quantitative transfer forces should therefore be validated on **device-relevant** **stacks** even when **G_c** trends are clear.

## Reader notes (navigation)

- [[reaxff-family]]
