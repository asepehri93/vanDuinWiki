---
id: paper:2018ashraf-fuel-235-201-pyrolysis-binary
type: paper
title: "Pyrolysis of binary fuel mixtures at supercritical conditions: A ReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2018.07.077"
year: 2018
authors:
  - "Chowdhury Ashraf"
  - "Sharmin Shabnam"
  - "Abhishek Jain"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Fuel 235 (2018) 194–207"
pdf_sha256: "f6e0cac3c7eb0cf6be258ea4e3431cf6f2b7fd1eb924ee23c9c11525e954c89d"
pdf_path: "papers/Ashraf_Shabnam_Fuel_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018ashraf-fuel-235-201-pyrolysis-binary -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Supercritical pressures in propulsion/combustion hardware invalidate low-P Arrhenius kinetic models that neglect pressure effects on pathways. This work uses ReaxFF MD to study **binary fuel pyrolysis** at supercritical conditions for JP-10/toluene and n-dodecane/toluene mixtures, comparing to detailed continuum chemistry where the continuum model fails to capture atomistic trends. Mixing ratio and density change cooperative decomposition: a more reactive component can accelerate breakdown of a less reactive partner beyond naive “fastest reaction dominates” intuition; pyrolysis products from one species can promote chemistry in others. The study maps regimes where first-order kinetics and simple Arrhenius behavior break down. **Rocket** **injector** and **diesel** **relevant** **fluids** often exist as **multicomponent** **liquids** at **elevated** **P**; the paper uses **mixtures** to expose **synergistic** **cracking** that **single-fuel** **models** omit.

## Methods

### Force-field lineage (ReaxFF, CHO-2016)

The study uses the **CHO-2016** combustion **ReaxFF** parameterization of **Ashraf** *et al.* (reference **[42]** in *Fuel*), developed as an update to **CHO-2008** (**Chenoweth** *et al.*) to improve **C1** chemistry and hydrocarbon mechanical properties. **Nonbonded** interactions taper to zero by **10 Å** as summarized in §2, with **EEM**-based charge equilibration consistent with standard **ReaxFF** practice.

### MD application — supercritical binary pyrolysis

**Engine / code.** **Reactive molecular dynamics** with **ReaxFF** follows the **Penn State** **pyrolysis** protocol of prior **ReaxFF** studies **[41,42]** (implementation details align with the **LAMMPS** workflows documented on **`[[2018ashraf-venue-paper]]`**).

**System size and composition.** Single-component benchmarks place **40** molecules of **n-dodecane**, **JP-10**, or **toluene** in **cubic** cells sized to **\(\rho = 0.2\)** and **\(0.4\ \mathrm{kg\,dm^{-3}}\)**. **Binary** sweeps fix **40 toluene** molecules and vary the co-reactant count to realize mixing ratios **\(\alpha\)** from **0.025** to **1.0**; **Table 1** lists **total atom** counts up to **2120** (**n-dodecane/toluene**) and **1640** (**JP-10/toluene**) at the highest loading.

**Boundaries / periodicity.** **Bulk liquid** cells are **cubic boxes** with **three-dimensional periodic boundary conditions** (**PBC**) as in **[41,42]**.

**Ensemble.** All production trajectories use **constant-volume** **NVT** MD.

**Timestep.** **\(\Delta t = 0.1\ \mathrm{fs}\)**.

**Duration / stages.** After energy minimization, systems are **equilibrated** with **NVT** MD at **1500 K** for **10 ps** (no pyrolysis during this window). **Ten** independent samples then undergo **NVT** **production** runs at **2000–2600 K** (**100 K** steps). **n-Dodecane**/**JP-10**-rich cases use **50 ps** production; **toluene**-rich and **mixture** cases use **200 ps** to accumulate sufficient **toluene** decomposition statistics (**§3**).

**Thermostat.** **Berendsen** thermostat with **100 fs** damping constant (**§3**).

**Barostat.** **N/A —** the protocol fixes **volume** and **diagnoses** **pressure** from the **NVT** state; **no** **NPT** **barostat** coupling is used in the **MD** stages described.

**Temperature.** **1500 K** equilibration; **2000–2600 K** production grid (**Table 1**).

**Pressure.** **Instantaneous pressures** at **0.2** and **\(0.4\ \mathrm{kg\,dm^{-3}}\)** reach **tens to hundreds of MPa** at **2000–2600 K** (tabulated **\(P,T,Z\)** in *Fuel*).

**Electric field.** **N/A —** no applied field.

**Replica / enhanced sampling.** **N/A —** brute-force **NVT** trajectories.

### Continuum reference (0D detailed chemistry)

**Zero-dimensional** **constant-volume** **isothermal** reactor integrations mirror the **MD** **\(T,\rho\)** state points using a **179-species**, **1895-reaction** **Arrhenius** mechanism (**§3**).

### Experiments

**N/A —** computational study; experiments appear only as **literature** context.

## Findings

### Outcomes and mechanisms

**Binary** **JP-10/toluene** and **n-dodecane/toluene** mixtures **pyrolyze differently** with **composition** and **density**, because **radical**/**product** pools from one component **accelerate** chemistry in the partner beyond a **single fastest-reaction** picture. **ReaxFF MD** resolves **atomistic** pathways at **supercritical** **\(T,\rho\)** where **continuum** models trained at **low** **\(P\)** miss **pressure-sensitive** channels.

### Comparisons

**Zero-dimensional** **detailed** kinetics at matched **\(T,\rho\)** shows where **continuum** **Arrhenius** networks **disagree** with **MD**-observed **decomposition** trends; the abstract argues this highlights **regimes** where **first-order** **Arrhenius** pictures **fail**.

### Sensitivity and design levers

**Mixing ratio** **\(\alpha\)**, **density** (**0.2** vs **0.4 kg dm\(^{-3}\)**), and **temperature** (**2000–2600 K**) control **reaction** timing and **product** **slates**; **Table 1** enumerates the **atom** budgets used for each **state point**.

### Limitations and outlook (as authored)

The article notes **CHO-2016** is **less** **extensively** tested on **very large** hydrocarbons than on smaller **training** targets, and that **closed-cell** **MD** omits **flow/mixing** physics present in **engines**.

### Corpus honesty

Numerical settings above are taken from **`papers/Ashraf_Shabnam_Fuel_2018.pdf`** §3 and **Table 1**; the Elsevier imprint lists **Fuel 235 (2019) 194–207** while the DOI landing metadata may read **2018**—use the PDF’s **issue** line for citations.


## Limitations

- Force-field uncertainty for large oxygenated product spaces; validation against experiment at matching P/T remains essential.
- **Jet** **fuel** **surrogate** **compositions** in **engines** include **additives** and **aromatic** **fractions** beyond the **binary** **blends** highlighted here; **extrapolation** should be done cautiously.
- **Reactor** **residence** **time** and **mixing** **nonuniformities** can shift **product** **slates** relative to **closed** **MD** **cells** at **fixed** **density**.

## Relevance to group

Application-forward **combustion/fuels + ReaxFF** paper for high-pressure pyrolysis of realistic mixtures.

## Citations and evidence anchors

- DOI: [10.1016/j.fuel.2018.07.077](https://doi.org/10.1016/j.fuel.2018.07.077)
- Abstract: `normalized/extracts/2018ashraf-fuel-235-201-pyrolysis-binary_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Supercritical fuel pyrolysis and mixture effects
- ReaxFF for hydrocarbon cracking at extreme conditions
