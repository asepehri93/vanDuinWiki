---
id: paper:2015botari-carbon-99-20-graphene-healing
type: paper
title: "Graphene healing mechanisms: A theoretical investigation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:reaxff-application
  - keyword:thermal-decomposition
source_refs: []
doi: "10.1016/j.carbon.2015.11.070"
year: 2015
authors:
  - "Tiago Botari"
  - "Ricardo Paupitz"
  - "Pedro Alves da Silva Autreto"
  - "Douglas S. Galvão"
venue: "Carbon, 99 (2016) 302–309"
pdf_sha256: "eece4b9d9ef58001d8034e5966c7aa09c66827a6e0f197ce6160335ae6e1555b"
pdf_path: "papers/ReaxFF_others/Botari_2016_Graphene_healing_mechanisms_Carbon.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015botari-carbon-99-20-graphene-healing -->

## Summary

Defect engineering and repair of **graphene** are central to nanocarbon electronics and microscopy, yet **vacancy healing** involves **bond rearrangements** that are difficult to capture with non-reactive potentials. Botari *et al.* use **reactive molecular dynamics** with a **ReaxFF**-style carbon field to follow **large perforated graphene** motifs as they evolve under **high-temperature annealing** with an explicit **carbon feedstock** and under **room-temperature** scenarios where **electron-beam** energy deposition mimics **scanning transmission electron microscopy (STEM)** conditions reported experimentally. The study emphasizes transient **non-hexagonal** intermediates—**linear carbon chains** and **five- and eight-membered rings** in planar and non-planar arrangements—as obligatory waypoints on routes back toward **hexagonal** graphene.

## Methods

### MD application (atomistic dynamics)

**LAMMPS** reactive MD uses **ReaxFF** (**Chenoweth *et al.* (2008) C/H/O**, *Carbon*). The model is **single-layer graphene** with a **circular hole (~3.2 Å radius)**, **in-plane PBC**, and perimeter atoms tied by **virtual springs** (**K = 30.0 kcal mol⁻¹ Å⁻²**); in the **electron-beam** scenario those edge atoms also receive **temperature fixing** to dissipate excess energy (*Carbon* Methods/figures). **Scenario (i)** anneals **300–2000 K** with **carbon adatoms** injected at **random positions** every **500 fs** with **random kinetic energies** (single-atom depositions). **Scenario (ii)** keeps the sheet at **300 K** but applies **cylindrical local heating** in a moving zone to mimic **STEM**-like excitation, with the same **500 fs** deposition schedule. Integration uses **0.1 fs** steps under **NVT** with a **Nose–Hoover chain thermostat** (parameters in *Carbon*). Selected **SCC-DFTB** (**DFTB+**, **Slater–Kirkwood** dispersion) calculations benchmark ReaxFF. **Barostat, applied electric fields, and enhanced sampling beyond the stated heating/deposition:** **N/A —** not used. **Hydrostatic pressure control:** **N/A —** not used (no **NPT** barostat). Total trajectory lengths per scenario are tabulated in the **PDF**.

### Force-field training

**N/A —** uses published **ReaxFF** and **DFTB** parametrizations; no new QM refit is reported as the primary contribution.

### Static QM / DFT

**N/A —** SCC-DFTB appears as a comparative electronic-structure tool, not as the main production method.

## Findings

With **high temperature** and **carbon supply**, reactive trajectories show the **hexagonal** lattice can **close** when edges and adatoms surmount rearrangement barriers; **oxidation**-adjacent **rearrangement** and **decomposition** of strained rim sites precede closure. Healing routes pass through **non-hexagonal intermediates** rather than a single **zippering** step. At **300 K**, **complete healing** in the model is tied to **localized heating** reminiscent of **STEM** conditions; without that localization, healing is **kinetically limited** on accessible MD timescales—an explicit **limitation** of pure room-temperature annealing in the setup. Authors highlight transient **linear carbon chains** and **five- and eight-membered** rings (including **Stone–Wales-like** motifs) as recurring waypoints before **sixfold** coordination dominates again. **Coverage** and **defect** distributions differ from experiment; quantitative barriers and full trajectory budgets should be taken from the **PDF** rather than this summary alone.

## Limitations

The **beam** model is a **phenomenological local heating + deposition** scheme, not a first-principles electron-scattering treatment; **single-atom carbon deposition** simplifies realistic plasmas/microscopes where **small hydrocarbon fragments** may dominate.

## Relevance to group

Connects **ReaxFF** **reactive MD** to **defect healing** in **nanocarbon**, a recurring theme alongside other **graphene** reactive simulations in the corpus.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
