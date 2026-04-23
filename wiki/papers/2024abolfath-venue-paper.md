---
id: paper:2024abolfath-venue-paper
type: paper
title: "A molecular dynamics simulation framework for investigating ionizing radiation-induced nano-bubble interactions at ultra-high dose rates"
updated: "2026-04-22"
confidence: low
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - domain:methods-software
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:galley-or-proof-pdf
candidate_tags:
  - "radiation-nanobubbles"
  - "ultra-high-dose-rate"
source_refs: []
doi: ""
year: 2024
authors:
  - "Ramin Abolfath"
venue: "Eur. Phys. J. D (proof/galley PDF in corpus; complete author list in VOR)"
pdf_sha256: "224262cd9776f149d5457ffa9100b0e974d0c65d9b914d9965ae0cf5b3f2731d"
pdf_path: "papers/Abolfath_Water_nanobubble_EurPhysD_2024_galley.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2024abolfath-venue-paper -->

## Summary

The corpus registers a **European Physical Journal D** **publisher proof/galley** PDF whose checked-in text extract begins with **author proof instructions** and **metadata**, not the scientific body of the article. **Metadata embedded in the proof** lists the article title **“A molecular dynamics simulation framework for investigating ionizing radiation-induced nano-bubble interactions at ultra-high dose rates”** and identifies **Ramin Abolfath** as corresponding author with affiliations including **Howard University**, **UT MD Anderson Cancer Center**, and **Sharif University of Technology**, alongside co-authors **Niayesh Afshordi** (**University of Waterloo** / **Perimeter Institute**) and **Sohrab Rahvar** (**Sharif University of Technology**). That scope statement—**ionizing radiation**, **aqueous nano-bubbles**, and **ultra-high dose-rate** conditions—signals an intersection of **radiation–matter** energy deposition models with **nanoscale cavitation** physics, but **numerical methods**, **potentials**, **timesteps**, and **dose-rate** definitions are **not recoverable** from the proof letter in **`normalized/extracts/2024abolfath-venue-paper_p1-2.txt`**. Treat this wiki entry as **provenance + metadata** until a **version-of-record** PDF or structured bibliography supplies **Methods**/**Results** text.

## Methods

### Extract / corpus status (D — review-style placeholder)

**Methods are not recoverable** from the checked-in **p1–2** extract (**proof** letter, not article body).

### Expected protocol categories (to fill from VOR — not asserted here)

**Water** model (**classical** vs **reactive**), **radiation** energy deposition (tracks vs coarse dose), **nanobubble** ICs, **BCs**, **Δt**, **MD**/**radiolysis** coupling—document after **full-text** ingest; refresh **`doi`**, **`normalized/`**, and this page together.

**Intended MD-style protocol (VOR TBD).** A **version-of-record** article is expected to specify a **molecular dynamics** **code**, **atom** counts, **PBC**/**wall** **boundaries**, **NVT**/**NPT**/**NVE** **ensemble**, **time step** (fs), **equilibration** and **production** (ps/**ns**), **thermostat**/**barostat** (damping) if **NPT** applies, **target** **temperatures**, **hydrostatic** **pressure** if used, and whether **ionizing** **radiation** is coupled via **prescribed** **energy** **deposition** or a hybrid scheme. **N/A**—none of the above are recoverable from the current **p1–2** **proof** **extract**; the wiki must **not** assert **dose** rates, **reactive** **force field** identity, or **sampling** schemes (no **metadynamics** until stated).

**MD application (corpus honesty).** The checked-in **proof** extract does not establish **LAMMPS**/**GROMACS** (or any) **MD** **package**, system **composition**, **timestep**/**duration**, **Nosé–Hoover**/**Berendsen** **thermostat** settings, **NPT** **barostat** parameters, or **N/A** for **external electric** **field**; treat all protocol lines as **N/A** until a **full** **PDF**/**VOR** backs them.

## Findings

No quantitative scientific findings are stated in the checked-in extract beyond publisher **metadata** fields (title, journal, author list). Do **not** cite **bubble** lifetimes, **dose-rate** thresholds, **radiolytic** yields, or **MD** performance metrics from this wiki entry. **Comparisons** to **experiment** or **literature** and **sensitivity** to **temperature** or **dose** are **N/A** in this **proof**-only state. **Limitations** and **outlook** are: refresh **`normalized/papers/2024abolfath-venue-paper.json`**, **`doi`**, and full-text **Findings** when a **VOR** PDF and **extraction** exist.

## Limitations

**DOI** and **full author list** are absent from normalized bibliography stubs at time of curation; **`extraction_quality`** is **partial**. **Confidence is low** by policy for proof-only ingest without article body text.

## Reader notes (MAS / retrieval)

Do not answer quantitative **radiation/MD** questions from this slug until **`doi`** and full-text extracts land.

## Relevance to group

Potential overlap with **radiation–matter** and **aqueous interface** simulation interests; **van Duin** involvement is **not** established from the extract.

## Citations and evidence anchors

<!-- Add DOI when registered in `normalized/papers/2024abolfath-venue-paper.json`. -->

## Related topics

- [[reaxff-family]]
