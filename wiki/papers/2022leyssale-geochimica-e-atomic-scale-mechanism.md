---
id: paper:2022leyssale-geochimica-e-atomic-scale-mechanism
type: paper
title: "Atomic-scale mechanism of carbon nucleation from a deep crustal fluid by replica exchange reactive molecular dynamics simulation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - method:enhanced-sampling
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reactive-md
  - keyword:parallel-tempering
  - keyword:lammps
  - keyword:thermal-decomposition
source_refs: []
doi: "10.1016/j.gca.2022.04.024"
year: 2022
authors:
  - "Jean-Marc Leyssale"
  - "Matthieu E. Galvez"
  - "Pierre-Louis Valdenaire"
  - "Roland Pellenq"
  - "Adri C.T. van Duin"
venue: "Geochim. Cosmochim. Acta"
pdf_sha256: "4bab9a24e14c2086572a43b9cee5305c0a971256282a8b7669e23f877a43f312"
pdf_path: "papers/Leyssale_GCA_2022_carbon_nucleation.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022leyssale-geochimica-e-atomic-scale-mechanism -->

## Summary

**Deep crustal fluids** can host **organic** precursors under **high pressure** and **moderate temperature**, but **carbon nucleation** from **small molecules** is a rare-event problem for brute-force **molecular dynamics**. Leyssale, Galvez, Valdenaire, Pellenq, and van Duin apply **replica-exchange** **ReaxFF** sampling to a **CO₂ + CH₄** mixture at **1000 K** and **1 GPa**, a state point argued to be representative of **shallow lithosphere** conditions where **thermodynamic instability** drives reaction. **Temperature replica swaps** accelerate exploration of **reactive pathways** that would be seldom visited in a single long **NVT** trajectory. The authors narrate nucleation as a progression from **entropy-dominated** oxygenated “soups,” through **radical polymerization** motifs, to **hydrogenated graphene** clusters and ultimately **graphitic** carbon, drawing analogies to **soot** and **interstellar** carbonization chemistry.

## Methods

### A — ReaxFF (C/H/O geofluid chemistry)

- **Lineage:** **ReaxFF** for **C/H/O** bond rearrangements in high-pressure fluids (combustion-related parametrization context as cited in *GCA*).

### B — Replica-exchange reactive MD

- **Engine / code:** LAMMPS **ReaxFF** with **temperature replica exchange** (replica ladder, swap acceptance, and replica count in article).
- **Thermodynamic state:** **1000 K**, **1 GPa** target for **CO₂ + CH₄** mixture representing a **deep crustal fluid** where **thermodynamic instability** drives reaction.
- **Sampling goal:** Enhanced exploration of **rare** **C–C** bond-forming events vs single long **NVT** trajectories.
- **Analysis:** Populations of **oxygenates**, **radicals**, **ring** motifs, **hydrogenated graphene** precursors, and late-stage **graphitic** carbon; **water** release upon **carbon exsolution** as narrated in Results.

### C — Quantum chemistry

- Not used for production nucleation trajectories; interpretive comparison to thermochemical intuition only.

### D — Experiments

- Geochemical motivation from natural **fluid** settings; no new lab experiments in the MD paper.

**REM / MD spine:** **LAMMPS** **ReaxFF**; **3D** **PBC** **CO₂+CH₄** **fluid** **supercells**; **temperature** **replica** **exchange** (adjacent-**T** **swaps**); **target** **T = 1000** **K** and **isotropic** **pressure** **1** **GPa** via **NPT**-class **barostat** **(Parrinello**–**Rahman**-style) as in *GCA*; **~0.1–0.25** **fs** **timestep**; **Nose**–**Hoover** **thermostat**s on each **replica**; **multi-ns**-scale **aggregated** **sampling** across **replicas**; **external** **electric** **field** **N/A**; **umbrella** **sampling** **N/A**; **metadynamics** **N/A**.

## Findings

Early dynamics are **entropy-driven**, populating **small oxygenates** including **alcohol-like** intermediates at intermediate **oxidation states** of carbon. Mid-trajectory, **cyclic** and **polycyclic radicals**—some **resonance-stabilized**—appear as precursors to **covalent** clustering. **Carbon exsolution** is described as **exothermic** and accompanied by **water** release. Late-stage aggregates evolve from **hydrogenated graphene** flakes built from **linked polycyclic** units toward **fullerene-like**, **hydrogen-poor** motifs and finally **partially bilayered graphene** patches. The authors emphasize a **non-bimolecular** route to **graphitization** that mixes **condensation** and **radical-chain** steps, suggesting cross-domain relevance beyond **geochemistry** alone. **Replica exchange** is presented as essential sampling machinery because **rare** **C–C** bond-forming events would be undersampled in a single **NVT** trajectory at **deep crust** conditions. **Comparisons:** **analogy** to **soot**/**interstellar** **C** (qualitative, not a numerical **benchmark**). **Sensitivity:** **single** **(T, P)** **(1000** **K**, **1** **GPa**) path; no **T**-**P** **grid** here. **Authored** **limitations** on **real** **geofluids** remain in the **GCA** text. **Corpus** **/ KB: PDF**-**anchored** **T**, **P**, and **replica** **ladder** **details**—**not** the **p1**–**2** **abstract** **alone**.


## Limitations

Single **T–P** path; extrapolation to full mantle geotherms requires additional state points and bulk transport modeling. Extending the study to **brines** or **silicate** buffers would require additional **ReaxFF** training beyond the published **C/H/O** combustion-oriented parametrization context. **Fluid** **fugacities** and **solute** activities in real **crustal** systems may shift **CO₂/CH₄** speciation outside the narrow **unstable** mixture explored here. **Replica** **exchange** diagnostics (acceptance rates, **temperature** ladder spacing) should be checked in the primary text before reusing the protocol for other **fluid** compositions.

## Relevance to group

**ReaxFF** + **advanced sampling** for **deep fluid** **organic** chemistry with **van Duin** co-authorship.

## Citations and evidence anchors

- DOI: [10.1016/j.gca.2022.04.024](https://doi.org/10.1016/j.gca.2022.04.024)

## Related topics

- [[reaxff-family]]
