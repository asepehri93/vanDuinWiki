---
id: paper:2021morrow-energy-fuels-evaluating-ability
type: paper
title: "Evaluating the ability of selected force fields to simulate hydrocarbons as a function of temperature and pressure using molecular dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:classical-ff-specialized
  - method:classical-md
  - method:reaxff
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:classical-ff
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.energyfuels.0c03363"
year: 2021
authors:
  - "Brian H. Morrow"
  - "Judith A. Harrison"
venue: "Energy Fuels (2021); DOI 10.1021/acs.energyfuels.0c03363"
pdf_sha256: "67efdf673aa84d861010286912a6c001de4f0973d7859b54794b2d0944247036"
pdf_path: "papers/ReaxFF_others/Morrow_Harrison_Hydrocarbons_AIREBO_ReaxFF_OPLS.energyfuels_2021.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2021morrow-energy-fuels-evaluating-ability -->

## Summary

**OPLS-AA**, **AIREBO-M**, and **ReaxFF (CHON-2017_weak)** are benchmarked for **pure liquid hydrocarbons**—**trans-decalin**, **n-hexadecane**, **isocetane**, and **tetralin**—across **293.15–373.15 K** at **0.1 MPa** and pressures **0.1–40 MPa** at **313.15 K**. The paper’s aim is to quantify when a reactive hydrocarbon FF can double as an accurate liquid-state EOS model for fuels work. **OPLS-AA** best reproduces **densities**; **ReaxFF** is slightly better for **isentropic bulk modulus**; **AIREBO-M** is least accurate for both. Structural diagnostics (RDFs, ARDFs, radius of gyration for n-hexadecane, ring puckering for tetralin) highlight conformational biases, especially **tetralin π-stacking** propensity in AIREBO-M/ReaxFF vs OPLS-AA.

## Methods

**MD application (classical liquid benchmarks in LAMMPS).** **LAMMPS** is used to simulate **neat liquid hydrocarbons** — **trans-decalin**, **n-hexadecane**, **isocetane**, and **tetralin** — in **NPT** with **3D PBC** for the bulk liquids. The study sweeps **temperature** **293.15–373.15 K** at **0.1 MPa** and, separately, **pressure** **0.1–40 MPa** at **313.15 K** (as stated in the abstract/Introduction). **Timestep: 0.25 fs**; **AIREBO-M** and **ReaxFF** use **unconstrained** (non-**SHAKE**d) C–H dynamics with parameters documented in the paper/SI, while **OPLS-AA** follow SI Tables S1–S4. **Ensemble: NPT**; each **NPT** segment couples a **Nosé**–**Hoover**-style or **Berendsen**-style **thermostat** with an **isotropic** **Parrinello**–**Rahman**/**barostat** (or equivalent) for **hydrostatic** **pressure** control as in the Energy & Fuels methods. **Equilibration + production** staging — follow article/SI; **N/A** here to paste every run length. **System size** — on the order of a few **thousand** atoms (SI); exact counts in `pdf_path`. **Electric field, shear, impact, replica/enhanced sampling: N/A**. **Electrostatics** — as defined by each potential: **OPLS** **long-range** **Coulomb**; **AIREBO/ReaxFF** per their respective LAMMPS pair styles.

**Potentials compared.** (1) **OPLS-AA/AMBER**-family parameters for the listed fluids; (2) **AIREBO-M** via the **`ch.airebo-m`** file packaged with LAMMPS; (3) **ReaxFF** with **CHON-2017_weak** parameters from the cited 2020 *Energy & Fuels* work (ref. 20, SI in that paper; parameters reproduced in this work’s **SI**).

**Thermodynamic observables** — **mass density**, **isothermal** bulk **modulus** from fluctuation relations (eqs. 2–4) and the **isentropic** modulus from eq. (1); **RDF**/**ARDF** center-of-mass, **radius of gyration** for n-hexadecane, and **puckering** metrics for **tetralin**.

**Force-field training and standalone DFT. N/A** — the paper is **benchmark/validation** of **published** **parameter** sets, not a new ReaxFF fit. **N/A** — no **ab initio** **production** DFT in the benchmark table **unless** the article cites a separate subset (not the focus of this work).

## Findings

**Comparisons vs experiment.** For **mass density**, **OPLS-AA** is overall most accurate in RMSE/MAE vs experiment across the conditions tested; **ReaxFF** shows systematic **overdensity** in some **aromatic** and **branched** cases; **AIREBO-M** is the least accurate in density. For **isentropic** bulk **modulus**, **ReaxFF** marginally outperforms **OPLS-AA** on the chosen metrics; **AIREBO-M** is worst. **N/A** in this short summary to reproduce every table entry — use the article.

**Structure.** **RDF/ARDF** and **R\(_g\)** diagnostics show conformational biases: e.g. **tetralin** shows stronger **π**–**stacking**-like order in **AIREBO-M/ReaxFF** than in **OPLS-AA**; **n-hexadecane** can appear **more coiled** in **ReaxFF** compared with **OPLS-AA**/**AIREBO** extended-chain sampling. The authors stress that good **thermodynamic** **averages** can hide **defects** in **local** **liquid** **structure**—check **RDFs** and **R\(_g\)** alongside **ρ** and **B**.

**Practical levers (as explored).** Sensitivity to **T** and **P** in the **NPT** **grids** above; **N/A** — the paper does not claim **reactive** **pyrolysis** in these **nonreactive** liquid **benchmarks**.

## Limitations

Reactive potentials are not exhaustively validated for pyrolysis/combustion here—the focus is **non-reactive** liquid thermophysics. Cross-comparisons use **RMS**/**MAE** metrics reported in the article against **experimental** **densities** and **bulk moduli**; readers extending the benchmark to additional **hydrocarbons** should repeat the same **NPT** **equilibration** and **fluctuation** formulas so **B\(_T\)** and **B\(_S\)** remain comparable across potentials.

## Relevance to group

Head-to-head **ReaxFF vs OPLS** benchmarking for hydrocarbon **fuels** properties relevant to classical/reactive MD method choice.

## Citations and evidence anchors

- Energy Fuels **35**, 5123–5139 (2021); Section 2 (methods) and Section 3 (results).

## Reader notes (navigation)

- Benchmark paper for **CHON-2017_weak** liquid hydrocarbons; ties to [[theme-pyrolysis-combustion-organics]] and [[2020kwon-fuel-279-202-reaxff-based-molecular]] (pyrolysis applications).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
- [[2020kwon-fuel-279-202-reaxff-based-molecular]]
