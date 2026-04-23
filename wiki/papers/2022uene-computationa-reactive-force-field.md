---
id: paper:2022uene-computationa-reactive-force-field
type: paper
title: "Reactive force-field molecular dynamics simulation for the surface reaction of SiH x ( x  = 2–4) species on Si(1 0 0)-(2 × 1):H surfaces in chemical vapor deposition processes"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - task:application
  - scale:atomistic
  - material:widegap-semiconductor
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2022.111193"
year: 2022
authors:
  - "Naoya Uene"
  - "Takuya Mabuchi"
  - "Masaru Zaitsu"
  - "Shigeo Yasuhara"
  - "Takashi Tokumasu"
venue: "Computational Materials Science, 204 (2022) 111193"
pdf_sha256: "aa3623229e83410153e3113a5aed0b7644ad4363a527efccf9b931997341f9cd"
pdf_path: "papers/ReaxFF_others/Uene_SiH_Si_CompMatSci_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022uene-computationa-reactive-force-field -->

## Summary

Reactive molecular dynamics with a **ReaxFF**-style bond-order potential is used to study **plasma-enhanced CVD–relevant** surface chemistry: **SiH<sub>x</sub> (x = 2–4)** impinging on a **hydrogen-terminated Si(100)-(2×1)** surface. The work targets **PECVD** contexts where gas-phase radicals reach the substrate and participate in **reflection, desorption, chemisorption, and physisorption**. An **existing parameter set is adjusted** so that **gas-phase dissociation energies** of the SiH<sub>x</sub> species are better reproduced before surface collision studies. The authors motivate the work by the need to treat **radical–surface** outcomes as **reactive** events rather than **prescribed** sticking coefficients in **reactor-scale** models.

## Methods

### Force-field training and targets (A)

- **Framework:** **ReaxFF**-type **bond-order** reactive MD for **Si/H** chemistry relevant to **SiH\(_x\)** (**x = 2–4**) interacting with **hydrogen-terminated silicon**.
- **Adjustment described in the article:** an **existing** parameter set is **refit** so **gas-phase dissociation energies** of **SiH\(_x\)** species match reference **energetics** more closely before **surface** collision studies (see primary text for training targets and weighting).
- **QM reference level:** follow the article’s statement of **reference energies** or **benchmarks** used to judge SiH\(_x\) dissociation—**not restated** here.

### Molecular dynamics and collision protocol (B)

- **Engine / code:** Reactive MD consistent with **LAMMPS**-style ReaxFF integration (as stated in *Computational Materials Science*; confirm **package** and **version** in the PDF).
- **Surface:** **Si(100)-(2×1):H**; **substrate temperature** and **adsorbed H coverage** are swept as control variables.
- **Impacts:** **SiH\(_x\)** radicals strike the surface **one at a time** (sequential impingement); each event is binned as **reflection**, **desorption**, **chemisorption**, or **physisorption**.
- **Reproducibility (numerics not duplicated here):** **Ensemble** (**NVT** with **surface** **thermostat** where used), **timestep**, **3D** **PBC** **slab** dimensions, **QEq** or fixed-charge **electrostatics**, **Coulomb** **cutoff**, and **per-impact** and **cumulative** **trajectory** length for **sequential** **impingement** of **SiH\(_x\)** are in the *Comput. Mater. Sci.* article; confirm there before reruns.

### MD application (CVD, single-impact)

**Engine / code:** **ReaxFF**-based **RMD** (typically **LAMMPS**). **Surface / composition:** **Si(100)-(2×1):H**; incident **SiH\(_2\)–SiH\(_4\)** **one** radical per **impact** with outcome bins (**reflection**/**desorption**/**chemisorption**/**physisorption**). **Substrate** **temperature** and **H** **coverage** are **control** variables. **N/A** — no **NPT** **barostat** or **hydrostatic** **pressure** run called out in this summary (constant-volume or fixed **lattice** patterns per article). **N/A** — no **shock** piston or static **interfacial electric field**; **N/A** — no **replica** or **metadynamics** beyond **RMD** unless the **SI** says otherwise. **Equilibration** and **per-impact**/**aggregate** **production** **duration (ps/ns)**: **N/A** — not restated in this **wiki** summary; see **VOR**/**SI**. **Coulomb** and **QEq** **details** per **primary** text.

## Findings

### Role of temperature

Higher **substrate temperature** promotes **bond breaking** in incident **SiH\(_x\)** and increases **desorption** of adsorbed species from the surface, shifting the balance among outcome channels in the authors’ classification.

### Role of hydrogen coverage

**Adsorbed H** **passivates** **dangling bonds**, **blocking** chemisorption sites, while **thermal motion** of surface **H** facilitates **reflection** and **desorption** of incoming radicals.

### Multiscale utility

**Outcome statistics** from **single-impact** trajectories supply **discrete** sticking/reflection weights usable as **boundary conditions** in **reactor-scale** models, with the caveat that **sequential** impacts omit **concurrent** **flux** and **coverage** transients.

### Outlook (paper)

The authors suggest extending the same **reactive** framework to **SiC**, **SiGe**, and related **CVD** chemistries.

## Limitations

Parameterization is focused on **gas-phase dissociation energetics** for selected species; **transferability** to other feedstocks or full reactor-scale behavior is not established in the excerpted material. **One-radical-at-a-time** **impingement** omits **flux** **overlap** and **surface** **coverage** transients present in **high-rate** **CVD**, so **outcome** statistics should be mapped to **continuum** **boundary** **conditions** with care. **Software** **timestep** and **thermostat** **choices** in the **full** **PDF** govern **energy** **drift** in **long** **production** **segments**; mirror those **settings** when **reproducing** **sticking** **distributions**.

## Relevance to group

Illustrates **ReaxFF surface chemistry** in **semiconductor CVD**-like settings (Si/H), adjacent to broader **reactive MD** practice in the corpus.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2022.111193](https://doi.org/10.1016/j.commatsci.2022.111193)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
