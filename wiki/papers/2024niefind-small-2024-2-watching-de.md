---
id: paper:2024niefind-small-2024-2-watching-de
type: paper
title: "Watching (De)Intercalation of 2D Metals in Epitaxial Graphene: Insight into the Role of Defects"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:reaxff
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:metallic-systems
  - keyword:lammps
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1002/smll.202306554"
year: 2024
authors:
  - "Niefind, F."
  - "Mao, Q."
  - "Nayir, N."
  - "Kowalik, M."
  - "Ahn, J.-J."
  - "Winchester, A. J."
  - "Dong, C."
  - "Maniyara, R. A."
  - "Robinson, J. A."
  - "van Duin, A. C. T."
  - "Pookpanratana, S."
venue: "Small"
pdf_sha256: "6db0b852eaa2eb1bccb463c70b2cec97519edd42a0782654c8c668ef162ffb78"
pdf_path: "papers/Niefind_Mao_Kowalik_Nayir_2D_Metals_graphene_Small_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024niefind-small-2024-2-watching-de -->

## Summary

Niefind and colleagues combine **photoemission electron microscopy (PEEM)** with **ReaxFF molecular dynamics** and **DFT** to compare **defect-gated (de)intercalation** of **two-dimensional Ag and Ga** sandwiched between **bilayer epitaxial graphene (EG)** and **SiC**. **PEEM** tracks **bright Ag-rich features** after **in situ annealing** (e.g., **436 K**), with **AFM**, **SEM-EDX**, and **XPS** supporting surface Ag. **Ag** shows **de-intercalation and re-intercalation** through roughly **circular** “windows,” with an estimated **intercalation front speed** near **0.5 nm s\(^{-1}\)** (±0.2 nm s\(^{-1}\)) from combined PEEM/AFM analysis. **Ga** **de-intercalates irreversibly** with **faster kinetics** and **non-circular** window shapes; **MD** shows **Ga pile-up** between graphene sheets before egress, and **DFT** indicates **stronger Ga–graphene binding**, consistent with observations.

## Methods

**Samples and intercalation context.** **2D metals** are prepared at the **EG/SiC** interface using **confinement heteroepitaxy (CHet)**-style processing: **oxygen plasma** generates **graphene defects** that act as **entry paths** for metal intercalation at elevated **temperature/pressure** conditions (as summarized in the introduction).

**PEEM and complementary microscopy.** **In situ PEEM** follows **intensity changes** associated with **Ag** redistribution during **annealing cycles** up to **~575 K** (regimes described around **405–494 K** in the discussion of ROI traces). **AFM** confirms **3D Ag particles** atop graphene with representative **heights ~15.2 nm ± 2.1 nm** and **steep sidewalls**; **SEM-EDX** and **laterally integrated XPS** corroborate **Ag** surface enrichment after annealing. Multiple **regions of interest** illustrate **zero-order-like** kinetics where **intercalation speed** is weakly dependent on **Ag structure size**, interpreted as **rate limitation by window/defect pathways**.

**1 — MD application (ReaxFF).** **Engine / code:** **ReaxFF** **molecular dynamics** in **LAMMPS** (as stated in the article; see *Computational Methods* for callouts and **PBC**). **System:** **2D** **Ag** and **Ga** at **EG/SiC**-type stacks; **full atom counts, timestep, ensemble, and run lengths** are in the **PDF** and are **not** itemized in this short wiki summary. **Thermostat** algorithm and time constant: **N/A** on *this* summary (see **VOR** **PDF**; **NVT** is the typical **ensemble** for the reported intercalation **T**). **In situ** **experimental** **T** (e.g. toward **~436 K** in discussed traces, stages up to **~575 K**) provide the thermal context; mapping **every** **MD** isotherm to experiment is in the **paper**. **Barostat / stress / E-field / replica or enhanced sampling:** **N/A** in the high-level description here — confirm whether the MD uses **NPT**-style cells or static **NVT**-like protocols in the **SI/PDF**; no external **electric field** in the protocol summary on this page.

**2 — Force-field training** — **N/A** as a new general **ReaxFF** **parameterization** report; the study **applies** a **ReaxFF** **parameter set** to **2D** **metal**/**graphene** chemistry (see *Computational Methods* for the exact **FF** line).

**3 — Static QM (DFT support).** **DFT** benchmarks **relative binding** of **Ga** vs **Ag** on **graphene** (and related **support** calculations); program, functional, and basis are given in the article. **4 — PEEM/AFM/EM** — in situ **PEEM** and complementary **AFM/SEM-EDX/XPS** (above) supply **observables** that the atomistic work interprets; **N/A** for a single MD “production run” line item list in this **summary**—use the **version-of-record** for tables.
## Findings

**Outcomes, comparisons, and levers.** **Ag** shows **semi-reversible** **(de)intercalation** through **defect** **windows** after **CHet**-style processing, with **PEEM/AFM**-inferred **front** speeds on the order of **0.5 nm s\(^{-1}\)** (±**0.2**). **Ga** **de-intercalates irreversibly**, with **faster** kinetics and **non-circular** windows; **ReaxFF MD** shows **Ga** **pile-up** between **graphene** sheets and **DFT** favors **stronger** **Ga–graphene** **binding** vs **Ag**—linking to **kinetic/thermodynamic** contrast. **Defect**-mediated paths and **metal**-dependent **graphene** **restructuring** are argued to **co-determine** kinetics. **ROIs** with **zero-order-like** kinetics (weak dependence of rate on **Ag** **structure** size) support **defect**/**window**-limited transport.

**Corpus honesty** — see **`## Limitations`** for model scope (**ReaxFF**/**projection** of **PEEM**).
## Limitations

**Surface spectroscopy/microscopy** integrates over **projection and surface sensitivity**; **MD** uses **ReaxFF approximations** to **quantum** energetics. **In situ** temperatures and **coverage** may not map one-to-one to all **device-relevant** environments.

## Relevance to group

**Adri C. T. van Duin** co-authors the **ReaxFF** modeling thread alongside **NIST/PSU** experimental imaging—an integrated **2D metal / graphene defect** case study for **reactive MD** validation against **PEEM**.

## Citations and evidence anchors

- PEEM/AFM kinetics and velocity estimate: **Results and discussion**, Fig. 1–2 region (*Small* **20**, 2306554 (2024)); DOI above.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
