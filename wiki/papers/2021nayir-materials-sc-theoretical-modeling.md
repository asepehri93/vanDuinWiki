---
id: paper:2021nayir-materials-sc-theoretical-modeling
type: paper
title: "Theoretical modeling of edge-controlled growth kinetics and structural engineering of 2D-MoSe2"
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
candidate_tags: []
source_refs: []
doi: "10.1016/j.mseb.2021.115263"
year: 2021
authors:
  - "Nadire Nayir"
  - "Yuanxi Wang"
  - "Yanzhou Ji"
  - "Tanushree H. Choudhury"
  - "Joan M. Redwing"
  - "Long-Qing Chen"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
venue: "Mater. Sci. Eng. B 271 (2021) 115263"
pdf_sha256: "c401c2cf81c7cff5da18e9674a40250e02918ca8b135dd35dabbf1483ae38e45"
pdf_path: "papers/Nayir_MoSe2_MatSciEngB_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021nayir-materials-sc-theoretical-modeling -->

!!! abstract "Scope"
    First ReaxFF description for Mo/Se/H trained on first-principles data for 2D MoSe\(_2\), used for MD and a Wulff-based model of edge-limited growth morphology.

## Summary

The article presents a ReaxFF parameterization for Mo/Se/H intended for large-scale reactive molecular dynamics of 2D MoSe\(_2\) synthesis and processing. Training draws primarily on first-principles energetics for periodic and non-periodic systems. The fitted potential is used to describe the metallic–semiconducting structural transition, defect energetics, and selenium-vacancy migration, and—together with a Wulff-construction-based model—to interpret morphology evolution of MoSe\(_2\) domains during growth. Edge formation energies of MoSe\(_2\) nanoribbons with different Se coverages are included in the training to support simulation of edge-mediated growth kinetics.

MoSe\(_2\) growth is edge-limited in many CVD conditions; embedding edge energetics directly in the reactive FF training set distinguishes this work from bulk-only fits.

## Methods

**Force-field training (ReaxFF for Mo/Se/H).** A **ReaxFF** set is **fitted** to **DFT** **energies and structures** for **bulk and few-layer MoSe\(_2\)**, **nanoribbon** **edge** **terminations** with varied **Se coverage**, and **defect** motifs relevant to **edge-limited** **CVD** **kinetics** (formation energies, **barriers**, and **Wulff** inputs). **Functional, basis, k-mesh**, and the **ReaxFF** **Monte Carlo** / **optimizer** **workflow** are given in *Mater. Sci. Eng. B* and the **SI**; the same lineage appears in other **van Duin**-group **ReaxFF** papers cited there. Training **benchmarks** the **metallic**↔**semiconducting** bistability and **Se-vacancy** **migration** trends advertised in the abstract.

**MD application (LAMMPS with the new ReaxFF).** **Molecular dynamics** with the **fitted** **ReaxFF** in **LAMMPS** (velocity **Verlet**-style **integration** as in **Section 2**) samples **edge** and **vacancy** **dynamics** in **NVT** **PBC** **supercells**; **time step (fs)**, **ps–ns** **duration**, and **Nosé–Hoover**-class **thermostat** **settings** for **setpoint** **temperatures** in **K** are **tabulated** in the **MSE** **B** **article** and **SI**. **NPT** **barostat** **— N/A** in the **highlighted** **NVT** **defect** **blocks** unless the **VOR** adds a **stress**-relaxation case. **Hydrostatic** **pressure (bar) — N/A** in those **NVT** **blocks**. **External** **E-field, shear, metadynamics — N/A** for the **cases** in the **abstract**-level **summary**.

**Continuum / Wulff coupling (not stand-alone MD).** **ReaxFF** **edge** **excess** **energies** feed a **Wulff**-type **model** (with the **L.-Q. Chen**-group **nucleation/continuum** **coupling** as stated) to relate **anisotropic** **edge** **stiffnesses** to **CVD** **island** **morphology**.

## Findings

**Outcomes and mechanisms.** The fitted **ReaxFF** recovers the **metallic/semiconducting** bistability, the **defect** energetics highlighted in the abstract, and the **Se-vacancy** migration trends used to interpret **CVD** kinetics. **Wulff**-based analysis connects **anisotropic** ReaxFF **edge** **energies** to **triangular** vs **hexagonal** **island** **shapes** and to shifts with **Se chemical potential**-like process variables in the model.

**Comparisons.** The article relates these predictions to **CVD MoSe\(_2\)** **morphology** data and to prior **DFT** **kinetic** work as cited; **figure-level** **numbers** belong in the **VOR** **PDF**.

**Sensitivity and levers.** **Edge Se coverage** and the **chemical** **potential** inputs to the **Wulff** construction move predicted **island** **habits**; **MD** at different **T** changes which **defect** pathways are **kinetically** **sampled**.

**Corpus honesty.** This wiki page is a **curated** **summary**; for **Wulff** **inputs**, **k-meshes**, and run parameters, use **`pdf_path`** and the **SI** tied to the **VOR** **DOI** — **not** a substitute for the **manuscript** **tables**.

## Limitations

Scope is limited to the chemistry and geometries covered by the training set and the growth models discussed in the paper.

## Relevance to group

Group-authored ReaxFF development for selenide TMDs with explicit edge energetics for growth phenomenology.

## Citations and evidence anchors

- DOI: [10.1016/j.mseb.2021.115263](https://doi.org/10.1016/j.mseb.2021.115263)

## Related topics

- [[reaxff-family]]
