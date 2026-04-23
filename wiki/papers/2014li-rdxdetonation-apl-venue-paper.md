---
id: paper:2014li-rdxdetonation-apl-venue-paper
type: paper
title: "Multistage reaction pathways in detonating high explosives"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:shock-compression
  - keyword:reactive-md
  - keyword:energetic-materials
  - keyword:aimd
candidate_tags: []
source_refs: []
doi: "10.1063/1.4902128"
year: 2014
authors:
  - "Li, Ying"
  - "Kalia, Rajiv K."
  - "Nakano, Aiichiro"
  - "Nomura, Ken-ichi"
  - "Vashishta, Priya"
venue: "Applied Physics Letters"
pdf_sha256: "7b37c2b405450da0aec26e06b1e311a4c87b5f3bfef9d4d807dad738b8118f2b"
pdf_path: "papers/ReaxFF_others/Li-RDXdetonation-APL14.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014li-rdxdetonation-apl-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

Large-scale reactive MD of shocked RDX crystal—validated against shorter quantum MD—resolves a two-stage chemistry: rapid N₂ and H₂O production within ~10 ps followed by delayed CO evolution past nanoseconds. Metastable carbon- and oxygen-rich clusters with fractal shapes are argued to bottleneck further oxidation to small gases; distinct unimolecular versus intermolecular channels are identified for the fast N₂ and H₂O channels (abstract; extract). The Letter situates the problem in the broader **detonation** context: **reaction-zone** width and **reaction time** are tied to **intermediate** products, and **sub-nanosecond** **RDX** pathways under **high P/T** had been poorly mapped because few reactive MD studies spanned both **~100 nm** length and **~100 ps** time scales simultaneously—motivating the scalable **ReaxFF** implementation (introduction, extract).

## Methods

### Reactive model and validation ladder

- **Large-scale parallel ReaxFF MD** (domain decomposition + message passing) targets **shock-induced chemistry** in **crystalline RDX**, with **subset trajectories** compared to shorter **quantum molecular dynamics (QMD)** benchmarks (**abstract**; introduction).

### Initial crystal / supercell (pre-shock)

- The Letter cites an **168 × 5 × 5** stack of **RDX unit cells** in a simulation box **~22.28 × 5.787 × 5.354 nm³** equilibrated near **room temperature** before **shock** loading (**APL** **105**, **204103**; extract).

### ReaxFF formulation (qualitative)

- **ReaxFF** uses **bond orders**, **dynamic charges**, and an **electronegativity equalization**-style scheme to follow **bond making/breaking** at cost below full **QMD** (extract/introduction).

### Shock protocol details

- **Piston speed**, **thermostatting**, and **duration** of the production shock runs appear in **APL** Methods—beyond the short extract on this wiki page.

### 1 — MD application (shocked crystalline RDX)

- **Engine / code:** **Large-scale parallel ReaxFF MD** with **domain decomposition** + **message passing** as stated in the **abstract**/introduction (extract); **N/A — explicit program name string not on indexed extract p1–3** (confirm in `papers/ReaxFF_others/Li-RDXdetonation-APL14.pdf`).
- **System size & composition:** **168 × 5 × 5** stack of **RDX unit cells** in a box **~22.28 × 5.787 × 5.354 nm³** equilibrated near **room temperature** before **shock** loading (**APL** **105**, **204103**; extract).
- **Shock / shear:** **shock** loading of the **crystal** after equilibration (**abstract**/introduction framing); **N/A — piston speed, shock direction, and Hugoniot state variables not on indexed extract p1–3** (APL Methods).
- **Boundaries / periodicity:** **PBC** implied by **crystal supercell** shock setup language in the Letter class; **N/A — explicit PBC statement not copied here** (PDF).
- **Ensemble:** **N/A — headline shock MD ensemble (NVT vs NVE vs MSST) not stated on indexed extract p1–3** (APL Methods).
- **Timestep / thermostat / barostat / production duration:** **N/A — not stated on indexed extract p1–3** (APL Methods).
- **Temperature / pressure:** **Room-temperature** **pre-shock** equilibration is noted for the initial cell (**extract**); **post-shock** thermodynamic control—**N/A — not on indexed extract p1–3**.
- **Electric field:** **N/A — not indicated** in the indexed extract opener.
- **Replica / enhanced sampling:** **N/A — not indicated** in the indexed extract opener.

### 2 — Force-field training

**N/A — new ReaxFF parameterization is not the focus** of the indexed abstract/extract window; the Letter emphasizes applying **ReaxFF** chemistry with **QMD** validation subsets (**abstract**).

### 3 — Static QM validation ladder

- **Quantum MD (QMD):** shorter **QMD** trajectories used as a **validation** reference against **ReaxFF** subsets (**abstract**); **N/A — DFT functional/basis/cutoffs not on indexed extract p1–3**.

## Findings

Simulations report a **two-stage** mechanism: **rapid N\(_2\)** and **H\(_2\)O** formation on **~10 ps** timescales, then **delayed CO** evolution on **nanosecond** timescales. **Large metastable carbon- and oxygen-rich clusters** with **fractal** morphology **bottleneck** further oxidation to **small gas products**, especially **CO**. **Distinct** **unimolecular** versus **intermolecular** routes dominate the **fast N\(_2\)** versus **fast H\(_2\)O** channels, respectively (abstract; extract pages 1–3). The authors highlight this as **first evidence** in their setup for **large C/O-rich clusters** as **intermediates** that **inhibit** **CO** production, yielding the **staged** picture of **N\(_2\)/H\(_2\)O** first and **CO** later (abstract paragraph in extract). The introduction also sketches the **detonation-wave** picture (**von Neumann spike**, reaction zone) to motivate why **intermediate** inventory sets **effective** **reaction time** in **HE** modeling (introduction, extract).

## Limitations

Reactive MD fidelity depends on the underlying reactive force field; extreme shock conditions stress any classical model.

## Citations and evidence anchors

- DOI `10.1063/1.4902128` (extract citation line).
- Abstract (extract page 1).

## Related topics

- [[theme-pyrolysis-combustion-organics]]
