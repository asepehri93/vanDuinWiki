---
id: paper:2018patra-acs-defect-dynamics
type: paper
title: Defect Dynamics in 2-D MoS2 Probed by Using Machine Learning, Atomistic Simulations,
  and High-Resolution Microscopy
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:2d-layered
- domain:ml-atomistic
- material:tmd
- method:reaxff
- task:experiment-integrated
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:lammps
- keyword:2d-materials
- keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: 10.1021/acsnano.8b02844
year: 2018
authors:
- Tarak K. Patra
- Fu Zhang
- Daniel S. Schulman
- Henry Chan
- Mathew J. Cherukara
- Mauricio Terrones
- Saptarshi Das
- Badri Narayanan
- Subramanian K. R. S. Sankaranarayanan
venue: ACS Nano
pdf_sha256: 829b5dfbeda616a0856d5605b16cf53c3edd7511db65754d43cae2e77c231e6a
pdf_path: papers/ReaxFF_others/acsnano_MoS2_ReaxFF_ML_Terrones_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018patra-acs-defect-dynamics -->

Genetic-algorithm searches with ReaxFF energies, large-scale ReaxFF molecular dynamics in LAMMPS, and in situ HRTEM are combined to map how sulfur vacancies organize in monolayer MoS2 and how those defects participate in the semiconducting 2H to metallic 1T transition.

## Summary

The study couples supervised learning style genetic algorithms (GA) with ReaxFF and microscopy to describe sulfur-vacancy ordering, dynamics, and their connection to the 2H→1T transition in monolayer MoS2. GA searches evolve binary “genomes” for sulfur occupancy on a triangular lattice using ReaxFF energies in LAMMPS (population 32, ~100-generation convergence) on ~5.2 nm × 5.8 nm sheets. MD uses the MoS2 ReaxFF parametrization in the NPT ensemble (300–1500 K, ambient pressure) on large defective sheets (up to ~21.8 nm × 24.9 nm; 17,140 atoms) with Nosé–Hoover thermostat and barostat. Experiments use electro-ablated monolayer MoS2 on grids for AC-S/TEM imaging.

Abstract-level context notes that **sulfur vacancies** are common in **MoS\(_2\)** and can reorganize under beam or thermal stimuli, so connecting **GA**-selected low-energy vacancy motifs with **in situ** microscopy and large-cell reactive MD targets the **2H** semiconducting versus **1T** metallic phase competition in defective monolayers.

## Methods
**1 — MD application (defective MoS₂).** **ReaxFF** (**Mo–S** parametrization cited from **JPCL 2017**) is run in **LAMMPS** on **periodic monolayer MoS₂** supercells up to **~21.8 nm × 24.9 nm** (**17 140 atoms** in the large-cell example) prepared with **GA-derived vacancy line patterns**. **MD** uses the **isotropic NPT** ensemble from **300–1500 K** at **ambient pressure** with **Nosé–Hoover** thermostat and barostat as stated in *ACS Nano*. **Timestep:** **N/A —** the accessible PDF text for this pass does not spell out **Δt**; confirm in the **article/SI** before reproducing runs. **Duration:** reactive **MD** segments span the **picosecond–nanosecond** range reported for **2H/1T** nucleation studies (exact lengths in **PDF**/**figures**). **PBC:** **in-plane periodic** monolayer cells. **Electric fields / enhanced sampling:** **N/A —** not used in the MD workflow summarized here.

**2 — Genetic algorithm search.** **GA** evolves binary **S-occupancy** genomes on a triangular lattice (**population 32**, **~100 generations**) using **ReaxFF** energies evaluated in **LAMMPS**.

**3 — Microscopy.** **Electro-ablated** monolayer **MoS₂** on **TEM grids** is imaged with **aberration-corrected STEM/TEM** under controlled dose.

**4 — Force-field training / DFT-only blocks.** **N/A —** this work **applies** a published **ReaxFF** and cites **DFT** for select energetic checks rather than presenting a new FF fit or standalone static-QM study.

## Findings
**Outcomes / mechanisms:** **GA**, **HRTEM**, and **MD** consistently indicate **sulfur vacancies** organize into **extended lines** as favored motifs. **Electron-beam** exposure localizes **2H → 1T** transformations near these **line defects**; **MD** shows how local **bond rearrangements** nucleate **1T** domains, with **temperature** and **defect density** influencing finite **1T** fractions.

**Comparisons:** **simulation** motifs are compared to **in situ** micrographs and to **DFT** energy ordering cited in the article.

**Sensitivity:** **defect density** and **temperature** (up to **1500 K** in MD) modulate **1T** stabilization.

**Limitations / outlook:** **ReaxFF** remains approximate versus **DFT** for **phase energetics**; long-time **defect diffusion** may need additional sampling strategies beyond the reported MD segments.

**Corpus honesty:** large-cell dimensions and **GA** parameters are taken from the **ACS Nano** main text; **timestep** must be read from **SI** if not visible in your local **PDF** export.

## Limitations

ReaxFF accuracy for MoS2 phase energetics is approximate relative to DFT; long-time defect evolution may require enhanced sampling beyond the MD segments reported.

## Relevance to group

Uses the MoS2 ReaxFF line developed in work connected to van Duin-group parametrization (cited ReaxFF MoS2 reference).

## Citations and evidence anchors

- DOI: [10.1021/acsnano.8b02844](https://doi.org/10.1021/acsnano.8b02844)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
