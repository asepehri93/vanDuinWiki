---
id: paper:2016pathak-physical-che-reactive-force
type: paper
title: "Reactive force field development for magnesium chloride hydrates and its application for seasonal heat storage"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - material:oxide
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:monte-carlo-sampling
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1039/C6CP02762H"
year: 2016
authors:
  - "Amar Deep Pathak"
  - "Silvia Nedea"
  - "Adri C. T. van Duin"
  - "Herbert Zondag"
  - "Camilo Rindt"
  - "David Smeulders"
venue: "Phys. Chem. Chem. Phys. 2016, 18, 15838-15847"
pdf_sha256: "3cbfecd5f50008b7f04731235d8ed5f990de9d934c3fe85703118bdf3178d06e"
pdf_path: "papers/Pathak_Nedea_MgCl2_hydrates_PCCP_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016pathak-physical-che-reactive-force -->

## Summary

Magnesium chloride hydrates are candidates for seasonal thermochemical heat storage: charging by dehydration and discharging by hydration, with hydrolysis as an irreversible side reaction that releases HCl and harms hardware. Changing hydrate stoichiometry alters water connectivity, so kinetic differences between monohydrate and dodecahydrate are not only shifts in equilibrium vapor pressure. Pathak, Nedea, van Duin, Zondag, Rindt, and Smeulders derive a ReaxFF description for MgCl\(_2\)·H\(_2\)O and MgCl\(_2\)·12H\(_2\)O from DFT bond and angle scans, reaction enthalpies, and equations of state, using a single-parameter search combined with Metropolis Monte Carlo moves in parameter space. Reactive MD on two-dimensionally periodic slabs from 300–500 K probes dehydration rates, Arrhenius trends for water diffusion, and HCl formation, contrasting transport-limited and reaction-limited regimes between the two hydrates.

## Methods

**Force-field training.** DFT reference data cover Mg–Cl, O–H, and HCl-related motifs needed for proton transfer and hydrolysis. The optimization alternates deterministic single-parameter moves with Metropolis Monte Carlo acceptance in parameter space to escape poor local minima. Validation includes lattice parameters, elastic data, and equations of state tabulated against DFT (Table 1 and related figures in *Phys. Chem. Chem. Phys.* **18**, 15838–15847), plus the proton-transfer motif used for hydrolysis: ReaxFF reports a barrier of **20.24 kcal mol\(^{-1}\)** for MgCl\(_2\)·12H\(_2\)O compared with **19.55 kcal mol\(^{-1}\)** from DFT for the same pathway.

**MD application.** Reactive MD uses **two-dimensional periodic slabs** built from experimental CIF-derived supercells by removing periodicity along one axis chosen parallel to the weaker **Mg–O** direction: **26.8 × 21.8 × 1000 Å** for MgCl\(_2\)·H\(_2\)O and **44.3 × 1000 × 21.9 Å** for MgCl\(_2\)·12H\(_2\)O (Section 3.3). **NVT** trajectories use a **Berendsen** thermostat with a **100 fs** damping constant and an integration **timestep of 0.25 fs**. Each production segment runs **up to 1 ns**, with reported averages taken from the **last 500 ps**. Temperatures **300, 350, 400, 450, and 500 K** bracket the dehydration and water-diffusion analysis; hydrolysis kinetics for the monohydrate are illustrated at **340 K** in the published figures. **N/A — barostat** — constant-volume **NVT** sampling without hydrostatic pressure control. **N/A — MD engine name** — not stated in the PCCP body text extracted here. **N/A — applied electric field; umbrella / metadynamics / replica exchange** — not used for production hydrates trajectories (Metropolis Monte Carlo appears only in the parameter-fitting workflow).

**Static QM / DFT.** VASP PAW/PBE benchmarks supply training curves, elastic properties, and the DFT proton-transfer barrier used to judge the reactive field.
## Findings

ReaxFF bulk moduli align with DFT for both hydrates, supporting coupled mechanical and reactive use of the field. Dehydration accelerates more steeply with temperature for MgCl\(_2\)·H\(_2\)O than for MgCl\(_2\)·12H\(_2\)O in the window studied, consistent with different water connectivity. HCl appears near **340 K** for the monohydrate—in line with experiment—while the dodecahydrate trajectories reported do not show HCl under the same conditions, indicating phase-selective hydrolysis risk. Water diffusion is slower through the monohydrate, so transport can co-limit dehydration even when thermodynamics favor water release; tabulated **H\(_2\)O** diffusivities versus temperature follow Arrhenius trends with parameters given in the paper’s tables. The authors position the model for seasonal heat-storage design: reproducing HCl onset against calorimetric data matters more than gas-phase chlorine chemistry alone. Porting to mixed salts or eutectics outside the training set, and rare-event statistics near hydrolysis onset, still require the article’s sensitivity discussion and longer replicate runs where the paper recommends them.

## Limitations

Reactive MD cannot capture all gas-phase chemistry at reactor scales; continuum transport and reactor geometry remain outside the model.

## Relevance to group

van Duin-coauthored ReaxFF parametrization for salt hydrates with explicit validation against DFT and targeted experiments.

## Citations and evidence anchors

- DOI: [10.1039/C6CP02762H](https://doi.org/10.1039/C6CP02762H)

## Related topics

- [[reaxff-family]]
