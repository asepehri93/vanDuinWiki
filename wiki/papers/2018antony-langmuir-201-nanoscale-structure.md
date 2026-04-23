---
id: paper:2018antony-langmuir-201-nanoscale-structure
type: paper
title: "Nanoscale structure and dynamics of water on Pt and Cu surfaces from MD simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:classical-ff-specialized
  - method:classical-md
  - material:metal-surface
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:lammps
  - keyword:water-interfaces
  - keyword:metallic-systems
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.8b02315"
year: 2018
authors:
  - "Andrew C. Antony"
  - "Tao Liang"
  - "Susan B. Sinnott"
venue: "Langmuir"
pdf_sha256: "a7a560c366597b0fd3a59756a0cef03b09d293b29a9006802b048134d40b7a30"
pdf_path: "papers/Others/2018_Antony_Langmuir.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018antony-langmuir-201-nanoscale-structure -->

## Summary

**Classical molecular dynamics** with the **third-generation charge-optimized many-body (COMB3)** **Pt/O/H** potential reproduces **DFT-supported** **sub-monolayer** water motifs on **Pt(111)**, including **√37** and **√39** reconstructions with **“575757” di-interstitial** defects. For **liquid** films, the **first wetting layer** shows a **buckled bilayer-like distribution** from the balance of **metal–water** adsorption and **H-bonding**. **Molecular kinetic spreading** analysis shows **water nanodroplets** spread **an order of magnitude slower** on large **Pt** than on **close-packed Cu** due to **interfacial molecular packing** differences. The study is positioned as a **fixed-bond** alternative to **reactive** treatments when the scientific question is **wetting morphology** and **kinetic spreading** rather than **dissociative** surface chemistry.

## Methods

### A — Interatomic potential (classical, fixed reactive chemistry)

- **COMB3** **third-generation charge-optimized many-body** potential for **Pt/O/H**; **Cu**-related wetting comparisons use the **COMB** treatment described in the article (not **ReaxFF**).

### B — Molecular dynamics (LAMMPS)

- **Engine:** **LAMMPS** with **`field.comb3.PtOH`** parameter file referenced in the paper.
- **Systems:** **Pt(111)** **sub-monolayer** ice/water motifs (**0.67 ML** hexagonal, **√37**/**√39** reconstructions, **575757** defects) and **multilayer** liquid films; **nanodroplet** **spreading** on large **Pt** vs **Cu** surfaces.
- **System size & composition:** **Metal–water** **slab** supercells containing **hundreds to thousands of atoms** (exact counts in *Langmuir* **Methods**).
- **Boundaries / periodicity:** **In-plane periodic boundary conditions** with finite **slab** thickness/vacuum as standard for surface **MD**.
- **Ensemble:** **NVT** **canonical** trajectories for wetting and spreading benchmarks (per **paper_keywords**).
- **Timestep:** **Femtosecond** integration **timestep** (exact **fs** in **Methods**).
- **Duration:** **Equilibration** and **production** run lengths in **ps**/**ns** tabulated in the article.
- **Thermostat:** **Nose–Hoover** or **Langevin** thermostat parameters as listed for each stage.
- **Barostat:** **N/A — hydrostatic barostat** not used for the cited **constant-volume** surface **NVT** cells unless **SI** documents **NPT** film thickness relaxation—verify in **PDF**.
- **Temperature:** **K** setpoints for sub-monolayer vs liquid-film studies.
- **Pressure:** **N/A — isotropic pressure** targets not applied for the **NVT** **slab** setups described at abstract level.

### C — Pure DFT (validation literature)

- **DFT** references from the literature benchmark **COMB3** **sub-monolayer** structures on **Pt(111)**.

### D — Analysis

- **Molecular kinetic theory** treatment of **spreading rates** tied to **interfacial** **density** profiles and **first-layer buckling** motifs discussed in **Results**.


## Findings

- COMB3 captures **experimentally reported** low-coverage ice/water motifs on Pt(111), including √37/√39 networks and **575757** defects, consistent with DFT literature cited in the paper.
- The first liquid layer next to Pt(111) exhibits a **characteristic two-layer buckling** pattern tied to adsorption vs hydrogen-bond competition.
- **Spreading rates** from **molecular kinetic theory** differ by about **one order of magnitude** between Pt and Cu for the large-surface droplet setups described, traced to **interfacial water density profiles**.
- The discussion ties **first-layer buckling** and **√37/√39** motifs to **kinetic** spreading: **interfacial packing** differences between **Pt** and **Cu** propagate into **order-of-magnitude** changes in **predicted spreading rates** for large droplets.


## Limitations

**Not ReaxFF:** chemistry is fixed-bond COMB3; dissociative chemistry is outside the model’s scope. van Duin appears via the Penn State author list as collaboration context, not as ReaxFF development here. **COMB3** **Pt/O/H** parameters should not be mixed ad hoc with **ReaxFF** **water** models in the same **simulation** cell without a defined **multiscale** **handshake**, because the **electrostatic** and **bonded** **partitioning** differ fundamentally. **Spreading** **comparisons** between **Pt** and **Cu** assume **comparable** **droplet** **sizes** and **thermostat** **protocols**; confirm **boundary** **conditions** when reusing **published** **kinetic** **coefficients**.

## Relevance to group

Penn State **Sinnott/Liang**-adjacent classical potential work on **metal–water** interfaces, relevant to benchmarking and multiscale contexts around reactive methods.

## Citations and evidence anchors

- DOI: `10.1021/acs.langmuir.8b02315`.

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
