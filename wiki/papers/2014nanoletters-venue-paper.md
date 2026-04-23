---
id: paper:2014nanoletters-venue-paper
type: paper
title: "Fluorination of graphene enhances friction due to increased corrugation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - material:graphene-carbon-nano
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:tribology
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:classical-ff
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/nl502147t"
year: 2014
authors:
  - "Qunyang Li"
  - "Xin Z. Liu"
  - "Sang-Pil Kim"
  - "Vivek B. Shenoy"
  - "Paul E. Sheehan"
  - "Jeremy T. Robinson"
  - "Robert W. Carpick"
venue: "Nano Letters"
pdf_sha256: "8fd7d8e73f5a730b5b30cc80a6a60487bd581c44c1f0269202077efe2a28949e"
pdf_path: "papers/ReaxFF_others/NanoLetters_Shenoy_et_al_2014.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014nanoletters-venue-paper -->

!!! abstract "Fluorinated graphene shows higher friction than pristine graphene in atomic-scale simulations, linked to increased surface corrugation (energy landscape roughness) from fluorination."

## Summary

This communication reports that **partial fluorination of graphene increases friction** in atomic-scale stick–slip simulations compared to pristine graphene. The authors relate the effect to **greater interfacial energy corrugation** (variation of interaction energy with lateral position) induced by fluorine, rather than to changes in contact area alone.

The study connects chemical functionalization of a 2D carbon surface to **tribological behavior at the nanoscale**, with implications for nanoscale contacts and surface-engineered graphene.

At the atomic scale, friction is often discussed via the Prandtl–Tomlinson picture where corrugation amplitude sets stick–slip severity; fluorination modulates that landscape chemically.

## Methods

Grounding: **`papers/ReaxFF_others/NanoLetters_Shenoy_et_al_2014.pdf`** (ACS **Just Accepted**, web date **29 Jul 2014** in extract) and `normalized/extracts/2014nanoletters-venue-paper_p1-2.txt` (metadata + keywords on file).

### 1 — MD application (atomistic dynamics)

The indexed extract records authorship/affiliations and **KEYWORDS** (**fluorinated graphene**, **friction**, **stick-slip**, **energy corrugation**) but **not** a complete simulation protocol.

- **Engine / code:** **Atomistic molecular dynamics**-style simulations are implied by the communication genre; **N/A — software** not in `2014nanoletters-venue-paper_p1-2.txt`.
- **System size & composition:** **N/A — not stated** in the indexed excerpt (fluorine **coverage**, tip model, and **atom** counts live in the full article).
- **Boundaries / periodicity:** **N/A — not stated** in the excerpt.
- **Ensemble:** **N/A — not stated** (no **NVT**/**NPT** line in `p1–2` text).
- **Timestep / duration / thermostat / barostat:** **N/A — not stated** in the excerpt.
- **Temperature:** **N/A — not stated** in the excerpt.
- **Pressure / normal load:** **N/A — not stated** in the excerpt (contact **pressure** is central to tribology but absent from `p1–2`).
- **Electric field:** **N/A — not stated.**
- **Replica / enhanced sampling:** **N/A — not stated.**

### Analysis framing (from keywords/title)

The study interprets **nanoscale friction** using **interfacial energy corrugation** and **atomic stick-slip** language (**KEYWORDS** in extract).

### Duplicate DOI note

Same DOI as **`[[2014li-venue-paper]]`** with a different `pdf_path`; pick one **PDF** for reproducibility and cite that path.

## Findings

### Outcomes and mechanisms

The communication (title/abstract themes echoed in **KEYWORDS**) argues **partial fluorination increases friction** versus **pristine graphene**, relating the effect to **increased energy corrugation** rather than contact area alone.

### Comparisons

**Pristine** versus **fluorinated graphene** is the primary **comparison** axis stated at ingest level.

### Sensitivity

**Fluorination** (surface chemistry / **coverage**) is the implicit **sensitivity** knob for friction in this framing; quantitative **coverage**–**friction** curves require the **final** **Nano Letters** **PDF**.

### Limitations and corpus honesty

**Just Accepted** PDF + **partial** extract: do not cite numerical loads, **timestep**s, or friction coefficients from this wiki page without checking the **version-of-record** article body.

## Limitations

- The ingest extract is **partial**; quantitative ranges (loads, coverage, simulation details) should be taken from the full PDF when citing specifics.
- Classical empirical potentials are used; **transferability** to different fluorine coverages, humid environments, or experimental tip chemistry requires case-by-case judgment.

## Relevance to group

Not a ReaxFF parameterization paper; it is relevant as **2D carbon surface chemistry + mechanics** context and as a citation for **functionalization-dependent interfacial energy landscapes** in nanoscale contacts.

## Reader notes (navigation)

- Theme hub: [[theme-oxides-silica-ceramics]].

## Citations and evidence anchors

- DOI: [10.1021/nl502147t](https://doi.org/10.1021/nl502147t)
