---
id: paper:2015fantauzzi-venue-surface-buckling
type: paper
title: "Surface Buckling and Subsurface Oxygen: Atomistic Insights into the Surface Oxidation of Pt(111)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:catalysis-surface
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
source_refs: []
doi: "10.1002/cphc.201500527"
year: 2015
authors:
  - "Donato Fantauzzi"
  - "Jonathan E. Mueller"
  - "Lehel Sabo"
  - "Adri C. T. van Duin"
  - "Timo Jacob"
venue: "ChemPhysChem"
pdf_sha256: "09d42133904593b44dca12903d72a3fc8f85d23bd34ecfb991ecec5a7027af43"
pdf_path: "papers/Fantauzzi_et_al-2015-ChemPhysChem.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015fantauzzi-venue-surface-buckling -->

## Summary

**Pt(111)** oxidation is a textbook surface-science problem, yet reconciling **coverage-dependent** structures, **subsurface** oxygen, and **temperature-programmed desorption (TPD)** experiments across literature datasets remains nontrivial. This **ChemPhysChem** article develops a unified **ReaxFF** picture for **O/Pt(111)** from **low** to **~1 monolayer-class** coverages, including **buckled** surface oxides, **subsurface** oxygen, and **place-exchange** motifs informed by prior DFT surveys. **Adri C. T. van Duin** coauthors, connecting the work to the Penn State reactive force-field lineage. The authors compute **reaction and diffusion barriers** among key structures and feed those barriers into a **first-principles-based TPD model** compared to measured spectra for selected initial oxygen preparations.

## Methods

### MD application (atomistic dynamics)

**N/A —** the paper’s core computations are **static ReaxFF energetics + barrier/kinetics analysis** feeding a **TPD model**, not long finite-temperature **molecular dynamics** trajectories with reported **timestep**, **thermostat**, and **ns**/**ps** **production** lengths. **ReaxFF** energy and force evaluations are used on **Pt(111)** **PBC slab supercells** with oxygen at multiple coverages (atom counts in the PDF/SI), without **LAMMPS**-style production **MD**, **NPT** control, applied electric fields, or time-stamped dynamical trajectories.

### Force-field training

**N/A —** uses a **published Pt/O ReaxFF** parameterization (“recently developed” in the sense of the article’s introduction) rather than deriving a new parameter set in this manuscript.

### Static QM / DFT (validation layer)

- **DFT spot checks:** the **Supporting Information** contains **DFT validations** of **formation energies** for selected **high-symmetry** structures along the convex hull (as stated in the main text), used to anchor key ReaxFF energetics.

### Kinetics + TPD modeling protocol (as authored)

- **Structures / pathways:** enumerate **O/Pt(111)** motifs spanning **adsorbate-only**, **buckled high-coverage oxides**, **subsurface oxygen**, and **place-exchange**-like configurations; construct a **convex hull** in coverage–energy space to identify stable phases and coexistence regions.
- **Barriers / prefactors:** perform **ReaxFF geometry optimizations** and **transition-state searches** for bottleneck steps; compute **ReaxFF vibrational frequencies** for **TST prefactors** (Eq. (4) and Table 1 in the article).
- **TPD simulation:** integrate a **first-principles-based TPD model** (Voter-type TST framework as cited) using a **1 K s⁻¹** heating rate and parameters tabulated in **Table 1**, then compare simulated **O₂ TPD** traces to experimental spectra for multiple initial coverages.

## Findings

- **Phase diagram / motifs:** ReaxFF identifies multiple **stable/regime-separated** surface phases up to ~**1 ML O**-equivalent coverage, including **buckled** and **subsurface-O** arrangements that reorganize the **Pt(111)** surface beyond simple adsorbate lattices.
- **TPD linkage:** the barrier + prefactor network is used to simulate **TPD peak structure** (including multi-peak composition) in qualitative-to-quantitative agreement with selected experimental datasets referenced in the paper.
- **Interpretive claim:** **buckling** and **subsurface oxygen** are argued to be mechanistically important for reconciling **STM/TPD** phenomenology that is easy to misread from **isolated DFT** adsorption studies alone.
- **Comparisons:** simulated spectra are compared **vs** published **TPD**/**STM** experiments (explicit references in the article).
- **Sensitivity:** peak shapes depend on **heating rate** (**1 K s⁻¹** in the model), **coverage**, and the assumed **reaction** network.
- **Limitations / corpus honesty:** **DFT** validation lives largely in **SI**; cite the **PDF**/**SI** for numerical **barrier** tables.

## Limitations

**ReaxFF** accuracy is bounded by its **training scope**; **electrolyte/electrochemical** environments are outside the **UHV TPD**-centric validation shown here.

## Relevance to group

Demonstrates **van Duin-group** **ReaxFF** deployment for **noble-metal oxidation** with explicit **experimental** desorption constraints.

## Citations and evidence anchors

- DOI: [10.1002/cphc.201500527](https://doi.org/10.1002/cphc.201500527)

## Related topics

- [[reaxff-family]]
