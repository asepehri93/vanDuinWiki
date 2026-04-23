---
id: paper:2015ostadhossein-physical-che-stress-effects
type: paper
title: "Stress effects on the initial lithiation of crystalline silicon nanowires: reactive molecular dynamics simulations using ReaxFF"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - material:widegap-semiconductor
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:lammps
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1039/C4CP05198J"
year: 2015
authors:
  - "Alireza Ostadhossein"
  - "Ekin D. Cubuk"
  - "Georgios A. Tritsaris"
  - "Efthimios Kaxiras"
  - "Sulin Zhang"
  - "Adri C. T. van Duin"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "69de2610ee79ff3a1d5311d4733251229090fd0bcc62bf428c6fe0203d3ef294"
pdf_path: "papers/Ostadhossein_PCCP_LiSi_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015ostadhossein-physical-che-stress-effects -->

## Summary

**ReaxFF** (**Fan et al.** **Si–Li** parameterization) **MD** in **LAMMPS** studies **lithiation** of an **h112**-oriented **crystalline silicon nanowire** (**~5976 Si**) with a **Li reservoir**, emphasizing **(111)** **layerwise** insertion, **amorphization**, a **sharp** **amorphous–crystalline interface (ACI)**, and **compressive stress** that can **stall** the reaction front at **~300 K**. The article also reports **high-temperature** behavior including **amorphous-to-crystalline** **Li–Si** transitions near **1200 K** at **Li:Si ≈ 4.2:1**, connecting **kinetic** lithiation pathways to **phase** behavior accessible at **elevated** **T** in simulation. This **PCCP** article is the **version-of-record**-style entry paired in the corpus with a **proof-PDF** sibling slug documented in `docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`.

## Methods

### Force-field training (validation against QM)

**ReaxFF Si–Li** (**Fan** parameters within the **van Duin** formulation) with **EEM** charges; **QM reference:** **DFT** **NEB** and related benchmarks for **Li** diffusion in **c-Si**/**a-Si** used to validate **migration barriers** as discussed in the article.

### MD application (atomistic dynamics)

**Reactive molecular dynamics** in **LAMMPS** lithiates an **h112** **crystalline Si nanowire** containing **~5976 Si atoms** in a cell **~8.43×9.22 nm²** in cross-section with **periodic boundary conditions (PBC)** along **x,y** ([110]/[111]), a **Li reservoir**, a **reflective** top boundary, and a fixed **bottom** layer. **Equilibration:** **NVT** with **Nosé–Hoover** thermostat from **~1 K** (**10 ps**) then **temperature** ramp to **600 K** at **0.048 K/fs**, then hold for **~2.2 ns** in the equilibration segment described in the paper. **Production:** **velocity Verlet** with **Δt = 0.25 fs**; **NVE** segments are used where noted alongside **NVT**; **virial stress** tracks **chemo-mechanical** fields at the **ACI**. **Barostat / NPT pressure:** **N/A** for the summarized **constant-volume** **nanowire** workflow. **Electric field / umbrella or metadynamics:** **N/A**.

## Findings

- **ReaxFF** **Li** diffusion barriers in bulk **c-Si**/**a-Si** match **DFT** benchmarks (e.g., **~0.58 eV** path discussed vs **DFT ~0.55 eV**).
- Lithiation proceeds by **Li** insertion between **(111)** bilayers, **peeling** layers and **amorphizing**; **high local Li** needed to break **Si–Si** bonds explains **sharp ACI**; **compressive stress** at **ACI** can **retard** the reaction front (**~300 K** conditions).
- At **~1200 K**, **Li:Si ≈ 4.2:1** shows **amorphous→crystalline** **Li–Si** behavior as reported, illustrating **temperature**-driven **ordering** distinct from room-temperature **frontal** lithiation.

## Limitations

**ReaxFF** training limits; **NW** model vs experimental **TEM** cells; reflection/thermostat choices affect front kinetics; **2D periodic** **NW** idealization omits full **electrode** microstructure. **Electrolyte** and **SEI** chemistry are absent, so **voltage**-dependent **driving forces** for **Li** insertion are not modeled explicitly in the reactive **MD** shown.

## Relevance to group

Core **van Duin** / **Penn State** **Si anode** **ReaxFF** application paper on **chemomechanical lithiation**. The **PCCP** article is frequently cited alongside other **Si** **nanostructure** **lithiation** simulations in the corpus when discussing **stress**-retarded **reaction** fronts and **amorphization** at **sharp** interfaces.

## Citations and evidence anchors

DOI `10.1039/C4CP05198J`.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
