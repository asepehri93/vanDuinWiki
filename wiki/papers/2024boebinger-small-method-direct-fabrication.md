---
id: paper:2024boebinger-small-method-direct-fabrication
type: paper
title: "Direct fabrication of atomically defined pores in MXenes using feedback-driven STEM"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:methods-software
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:method-development
  - keyword:validation-experiment
candidate_tags:
  - "E-BeamSim"
source_refs: []
doi: "10.1002/smtd.202400203"
year: 2024
authors:
  - "Matthew G. Boebinger"
  - "Dundar E. Yilmaz"
  - "Ayana Ghosh"
  - "Sudhajit Misra"
  - "Tyler S. Mathis"
  - "Sergei V. Kalinin"
  - "Stephen Jesse"
  - "Yury Gogotsi"
  - "Adri C. T. van Duin"
  - "Raymond R. Unocic"
venue: "Small Methods"
pdf_sha256: "4853e029fca304b32dbf76d90b50af098ce57bb72319e97a62c3e38a770c76b7"
pdf_path: "papers/Boebinger_Small_Methodology_2024_MXene_defects.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024boebinger-small-method-direct-fabrication -->

## Summary

Nanopores in two-dimensional materials are technologically interesting for ion transport, nanofiltration, and related membrane applications, but many fabrication routes rely on plasma etching or broad-beam irradiation with limited in situ control. This *Small Methods* article reports a **feedback-driven aberration-corrected scanning transmission electron microscopy (STEM)** workflow that combines sub-angstrom electron probes, **real-time atomic imaging**, and **automated** pore sculpting to study how **Ti₃C₂Tₓ MXene** transforms under electron-beam processing as a function of temperature. Complementing the microscope work, the authors introduce an **Electron-Beam Simulator (E-BeamSim)** to visualize atomic movements and interactions under irradiation, and they connect the experimental motivation to prior **reactive force field** studies of beam- and ion-induced defect evolution in graphene that established dose-, ion-size-, and ion-species-dependent trends in defect types and nanopore sizes. The MXene focus extends that mechanistic picture to a chemically complex, surface-terminated two-dimensional ceramic where oxygen-, fluorine-, and hydroxyl-bearing terminations and titanium sublattice mobility can couple to beam-induced disorder.

## Methods

### In situ STEM fabrication (experiment)

**Aberration-corrected STEM** with **feedback**/**real-time** imaging during **nanopore** sculpting in **Ti\(_3\)C\(_2\)T\(_x\)** (**MXene**).

### Irradiation simulation (E-BeamSim)

**E-BeamSim** tracks **displacements** and **edge** restructuring under **e-beam** exposure.

### Atomistic context (literature / cited ReaxFF MD)

Intro cites **ReaxFF MD** on **ion**-irradiated **graphene** (defect/**nanopore** statistics vs **dose**, **ion** species) as precedent for **knock-on**/**vacancy** behavior; **MXene** adds **surface termination** and **T**-dependent **mobility** (**layerwise** vs **disordered** removal)—full **dose**/**energy** in article/**SI**.

**MD application (literature context; not new ReaxFF in this paper).** This **Small Methods** report centers on **STEM** and **E-BeamSim**; prior **graphene** **ion**-irradiation **ReaxFF** **molecular dynamics** in the **cited** **literature** used **LAMMPS**-class **engines** with **periodic** **supercells**, **NVT** or **NVE** exposure segments, **time step** and **duration** tied to **dose** metrics, and **Nosé–Hoover** or **Berendsen** **thermostats** as in those sources—**N/A** to restate those **ion**-MD numbers on this page. This **MXene** work’s own **simulation** is **E-BeamSim** (not **ReaxFF**); **N/A**—**NPT** **barostat**; **N/A**—**external** **DC** **electric field** in the **E-BeamSim** description here; **N/A**—**metadynamics**. **Temperature** is a key **experimental** control for **STEM** processing.

## Findings

At **room temperature**, electron-beam exposure induces **random atomic displacements** and **titanium pile-up** at nanopore edges; **E-BeamSim** reproduces this qualitative edge-disorder behavior. At **elevated temperature**, after **surface-group** removal and with increased atomic mobility, the system undergoes transformations consistent with **more selective**, **layer-resolved** atom removal, enabling more **controlled** pore growth relative to the room-temperature regime. The authors frame these observations as a route toward **defect engineering** not only in functionalized MXenes but more broadly in other two-dimensional layers where beam processing can be paired with temperature as a control knob.

**Comparisons and sensitivity.** **E-BeamSim** **compares** qualitatively to **STEM** at **room** vs **elevated** **temperature**; **sensitivity** to **beam** **dose** and **energy** is in the **main** text/**SI**. **Corpus honesty:** **ReaxFF** precedents are **literature**-level, not new **fits** in this article.

## Limitations

Quantitative beam **dose**, **energy**, and full simulation parameter sets must be taken from the **main text** and **Supporting Information** rather than this wiki summary. E-BeamSim and cited ReaxFF precedents are complementary tools; direct one-to-one quantitative mapping from graphene ion irradiation to MXene electron-beam chemistry should be treated cautiously without article-specific validation.

## Relevance to group

Couples **ReaxFF-capable** modeling (**van Duin**/**Yilmaz**) with **in situ electron microscopy** of **2D ceramics** for **nanopore** fabrication.

## Citations and evidence anchors

- DOI: `10.1002/smtd.202400203`

## Related topics

- [[reaxff-family]]
