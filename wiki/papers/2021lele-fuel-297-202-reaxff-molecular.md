---
id: paper:2021lele-fuel-297-202-reaxff-molecular
type: paper
title: "ReaxFF molecular dynamics study on pyrolysis of bicyclic compounds for aviation fuel"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2021.120724"
year: 2021
authors:
  - "Aditya Lele"
  - "Hyunguk Kwon"
  - "Karthik Ganeshan"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Fuel 297:120724 (2021)"
pdf_sha256: "aeb707b4d10d8e5eed09c5d2cbb594b3ee08d60caceb904c43f4e9b33d4ae468"
pdf_path: "papers/Lele_Fuel_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021lele-fuel-297-202-reaxff-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The article investigates **initial pyrolysis** of **four head-to-head (HtH) bicyclic alkanes** (**HtH-3** through **HtH-6**) that were synthesized as **aviation-fuel candidates**, using **ReaxFF**-based **molecular dynamics** with the **CHO-2016** combustion force field. The fuels fall into two structural classes: **cyclic alkanes joined by a four-membered ring** (e.g., **HtH-3**, **HtH-5**) versus **cyclic alkanes joined by a single central C–C bond** (**HtH-4**, **HtH-6**). The authors follow the same systematic workflow as in their prior study of **HtH-1** and **HtH-2**, computing **global Arrhenius parameters** from simulated decomposition trajectories, classifying **elementary** pathways, and comparing **relative reactivity** among candidates—including comparison to **JP-10** as a familiar jet-fuel reference in the kinetic discussion. The abstract emphasizes two dominant reaction classes: **cleavage of the central linkage** yielding **cyclic radicals** (or related fragments) versus **ring-opening** routes that produce **small alkenes**, with the balance **strongly temperature-dependent**. The paper also reports **path-integral molecular dynamics (PIMD)** for **HtH-3** as a sample case to probe **nuclear quantum effects** alongside classical **ReaxFF** trajectories.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** CHO-2016 ReaxFF in LAMMPS with ReaxAMS/ADF workflows for PES/TS/IRC support as in the *Fuel* article.
- **System & composition:** For each HtH fuel, 40 energy-minimized molecules in a periodic cell at 0.2 kg dm\(^{-3}\) (manuscript reports ideal-gas-like initial pressures on the order of 150–330 atm at the equilibration temperature).
- **Boundaries / periodicity:** 3D periodic supercell.
- **Ensemble:** NVT.
- **Timestep:** 0.1 fs in production NVT runs.
- **Duration / stages:** Equilibration NVT at 1500 K with Berendsen thermostat (100 fs damping) before decomposition; production NVT 1500–3000 K; ten independent initial seeds per temperature; at 1500 K, collective-variable driven hyperdynamics (CVHD) to accelerate rare events. Reaction parsing with an in-house code.
- **Thermostat:** Berendsen (100 fs damping) in the equilibration line above.
- **Barostat / pressure:** N/A — NVT; high initial gas-like pressure is from density/temperature, not a barostat setpoint in the sense of constant hydrostatic P.
- **Temperature:** 1500 K equilibration; production 1500–3000 K.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** CVHD at 1500 K; N/A for umbrella/metadynamics in the sense of the MD checklist (hyperdynamics is the accelerated-dynamics method used where stated).

### 2 — Force-field training (ReaxFF and related)

N/A for a new global fit in this application paper — CHO-2016 (Ashraf *et al.*) is used as published; see *Fuel* for citation.

### 3 — Static QM / DFT (validation and BDE benchmarks)

B3LYP/6-311G++ bond dissociation energies in Jaguar for key C–C bonds (Table 1, Section 3) to support interpretation of reactivity classes; not a production AIMD study.

### 4 — Review

N/A — primary application article.

## Findings

**Bond dissociation energy** trends from **DFT** and **ReaxFF** align qualitatively: **four-membered ring** junctions in **Group 1** feature very low **C–C BDEs** (about **21–26 kcal mol\(^{-1}\)** in the article’s **Table 1**), favoring early fragmentation relative to **Group 2** molecules where central and adjacent **C–C** bonds fall nearer **52–76 kcal mol\(^{-1}\)**. Decomposition profiles at **2000 K** (see **Fig. 2**) show **Group 1** fuels more reactive than **Group 2**, consistent with the earlier **HtH-1** vs **HtH-2** comparison. **Global Arrhenius** parameters aggregated across temperatures appear in **Table 2** of the paper; fuels exhibit **faster or comparable** decomposition versus **JP-10** under the reported analysis. **Endothermicity** during early pyrolysis is analyzed as a **thermal-management** indicator for engine cooling concepts. **PIMD** results for **HtH-3** illustrate how **nuclear quantum effects** can modulate reaction dynamics relative to classical **MD**, as discussed in the dedicated section. **Comparisons:** group 1 vs 2 bicyclics; vs JP-10 in Arrhenius discussion; BDE table vs ReaxFF trends. **Corpus / KB honesty:** all numerical protocol and table values from `pdf_path` at *Fuel* **297**, **120724** (2021).

## Limitations

Classical **ReaxFF** omits explicit **electronic** excitations; **PIMD** adds cost and still approximates quantum nuclei. **High-temperature**, **high-pressure** gas-phase cells simplify real **injector** and **sooting** environments.

## Relevance to group

Penn State **fuels** work extending **ReaxFF** pyrolysis studies toward **high-energy-density** bicyclic **aviation** candidates.

## Citations and evidence anchors

`papers/Lele_Fuel_2021.pdf` — **Fuel** **297**, **120724** (2021). https://doi.org/10.1016/j.fuel.2021.120724

## Related topics

- [[2021lele-venue-paper]]
- [[reaxff-family]]
