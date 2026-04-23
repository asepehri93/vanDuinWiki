---
id: paper:2021shin-computationa-impact-three-body
type: paper
title: "Impact of three-body interactions in a ReaxFF force field for Ni and Cr transition metals and their alloys on the prediction of thermal and mechanical properties"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:metallic-systems
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2021.110602"
year: 2021
authors:
  - "Yun Kyung Shin"
  - "Yawei Gao"
  - "Dongwon Shin"
  - "Adri C. T. van Duin"
venue: "Comput. Mater. Sci. 197 (2021) 110602"
pdf_sha256: "1deeb92dd0bb1bb9d9ac2f8294c1cf5b481c599841444218a6246d6698b13167"
pdf_path: "papers/Shin_CompMatSci_NiCr_metal_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021shin-computationa-impact-three-body -->

!!! abstract "Scope"
    Adds **three-body (valence-angle) terms** to **Ni/Cr ReaxFF**, fixing **C\(_{12}\)≠C\(_{44}\)** elastic behavior and **stacking-fault energy** for fcc Ni; **melting** via **hysteresis MD**; **Ni\(_3\)Cr** alloy stability vs DFT.

## Summary

Standard ReaxFF metal descriptions without explicit three-body angle terms yield equal C\(_{12}\) and C\(_{44}\) for fcc nickel and a negative stacking-fault energy that spuriously accelerates fcc→hcp transformation. This work augments the Ni and Cr ReaxFF parameter sets with three-body interactions for the transition metals, reproducing experimental elastic constants for fcc Ni and bcc Cr at finite temperature. Temperature-dependent lattice expansion from 0 to 1700 K follows expected trends (higher expansion for Ni versus Cr). Melting points from hysteresis molecular dynamics with large cells and voids land near 1698 K for Ni (~1.7% of experiment) and 2410 K for Cr (~10%). A combined Ni/Cr alloy parameterization predicts, consistently with DFT, negative heat of formation for fcc-like Ni\(_3\)Cr and positive heats for bcc solid solutions, suggesting phase separation tendencies. Elastic constants at 0 K match DFT within about 5–10% except for a larger deviation in C\(_{33}\) as noted in the abstract.

## Methods

**1 — MD application (LAMMPS, ReaxFF).** **Molecular dynamics** in **LAMMPS** with the fitted **ReaxFF** for **fcc** **Ni** and **bcc** **Cr** and **Ni–Cr** **alloys** uses **3D** **PBC** **supercells** containing 10⁴+ **atoms** in **void**-containing **melting** setups. **NVT** trajectories with a **thermostat** cover **thermoelastic** properties and **hysteresis** **heating**/**cooling** **melting**; **lattice** **expansion** **vs** **temperature** (**0**–**1700** **K**) and **T\(_m\)** (≈**1698** **K** for **Ni**, **2410** **K** for **Cr** in the reported **hysteresis** runs) are extracted from the article. **Timestep** (**fs**), **equilibration** and **production** **lengths** in **ps**–**ns**, and optional **NPT** / **Parrinello**–Rahman **barostat** use are in *Comput. Mater. Sci.* **N/A — external** **electric** **field**; **N/A — umbrella** in the main metal benchmark suite.

**2 — Force-field training.** The **ReaxFF** for **Ni/Cr** is **augmented** with **valence** **angle** (**three-body**) **terms**; the **parrex**-style **parameter** **fit** **optimi**zation **targets** **DFT** **reference** data (**elastic** **tensors** at 0 K, **stacking** **fault** **energies**, **equation-of-state**-type **reaction** subsets) and **experimental** **validation** for **melting**/**elastic** behavior. **EEM**-style **QEq** with a ~5 **Å** bond **cutoff** is discussed **versus** **EAM**-style **metal** **potentials** in the introduction.

**3 — Static QM (validation).** **DFT** supplies **0** **K** **elastic** data and **alloy** **formation** **energies** compared to the fitted **ReaxFF**; **C\(_{33}\)** shows a larger **benchmark** **error** in some cases.

**4 — Experiments.** **N/A** — the paper **compares** to **published** **experimental** **melting** and **elastic** **data** for **metals** from the literature, not a new **laboratory** program.
## Findings

- Three-body terms remove the unphysical C\(_{12}\)=C\(_{44}\) degeneracy and improve stacking-fault energetics for Ni relative to the prior ReaxFF treatment described.
- Predicted thermal expansion and melting temperatures align semiquantitatively with experiment under the hysteresis setups employed.
- Ni/Cr alloy energetics from ReaxFF follow the DFT trend favoring ordered fcc Ni\(_3\)Cr over disordered bcc mixtures in the tests shown.

**Comparisons and sensitivity.** **ReaxFF** is **compared** to **DFT** and **experimental** **elastic**/**melting** data; **temperature**-dependent **lattice** response and **hysteresis**-based **T\(_m\)** are central **levers**. **Corpus:** confirm **C\(_{33}\)** and any **NPT** usage in the full **PDF**.

## Limitations

Remaining discrepancies (e.g., C\(_{33}\)) and melting hysteresis sensitivity to simulation setup are discussed in the article.

## Relevance to group

Core ReaxFF metals methodology from the group extending transferable metal descriptions for alloy and corrosion workflows.

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2021.110602](https://doi.org/10.1016/j.commatsci.2021.110602)

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[reaxff-family]]
