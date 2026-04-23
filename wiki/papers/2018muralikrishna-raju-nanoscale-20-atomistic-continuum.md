---
id: paper:2018muralikrishna-raju-nanoscale-20-atomistic-continuum
type: paper
title: Atomistic and continuum scale modeling of functionalized graphyne membranes
  for water desalination
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:water-silica-geo
- material:graphene-carbon-nano
- domain:reactive-md
- method:reaxff
- method:continuum-or-mesoscale
- task:application
- scale:multiscale
candidate_tags: []
source_refs: []
doi: 10.1039/c7nr07963j
year: 2018
authors:
- Muralikrishna Raju
- Pavan B. Govindaraju
- Adri C. T. van Duin
- Matthias Ihme
venue: Nanoscale
pdf_sha256: 9dd462ce05d18bbde5d613ca28d9d6b74376f7bf9367f70f1d73905c52dc3c4d
pdf_path: papers/Raju_Nanoscale_2018.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018muralikrishna-raju-nanoscale-20-atomistic-continuum -->

## Summary

This **Nanoscale** article evaluates **α-** and **γ-graphyne** membranes—bare and **hydrogenated**, with varied **pore chemistry** and **geometry**—as **desalination** candidates using **ReaxFF reactive molecular dynamics** in **LAMMPS** for **atomistic transport** metrics and **continuum-scale** analysis for **cross-flow reverse-osmosis** device context. **MD** predicts extremely high **intrinsic water permeability** and strong **ion rejection** for certain **pore sizes**, while the **continuum upscaling** argues that **module-level transport limitations** partially blunt the **MD-only** advantage—yet still project **meaningful energy / recovery** improvements versus **thin-film composite** benchmarks under stated assumptions. **Adri C. T. van Duin** is a coauthor on the **atomistic** modeling thread. The paper’s **multiscale** message is that **pore-scale** **permeability** must be read together with **pressure drop** and **concentration polarization** in a **module**, not as a standalone **MD** headline.

## Methods
**1 — MD application (membrane permeation).** All atomistic simulations were run with **LAMMPS** as stated in *Nanoscale* (`papers/Raju_Nanoscale_2018.pdf`). The authors build **nanoporous α- and γ-graphyne** membranes (bare and **hydrogenated**) in **three-dimensional periodic boundary conditions (PBC)** with explicit **water** and **ions**; supercell sizes and stoichiometries follow their membrane construction tables and figures. After **10 000-step** energy minimization, cells are equilibrated in the **isotropic NPT** ensemble for **250 ps** at **1 atm** and **313 K** using a **Nosé–Hoover** thermostat (**10 fs** coupling) and **Nosé–Hoover** barostat (**100 fs** coupling). Production **nonequilibrium permeation** runs use the **NVT** ensemble for **250 ps** at **313 K** with a **0.10 fs** timestep while applying controlled **normal pressures** along the permeation axis in the **100–2500 MPa** range reported in the article. **Electric fields:** **N/A —** not used. **Replica / enhanced sampling:** umbrella / metadynamics workflows implemented with **PLUMED** (called from **LAMMPS**) are used for selected **permeation free-energy** analyses as reported in the article (separate from the main throughput/rejection MD trajectories).

**2 — Continuum / process modeling.** A **cross-flow reverse-osmosis** module model upscales MD-derived permeabilities to engineering metrics (permeate recovery, energy) including **pressure drop** and **concentration polarization**; model equations and parameters are documented in the article and **ESI**.

**3 — Force-field training.** **N/A —** the study applies published **ReaxFF** parameter sets for **C/O/H** graphyne and water (with **K/Cl** extensions for saline environments) with validation against selected **DFT** references in the article, rather than reporting a new ReaxFF optimization campaign.

**4 — Static QM / AIMD.** **N/A —** central claims are **ReaxFF MD** plus continuum analysis rather than AIMD production runs.

## Findings
The **MD** portion reports **>90 % ion rejection** for **pore areas ~20–50 Å²** under applied pressures up to **~1 GPa**, with intrinsic **water permeabilities** reaching up to **~85 L·cm⁻²·day⁻¹·MPa⁻¹**—orders of magnitude above commercial **thin-film composite (TFC)** **RO** membranes and substantially above **nanoporous graphene** benchmarks quoted in the abstract. **Mechanistically**, the paper ties flux and selectivity to **in-pore water velocity**, **density**, and **ion energy barriers** as a function of **pore chemistry**, **hydrogenation**, and **geometry**.

**Comparisons versus engineering baselines:** the **continuum upscaling** shows that **module-level transport** (recovery, polarization, hydraulic losses) **dilutes** the raw MD permeability advantage, yet still projects up to **~6× higher permeate recovery** or **~6 % lower energy** than **TFC** references under the stated operating assumptions.

**Sensitivity / design levers:** performance depends strongly on **pore area**, **functionalization**, and **applied pressure**; the continuum section further shows how **feed-flow** and **packing** assumptions move the headline MD benefit.

**Limitations / outlook (authored framing):** the article itself stresses that **graphyne manufacturability** and **real module hydraulics** remain open challenges beyond the simulation scope.

**Corpus / PDF honesty:** numerical permeabilities, rejection thresholds, and RO upscaling factors above are taken from the **abstract and main-text scaling discussion** on `pdf_path`; reproduce **exact** values from the **PDF**/**ESI** when citing outside this wiki.

## Limitations

- **Classical force fields** for **graphyne–water–ion** systems have **uncertainty** near **sub-nm** pores; **quantitative** barriers benefit from **QM spot checks**.
- **Manufacturability** of **graphyne** remains a **materials synthesis** challenge outside the simulation scope.

## Relevance to group

Shows **van Duin-group participation** in **2D nanoporous carbon** **water** modeling coupled to **engineering-scale** interpretation.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1039/c7nr07963j` (`papers/Raju_Nanoscale_2018.pdf`).

## Related topics

- [[graphene-nanocarbon]]
- [[theme-water-silica-geo]]
