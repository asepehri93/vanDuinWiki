---
id: paper:2017pulse-venue-paper
type: paper
title: "Pulse laser induced graphite-to-diamond phase transition: the role of quantum electronic stress"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1007/s11433-016-0421-0"
year: 2017
authors:
  - "ZhengFei Wang"
  - "Feng Liu"
venue: "Science China Physics, Mechanics & Astronomy"
pdf_sha256: "bbee186c8cb15593f514f134615c4a03efb5aafcb400fc7d072ca089a4103bd7"
pdf_path: "papers/Others/Pulse_laser_graphite_to_diamond_QES_role.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2017pulse-venue-paper -->

## Summary

Ultrafast laser excitation can drive a graphite-to-diamond structural transition without the macroscopic high-pressure apparatus used in conventional synthesis. This work frames that process using density-functional-theory-based first-principles calculations and the concept of **quantum electronic stress (QES)**: lattice stress arising from electronic excitation and carrier redistribution, formulated within the same theoretical lineage as excited-state stress descriptors in DFT. The authors study how photoexcited carriers in graphite generate QES, how that stress depends on carrier density and crystallographic direction, and how spontaneous structural relaxation can lower QES by transforming the bonding network toward a diamond-like arrangement. The abstract and introduction motivate QES as a quantitative handle—analogous to pressure in classical transitions—for characterizing laser-induced phase change when electronic excitation is the primary driver. The local corpus extract is **partial** (early pages plus publisher metadata); detailed numerical settings, convergence, and supercell choices for all reported relaxations should be confirmed from the full PDF when using this entry for quantitative reproduction.

## Methods

### 1 — MD application (atomistic dynamics)

**N/A** — this work is **static / first-principles** modeling of **photoexcited graphite** without reported production **AIMD** trajectories on the indexed pages.

### 2 — Force-field training

**N/A** — no classical reactive **FF** fit.

### 3 — Static QM / DFT-only

**Density-functional theory** calculations formulate **quantum electronic stress (QES)** as a stress tensor induced by **electronic excitation / carrier redistribution**, then use **DFT-based structural relaxation** of **graphite** polymorphs under imposed **carrier densities** to follow how **QES** evolves toward minima (abstract + introduction on indexed pages). **Functional, basis, cutoff, and k-mesh** settings that control the reported **QES** magnitudes and relaxed **c/a** trends are **not** duplicated here because the repository extract `normalized/extracts/2017pulse-venue-paper_p1-2.txt` is **partial** (front matter + introduction only).

- **Functional / level:** **N/A** — specific exchange–correlation designation beyond “first-principles DFT” is not stated in the indexed excerpt.
- **Dispersion:** **N/A** — vdW / **DFT-D** usage not stated in the indexed excerpt.
- **Basis:** **N/A** — localized vs plane-wave basis and cutoffs not stated in the indexed excerpt.
- **k-sampling:** **N/A** — **k**-mesh or Γ-only conventions not stated in the indexed excerpt.
- **Structures / pathways:** **Hexagonal** and **rhombohedral graphite** motifs discussed in the introduction as parents for **laser-induced** transformation toward **diamond**-like bonding when **QES** is minimized along relaxation pathways implied by the abstract.
- **Properties computed:** **QES tensor** components (especially **c-axis** anisotropy), **carrier-density** scaling (**approximately linear** growth of anisotropic **QES** with carrier density in the abstract), **total energy** changes along **structural relaxation** paths that lower **QES** while converting bonding topology toward **diamond**.

### 4 — Review / non-simulation framing

**N/A** — primary **research article** in *Sci. China Phys. Mech. Astron.*, not a review.

## Findings

### Outcomes and mechanisms

**Photoexcited carriers** in **graphite** generate a **large, anisotropic QES** whose magnitude grows **roughly linearly** with **carrier density** (abstract). Treating **QES** as a guiding stress variable, **structural relaxation** can **spontaneously** move the network from **graphite** toward **diamond**-like coordination as **QES** is **reduced and minimized** along the relaxation path.

### Comparisons

The authors frame **pulse-laser-induced** transformations by analogy to **pressure-induced** transitions, arguing **QES** plays a role similar to **mechanical pressure** for ranking polymorph stability under electronic excitation.

### Sensitivity / design levers

**Carrier density** and **crystallographic direction** (introduction emphasizes the **largest QES** along the **c-axis**) control how effectively **c/a** can be reduced, linking electronic excitation to the **graphite → diamond** pathway discussed for both **rhombohedral** and **hexagonal** graphite motifs.

### Limitations and corpus honesty

Indexed text is **partial**; **numerical thresholds** (critical carrier densities, stress tensor values in GPa, total-energy ordering of polymorphs) must be read from the **full article PDF** (`pdf_path`) and any **SI**—this page summarizes only what the abstract/introduction state on disk here.

## Limitations

Local PDF text extraction is **partial**; this note does not replicate all figures, supplementary material, or convergence data from the article.

## Relevance to group

Provides a DFT-level picture of **excited-state carbon** phase behavior, complementary to reactive MD and ReaxFF studies of carbon materials elsewhere in the corpus.

## Citations and evidence anchors

- DOI: [10.1007/s11433-016-0421-0](https://doi.org/10.1007/s11433-016-0421-0)

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
