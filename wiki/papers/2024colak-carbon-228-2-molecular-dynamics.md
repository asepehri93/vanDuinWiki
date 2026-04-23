---
id: paper:2024colak-carbon-228-2-molecular-dynamics
type: paper
title: "Molecular dynamics simulations of 2D-layered graphene sheets with tandem repeat proteins"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - material:graphene-carbon-nano
  - material:polymer-organic
  - method:classical-md
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2024.119332"
year: 2024
authors:
  - "Oguzhan Colak"
  - "Adrien Nicolaï"
  - "Vincent Meunier"
  - "Melik C. Demirel"
venue: "Carbon 228, 119332 (2024)"
pdf_sha256: "abf88f5a72c1d45b5e345fb46cac740ebe73c07d5f1117ca1aa85b213249b7b6"
pdf_path: "papers/Others/Colak_carbon_2024.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024colak-carbon-228-2-molecular-dynamics -->

## Summary

**2D nanomaterials** are frequently combined with **proteins** to engineer **biocomposites** with tunable **mechanics**, but atomistic design requires models that capture both **sheet** mechanics and **biopolymer** conformations. This **Carbon** article studies **graphene oxide (GO)** nanosheets embedded in a matrix of **recombinant squid-inspired tandem-repeat (TR) proteins**, extending earlier **GO/MXene + TR protein** composite work from the same group. The central claim is that **TR proteins** provide **controlled chain length and structure**, producing **repeatable mechanical properties** that **scale quasi-linearly** with the number of repeat units—consistent with an **experimental trend** cited in the introduction. The study positions the platform as a route toward **ordered 2D biocomposites** where **stiffness** and **flexibility** can be traded systematically through **protein** architecture rather than only through **filler** loading. The motivation is practical for **nanocomposite** design: **TR** proteins offer a **polymer** degree of freedom that can be engineered independently of **GO** oxidation or **sheet** concentration, which matters when manufacturing constraints fix the **2D** phase but not the **matrix** compliance. Quantitative moduli and stress–strain points should be taken from the **Carbon** article text, figures, and SI.

## Methods

### Classical atomistic MD (B; non-ReaxFF)

**GO** + **tandem-repeat (TR) protein** composites under **mechanical** loading (**BCs**, **strain rate**, moduli, **stress–strain**) per *Carbon* **228**, **119332**; **FF** details in **`papers/Others/Colak_carbon_2024.pdf`**.

### Comparison to experiment

Metrics compared to **published** mechanical data for this **biomimetic** system.

### Design variable (TR repeat count)

**TR** **repeat** count tunes **stiffness** largely **orthogonal** to **GO** chemistry/**loading**—the paper’s scaling claim.

**MD application (classical, GO + TR protein).** **Molecular dynamics** (package in *Carbon* **228** **119332**) on **graphene oxide**+**tandem-repeat** **protein** composites at the **temperature** setpoints in *Carbon* (see **Methods** for **K**): **NVT** or **NPT** **uniaxial**/**biaxial** **deformation** as in the **Methods**; **periodic** **PBC**; **atom** counts, **GO** oxidation level, **protein** **chain** **length** sweeps, **time step** (fs), **equilibration**/**production** (ns), **Nosé–Hoover** **thermostat** and **NPT** **barostat** (if used for **stress** control) are in the **primary** text. **N/A**—**external electric field**; **N/A**—**metadynamics**; **Shear**/**strain** **rate** for **mechanical** tests as tabulated.

## Findings

**Simulation-derived** mechanical responses align with **published experiments** for this composite class in the comparisons shown. **Tandem repeat count** acts as a **predictable design variable** for **stiffness** in the models tested, supporting the quasi-linear scaling narrative. The article frames these results as useful guidance for **bioinspired** materials engineering even though atomistic models omit some **biological** complexity (ionic strength, full hydration kinetics, and potential **charge transfer** when relevant). For the knowledge base, the key transferable point is **design separability**: **TR protein** length provides an orthogonal knob to **filler** fraction, enabling mechanical tuning without necessarily changing **GO** oxidation or **sheet** concentration—useful when processing constraints fix the **2D** content but still require **compliance** adjustments.

## Limitations

**Force-field** dependence for **proteins** and **oxidized graphene** surfaces; limited sampling of complex **biological** environments; classical models omit **charge-transfer** effects when they matter for adhesion.

## Relevance to group

Included as neighboring **2D biocomposite mechanics** context (**Demirel / Meunier**); no **van Duin** authorship.

## Citations and evidence anchors

https://doi.org/10.1016/j.carbon.2024.119332 — Abstract (~p. 1) states GO + TR protein focus and scaling claim.

## Related topics

- [[graphene-nanocarbon]]
