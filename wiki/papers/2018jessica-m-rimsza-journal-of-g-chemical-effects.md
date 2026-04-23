---
id: paper:2018jessica-m-rimsza-journal-of-g-chemical-effects
type: paper
title: "Chemical effects on subcritical fracture in silica from molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - method:reaxff
  - task:application
  - material:silicate-glass
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1029/2018JB016120"
year: 2018
authors:
  - "Jessica M. Rimsza"
  - "Reese E. Jones"
  - "Louise J. Criscenti"
venue: "J. Geophys. Res.: Solid Earth"
pdf_sha256: "0b1a255e269e6ba071a819293482dfe5f114d57962093d0c257d75dd093be8be"
pdf_path: "papers/ReaxFF_others/Rimsza-JGR-2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018jessica-m-rimsza-journal-of-g-chemical-effects -->

## Summary

**ReaxFF** (**USER-REAXC**, **Yeon & van Duin 2015 Si/O/H**) **MD** in **LAMMPS** evaluates **mode-I** loading of **silica** with three scenarios: **vacuum** dynamic fracture, **water-filled** crack dynamic fracture, and **water** with **static** subcritical load plus dissolution tracking. The central question is whether humidity primarily sharpens crack tips through surface chemistry or also softens the bulk process zone through water-mediated Si–O scission. **Water** reduces **K\(_{IC}\)**-like toughness metrics by **~25%**, consistent with experiment; **water** **plasticizes** the **process zone** broadly, not only **surface** sites, lowering **Si–O** rupture thresholds **without** requiring large **dissolution** flux. The **JGR** framing connects **geophysical** **subcritical** fracture to **atomistic** **stress corrosion** language used in **materials** science.

## Methods

- **Engine / code:** **LAMMPS** **molecular dynamics** with **USER-REAXC** **ReaxFF** integration.
- **Potential:** **ReaxFF Si/O/H** parameterization **Yeon & van Duin (2015)** via **USER-REAXC**; prior **surface energy**/**modulus** benchmarks discussed in-paper.
- **Thermostat:** **Nosé–Hoover** (or equivalent **NVT** **thermostat** parameters) as specified in *J. Geophys. Res.* **Methods** for the **300 K** production segments.
- **Crack geometry:** **LEFM** **mode-I** displacement field applied to **far-field** atoms; **frozen** boundary band; interior **mobile**; **nonperiodic** in-plane after initial relaxation.
- **Protocol A (mechanical):** Increment **K\(_I\)** by **0.071 MPa·√m** steps; **NVT** **300 K**, **0.1 fs**, **5 ps** per step; **100** steps to **K\(_I\)≈0.65 MPa·√m** fracture.
- **Protocol B (chemical):** Fixed load; add **water** in crack at **0.5 g/cm³**; **reflective** walls; **500 ps** **NVT** at **300 K**, **0.1 fs**.
- **Protocol C (coupled):** **Iterative loading** + **GCMC** water resupply to maintain coverage as volume opens (details in paper).
- **Diagnostics:** Track **Si–O** bond populations, **coordination** defects, and **dissolution**-like events separately so **mechanical** failure can be distinguished from **corrosion**-like mass loss.

**Additional controls.** **PBC / geometry:** **mode-I** **LEFM** displacement on **far-field** atoms with a **frozen** boundary band and **mobile** interior; **nonperiodic** opening in the crack plane after relaxation (see article). **Barostat / bulk pressure:** **N/A — NPT** hydrostatic control not used for the quoted **NVT** **fracture** stages. **Electric field:** **N/A — bias** not applied. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not reported.

## Findings

**Outcomes and mechanisms.** **Water** lowers effective **toughness** metrics by **~25%** versus **inert** environments while **plasticizing** the **process zone** through **Si–O** scission pathways that are not limited to the immediate **crack tip**; **dissolution** can be minor yet **subcritical** **failure** accelerates because **solvation** lowers **bond** rupture thresholds.

**Comparisons.** Trends are discussed against **experimental** stress-corrosion **literature** for **silica** and against purely **surface**-roughening pictures.

**Sensitivity.** **Stress** level, **water** presence (**0.5 g/cm³** in the static-chemistry cell), and **loading** protocol (**K\(_I\)** stepping vs fixed load + **GCMC** resupply) change how **decomposition** vs **mechanical** damage partition.

**Limitations and PDF grounding.** Absolute **ReaxFF** **fracture** numbers and **GCMC**+**MD** coupling approximations limit transferability; confirm **coordination** definitions in the **JGR** **PDF** (`pdf_path`).
## Limitations

**ReaxFF** fracture absolute values; **GCMC**+**MD** coupling approximations; **2D** **slit** crack idealization. Real geological silica networks include disorder, microporosity, and ionic impurities that can couple to subcritical crack growth in ways a single ideal crack cannot represent, so the reported toughness shifts are best interpreted as mechanistic trends benchmarked against the experimental window cited in the paper.

## Relevance to group

Pairs with **[[2018jcp-silica-hydrophil-venue-paper]]** on **silica** **reactivity**; uses **van Duin** **Si/O/H** parameter line.

## Citations and evidence anchors

- DOI: `10.1029/2018JB016120`.

## Reader notes (navigation)

- Silica mechanics and tribochemistry cluster: [[theme-oxides-silica-ceramics]]; parameter line [[2016yeon-venue-la5b04062-2]] / Yeon Si/O/H ReaxFF.

## Related topics

- [[2018jcp-silica-hydrophil-venue-paper]]
- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
