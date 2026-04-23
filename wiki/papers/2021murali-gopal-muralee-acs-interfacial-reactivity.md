---
id: paper:2021murali-gopal-muralee-acs-interfacial-reactivity
type: paper
title: "Interfacial reactivity and speciation emerging from Na-montmorillonite interactions with water and formic acid at 200 °C: Insights from reactive MD, IR spectroscopy, and X-ray scattering"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acsearthspacechem.0c00286"
year: 2021
authors:
  - "Murali Gopal Muraleedharan"
  - "Hassnain Asgar"
  - "Seung Ho Hahn"
  - "Nabankur Dasgupta"
  - "Greeshma Gadikota"
  - "Adri C. T. van Duin"
venue: "ACS Earth Space Chem. 2021, 5, 1006–1019"
pdf_sha256: "3567d6ac9c50217401ae7cc187a066a7de053acf36f2b1c278c57b62659248a9"
pdf_path: "papers/Muraleedharan_ACS_EarthSpace_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021murali-gopal-muralee-acs-interfacial-reactivity -->

## Summary

Muraleedharan *et al.* develop a **ReaxFF** description for **Na-montmorillonite** interacting with **water** and **formic acid** at **473 K** and **1 atm**, training against **DFT** reaction energetics and validating against **FTIR** spectra of unreacted and reacted mixtures and against **small-/wide-angle X-ray scattering** signatures associated with **carbonate/bicarbonate** products in **clay interlayers**. The scientific target is **interfacial speciation** under **hydrothermal**-relevant conditions: which **pathways** produce **carbonate**, **formate**, and **hydroxide** species, and how reactivity differs across **edge**, **facet**, and **interlayer** regions where **acidity** and **confinement** vary. **Adri C. T. van Duin** is a coauthor, aligning the paper with the group’s **clay–fluid** reactive modeling and **geo** chemistry portfolio.

## Methods

**Experiments (clay + fluid, 200 °C).** **SWy-3** **Na-montmorillonite** is reacted with **water** and **1:1 formic acid/water** in **Parr** vessels at **200 °C (473 K)**, **2 h**, **1 atm**; solids are recovered for **FTIR**, and **SAXS/WAXS** target **interlayer** **spacing** and **inorganic** **product** **signatures** after reaction (carbonate/bicarbonate **features** in the **X-ray** data as developed in the paper).

**Force-field training (ReaxFF for Na–clay + C/H/O).** A **ReaxFF** **parameterization** is adjusted so that **reaction** **energetics** and **vibrational** **fingerprints** from **ReaxFF**-based **IR** **simulations** **match** **DFT** **reference** data and the **experimental** **FTIR** for selected **clay+fluid** **compositions** (iterative **fit** **protocol** in the article). **QM** **reference** — **DFT** **reaction** **energies** and **mode** data as listed in the Methods; **N/A** in this short note to list every **functional**/**basis** line—see **SI**.

**MD application (ReaxFF, ADF and LAMMPS).** *Production speciation and kinetics* use **ReaxFF** in **Amsterdam Modeling Suite (ADF)**. **Ensemble: anisotropic NPT** with **fixed x, y** cell edges and a **weak Berendsen** thermostat/barostat (**0.1 ps** temperature damping per the article). **Time step: 0.25 fs**; **velocity Verlet** integration. **Total trajectory length ~0.6 ns**; **three** independent replicates with different **initial** **geometries** to average **observables**. *IR postprocessing* uses a **ReaxFF/LAMMPS** path with **NPT** runs of **up to ~20 ps**; the **total dipole moment** is **recorded** every **0.5 fs** for line-shape analysis. **State conditions** are matched to the **laboratory** **batch** targets **T = 473 K**, **P = 1** **atm** (after *gas-phase* pre-equilibration to the **target** **density** described in the Methods, prior to reactivity). **3D** **PBC** **clay+fluid** **supercells** resolve **interlayer**, **edge**, and **facets** in Figure 1. **Electric field, shear, shock, metadynamics — N/A**.

**Static DFT — N/A** as a separate *results* code path beyond **DFT** used to **build** and **refine** the **ReaxFF** and to benchmark **reaction** **energies** as stated in the article.

## Findings

**IR validation.** **Simulated** **ReaxFF**-based **IR** **line** **shapes** align with **experimental** **FTIR** for **unreacted** and **reacted** **assemblages** after the **reparameterization**, supporting **carbonate**, **formate**, and **hydroxide** **assignments** under **confinement**.

**Scattering.** **SAXS/WAXS**-guided **validation** of **inorganic** **interlayer** **carbonation** (e.g. **sodium** **carbonate/bicarbonate**-related **features**) is used as an **independent** **experimental** check beyond **IR** alone.

**Interfacial chemistry.** The authors stress that **reaction** **pathways** **differ** **between** **clay** **edge**, **tactoid** **face**, and **interlayer** **pores** because of **pH**/**acidity** **gradients** and **nanoconfinement**. **N/A** in this **note** to map every **reaction** **name**; see **Results** in `pdf_path`.

**Sensitivity and outlook.** The **T**=**200 °C**, **1 atm** **batch** **chemistry** and **synthetic** **MMT** **assumptions** frame **where** the **ReaxFF** is **tied**; **geologic** **diversity** **outside** the **fit** is a **knowledge** **gap**—see **## Limitations**.

## Limitations

Idealized **clay** cells only partially represent **stacking faults** and **cation substitutions** in natural samples. **FTIR** and **scattering** validation ties parameters to specific **batch** chemistry; transfer to other **clay** sources requires prudence.

## Reader notes (navigation)

Use this entry as a **geo**/**environmental** bridge to [[theme-water-silica-geochemistry]]; keep **`experiment-integrated`** in frontmatter for **retrieval** filters that prioritize **validation** workflows.

## Relevance to group

Showcases **ReaxFF reparameterization** plus **experimental** validation for **clay–fluid** chemistry (**van Duin** co-author).

## Citations and evidence anchors

- ACS Earth Space Chem. **5**, 1006–1019 (2021); DOI **10.1021/acsearthspacechem.0c00286** — **Methods** §2 and **Results** on **IR/SAXS** benchmarks.

## Related topics

- [[reaxff-family]]
- [[theme-water-silica-geochemistry]]

