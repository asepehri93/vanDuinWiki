---
id: paper:2017shuttleworth-j-phys-chem-development-reaxff
type: paper
title: "Development of the ReaxFF Reactive Force-Field Description of Gold Oxides"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:catalysis-surfaces
  - method:reaxff
  - material:metal-surface
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:catalysis-surface
  - keyword:oxide-surface
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.7b08832"
year: 2017
authors:
  - "I. G. Shuttleworth"
venue: "The Journal of Physical Chemistry C 121, 25255–25270 (2017)"
pdf_sha256: "3e71aaecfe30a5542eda7a5129e6a58f54673ddc572bb2ed3b471cff4f3808fd"
pdf_path: "papers/ReaxFF_others/Shuttleworth_JPCC_AuO_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017shuttleworth-j-phys-chem-development-reaxff -->

## Summary

Gold surfaces are often considered inert, yet **oxygen** interactions at **Au** interfaces matter for oxidation catalysis, surface science, and nanoscale processing. This **Journal of Physical Chemistry C** article develops a **ReaxFF** description for **Au–O** chemistry by training against **quantum mechanical** data for **bulk and surface** gold, **O\(_2\)**, and **gold oxide** motifs. The resulting model supports **large-scale MD** of **O\(_2\)** interacting with multiple **Au** facets and reconstructions, as well as **grand canonical Monte Carlo combined with MD (GC-MC/MD)** sampling for **Au nanoclusters** where facet-specific reactivity is central. The work is positioned as enabling reactive simulations at scales inaccessible to routine **DFT dynamics**, while retaining a bond-order reactive framework consistent with broader ReaxFF practice.

## Methods

### 1 — MD application (atomistic dynamics)

Validation **molecular dynamics** uses the fitted **ReaxFF** model to emulate **O\(_2\)** interacting with **Au(111)** and several **Au(110)**/**Au(100)** reconstructions reported in the abstract—**missing-row (1×2)-mr-Au(110)**, **pairing-row (1×3)-pr-Au(110)**, **trenched (1×3)-tr-Au(110)**, and **added-row (2×1)-ar-Au(100)**—together with **grand canonical Monte Carlo / MD (GC-MC/MD)** sampling of **Au nanoclusters** where **O\(_2\)** adsorption/desorption attempts alternate with **MD relaxation** of surface stress at a fixed **oxygen chemical potential** (*J. Phys. Chem. C* **121**, 25255–25270).

- **Engine / code:** **ReaxFF** reactive MD as described in the article (typical deployment uses **LAMMPS** in this literature; confirm executable and input decks in **`pdf_path`**).
- **System size & composition:** **Au** slabs with the reconstructions named above plus **finite Au nanoclusters** for **GC-MC/MD**; explicit **atom counts** per figure are **N/A** on the indexed abstract pages.
- **Boundaries / periodicity:** **N/A** — slab **PBC** vs cluster boundary conditions are not restated in the indexed excerpt.
- **Ensemble:** **N/A** — **NVT/NPT** labels for the O\(_2\) impingement trajectories are not in the indexed excerpt.
- **Timestep:** **N/A** — **Δt (fs)** not in the indexed excerpt.
- **Duration / stages:** **N/A** — total **ps/ns** per validation case not in the indexed excerpt.
- **Thermostat:** **N/A** — not stated in the indexed excerpt.
- **Barostat:** **N/A** — hydrostatic **NPT** not indicated on indexed pages for these gas–surface runs.
- **Temperature:** **Thermal processing** toward **melting** of **Au** is discussed qualitatively for **subsurface O** uptake in bulk; numeric **K** schedules are in the **PDF**, not duplicated here.
- **Pressure:** **N/A** — bulk **hydrostatic** targets not summarized on indexed pages.
- **Electric field:** **N/A** — not used.
- **Replica / enhanced sampling:** **N/A** for pure **MD** legs; **GC-MC/MD** couples **Monte Carlo** oxygen exchanges with **MD**.

### 2 — Force-field training

**ReaxFF Au–O** development fits bond-order parameters against an **extended QM training set** spanning **bulk Au**, **O\(_2\)**, **gold oxides**, and **Au surfaces** including the reconstructions above; **Au–Au** terms are reinvestigated where **reconstructions** modify near-surface bonding, with **relativistic** corrections evaluated as stated in *JPCC*.

### 3 — Static QM / DFT-only

**DFT (and related QM)** reference data drive the **parameter optimization**; **QM MD** is not the large-scale validation engine.

### 4 — Review / non-simulation framing

**N/A** — primary **parameterization + validation** article, not a review.

## Findings

### Outcomes and mechanisms

**Subsurface oxygen diffusion** into bulk **Au** is **strongly limited** in the modeled regimes and becomes prominent mainly when **thermal processing approaches substrate melting**, matching the picture that bulk oxide formation is difficult until **high-temperature** processing overcomes kinetic barriers. **GC-MC/MD** on **nanoclusters** indicates **(111)** and **(100)** facets remain comparatively **unreactive** toward **O\(_2\)** under the explored conditions—consistent with experimental **facet inertness** trends in the authors’ framing.

### Comparisons

Simulation trends are explicitly compared to **experimental** expectations for **Au oxidation** and **oxygen** penetration depth.

### Sensitivity / design levers

**Oxygen chemical potential** (via **GC-MC/MD**) and **temperature** jointly set **surface vs subsurface** oxygen uptake on **finite** particles; **reconstruction** family changes the **Au–O** reactivity landscape on extended surfaces.

### Limitations and corpus honesty

Claims are **ReaxFF-contingent**; **electrolyte**, **solvation**, and **electrochemical bias** outside the **Au–O** training scope require additional validation. **Thermostat/timestep** numerics for each validation run live in **`pdf_path`**, not in the indexed abstract snippet.

## Limitations

Transferability outside **Au–O** chemistry (organics, halides, electrochemical double layers) requires additional training and validation.

## Reader notes (MAS / retrieval)

Emphasize **GC-MC/MD** oxygen reservoirs when summarizing **nanoparticle** facet inertness claims.

## Relevance to group

Worked example of **ReaxFF reparameterization** for **noble-metal oxidation** with explicit **surface-structure** coverage and **GC** sampling.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.7b08832](https://doi.org/10.1021/acs.jpcc.7b08832)

## Related topics

- [[reaxff-family]]
