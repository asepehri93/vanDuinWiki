---
id: paper:2019mao-physical-che-atomistic-insights
type: paper
title: "Atomistic insights into the dynamics of binary collisions between gaseous molecules and polycyclic aromatic hydrocarbon dimers"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:reactive-md
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1039/C8CP07060A"
year: 2019
authors:
  - "Qian Mao"
  - "Juan Zhou"
  - "Kai H. Luo"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "42d5bc3def122b1934b1e952730d06aa9e33493965cfce8ca88c6f6d2b9e2085"
pdf_path: "papers/Mao_PCCP_collision_N2_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019mao-physical-che-atomistic-insights -->

## Summary

**Polycyclic aromatic hydrocarbon (PAH) dimers** are frequently invoked as **soot nuclei**, yet most **kinetic** models either treat dimerization as **irreversible** or neglect **collisions** with **hot bath gases** present in **engines** and **flames**. The **PCCP** study therefore occupies a **middle ground** between **supersonic jet** experiments that emphasize **low-temperature** **physical dimers** and **flame** simulations that historically **lumped** **bath gas** effects into **effective** **sticking** **coefficients** without **explicit** **collision** **dynamics**. **Mao**, **Zhou**, **Luo**, and **van Duin** perform **ReaxFF molecular dynamics** of **binary collisions** between **N\(_2\)**, **CO**, **CO\(_2\)**, and related **projectiles** with **stacked PAH dimers** sampled from prior **dimerization** studies. The work classifies **scattering** outcomes by **N\(_2\)** **residence time** inside the dimer scaffold, links **energy transfer** to **dimer lifetime**, and quantifies how **projectile mass** biases **decomposition** back to **monomers**.

## Methods

**2 — Force-field training (as used, not re-fit here).** The **C/H/O/N** **ReaxFF** set combines **C-2013** carbon parameters with the broader **hydrocarbon**/**gas**-phase training of the **C/H/O/N** library documented in the paper; **ESI** tabulates the **ReaxFF** **bond-order** **parameters** used in this work.

**1 — MD application (binary collision trajectories).** **ReaxFF** **MD** is implemented in **LAMMPS**. **Stacked** **PAH** **dimers** are taken from prior **dimerization** work (same program). **Binary-collision** cells place a **PAH** **dimer** in a **cubic** **(70 Å)³** **PBC** box with **50 Å** initial **separation** to the **projectile** gas molecule; **impact parameters** and **collision** **angles** are **sampled** as specified in **§2.2** (including **1000** **independent** trajectories per **(temperature, dimer)** case in the **PCCP** text). **Collisions** are integrated in the **microcanonical (NVE)** ensemble with a **0.1 fs** timestep for **10⁶** steps (**~100 ps** total per trajectory in the article’s equation-of-motion block). **Thermostat:** **N/A** for these **NVE** segments—no **Nosé–Hoover**/**Berendsen** **thermal** **bath** is applied during the **quoted** **collision** integration. **Initial** **translational** and **rotational** **energies** of the **dimer** and **projectile** are assigned from **Maxwell** / **equipartition**-style distributions at the **target** **temperature**; **N₂**, **CO**, and **CO₂** are treated with **ReaxFF**-consistent **internal** **bond** models (harmonic oscillators for diatomic/polyatomic projectiles, per **§2.2**). **Thermostat**/**barostat** during the **collision** segment: **N/A** — **NVE** **binary-collision** **dynamics** (not constant-**T** **NVT** production). **Mean** **hydrostatic** **pressure** as an **NPT** target: **N/A** — isolated **collision** studies without **bulk** **pressure** coupling. **External electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**. **System sizes / compositions:** as defined by the **pyrene-** and **larger**-**PAH** **dimer** models in **Figs. 1–2**; exact **atom** counts follow from those **dimer** constructions plus one **gaseous** **projectile**.
## Findings

When **N\(_2\)** remains **trapped** only briefly, **specular-like** scattering dominates, whereas long **residence** enables **inelastic** energy accommodation; **temperature** and **dimer size** shift the balance, with **specular** channels favored at **high T** on **small** dimers and **inelastic** channels more visible at **low T** on **large** dimers. **Collisional energy transfer** excites **internal** **vibrational** modes that **accelerate** **decomposition** to **monomers** relative to **isolated** dimers. **Heavier** projectiles are more effective at **promoting decomposition** at comparable **collision** conditions. **Larger** dimers and **lower** temperatures **reduce** **decomposition rates**, but **any** gas-phase collisions **net destabilize** dimers compared with **vacuum** baselines discussed in the article. The **PCCP** paper explicitly motivates **engine**-relevant **collision** **frequencies** by citing **Frenklach**-style arguments that **N\(_2\)** **collision** **times** can be **comparable** to **dimer** **lifetimes** under **high-pressure** **combustion**, justifying **gas-mediated** **kinetic** **models** beyond **vacuum** **dimerization** **alone**. **Projectiles** beyond **N\(_2\)** (**CO**, **CO\(_2\)**) extend the same **framework** to **oxidizing** versus **inert** **bath** compositions.

## Limitations

ReaxFF accuracy for PAH–gas collisions should be benchmarked against higher-level QM for selected configurations.

## Relevance to group

Extends ReaxFF soot-precursor work by explicitly coupling PAH dimers to realistic gaseous collision partners relevant to combustion environments.

## Citations and evidence anchors

- DOI: [10.1039/C8CP07060A](https://doi.org/10.1039/C8CP07060A)

## Related topics

- [[reaxff-family]]
