---
id: paper:2021urquiza-x-atomistic-insights
type: paper
title: "Atomistic Insights on the Full Operation Cycle of a HfO2-Based Resistive Random Access Memory Cell from Molecular Dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:ereaxff
  - method:classical-md
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:charge-equilibration
  - keyword:reactive-md
  - keyword:oxide-surface
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.1c01466"
year: 2021
authors:
  - "M. Laura Urquiza"
  - "Md Mahbubul Islam"
  - "Adri C. T. van Duin"
  - "Xavier Cartoixà"
  - "Alejandro Strachan"
venue: "ACS Nano"
pdf_sha256: "845df43121d0f06f139beafb0c4adb8ad18ed4dc63b845023a0a746bc8b2e83b"
pdf_path: "papers/Urquiza_ACS_Nano_HfO2_RRAM_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2021urquiza-x-atomistic-insights -->

## Summary

Valence-change **RRAM** in **HfO₂** involves forming, reset, and set transitions mediated by oxygen redistribution and local stoichiometry changes. The work reports large-scale **molecular dynamics** with an **extended charge equilibration treatment (EChemDID)** so external electric fields and electrochemical driving forces enter the reactive simulation consistently with redox and ion migration. Trajectories resolve oxygen motion, Hf coordination changes, and conductive filament (CF) evolution during full device operation cycles. **ACS Nano** framing emphasizes **industry-relevant** **oxide** **RRAM** stacks where **forming** voltages and **thermal** budgets couple to **oxygen** **substoichiometry** in **HfO\(_{2-x}\)**.

## Methods

**1 — MD application (ReaxFF + EChemDID, LAMMPS).** **Metal–HfO₂–metal** **stacks** with a **Hf** **active** **electrode** (oxygen-scavenging) are built with ~10⁴ **atoms** and **3D** **PBC** in **LAMMPS**; after **relaxation** a **substoichiometric** **interfacial** **HfO\(_{2-x}\)** layer forms as in the **device** model. **NVT** **molecular dynamics** (see **thermostat** and **timestep** in **fs** in *ACS Nano*) run **ps**–**ns** **equilibration** and **cycled** **forming** / **reset** / **set** **stages** at defined **temperature** (**K**). **EChemDID** maps **biases** to **atomic** **electrochemical** **potentials** so **O** **migration** follows **redox**-consistent **forces**; **static** and **ramped** **electric** **field** or **voltage** **protocols** are those in the paper (not a separate **kMC** **layer**). **Barostat** and **N/A** **independent** **isotropic** **pressure** **control** in the excerpted **NVT** **filament** **protocol**; **N/A —** **metadynamics** for the standard **operating** **trajectories**.

**2 — Force-field training. N/A** — the article **applies** a **ReaxFF** + **EChemDID** **coupling** to **HfO₂** **RRAM**; it is not primarily a new **ReaxFF** **fit** report.

**3 — Experiments. N/A** — **computation** with **literature** **context** for **device** **metrics**.
## Findings

**Forming:** The conductive filament forms via **net oxygen migration toward the active electrode** (oxygen exchange/cascade displacement toward the AE), rather than simple aggregation of pre-existing vacancies alone. **Reset:** Filament breakup is dominated by **lateral** vacancy/oxygen motion rather than purely vertical transport along the filament axis. **Bipolar versus unipolar behavior:** Depending on temperature, reset proceeds via **bias-governed oxygen diffusion (bipolar/redox)** or **thermally driven diffusion (unipolar/thermochemical)**. **Set:** Similar to reset in involving lateral oxygen motion, driven by **field localization** near residual conductive paths. Strain from inhomogeneous oxygen removal generates **pseudo electric fields** associated with local electronic response (including nanoscale p–n–p features on the order of ~3 nm width reported in the abstract’s electronic discussion). The **galley** PDF path in front matter should be reconciled with any **publisher** **VOR** PDF before citing **figure** **panels** in **benchmarks**.

**Comparisons, sensitivity, corpus.** **Bias**, **temperature**, and **voltage** **cycling** set whether **O** **migration** is **reaction**-limited or **thermally** **activated**; all **V**/**I** **numbers** belong in the **VOR** **galley** reconciliation.

## Limitations

The corpus PDF is a **galley/proof** duplicate; quantitative kinetics and absolute voltages should be verified against the version-of-record PDF when available.

**Electrode** **roughness**, **grain** **boundaries**, and **electroforming** **variability** across **industrial** **RRAM** **arrays** are not captured in single **ideal** **slab** **cells**; use these **trajectories** to **qualitatively** **rank** **oxygen** **migration** **trends** rather than as **yield** **predictors** for **specific** **die** **maps**.

**Filament** **statistics** across **cycle** **counts** require **ensemble** **sampling** beyond the **single-stack** **movies** highlighted for **forming/reset/set** **qualitative** **mechanisms**.

## Reader notes (navigation)

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
