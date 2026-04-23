---
id: paper:2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion
type: paper
title: "Cathodic Corrosion at the Bismuth–Ionic Liquid Electrolyte Interface under Conditions for CO2 Reduction"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:dft-static
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:catalysis-surface
source_refs: []
doi: "10.1021/acs.chemmater.8b00050"
year: 2018
authors:
  - "Jonnathan Medina-Ramos"
  - "Weiwei Zhang"
  - "Kichul Yoon"
  - "Peng Bai"
  - "Ashwin Chemburkar"
  - "Wenjie Tang"
  - "Abderrahman Atifi"
  - "Sang Soo Lee"
  - "Timothy T. Fister"
  - "Brian J. Ingram"
  - "Joel Rosenthal"
  - "Matthew Neurock"
  - "Adri C. T. van Duin"
  - "Paul Fenter"
venue: "Chem. Mater."
pdf_sha256: "2f06941fb0d800186e940881ae40a5df8ef3a28444c7a9db780b319793bfec71"
pdf_path: "papers/MedinaRamon_ChemMat_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2018jonnathan-medina-ram-chem-mater-2-cathodic-corrosion -->

## Summary

The paper investigates **cathodic corrosion** of **bismuth** in contact with an **ionic-liquid electrolyte** under **CO₂ electroreduction**–relevant **potentials**, combining **ReaxFF molecular dynamics** and **DFT** to connect **interfacial disorder**, **charge state**, and **metal migration** into the **electric double layer**. **ReaxFF** is used to capture **large-scale ionic rearrangements** and **surface roughening** at **negative bias**, while **DFT** supports **local bonding** interpretations (e.g., **Bi migration** motifs). **Adri C. T. van Duin** is among the coauthors bridging **reactive MD** with **electrocatalysis-focused** collaborators. The study targets a failure mode—metal etching under cathodic bias—that can masquerade as poor catalytic selectivity if interfacial reconstruction is ignored. **CO₂RR** literature often emphasizes **C–C** coupling and **Faradaic efficiency**, but **catalyst** **durability** under **reducing** bias can be limited by **metal** **dissolution** when **ionic liquids** penetrate and destabilize **near-surface** **Bi** layers.

## Methods

**MD application (ReaxFF, electrified Bi–ionic-liquid interface).** **LAMMPS**-style **ReaxFF MD** treats **Bi(001)** **slabs** solvated with **ionic-liquid** species relevant to **CO\(_2\)** **electroreduction** conditions (**atom** counts and **supercell** vectors in *Chem. Mater.* **Methods**). Cells use **three-dimensional periodic boundary conditions (PBC)** for the **slab**/**electrolyte** geometry unless the article specifies otherwise. **Cathodic** bias is imposed through **charge**, **field**, or **excess-electron** protocols as defined in the paper—an **approximate constant-potential** treatment rather than a full **ab initio** **continuum** **electrode** solver (see **Limitations**). **Ensemble:** **NVT**-class trajectories with thermostat parameters and **timestep** in **fs** tabulated in **Methods**/**SI** (`pdf_path`); target **temperature** (often near **300 K** unless the article specifies other **NVT** set points) is defined there. **Duration:** production segment lengths in **ps**/**ns** are given in the **peer-reviewed PDF**—not duplicated numerically here. **Barostat:** **N/A — NPT** isotropic volume fluctuation is not the focus for the quoted **interface** **MD**. **Pressure / stress:** **N/A — target hydrostatic pressure (bar/GPa)** is not a headline control beyond **interfacial** **stress** diagnostics discussed in the article. **Shear / strain rate:** **N/A**. **Replica / enhanced sampling:** **N/A — umbrella sampling, metadynamics, or replica exchange** is not highlighted in the main text—confirm **SI** if any rare-event workflow appears.

**Static QM / DFT.** Complementary **DFT** uses the **functional**, **basis**, and **k-mesh** choices stated in *Chem. Mater.* to evaluate **adsorption** and **migration** energetics for **Bi** and **electrolyte** fragments where **ReaxFF** needs **QM** anchors.

**Trajectory diagnostics.** **RMS** **surface** **roughness**, **coordination** statistics, and **Bi** **migration** metrics versus **cathodic** severity separate **reversible** elastic motion from **irreversible** **etching**-like events.

**Experiments.** **Synchrotron**/**spectroscopy**-motivated validation and related **experimental** discussion appear in the article—**beamline** conditions and **sample** protocols belong to `pdf_path`.

## Findings

**Outcomes.** More **negative** **surface** **charge** correlates with **increased** **RMS** **roughness** and **Bi** **migration** into the **electric double layer**, i.e., **cathodic corrosion** rather than a static **passive** **interface**.

**Comparisons.** **DFT** fragments and **synchrotron**/**spectroscopy**-motivated **experiment** in the article **benchmark** the qualitative **ReaxFF** trends.

**Sensitivity.** **Bias** severity and **electrolyte** composition control how quickly **disorder** accumulates in the short **MD** windows shown.

**Limitations and PDF grounding.** **Constant-potential** approximations and **IL** **force-field** fidelity cap predictive **quantitative** accuracy; **operando** imaging remains necessary. All **numerical** protocols: **`pdf_path`**.
## Limitations

- **Electrochemical potential control** in **classical reactive MD** is approximate; compare **DFT** and **experiment** where quoted in the paper.
- **Ionic liquid force-field** fidelity for **long-time** dynamics may require **validation** on **subset processes**.
- CO₂RR selectivity metrics from experiment can be convolved with cathodic corrosion that roughens Bi; the MD story highlights atomic-scale roughening trends but does not replace operando microscopy for linking surface area evolution to Faradaic efficiency.

## Relevance to group

Demonstrates **ReaxFF** applied to **electrified interfaces** with **ionic liquids**, a recurring theme in **electrochemistry + reactive MD**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.chemmater.8b00050` (`papers/MedinaRamon_ChemMat_2018.pdf`).

## Reader notes (navigation)

- Bi–ionic-liquid **cathodic corrosion** under CO₂RR-relevant bias: cluster with [[batteries-interfaces-reaxff]] and [[2018dengpan-dong-in-this-stud-multiscale-modeling]] (ionomer electrochemistry).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
