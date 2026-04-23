---
id: paper:2018ostadhossein-venue-paper
type: paper
title: Do nickel and iron catalyst nanoparticles affect the mechanical strength of
  carbon nanotubes?
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:mechanics-tribology
- domain:reactive-md
- material:graphene-carbon-nano
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:reaxff-application
- keyword:lammps
- keyword:nvt-simulation
- keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: 10.1016/j.eml.2017.12.007
year: 2018
authors:
- Alireza Ostadhossein
- Kichul Yoon
- Adri C.T. van Duin
- Jin Won Seo
- David Seveno
venue: Extreme Mechanics Letters
pdf_sha256: c0e0a06bdd87828d00ec358d97e749988d38a283120d0e835243f8d6c023f05c
pdf_path: papers/Ostadhossein_Ni_CNT_ExtremeLetters_2018.pdf
extraction_quality: partial
group_affiliation: false
---
<!-- id:paper:2018ostadhossein-venue-paper -->

ReaxFF molecular dynamics in LAMMPS is used to tensile-test defect-free single-wall carbon nanotubes in contact with Ni and Fe nanoparticles in metallic and oxidized forms. Simulations resolve stress–strain behavior, bond-order evolution, and failure pathways to explain how catalyst particles that are essential for CNT growth can weaken the tubes.

## Summary

Reactive MD with ReaxFF explores how Ni and Fe catalyst nanoparticles (pure and oxidized) alter the tensile strength and failure mechanism of defect-free single-wall CNTs. Simulations use LAMMPS in the NVT ensemble with a Nosé–Hoover thermostat at 300 K, an initial timestep of 1 fs with restarts at selected strains using 0.5 fs to reduce premature bond cleavage from numerical noise, stress from `stress/atom`, and a fixed nanotube wall thickness of 0.34 nm, with multiple tubes per nanoparticle case for statistics.

The framing problem is that **CVD** growth often leaves **Ni** or **Fe** catalyst particles embedded in or attached to otherwise pristine tubes, so understanding whether metallic versus oxidized catalyst residues weaken **C–C** bonds—and by which chemistry—guides interpretation of measured nanotube strengths and failure statistics.

## Methods
**1 — MD application (tensile failure with catalyst contact).** **ReaxFF** trajectories are integrated in **LAMMPS** in the **NVT** ensemble with a **Nosé–Hoover** thermostat at **300 K**; stresses/strains come from **`stress/atom`**. **Oxidized Fe/Ni nanoparticles** are prepared with **hybrid GC-MC + MD** oxygen insertion under a **µVT** oxygen reservoir, including **NPT** segments (**10 ps**, **300 K**, **0.1 MPa**) to equilibrate oxides before contact with **(10,0) single-wall CNTs** (defect-free, **~0.34 nm** wall thickness as fixed in the protocol). Tensile tests use an initial **1 fs** timestep, restarting at strains **0.08–0.12** with **0.5 fs** to reduce catastrophic bond cleavage from integration noise; **≥6** replicas per case are averaged. **System sizes** follow the **Extreme Mechanics Letters** construction tables (full atom counts in PDF). **PBC:** **three-dimensional PBC** for the supercells described in the article. **Barostat during tensile pulls:** **N/A —** tensile production uses **NVT** without hydrostatic barostat control. **Electric fields / enhanced sampling:** **N/A —** not used beyond the stated **GC-MC** oxidation pretreatment.

## Findings
**Outcomes:** **pure metal** (**Ni**, **Fe**) nanoparticles **lower CNT failure stress/strains** more strongly than **oxidized** counterparts at comparable oxygen content; among oxides, **Fe-oxide** contacts are more damaging than **Ni-oxide** for the same oxygen loading. **Mechanisms:** **Ni** failures concentrate on **C–C bonds** directly interacting with **Ni**, whereas **Fe** cases include weakening of **C–C** bonds **not** directly bonded to **Fe**.

**Comparisons:** trends are interpreted relative to **oxidation state** and **element** (Ni vs Fe) for industrially relevant **CVD** catalyst residues.

**Sensitivity:** **oxygen content** and **metal identity** shift both **failure strain** and **bond-order evolution** along the stress–strain curve.

**Limitations:** the ingested file is an **Elsevier proof**; compare final **VOR** pagination. **Rates** at **300 K** tensile MD are not direct **CVD** growth maps.

**Corpus honesty:** protocol numbers above are from `papers/Ostadhossein_Ni_CNT_ExtremeLetters_2018.pdf`; confirm any updated values against the **published article**.

## Limitations

The ingested PDF is an Elsevier proof; final pagination and minor edits may differ from the version of record.

## Relevance to group

Adri C. T. van Duin is a co-author; study highlights ReaxFF for mechanical failure of carbon nanostructures in contact with transition-metal catalysts.

## Citations and evidence anchors

- DOI: [10.1016/j.eml.2017.12.007](https://doi.org/10.1016/j.eml.2017.12.007)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
