---
id: paper:2023leon-c-thijs-j-phys-chem-effect-fe
type: paper
title: "Effect of Fe–O ReaxFF on Liquid Iron Oxide Properties Derived from Reactive Molecular Dynamics"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:alloys-metallurgy
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:validation-experiment
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.3c06646"
year: 2023
authors:
  - "Leon C. Thijs"
  - "Efstratios M. Kritikos"
  - "Andrea Giusti"
  - "Marie-Aline van Ende"
  - "Adri C. T. van Duin"
  - "XiaoCheng Mi"
venue: "J. Phys. Chem. A"
pdf_sha256: "293558373799010d27b552ae080c81f65d237ee6dbb82ee49fb6ddc9ca94e432"
pdf_path: "papers/Thijs_Kritikos_FeO_liquid_JPCA_2023.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023leon-c-thijs-j-phys-chem-effect-fe -->

## Summary

Liquid **Fe–O** is modeled at **2000 K** over oxidation degrees **\(Z_\mathrm{O} = \mathrm{O}/(\mathrm{O}+\mathrm{Fe})\)** with **0 < \(Z_\mathrm{O}\) < 0.6**, motivated by **iron powder combustion** as an energy carrier. This benchmark-style reactive MD study compares several **ReaxFF** parameterizations for the same thermodynamic state and observables, against experiment and thermodynamic data where available. The authors evaluate how choice of Fe–O ReaxFF affects **minimum-energy paths**, **structure**, **(im)miscibility of liquid phases**, **transport coefficients**, and **mass and thermal accommodation coefficients**, comparing to experiments and equilibrium calculations when possible, with the overarching goal of identifying which macroscopic observables are most sensitive to parameter-line differences.

## Methods

### Simulation matrix (B)

**Liquid Fe–O** at **2000 K**, scanning **oxygen fraction** **\(Z_\mathrm{O}=\mathrm{O}/(\mathrm{O}+\mathrm{Fe})\)** with **0 < \(Z_\mathrm{O}\) < 0.6**.

### Observables

**Minimum-energy paths**, **structure**, **liquid miscibility**, **transport** coefficients (**diffusivity**/**viscosity** proxies), **mass/thermal accommodation** coefficients for **gas–liquid** models.

### Parameter-set comparison (A)

Multiple literature **Fe–O ReaxFF** sets run **side-by-side** vs **experiment** and **equilibrium** references; diagnostics separate **structural** vs **transport** sensitivity.

The *J. Phys. Chem. A* framing ties the benchmark to **iron powder combustion** as a **metal-fuel** concept: **liquid** **oxide** **microphysics** controls **evaporation**, **condensation**, and **gas–surface** **accommodation** in **spray**/**particle** flames, so **force-field** differences that shift **miscibility** or **transport** can propagate to **macroscopic** **burning** models even when **short-range** **pair** **correlations** look similar.

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** with each compared **Fe–O** **ReaxFF** **parameter** **line** (as listed in the article). **System & composition:** **Bulk** **liquid** **Fe–O** at **2000** K, **0 < \(Z_\mathrm{O}\) < 0.6** in **O/(O+Fe)**. **Boundaries / periodicity:** 3D **PBC** **melt** cells. **NVT** **production** **runs** at **2000** **K** use **fs**-scale **timesteps** and **multi-ns** **durations** as tabulated; **N/A** on this page for every **NVT** **thermostat** **constant** and **ns** **clock** (see *J. Phys. Chem. A* **Methods** and SI). **Pressure, electric field, shear, shock, enhanced sampling:** **N/A** in this short summary for the **liquid** **Fe–O** **benchmark** (see **PDF** if a subsection adds one of these).

### 2 — Force-field training

**N/A** in the sense of a **new** **fit**—this paper **compares** **existing** **Fe–O** **ReaxFF** **lines**; training histories differ by line and are in the **original** parameterization papers.

### 3 — Static QM

**N/A** for **on-the-fly** **ab initio** **MD**; the article references **thermodynamic** and **structural** **comparators** and **MEP**-class analyses as described in the **Methods**.

## Findings

### Sensitivity conclusion

**Different Fe–O ReaxFF lines** predict **markedly different** **liquid** properties and **accommodation/transport** numbers at identical **T**/**composition**.

### Implication

Authors argue an **improved Fe–O** parametrization is needed for **iron combustion** modeling, and identify which **observables** diverge most across **parameterizations**.

Across **2000** **K** **liquid** **Fe–O** **compositions**, **transport** and **accommodation** **coefficients** **compared** with **literature** **and** **equilibrium** **surrogates** show **strong** **sensitivity** to which **ReaxFF** **line** is chosen—this is a **central** **limitation** of **empirical** **reactive** **MD** for **metal** **spray** **flames** when **oxidation** **reaction** **networks** are not identically **encoded** between **parameter** **sets**. **Future** **work** would **tighten** the **Fe–O** **database** against **high-T** **experiments**; **quote** **PDF** **tables** in `pdf_path` for **values** **not** repeated here.

## Limitations

ReaxFF accuracy is parameter-set- and training-data-dependent; high-temperature liquid iron oxide properties are sparsely characterized experimentally at atmospheric pressure, which constrains validation. When multiple Fe–O parameter lines disagree, the authors’ comparative framing should be read as identifying sensitivity hotspots—transport and accommodation numbers may shift non-linearly if short-range oxygen packing is misrepresented—even when qualitative liquid miscibility trends look similar across force fields. The **2000** **K** **scan** over **\(Z_\mathrm{O}\)** is a deliberate **computational** **benchmark** design: it separates **structural** **sensitivity** from **transport**/**accommodation** **sensitivity** when comparing **published** **Fe–O** **lines** side by side.

## Relevance to group

**Adri C. T. van Duin** co-authors; connects ReaxFF combustion chemistry to **metal fuels** and group expertise in reactive MD parameter assessment.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.3c06646](https://doi.org/10.1021/acs.jpca.3c06646)

## Reader notes (navigation)

- Metal combustion and liquid oxide benchmarking: pairs with [[theme-pyrolysis-combustion-organics]] and broader [[reaxff-family]] Fe–O parameter discussions.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
