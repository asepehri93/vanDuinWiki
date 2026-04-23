---
id: paper:2018hu-nat-role-disordered
type: paper
title: "Role of disordered bipolar complexions on the sulfur embrittlement of nickel general grain boundaries"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - method:reaxff
  - task:application
  - material:metal-surface
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41467-018-05070-2"
year: 2018
authors:
  - "Tao Hu"
  - "Shengfeng Yang"
  - "Naixie Zhou"
  - "Yuanyao Zhang"
  - "Jian Luo"
venue: "Nat. Commun."
pdf_sha256: "290e04f79b51d3c71462090cf9bedcf9fdd77bd38b8b0388c7111af1123582d7"
pdf_path: "papers/ReaxFF_others/Hu_NatureComm_2018_ReaxFF_NiS.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018hu-nat-role-disordered -->

## Summary

**Sulfur embrittlement of nickel** is a long-standing metallurgical puzzle. The **abstract** reports **aberration-corrected STEM** combined with **semi-grand-canonical hybrid Monte Carlo / molecular dynamics** using a **DFT-trained ReaxFF** for **Ni–S**, revealing—unexpectedly—that **the same general grain boundaries** can exhibit **both amorphous-like and bilayer-like facets**. **Lower-Miller-index** **grain surface** orientation, rather than **misorientation alone**, is argued to **dictate** which **interfacial structure** appears—challenging traditional emphasis on **misorientation**. Both complexion families show **partial bipolar structural order** within **thermodynamically two-dimensional intergranular phases** (“complexions”), linked in the paper to **brittle intergranular fracture**. The authors also connect the mechanism to **abnormal grain growth** in **S-doped Ni** and suggest broader relevance of **disordered yet partially ordered** interfaces across materials.

## Methods

**Experiments** saturate **Ni** with **S**, perform **isothermal** anneals and **quenches** across **temperature** windows including **500–675 °C**, and characterize **tens of GB facets** with **AC-STEM** (**ABF/HAADF**) plus **EDXS/EELS**-based **adsorption** metrics (**Γ_S** examples appear in the main text).

**Atomistic sampling:** **Hybrid Monte Carlo / molecular dynamics** (**MC/MD**) with a **DFT**-trained **ReaxFF** for **Ni–S** is carried out in **LAMMPS**-class software as described in **Nat. Commun.** Methods, using **semi-grand-canonical** control to vary **S** content while exploring **grain boundary** **supercells** containing **hundreds to thousands of atoms** under **3D periodic boundary conditions**. **Timestep** and **thermostat** settings for the hybrid moves appear in the **PDF**; **N/A — external electric field** during the equilibrium sampling emphasized here. **NPT** vs **NVT** choices follow the article’s **pressure**/**stress** prescriptions for the simulation cells (see **PDF** tables).

**STEM image simulations** compare model **disorder** and **segregation** to **microscopy**. Analysis emphasizes **bipolar** signatures and **excess** **S** **areal densities** for **Type A vs Type B** facets.

## Findings

**Outcomes & mechanisms:** **Type A** (**amorphous-like**) vs **Type B** (**bilayer-like**) **complexions** coexist on **general** **Ni** **grain boundaries** under **S** segregation; both families show **partial bipolar order** within **thermodynamically two-dimensional** interfacial films linked to **brittle** **intergranular fracture**.

**Comparisons:** **AC-STEM** **EDXS**/**EELS** **Γ\(_S\)** values are compared to **hybrid MC/MD** + **ReaxFF** predictions (example paired entries near **34.9** vs **23.9** **S**/nm² for **Type A** and **12.6** vs **12.1** **S**/nm² for **Type B** facets in **Table 1**—operators must verify exact rows in **`pdf_path`**).

**Sensitivity:** **annealing temperature** shifts the fraction of **faceted** boundaries (article quotes **~54%** at **500 °C** increasing toward **~84%** at **675 °C** in the summarized statistics); **lower-Miller-index** terminating **grain** **surface** orientation—not **misorientation** alone—is argued to dictate which **complexion** appears.

**Limitations / outlook:** **ReaxFF** remains **empirical** for **liquid-like** **IGFs**; **kinetics** may prevent full **equilibrium**; **STEM** gives **projected** structural information.

**Corpus honesty:** mechanistic sentences above track the **abstract**/**introduction** plus **Table 1** visible in **`normalized/extracts/2018hu-nat-role-disordered_p1-2.txt`**; deeper **MD** parameters require the **full** **PDF**.

## Limitations

**ReaxFF** remains **empirical** for **liquid-like** **IGFs**; **kinetics** may impede full **equilibrium** in experiments. **STEM** provides **projected** information; **3D** connectivity may differ. **Ni–S** parameter **transferability** to **alloys** is not automatic.

## Relevance to group

Demonstrates **ReaxFF** in **open-system** **hybrid MC/MD** for **metallurgical segregation** and **complexion** physics—distinct from **oxide** applications but sharing the **same reactive FF** toolchain used in **materials** modeling across the wiki.

## Citations and evidence anchors

- DOI: `10.1038/s41467-018-05070-2` — `papers/ReaxFF_others/Hu_NatureComm_2018_ReaxFF_NiS.pdf`; extract `normalized/extracts/2018hu-nat-role-disordered_p1-2.txt`.

## Related topics

- [[reaxff-family]]
