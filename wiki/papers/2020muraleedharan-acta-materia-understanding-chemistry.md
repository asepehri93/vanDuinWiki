---
id: paper:2020muraleedharan-acta-materia-understanding-chemistry
type: paper
title: "Understanding the chemistry of cation leaching in illite/water interfacial system using reactive molecular dynamics simulations and hydrothermal experiments"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2019.12.059"
year: 2020
authors:
  - "Murali Gopal Muraleedharan"
  - "Ryan Herz-Thyhsen"
  - "Janet C. Dewey"
  - "John P. Kaszuba"
  - "Adri C. T. van Duin"
venue: "Acta Materialia"
pdf_sha256: "d3ab6f32448c721a1fa4384838ccdc8332e4485b90da67c81ebf689acbccc34a"
pdf_path: "papers/Muraleedharan_ActaMater_2020_Cation_Leaching.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020muraleedharan-acta-materia-understanding-chemistry -->

Large-scale **ReaxFF MD** of **illite/water** interfaces is paired with **hydrothermal leaching experiments** to resolve proton-mediated pathways for **K⁺**, **Al**, and **Si** release and to compare time scales with continuum leaching kinetics.

## Summary

Simulations show **K⁺** leaching earlier and at higher concentration than network **Al** and **Si**. Trajectory analysis identifies proton attack on **Al–O–Si** linkages via NBO protonation, silanol formation after **Al–O** cleavage, **K⁺** migration to the surface, **KOH** formation and outward diffusion, and later **Al(OH)₃**- or **Si(OH)₄**-like release contributing to Al/Si loss. **MD** surface reactivity is compared to bulk **hydrothermal** leach curves; the authors report **orders-of-magnitude** **gaps** between the two, motivating scale-bridging. Structural metrics indicate **more than 20%** cation loss is needed for strong illite distortion in the model. The work situates illite-rich clays in geothermal and barrier contexts; authoritative tables and numbers are in the **PDF**/SI, not recopied exhaustively on this page.

## Methods

**Experiment (hydrothermal leaching).** Natural or prepared **illite**-bearing material is leached in **autoclave** hydrothermal conditions; **aqueous** analytics follow **K**, **Al**, and **Si** over **laboratory** **(days–months)** time scales. **P**, **T**, and exact **sample** **preparation** are in the **version-of-record** at `pdf_path` (not in the short local **p1-2** extract).

**1 — MD application (illite / water, ReaxFF).** The study uses **large-scale ReaxFF reactive MD** of **illite in water** (code name: read the **Acta** **Methods**—often **LAMMPS** in this line of work). **System** **size** and **slab** **vs** **interlayer** **construction** are given in the **article** and **figures**; the **abstract** alone only states **large-scale** **ReaxFF** **MD**, not **N** **atoms**. **PBC:** **3D** **periodic** **slab-in-water** **(as** in **VOR**). **Ensemble:** **NVT** at **target** **temperatures** in **K** **(see** **VOR**; not only **p1-2**). **Timestep:** **0.25** **fs**; **integrator:** **velocity** **Verlet** **(Methods**). **Thermostat:** **Berendsen** with **0.1** **ps** **damping** **(temperature** **coupling**). **Duration** **/** **equilibration** **and** **production (ps** **/ ns):** **N/A** in the indexed **extract**—transcribe from **`pdf_path`**. **Barostat** **&** **hydrostatic** **pressure** **(NPT):** **N/A** for the **NVT** **stages** summarized here. **Shear** **/** **shock:** **N/A**. **External** **electric** **field:** **N/A**. **Replica** / **umbrella** / **metadynamics:** **N/A**; any **NEB**-style or reaction-path postprocessing is **post-trajectory** (see **VOR**). **QEq** update and **cutoffs** (ReaxFF): **N/A** in the p1-2 snippet—see **SI** / full text.

**2 — Force-field training.** **N/A**—the work **applies** a **cited** **ReaxFF** for aluminosilicate / illite-relevant chemistry; it is not a de novo QM-driven ReaxFF parameterization paper.

**3 — Static QM / DFT-only (headline result).** **N/A**—the lead evidence is **ReaxFF** **MD** **paired** with **experiments**; any **auxiliary** **QM** **(if** **listed**)** is **not** the **p1-2** **excerpt** focus.

## Findings

- **K⁺** is mobilized before substantial **Al/Si** network dissolution under the modeled neutral-water chemistry.
- Protonation sequence rationalizes **KOH**-mediated potassium transport and later **Al/Si** hydroxide release.
- MD-derived surface kinetics do **not** directly match bulk experimental leaching rates without additional transport or scaling arguments.
- Structural degradation becomes pronounced only after substantial cumulative leaching in the MD-based distortion metric.

## Limitations

Reactive FF accuracy for aluminosilicate clay edge/interlayer chemistry; accessible MD times vs laboratory leaching times; experiments on natural/powder samples may include mineral admixtures not in the idealized model.

## Relevance to group

van Duin (corresponding, Penn State Mechanical Engineering); collaboration with University of Wyoming geochemistry and hydrothermal experiments.

## Reader notes (navigation)

- [[2020muraleedharan-venue-paper]] (Elsevier PDF proof duplicate)
- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
