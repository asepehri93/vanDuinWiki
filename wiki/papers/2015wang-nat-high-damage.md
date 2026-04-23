---
id: paper:2015wang-nat-high-damage
type: paper
title: "High damage tolerance of electrochemically lithiated silicon"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:mechanics-tribology
  - method:classical-md
  - method:continuum-or-mesoscale
  - material:widegap-semiconductor
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:metallic-systems
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/ncomms9417"
year: 2015
authors:
  - "Xueju Wang"
  - "Feifei Fan"
  - "Jiangwei Wang"
  - "Haoran Wang"
  - "Siyu Tao"
  - "Avery Yang"
  - "Yang Liu"
  - "Huck Beng Chew"
  - "Scott X. Mao"
  - "Ting Zhu"
  - "Shuman Xia"
venue: "Nature Communications"
pdf_sha256: "5d72e533078fd2e1d03113fbb0e5728a88cbcdd91588c8475867afd24af7b65e"
pdf_path: "papers/ReaxFF_others/Wang_NatureComm_2015_LiS.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2015wang-nat-high-damage -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **Nature Communications** article identified by `doi` and `pdf_path`. The study is **integrated experiment + continuum + MD**, not a **ReaxFF** parameterization paper.

## Summary

**In situ transmission electron microscopy (TEM)** bending tests on **partially lithiated silicon nanowires** show **brittle fracture** in the **crystalline Si core** versus **ductile** deformation in the **amorphous Li-rich shell**, establishing a **core–shell** **mechanics** contrast during **electrochemical** **Li** insertion. **Nanoindentation** on **lithiated Si thin films** maps a **brittle-to-ductile** transition as the **Li:Si** ratio exceeds **~1.5**, linking **composition** to **fracture toughness** at the **micrometer** scale. **Continuum finite-element (FE)** modeling and **atomistic molecular dynamics (MD)** interpret the trends via **bonding** changes and **lithiation-induced toughening** in the **amorphous** phase. The study is **experiment-forward** with **simulation** support rather than a **ReaxFF** **parameterization** paper.

## Methods

**Experiments and continuum:** Partially lithiated **Si nanowires** undergo **in situ TEM** bending/compression with the **Li/Li₂O**-based electrochemical cell and applied bias (e.g. **~−2 V** lithiation conditions in the Results narrative, `papers/ReaxFF_others/Wang_NatureComm_2015_LiS.pdf`). **Nanoindentation** on **a-Si** films on **Ti** targets controlled **Li:Si** ratios; **Michelson interferometry** and **Stoney’s equation** give **biaxial stress** during lithiation/delithiation (Methods, Fig. 2). A **continuum finite-element** elasticity–plasticity model reproduces the **core–shell** bend and reports very large tensile strains in the lithiated shell (Fig. 1e; Supplementary discussion referenced in the article).

**MD application (pre-cracked a-Li\(_x\)Si):** **LAMMPS** with a literature **ReaxFF** parametrization for **Li–Si** (Methods, “Molecular dynamics simulations…”). **a-Li\(_x\)Si** glasses are built by random **Li** insertion into **c-Si** and **melt–quench** (**~2 × 10¹² K s⁻¹**), boxes about **16 × 10 × 1.5 nm** with **~3 nm** pre-cracks; **3D PBC** with fixed out-of-plane thickness (**plane strain**). The protocol uses **5 K** athermal tensile loading with **1 fs** timestep at **5 × 10⁸ s⁻¹** engineering strain rate until failure—interpreted as **NVE**-style energy-conserving dynamics; the article paragraph stresses **5 K** rather than thermostat nomenclature (confirm exact ensemble wording in the PDF/SI if needed). **Duration** is “until failure” under the imposed **strain rate** rather than a fixed **ns** cap (see article for trajectory length). No barostat, controlled hydrostatic pressure, field in MD, or enhanced sampling is reported.

**Force-field training:** **N/A —** published **Li–Si ReaxFF** is applied, not refit here.

**Static QM / DFT:** **N/A —** not the dominant computational modality relative to experiment, FE, and ReaxFF MD.

## Findings

**In situ TEM** shows a **brittle crystalline Si core** versus a **ductile amorphous Li-rich shell** after lithiation, with a coherent **surface oxide** that strains with the shell (Fig. 1, same PDF). **FE** reports **~47%** tensile axial strain and **~45%** lateral thinning in **a-Li\(_{3.75}\)Si** near the kink, qualitatively matching the morphology (Fig. 1d–e). **Nanoindentation** shows **fracture toughness** of **a-Li\(_x\)Si** rising with **Li**, with a **brittle-to-ductile** transition near **Li:Si ≳ 1.5** (Results). **ReaxFF MD** gives **brittle** crack advance in **Li-lean** glasses and **ductile blunting** in **Li-rich** glasses, paralleling that trend (Discussion). **Li concentration** shifts **covalent Si–Si** versus **Li-involved** bonding character near the crack tip in the MD interpretation. The Discussion contrasts ideal simulated glasses with real nanowires, strain-rate gaps, and related caveats. This publication is **not** van Duin-group work; it is a **benchmark** adjacent to battery-mechanics themes.

## Limitations

**Nanowire** and **thin-film** **mechanics** may differ from **composite** **electrodes** in **full cells** with **binder**, **porosity**, and **SEI**. **MD** **potentials** for **Li–Si** may not capture **electrolyte** chemistry or **long-time** **creep** relevant to **calendar** aging.

## Relevance to group

Benchmark-style **battery mechanics** paper adjacent to **group** interests in **electrode** **failure**, though not **ReaxFF**-centric.

## Citations and evidence anchors

- **DOI:** `10.1038/ncomms9417` — `papers/ReaxFF_others/Wang_NatureComm_2015_LiS.pdf`.

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]

## Reader notes (navigation)

This **Nature Communications** study is **not** a **ReaxFF** paper; link it to **group** **Si** **lithiation** **ReaxFF** pages for **complementary** **atomistic** versus **in situ** **mechanics** perspectives on **Li:Si**-dependent **ductility**. **Nanoindentation** **geometry** and **film** **preparation** details belong to the **Nature Communications** methods sections referenced by this summary.
