---
id: paper:2017patrito-venue-research
type: paper
title: "Thermal Stability of Organic Monolayers Grafted to Si(111): Insights from ReaxFF Reactive Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:oxide-surface
  - keyword:lammps
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.7b05444"
year: 2017
authors:
  - "Federico A. Soria"
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
  - "Eduardo M. Patrito"
venue: "ACS Appl. Mater. Interfaces"
pdf_sha256: "b91d4058a6c6f84f731317b803d770a528c949b85c4e00a9185d1508b4521e9f"
pdf_path: "papers/Patrito_Zhang_SiC_ACS_AMI_2017_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017patrito-venue-research -->

!!! abstract
ReaxFF MD (ADF + LAMMPS, 0.1 fs, 1500–2000 K) on Si(111) slabs with alkyl (50% coverage) and methyl/propynyl/propenyl full-coverage monolayers reveals two-silicon dehydrogenation pathways and coverage-dependent alkene desorption.

## Summary

**ReaxFF** parametrization for **Si/C/H** optimized to **DFT** training sets for **alkyl-on-Si(111)** chemistry (**van Duin** parameter lineage) targets **pentacoordinate** **Si** intermediates and **homolytic** **Si–C** events that dominate **hot** **organosilicon** decomposition. **MD** uses **velocity Verlet**, **0.1 fs** timestep, **temperature damping 100 fs**, **800 ps** runs from **1500–2000 K** after **300 K, 1 ps** thermalization (**ADF2016** and **LAMMPS**). **Si(111)** slabs use **six bilayers**; **6×8** and **8√3×8** cells (**48** or **64** top Si atoms) with **200 Å** vacuum; **both surfaces** functionalized in many cases. Systems include **50%** alkyl + **50%** hydrogen at top sites (**ethyl, propyl, pentyl, decyl**) and **100%** **Si–CH₃**, **Si–CCCH₃**, **Si–CHCHCH₃**. High temperatures accelerate decomposition within accessible MD timescales (authors justify **1500–2000 K** window after ethyl scan **1200–2200 K**), trading **laboratory** temperatures for **activated** chemistry within **nanosecond** trajectories.

## Methods

### 1 — MD application (atomistic dynamics)

**ReaxFF** reactive molecular dynamics probes **thermal decomposition** of **organic monolayers** on **Si(111)** at elevated temperatures so that bond-breaking events occur within accessible nanosecond trajectories. Simulations use **velocity Verlet** integration with **Δt = 0.1 fs**, **Berendsen thermostat** coupling (**100 fs** damping constant in the article), **800 ps** production segments after **1 ps** thermalization from **300 K** into the **1500–2000 K** window used for the grafted layers (authors motivate the hot window with a prior ethyl-layer scan up to **2200 K**). Calculations are reported from **ADF2016** and cross-checked in **LAMMPS** as stated in the article.

- **Engine / code:** **ADF2016** and **LAMMPS** with **ReaxFF** (same DOI as **[[2017federico-a-soria-acs-thermal-stability]]**; this corpus path may be a **proof** PDF).
- **System size & composition:** **Si(111)** slabs with **six bilayers**, **6×8** and **8√3×8** surface unit cells (**48** or **64** top-layer Si sites), **~200 Å** vacuum gap, and **both** surfaces functionalized in the geometries discussed in the article. Monolayers include **50%** alkyl + **50%** H (**ethyl, propyl, pentyl, decyl**) and full-coverage **Si–CH₃**, **Si–CCCH₃**, and **Si–CHCHCH₃** terminations.
- **Boundaries / periodicity:** **Three-dimensional periodic** slab supercells with vacuum along the surface normal (geometry conventions in the article figures).
- **Ensemble:** **NVT** hot-MD segments after initial thermalization (**canonical** sampling with Berendsen coupling as reported).
- **Timestep:** **0.1 fs** (required for stiff **Si–C/H** motion at **1500–2000 K** in the authors’ protocol).
- **Duration / stages:** **1 ps** ramp/thermalization from **300 K**, then **800 ps** reactive sampling in the reported high-temperature window(s).
- **Thermostat:** **Berendsen** temperature control with **100 fs** damping constant (article text).
- **Barostat:** **N/A** — constant-volume **NVT** hot runs without hydrostatic **NPT** control in the protocol summarized here.
- **Temperature:** **300 K** initialization, then **1500–2000 K** production temperatures depending on layer chemistry (per article).
- **Pressure:** **N/A** — no stress-control barostat in the summarized **NVT** decomposition protocol.
- **Electric field:** **N/A** — not used.
- **Replica / enhanced sampling:** **N/A** — direct **hot** MD rather than umbrella / metadynamics.

### 2 — Force-field training

**Si/C/H ReaxFF** parameters optimized against **DFT** training data for **alkyl-grafted Si(111)** chemistry (including **pentacoordinate Si** motifs and **homolytic Si–C** pathways) along the **van Duin** reactive silicon–hydrocarbon lineage cited in the article.

### 3 — Static QM / DFT-only

**DFT** reference energies/structures enter **only** as **training data** for ReaxFF; **ab initio MD** is **not** the production tool for the reported thermal decomposition trajectories.

## Findings

- **Silyl radicals** from **Si–C homolysis** drive dehydrogenation; main pathways require **two lattice Si centers**, not only one, so **pairwise** **Si** reactivity matters beyond local **substituent** chemistry.
- **Flexible n-alkyl** chains dehydrogenate readily (**β-H** routes → **1-alkene** desorption); **lower coverage** allows deeper **methylene** dehydrogenation including terminal **methyl** on long chains.
- **Rigid alkynyl/alkenyl** substituents hinder terminal **methyl** abstraction → **higher thermal stability** versus saturated analogs at comparable coverages.
- Surfaces trend toward **hydrogen termination** as **Si–C** bonds break and **Si–H** forms during decomposition, altering subsequent **radical** recycling.

## Limitations

Proof PDF in corpus; elevated temperatures accelerate kinetics—extrapolate to lower **T** with care.

## Relevance to group

**Adri C. T. van Duin** co-authorship; demonstrates **ReaxFF** for **semiconductor organics** degradation. The **ACS Appl. Mater. Interfaces** article is a useful reference for **Si(111)** **graft** **thermolysis** benchmarks when calibrating **Si/C/H** **reactive** models against **DFT** **barriers** and **desorption** **product** channels.

## Citations and evidence anchors

- DOI: `10.1021/acsami.7b05444`

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
