---
id: paper:2022zhu-venue-paper
type: paper
title: "Mechanistic study of chemical looping reactions between solid carbon fuels and CuO"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:reaxff-application
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.combustflame.2022.112216"
year: 2022
authors:
  - "Wenbo Zhu"
  - "Richard A. Yetter"
  - "J. Eric Boyer"
  - "Adri C. T. van Duin"
venue: "Combustion and Flame (in press in corpus proof; see DOI)"
pdf_sha256: "a4881e065ca63f17209da59f068d4b716313c2dda6f2a3e60134ab009b994f6e"
pdf_path: "papers/Zhu_CombFlame_CuO_looping_2022_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2022zhu-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **Combustion and Flame** article identified by `doi`. **Barrier** values quoted below are taken from the **abstract** as reported in the corpus extract; confirm against the **version of record** if the galley text differs.

## Summary

The work combines **ReaxFF molecular dynamics** and **experiments** on **CuO–carbon** mixtures to probe **chemical-looping combustion (CLC)**-relevant **oxidation** of **n-butane** and **simplified solid fuels** (**lignite**, **anthracite**) in contact with **CuO nanoparticles**. **Activation energies** from modeling are compared to **flammability / flame speed** measurements to argue for **temperature-dependent** competition between **surface oxidation** on **CuO** and **O<sub>2</sub>**-based pathways. The abstract frames **CLC** as a **carbon** **conversion** strategy where **oxygen carriers** such as **CuO** participate in **fuel oxidation**, motivating **atomistic** insight into **CuO–hydrocarbon** and **CuO–char** interfaces alongside **flame** measurements (abstract).

## Methods

### ReaxFF molecular dynamics (A/B)

- **Interaction model:** **ReaxFF** for **C/H/O** **hydrocarbon** and **solid-carbon** oxidation in contact with **CuO** nanoparticle motifs (parameter lineage in the **Combustion and Flame** article).
- **Simulation setup:** **Supercells**, **ensembles**, **thermostats**, and **reaction-path sampling** used to extract **effective barriers** for **CuO-surface** oxidation vs **O\(_2\)**-mediated channels—**full numerical settings** are in the **VOR/SI** (corpus file here is a **proof** PDF).

### Experiments (integrated)

- **Observables:** **Thermal response**, **flammability**, and **flame speeds** for **CuO + carbon** mixtures as summarized in the abstract.
- **Fuels:** **Gas-phase n-butane** versus **solid** **lignite** / **anthracite** proxies to span **volatile** vs **condensed** carbon.

### Kinetic analysis

- **Arrhenius** plots and **regime** assignments connect modeled **barriers** to measured **activation energies**, including **oxygen uncoupling** from **CuO** nanoparticles for **anthracite**-like cases.

### MD application (ReaxFF + solid fuel / CuO)

**Engine / code:** **LAMMPS**-style **ReaxFF** for **C/H/O** **hydrocarbon**/**char** in contact with **CuO** **nanoparticle**-like **models** as in *Combust. Flame*. **3D** **PBC** **supercell** size, **T** program, **timestep**, **ps**/**ns** stages, and **thermostat** for **sampling** **reaction** **barriers** are in the **VOR**/**SI** (this **galley** path is for **hash** provenance). **N/A** — no **NPT** **barostat** or **shock** **piston** in the protocol summarized on this page unless the **article** states it; **N/A** — no static **interfacial electric field**; **N/A** — no **replica**/**metadynamics** beyond the reported **RMD**; **Coulomb** and **QEq** **per** **VOR**.

## Findings

### n-Butane (gas-phase surrogate)

**CuO-surface** oxidation carries a much **lower barrier** than **O\(_2\) combustion** in the quoted comparison (**~9.2** vs **~53.3 kcal mol\(^{-1}\)** in the **abstract**), so **surface** oxidation dominates in that framing.

### Lignite (solid fuel)

**O\(_2\) combustion** vs **CuO-surface** reaction barriers are **closer** (**~23.0** vs **~6.3 kcal mol\(^{-1}\)** in the **abstract**), implying **stronger competition** between pathways.

### Anthracite model and CuO decomposition

**Arrhenius** analysis shows **two kinetic regimes**; the **crossover** is associated with **O\(_2\)** release from **CuO** nanoparticles, aligning with **experimental** shifts in **activation energy** when **CuO** decomposition matters.

### Integrated barrier–experiment link

The authors connect **simulated barriers** to **flammability** / **flame speed** trends to argue which **oxidation channel** limits **rate** in different **temperature** windows, spanning **volatile** and **condensed** carbon **CLC** scenarios.

## Limitations

Corpus PDF is an **Elsevier proof**; **final pagination** and **SI tables** should be checked against the **version of record**.

## Relevance to group

**van Duin-group** **ReaxFF** on **fuel oxidation** with **CuO** and **experimental** validation.

## Citations and evidence anchors

- DOI: [10.1016/j.combustflame.2022.112216](https://doi.org/10.1016/j.combustflame.2022.112216)

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
