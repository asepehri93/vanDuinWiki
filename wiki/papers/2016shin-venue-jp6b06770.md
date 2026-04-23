---
id: paper:2016shin-venue-jp6b06770
type: paper
title: "Development of a ReaxFF reactive force field for the Pt–Ni alloy catalyst"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.6b06770"
year: 2016
authors:
  - "Yun Kyung Shin"
  - "Lili Gai"
  - "Sumathy Raman"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A"
pdf_sha256: "d40410ed85d95cff7a8057df0c227dbedaa99c30a469cbe4781bd92ab6f230b2"
pdf_path: "papers/Shin_PtNiCHO_JPCA_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016shin-venue-jp6b06770 -->

## Summary

This paper develops a **ReaxFF** description of **Pt/Ni/C/H/O** aimed at **heterogeneous catalysis**, fitting to **DFT** data on **Pt–Ni alloy** equations of state, **surface energies** of **Pt\(_x\)Ni\(_{1-x}\)** facets, and **adsorption** of **O**, **H**, **C**, **hydrocarbon fragments**, **CO**, **OH**, and **H\(_2\)O**. **GCMC** and **MD** on **slabs** and **nanoparticles** probe **Pt** vs **Ni segregation** under **vacuum**, **H\(_2\)**, and **O\(_2\)**, matching trends for **Pt-rich** compositions while noting weaker behavior for **Ni-rich** alloys. **ExxonMobil** coauthorship reflects **industrial catalysis** context.

## Methods

**1 — MD application (GCMC and classical MD).** After parametrization, **grand-canonical Monte Carlo (GCMC)** and **molecular dynamics (MD)** probe **surface segregation** for a **Pt\(_3\)Ni** **slab** and a **truncated cuboctahedral** nanoparticle exposing **(111)** and **(100)** facets under **vacuum**, **H\(_2\)**, and **O\(_2\)**, with **PBC** as in the published models. **Timestep**, **thermostat/barostat** choices, **temperature** and **pressure** setpoints, **run lengths**, and **electrostatic** details are **N/A —** not restated in the indexed excerpt; use **`pdf_path`**. **Electric fields** and **enhanced sampling** beyond **GCMC/MD** are **N/A —** not indicated in that excerpt.

**2 — Force-field training.** The authors develop **Pt/Ni/C/H/O** **ReaxFF** parameters for **heterogeneous catalysis** on **Pt–Ni** alloys using **DFT** reference data for **equations of state** of **Pt\(_3\)Ni**, **PtNi**, and **PtNi\(_3\)**, **Pt\(_x\)Ni\(_{1-x}\)(111)** **surface energies** with **\(x = 0.67\)–\(0.83\)**, and **adsorption energies** of **O**, **H**, **C**, **CH**, **CH\(_2\)**, **CH\(_3\)**, **CO**, **OH**, and **H\(_2\)O** on **Pt\(_8\)Ni\(_4\)**, **Pt\(_9\)Ni\(_3\)**, and **Pt\(_{10}\)Ni\(_2\)** reference cells, emphasizing reproduction of **composition-dependent binding-strength orderings** tabulated in the paper. **DFT** program, **functional**, **basis**, and **k**-mesh settings for the training set are **N/A —** not duplicated here.

**3 — Static QM / DFT.** **DFT** supplies **equations of state**, **surface energies**, and **adsorption** energies that define the **ReaxFF** training targets. Full **DFT** software, **functional**, **basis**, and **k**-mesh tables are in **`pdf_path`** rather than duplicated here.

**GCMC**/**MD** segregation studies use **PBC** slabs and a truncated cuboctahedral nanoparticle with explicit **H\(_2\)** or **O\(_2\)** as in **J. Phys. Chem. A**. Applied electric fields and umbrella, metadynamics, or replica-exchange sampling are **N/A —** not indicated in the abstract-level excerpt. Timestep, equilibration and production lengths, and thermostat or barostat parameters are **N/A —** not transcribed here.

## Findings

**Segregation trends (vacuum).** The fitted field reports **Pt surface segregation** for **(111)** at **\(x \geq 0.67\)** and for **(100)** at **\(x \geq 0.62\)** in **vacuum** in the authors’ analysis.

**Adsorbate-driven segregation.** **H** and **CH\(_3\)** are associated with driving **Pt** to the surface, whereas **oxidation intermediates/products** such as **C**, **O**, **OH**, **H\(_2\)O**, **CO**, **CH**, and **CH\(_2\)** tend to draw **Ni** to the surface. Under **O\(_2\)**, **Ni** segregates to the surface of a model **PtNi** nanoparticle, whereas under **H\(_2\)** or **vacuum**, **Pt** segregation is favored—consistent with the differential **affinities** discussed in the article.

**Transferability limits.** The authors state the parametrization **performs reasonably** for **Pt:Ni** ratios **greater than ~0.6** but has **difficulty** with **Ni-rich** compositions (**\(x < 0.6\)**), motivating **additional training** for Ni-rich **alloys**.

## Limitations

- **Bimetallic** reactive spaces are large; remaining errors map to specific **composition**/**adsorbate** corners.

## Relevance to group

Core **ReaxFF parametrization** publication from **van Duin**’s group on **alloy catalyst** modeling.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpca.6b06770` (`papers/Shin_PtNiCHO_JPCA_2016.pdf`).

## Related topics

- [[reaxff-family]]
