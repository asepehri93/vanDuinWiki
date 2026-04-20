---
id: paper:2022mike-pols-acs-what-happens
type: paper
title: "What Happens at Surfaces and Grain Boundaries of Halide Perovskites: Insights from Reactive Molecular Dynamics Simulations of CsPbI3"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:mechanics-tribology
  - material:widegap-semiconductor
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.2c09239"
year: 2022
authors:
  - "Mike Pols"
  - "Tobias Hilpert"
  - "Ivo A. W. Filot"
  - "Adri C. T. van Duin"
  - "Sofía Calero"
  - "Shuxia Tao"
venue: "ACS Appl. Mater. Interfaces 14, 40841–40850 (2022)"
pdf_sha256: "4e0e54fed3c25412da77fa2c0185d06ca01bc4874dafa1d54c8d2bfd154fa7f8"
pdf_path: "papers/Pols_ACS_AMI_CsPbI3_2022.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2022mike-pols-acs-what-happens -->

## One-paragraph summary

**ReaxFF MD** study of **CsPbI\(_3\)** focusing on how **surfaces, surface defects, and grain boundaries** participate in **degradation chemistry** and relative **stability**. The authors relate computed **surface stability trends** to experimental prevalence of facets where comparable data exist, and mechanistically track evolution of **PbI\(_x\)**-like local coordination environments via **octahedral connectivity** changes (**corner → edge → face sharing**). **Pb dangling bonds** and **iodine sterics** are highlighted as drivers of degradation reactions; defect engineering can **stabilize** some boundaries by increasing steric hindrance even though clustered defects often accelerate failure.

## Methods

ReaxFF parameterization appropriate to Cs–Pb–I (per study)/halide perovskite chemistry; reactive trajectories comparing multiple surface terminations and grain-boundary constructs; stability ordering analysis aligned with experimental surface occurrence where discussed.

## Findings

Established **stability ordering** across several **surface types** consistent with experimental observations in the framing of the paper; degradation proceeds through staged **Pb–I connectivity** motifs; some **GB configurations** stabilize relative to pristine surfaces due to **local steric blocking** of reactive iodine species, while defect clustering generally harms stability.

## Limitations

Classical reactive model for complex electronic-structure-sensitive photophysical systems; long-time annealing and photogenerated carriers are outside the classical ReaxFF scope unless augmented by higher-level calibration.

## Relevance to group

Connects the group’s **ReaxFF** expertise to **halide perovskite durability** at **interfaces and microstructure features** that dominate practical thin-film devices.

## Citations and evidence anchors

https://doi.org/10.1021/acsami.2c09239 — Abstract (~p. 1) states mechanistic claims about octahedral sharing and steric control.

## Related topics

- [[reaxff-family]]
