---
id: paper:2016cao-venue-early-stage
type: paper
title: "Early stage oxynitridation process of Si(001) surface by NO gas: Reactive molecular dynamics simulation study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:oxides-ceramics
  - material:widegap-semiconductor
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:reactive-md
  - keyword:neb
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1063/1.4944707"
year: 2016
authors:
  - "Haining Cao"
  - "Pooja Srivastava"
  - "Keunsu Choi"
  - "Seungchul Kim"
  - "Kwang-Ryeol Lee"
venue: "J. Appl. Phys."
pdf_sha256: "1710a1d7708dd7328549533517532d315e159315d5cb171a7ee7f9306dfda1e3"
pdf_path: "papers/ReaxFF_others/Cao_NO_Silicon_MOSFET_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016cao-venue-early-stage -->

## Summary

Ultrathin gate oxynitrides on silicon are produced by exposing clean surfaces to nitric oxide so nitrogen and oxygen incorporate within a few angstroms of the interface. Cao et al. apply ReaxFF reactive molecular dynamics to NO chemisorption and reaction on reconstructed Si(001) between 300 K and 1000 K, aggregating 1120 independent single-molecule NO events to extract temperature-dependent kinetic information for early oxynitridation. Complementary density-functional nudged elastic band calculations compare activation barriers for intra-dimer versus inter-dimer NO bridge precursors prior to dissociation, while sequential NO dosing simulations probe self-limiting film growth and nitrogen/oxygen depth profiles.

The study is motivated by advanced metal–oxide–semiconductor field-effect transistors, where silicon oxynitride films buffer the silicon channel from high-\(k\) dielectrics, suppress boron penetration from doped gates, and tune interfacial defect densities relative to pure oxide stacks. Nitric oxide is treated as a primary nitrogen precursor compared with nitrous oxide routes often used in furnace chemistry.

## Methods

### MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** is used for the **reactive molecular dynamics** simulations (*J. Appl. Phys.* **119**, **125305**; **`pdf_path`**).
- **Interaction model:** **ReaxFF** for **N / O / Si / H** as referenced in the article (including the benchmark note pointing to **SI-1**).
- **System / composition:** **Si(001)** **slab** model (**1476 Si** atoms) with lateral dimensions **2.256 nm × 2.256 nm** and **5.282 nm** total thickness; **~1.1 nm vacuum** above the surface; **dimer-row** orientation aligned with the simulation box axes as in Fig. 1.
- **Boundaries / frozen regions:** **Periodic boundary conditions** in the two **lateral** directions; **bottom two Si layers** (**0.27 nm**) **fixed**; **29 layers** (**3.85 nm**) below the reactive region act as a **heat bath** with **temperature rescaling every timestep**; **top 10 layers** (**1.33 nm**) unconstrained for chemistry.
- **Timestep:** **0.5 fs** (stated as the rescaling interval for the bath layer control).
- **Thermostat / thermal control:** **Berendsen thermostat** couples the **heat-bath** region and the **topmost free layer** during substrate equilibration at the reaction temperatures (**300**, **500**, **700**, **900 K** are explicitly mentioned in the Methods excerpt).
- **Temperature / statistics:** **1120** independent **single-NO** events sampled for kinetics across **300–1000 K** (abstract); representative trajectory lengths for classification snapshots are on the order of **~1–5 ps** at stated temperatures (see figure captions in **`pdf_path`**).
- **Sequential dosing:** After **10 ps** equilibration at the reaction temperature, **NO** is added every **20 ps** in the consecutive-reaction growth studies (Methods text).
- **Initial NO placement / energy:** **NO** starts **0.35 nm** above the surface; initial **NO** translational energy corresponds to **300 K** thermal energy (**~38 meV** as written).
- **Ensemble:** The manuscript describes **constant-temperature** control via rescaling/thermostatting of bath regions while keeping dynamical **Newtonian** evolution in the reactive zone—read **`pdf_path`** for the precise **NVT**-vs-**NVE** phrasing used by the authors.
- **Barostat / pressure:** **N/A — fixed-volume slab** workflow; no **NPT** **pressure** targeting is described in the excerpted Methods text.
- **Electric field:** **N/A — not used.**
- **Replica / enhanced sampling:** **N/A — not used.**

### Force-field training

**N/A — not a parameterization paper**; the manuscript **applies** an established **ReaxFF** description for **NO + Si(001)** chemistry.

### Static QM / DFT (NEB benchmarks)

- **Method:** **Nudged elastic band (NEB)** calculations compare **intra-dimer** vs **inter-dimer** **NO bridge** precursors on the way to dissociation.
- **Authored kinetic conclusion:** Even if an **intra-dimer** complex can be **lower in energy**, the **inter-dimer bridge** pathway is argued to dominate because its **activation barrier** is **lower** in the NEB results (abstract-level statement).

## Findings

- **Validation:** The authors state that the **statistical MD kinetics** are **consistent** with prior **experimental** and **theoretical** literature on **NO** chemistry on **Si**, supporting use of the reactive MD approach for this interface problem.
- **Pathway selection:** **NEB** results motivate favoring an **inter-dimer bridge** intermediate for **NO dissociation** despite **thermodynamic** preferences for some **intra-dimer** geometries—i.e., **kinetic** control of the dominant channel in their model.
- **Growth phenomenology:** **Low-temperature** sequential dosing shows **self-limiting** incorporation consistent with **STM**-oriented expectations discussed in the paper, while **higher temperature** broadens **N/O depth** distributions—framed as guidance for **oxynitridation thermal budgets** in gate-stack processing.

## Limitations

Numerical barriers and prefactors must be taken from the article and SI; ReaxFF omits explicit electronic excitations beyond the empirical bond-order form.

## Relevance to group

Silicon oxynitridation and gate-stack processing are classic ReaxFF application areas for semiconductor oxidation.

## Citations and evidence anchors

- DOI: [10.1063/1.4944707](https://doi.org/10.1063/1.4944707)

## Related topics

- [[reaxff-family]]
