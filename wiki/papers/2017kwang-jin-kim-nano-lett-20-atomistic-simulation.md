---
id: paper:2017kwang-jin-kim-nano-lett-20-atomistic-simulation
type: paper
title: "Atomistic Simulation Derived Insight on the Irreversible Structural Changes of Si Electrode during Fast and Slow Delithiation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:batteries-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.7b01389"
year: 2017
authors:
  - "Kwang Jin Kim"
  - "James Wortman"
  - "Sung-Yup Kim"
  - "Yue Qi"
venue: "Nano Lett. 2017, 17, 4330–4338"
pdf_sha256: "70568045d7df9afd3f6c14dd0f2284d0bd7f9333ddfca5bfc8c2f213e69525a4"
pdf_path: "papers/ReaxFF_others/Kim_Qi_LiSi_acs.nanolett_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017kwang-jin-kim-nano-lett-20-atomistic-simulation -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **Nano Letters** article identified by **`doi`**, **`title`**, and **`pdf_path`**, using the **journal PDF** (`papers/ReaxFF_others/Kim_Qi_LiSi_acs.nanolett_2018.pdf`) plus the short local extract for abstract-level context.

## Summary

**Reactive molecular dynamics** with a **continuous delithiation** scheme—controlling **electrochemical potential gradient** and **delithiation rate**—is applied to an **aluminum-oxide-coated** **silicon** **thin-film** model to compare **fast** vs **slow** **Li** removal. **Fast** delithiation produces a **dense Si-rich network** near the **surface** and **nanoscale porosity** inside **amorphous Li\(_x\)Si**, ending near **a-Li\(_{1.2}\)Si** with about **141%** **volume dilation** and **substantial residual Li**. **Slow** delithiation allows **near-equilibrium** contraction to a **nearly Li-free** **a-Li\(_{0.2}\)Si**-like state with about **44%** dilation and **no persistent inner void**. Even when **little Li** remains, the **delithiated glass** can sit at **higher volume** (**lower density**) than an **equilibrated** structure at the **same composition**; the paper attributes this **excess volume** to **loss of directly bonded Si–Si pairs**, which **accelerates** **subsequent relithiation**. **Qualitative** **operating guidelines** (e.g., **delithiation rate** and **depth of charge** to limit **trapped Li** and **coating delamination**) are discussed in light of the **atomistic** **degradation** picture.

## Methods

**1 — MD application (continuous delithiation with ReaxFF in LAMMPS).** **ReaxFF-based MD** is run in **LAMMPS** using the authors’ **continuous delithiation** algorithm on an **alumina-coated a-Li\(_x\)Si thin film** model (**Figure 1a**). **Initial lithiated glass** (**a-Li\(_{3.75}\)Si**) is prepared by **melting at 2500 K** and **quenching to 298 K** under **NPT**; **lithiated a-Al\(_2\)O\(_3\)** (**a-Li\(_8\)Al\(_2\)O\(_3\)**) coatings are built and **attached on both sides**, with reported **298 K densities ~1.12 g cm⁻³** (**a-Li\(_{3.75}\)Si**) and **~1.68 g cm⁻³** (**a-Li\(_8\)Al\(_2\)O\(_3\)**) matching experiments as cited. **Boundary / periodicity:** **3D periodic** **slab/sandwich** supercell for the **a-Li\(_x\)Si** film with **lithiated a-Al\(_2\)O\(_3\)** coatings on both sides (normal-direction **Li extraction** protocol described in the article). **Li removal** occurs **only outside a buffer zone** defined by the **10% Al-atom region** nearest each **interface**, so the **a-Li\(_x\)Si surface** and **Li\(_x\)Si/coating interface** are not artificially interrupted. Each **delithiation step** removes a **fixed batch ΔN = 100 Li atoms** (randomly chosen outside the buffer), followed by **NVT relaxation** at **900 K** using the **Nosé–Hoover thermostat** and **velocity Verlet** integration with **Δt = 0.1 fs**. **Delithiation rate** is controlled by the **relaxation time Δt** between removals (**ΔN/Δt**), implementing **“fast”** versus **“slow”** stripping relative to an **estimated Li diffusion equilibration time** discussed in the article (they relate **Δt** to a **1D diffusion** estimate using **D ≈ 2.98×10⁻⁶ cm² s⁻¹** for **a-Li\(_{3.75}\)Si at 900 K** from their prior MD). **N/A — barostat during production delithiation cycles**: the quoted relaxation stage is **NVT** at **900 K**; **NPT** appears in the **preparation** melting/quench segment, not as the stated ensemble for each post-removal relaxation block. **N/A — external electric field**: not part of the described MD control scheme.

**2 — Force-field training.** **N/A — new ReaxFF fit in this Letter**: the study uses a **published Li–Si–O ReaxFF** parameterization as cited in the article/SI (this page does not reproduce parameter file lineage).

**3 — Static QM / DFT.** **N/A — on-the-fly DFT**: the Introduction contrasts prior **DFT-based stripping** schemes for **size limits**; the **production** tool here is **ReaxFF MD**.

**4 — Review / non-simulation framing.** **N/A**: primary **Nano Lett.** application note.

## Findings

**Outcomes and mechanisms.** **Fast delithiation** leaves a **dense Si-rich network** near the **surface** and **nanoporosity** inside **a-Li\(_x\)Si**, with **~141% volume dilation** and **substantial trapped Li** (**~a-Li\(_{1.2}\)Si** end state in their labeling). **Slow delithiation** allows **near-equilibrium** contraction to a **nearly Li-free** **~a-Li\(_{0.2}\)Si**-like state, **~44% dilation**, and **no persistent inner void**. Even without trapped Li, **delithiated glass** can occupy **higher volume (lower density)** than an **equilibrated** structure at the **same composition**; the authors tie this **excess volume** to **loss of directly bonded Si–Si pairs**, which **accelerates subsequent relithiation** in their trajectories.

**Comparisons.** The article connects **simulated irreversible dilation**, **pores**, and **trapped Li** to **experimental** observations on **nanostructured Si** volumes and **NMR evidence** for **trapped Li** (cited in the Introduction/Discussion).

**Sensitivity and design levers.** **Delithiation rate** (**ΔN/Δt**), **depth of charge** (how much Li remains extractable from the reservoir), and the **interface/buffer protocol** are the main computational knobs tied to **void formation**, **coating delamination**, and **residual Li**.

**Limitations and outlook (as authored).** **SEI growth** and related **capacity fade** channels are **explicitly out of scope**; simulated **current densities** are **enormously higher** than laboratory cells by design, analogous to high **strain-rate** MD deformation studies.

**Corpus / PDF honesty.** Protocol details above are taken from the **ingested ACS PDF** text; if your local copy differs, reconcile against the **DOI** version.


## Limitations

- **ReaxFF** **accuracy** depends on **training** **chemistry** and **environment**; **quantitative** **voltage**/**rate** **mapping** to **experiment** requires **careful** **interpretation**.
- **SEI**, **electronic** **conductivity**, and **long-time** **cycle** **statistics** are **not** the **primary** **modeling** **targets** here.

## Relevance to group

**Methodological** reference for **controlled** **delithiation** in **large-scale** **reactive** **MD** of **Si** **anodes**; **not** a **van Duin**-group **publication** (**Michigan State University** authors).

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.nanolett.7b01389](https://doi.org/10.1021/acs.nanolett.7b01389)

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
