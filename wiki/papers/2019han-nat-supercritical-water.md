---
id: paper:2019han-nat-supercritical-water
type: paper
title: "Supercritical water gasification of naphthalene over iron oxide catalyst: A ReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - material:oxide
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:catalysis-surface
  - keyword:nvt-simulation
source_refs: []
doi: "10.1016/j.ijhydene.2019.09.215"
year: 2019
authors:
  - "You Han"
  - "Tengzhou Ma"
  - "Fang Chen"
  - "Wei Li"
  - "Jinli Zhang"
venue: "International Journal of Hydrogen Energy"
pdf_sha256: "a8210bce3df5e55451087fc275f81398c9440ec9a283523aa58c581eb8f9451e"
pdf_path: "papers/ReaxFF_others/Han_Fe_supercritical_IJHE_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019han-nat-supercritical-water -->

## Summary

**ReaxFF MD** (ADF/SCM) explores **iron-oxide-catalyzed supercritical water gasification (SCWG)** of **naphthalene** as a **PAH** surrogate. **SCW** supplies **H** for **H\(_2\)** and **O** for **CO** while **Fe\(_2\)O\(_3\)** clusters provide **labile oxygen** and catalytic **C–C** activation. Simulations sweep composition/temperature to map **H\(_2\)/CO** evolution, **catalyst deactivation** (carbon, **O** vacancy, **Fe** loss), and **O\(_2\)** **regeneration** pathways. **International Journal of Hydrogen Energy** framing connects **SCWG** to **renewable** **waste** streams where **PAHs** model **tar** chemistry from **biomass** **pyrolysis** condensates.

## Methods

- **Catalyst:** **α-Fe\(_2\)O\(_3\)**-derived **cluster** (~**15 Å** diameter) after heat/cool protocol + minimization (details in **SI**).
- **Cell:** **Periodic** **60×60×60 Å\(^3\)** boxes with **random** reactant placement (ADF library).
- **Potential:** **ReaxFF** parametrization from **Shin et al.** (Fe–O–C–H).
- **MD:** Energy minimization → heat **0–300 K** (**30 K/ps**) → hold **300 K** for **20 ps** → ramp to target (**100 K/ps**) → **800 ps** production at **3000 K** (main text); **NVT**, **Berendsen** thermostat **100 fs** damping, **0.25 fs** timestep. **ADF** ReaxFF module for integration and analysis (**Table 1** cases).
- **Rationale:** Elevated **T** accelerates chemistry to fit **~ns** windows (discussion cites Voter et al.).

**Engine, cell, and pressure targets.** **Reactive molecular dynamics** uses the **ADF**/**SCM** **ReaxFF** module (not **LAMMPS** for the main production runs tabulated) in **periodic** **60 Å** cubic **cells** with **α-Fe₂O₃** clusters and **random** reactant placement as above. **Atoms:** total counts follow from stoichiometries in **Table 1** of the article. **NVT** at **3000 K** with **Berendsen** thermostat (**100 fs** damping) and **0.25 fs** **timestep** for **800 ps** **production** after heating ramps. **Barostat / hydrostatic pressure:** **N/A** — **constant-volume** **NVT** without **GPa** servocontrol in the summarized cases. **External electric field:** **N/A**. **Enhanced sampling:** **N/A** — brute-force **MD** at elevated **temperature** to accelerate chemistry.

## Findings

- **Synergy** between **SCW** and **Fe oxide** promotes **NAP** conversion and **H\(_2\)/CO** formation.
- **Water** acts as both **H** and **O** source; **oxide** supplies **lattice oxygen**, activates **SCW**, and weakens **C–C** bonds.
- **Parameter trends:** More **H\(_2\)O** raises **H\(_2\)**/**CO** yields and **lattice-O** replenishment but can **slow** **CO** generation rate; **high NAP** loading increases **H\(_2\)** recovery yet lowers **carbon gasification efficiency**.
- **Deactivation:** **Carbon deposition**, **lattice oxygen** depletion, **Fe** loss; **SCW** mitigates **Fe** loss; **calcination in O\(_2\)** clears **C** and restores **O**. **Parameter sweeps** over **naphthalene** loading and **water** fraction illustrate trade-offs between **H\(_2\)** **yield** and **carbon** **gasification** efficiency quoted in the abstract-level discussion.

## Limitations

**3000 K**, **sub-ns** trajectories are **accelerated** conditions; quantitative agreement with **pilot SCWG** requires extrapolation.

**Continuous** **flow** **reactors**, **sulfur**/**alkali** **poisons**, and **supported** **catalyst** **morphologies** differ from **isolated** **Fe\(_2\)O\(_3\)** **clusters** in **periodic** boxes; scale **Fe**/**O** **stoichiometry** trends cautiously to **fixed-bed** **pilot** units.

**Char** **gasification** **kinetics** for **lignin**/**cellulose** **oligomers** beyond **naphthalene** may require **additional** **ReaxFF** **training** if **oxygenated** **PAH** **intermediates** dominate **tar** under **real** **feedstocks**.

**Pressure** **vessels** for **SCW** **operation** introduce **mechanical** **constraints** and **concentration** **gradients** absent from **uniform** **periodic** **supercells** in the **MD** **study**.

## Relevance to group

Uses **van Duin-lineage** **ReaxFF** Fe parameters extended by **Shin** and collaborators for **heterogeneous** **SCW** chemistry.

## Citations and evidence anchors

- `papers/ReaxFF_others/Han_Fe_supercritical_IJHE_2019.pdf`

## Related topics

- [[reaxff-family]]
