---
id: paper:2024l-vermeersch-j-phys-chem-computational-insights
type: paper
title: "Computational Insights into Tunable Reversible Network Materials: Accelerated ReaxFF Kinetics of Furan-Maleimide Diels–Alder Reactions for Self-Healing and Recyclability"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - method:dft-static
  - material:polymer-organic
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:enhanced-sampling
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.4c05470"
year: 2024
authors:
  - "L. Vermeersch"
  - "T. Wang"
  - "N. Van den Brande"
  - "F. De Vleeschouwer"
  - "A. C. T. van Duin"
venue: "J. Phys. Chem. A 2024, 128, 10431–10439"
pdf_sha256: "e3aa19f2455c8b23e342c12aaddc7250a3d536d07cf5143fb862cb56ba09289f"
pdf_path: "papers/Vermeersch_JPCA_DielsAlder_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024l-vermeersch-j-phys-chem-computational-insights -->

## Summary

The paper develops a **ReaxFF** description for **furan / N-methylmaleimide** **Diels–Alder (DA)** and **retro-DA** chemistry relevant to **covalent adaptable networks (CANs)**, trained against **M06-2X-D3/cc-pVDZ** barriers and paths, then uses **bond-boost accelerated ReaxFF MD** to study **gas-phase** retro-DA **stereoselectivity**, **temperature**, **bond-boost parameters**, and a **polymer-backbone** model system—reported as a first reactive-MD-oriented step toward **CAN** kinetics with **DA** linkers.

## Methods

- **QM reference:** **Gaussian 16**; **M06-2X** with **Grimme D3** dispersion and **cc-pVDZ**; **TS** characterization by one imaginary mode and **IRC** paths; **Eyring–Polanyi** estimates of **endo/exo** ratios at **300 K** from QM barriers.
- **ReaxFF training:** Starting from **Kowalik et al. 2019** parameters, **retraining** against the QM **forward/retro barriers**, **reaction energies**, and **geometries** along the path (per Methods and Results).
- **ReaxFF MD + bond boost:** Boxes of **40** **endo** and **40** **exo** products (and later **10** products with **polymer backbone**); **bond boost** on the four **C** atoms involved in cycloaddition; **target distance** **3.0 Å**; bond-break detection at **bond order 0.3** (~**2.45 Å**); **F2 = 0.25**; **F1** scanned **90–130** (and higher **F1** noted to remove stereoselectivity); **5000** steps boost duration as stated.
- **Stereoselectivity readout:** Concentrations of **endo/exo** reagents after successful boosts; comparison to **Eyring** expectations and literature **retro** barrier splitting for **furan–maleimide**-class systems.

**1 — MD (bond-boosted ReaxFF).** **LAMMPS**-style **ReaxFF** dynamics with **bond boost** (see *Computational* section: **F1**/**F2**, **target 3.0 Å**, **5000**-step boost; **NVT**-like gas-phase product boxes; **N/A** for **NPT** /**barostat**: not part of the narratives summarized. **PBC** where used for the simulation cells as in the **PDF**. **Timestep, thermostat, total trajectory length, pressure:** **N/A** if not in this page—**see article**. **Electric field:** **N/A**. **Enhanced sampling:** **bond boost** (not **umbrella** in this summary). **2 — ReaxFF training (relative to Kowalik et al.)** and **3 — static QM (Gaussian M06-2X-D3/cc-pVDZ)**: in the first bullets under **Methods**; **Kowalik** parent is the **starting** parameter set.
## Findings

- The **retrained ReaxFF** reproduces QM **energy profiles** with small mean errors (barriers/reaction energies cited in the paper; **endo** retro barrier and **endo** reaction energy show slightly larger deviations than other entries in their Table 1).
- From **DFT** (**endo** vs **exo** retro barrier difference **~2.2 kcal/mol**) and **ReaxFF** (**~2.7 kcal/mol**), **endo/exo** ratios at **298.15 K** are estimated as **~41 (DFT)** vs **~95 (ReaxFF)** by **Eyring**, bracketing an **experimental** ratio **~69** cited in the article—used as a consistency check for the reactive MD stereoselectivity analysis.
- **Bond-boost MD** on **40-molecule** **endo** and **exo** sets shows **endo** adducts decompose more readily than **exo**, matching the **retro** barrier ordering; **F1** tunes how often boosts succeed and must stay below the regime where all events succeed (loss of selectivity at overly high **F1**).
- **Higher temperature** simulations (reported relative to **300 K** reference) and the **polymer-backbone** model illustrate how environment and acceleration parameters shift **endo/exo** outcomes, supporting the use of the parametrization for more complex **CAN** models in follow-on work. **Comparisons** to **DFT/IRC**, **Eyring** ratios, and a cited **experimental** **endo/exo** ratio (paper’s Table 1 narrative) are in the bullets. **VOR** **PDF** is authoritative for **F1**/**T** values.
## Limitations

Training and dynamics are focused on **gas-phase** and simplified **network fragments**; extrapolation to full polymer **CAN** condensed-phase kinetics requires additional validation.

## Relevance to group

**van Duin-group** **ReaxFF** development and **reactive MD** methodology for **polymerizable** / **reversible** networks.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.4c05470](https://doi.org/10.1021/acs.jpca.4c05470)

## Related topics

- [[reaxff-family]]
