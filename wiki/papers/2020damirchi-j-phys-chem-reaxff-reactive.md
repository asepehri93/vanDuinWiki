---
id: paper:2020damirchi-j-phys-chem-reaxff-reactive
type: paper
title: "ReaxFF Reactive Force Field Study of Polymerization of a Polymer Matrix in a Carbon Nanotube-Composite System"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:parameterization
  - material:graphene-carbon-nano
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.0c03509"
year: 2020
authors:
  - "Behzad Damirchi"
  - "Matthew Radue"
  - "Krishan Kanhaiya"
  - "Hendrik Heinz"
  - "Gregory M. Odegard"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "2bd6cd8cdbf7e1364d03751c4b55e1e362513135c855a43e0d7b130b176b153c"
pdf_path: "papers/Damirchi_JPC_2020_CNT_polymer.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020damirchi-j-phys-chem-reaxff-reactive -->

**ReaxFF** carbon parameters are retrained against **PCFF-IFF / DFT-D2** benchmarks for **flattened CNT** geometries, then used with **accelerated (bond-boost) ReaxFF MD** to follow epoxy-amine **curing** near circular vs flattened nanotubes.

## Summary

The work addresses **epoxy (diglycidyl ether of bisphenol F, Bis-F) + curing agent (diethyltoluenediamine, DEDTA)** polymerization in the presence of **armchair CNTs** spanning multiple diameters. ReaxFF **C–C graphitic parameters** are adjusted so **flattened CNT (flCNT)** energetics and geometries better track reference data; **bond-boost MD** promotes cross-linking events within tractable times. Binding energies and polymer alignment differ between **curved vs flat** flCNT regions, with implications for **interfacial load transfer**.

## Methods

- **Reference data:** **DFT-D2** and **PCFF-IFF** datasets for **open vs flattened** CNT energies across diameters; train-set augmentation where collapsed flCNT minima appear during optimization.
- **ReaxFF training:** Monte-Carlo/ReaxFF training workflow (as described) updating carbon parameters relevant to **π-bonding and bending**; comparison of threshold diameters where flattening becomes favorable.
- **Production MD:** **LAMMPS**-style ReaxFF runs reported with **timestep 0.25 fs** and overall segments up to **500 ps** (order **2×10\(^6\)** steps) including heating to **500 K** (see article for staged protocol); **bond-boost** constraints to accelerate targeted reaction channels with energy-based rejection of unphysical barrier crossings. **Thermostat:** **Nosé–Hoover** in the **Ar**-**bombardment** and **pressure**-serviced **segments** described in the article; **Berendsen**/**Nosé** details for **curing** **stages** follow the **primary** **text**. **Barostat:** **anisotropic** **NPT**-like **control** with **~250 fs** **damping** (~**1000** **timesteps**) for **graphene** **+** **Ar** **studies**; **N/A** — **barostat** not used in **pure** **NVT** **epoxy** **curing** **windows** if so stated.
- **Systems:** Isolated **(n,n)** armchair tubes including **(15,15)** among others for binding and polymerization comparisons. **PBC** in **3D** for the **isolated** **nanotube** + **resin** supercells. **NPT / barostat: N/A** in the **protocol** **summary** above; **constant-volume** **ReaxFF** **stages** are reported for **curing** **(NVT**-class **dynamics** per article). **Electric field: N/A** beyond **intramolecular** **bias**; **replica / umbrella: N/A**.

## Findings

- Optimized parameters reduce **over-flattening** of large-diameter tubes versus **ReaxFF C-2013**, improving agreement with **PCFF-IFF/DFT-D2** trends for flCNT width and relative energies.
- **DEDTA** binds more strongly to **flat** flCNT regions than to **curved** segments (reported binding energies \(\sim\)15 vs \(\sim\)24 kcal/mol with consistent PCFF-IFF agreement for the gap).
- **Dimer/crosslink production** is enhanced near **flCNTs**, suggesting better **coating** and **load transfer** than for circular CNTs under the simulated conditions.
- **π–π stacking** between aromatic moieties and CNT walls yields **high alignment** of polymer fragments along the tube axis.

The **J. Phys. Chem. C** abstract emphasizes that **flat** **flCNT** regions are more favorable adsorption sites than **curved** sidewalls (higher **binding energies** there), that **higher dimer generation** near **flCNTs** yields more effective **nanotube coating** and **higher load transfer** than **circular** CNTs under their protocol, and that the simulations are presented as an atomistic route to observe **epoxy–amine polymerization** together with **CNT** interactions.

## Limitations

Bond-boost acceleration changes effective kinetics; isolated-tube geometry omits entangled CNT–CNT networks. Parameter transfer beyond the Bis-F/DEDTA chemistry should be validated.

## Relevance to group

**van Duin-group** ReaxFF on **CNT–epoxy interfaces** with explicit **parameter refinement** and **accelerated reactive MD**.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.0c03509](https://doi.org/10.1021/acs.jpcc.0c03509)

## Related topics

- [[reaxff-family]]
