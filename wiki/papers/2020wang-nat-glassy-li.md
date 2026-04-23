---
id: paper:2020wang-nat-glassy-li
type: paper
title: "Glassy Li metal anode for high-performance rechargeable Li batteries"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:li-metal-anode
  - method:reactive-md-generic
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:nvt-simulation
  - keyword:reactive-md
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41563-020-0729-1"
year: 2020
authors:
  - "Xuefeng Wang"
  - "Gorakh Pawar"
venue: "Nature Materials (2020)"
pdf_sha256: "78ce41f0a0b65c703780a667f6ef47ec3f21c283aff84427e52dbd5d7e77723c"
pdf_path: "papers/ReaxFF_others/Wang_Pawar_NatureMat_2020_GlassyLi.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020wang-nat-glassy-li -->

**Cryogenic (scanning) transmission electron microscopy** resolves **electrodeposited lithium (EDLi)** from early **nucleation** through **growth**, revealing **disordered (“glassy”)** Li at short times / selected conditions and a **disorder–order** transition as **deposition time** and **current density** evolve. **Reactive molecular dynamics (r-MD)** simulations interpret **atomic-scale** kinetics and **critical cluster sizes** for **ordering**.

## Summary

The paper combines **cryo-EM**/**cryo-TEM** on **EDLi** across **0.1–2.5 mA cm⁻²** and **5–20** **min** with **LAMMPS** **r-MD** using a **Li**-trained **Reaxff** (authors’ “r-MD” label) to link **nucleation** to **spontaneous** **crystallization** past a **~5 nm** scale. Initially many deposits look **amorphous/glassy**; longer **t** and higher **j** yield **bcc**-like **order**; **r-MD** **predicts** a **critical** size for **ordering** in line with **HRTEM**-inferred **domains** ~**5 ± 3** **nm**.

## Methods

**1 — MD application (r-MD, LAMMPS).** **Li**-parametrized **Reaxff** as implemented; **MAPS** (Scienomics **v4.0.1**) for setup. **Nose-Hoover thermostat**, **NVT**; **~0.0534 g cm⁻³** **Li** **density**; default **0.5 fs** time step (**0.1** and **0.25** **fs** in tests per **SI**). **Staged** protocol: **ramp to 500 K** (**0.1 ns**), **quench to 300 K** (**0.2 ns**), **hold 300 K** (**5 ns** default) for **nucleation** in **500–1500**-atom **ensembles**. **N/A** — NPT (constant-**volume** NVT in protocol). **N/A** — external **electric** **field**; **N/A** — metadynamics. **PBC** in the small **Li** **droplet**/bulk cells as in **SI**. **N/A** — *hydrostatic* **pressure** control: **NVT** without **NPT** **stated** for the **r-MD** (confirm **SI** for any **stress** **protocol**).

**2 — Experiment (cryo-TEM/EM).** **EDLi** on **current** **collectors**; **0.1–2.5 mA cm⁻²**; **5–20 min**; **FFT**/**HRTEM**; **cell** and **electrolyte** details in the article/ **SI**. **N/A** — in situ MD of full **electrolyte** at **ab initio** cost.

**3 — Force-field training.** **N/A** — the article **use**s a **published** **Li** **r-MD** model; not refit in the paper text summarized here.

**4 — Static QM.** **N/A** — not the paper’s main contribution.

**5 — Review or non-simulation.** **N/A** — research article (experiment + MD).

## Findings

**Outcomes and mechanisms.** **Glassy** / **amorphous**-appearing **EDLi** (weak **bcc** **FFT** **spots**) can occur at **short** **t** / **moderate** **j**; a **DOPT** toward **bcc** **increases** with **t** and **j**. **Crystalline** **patches** reach **~5 ± 3** **nm** in an **early** **ordering** **stage**; **r-MD** supports **spontaneous** **ordering** **beyond** a **~5** **nm**-scale **cluster**—**aligned** with the **TEM** narrative. By **~20** **min**, **large** **>50** **nm** **bcc** **domains** and strong **diffraction** appear. **Reversibility** in **cycling** **tests** is **better** for more **“glassy”** regimes in the data shown.

**Comparisons and sensitivity.** **TEM**/ **r-MD** **juxtaposed**; **j** and **t** are **swept** as **levers**; **temperature** **ramps** in **r-MD** stages.

**Authored limitations.** Ex situ **cryo** can miss some **side** **reactions**; **r-MD** **Reaxff** is **not** a **universal** **potentiostatic** model.

**Corpus honesty.** **Quantitative** **TEM** and **r-MD** **numbers** live in the **VOR** `pdf_path`.

## Limitations

**r-MD** details (potential, constraints) must be read from the **paper**; **cryo** imaging may omit **electrolyte** side reactions not captured in **ex situ** snapshots.

## Relevance to group

Uses **reactive MD** (as labeled by the authors) alongside **high-resolution** **electron microscopy** for **Li** **metal** **morphogenesis**—adjacent to **ReaxFF** battery-interface studies in the broader corpus.

## Citations and evidence anchors

- DOI: `10.1038/s41563-020-0729-1`

## Related topics

- [[batteries-interfaces-reaxff]]
