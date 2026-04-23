---
id: paper:2015zhu-physics-lett-molecular-dynamic
type: paper
title: "Molecular dynamic simulation of thermite reaction of Al nanosphere/Fe2O3 nanotube"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:organics-polymers-pyrolysis
  - task:application
  - scale:atomistic
  - material:alloy-bulk
paper_keywords:
  - keyword:reaxff-application
  - keyword:energetic-materials
  - keyword:combustion
  - keyword:lammps
  - keyword:reactive-md
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.physleta.2015.09.041"
year: 2015
authors:
  - "Zhi-Yang Zhu"
  - "Bo Ma"
  - "Cui-Ming Tang"
  - "Xin-Lu Cheng"
venue: "Phys. Lett. A"
pdf_sha256: "59f83c3f0e197d591d058e756f6d279a6f8615ccc73a5bd3801ff0b813e1b752"
pdf_path: "papers/ReaxFF_others/Zu_BoMa_Al2O3_Fe_thermite_PhysicsLetterA_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2015zhu-physics-lett-molecular-dynamic -->

## Summary

**LAMMPS** molecular dynamics with a **ReaxFF** parameterization for **Al–Fe–O** studies **thermite-type** reaction of an **aluminum nanosphere** with a **hematite (Fe\(_2\)O\(_3\)) nanotube**, a geometry chosen to expose **nanoscale** transport and **interface-limited** oxidation relative to bulk **Al/Fe\(_2\)O\(_3\)** foils. The authors monitor **bond-order** evolution, programmed **heating**, and **energy release** to connect **ignition delay**, **ignition temperature**, and **multistep** chemistry to **nanostructure** and simulation knobs such as **initial separation** and **heating rate**. The framing emphasizes that **nanothermite** behavior can depart from a single global **redox** equation because **O** can evolve from **hematite** at high temperature and because **alloying** channels contribute additional heat.

## Methods

### MD application (atomistic dynamics)

Zhu *et al.* use **LAMMPS** with the **Al–Fe–O ReaxFF** parameterization of **van Duin *et al.*** (§2 of *Phys. Lett. A* **380**, **194–199**). The model is a **non-periodic** **Al/Fe₂O₃** cluster: an **α-Fe₂O₃** nanotube (**753 Fe**, **468 O**) with length **3 nm**, outer diameter **3 nm**, and wall thickness **0.5 nm**, plus an **Al** nanosphere (**555 Al**, diameter **2.6 nm**), **1776 atoms** total. **System1–System3** differ only in the **initial sphere–tube gap** (**1.0**, **1.5**, **2.0 nm**).

All runs use the **canonical (NVT)** ensemble, **Δt = 0.5 fs**, and three stages: **(1)** relaxation at **300 K** for **5 ps**; **(2)** heating in **50 K** increments up to the ignition temperature at **3 K/ps** or **0.5 K/ps** (ignition is identified from the onset of rapid **Al–O** bond formation in step 3); **(3)** **300 ps** of reactive evolution while tracking bond populations and energetics. **Barostat / controlled pressure:** **N/A —** the workflow is **NVT** on an isolated cluster, not constant-pressure bulk. **Thermostat:** the article states **NVT** temperature control (**300 K** hold; stepped heating) but **does not name** the thermostat algorithm in §2—reproduce from **`pdf_path`** if your integrator requires an explicit coupling scheme. **Electric field:** **N/A — not used.** **Replica / enhanced sampling:** **N/A — not used.** **Analysis** follows **Al–O**, **Al–Al**, **Al–Fe**, **Fe–O**, **Fe–Fe**, and **O–O** bond counts versus time to locate ignition and classify chemistry.

### Force-field training

**N/A — application paper** using a literature **ReaxFF** parameter set for **Al/Fe/O**; no new ReaxFF optimization workflow is reported as the contribution.

### Static QM / DFT

**N/A — not a DFT study**; reactive dynamics are **ReaxFF MD** only in this letter.

## Findings

- **Sensitivity (geometry):** Increasing the **initial sphere–tube separation** raises **ignition temperature** and lengthens **ignition delay** (Systems **1 → 3** ordering in the abstract-level summary).
- **Sensitivity (heating rate):** Lowering the heating rate from **3 K/ps** to **0.5 K/ps** **lowers** the quoted **ignition temperature** for **System2** (authors relate this qualitative trend to experimental discussions of heating-rate effects).
- **Mechanism picture:** Under **~1450 K** (System2 example at **3 K/ps**), **O₂** release from the **hematite** nanotube appears in the trajectory analysis; the authors describe the overall event as a **multiphase** process rather than a single global **thermite** stoichiometry.
- **Energetics:** **System2** is associated with **~3.96 kJ/g** **energy release** in the abstract, with additional heat tied to **alloying** channels beyond the nominal redox pair.
- **Authored contrast to textbook thermite:** The letter argues nanoscale **Al/Fe₂O₃** chemistry is **pathway-dependent** and **does not** collapse to the simple analytical **thermite** equation used for macroscopic mixtures.

## Limitations

The corpus PDF filename uses a **2016** volume year while the DOI landing metadata can read as **2015** receipt—cite by **DOI** and volume **380**, pages **194–199**. Any **non-periodic** cluster finite-size effects and **3D** radiative/pressure coupling of real thermites are not represented at atomistic cluster scale; quantitative ignition temperatures are **model- and protocol-dependent**.

## Relevance to group

Uses ReaxFF (cited van Duin et al.) for nanoscale thermite chemistry relevant to energetic materials and reactive MD benchmarking.

## Citations and evidence anchors

- DOI: [10.1016/j.physleta.2015.09.041](https://doi.org/10.1016/j.physleta.2015.09.041)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
