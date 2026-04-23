---
id: paper:2016le-nanotechnolo-mechanical-properties
type: paper
title: "Mechanical properties of borophene films: a reactive molecular dynamics investigation"
updated: "2026-04-20"
confidence: med
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
pdf_sha256: "ac3ce0a9928f6b84922c53dba73d39da238329e97f2dbd79daef4967fc8bc82d"
pdf_path: "papers/ReaxFF_others/Le_2016_Nanotechnology_27_445709.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nose-hoover
---

<!-- id:paper:2016le-nanotechnolo-mechanical-properties -->

## Summary

**Reactive MD** with **ReaxFF** (**B–B** interactions) in **LAMMPS** evaluates **uniaxial tension** of **five free-standing borophene polymorphs** with **hexagon-hole fractions η ≈ 0.10–0.15** across **1, 300, and 600 K**, reporting **2D Young’s moduli**, **fracture stresses/strains**, and **anisotropy** between **armchair** and **zigzag** loading. The study complements **boron** **allotrope** surveys by giving **reactive** **failure** pathways and **orientation-dependent** **strength** trends for **polymorphic** **sheets** that are still challenging to synthesize uniformly in experiment.

## Methods

- **Potential / integrator:** **ReaxFF** for boron (cited prior parametrization **[18]**); **LAMMPS** with **velocity Verlet** **[20]**.
- **Boundary conditions:** **Periodic in-plane**; **~20 Å vacuum** along **z** for a **single layer**; initial **NPT relaxation** (**Nosé–Hoover** thermostat + barostat) **1.25 ps** to **zero stress**.
- **Loading:** **Constant engineering strain rate 2.5 × 10⁸ s⁻¹** along **armchair** or **zigzag**; **lateral stress** adjusted with **NPT** in the **transverse in-plane** direction to approximate **uniaxial** stress; temperatures **1, 300, 600 K** explored.
- **Structures:** Five sheets with **η = 1/9 (α sheet), 1/8 (types A,B), 2/15, 4/27**; atom counts **~4.8k–5.6k** (**Table 1** lists box dimensions).

**Protocol details not recovered here.** Explicit **integration timestep (fs)**, **total trajectory duration**, **Nosé–Hoover** thermostat/barostat coupling constants beyond the qualitative **NPT relaxation** line, **electrostatic cutoffs**, **applied electric fields**, and **enhanced sampling** variants are **not** stated on the short extract used for bootstrap curation—see the **Nanotechnology** PDF (**DOI** in front matter) for the authoritative parameter table.

## Findings

Young’s modulus and tensile strength decrease with increasing temperature for the five borophene polymorphs studied; fracture is analyzed with stress–strain curves and Figures 2–3 in the article. At **300 K**, the abstract reports **2D Young’s moduli** **63–136 N m⁻¹** and **fracture stresses** **12–19 N m⁻¹** across the five sheets, with strains at tensile strength about **9–14% (1 K)**, **11–19% (300 K)**, and **10–16% (600 K)** depending on structure and temperature. Primary levers are temperature (**1**, **300**, **600 K**), loading direction (armchair versus zigzag), and hexagon-hole fraction **η**. High strain rate (**2.5 × 10⁸ s⁻¹**) and free-standing models differ from supported borophene experiments (see **## Limitations**).

**Corpus note.** Duplicate registered PDF: [[2016le-nanotechnolo-mechanical-properties-2]].

## Limitations

**Strain rate 10⁸ s⁻¹** is **many orders of magnitude** above experiment—standard MD limitation; qualitative trends vs **quantitative** strengths may differ.
- Models omit **substrate** interactions (noted as future work).
- **ReaxFF** for **boron** focuses on **mechanical** **failure** and **connectivity**; **electronic** **band** properties and **defect** **optics** are outside the classical reactive Hamiltonian.
- **Experimental** **borophene** often requires **substrates** or **encapsulation**; **free-standing** **simulations** should be read as **upper-bound** **mechanical** trends for **ideal** **sheets**.
- **Defect** **density** and **grain** **boundaries** in **synthesized** **boron** **films** can reduce **strength** relative to **pristine** **simulation** **cells** even when **polymorph** **labels** match.

## Relevance to group

Demonstrates **ReaxFF + LAMMPS** **mechanical** benchmarking on **2D boron allotropes** complementary to **carbon** reactive studies in the corpus.

## Citations and evidence anchors

- DOI: [10.1088/0957-4484/27/44/445709](https://doi.org/10.1088/0957-4484/27/44/445709) — *Nanotechnology* **27**, 445709 (2016).

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Duplicate PDF bytes: [[2016le-nanotechnolo-mechanical-properties-2]].
