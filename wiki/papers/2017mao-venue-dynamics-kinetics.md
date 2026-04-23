---
id: paper:2017mao-venue-dynamics-kinetics
type: paper
title: "Dynamics and kinetics of reversible homo-molecular dimerization of polycyclic aromatic hydrocarbons"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:lammps
  - keyword:combustion
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors:
  - "Qian Mao"
  - "Yihua Ren"
  - "K. H. Luo"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "41d6ba0fd35e8996f7657ced2ad03b052a6b261aeebae776f1e16d9e6d84c7f9"
pdf_path: "papers/Mao_Qian_JCPSA6_vol_147_iss_24_244305_1_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017mao-venue-dynamics-kinetics -->

!!! abstract
Reactive MD with a C/H ReaxFF parametrization is used to study reversible physical dimerization of PAHs as a function of temperature, impact parameter, and molecular size, and to extract forward/reverse rate constants compared with a pyrene dimer experiment.

## Summary

The work reports molecular dynamics with a ReaxFF description of carbon and hydrogen to study reversible homo-molecular dimerization of polycyclic aromatic hydrocarbons (PAHs). Collisions are analyzed over a range of temperatures, impact parameters, and orientations. Coronene dimer energetics from ReaxFF are compared in the supplementary material to semiempirical PM3 and DFT (U)M06-2X/def2SVP references to justify the reactive force field for longer trajectories than feasible with quantum methods. The study quantifies enhancement factors for dimerization, lifetimes within a capture radius as a function of impact parameter, and temperature- and PAH-dependent rate constants used in a reversible kinetic model. The authors conclude that physical dimerization is unlikely to dominate at typical flame temperatures and PAH concentrations, pointing to chemical growth routes instead.

## Methods

**A — Force-field training / fitting:** **C/H ReaxFF** trained against **QM** data; **QEq** updates **atomic charges** each step; **bond/angle/torsion**, **over/under-coordination**, **vdW**, and **Coulomb** terms as in **Sec. II.A** of the article.

**B — Molecular dynamics / sampling (bimolecular collisions in LAMMPS).** **PAH monomers** (**Fig. 1** set including **five-membered** and **six-membered** rings) are **geometry-minimized** (**conjugate gradient**) then **vibrationally equilibrated** at the target temperature with **10⁶** iterations at **Δt = 0.25 fs** using a **Nosé–Hoover thermostat**. **Binary homo-molecular collisions** are then integrated in the **microcanonical (NVE)** ensemble in **LAMMPS** (**reax/c** pair style) with **3D periodic boundary conditions**, **Δt = 0.25 fs**, **100 ps** total collision time, **10 000** stochastic velocity draws per **(PAH, T, impact parameter)** case for statistics. **System size & composition:** **two PAH molecules** per collision event (**~52 atoms** for a **pyrene–pyrene** encounter as a representative lower bound; larger PAHs scale up—see Fig. 1). **Impact parameter** is scanned to define a **capture radius**; initial **separation** is **30 Å** (justified against binding-energy decay with distance in the SI). **OVITO**/**VMD**-class visualization is used in the paper. **N/A — barostat / pressure control**: **NVE** collision dynamics—**no** thermostat/barostat during the **100 ps** collision segment.

**C — DFT / static QM:** **Coronene dimer** reference curves vs **PM3** and **(U)M06-2X/def2SVP** (**Fig. S1**, **Table S1** in **SI**) motivate **ReaxFF** accuracy for the **long** reactive trajectories.

**D — Review / non-simulation framing.** **N/A**: primary **JCP** study. **Proof PDF note:** `papers/Mao_Qian_JCPSA6_vol_147_iss_24_244305_1_proof.pdf`—confirm **final DOI/pagination** from the publisher site when citing.

## Findings

**Outcomes and mechanisms.** **Homo-molecular dimerization enhancement factors** grow at **lower temperature** and for **smaller PAHs**—the effect is **not size-independent**. Within the **capture radius**, **dimer lifetimes** **decrease** as **impact parameter** increases. **Forward and reverse rate constants** depend on **temperature** and **PAH identity** and are extracted from the **collision statistics** to build a **reversible kinetic model**.

**Comparisons.** The reversible model is compared against **pyrene dimerization experiments** (**Sabbah et al., *J. Phys. Chem. Lett.* 2010** as cited in the article).

**Sensitivity and design levers.** **Temperature**, **impact parameter**, and **PAH size/orientation** distributions are the primary levers explored in the MD campaign.

**Limitations and outlook (as authored).** The article argues that under **typical flame temperatures and PAH concentrations**, **physical dimerization** is **unlikely to dominate** relative to **chemical growth** channels—framing a shift in emphasis for soot inception models.

**Corpus / PDF honesty.** Detailed kinetics tables live in the **SI**; this entry is grounded in the **proof PDF** text—reconcile numbers against the **VOR** when available.

## Limitations

Proof PDF; QM benchmarks are limited to smaller systems and short times; ReaxFF binding energies deviate from high-level DFT though trends are matched for parametrization context.

## Relevance to group

Adri C. T. van Duin is a co-author; the study applies group ReaxFF methodology to combustion-relevant PAH dynamics.

## Citations and evidence anchors

Prefer the version-of-record **J. Chem. Phys.** citation when DOI is confirmed from the publisher.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]

## Reader notes (navigation)

- Proof PDF filename: `papers/Mao_Qian_JCPSA6_vol_147_iss_24_244305_1_proof.pdf`.
