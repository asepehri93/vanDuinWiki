---
id: paper:2018rismiller-fuel-215-201-water-assisted
type: paper
title: Water assisted liquefaction of lignocellulose biomass by ReaxFF based molecular
  dynamic simulations
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:organics-polymers-pyrolysis
- domain:reactive-md
- material:polymer-organic
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:thermal-decomposition
- keyword:reaxff-application
- keyword:lammps
- keyword:nvt-simulation
- keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: 10.1016/j.fuel.2017.11.108
year: 2018
authors:
- Sean C. Rismiller
- Melinda M. Groves
- Min Meng
- Yuan Dong
- Jian Lin
venue: Fuel
pdf_sha256: 0b5a14c29a8d05d653f9558ac9372571ba3fc783b889dac00032f7b37a2b532e
pdf_path: papers/ReaxFF_others/Rismiller_Fuel_2018_lignocellulose.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018rismiller-fuel-215-201-water-assisted -->

## Summary

**ReaxFF** **MD** in **LAMMPS** simulates **pyrolysis/liquefaction** of **cellulose** and **lignin** models with **0**, **33 wt%**, and **66 wt%** **water** at **1250–2000 K** over **6 ns**, characterizing **product** **phases**, **elemental** **ratios**, **higher heating value** proxies, and **time evolution** of **water** and **organics**. The study separates **cellulosic** and **lignin** fractions to compare how **water** couples to **depolymerization** versus **condensation** chemistry in **lignocellulosic** biomass models. **Elevated** **temperatures** and **nanosecond** trajectories are used to access **reactive** events within classical **MD** budgets, with explicit acknowledgment that this is an **accelerated** window relative to **laboratory** **pyrolysis** timescales.

## Methods
**1 — MD application (lignocellulose pyrolysis/liquefaction).** **ReaxFF** (**lignocellulose** parametrization as cited) is implemented in **LAMMPS**. **Models:** **eight** **β-phase cellulose** chains (**10** glucose units each) from **Cellulose Builder** plus **six-molecule Adler lignin** bundles; **partial charges** pre-calibrated with **VASP** inside **Materials Studio** before switching to **ReaxFF**. **System size:** combined **cellulose + lignin + water** supercells reach **~10³–10⁴ atoms** once solvated at the quoted loadings (exact counts in *Fuel* tables). **Water loadings:** **0, 33, and 66 wt %** water. **Protocol:** **NPT annealing/equilibration** at **1 atm** and **300 K** to reach stable densities, then **NVT** production at the **NPT-relaxed** cell volume; **production** segments extend to **6 ns** per reported high-temperature window with **0.25 fs** timestep (article emphasizes longer trajectories than earlier **250 ps** literature comparisons). **Temperatures:** **1250–2000 K** reactive windows. **Thermostat:** temperature control during **NPT**/**NVT** stages follows the **thermostat** prescription in *Fuel* **Methods** (see PDF for damping constants). **PBC:** **three-dimensional PBC** for bulk biomass boxes. **Electric fields / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** applies a published **lignocellulose ReaxFF** parameterization.

**3 — Static QM.** **N/A —** beyond **VASP** charge preparation noted above.

## Findings
**Outcomes / mechanisms:** **Water** accelerates **cellulose** breakdown, increases **oxygenation** of products, and shifts products from **char** toward more **oil-like** fractions versus **dry cellulose** in these runs. **Lignin** chemistry is comparatively **insensitive** to **water** loading in the simulated window, consistent with experimental **char**-leaning **lignin liquefaction** behavior discussed by the authors.

**Comparisons:** trends are discussed relative to **dry vs hydrated** runs across the **1250–2000 K** sweep.

**Sensitivity:** higher **temperature** diminishes the **oxygenating** role of **water** on **cellulose** within the modeled kinetics.

**Limitations:** **high-T**, **nanosecond** MD accelerates chemistry versus reactors; product lumping follows simulation-specific definitions in **Fuel**.

**Corpus honesty:** protocol elements follow **`papers/ReaxFF_others/Rismiller_Fuel_2018_lignocellulose.pdf`**; confirm numerical cutoffs in the **article**.

## Limitations

High-temperature, short-time MD exaggerates kinetics versus laboratory pyrolysis/liquefaction; product quantification is simulation-limited and model-dependent. **Yield** classifications (**oil**/**char**/**gas**) follow simulation-specific **cutoffs** that should be copied from the **Fuel** article when reproducing **trends**, not inferred from this wiki alone.

## Relevance to group

Shows **ReaxFF** application to **biomass** conversion chemistry. The **Fuel** article complements other **lignocellulose** **pyrolysis** entries in the corpus by isolating **water** **loading** as an explicit variable while holding **cellulose** and **lignin** **models** fixed across **temperature** sweeps.

## Citations and evidence anchors

- DOI: [10.1016/j.fuel.2017.11.108](https://doi.org/10.1016/j.fuel.2017.11.108)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
