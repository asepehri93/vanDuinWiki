---
id: paper:2024yongjian-yang-j-phys-chem-adsorption-co2
type: paper
title: "Adsorption of CO₂ by amine-functionalized metal–organic frameworks using GCMC and ReaxFF-based metadynamics simulations"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:catalysis-surfaces
  - method:reaxff
  - method:monte-carlo
  - method:enhanced-sampling
  - task:parameterization
  - task:application
  - material:zeolite-porous
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:monte-carlo-sampling
  - keyword:enhanced-sampling
  - keyword:lammps
  - keyword:validation-experiment
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c07183"
year: 2024
authors:
  - "Yongjian Yang"
  - "Yun Kyung Shin"
  - "Hideaki Ooe"
  - "Urara Hasegawa"
  - "Setsuko Yamane"
  - "Hayata Yamada"
  - "Adri C. T. van Duin"
  - "Yasuhiro Murase"
  - "John C. Mauro"
venue: "J. Phys. Chem. C"
pdf_sha256: "68e518e3c2bd0b1247b3c1e2c6a82086845792e3ee315ff916e96d4e1c82121e"
pdf_path: "papers/Yang_Shin_JPC_2024_CO2_MOF_GCGC.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024yongjian-yang-j-phys-chem-adsorption-co2 -->

Grand canonical Monte Carlo (RASPA) screens CO₂ and H₂O uptake on amine-decorated Zn-MOF candidates; Jaguar DFT (M06-2X-D3/6-311++G**) ranks linker-level physisorption vs chemisorption; a ZIF-oriented ReaxFF is extended with CO₂–amine chemistry and metadynamics (LAMMPS + PLUMED) estimates chemisorption barriers, alongside experimental adsorption tests on synthesized samples.

## Summary

Twenty primary-amine Zn MOFs (CSD or linker-substituted models) are downselected using Zeo++ pore metrics, RASPA GCMC for CO₂ and H₂O at 100 kPa and 298 K (including dilute CO₂–O₂–N₂ mixtures), and MPNN-predicted charges under charge neutrality. DFT on gas-phase linkers compares physisorbed vs chemisorbed CO₂ and probes water-assisted stabilization (e.g., CH₃NH₂ + CO₂ + H₂O clusters, transition states for carbamate-like paths). A ReaxFF trained for ZIF water stability is augmented with CO₂ physisorption/chemisorption energies and CH₃NH₂–CO₂ reaction energetics; parameters are listed in Supporting Information. Well-tempered metadynamics (Gaussian hills, PLUMED) with distance-based CVs drives CO₂ toward −NH₂ in dry, water-assisted, and (for PEI-like cases) methylamine-assisted setups; NVT at 300 K, Δt = 0.25 fs, 1–4 ns runs, multiple initial velocities for barrier statistics. Experiments measure CO₂ uptake under humid air (2500 ppm CO₂) and related characterization (article §2.6).

## Methods

- **Screening:** RASPA GCMC; Generic MOFForce field for physisorption; MPNN charges; Zeo++ voids; multiple gas compositions including 400 ppm and 1% CO₂ scenarios in tables.
- **DFT:** Jaguar, M06-2X-D3, 6-311++G**; full relaxations; transition-state searches with one imaginary frequency where reported (SI).
- **ReaxFF + metadynamics:** Extended ReaxFF for amine–CO₂ chemistry; LAMMPS; PLUMED metadynamics (Gaussian height ~10 kJ/mol, σ = 0.1, hill frequency 1000 steps, well-tempered bias factor ~100, lower walls to suppress spurious inter-amine reactions); collective variables primarily interatomic distances among N, C (CO₂), O, and helper atoms (Table 2).
- **Experiment:** Synthesis and CO₂ uptake protocols for selected MOFs and ZIF-8/PEI blends (§2.6).

**1 — MD application (ReaxFF + metadynamics).** **Engine:** **LAMMPS** + **PLUMED**; **NVT** at **300** **K**; **PBC** **3D** **MOF** **unit** **cells** with **PLUMED**-wrapped **PBC** as in the **SI**; **NVT** **thermostat** chain as in the **article** (confirm details in **`pdf_path`**); **Δt = 0.25** **fs**; **1–4** **ns** **restarts** for **barrier** **stats**; **well**-**tempered** **metadynamics** (Gaussian **hills** **~10** **kJ/mol**, **σ = 0.1**, **hill** **period** **1000** **steps**, **well**-**tempered** **bias** **~100** as **summarized**; **lower** **walls** to **block** spurious **amine**–**amine** **chemistry**); **CVs** are **interatomic** **distances** among **N**, **C** **(CO₂)**, **O**, and **selected** **helpers** (**Table** **2**). **GCMC** (RASPA) **legs** for **adsorption** use **100** **kPa** / **298** **K** and **dilute** **air**-like **mixtures** as in **Tables** (not the same **code** path as **LAMMPS**). **N/A** — **NPT** **metadynamics** in the **summary** here; **N/A** — **external** **uniform** **E-field** in the **stated** **ReaxFF** **leg** (field-like **biases** only via **PLUMED** **as** **written** for **metadynamics**). **N/A** — **replica** **exchange** in the **brief** text.

**2 — Force-field training** — **ReaxFF** **extended** for **ZIF** **+** **amine** **+** **CO₂** with **Jaguar** **M06**-**2X**-**D3/6-311++G\*\*** **reaction/adsorption** **targets** and **SI**-listed **parameters**. **3 — Static QM (Jaguar).** **Cluster**-level **physisorption** **vs** **chemisorption** and **TS** **searches** as **described** in **article/SI**. **4 — Grand canonical Monte Carlo (RASPA).** **Screening** **isotherms**; **not** a **ReaxFF** **MD** **block** but part of the **multi**-**method** **workflow**.
## Findings

1. At high CO₂ fugacity, uptake is dominated by physisorption; at dilute CO₂ (e.g., air-like 2500 ppm), chemisorption contributions become prominent in the analysis.
2. Gas-phase DFT shows water can stabilize carbamate-like products and make chemisorption more exothermic; metadynamics reports high intrinsic barriers for dry chemisorption on several frameworks, reduced with explicit water or −NH₂ assistance pathways.
3. ZIF-8 mixed with polyethylenimine shows high initial chemisorption but degrades on cycling, while amine-functionalized MOFs show lower amine utilization under humid air in the experiments—contrasting simulation-experiment roles of water and diffusion.
4. The paper positions the workflow as an example of combining screening, reactive FF development, and rare-event simulation for MOF CO₂ capture.

**Corpus honesty** — see **`## Limitations`** for **ReaxFF** **transfer** across **linkers** and **sparse** **experimental** **statistics**.
## Limitations

ReaxFF accuracy for full periodic MOF reactivity, force-field transferability across linker libraries, and limited experimental statistics on every candidate remain constraints.

## Relevance to group

Co-authored by van Duin; extends ReaxFF for MOF–amine–CO₂ chemistry with metadynamics and experimental validation.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.3c07183](https://doi.org/10.1021/acs.jpcc.3c07183)

## Related topics

- [[reaxff-family]]
