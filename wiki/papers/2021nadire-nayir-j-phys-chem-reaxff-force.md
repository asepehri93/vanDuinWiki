---
id: paper:2021nadire-nayir-j-phys-chem-reaxff-force
type: paper
title: "A ReaxFF Force Field for 2D-WS2 and Its Interaction with Sapphire"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - material:tmd
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:2d-materials
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.1c03605"
year: 2021
authors:
  - "Nadire Nayir"
  - "Yun Kyung Shin"
  - "Yuanxi Wang"
  - "Mert Y. Sengul"
  - "Danielle Reifsnyder Hickey"
  - "Mikhail Chubarov"
  - "Tanushree H. Choudhury"
  - "Nasim Alem"
  - "Joan Redwing"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C 2021, 125, 17950–17961"
pdf_sha256: "41f7e8f8dcb2c4ec3e2db683f0a3c641c0c92129fe1c2abd8f55122c0cec0516"
pdf_path: "papers/Nayir_WS2_Sapphire_JPCC_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021nadire-nayir-j-phys-chem-reaxff-force -->

!!! abstract "Scope"
    New ReaxFF parameters for W/S/H/Al/O describe monolayer and few-layer WS\(_2\) (phases, defects, edges, grain boundaries) and WS\(_2\)/sapphire interfaces, trained on quantum-mechanical data and checked against ADF-STEM experiments reported in the article.

## Summary

The work introduces a ReaxFF parameter set for 2D WS\(_2\) and its interaction with sapphire, aimed at large-scale reactive molecular dynamics of synthesis-relevant structure and defects. The training set includes periodic and nonperiodic quantum data on semiconducting and metallic WS\(_2\), point and line defects (including ripplocations), edge excess energies at different sulfur coverages, and W(SH)\(_2\)S\(_2\) bond/angle energetics. For the metal–oxide interface, data cover corundum Al\(_2\)O\(_{3-x}\)S\(_x\), sulfur in fcc Al, and sulfur adsorption and diffusion on Al(100) and Al(111). Benchmark molecular dynamics and comparison to post-training DFT and annular dark-field scanning transmission electron microscopy (ADF-STEM) experiments are used to assess the model; fitting details, parameters, and extended methods are documented in the Supporting Information.

## Methods

**Force-field training (ReaxFF for W/S/H/Al/O).** A **ReaxFF** set is **fitted** to **DFT/QM** reference data covering **2D WS\(_2\)** (2H/1T, **defects**, **edges**, **grain boundaries**), **W(SH)\(_2\)**-class **local** **hydration** motifs, and **sapphire**-relevant **Al–O–S** and **Al–S** environments (corundum **Al\(_2\)O\(_3\)**-based training points, **S** in **fcc** **Al**, and **S** **adsorption/diffusion** on **Al(100)** and **Al(111)**), with tables in the *J. Phys. Chem. C* paper and **SI**. **Optimization** uses the **group**’s **ReaxFF** **Monte Carlo** / **CMA-ES**-style **workflow**; the **parameter** **file** is in the **SI**.

**MD application (LAMMPS ReaxFF).** **LAMMPS** with the new **ReaxFF** is used for **slab/ribbon** and **WS\(_2\)/sapphire** **case studies** (phase **changes**, **defect** **transport**, **interface** **morphology**). **NVT** **thermostat** at **reported** **temperatures** in **K** and **ps–ns**-scale **trajectory** **lengths** as **tabulated** in **Section 2** and the **Results** of *J. Phys. Chem. C* (exact **K** and **fs** **values** in **`pdf_path`**, not re-keyed on this page); **3D** **PBC** with **slab** **buffer** **freezing** as **specified** in **Section 2**. **NPT** **stress** **tests** only where **listed** in the **VOR**+**SI**. **Barostat — N/A** in **strict** **NVT** **defect** **blocks**; **NPT** only where the **text** **lists** **it**. **Hydrostatic** **pressure** in **(bar):** **N/A** as a **separate** **user** **knob** in **NVT** **defect** **blocks**; **1** **bar**-style **NPT** only in **dedicated** **segments**. **E-field, metadynamics, shock — N/A** in the **benchmarks** summarized in the **abstract**-level **summary** on this page.

**Static QM (training only).** **DFT** is the **reference** for **fitting**; **not** a separate **PES** **publication** **beside** the **ReaxFF** work.

**Experiments.** **ADF-STEM** of **CVD** **WS\(_2\)** on **sapphire** where **cited** for **interface** **morphology**.

## Findings

**Model behavior.** The **ReaxFF** recovers the **2H**↔**1T** **displacive** **trend**, **S-vacancy** **migration** **barriers**, **line**-**defect** **energetics** (including **ripplocations**), **1T** **domain** **nucleation** on **2H** **basal/edge** **regions**, and **grain-boundary** **trends** vs **S** **chemical** **potential** (including **S-** vs **W-terminated** **edges**). **Coalesced** **WS\(_2\)** on **sapphire** is used to discuss **epitaxy**-relevant **shapes**.

**Comparisons.** **Post-hoc** **DFT** **checks** and **STEM** **images** support selected **barriers/structures**; **tabulated** **meV/Å** **values** are in the **PDF**/**SI**, not re-keyed on this page.

**Sensitivity and levers.** **T**, **S** **chemical** **potential** / **coverage**, and **substrate** **orientation** shift **predicted** **defect** **populations** and **morphology**.

## Limitations

Training and validation scope follow the systems and conditions in the article and Supporting Information; transfer to other substrates or chalcogen chemistries requires separate assessment.

## Relevance to group

Develops and validates group-lineage ReaxFF for a major 2D TMD system and its oxide substrate, with joint experimental (STEM) validation.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.1c03605](https://doi.org/10.1021/acs.jpcc.1c03605)

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Cross-link other 2D TMD or oxide-interface theme hubs in `wiki/concepts/` when curated.
