---
id: paper:2015ong-venue-jp508184f
type: paper
title: "Lithium ion solvation and diffusion in bulk organic electrolytes from first-principles and classical reactive molecular dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - method:aimd
  - method:reaxff
  - method:dft-static
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:aimd
  - keyword:lammps
  - keyword:batteries-interfaces
  - keyword:nose-hoover
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/jp508184f"
year: 2015
authors:
  - "Mitchell T. Ong"
  - "Osvalds Verners"
  - "Erik W. Draeger"
  - "Adri C. T. van Duin"
  - "Vincenzo Lordi"
  - "John E. Pask"
venue: "Journal of Physical Chemistry B"
pdf_sha256: "b07e97b1a98381d160c9fedda0da6bcc53509ca41c25f9317f8f1637314de3be"
pdf_path: "papers/Ong_JPCB_IL_DFT_ReaxFF_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015ong-venue-jp508184f -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **J. Phys. Chem. B** article identified by `doi` and `pdf_path`. Quantitative **diffusion** and **coordination** values should be checked against the **full Methods/Results** in the PDF.

## Summary

**Born–Oppenheimer AIMD** (**VASP**, **PAW–PBE**, **Γ-only**, **450 eV**, **NVT** **Nosé–Hoover**, **0.5 fs**, **330 K**) characterizes **Li⁺**/**PF₆⁻** solvation and **diffusion** in **EC**, **EMC**, and **3:7 EC/EMC** at dilute **~0.23 M** salt conditions. **ReaxFF** (**LAMMPS**) extends selected electrolytes to **~1 ns** and **~6400 atoms** to probe **finite-size** and **sampling** effects versus **DFT** reference. The abstract emphasizes **tetrahedral** **Li⁺** first shells involving **carbonyl** and/or **ether** oxygens (sometimes **PF₆⁻** participation), **larger diffusivity** in **linear EMC** than **cyclic EC**, and weaker, poorly defined **PF₆⁻** first shells associated with higher anion mobility—motivating **electrolyte design** heuristics (abstract, extract).

## Methods

### Static QM / AIMD (primary)

**Born–Oppenheimer AIMD** in **VASP** with **PAW** potentials and the **PBE** GGA; **Γ-only** Brillouin sampling; **450 eV** plane-wave cutoff (as in the article’s Methods). **Born–Oppenheimer** propagation uses **NVT** **Nosé–Hoover** chains (**~1000 cm⁻¹** frequency, **~32 fs** period), **Δt = 0.5 fs**, **330 K**, with **~5–7.5 ps** equilibration followed by **~30 ps** production trajectories for **EC**, **EMC**, and **3:7 EC/EMC** electrolytes at dilute **~0.23 M** LiPF₆-like stoichiometry in **three-dimensional periodic boundary conditions (PBC)** cubic **supercells** (lattice vectors in **`pdf_path`**). **Analysis:** radial distribution functions, coordination numbers, residence times, and **Li⁺**/**PF₆⁻** diffusion coefficients from **VACF** and **MSD** treatments with **5–15 ps** averaging windows and **50 fs** time origins as reported.

### MD application (ReaxFF validation / scaling)

**LAMMPS** **ReaxFF** runs use **NVT** with a **Nosé–Hoover chain** thermostat (**three** chains), **Δt = 0.25 fs**, **~1333 cm⁻¹** chain frequency; an illustrative **EC** cell (**630 EC + 10 LiPF₆** formula units) uses **~125 ps** equilibration plus **~1 ns** production at **330 K** to probe finite-size and sampling effects relative to AIMD, likewise under **3D PBC** with box vectors reported in the article.

### Force-field training

**N/A —** this work **uses** a published **organic electrolyte** ReaxFF parametrization for comparison to AIMD; it is not primarily a new ReaxFF fitting paper.

Bulk **AIMD** and **ReaxFF** validation trajectories are **constant-volume** (**NVT**); **barostat / applied pressure**, **electric fields**, and **umbrella-style enhanced sampling** are **not** part of the protocols summarized above.

## Findings

**Solvation:** **Li⁺** is coordinated in roughly **tetrahedral** fashion by **carbonyl** and/or **ether** oxygens of the carbonates and sometimes by **PF₆⁻**, with preferred motifs depending on **EC** vs **EMC** vs mixture. **Diffusion:** **Li⁺** **diffusivity** is somewhat **larger in EMC than in EC** in the authors’ calculations; magnitude tracks **strength of Li⁺ solvation** in their analysis. **PF₆⁻** shows **higher diffusivity** when its first solvation shell is **weakly bound / poorly defined**. **Model comparison:** **ReaxFF** reproduces many **Li⁺–O** coordination features versus **AIMD** but can differ in **ether-oxygen** angular/PCF detail; reported **diffusion coefficients** for ReaxFF vs AIMD agree within roughly **40–50%** in the cases highlighted—used to argue for **ReaxFF** as a **scalable** complement while noting **DFT** finite-size limits.

## Limitations

**Dilute** salt vs commercial concentrations; **PBE** electrolyte chemistry; **ReaxFF** organics parametrization limits for subtle **EC/EMC** ether conformations.

## Relevance to group

**Adri C. T. van Duin** co-authorship; couples **AIMD** electrolyte benchmarks with **ReaxFF** **scaling** arguments.

## Citations and evidence anchors

DOI `10.1021/jp508184f`.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
