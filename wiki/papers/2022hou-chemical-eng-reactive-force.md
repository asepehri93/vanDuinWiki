---
id: paper:2022hou-chemical-eng-reactive-force
type: paper
title: "A reactive force field molecular dynamics study on the inception mechanism of titanium tetraisopropoxide (TTIP) conversion to titanium clusters"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - material:oxide
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:lammps
  - keyword:thermal-decomposition
source_refs: []
doi: "10.1016/j.ces.2022.117496"
year: 2022
authors:
  - "Dingyu Hou"
  - "Muye Feng"
  - "Jili Wei"
  - "Yi Wang"
  - "Adri C.T. van Duin"
  - "Kai H. Luo"
venue: "Chem. Eng. Sci."
pdf_sha256: "ec467d2d6f66a40bd0d1cba8c02dc56b5c1918f0060e2c39030e2629f7aad2f5"
pdf_path: "papers/Hou_TTIP_conversion_ChemEngSci_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022hou-chemical-eng-reactive-force -->

## Summary

**ReaxFF reactive MD** with a newly developed **Ti/C/H/O** potential maps **titanium tetraisopropoxide (TTIP)** droplet conversion to **Ti-bearing clusters** in **1000–2500 K** with optional **O₂**, motivated by **flame** and **aerosol** synthesis routes where **organometallic** precursors first **pyrolyze** in **gas** phase before **nucleating** **oxide** **nanoparticles**. The study identifies **intermediate Ti species** and early **decomposition pathways**, and examines how **temperature**, **O₂ concentration**, and **high-temperature residence time** shift **cluster inception** and **stoichiometry**. Highlights include **non-monotonic** temperature effects (weaker **Ti–O** bonds at high \(T\)), earlier appearance of **Ti\(_2\)O\(_x\)C\(_y\)H\(_z\)** vs **TiO\(_2\)** in **pyrolysis** without **O\(_2\)**, faster **TiO\(_2\)** formation and higher yield with **ambient O\(_2\)**, and faster cluster formation when **residence time** is shortened (favoring **TiO\(_2\)** **vapor condensation**). **Cluster growth** is described as **Ti–O** bond formation to **Ti–O\(_x\)C\(_y\)H\(_z\)** moieties or clusters followed by **C–O** scission releasing **hydrocarbon** fragments.

## Methods

- **Engine:** **ReaxFF** in **LAMMPS** for **gas-phase** / **precursor** chemistry with **bond-order** updates each timestep.
- **Force field:** New **Ti/C/H/O** **ReaxFF** parametrization for **TTIP**-derived chemistry (fitted to **QM** and related reference data as enumerated in the article, including **dissociation** and **cluster** energetics).
- **Systems:** **Isolated** precursor **droplet** models in **high-temperature** environments; **1000–2500 K**; with and without **O\(_2\)** to separate **pyrolysis**-limited and **oxidation**-accelerated pathways.
- **Analysis:** **Species** tracking, **reaction pathway** identification, **cluster** size and **composition** metrics, and **residence-time** sweeps to connect **vapor** **supersaturation** to **nucleation** rates.

**Atomistic protocol (full parameters in *Chem. Eng. Sci.*):** **LAMMPS** `reax/c` **reactive** **molecular dynamics**; **gas-phase** **TTIP** **droplet** **supercells** with **3D** **PBC**; **NVT** **ensemble** at **1000–2500 K**; **sub-fs** **timestep** and **Nose–Hoover**-class **thermostat** as reported; **ps**–**ns** **equilibration** and **production**; **barostat** **N/A** for the **constant-volume** **gas-phase** **protocols** summarized; **hydrostatic** **pressure** **N/A** in that sense; **external** **electric** **field** **N/A**; **umbrella**/**metadynamics**/**replica** **exchange** **N/A**; **atom** counts and **O₂** **partial** **pressures** in the **PDF**.

## Findings

- **Temperature:** Very high **pyrolysis** temperature does not always maximize **incipient** clusters because **Ti–O** bonding can **weaken** at high \(T\), changing the balance between **fragmentation** and **aggregation**.
- **Stoichiometry vs. environment:** **Ti\(_2\)O\(_x\)C\(_y\)H\(_z\)** appears before **TiO\(_2\)** in **pyrolysis**; with **O\(_2\)**, **TiO\(_2\)** forms earlier and at higher **concentration** in the simulated window.
- **Residence time:** Shorter high-\(T\) residence boosts clusters by **condensing** **TiO\(_2\)**-rich **vapor** before extensive **organic** decomposition dilutes **oxide** precursors.
- **Growth mechanism:** **Ti–O**-mediated **aggregation** plus **bond-breaking** that **ejects** **hydrocarbon** pieces, consistent with a **stepwise** conversion from **alkoxide** ligands to **oxide** **cores**.


## Limitations

Flame-synthesis models still often rely on simplified global chemistry; this paper focuses on **atomistic inception** rather than full reactor-scale coupling. **Cluster** **counting** thresholds and **species** **definitions** should be taken from the **Chem. Eng. Sci.** text when comparing to other **Ti** **precursor** studies.

## Relevance to group

**ReaxFF** parametrization and application for **Ti–O–C–H** chemistry with **van Duin** co-authorship—relevant to **oxide** **nanoparticle** formation from **organometallic** precursors. **Chem. Eng. Sci.** readers comparing to **continuum** **flame** models should treat these trajectories as **elementary**-path **libraries** for **nucleation** rather than full **reactor** **maps**.

## Citations and evidence anchors

- DOI: [10.1016/j.ces.2022.117496](https://doi.org/10.1016/j.ces.2022.117496)

## Related topics

- [[reaxff-family]]
