---
id: paper:2013monti-venue-research
type: paper
title: "Reactive dynamics simulation of monolayer and multilayer adsorption of glycine on Cu(110)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:reactive-md
source_refs: []
doi: "10.1021/jp312828d"
year: 2013
authors:
  - "Susanna Monti"
  - "Cui Li"
  - "Vincenzo Carravetta"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "4c4f2af8dcf6307c560243c0da8cf4dbf0fe2395072fe4d848e8855599ffa1a0"
pdf_path: "papers/ReaxFF_others/Monti_Glycine_CuO_JPC_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013monti-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

The interaction of glycine with metal surfaces couples surface coordination chemistry with hydrogen-bond networks in two-dimensional adlayers. This Journal of Physical Chemistry C article uses **ReaxFF reactive molecular dynamics** to follow **neutral gas-phase glycine** impinging on **Cu(110)** across mono- and multilayer coverages. Reactive trajectories permit **deprotonation**, **zwitterionic-like** arrangements, and diffusion-mediated ordering over nanosecond-scale runs, capturing pathways that static single-configuration DFT would omit. The authors relate their structural motifs to experimental and theoretical literature on amino-acid ordering on copper, emphasizing how coverage modulates binding denticity and long-range chirality patterns. The 2013 JPCC study complements the companion Langmuir article on glycine and diglycine spectroscopy on Cu(110) by prioritizing dynamical pathways over static cluster models. Together, these papers illustrate when reactive MD is necessary for amino acids because proton transfers and H-bond networks fluctuate on simulation time scales accessible to ReaxFF but not to single-point DFT alone.

## Methods

**Engine / reactive model:** **ReaxFF** reactive molecular dynamics as implemented in the authors’ workflow (see article for code and timestep), with **bond-order** updates each integration step so **carboxyl deprotonation**, **interlayer proton transfer**, and **diffusion** can occur without preset reaction templates.

**System:** **Cu(110)** **slabs** with **in-plane periodic** boundary conditions; **neutral gas-phase glycine** starting structures evolve toward **anionic** **glycinate**-like motifs as summarized in the abstract. **Mono-** vs **multilayer** regimes are distinguished by **coverage** in the simulation protocol described in the paper.

**Thermodynamics / stages:** **Equilibration** and **production** segments use the **thermostatting** and **duration** choices stated in *J. Phys. Chem. C* (**full numerical table** not reproduced in the short extract; consult **`papers/ReaxFF_others/Monti_Glycine_CuO_JPC_2013.pdf`** for **timestep**, **ensemble**, and **total simulated time**).

**Analysis:** **Radial distribution functions**, **coordination** metrics, and **denticity** classification (**bidentate** vs **tridentate**) versus **coverage** follow the **Results** procedures; the abstract highlights **~2 Å** average **Cu–O/N** distances for the most stable motifs identified.

**MD slots not in p1–2 extract:** **N/A —** literal **LAMMPS**-level **integration** settings, **supercell atom** totals, full **3D periodic** cell vectors, whether **NPT** **pressure** coupling or **constant-volume NVT**/**NVE** legs are used for each stage, **target temperature** windows beyond the abstract’s qualitative thermalization language, **Berendsen**/**Nosé–Hoover**-class **thermostat** parameters, **electric fields**, and **enhanced sampling** are not quoted from **`normalized/extracts/2013monti-venue-research_p1-2.txt`**; confirm in **`papers/ReaxFF_others/Monti_Glycine_CuO_JPC_2013.pdf`**.

**2 — Force-field training:** **N/A —** employs literature **ReaxFF** for **glycine–Cu** chemistry.

**3 — Static QM / DFT-only:** **N/A —** primary evidence is **reactive MD** trajectories plus literature comparisons.

## Findings

**Outcomes and mechanisms:** **Chemisorbed** arrangements that **deprotonate** the **carboxyl** and **transfer protons** to **second-layer** molecules are among the most stable motifs identified, with **carboxyl oxygens** and **amino nitrogens** near **Cu** at roughly **2 Å** average distances (abstract). **Adsorption** proceeds through **multistep** pathways with **intermediate** coordination states.

**Comparisons:** **Low coverage** favors **bidentate**-like attachment, whereas **higher coverage** yields long-range ordered **heterochiral** domains where **tridentate** motifs become prominent, consistent with the **literature survey** embedded in the paper. **Reactive** trajectories connect **kinetic** accessibility of **zwitterionic-like** states to **long-range packing**, which **fixed-composition** energy minimizations would miss.

**Sensitivity / design levers:** **Coverage** modulates **denticity** and **chiral** ordering; **nanosecond-scale** runs place the model in a regime where **surface diffusion** and **reordering** compete with **desorption** for the **finite** cells used.

**Limitations and outlook:** **ReaxFF** parameters for **amino acids** on **transition metals** should be checked against **DFT** for quantitative energetics; **impingement** protocols may differ from slow **dosing** experiments.

**Corpus honesty:** Companion **spectroscopy/diglycine** study: **`[[2013monti-venue-la-2013-01746d]]`**.

## Limitations

ReaxFF parameters for amino acids on transition metals should be checked against DFT for quantitative energetics; finite system sizes may alter chiral domain sizes. Impingement protocols in MD may differ from molecular beam experiments dosing glycine slowly. Thermal equilibration assumptions should match the article when reproducing coverage-dependent ordering.

## Related topics

- [[reaxff-family]]
