---
id: paper:2015islam-venue-paper
type: paper
title: "Mechanical properties of stanene under uniaxial and biaxial loading: a molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:classical-md
  - task:application
  - scale:atomistic
  - material:widegap-semiconductor
source_refs: []
doi: "10.1063/1.4931572"
year: 2015
authors:
  - "Satyajit Mojumder"
  - "Abdullah Al Amin"
  - "Md Mahbubul Islam"
venue: "Journal of Applied Physics 118, 124305 (2015)"
pdf_sha256: "4bf00387d9f3c0628b14877aad4550c9ff8e8250511e2139f3b986f873d201cc"
pdf_path: "papers/Islam_Stanene_APL2015.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2015islam-venue-paper -->

## Summary

Mojumder, Al Amin, and Islam report **classical molecular dynamics** of **α-stanene** mechanics using a **modified embedded-atom method (MEAM)** potential for **Sn** (**not ReaxFF**). They apply **uniaxial** tension along **armchair** and **zigzag** directions and **equibiaxial** tension, scanning **temperature** (**100–250 K** in the Methods text) and **strain rate** (**10⁶–10⁹ s⁻¹**). The **J. Appl. Phys.** abstract summarizes **lower fracture strength and strain with increasing temperature**, **higher** ultimate properties for **zigzag** than **armchair** uniaxial loading, **near-isotropic** response under **biaxial** loading, and **higher** strength/strain at **higher** strain rates—motivated as context for **mechanically tunable** **2D Sn** electronics proposals.

## Methods

**MD application — potential, code, and model geometry.** **MEAM** interactions for **tin** are used with parameters tabulated in **Table I** of the paper. Simulations are executed in **LAMMPS**. The **stanene** sheet is **~20.50 nm × 20.50 nm** (**4032 Sn** atoms) with **armchair along +x** and **zigzag along +y**; **in-plane PBC** applies in **x** and **y**, while **z** is **non-periodic** with free surfaces.

**Equilibration and ensembles.** After **conjugate-gradient** relaxation of the buckled sheet, the protocol performs **10 ps** in the **NVE** ensemble, followed by **50 ps** of **NPT** equilibration at **1 atm** and the target **temperature** to relax residual stresses, then **deformation** simulations under the **uniaxial / biaxial strain** protocols described in the article.

**Timestep, thermostat/barostat, loading.** An MD **timestep of 1.0 fs** is used throughout. **Uniaxial** tests strain along **x** or **y** at prescribed **constant strain rates**; **biaxial** tests strain **x** and **y** simultaneously. **Virial stress** is accumulated with the averaging window described in the paper.

**Force-field training / reactive chemistry.** **N/A —** **MEAM** parameters are taken from the cited **MEAM** development for **Sn**; no **ReaxFF** refit is performed.

**Electric fields, replica sampling.** **N/A —** not used.

## Findings

**Anisotropy and loading mode.** **Uniaxial zigzag** loading yields **higher** fracture strength/strain than **uniaxial armchair** loading in the reported curves; **equibiaxial** loading shows **much smaller** directional contrast, consistent with the abstract’s summary.

**Temperature and rate sensitivity.** Fracture metrics **decrease** with increasing **temperature** and **increase** with increasing **strain rate** over the ranges simulated.

**Comparisons.** The relaxed sheet exhibits **out-of-plane buckling** (~**1.02 Å** height in the article) consistent with prior **MEAM**/**DFT** literature cited therein; detailed numerical tables and stress–strain plots should be read from the **J. Appl. Phys.** PDF.

## Limitations

- **MEAM** accuracy depends on the fitted **Sn** database; **reactive** chemistry (**oxidation**) of **Sn** surfaces is outside the classical potential’s intended scope unless reparameterized.
- AIP download banner text appears in some extracts; article id **124305** appears in bibliographic headers.

## Relevance to group

**Md Mahbubul Islam** (Penn State affiliation in extract) connects the entry to the host group’s broader **2D materials MD** portfolio, even though this specific manuscript is **not a ReaxFF paper**.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1063/1.4931572](https://doi.org/10.1063/1.4931572)

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

This entry documents **MEAM** **stanene** mechanics; for **reactive** **Sn** **oxidation** or **electronic** **structure** of **defects**, use **DFT** or **ReaxFF** pages tagged for **tin** **surfaces** instead of extrapolating **MEAM** **fracture** data.
