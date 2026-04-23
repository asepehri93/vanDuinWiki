---
id: paper:2024he-chemical-eng-atomistic-insights
type: paper
title: "Atomistic insights into role of urea additive in lithium nanoparticles formation"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:organics-polymers-pyrolysis
  - task:application
  - domain:batteries-electrochemistry
paper_keywords:
  - keyword:lammps
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:nose-hoover
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1016/j.cej.2024.154822"
year: 2024
authors:
  - "Ruitian He"
  - "Kai H. Luo"
venue: "Chemical Engineering Journal, 497 (2024) 154822"
pdf_sha256: "c84fd0557a1f58412100929eb42ed2d7b9fc88589e4872f7a53c78569eefc107"
pdf_path: "papers/ReaxFF_others/Luo_group_combustion_synthesis.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024he-chemical-eng-atomistic-insights -->


## Summary

Reactive MD compares pyrolysis and oxidation of a lithium precursor droplet with and without urea at spray-flame-relevant conditions, linking urea to lithium distribution, cluster pathways, gas release, and microexplosion intensity. The study is positioned as **atomistic** support for how **urea**—often discussed in **flame spray pyrolysis** recipes—modifies **LiNO₃** decomposition, **cluster nucleation**, and **oxidation** in a hot **O₂** environment, even though the simulated droplet is **nanometric** rather than micrometric.

## Methods

Simulations use **bond-order ReaxFF MD in LAMMPS** with a **0.3 Angstrom** bond-order cutoff for connectivity. A **spherical droplet** (initial diameter **10 nm**, **373 K**) sits in a **40 nm** cubic box; the ambient beyond the droplet is **O2** at **0.1 MPa** with ambient temperatures **1500-3000 K** (main analysis at **1500 K**). The precursor is **LiNO3** at **2 mol/L** in water; **2.5 wt% urea** matches Deng et al. experiments cited in the paper. The **90-10** interface criterion gives droplet diameter and volume. Production runs use the **NVT** ensemble with a **Nose-Hoover** thermostat. The authors note droplets are nanoscale in the study versus micrometer-scale in practical flame spray pyrolysis but argue atomic-scale diffusion, reaction, and nucleation control product properties.

**1 — MD application (integrated).** **Engine:** **LAMMPS** with **ReaxFF** (bond-order connectivity). **System:** ~**10 nm** droplet in a **40 nm** cubic **periodic** box (full **atom** counts: **N/A** on this page—see article). **Ensemble / thermostat:** **NVT** with **Nose–Hoover**. **Timestep, trajectory length, equilibration vs production:** **N/A** here—see the PDF *Computational Methods*. **Barostat / GPa stress control:** **N/A** for the protocol summarized. **O2 environment** at **0.1 MPa**; **T** in **1500–3000 K** (main analysis **1500 K**). **Electric field** and **replica / umbrella / metadynamics** sampling: **N/A** in the material summarized. **2 — Force-field training:** **N/A** (uses an existing Reaxff description; not a new parametrization paper). **3 — Static QM:** **N/A** as the main methodology.
## Findings

**Outcomes and mechanism.** At **1500 K** and **0.1 MPa**, urea yields **more uniform lithium** in the droplet (radial Li density), **fewer large Li-rich agglomerates (Li3+X)**, and **more gas evolution** than the no-urea case. Microexplosion is **stronger with urea**: more H2 and carbon oxides trap in the droplet, enlarging the internal bubble and **fragmenting the droplet** (child droplet formation) versus a weaker burst without urea that leaves a deformed, Li-segregated droplet. The authors attribute finer Li-containing products to **altered cluster pathways**: Li clusters bond to urea-derived atoms, then break to gases, weakening Li-Li bonding (fewer Li-Li bonds after ~8 ns). Byproducts such as **ammeline/ammelide-type C_iN_xO_yH_z** species appear in the simulation, consistent with cited urea thermogravimetry literature.

**Comparisons and sensitivity.** The discussion references **Deng et al.** for recipe alignment (**2.5 wt% urea**) and uses **T**-dependent trends (**1500–3000 K**) in droplet and cluster metrics (**Fig. 5** in the paper). **Limitations** and **corpus honesty** are in **`## Limitations`**; ground quantitative claims in the **PDF** rather than this summary alone.
## Limitations

Nanoscale droplets and short simulated times do not map one-to-one to industrial **flame spray** reactors; thermochemistry and transport are **model-dependent** through the chosen **ReaxFF** parameterization and **NVT** thermostat. Extrapolation to other **precursors**, **oxidizer pressures**, or **urea** loadings requires additional validation.

## Relevance to group

Illustrates **LAMMPS/ReaxFF** applied to **lithium precursor** chemistry in **oxidizing** environments—adjacent to **battery** and **combustion synthesis** threads in the corpus, with explicit numerical **protocol** detail (box size, droplet criterion, temperature window).

## Citations and evidence anchors

- DOI: [https://doi.org/10.1016/j.cej.2024.154822](https://doi.org/10.1016/j.cej.2024.154822)

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
