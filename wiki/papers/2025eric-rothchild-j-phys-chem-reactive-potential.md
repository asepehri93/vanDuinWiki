---
id: paper:2025eric-rothchild-j-phys-chem-reactive-potential
type: paper
title: "Reactive Potential for the Simulation of Active Brazing of a Ceramic–Metal Interface"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - method:reaxff
  - method:dft-static
  - material:oxide
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:metallic-systems
  - keyword:oxide-surface
source_refs: []
doi: "10.1021/acs.jpcc.5c00228"
year: 2025
authors:
  - "Eric Rothchild"
  - "Diana M. van Duin"
  - "Malgorzata Kowalik"
  - "Ian Winter"
  - "Anne Grillet"
  - "Adri C. T. van Duin"
  - "Michael Chandross"
venue: "J. Phys. Chem. C"
pdf_sha256: "4431aab52eadbef165c58b83bf6c894a0acd5dffed698971094687a8b6a4de6c"
pdf_path: "papers/Rothchild_RxFF_2025_JPC_alloy_brazing.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025eric-rothchild-j-phys-chem-reactive-potential -->

## Summary

The paper develops a **seven-element Fe/Ni/Co/Ag/Al/Zr/O** **ReaxFF** parameterization aimed at **liquid metal–metal** and **liquid metal–alumina** interfaces relevant to **active brazing** (Ag–Zr filler on **Kovar** vs **α-Al\(_2\)O\(_3\)**), emphasizing **surface tension**, **heats of formation**, and **interfacial reactions** connected to **run-out** in braze joints.

## Methods

- **QM training data:** **Amsterdam Modeling Suite (AMS) 2021.102** — periodic **BAND** with **PBE-D3**, **DZ** basis, small frozen core, scalar relativity, “good” numerical quality; cluster **ADF** calculations preferentially **PBE-D3**, **TZ** basis, “very good” quality; **BLYP-D3** or **M06** used where **PBE-D3** failed to converge (noted for some **Fe/Co** angle scans). **H/O** started from the **aqueous** ReaxFF branch; **Zr–O** training augmented with **OQMD** data; training included metals, oxides, alloys, and mixed-metal oxides. **Zr/O** parameters transferred from combustion to aqueous branches were **refit** to better capture **suboxide** energetics.
- **ReaxFF optimization:** Standalone **ReaxFF** trainer (Penn State **Materials Computation Center** distribution referenced in the article) with parabolic interpolation/extrapolation workflow; initial parameters merged from prior ReaxFF lines as described.
- **Melting and surface tension (LAMMPS):** **Melting temperatures** via **solid–liquid coexistence** workflows (**0.5 fs** timestep, **Langevin** thermostat for initial solid equilibration; **Nosé–Hoover** coexistence segments, **PTM** structure analysis in **OVITO** with criteria stated in the paper). **Surface tensions** from **liquid slabs** (**~4000 atoms**, **NVT**, **1.5 ns** production, stress sampling).
- **Diffusion:** **MSD** slopes from **~100 ps** liquid simulations (**~9826-atom** cells) for **Ag** and dilute **Al/Zr/O** in Ag.
- **Interface MD:** **Molecular dynamics** in **LAMMPS**; **Al\(_2\)O\(_3\)** vs **Ag** and **Ag–Zr** liquids at **1600 K** for **500 ps**; **Kovar(111)** vs **Ag**, **Ag–10% Zr**, **Ag–10% Al** slabs (**924** liquid on **1728**-**atom** substrate) at **1600 K** for **600 ps** with **3D PBC** **periodic** **slabs**; additional **600 ps** after **Al** addition. **1 atm**-like **NPT** may appear in other validation blocks, but the quoted interfacial runs are typically **NVT** at high **T**; **N/A** — isotropic **pressure** control in every short interfacial segment. **N/A** — static **external electric field**; **N/A** — **metadynamics**; **N/A** — **umbrella** in this **brazing** interfacial protocol summary.
## Findings

- The force field reproduces many **heats of formation** and **equations of state** reasonably across metals/oxides; **liquid Ag/Al alloy surface tensions** track experiments with noted trade-offs in parameterization.
- **Melting points** are **qualitatively** sensible for the braze-relevant window, but **pure Ag** is **~350 K** above experiment in this parameterization—nonetheless below oxides/Kovar such that **molten filler vs solid substrates** can still be staged.
- **Ag–Al\(_2\)O\(_3\)** simulations show **Zr scavenging oxygen** and forming **Zr-rich suboxide** clusters; **pure Ag** also shows **O** transfer that the authors flag as a **limitation** of the model.
- **Kovar** interfaces show **Zr-driven intermetallic** formation and complex segregation; **Ag–10% Al** does not show strong **Al** excess at the Kovar interface in these short trajectories, in tension with some **EAM** literature but aligned with other cited braze studies.
## Limitations

The authors highlight **elevated Ag melting**, problematic **Ag–alumina** behavior including **O scavenging by pure Ag**, and **Ag–alumina interface instability** as weaknesses; quantitative comparison to experiment for suboxide stoichiometry may require **grand-canonical** or fixed-**μ** protocols not used here.

## Relevance to group

**Rothchild**, **Diana M. van Duin**, **Kowalik**, **Chandross**, **van Duin**: **ReaxFF** for **active brazing** **Ag–Zr** fillers on **alumina**/**Kovar**-class interfaces.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpcc.5c00228](https://doi.org/10.1021/acs.jpcc.5c00228)

## Related topics

- [[reaxff-family]]
