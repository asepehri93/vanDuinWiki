---
id: paper:2016peeters-venue-paper
type: paper
title: "N-doped graphene: Polarization effects and structural properties"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:graphene-carbon
  - keyword:npt-simulation
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.93.174112"
year: 2016
authors:
  - "Hossein Ghorbanfekr-Kalashami"
  - "M. Neek-Amal"
  - "F. M. Peeters"
venue: "Phys. Rev. B 93, 174112 (2016)"
pdf_sha256: "14f9b116db71aeacc09da4c1a0496d830ee7433d2924a52907d4b9ca511e1d95"
pdf_path: "papers/ReaxFF_others/Peeters_group_N_graphene_PhysRevB.93.174112.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2016peeters-venue-paper -->

## Summary

Nitrogen-doped graphene is studied as a route to tune electronic and mechanical properties, but random versus clustered nitrogen placements can yield different mesoscale morphologies and dipolar responses. Ghorbanfekr-Kalashami, Neek-Amal, and Peeters perform large-scale ReaxFF MD on periodic graphene supercells where carbon atoms are stochastically replaced by nitrogen at several N/C ratios, allowing occasional N–N neighbors. Observables include out-of-plane rippling, surface roughness, formation energies, elastic moduli, tensile strength, strain-to-failure, and a net in-plane dipole moment that emerges from broken sublattice symmetry in the doped sheets.

## Methods

**Force-field training:** **N/A —** the authors use an established ReaxFF parameterization for C/N systems (cited in *Phys. Rev. B* **93**, 174112) rather than reporting a new fit in this paper.

**MD application (ReaxFF in LAMMPS).** Pristine graphene reference cells contain **11 200** carbon atoms in a periodically repeated in-plane supercell of about **18 nm × 18 nm**. Nitrogen dopants are introduced by random substitutional Monte Carlo placement at concentrations up to **5 %**, generating several independent realizations (typically **five** per concentration) to average disorder. **Periodic boundary conditions** apply in-plane (**x** and **y**). Simulations use the **ReaxFF** reactive potential within **LAMMPS**, with an **NPT** ensemble implemented via **Nosé–Hoover thermostat and barostat**, a **0.1 fs** timestep, an initial relaxation of about **10 ps**, and **200 ps** of displacement-controlled in-plane tensile loading along **x**/**y** after equilibration (see section II of the article for the strain-control protocol references).

**N/A — applied electric field:** not part of the reported protocol.

**N/A — umbrella / metadynamics / replica exchange:** not reported.

**N/A — AIMD production trajectories:** **N/A —** comparisons to experiment and *ab initio* literature are cited, but the large-scale tensile work is classical reactive MD.

Pressure and temperature targets are imposed through the stated NPT Nosé–Hoover setup; consult the article for numerical targets and strain rates.

## Findings

**Nitrogen** introduces **ripples** and raises **roughness** in a manner that depends on **both** **global N/C** and **local clustering**. **Formation energy** grows **nonlinearly** with **doping** as **N–N** pairs become more frequent. **Young’s modulus**, **ultimate strength**, and **strain-to-failure** **decrease** with increasing **nitrogen** content in the simulated **tensile** tests. The field-predicted **in-plane dipole**—interpreted as **ferroelectric-like** **ordering** only in a **classical** sense—varies with **dopant** distribution, connecting **mechanical softening** to **electrostatic** symmetry breaking. The authors contextualize these trends with selected **experimental** and **ab initio** references noted in the paper while cautioning that **ReaxFF** does not recover **quantum** **band structures**. For **MAS** retrieval, the key takeaway is a **scalable** demonstration that **substitutional N** simultaneously perturbs **morphology**, **mechanics**, and **dipolar** response in **large** **supercells** inaccessible to **DFT** tensile tests.

## Limitations

ReaxFF remains an empirical reactive model; quantitative electronic structure (band gaps, defect states) is not at DFT quality. For **electronic** applications of **N-doped graphene**, treat these results as **mechanical** and **morphological** priors rather than **transport** predictions. **Strain-rate** and **defect** distributions in real **CVD** films may differ from the **random substitution** ensembles emphasized here. **Edge** **termination** and **substrate** interactions can further modulate **N** incorporation beyond the **periodic** **bulk** graphene motifs studied in the manuscript.

## Relevance to group

Demonstrates large-scale ReaxFF MD for doped graphene mechanics and polarization-like responses.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.93.174112](https://doi.org/10.1103/PhysRevB.93.174112)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
