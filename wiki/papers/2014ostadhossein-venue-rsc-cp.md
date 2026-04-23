---
id: paper:2014ostadhossein-venue-rsc-cp
type: paper
title: "Stress effects on the initial lithiation of crystalline silicon nanowires: reactive molecular dynamics simulations using ReaxFF"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:metallic-systems
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/C4CP05198J"
year: 2014
authors:
  - "Alireza Ostadhossein"
  - "Ekin D. Cubuk"
  - "Georgios A. Tritsaris"
  - "Efthimios Kaxiras"
  - "Sulin Zhang"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys. (2014); DOI 10.1039/c4cp05198j"
pdf_sha256: "d95ad9dff270ad9e795c6fcaea4c7ad2a4f8b103fbd4e1e7bc70a8576e5ab9af"
pdf_path: "papers/Ostadhossein_PCCP_LiSi_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014ostadhossein-venue-rsc-cp -->

## Summary

Silicon **anodes** for lithium-ion batteries undergo large **volume expansion** and **stress** during **lithiation**, motivating atomistic models that connect **mechanical load** to **early-stage Li insertion** pathways. This **PCCP** article (Harvard/Kaxiras and Penn State collaboration; **Adri C. T. van Duin** coauthor) applies **ReaxFF reactive molecular dynamics** to **initial lithiation** of **crystalline silicon nanowires** under controlled **mechanical stress**, examining how stress couples to **Li** ingress, **phase** evolution, and **fracture** propensity at the nanoscale. Per [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md), the corpus **`pdf_path`** here is a **publisher proof** PDF; a **canonical sibling** with the **version-of-record** article PDF is **`[[2015ostadhossein-physical-che-stress-effects]]`** (`papers/Ostadhossein_PCCP_LiSi_2014.pdf`). Use the **VOR** PDF for authoritative pagination, final figures, and numerical tables.

## Methods

Grounding: **`papers/Ostadhossein_PCCP_LiSi_proof.pdf`** (publisher **proof** for **Phys. Chem. Chem. Phys.**, DOI `10.1039/C4CP05198J`) and `normalized/extracts/2014ostadhossein-venue-rsc-cp_p1-2.txt` (proof boilerplate + graphical-abstract lead only).

### 1 — MD application (atomistic dynamics)

The typeset article reports **ReaxFF reactive molecular dynamics** of **initial lithiation** in **crystalline silicon nanowires** under **stress** (**Summary**). On this slug, **numerical** **MD** protocol lines are **not recoverable** from the indexed extract.

- **Engine / code:** **ReaxFF MD** (article subject); **N/A — MD software** not in proof boilerplate excerpt.
- **System size & composition:** **Si nanowire** models with explicit **Li** insertion (**Summary**); **N/A — atom counts/dimensions** not in `p1–2` text.
- **Boundaries / periodicity:** **N/A — not stated** in the indexed proof excerpt.
- **Ensemble:** **N/A — not stated** in the indexed excerpt (likely **NVT**/**NPT** variants in article—confirm in **VOR** PDF).
- **Timestep / duration / thermostat / barostat:** **N/A — not stated** in the indexed excerpt.
- **Temperature:** **N/A — explicit set points** not in the proof excerpt on file.
- **Pressure / stress:** **Mechanical stress** control is the paper’s headline variable (**Summary**), but **N/A — quantitative stress protocol** not in `p1–2` text.
- **Electric field:** **N/A — not stated.**
- **Replica / enhanced sampling:** **N/A — not stated.**

### 2 — Force-field training

**N/A —** application-focused **ReaxFF** study on this topic; any **parameter** lineage discussion belongs to the **PCCP** article body.

### Canonical sibling (version of record)

Prefer **`[[2015ostadhossein-physical-che-stress-effects]]`** (`papers/Ostadhossein_PCCP_LiSi_2014.pdf`) for **pagination**, **tables**, and reproducible **MD** settings.

## Findings

### Outcomes and mechanisms

The manuscript (typeset) analyzes how **stress** modifies **early lithiation** in **crystalline Si nanowires**, including **heterogeneous** **Li** distribution and **mechanical failure** precursors in a **reactive** **MD** framing (**Summary**).

### Comparisons and sensitivity

**Stress state** is the primary **sensitivity** axis at the level of this wiki summary; **quantitative** stress–strain–composition relationships must be taken from the **VOR** **PDF**, not the proof excerpt.

### Corpus honesty

**Proof PDF** ingest + **boilerplate-heavy** extract: do not treat this slug as the authoritative source for **numbers**; use **`[[2015ostadhossein-physical-che-stress-effects]]`** for **evidence**-stable citations.

## Limitations

**Proof PDF** ingest complicates copy-paste of tables; **ReaxFF** accuracy limits predictions at high **Li** content and for long-time **diffusion**; nanowire models omit **binder**, **electrolyte**, and **SEI** complexity.

## Relevance to group

**van Duin**-coauthored **PCCP** contribution on **Si anodes** linking mechanics and lithiation—close to [[batteries-interfaces-reaxff]].

## Citations and evidence anchors

- https://doi.org/10.1039/C4CP05198J — PCCP article (`c4cp05198j`).

## Reader notes (navigation)

- Canonical VOR sibling: [[2015ostadhossein-physical-che-stress-effects]]

## Reader notes (MAS / retrieval)

Prefer **`[[2015ostadhossein-physical-che-stress-effects]]`** for VOR-grounded citations; keep this slug for proof-PDF provenance.

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
