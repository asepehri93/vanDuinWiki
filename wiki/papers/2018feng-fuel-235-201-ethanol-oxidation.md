---
id: paper:2018feng-fuel-235-201-ethanol-oxidation
type: paper
title: "Ethanol oxidation with high water content: a reactive molecular dynamics simulation study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:combustion
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:lammps
  - keyword:nose-hoover
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2018.08.040"
year: 2018
authors:
  - "Muye Feng"
  - "Xi Zhuo Jiang"
  - "Weilin Zeng"
  - "Kai H. Luo"
  - "Paul Hellier"
venue: "Fuel 235 (2019) 515–521 (available online 2018)"
pdf_sha256: "b26f5f839dac90559397eeb284a988fd38dad30477d0902c95fa848fa770aac0"
pdf_path: "papers/ReaxFF_others/Feng_Ethanol_water_Fuel_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018feng-fuel-235-201-ethanol-oxidation -->

## Summary

**ReaxFF molecular dynamics** compares **hydrous ethanol oxidation** to **dry / N₂-diluted** counterparts at the atomistic level, reporting faster **net oxidation** with **water** present, accelerated **ionization** and **radical** production, stronger **OH** chemistry that **oxidizes CO** to **CO₂**, and a **temperature-dependent** role for **water content** (more important at **low T**). The **Fuel** article frames **hydrous** oxidation as technologically relevant to **renewable** **oxygenated** fuels where **moisture** is unavoidable, and positions **atomistic** **ReaxFF** trajectories as a way to separate **kinetic** roles of **H₂O** (as **third-body** partner, **OH** source, and **ionization** mediator) from **diluent** effects of **N₂** in otherwise matched stoichiometries.

## Methods

From the **Fuel** article PDF (`pdf_path`).

- **Software / FF:** **LAMMPS** with **ReaxFF** **C/H/O/N** parameters (references in **Sec. 2**); **VMD** visualization; **ChemTraYzer** pathway analysis.
- **Systems (Table 1):** **40** ethanol + **120** **O2** + diluent: **System 1** **480** **N2**, box **80 A**; **System 2** **480** **H2O** replaces **N2**, box **72.65 A**; **System 3** **20** **H2O**, box **54.48 A** (variable ethanol/water ratio). Densities matched across setups by adjusting the cubic cell.
- **Protocol:** **NVT** with **Nose-Hoover** thermostat (**damping 100 fs**). **Minimization** (conjugate gradient) then **NVT** equilibration **1000 K** for **50 ps**. **Reactive** **NVT** production **1000 ps** at **2000-3000 K** (**200 K** increments). **Timestep 0.1 fs**; bond-order cutoff **0.2** for species detection; trajectories saved every **100 fs**. **Three** replicate initial conditions per (**system**, **T**) (**54** total simulations).
- **Geometry / pressure:** Each **system** in **Table 1** is a **3D PBC** cubic **supercell** with **atom** totals fixed by the **40** ethanol + **120** O₂ + diluent stoichiometry and box sizes quoted above. **N/A — NPT barostat** and **N/A — target hydrostatic pressure** during the constant-volume **NVT** oxidation trajectories.

## Findings

- **Ethanol oxidation** proceeds **faster in water-containing** environments than in the **N₂** reference case described in the abstract framing.
- **Water** promotes **ionization** steps and **radical** generation, increasing **OH** pool size; **OH** subsequently attacks **C₁/C₂** intermediates and drives **dehydrogenation** sequences.
- **CO** yields are **lower** in hydrous runs because **CO + OH → CO₂** channels become accessible, so **CO₂** rises at **CO**’s expense.
- **Water-content** effects are **large at low temperature** but **muted at high temperature** per the authors’ statement. **ChemTraYzer**-style pathway summaries in the paper help group **elementary** steps into **pools** (**OH**, **HO₂**, **CO**, **CO₂**) so operators can compare **hydrous** vs **dry** **branching** without hand-enumerating every **ReaxFF** bond event.

## Limitations

- **ReaxFF** chemistry is parametrization-dependent; quantitative **ignition** metrics should be validated against **experiment** or higher theory when available.
- **Periodic** **cubic** cells with **homogeneous** **initial** **mixtures** omit **turbulent** **straining** and **wall** **losses** present in **engines**; extrapolate **OH**/**CO** trends cautiously to **device** **burners** without matching **mixing** **times**.
- **Soot**/**NO\(_x\)** **coupling** and **three-dimensional** **flame** **fronts** are outside the **closed-cell** **ethanol** **oxidation** **study** design.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
