---
id: paper:2018gonzalez-valle-acs-thermal-transport
type: paper
title: "Thermal transport across SiC–water interfaces"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - material:widegap-semiconductor
  - method:classical-md
  - task:application
paper_keywords:
  - keyword:water-interfaces
  - keyword:classical-ff
  - keyword:nve-simulation
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.8b10307"
year: 2018
authors:
  - "C. Ulises Gonzalez-Valle"
  - "Satish Kumar"
  - "Bladimir Ramos-Alvarado"
venue: "ACS Appl. Mater. Interfaces 10, 29179–29186 (2018)"
pdf_sha256: "d628876dfc27541134e6705a337cc113f0581ee1cacb4de380ae36ec631a938d"
pdf_path: "papers/Others/20. Thermal Transport across SiC−Water Interfaces.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018gonzalez-valle-acs-thermal-transport -->

## Summary

**Nonequilibrium classical molecular dynamics** computes **thermal boundary conductance (TBC)** across **3C–SiC | water** interfaces, scanning **crystallographic orientation**, **Si vs C termination**, and **hydrophilic vs hydrophobic** **solid–liquid coupling** strengths, then relates **interfacial liquid structure**—including **density depletion lengths**—to **TBC**, showing **wetting metrics alone** are not universal predictors of **heat flow**. The work targets **thermal management** at **wide-bandgap** **semiconductor** **cooling** interfaces where **Kapitza** resistance can dominate **junction** temperatures; by sweeping **LJ** **solid–water** **ε** across **hydrophilic/hydrophobic** regimes, the paper separates **contact-angle-like** metrics from **structure-resolved** heat-transfer descriptors.

## Methods

From **ACS Appl. Mater. Interfaces** PDF (`pdf_path`).

- **Interactions:** **SPC/E** water; **LAMMPS** + **VMD**; **SiC** slabs with **fixed** bottom layers and **frozen** constraint region; **6 nm** gap between opposing slabs filled with **1000-1100** **H2O** molecules (adjusted with **wettability** to keep bulk pressure consistent per article). **LJ** solid-liquid parameters scanned to vary **hydrophilic / hydrophobic** coupling (**epsilon_SL** ranges tied to prior wetting work).
- **Equilibration:** **Minimization**; **NVT** at **300 K** (**1 ns**) with **Nose-Hoover** (**time constant 100 fs**); **NVE** **1 ns** stability check.
- **Nonequilibrium thermal:** Energy **add/remove** in hot/cold slab regions (**5 ns** ramp); **production** **7.5 ns** sampling **KE** and coordinates every **10 ps**. **Timestep 1 fs**. **Thermal boundary conductance** **G** from **G = J / Delta T_int** with heat currents **5-15 nW** tested for linear response.

## Findings

- **TBC** varies with **plane** and **termination** beyond what a single **wetting** descriptor captures; **interfacial water structure** must be included.
- **Hydrophilic** coupling tends to increase **TBC** vs **hydrophobic** cases in the trends summarized, but **exceptions** known from other systems motivate the **structure-aware** analysis used here.
- Using **density depletion length** as a descriptor **reconciles** disparate **TBC** estimates that would otherwise appear inconsistent when only **contact-angle–like** metrics are used.
- **Linear-response** checks (**5–15 nW** heat currents) support extracting **G** from **steady** **ΔT** across the **interface** without spurious **nonlinear** heating artifacts in the reported protocol window.

## Limitations

- **Classical** potentials for **SiC–water** may miss **quantum** corrections and **polarization** effects important for some **quantitative** comparisons.
- **LJ** **mixing** rules used to dial **hydrophilic/hydrophobic** coupling are **phenomenological**; **ab initio** **interfacial** **spectroscopy** would be needed to **tie** **ε** **scans** to **specific** **surface** **terminations** in **experiment**.
- **Surface** **oxidation** or **hydrocarbon** **contamination** on **SiC** **in** **device** **fabrication** can alter **wetting** and **TBC** relative to the **idealized** **cleaved** **slabs** simulated.

## Related topics

- [[2018c-ulises-gonzalez-va-j-phys-chem-investigation-wetting]]
- [[reaxff-family]]

## Reader notes (navigation)

Cross-link **thermal boundary conductance** surveys when comparing **SiC** **power** **electronics** cooling concepts to **diamond** or **oxide** **substrates** in other corpus entries.
