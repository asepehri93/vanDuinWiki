---
id: paper:2013berdiyorov-venue-c3ra43487g
type: paper
title: "Influence of vacancy defects on the thermal stability of silicene: a reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:nose-hoover
  - keyword:reactive-md
source_refs: []
doi: "10.1039/c3ra43487g"
year: 2013
authors:
  - "Berdiyorov, G. R."
  - "Peeters, F. M."
venue: "RSC Advances"
pdf_sha256: "a983525ae86a956a8fdfe3a715b1b74c8dcbd0ea7543a64ddba02afc55097791"
pdf_path: "papers/ReaxFF_others/Berdiyorov_silicene_RoySocAdv_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013berdiyorov-venue-c3ra43487g -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical results and figures, use the peer-reviewed article.

## Summary

Reactive molecular dynamics with **ReaxFF** is used to study how **vacancy defects** affect the structure and **thermal stability** of freestanding **silicene** (buckled honeycomb silicon). Pristine silicene is reported to remain stable up to about **1500 K** before transitioning toward a three-dimensional amorphous configuration on the simulated time scale. Vacancies locally distort the lattice and **lower** the critical temperature substantially (order tens of percent relative to the pristine case, depending on defect size), while the defective sheets are still described as stable well above room temperature for **500 ps** simulations. **Hydrogen termination** of dangling bonds at defect edges is reported to **improve** stability.

## Methods

### MD application (atomistic dynamics)

**Engine / code:** **LAMMPS** **reactive molecular dynamics** with **ReaxFF** (`papers/ReaxFF_others/Berdiyorov_silicene_RoySocAdv_2013.pdf`; `normalized/extracts/2013berdiyorov-venue-c3ra43487g_p1-2.txt`).

**System size & composition:** **960 Si** atoms in a buckled **silicene** supercell; **vacancy** models remove up to **several** atoms with local **reconstruction** motifs (**§3**).

**Boundaries / periodicity:** **Periodic boundary conditions** in the **basal plane** to suppress edge effects (**extract §3**).

**Ensemble / temperature protocol:** **NPT** heating at **4 K/ps** toward **2000 K**, then **500 ps** sampling at the target **temperature**; observables averaged over **five** velocity draws (**Methods** summary on this page).

**Timestep:** **0.25 fs** for all reported runs.

**Thermostat / barostat:** **Nosé–Hoover** thermostat (**100 fs** damping) and barostat (**2 ps** damping) under **NPT** (**Methods**).

**Pressure:** **NPT** barostat active during heating/sampling as described in the article (**target pressure** value **N/A —** not transcribed in this wiki—see **`pdf_path`**).

**Electric field:** **N/A —** not used.

**Replica / enhanced sampling:** **N/A —** standard **MD** heating only.

**Hydrogen passivation series:** Additional runs **saturate dangling bonds** at vacancy edges with **H** for comparison to bare vacancies (**abstract**).

### Force-field training

**N/A —** applies published **ReaxFF** **Si** chemistry (**parameter provenance** in **`pdf_path`**); no new **QM** refit is reported in this **application** article.

## Findings

**Outcomes:** **Pristine** buckled **silicene** remains **2D** up to **~1500 K** before transitioning to a **3D amorphous** configuration on **500 ps** trajectories; **Lindemann**-based metrics locate a sharp **2D→3D** transition near **~1450–1550 K** (article; excerpt abstract). **Vacancies** locally reconstruct (**pentagon**/**nonagon** motifs for monovacancies in the structural figures) and **reduce** the critical temperature by **>30%** relative to pristine sheets depending on **defect size**, while defective sheets remain stable **well above room temperature** within the same **500 ps** window (abstract/excerpt). **Hydrogen** passivation of **dangling bonds** at defect edges **increases** stability versus bare vacancies (abstract).

**Comparisons:** **DFT** literature values for **lattice** spacing and **buckling** are cited alongside **ReaxFF** relaxed geometries in **§3** of **`pdf_path`**.

**Sensitivity:** **Temperature** ramp rate (**4 K/ps** to **2000 K** in **NPT** heating), **vacancy size**, and **H** passivation.

**Limitations:** **960-atom** supercells, **500 ps** sampling, and **ReaxFF** transferability bound quantitative critical temperatures for **freestanding silicene**.

**Corpus honesty:** RSC Advances **publication year** in PDF header may read **2014** while frontmatter **year** stays **2013** per DOI metadata—use **`pdf_path`** pagination for citations.

## Limitations

- Finite system sizes, short nanosecond-scale trajectories, and force-field accuracy set bounds on quantitative critical temperatures and on transferability to supported silicene experiments.

## Relevance to group

Illustrates **ReaxFF** application to **2D group-IV** allotropes and defect chemistry—adjacent to the group’s broader reactive-MD materials work.

## Citations and evidence anchors

- Abstract and introduction: motivation, stability claims, passivation idea (RSC Adv.; DOI above).

## Reader notes (navigation)

- Sibling **publisher proof-query fragment** PDF: [[2013berdiyorov-venue-c3ra43487g-grabs]].

## Related topics

- [[reaxff-family]]
