---
id: paper:2016dong-carbon-104-2-molecular-dynamic
type: paper
title: "Molecular dynamics simulation of layered graphene clusters formation from polyimides under extreme conditions"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:carbon-hydrocarbon
  - material:graphene-carbon-nano
  - material:polymer-organic
  - task:application
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:thermal-decomposition
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2016.03.050"
year: 2016
authors:
  - "Yuan Dong"
  - "Sean C. Rismiller"
  - "Jian Lin"
venue: "Carbon"
pdf_sha256: "1ef8693e862002618cb2e07b5daeaa9afc642f6625fa3f806793d18279af53f7"
pdf_path: "papers/ReaxFF_others/Dong_Carbon_polyimides_graphene_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016dong-carbon-104-2-molecular-dynamic -->

## Summary

Laser processing can convert polymer precursors into **graphene-like** carbon without traditional metal catalysts, but the **pressure–temperature** pathway that favors **sp\(^2\)** network growth over charring is difficult to probe in situ. This **Carbon** article uses **ReaxFF molecular dynamics** to mimic **laser-analog** **high pressure–temperature** spikes applied to **polyimide** models, contrasting them with milder **isobaric** protocols. The scientific question is whether **layered graphene clusters** can emerge from **polyimide pyrolysis** under extreme **NVT**-style conditions, and how emitted gas species and carbon-ring statistics evolve compared with lower-pressure decomposition that yields small molecules without extended graphitic layers.

## Methods

**MD application (ReaxFF in LAMMPS):** **ReaxFF** in **LAMMPS** uses a **0.25 fs** timestep and **3D PBC**. The cell holds **32** **PI** monomers (**C\(_{22}\)H\(_{12}\)N\(_2\)O\(_5\)**) on an **FCC** lattice, **compressed** to experimental density **~1.308 g/cm³**, then held at **300 K** for **40 ps**. Branch (**i**): **NVT** heating **300 K → \(T_p\)** (**2400, 2700, or 3000 K**); the fixed-volume constraint yields internal pressures **~3 GPa**, taken as a laser-like **high \(P,T\)** spike. Branch (**ii**): **NPT** at the same **\(T_p\)** but **27 MPa**, giving **small-molecule** decomposition without **layered graphene**. **Analysis** tracks **carbon ring** populations, **ring–ring** **PDFs**, and gas releases (**H\(_2\)O**, **N\(_2\)**, **H\(_2\)**, **CO**, …) to infer pathways. **Thermostat/barostat variants, anneal schedule after heat-up, and total production time:** **N/A — complete protocol tables are in the journal PDF**, not the short front-matter extract.

**Force-field training:** **N/A — application study** using an existing **C/H/O/N** **ReaxFF** parameterization referenced from prior shock, pyrolysis, and polymer work (see paper introduction).

**Static QM / DFT:** **N/A — not the focus**; monomer **bond lengths/angles** are pre-optimized with the **VAMP** package in **Materials Studio 7.0** as stated in the **Simulation methods** section, but the production study is **ReaxFF MD**.

## Findings

Under **NVT** conditions near **~3 GPa** and **T > 2400 K**, the simulations form **layered graphene clusters** from polyimide, qualitatively consistent with experimental reports on laser processing of polyimide summarized by the authors. Under **NPT** near **~27 MPa**, pyrolysis yields **small molecules** without graphene formation, emphasizing strong sensitivity to the **mechanical** pathway. The paper interprets differences through emitted gas inventories and carbon-network metrics, proposing distinct reaction routes for high-pressure versus low-pressure protocols within the ReaxFF model. The central comparative lever is therefore the **mechanical pathway** (**GPa-scale NVT** vs **MPa NPT**), not temperature alone.

## Limitations

Mapping simulation protocols to real laser heating is approximate; high-temperature reactive MD can depend on parameterization details and timestep stability.

## Reader notes (MAS / retrieval)

Highlight **GPa NVT** vs **MPa NPT** contrast when users ask why **polyimide** sometimes yields **graphene** vs only small molecules.

## Relevance to group

Illustrates **ReaxFF carbonization** chemistry tied to **laser synthesis** of graphene from **polymers**, adjacent to broader nanocarbon work in the knowledge base.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2016.03.050](https://doi.org/10.1016/j.carbon.2016.03.050)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
