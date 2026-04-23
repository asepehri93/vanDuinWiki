---
id: paper:2019gao-physical-che-reaxff-molecular-2
type: paper
title: "A ReaxFF molecular dynamics study of molecular-level interactions during binder jetting 3D-printing"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - method:reaxff
  - task:application
  - material:oxide
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:nvt-simulation
  - keyword:oxide-surface
  - keyword:validation-experiment
  - keyword:berendsen-thermostat
  - keyword:polymer
source_refs: []
doi: "10.1039/c9cp03585k"
year: 2019
authors:
  - "Yawei Gao"
  - "Yun Kyung Shin"
  - "Daniel Martinez"
  - "Guha Manogharan"
  - "Adri C. T. van Duin"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "794dc1fff4e9df96b836919a56de7675678e64c3d190930177db37b1937e548f"
pdf_path: "papers/Gao_PCCP_binder_jetting_3D_printing_online.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019gao-physical-che-reaxff-molecular-2 -->

!!! note "Corpus PDF role"
    This slug registers the **`..._online.pdf`** file bytes for the *PCCP* article (**DOI `10.1039/c9cp03585k`**). Scientific content matches **[[2019gao-physical-che-reaxff-molecular]]** (alternate **PDF** path).

## Summary

**Binder jetting additive manufacturing** deposits liquid **binder** onto **metal powder** beds; green parts then undergo **curing**, **binder burn-out**, and **sintering**. The **PCCP** study (**Physical Chemistry Chemical Physics**, **DOI** **10.1039/c9cp03585k**) models **AISI** **316L** **stainless** **steel** **powder** as **Cr-rich** **oxide** **nanoparticles** bonded by **aqueous** **diethylene** **glycol** (**DEG**), stepping a **simplified** **thermal** **protocol** (**print** → **cure** → **burn-out** → **sinter**) while tracking **H-bonds**, **organic** **oxidation**, and **Cr–O** **bridge** formation that mirror **green**-stage **cohesion** trends discussed in **additive** **manufacturing** **literature**. At the **atomistic** scale, early-stage cohesion between **oxide-passivated** **stainless steel** particles depends on **hydrogen bonding**, **oxidation** of organic **diols**, and formation of **metal–oxygen** bridges. This paper uses **ReaxFF** molecular dynamics with a **Cr-rich oxide** nanoparticle model and aqueous **diethylene glycol (DEG)** to simulate a simplified **print → cure → burn-out → sinter** thermal protocol. The work relates evolving **H-bond networks**, **DEG** **oxidation** chemistry, and **Cr–O** bond formation to a **restraint-potential** “**breaking strength**” proxy that separates two nanoparticles under controlled strain-rate pulling. Compositional sweeps (**water vs DEG**) and comparisons among **2-ethoxyethanol**, **DEG**, and a more **hydroxyl**-rich **triol** clarify how **binder** chemistry affects **green**-stage cohesion in the model.

## Methods

### Force-field lineage (A)

**Cr/C/H/O ReaxFF** (**Shin et al.**) for **Cr₂O₃**-like **passivated** nanoparticles—same science as **[[2019gao-physical-che-reaxff-molecular]]**.

### Molecular dynamics and mechanical probe (B)

**Preparation, print/cure/burn-out/sinter** staging, **NVT**, **Berendsen** (**100 fs**), **restraint** potential (**Eq. 3**), and **Sets A/B** match the **VOR** article summarized on **[[2019gao-physical-che-reaxff-molecular]]**; this slug differs only by **`..._online.pdf`** bytes.

**Restraint** **separation** applies a **bell-shaped** **force** between **paired** **atom** **lists** on **two** **nanoparticles**, **ramping** **separation** at a **controlled** **strain** **rate** so **peak** **force** **before** **rupture** serves as a **scalar** **proxy** for **green** **strength**—the same **Eq.** **3** **machinery** described on the **canonical** **page**.

### DFT (C)

**Not applicable** as primary—**ReaxFF** **BJP** application.

**Corpus duplicate note.** Same protocol narrative as [[2019gao-physical-che-reaxff-molecular]]: **periodic** **80 Å** / **200 Å** **cells**, **NVT** **Berendsen** staging, multi-**K** ramps (**300 K** print, **393 K** cure, **900 K** burn-out, **1900 K** sinter per the **PCCP** article), and restraint **MD** with **production** segments in **ps**/**ns** scales given in the **PCCP** **PDF**. **Barostat / pressure servo:** **N/A** (constant-volume workflow). **External electric field:** **N/A**. **Enhanced sampling:** **N/A**.

## Findings

### Mechanisms, limitations, outlook

Qualitative conclusions match **[[2019gao-physical-che-reaxff-molecular]]**: **H-bond**-mediated **print/cure** cohesion, **DEG** consumption at **burn-out**, **Cr–O** **sinter** bridges, **hydroxyl** trends among binders, and **nanoscale**/**ns** scope limits for **industrial** **BJP** mapping.

**Stage-resolved** **observables** on the **canonical** page include **radial distribution** shifts for **Cr–O** during **sintering**, **DEG** **fragmentation** products after **900 K** **burn-out**, and **restraint-force** **peaks** during **separation** that rank **binder** **chemistry**—read **`[[2019gao-physical-che-reaxff-molecular]]`** for **Table 1**/**Eq. 3** locators tied to those **plots**.

## Limitations

**Nanoparticle** size and **nanosecond** MD windows do not reproduce industrial **time/length** scales for **BJP**; the study targets **qualitative** **mechanistic** trends rather than **quantitative** part-scale **properties**.

## Reader notes (navigation)

- Alternate PDF: **[[2019gao-physical-che-reaxff-molecular]]**
- [[reaxff-family]]
