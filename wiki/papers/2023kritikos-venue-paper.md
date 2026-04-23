---
id: paper:2023kritikos-venue-paper
type: paper
title: "Atomistic insight into the effects of electrostatic fields on hydrocarbon reaction kinetics"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:reactive-md
  - keyword:dft-static
  - keyword:lammps
  - keyword:charge-equilibration
candidate_tags: []
source_refs: []
doi: "10.1063/5.0134785"
year: 2023
authors:
  - "Efstratios M. Kritikos"
  - "Aditya Lele"
  - "Adri C. T. van Duin"
  - "Andrea Giusti"
venue: "J. Chem. Phys."
pdf_sha256: "dcf24cde48ae28cab171a0b9cbe79838072e2038bd1be6377b170361fdf0eefc"
pdf_path: "papers/Kritikos_efield_combustion_JCP_2023.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023kritikos-venue-paper -->

## Summary

**Reactive MD (ReaxFF CHO-2016 hydrocarbon combustion field)** and **DFT** are cross-compared to assess **field-induced polarization** and the coupling of **external electrostatic fields** to **reaction pathways** and **transport** in **hydrocarbon oxidation / pyrolysis** contexts, culminating in **large-scale** **n-dodecane + O₂** combustion simulations with imposed **electric fields**. The work targets settings such as **plasma-assisted** or **field-enhanced** combustion where **explicit** electrostatic coupling may not be negligible relative to thermal driving forces.

The *J. Chem. Phys.* abstract motivates the study by noting that **electric fields** can alter **reaction rates** even when **thermal** effects are modest, and that **atomistic** models must self-consistently treat **charge redistribution**, **collisional energy transfer**, and **field–dipole** alignment for **polar** versus **nonpolar** species in **oxidizing** environments.

## Methods

### Charge response validation (A/C)

Compare **ReaxFF QEq** under **E-fields** to **DFT** **charge partitioning** schemes for molecular/cluster **polarization** (partitioning choices in the article).

### Barrier shifts (C)

**NEB**-type paths for selected steps under **oriented fields** to quantify **oxidation** vs **pyrolysis**-class **barrier** changes.

### Molecular collision tests (B)

**ReaxFF** **bimolecular** trajectories separating **Lorentz** vs **Coulomb** contributions vs **orientation**/**polarity**.

### Large-scale combustion MD (B)

**n-Dodecane/O\(_2\)** with **strong E-fields**; monitor **translational/rotational** vs **vibrational** energy channels.

### Validation ladder

Small-system **charge**/**barrier** checks before **macroscale** reactive cells to avoid **thermal** masking of **field** effects.

### 1 — MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** with the **ReaxFF CHO-2016** hydrocarbon **combustion** field. **Systems & composition:** subsections span **QEq**/charge benchmarks, **bimolecular** **collision** cells, and **large-scale n-dodecane + O\(_2\)** **combustion** with **imposed static external electric fields** (magnitude, orientation, and duration are in the JCP article, not re-tabulated here). **Boundaries / periodicity:** **PBC** for gas-phase **combustion** MD as implemented in the paper. **Ensemble, timestep, production length, thermostat, barostat:** the **large** **n-dodecane**/**O\(_2\)** **combustion** **MD** and the **cluster** **tests** are run with **LAMMPS**-standard **NVT**/**NVE**-like **choices** (per scenario) over **ps**–**ns** **spans** as tabulated; **N/A** for re-listing every **NVT** **thermostat** and **ns** **duration** in this **wiki** (see **JCP**). **Temperature / pressure / stress:** set by the scenario in each section (e.g. combustion **vs** cluster tests); **N/A** for a single table on this page. **Electric field:** **central** to the work—**oriented** fields in **MEP**/**NEB** analyses, **Lorentz**-related effects in bimolecular tests, and **field-coupled** **macroscale** **reacting** flows. **Coulomb / QEq update:** **ReaxFF** charge equilibration compared to **DFT** partitioning. **Shear, shock:** **N/A** in the abstracted scope. **Enhanced-sampling MD:** **N/A** — the pathway tool is **NEB** (minimization/path search), not umbrella metadynamics in MD.

### 2 — Force-field training

**N/A** — the study **uses** a published **ReaxFF** **CHO** line; training new parameters is not the focus.

### 3 — Static QM (DFT)

**DFT** supplies reference **charges** and supports **MEP**/**NEB** barriers under **fields** for **oxidation** **vs** **pyrolysis** classes. **N/A** — program, **functional**/**basis**/**k**-sampling, and all numerical settings appear in the JCP main text and SI, not in this short wiki page.

## Findings

### QEq vs DFT

**Field-induced charges** from **ReaxFF** track **DFT** trends sufficiently (per abstract) to justify large reactive runs.

### Pathway selectivity

**MEP** results suggest fields can **accelerate/inhibit oxidation** more than **pyrolysis** steps in their **C/H electronegativity** argument.

### Species polarity

**Polar** molecules align and show **kinetic** changes; **apolar** species respond mainly through **weak induced** dipoles.

### Combustion-scale observations

Strong fields couple **translation/rotation** to **charge transfer** and can **reduce vibrational** excitation via **stabilization**-type effects in their analysis.

### Design knob

**Field alignment** with **dipoles** can bias **rotational** vs **vibrational** heating by species **polarity**.

The **abstract-level** **takeaway** repeated in the **JCP** entry is that **electrostatic** biases can be **nonthermal** levers on **reaction** **selectivity** when **polarization** and **collisional** energy partitioning are treated together—motivating the **validation ladder** (small **cluster** tests before **large** **combustion** cells) described above.

## Limitations

Field strengths and system sizes may not map directly to laboratory flames; ReaxFF chemistry uncertainties remain for **combustion** under extreme conditions.

## Relevance to group

**van Duin**-authored **electrostatic-field–coupled ReaxFF combustion** study with **Lele**; complements other **field-coupled reactive MD** threads in the corpus.

## Citations and evidence anchors

- DOI: [10.1063/5.0134785](https://doi.org/10.1063/5.0134785)

## Related topics

- [[2023kritikos-venue-paper-2]]
- [[reaxff-family]]
