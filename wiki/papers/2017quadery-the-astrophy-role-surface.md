---
id: paper:2017quadery-the-astrophy-role-surface
type: paper
title: "Role of Surface Chemistry in Grain Adhesion and Dissipation during Collisions of Silica Nanograins"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:water-silica-geo
  - method:classical-md
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:oxide-surface
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.3847/1538-4357/aa7890"
year: 2017
authors:
  - "Abrar H. Quadery"
  - "Baochi D. Doan"
  - "William C. Tucker"
  - "Adrienne R. Dove"
  - "Patrick K. Schelling"
venue: "The Astrophysical Journal 844, 105 (2017)"
pdf_sha256: "5766e4a703280b38957fc9de1c79a39115d6f9a9929be508e662aaa09e8a65ef"
pdf_path: "papers/ReaxFF_others/Quadery_2017_ApJ_844_105.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017quadery-the-astrophy-role-surface -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

## Summary

This Astrophysical Journal article uses classical atomistic simulations of colliding nanometer-scale silica grains to probe how surface hydroxylation and broader surface chemistry modify adhesion and kinetic-energy dissipation during pairwise impacts. The scientific motivation is planet formation: growth from dust to planetesimals begins in a regime where non-gravitational forces dominate, and laboratory experiments on sticking often use mineral grains whose surfaces are more passivated than grains in protoplanetary environments. The authors connect their simulations to longstanding puzzles about collisional growth barriers and to coarse contact models such as Johnson–Kendall–Roberts and soft-sphere approaches that lump surface interactions into effective surface energies without explicit chemistry. The introduction additionally contrasts classical velocity limits for sticking derived from idealized models with experimental and simulation evidence that real collisions often fragment grains except at very low speeds, motivating explicit chemical interaction models that can modify sticking probabilities beyond van der Waals scaling laws.

## Methods

### 1 — MD application (atomistic dynamics)

**Classical atomistic simulations** (pairwise **collision MD** of **nanometer SiO₂** grains) probe how **surface hydroxylation / passivation** changes **adhesive forces** and **kinetic-energy dissipation** during impacts, motivated by **planet-formation** dust coagulation where **chemical environment** differs between **Earth laboratories** and **space** (*Astrophys. J.* **844**, 105; DOI in front matter). The indexed extract `normalized/extracts/2017quadery-the-astrophy-role-surface_p1-2.txt` covers **introduction + abstract**; **numerical MD settings** below are therefore **`N/A` from the excerpt** and must be read from **`pdf_path`**.

- **Engine / code:** **Classical molecular dynamics** with a **fixed Si/O potential** for **silica** (functional form and parameter source named in the article Methods).
- **System size & composition:** **Nanometer-scale SiO₂** grains with **controlled surface chemistry** (hydroxylated vs less-passivated limits compared in the article); explicit **atom counts** are **N/A** on the indexed pages.
- **Boundaries / periodicity:** **N/A** — whether grains use **PBC** or free clusters is not stated in the indexed excerpt.
- **Ensemble:** **N/A** — **NVE/NVT/NPT** choice not stated in the indexed excerpt.
- **Timestep:** **N/A** — **Δt (fs)** not stated in the indexed excerpt.
- **Duration / stages:** **N/A** — collision staging / equilibration lengths not stated in the indexed excerpt.
- **Thermostat:** **N/A** — thermostat not stated in the indexed excerpt (binary collisions may be **NVE**-like; confirm in PDF).
- **Barostat:** **N/A** — **NPT** barostat not indicated for the collision protocol on indexed pages.
- **Temperature:** **N/A** — thermostatted target **T** not stated in the indexed excerpt.
- **Pressure:** **N/A** — bulk **hydrostatic pressure** control not stated for the collision runs on indexed pages.
- **Electric field:** **N/A** — not used.
- **Replica / enhanced sampling:** **N/A** — direct collision sampling.

### 2 — Force-field training

**N/A** — the work **adopts** a published **classical Si/O** model for **silica**; it does **not** report a new **ReaxFF** or **DFT** refit.

### 3 — Static QM / DFT-only

**N/A** — **DFT** is **not** the engine for the reported **collision MD** (any QM cited is contextual literature, not on-the-fly dynamics here).

### 4 — Literature / modeling context (non-MD primary text)

Introduction surveys **Johnson–Kendall–Roberts** / **soft-sphere** contact models, **population-balance** collision statistics, and experimental fragmentation trends to motivate **explicit chemistry** beyond **vdW-only** adhesion.

## Findings

### Outcomes and mechanisms

Surface **hydroxylation** weakens **adhesive forces** and reduces **kinetic-energy dissipation** during pairwise **nanosilica** collisions versus **less-passivated** surfaces in the authors’ models—consistent with **stronger chemical bonding** contributions during close approach rather than **vdW-only** scaling.

### Comparisons

The discussion contrasts **Earth-like passivated** mineral surfaces with **space-like** surfaces where **dangling bonds** may persist, arguing laboratory **sticking** experiments can be **pessimistic** relative to astrophysical regolith if chemistry differs. **Continuum JKR / soft-sphere** pictures are cited as **incomplete** without explicit **reactive** interaction terms.

### Sensitivity / design levers

**Surface termination** (hydroxyl coverage vs bare/reactive silica) and **collision velocity** (up to **several km s⁻¹** for **negligible angular momentum** nanograins in the article’s scenario) shift outcomes between **adhesion** and **fragmentation** channels.

### Limitations and corpus honesty

Results are demonstrated for **nanometer** grains with **negligible angular momentum**—distinct from macroscopic impact experiments where **fragmentation** dominates at much lower speeds unless chemistry changes. Full **velocity sweeps**, **statistics**, and **parameter tables** are on **`pdf_path`**; this summary follows the **abstract + introduction** captured in-repo.

## Limitations

Coarse models of grains as spheres with simplified contact mechanics are contrasted in the paper; full astrophysical environments (ice, charging, radiation) extend beyond the silica-focused setup.

## Relevance to group

Connects **tribology-style surface chemistry** to planetary science; methodological kinship with atomistic studies of oxide interfaces and water-driven passivation elsewhere in the knowledge base.

## Citations and evidence anchors

- DOI: [10.3847/1538-4357/aa7890](https://doi.org/10.3847/1538-4357/aa7890)

## Reader notes (navigation)

- Astrophysical dust aggregation (classical MD): [[theme-oxides-silica-ceramics]]; tribology-adjacent surface chemistry.

## Related topics

- [[theme-oxides-silica-ceramics]]
- Oxide nanoparticles and surface hydroxylation (corpus cross-links)
