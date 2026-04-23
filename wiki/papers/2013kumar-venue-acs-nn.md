---
id: paper:2013kumar-venue-acs-nn
type: paper
title: "The impact of functionalization on the stability, work function, and photoluminescence of reduced graphene oxide"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - method:dft-static
  - method:reactive-md-generic
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reactive-md
  - keyword:dft-static
  - keyword:graphene-carbon
  - keyword:polymer
source_refs: []
doi: "10.1021/nn305507p"
year: 2013
authors:
  - "Priyank V. Kumar"
  - "Marco Bernardi"
  - "Jeffrey C. Grossman"
venue: "ACS Nano"
pdf_sha256: "1a3cda066c6534aa120b537ce79548218ed3d200d90f4627b32c148e81cb9090"
pdf_path: "papers/ReaxFF_others/Kumar_Bernardi_Grossman_GrapheneOxide_ACSNano_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013kumar-venue-acs-nn -->

## Evidence and attribution

!!! note "Evidence"

    Prose below summarizes the **peer-reviewed article** (**DOI `10.1021/nn305507p`**).

## Summary

**Classical MD** (including **reactive force fields** to generate realistic **disordered rGO** models) and **DFT** are combined on **statistical ensembles** of **reduced graphene oxide** structures to separate how **oxygen-containing groups** (e.g. **carbonyl**, **hydroxyl**, **epoxy**) affect **thermodynamic stability**, **work function**, and **photoluminescence**. The study highlights **metastable carbonyl-rich** motifs and **room-temperature** tendencies toward **hydroxyl-rich** arrangements via **carbonyl→hydroxyl**-type transformations near **vacancies/holes**, and quantifies **work-function tunability** (up to about **2.5 eV** shifts at fixed oxygen content by rearranging group fractions) and **PL** sensitivity to **epoxy/carbonyl** fractions.

## Methods

**Sources:** **`papers/ReaxFF_others/Kumar_Bernardi_Grossman_GrapheneOxide_ACSNano_2013.pdf`** and `normalized/extracts/2013kumar-venue-acs-nn_p1-2.txt` (through **Figure 1** caption).

**1 — MD application.** **Engine / code:** **classical molecular dynamics** with **reactive force fields** to **oxidize**/reduce **GO** ensembles (**abstract** + introduction); MD software string **N/A** on excerpt. **System size & composition:** **>360** **rGO** realizations, each **>200 atoms** in the simulation **cell**, from nine initial **GO** **compositions** with **15%, 20%, 25%** oxygen and **epoxy:hydroxyl** **3:2** or **2:3** (**extract**). **Boundaries / periodicity:** **periodic** **graphene** **supercells** with groups on both sides (**Figure 1** schematic language). **Ensemble / thermostat / barostat:** high-**temperature** **MD** at **1500 K** for **thermal reduction** is described as **constant-temperature** annealing in the protocol narrative, i.e. **NVT**-class sampling unless the **Methods** specify **NVE**/**NPT** instead (**read `pdf_path`** for the exact ensemble string); **thermostat** law and any **barostat**/**pressure** coupling details **N/A** on **p1–2** excerpt. **Timestep:** **N/A** on excerpt. **Duration / stages:** **thermal reduction** **MD** leg then **DFT** relaxation (**Figure 1a**); **ps**/**ns** budgets **N/A** here. **Temperature:** **1500 K** reduction **MD**; **300 K** kinetic discussion for **room-temperature** rearrangements in **Findings**/**abstract**. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

**2 — Force-field training.** **N/A** — uses established **reactive FF** reduction workflow cited in the article rather than fitting a new field in this paper.

**3 — Static QM / DFT.** **DFT** on the generated ensembles for **reaction** pathways, **work function**, **band** structure, and **PL** trends (**abstract**).

## Findings

**Outcomes & mechanisms:** **Carbonyl-rich** rGO from the **3:2** pathway is **metastable** and converts toward **hydroxyl-rich**, **lower-defect** rGO via **carbonyl→hydroxyl** chemistry near **vacancies**/**holes** at **300 K** in the modeled kinetics.

**Comparisons:** **Abstract** positions results as guidance for **experimental** tailoring of **functional groups** in **optoelectronics** and **renewable energy** devices—quantitative agreement with any specific **measurement** should be checked case by case.

**Sensitivity / design levers:** **Oxygen concentration** (**15–25%**) and **epoxy:hydroxyl** ratio control whether reduction yields **carbonyl-rich** vs **hydroxyl-rich** motifs; **group fractions** tune **work function** (up to ~**2.5 eV** at fixed O) and **PL** peak **frequency** via **epoxy**/**carbonyl** modulation.

**Limitations & outlook:** **DFT** approximations and **classical** **reactive FF** stages limit quantitative **barriers**/**bands**; large ensembles still miss rare **defect** arrangements (**see also** **`## Limitations`**).

**Corpus honesty:** **MD** thermostat/timestep/cell vectors are not duplicated from **`normalized/extracts/2013kumar-venue-acs-nn_p1-2.txt`**; use **`pdf_path`** **Methods** when reproducing trajectories.

## Limitations

Finite cell sizes and sampling may miss long-wavelength disorder; DFT approximations affect absolute band energies and optical peaks. The **reactive FF** stage that generates **rGO** **ensembles** also inherits **classical** uncertainties for **oxygen** **functionalization** energetics, so **DFT** refinements remain the **authority** for **quantitative** **barriers** and **band** edges. **Work-function** shifts and **PL** trends reported here are **model-dependent** and should be checked against **measurement** **conditions** (substrate, environment, excitation wavelength) when comparing to **device** data. **Ensemble** sizes in the original study are large for **DFT**, but **rare** **defect** **arrangements** can still dominate **tail** **properties** in **disordered** **rGO**. **ACS Nano** **figures** should be consulted for **quantitative** **work-function** **trends** tied to specific **functional-group** **counts**.

## Reader notes (navigation)

- [[graphene-nanocarbon]]
