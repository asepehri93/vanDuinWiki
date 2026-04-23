---
id: paper:2016le-nanotechnolo-mechanical-properties-2
type: paper
title: "Mechanical properties of borophene films: a reactive molecular dynamics investigation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1088/0957-4484/27/44/445709"
year: 2016
authors:
  - "Minh Quy Le"
  - "Bohayra Mortazavi"
  - "Timon Rabczuk"
venue: "Nanotechnology"
pdf_sha256: "810f56b1099879f1238f9f2e9a72acce974c3ff9f80b5527cb8137ca6e250b92"
pdf_path: "papers/ReaxFF_others/le_2016_borophene_nanotechnology.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
---

<!-- id:paper:2016le-nanotechnolo-mechanical-properties-2 -->

## Summary

This *Nanotechnology* study uses reactive molecular dynamics with the ReaxFF boron potential in LAMMPS to evaluate the mechanical response of five free-standing borophene polymorphs whose hexagon-hole fraction \(\eta\) lies in the experimentally emphasized range near 0.10–0.15. Uniaxial tension is applied along armchair and zigzag directions at 1 K, 300 K, and 600 K at a constant engineering strain rate of \(2.5\times10^{8}\,\mathrm{s^{-1}}\), with NPT control in the transverse in-plane direction to approximate uniaxial loading. The work reports two-dimensional Young’s moduli, fracture stresses, and failure strains as functions of temperature and crystal orientation, and it relates fracture mechanisms to the anisotropic arrangement of boron rows.

## Methods

The authors implement ReaxFF for boron as cited in the paper, integrate with velocity Verlet in LAMMPS, and use **periodic** in-plane **boundary** conditions with vacuum normal to the sheet. Slabs are at least about 4 nm thick in the non-periodic direction where applicable to the boron sheet construction, with initial **NPT** relaxation using a **Nose–Hoover** **thermostat** and **barostat** to reach near-zero in-plane stress before loading. Five distinct boron sheets with \(\eta = 1/9\) (α), two \(1/8\) types (A and B), \(2/15\), and \(4/27\) are built with on the order of \(4.8\times10^{3}\)–\(5.6\times10^{3}\) **atoms**; Table 1 in the article lists box dimensions. Loading applies constant engineering strain along armchair or zigzag with the transverse in-plane stress relaxed under **NPT** to mimic uniaxial tension at **1 K**, **300 K**, and **600 K** (**temperature** grid from the abstract). The strain rate is high relative to experiment, which is standard for accessible nanosecond trajectories.

**Protocol details not recovered here.** Explicit **timestep**, **total MD duration**, detailed **Nose–Hoover** coupling constants, **electrostatic** settings, **applied fields**, and **enhanced sampling** are **not** stated on the short extract used for bootstrap curation—see the **Nanotechnology** PDF for the authoritative parameter table.

## Findings

Same abstract-level results as [[2016le-nanotechnolo-mechanical-properties]]: Young’s modulus and tensile strength decrease with temperature; strong armchair/zigzag anisotropy; at **300 K**, **2D Young’s moduli** **63–136 N m⁻¹** and fracture stresses **12–19 N m⁻¹**; strains at tensile strength about **9–14% (1 K)**, **11–19% (300 K)**, and **10–16% (600 K)** depending on polymorph and temperature; fracture is discussed with stress–strain curves (Figures 2–3). The article positions ReaxFF borophene mechanics against limited prior DFT literature cited there. Control axes are **η** (**1/9**, **1/8** types A/B, **2/15**, **4/27**), loading angle, and temperature. Strain-rate and substrate-free caveats match the sibling page.

**Corpus note.** Duplicate IOP PDF bytes versus [[2016le-nanotechnolo-mechanical-properties]]; use whichever local PDF matches your manifest hash.

## Limitations

The two registered local PDFs for the same DOI have different SHA-256 hashes; operators should prefer whichever file is artifact-free for reading. The simulated strain rate is many orders of magnitude above laboratory rates, so absolute strengths are best interpreted qualitatively unless compared across potentials and protocols within the same study. Substrate interactions are not included, which matters for supported borophene experiments.

## Relevance to group

Duplicate ingest for a **2D boron** **ReaxFF** mechanics reference; keeps manifest completeness without forking narrative from the primary slug.

## Citations and evidence anchors

- DOI: [10.1088/0957-4484/27/44/445709](https://doi.org/10.1088/0957-4484/27/44/445709).

## Related topics

- [[2016le-nanotechnolo-mechanical-properties]]
- [[reaxff-family]]
