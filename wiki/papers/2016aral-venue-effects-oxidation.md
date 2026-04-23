---
id: paper:2016aral-venue-effects-oxidation
type: paper
title: "Effects of oxidation on tensile deformation of iron nanowires: Insights from reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:alloys-metallurgy
  - domain:mechanics-tribology
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:oxide-surface
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1063/1.4963828"
year: 2016
authors:
  - "Gurcan Aral"
  - "Yun-Jiang Wang"
  - "Shigenobu Ogata"
  - "Adri C. T. van Duin"
venue: "J. Appl. Phys."
pdf_sha256: "3e2ae8f4e18ca59279003edddf9b5197ac5e5333aac4bf01b913850298ffc12e"
pdf_path: "papers/Aral_Fe_nanowires_JAP_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2016aral-venue-effects-oxidation -->

## Summary

Aral *et al.* couple **oxidation chemistry** with **tensile deformation** of **iron nanowires** at **room temperature** using **variable-charge ReaxFF molecular dynamics**, comparing **inert/vacuum** conditions to **dry O\(_2\)** exposure that builds **oxide** shells on the **Fe** surface. The study asks how **oxide thickness** modifies **yield stress**, **critical strain**, **twinning**, and the onset of **plasticity** in **nanoscale** **Fe**, where **surface** effects already dominate mechanical response even without oxidation. **Adri C. T. van Duin** is a coauthor, and the work exemplifies the group’s use of **reactive MD** to treat **metal–oxygen** bond formation concurrently with **mechanical loading**, rather than preoxidizing to a fixed stoichiometry and then deforming rigidly.

## Methods

### MD application (atomistic dynamics)

**Force field:** **Variable-charge ReaxFF** in **LAMMPS** (parallel implementation cited in §II) with **EEM/QEq-style** charge updates each step as described in the article.

#### Oxidation stage (build oxide shells on bcc Fe nanowires)

- **System:** Cylindrical **Fe** nanowire, **bcc** lattice constant **a = 2.86 Å**, **24,050 Fe** atoms, diameter **5.0 nm**, length **14.3 nm** along **[001]** (tensile axis in later mechanical tests).
- **Gas environment:** **2000 O₂** molecules placed randomly above the wire surface to represent **dry O₂** exposure.
- **Target oxide thicknesses:** Growth is halted at three nominal **oxide shell** thicknesses quoted in the abstract (**≈4.81 Å**, **≈5.33 Å**, **≈6.57 Å**) by removing remaining gas-phase oxygen once the desired shell is achieved (§III).
- **Ensemble / thermostat:** **NVT** at **T = 300 K** with a **Nosé–Hoover thermostat chain** applied to **all atoms** during oxidation; **3D periodic** boundaries (§III).
- **Duration (example trajectory):** The text reports an oxidation segment consuming **2870 O** atoms over **3.35 ns** for the illustrated core–shell formation case (figures in §III/SI).
- **Barostat / pressure:** **N/A — oxidation segment is NVT** without documented hydrostatic pressure targeting beyond periodic gas/solid setup.

#### Mechanical testing (tensile pulls on pure and oxide-coated wires)

- **Preparation:** **Conjugate-gradient** energy minimization for each wire; **NPT** relaxation at **300 K** to relieve construction stresses (§III).
- **Tensile MD:** **NVT** at **300 K** with **Nosé–Hoover** thermostat; **velocity Verlet** integration with **Δt = 0.5 fs**; charges updated every MD step as in ReaxFF/EEM (§III).
- **Strain / duration:** **Uniaxial constant strain rate 0.01% ps⁻¹** (**10⁸ s⁻¹**) applied along **[001]** by rescaling the periodic box up to **16%** engineering strain; total tensile segment **1.5 ns** (§III).
- **Stress:** **Virial** atomic stresses averaged and corrected to **engineering stress** using the true wire volume (§III).
- **Boundaries after oxidation:** For tensile, **PBC only along the axial (loading) direction** with **free** lateral boundaries to reduce spurious lateral stress transmission (§III).
- **Electric field:** **N/A — not used.**
- **Replica / enhanced sampling:** **N/A — not used.**

### Force-field training

**N/A — not a parameterization paper**; the manuscript applies an established **ReaxFF Fe/O** description for coupled oxidation + mechanics (see references in §II for parameter origins).

### Static QM / DFT

**N/A — no central DFT production results** for the nanowire oxidation/tension trajectories in the sense of AGENTS block 3; QM appears only as background for **ReaxFF** validation references.

## Findings

- **Mechanical softening with oxidation:** Increasing **oxide shell thickness** on the modeled **Fe** nanowires **reduces yield stress** and **critical strain** relative to thinner shells / cleaner surfaces (abstract + §IV narrative).
- **Earlier plasticity:** Oxidized wires yield at **lower applied strain** and require **lower external stress** to initiate plasticity, i.e., the oxide shell shifts the onset of plastic deformation earlier under the simulated conditions.
- **Twinning:** **Twinning** remains important for both bare and coated wires, but **twin nucleation** occurs at **lower strain** when **oxide thickness** increases (abstract-level claim; see §IV for microstructural snapshots and stress–strain curves).
- **Oxidation kinetics context:** The oxidation portion is described as showing **fast initial oxidation** followed by **slow growth** consistent with **logarithmic-growth** discussions in the article (§IV; see SI figures referenced there).

## Limitations

**Nanowire** models omit **grain boundaries** and **alloying** common in structural **steels**; **strain rates** are MD-accessible and may exceed experiment. When comparing to **oxidation-first** experiments, note that the simulation protocol may **pre-oxidize** or **co-oxidize** relative to real **atmospheric** exposure schedules.

## Relevance to group

Direct **van Duin-group** collaboration on **ReaxFF** modeling of **metal oxidation** coupled to **nanomechanics**.

## Citations and evidence anchors

- DOI: [10.1063/1.4963828](https://doi.org/10.1063/1.4963828)

## Related topics

- [[reaxff-family]]
