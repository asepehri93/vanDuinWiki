---
id: paper:2021mike-pols-j-phys-chem-atomistic-insights
type: paper
title: "Atomistic insights into the degradation of inorganic halide perovskite CsPbI3: A reactive force field molecular dynamics study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - material:widegap-semiconductor
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.1c01192"
year: 2021
authors:
  - "Mike Pols"
  - "José Manuel Vicent-Luna"
  - "Ivo Filot"
  - "Adri C. T. van Duin"
  - "Shuxia Tao"
venue: "J. Phys. Chem. Lett. 2021, 12, 5519–5525"
pdf_sha256: "4856dc1329e7a8639a8aeb602283448879d41f8e1519979d40977ba7b482ffde"
pdf_path: "papers/Pols_JPC_Letters_CsPbI3_perovskites.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021mike-pols-j-phys-chem-atomistic-insights -->

## Summary

A **ReaxFF** parameter set for **inorganic CsPbI\(_3\)** is fitted to **DFT (PBE + DFT-D3(BJ))** reference data computed in **VASP**, including equations of state, charges, formation energies, and defect energetics/migration for perovskite phases and precursors (CsI, PbI\(_2\)). Monte Carlo force-field optimization in **AMS 2020** starts from literature **Cs/I electrolyte-water** parameters and **Pb parameters adapted from Pt** (Fantauzzi *et al.*). The letter then applies ReaxFF MD to **phase stability versus temperature** and to **defective cells**, showing anharmonic lattice fluctuations drive phase behavior and that **iodine vacancies** seed Frenkel defects and Pb–I cluster formation leading to **PbI\(_2\)**-like decomposition.

Opening motivation ties metal-halide perovskite deployment to unresolved environmental stability: moisture, heat, and illumination can trigger phase segregation and lead-halide precipitation, so atomistic reactive MD on **CsPbI\(_3\)** with explicit vacancies links iodine transport to decomposition microstructures at elevated temperature.


## Methods

**Force-field training (ReaxFF for Cs–Pb–I).** Reference data are from **DFT** with **PBE + DFT-D3(BJ)** in **VASP** (see SI Supporting Notes 1–3 for convergence and supercells). The training set covers perovskite-related phases and precursors (including **CsI** and **PbI\(_2\)**) with **equations of state**, **atomic charges**, **formation energies**, and **defect** formation and **migration** barriers. Optimization uses the **Monte Carlo**-based ReaxFF optimizer in **AMS 2020**; the starting point combines **Cs/I** ReaxFF parameters from Fedkin *et al.* (electrolyte–water set) and **Pb**-like parameters adapted from **Pt** (Fantauzzi *et al.*), then adjusted for Pb. Optimized parameters are in the **Supporting Information**.

**MD application (ReaxFF molecular dynamics in AMS 2020).** All **ReaxFF** **molecular dynamics** in the study is run in **AMS 2020** with the **fitted** **potential** (SI gives **full** **integration** and **cell** **settings**). The letter uses these runs for: (i) **bulk** **CsPbI\(_3\)** **phase** **stability** vs **T** on a **~100–700** **K** **grid**; (ii) **NPT** **@ 1** **atm** **self**-**diffusion** of **I** **vacancies** and **I** **interstitials** at **450–700** **K** (Supporting **Note 2**); and (iii) **600 K** dynamics of **iodine-vacancy**-enriched supercells (doping order **~3×10\(^{19}\)** **cm\(^{-3}\)** in the letter). **3D** **PBC** **perovskite** **supercells**; **system** **size**, **time step (fs)**, **equilibration vs production (ps–ns)**, **thermostat**/**barostat** **tuning**, and **Ewald/QEq** **details** are in the **letter**+**SI** (not re-copied here). **External** **E-field, shear, metadynamics — N/A** in these **runs**. **Barostat** — **NPT** for the **1** **atm** **defect**-**diffusion** **block**; other **segments** as **tabulated** in the **SI**.

## Findings

**Outcomes and mechanisms.** **Phase behavior:** the letter attributes **phase instability** in part to anharmonic lattice motion and **Cs** displacement from preferred sites at low **T**, favoring conversion toward a **non-perovskite** (yellow) phase, while at higher **T** the dynamics are more isotropic. **Defects:** both **I vacancies** and **I interstitials** are **mobile**; the authors report Arrhenius-like diffusion with activation energies of order **~0.19 eV (vacancy)** and **~0.28 eV (interstitial)** in the temperature ranges quoted. **Vacancy-assisted decomposition:** I vacancies are argued to be especially **detrimental**—they promote local restructuring (edge-sharing octahedral motifs, **Pb\(_x\)I\(_y\)** clusters) that can evolve toward **PbI\(_2\)**, whereas other **vacancy types** may remain stable to higher temperatures before decomposing.

**Comparisons (model vs DFT).** The fitted ReaxFF matches **bulk EOS**, formation energetics, and key **defect/migration** quantities vs the **PBE+D3** training data; a highlighted check is the **octahedral tilting** barrier (~**0.14 eV** ReaxFF vs **0.17 eV** DFT in the main text).

**Sensitivity.** Phase metrics and **diffusivities** are tracked as functions of **temperature** and **defect loading**; readers should use the main text + SI for exact run conditions when transferring numbers.

## Limitations

ReaxFF accuracy is bounded by the DFT rung and training set; explicit device interfaces (contacts, moisture) are outside this parameterization.

## Relevance to group

First **ReaxFF** line for **all-inorganic halide perovskite** stability with **van Duin** co-authorship.

## Citations and evidence anchors

- J. Phys. Chem. Lett. **12**, 5519–5525 (2021); SI for parameters and diffusion analysis.

## Related topics

- [[reaxff-family]]
