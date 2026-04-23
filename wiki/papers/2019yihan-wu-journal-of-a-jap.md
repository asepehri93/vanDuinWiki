---
id: paper:2019yihan-wu-journal-of-a-jap
type: paper
title: "Strain-modulated early stage oxidation of Fe films"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - material:oxide
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:lammps
  - keyword:nose-hoover
  - keyword:npt-simulation
source_refs: []
doi: "10.1063/1.5094966"
year: 2019
authors:
  - "Yihan Wu"
  - "Wenshan Yu"
  - "Shengping Shen"
venue: "Journal of Applied Physics (2019), 125, 245305"
pdf_sha256: "ebbf477e1689731b98af8632f1364f7e50c5769531d6ca605ad7eb5974798d36"
pdf_path: "papers/ReaxFF_others/Wu_JAP_2019_Fe_oxidation_strain.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019yihan-wu-journal-of-a-jap -->

!!! abstract "Summary"

ReaxFF Fe/O/H molecular dynamics in LAMMPS simulates early oxidation of biaxially prestrained Fe(100), Fe(110), and Fe(111) films exposed to high O₂ pressure in a vacuum gap. Nosé–Hoover NPT equilibration, strain application, and 500 ps production at 1 fs with QEq each step bracket the oxidation kinetics reported below.

## Summary

Early-stage metal oxidation couples oxygen flux, surface orientation, and mechanical strain in thin films. Wu et al. study bcc iron slabs with ReaxFF Fe/O/H parameters in LAMMPS, applying biaxial prestrain to Fe(100), Fe(110), and Fe(111) films before exposing surfaces to molecular oxygen at elevated gas-phase pressure relative to ambient. Charge equilibration each timestep captures polar bond evolution during oxidation. The study targets strain-engineered oxidation differences relevant to films grown on mismatched substrates where residual stress is unavoidable.

## Methods

**Engine / code:** **LAMMPS** with **ReaxFF** **Fe/O/H** (as in *J. Appl. Phys.* **125**, **245305**). **System:** **bcc** **Fe** **slabs**; simulation cells are approximately **30 × 30 × 30 Å** body-centered-cubic **iron** slabs with **periodic** boundaries **in-plane** and a **vacuum** gap holding on the order of **21–23** **O₂** molecules corresponding to roughly **10 MPa** equivalent **ideal-gas** **pressure** in the article’s estimate. Preparation equilibrates **iron** at **600 K** for **30 ps** using **Nosé–Hoover** **NPT** dynamics, then ramps **biaxial** **prestrain** to **tensile** limits near **8%**, **7%**, and **8%** or **compressive** limits near **−3%**, **−2.6%**, and **−1.5%** for **(100)**, **(110)**, and **(111)** surfaces respectively, matching the values quoted in **Section II**. **Production** **oxidation** runs **500 ps** with a **1 fs** **timestep** and **QEq** every step, with an **O₂** **replenishment** heuristic tied to **oxygen** **charges** near the surface. **Oxide** **phase** identification and **diffusivity** calculations follow post-processing definitions in the article. Full reproducibility requires the exact **ReaxFF** file, **strain** tensors, **thermostat** **damping** parameters, and **boundary** conditions from *J. Appl. Phys.* **125**, **245305**, **DOI** 10.1063/1.5094966.

**Electric field:** **N/A** — not used. **Replica / metadynamics / umbrella:** **N/A** — not reported. **NPT** during **production** **oxidation:** the excerpt above uses **NVT**-like **production** with **O₂** gas—confirm against the PDF whether **NPT** applies to the **slab+gas** cell during **oxidation**; if strictly **NVT**/**NVE**, then **NPT** **barostat** is **N/A** for that **stage** per the article.

## Findings

Oxygen occupies tetrahedral sites during oxidation with body-centered-cubic to face-centered-cubic transformations, especially on (100). Prestrain changes the relative oxidation rates among facets and steers ordered versus disordered oxide evolution. Fe/O diffusivities at 1:1 stoichiometry are very low in the modeled regime, suggesting FeO can slow further oxygen ingress. Together, the results link elastic loading to early oxidation microstructure. The facet-dependent ordering suggests that texture engineering could steer protective versus porous oxide morphologies even before long-term corrosion enters the picture. Corrosion modelers should import both the strain tensor and the facet distribution from experimental texture data when attempting quantitative match, because the paper shows strong orientation sensitivity even under identical oxygen pressure. The high O₂ pressure used to accelerate oxidation should be interpreted as a computational convenience analogous to elevated temperature in other rare-event studies: it reveals pathways that may also appear at ambient pressure over longer times, but relative rates may shift. Finally, QEq every timestep is computationally expensive; reproduction budgets should account for that cost when scaling to larger slabs.

## Limitations

High O₂ pressure accelerates reactions beyond ambient corrosion timescales; thin-film strain states are idealized.

## Relevance to group

ReaxFF iron oxidation benchmark with mechanical loading coupling.

## Citations and evidence anchors

DOI: [10.1063/1.5094966](https://doi.org/10.1063/1.5094966)

## Related topics

- [[reaxff-family]]
