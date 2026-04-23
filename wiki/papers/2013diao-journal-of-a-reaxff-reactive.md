---
id: paper:2013diao-journal-of-a-reaxff-reactive
type: paper
title: "ReaxFF reactive force field for molecular dynamics simulations of epoxy resin thermal decomposition with model compound"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:reactive-md
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1016/j.jaap.2013.05.005"
year: 2013
authors:
  - "Diao, Zhijun"
  - "Zhao, Yuemin"
  - "Chen, Bo"
  - "Duan, Chenlong"
  - "Song, Sun"
venue: "Journal of Analytical and Applied Pyrolysis"
pdf_sha256: "6ff5c21f6d0610abd531d5d3504c63950e29958e3fb6100f2a98485a091e8c58"
pdf_path: "papers/ReaxFF_others/Diao_epoxides_JAAP_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013diao-journal-of-a-reaxff-reactive -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

**ReaxFF** MD is used to study **thermal decomposition** of an **epoxy resin** model, scanning **temperature** and **heating rate** effects on small-molecule product evolution. Decomposition is reported to initiate via **ether C–O** cleavage, with major small-molecule products including **H₂O**, **CO**, and **H₂**. The authors classify **H₂O** and **H₂** formation mechanisms (radical attack vs **1,1/1,2/1,3 elimination** channels) observed in trajectories and compare qualitative trends to experimental pyrolysis literature for epoxies.

## Methods

**1 — MD application (atomistic dynamics).** **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** as implemented in the article (the **JAAP** **Methods** section should be checked in **`pdf_path`** for the explicit **MD** package name; community practice often cites **LAMMPS** with **ReaxFF**). **System size & composition:** **15** epoxy-resin **model** molecules in a **33 Å × 33 Å × 33 Å** periodic cell at **~0.47 g/cm³** initial density (**~10³ atoms** class **supercell** per the article and `normalized/extracts/2013diao-journal-of-a-reaxff-reactive_p1-2.txt`). **Boundaries / periodicity:** **three-dimensional periodic boundary conditions** on the cubic cell. **Ensemble / staging:** structures are **energy minimized** to **1 kcal/mol/Å** residual force tolerance, then **NPT**-equilibrated at **300 K** for **50 ps** with **Berendsen** thermostat and **barostat**, compressing the cell toward **~1.0 g/cm³** solid-like density (**~31.7 × 22.0 × 22.6 Å³** box quoted in the article). **Pyrolysis** production uses **NVT** **MD** with **velocity Verlet** integration (**0.1 fs** timestep), **Berendsen** thermostat (**100 fs** damping), **temperature-programmed** heating from **300 K** to **2300 K** at **100–500 K/ps**, plus additional **constant-temperature** runs at **2800 K**, **3300 K**, and **4300 K** as reported. **Duration:** equilibration and pyrolysis segment lengths are given in the **Methods**/**Results** of **`pdf_path`** (not fully transcribed in the short extract). **Temperature:** spans **300–4300 K** in the protocol summary above. **Pressure:** **NPT** leg at **300 K** uses **barostat** coupling toward target density; **NVT** pyrolysis legs are **constant-volume** with **N/A —** no additional **GPa**-scale **hydrostatic pressure** control stated for those **NVT** segments. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not reported. **Species analysis:** **bond-order cutoff 0.3** for product classification.

**2 — Force-field training.** **ReaxFF** uses an **H/C/N/O** parameter set cited in the article (developed against **QM** references for oxygen-containing organics as given there). **N/A —** this paper applies an existing parameterization line; it is not principally a new **general** **ReaxFF** extension paper.

**3 — Static QM / DFT.** **N/A —** **QM** is referenced for **force-field** context, not as standalone **DFT** production results in the sense of AGENTS block **3**.

## Findings

**1 — Outcomes & mechanisms.** **Thermal decomposition** is initiated preferentially by **ether (C–O)** cleavage; **initial reaction temperature** and **initiation time** trends with **heating rate** and **final temperature** are discussed in the **Abstract**/**Results** (see **`pdf_path`** for quantitative tables). Major small-molecule products tracked include **H₂O**, **CO**, and **H₂**; the authors classify **H₂O**/**H₂** formation via **radical attack** and **1,1- / 1,2- / 1,3-elimination** channels observed in trajectories.

**2 — Comparisons.** The article states **qualitative agreement** between simulation **mechanisms**/**chemical events** and prior **experimental** observations on epoxy **pyrolysis** (abstract-level claim; see **`pdf_path`** for literature pointers).

**3 — Sensitivity & design levers.** **Heating rate** (**100–500 K/ps** in the programmed ramps), **final temperature**, and **constant-T** set points (**2800–4300 K**) are the primary computational **knobs** reported in the wiki-grounded summary.

**4 — Limitations & outlook (as authored).** **Abstract**/**Introduction** motivate **extreme** conditions relevant to **PCB** processing contexts; **nanosecond** trajectories and **model-compound** cells imply caveats on **network** effects in real **thermosets** (see **## Limitations**).

**5 — Corpus honesty.** Substantive numerical tables and figure callouts should be taken from **`pdf_path`**; corrected-proof sibling: **`[[2013diao-journal-of-a-reaxff-reactive-2]]`**.

## Limitations

- Model compound / short-chain representation may omit network effects in real thermoset matrices; ReaxFF parameter uncertainty affects quantitative kinetics.

## Relevance to group

Demonstrates **ReaxFF** for **polymer pyrolysis** and waste-treatment adjacent contexts (PCBs noted in the article motivation).

## Citations and evidence anchors

- Abstract and Sec. 1: decomposition claims (J. Anal. Appl. Pyrol.; DOI above).

## Reader notes (navigation)

- Corrected-proof PDF variant: [[2013diao-journal-of-a-reaxff-reactive-2]].

## Related topics

- [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]
