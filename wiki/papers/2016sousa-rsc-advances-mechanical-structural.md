---
id: paper:2016sousa-rsc-advances-mechanical-structural
type: paper
title: "Mechanical and structural properties of graphene-like carbon nitride sheets"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/C6RA14273G"
year: 2016
authors:
  - "J. M. de Sousa"
  - "T. Botari"
  - "E. Perim"
  - "R. A. Bizao"
  - "Douglas S. Galvão"
venue: "RSC Advances (2016) 6, 76915–76921"
pdf_sha256: "75bbc879688b84c30f1711a2ea848f7000bb5b1e90816b956ce7f1701c2f93c5"
pdf_path: "papers/ReaxFF_others/deSousa_RSC_Advances_C3N4_2016.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nose-hoover
  - keyword:2d-materials
---
<!-- id:paper:2016sousa-rsc-advances-mechanical-structural -->

## Summary

Fully atomistic **reactive molecular dynamics** with **ReaxFF** (implemented in **LAMMPS**) studies **mechanical failure** of three **graphene-like carbon nitride** models: **graphene-based g-CN**, **triazine-based g-C\(_3\)N\(_4\)**, and **heptazine-based g-C\(_3\)N\(_4\)** membranes. Uniaxial stretching along two principal directions is compared at **10 K**, **300 K**, and **600 K** to connect **topology/density/bonding** differences to **ultimate strain** and **fracture patterns**.

Carbon nitrides span competing motifs with different in-plane hole densities; reactive MD captures bond rupture beyond harmonic elasticity when strains become large.

## Methods

**1 — MD application (reactive classical MD).** Simulations use **ReaxFF** in **LAMMPS** on **graphene-based g-CN**, **triazine-based g-C\(_3\)N\(_4\)**, and **heptazine-based g-C\(_3\)N\(_4\)** membranes with lateral dimensions of order **160 × 150 Å** and **6068**, **9240**, and **8624** atoms, respectively (**RSC Adv.**). **PBC** apply in the in-plane **X** and **Y** directions. Before stretching, structures are thermalized in the **NPT** ensemble with **external pressure set to zero** so no initial in-plane stress is imposed; temperature is controlled with a **Nosé–Hoover chain thermostat**. **Quasi-static uniaxial** loading is applied by **incrementally increasing the in-plane lattice parameter** along the two principal periodic directions at **10 K**, **300 K**, and **600 K**. Integration timestep, equilibration and production segment lengths, electrostatic cutoffs, **QEq** update settings, and strain rate in explicit time units are **N/A —** not stated in the indexed excerpt used here; use **`pdf_path`**. **Shear**, **shock**, **electric fields**, and **enhanced sampling** are **N/A —** not indicated there.

**2 — Force-field training.** **N/A —** the authors **adopt** a literature **ReaxFF** parameter set for these **C/N** frameworks after comparing predicted **bond lengths** and **lattice parameters** to prior references (see paper for stated deviations).

**3 — Static QM / DFT.** **N/A —** headline results are **classical reactive MD**, not **DFT** production trajectories.

## Findings

**Mechanical ranking.** **g-CN** exhibits the **lowest ultimate fracture strain**, followed by **heptazine-based** and then **triazine-based** **g-C\(_3\)N\(_4\)**, which the authors relate to differences in **density**, **topology**, and **bonding**.

**Anisotropy and temperature.** **Fracture patterns** depend on **stretch direction** along the principal axes. **Mechanical response** changes systematically across **10–600 K** in the sampled protocol.

Quantitative **failure strains** and **stress–strain** curves are given in **RSC Adv.** figures; follow the article’s stress definitions when comparing to plots.

The authors compare predicted **bond lengths** and **lattice parameters** to prior literature values to justify the **ReaxFF** parameter set. Fracture patterns are interpreted in terms of **density**, **topology**, and **bonding**.

## Limitations

- Reactive MD inherits **force-field** limitations for **charged/polar** environments and long-ranged electronic effects not explicitly in ReaxFF.
- Membrane models are **ideal 2D sheets**; experiments often involve **defects**, **substrates**, and **nonuniform** stress fields.

## Relevance to group

**2D carbon nitride** mechanical behavior under **ReaxFF**—adjacent literature for **nanocarbon/nitride** mechanics in reactive MD settings.

## Citations and evidence anchors

- DOI: [10.1039/C6RA14273G](https://doi.org/10.1039/C6RA14273G)
- Text-aligned pointers: `normalized/extracts/2016sousa-rsc-advances-mechanical-structural_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
