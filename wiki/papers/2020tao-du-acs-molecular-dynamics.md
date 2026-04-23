---
id: paper:2020tao-du-acs-molecular-dynamics
type: paper
title: "Molecular Dynamics Simulation of the Precipitation of Calcium Silicate Hydrate Nanostructures under Two-Dimensional Confinement by TiO2: Implications for Advanced Concretes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - material:cement-mineral
  - material:oxide
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:silica-silicate
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acsanm.9b02203"
year: 2020
authors:
  - "Tao Du"
  - "Hui Li"
  - "Mathieu Bauchy"
venue: "ACS Appl. Nano Mater. 2020, 3, 2176–2184"
pdf_sha256: "fdb50fb6cb7969415c5c0aa6d97994e015e218c96c9ab0d9bafeb65bfe7e39cb"
pdf_path: "papers/ReaxFF_others/du-et-al-2020-molecular-dynamics-simulation-of-the-precipitation-of-calcium-silicate-hydrate-nanostructures-under-two-1.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020tao-du-acs-molecular-dynamics -->

**Reactive MD (ReaxFF)** simulations follow **precipitation** of **calcium silicate hydrate (C–S–H)** gel inside **TiO₂ nanochannels** of varying **spacing**. **TiO₂** surfaces with **oxygen dangling bonds** adsorb **Ca** and **Si** differently, driving **nanoscale segregation** into **Ca-rich** and **Si-rich** regions; **surface hydroxylation** promotes **silicate polymerization**, with up to **~15% Q₄** silicon environments in the most polymerized confined C–S–H.

## Summary

Nanoengineered concrete benefits from understanding **C–S–H–nanomaterial** interactions. The study shows **faster polymerization** and **higher final polymerization** for C–S–H formed under **TiO₂ nanoconfinement**, **nanosegregated chemistry** at the hydroxylated interface, and **more compact** gel **morphology** inferred from **water mobility** patterns—linking confinement and surface chemistry to **nanostructure**.

## Methods

**1 — MD application.** **LAMMPS** with the **Kim et al. ReaxFF SiO** + **CHON** merger described in **Section 2**; **0.25 fs** time step. **TiO₂ rutile (110)** slit pores at **D19, D38, D59** (**~19.35, 37.93, 59.27 Å**); **constant** Si and Ca content across spacings; **PACKMOL** initial pack; **NVT** **300 K** relaxation, then **accelerated aging** at **1500 K** for **1 ns** (prior cited protocol) for C–S–H condensation; **NVT** at **300 K** for **MSD** of **H**; **Qₙ** tracking. **N/A** — NPT (constant-volume NVT in protocol as stated). **N/A** — metadynamics / replica exchange. **N/A** — external electric field. **Thermostat** details in **Section 2–3**; **N/A** here if a label is not repeated in the wiki—confirm the PDF. **PBC** in-plane for the confined slab geometry as in the article. **N/A** — NPT *pressure* control: **NVT**-based protocol.

**2 — Force-field training.** **N/A** — the article **uses** **Kim et al.** / merged **Reaxff**; no in-manuscript full refit is claimed.

**3 — Static QM.** **N/A** — the paper is MD-centric with literature-based FF.

**4 — Review or non-simulation.** **N/A** — research article with reactive MD.

## Findings

**Outcomes and mechanisms.** **Confinement** in **D19/D38/D59** spacings speeds **C–S–H** **polymerization** relative to the comparison cases in the paper, with up to **~15% Q₄** in the most polymerized confined region. **Hydroxylated TiO₂** drives **Ca** vs **Si** **adsorption** differences and **nanosegregation**; **Q₃**/**Q₄** concentrate in **Si-rich** areas. **Water** **MSD** supports a **more compact** **nanostructure** in confined films.

**Comparisons and sensitivity.** Channel **spacing** and **interface** chemistry (hydroxylation) are the main levers. **N/A** — new experimental data in the excerpt for this short summary; the full article has literature comparison.

**Authored limitations.** Extrapolation to long **cure** times and high-pH **electrolytes** is limited—see **## Limitations** on the page.

**Corpus honesty.** Full **supercell** **counts** and time windows are in the **PDF** / **Section 2**.

## Limitations

**ReaxFF** uncertainty for **high-pH** cement chemistry and **long curing** times means **laboratory** hydration experiments remain necessary for **engineering** property prediction beyond the nanoscale condensation stages summarized here.

## Relevance to group

Standard **ReaxFF** application space for **oxide–silicate** **interfacial** reactivity in **construction materials**.

## Citations and evidence anchors

- DOI: `10.1021/acsanm.9b02203`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
