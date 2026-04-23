---
id: paper:2016mortazavi-physical-che-mechanical-response
type: paper
title: "Mechanical response of all-MoS2 single-layer heterostructures: a ReaxFF investigation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - material:tmd
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/c6cp03612k"
year: 2016
authors:
  - "Bohayra Mortazavi"
  - "Alireza Ostadhossein"
  - "Timon Rabczuk"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "caed4a000ddfea887de9455f7b3955885b5eb37abd6210f76e93a87088a14d66"
pdf_path: "papers/Mortazavi_MoS2_PCCP_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016mortazavi-physical-che-mechanical-response -->

## Summary

**ReaxFF molecular dynamics** is applied to **all-MoS2 single-layer heterostructures** to probe **mechanical response** and **failure mechanisms** under the loading protocols described in the article. The work connects **structural motifs** accessible in **2D hetero-stacking** to **stress–strain behavior**, **fracture**, and **energy dissipation** channels that differ from **homogeneous MoS2** sheets. **PCCP** framing places the study in the **atomistic materials mechanics** literature for **transition metal dichalcogenides**.

## Methods

Simulations use a **MoS₂ ReaxFF** parametrization trained against **QM** data for bond dissociation, valence-angle bending, small-molecule energetics, and condensed-phase **formation energies** and **equations of state** as described in the parameterization citation. **Uniaxial tensile** tests are performed in **LAMMPS** with **Δt = 0.25 fs** after **energy minimization**. **Pristine 2H** and **1T** monolayers use roughly **12,000 atoms** in **~27 nm × 13 nm** periodic cells, whereas **2H/1T** heterostructure models enlarge to **~20,000 atoms** in **~24 nm × 24 nm** cells. Loading explores **armchair**, **zigzag**, and two additional in-plane angles near **10°** and **20°** relative to the armchair axis; heterostructures vary the characteristic **1T** domain size and concentration with a fixed **β-type** grain boundary (**Figure 1c**).

**MD application.** After **energy minimization**, samples undergo **room-temperature equilibration** using a **Nose-Hoover thermostat** coupled to an **NPT** integrator with **50 fs** temperature damping and **100 fs** pressure damping to reach **near-zero** in-plane stress. **Uniaxial tension** then applies a **constant engineering strain rate of 10⁷ s⁻¹** along the loading axis while the **perpendicular in-plane stress** is relaxed with **NPT** to maintain **near-zero lateral stress** (true **uniaxial** conditions in-plane). **Stress–strain** reporting averages over **250 fs** windows. **Total production tensile duration (ns)** is **not** restated as a single headline number in the excerpt summarized here (**N/A** — consult **PCCP** figures/tables). **Applied electric fields, replica exchange, umbrella sampling, and metadynamics** are **not** used (**N/A**).

**Force-field training.** **N/A** — uses the **published MoS₂ ReaxFF** parameterization cited in the paper rather than reporting a new fit here.

**Static QM / DFT.** **N/A** — **QM** enters only as the **training manifold** for the **ReaxFF** potential.

## Findings

Pristine **2H MoS₂** elastic response matches experiment and prior ab initio benchmarks for the directions reported, supporting baseline accuracy of the potential. **2H/1T** single-layer heterostructures show orientation- and microstructure-dependent moduli and failure strains distinct from homogeneous sheets because of phase registry and **β-type** grain-boundary topology. Reactive bonds allow fracture beyond harmonic elastic regimes typical of non-reactive empirical TMD models. Heterostructure comparisons are primarily versus homogeneous **2H** and **1T** baselines in this study. Loading angle, **1T** domain size and concentration, and heterostructure morphology (parameter **D** in Fig. 1c) are explicit structural knobs. The discussion addresses strain-rate effects, finite-size artifacts, and the need to benchmark new heterostructure morphologies against DFT or experiment when extrapolating—see the *Phys. Chem. Chem. Phys.* article for full caveats.

## Limitations

- **ReaxFF MoS2** parameterizations must be checked against **DFT/experiment** for each **new stacking** or **phase** explored.
- **Strain-rate** and **system-size** effects influence **brittle vs ductile** interpretations in MD.

## Relevance to group

Adds a **TMD mechanics** reference using **ReaxFF**, adjacent to the group’s broader **2D materials + reactive simulation** coverage.

## Citations and evidence anchors

- Title/DOI block in `papers/Mortazavi_MoS2_PCCP_2016.pdf`; **DOI:** `10.1039/c6cp03612k`.

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- **PCCP** **2016** mechanics reference for **all–MoS₂** **2H/1T** **single-layer** heterostructures.
