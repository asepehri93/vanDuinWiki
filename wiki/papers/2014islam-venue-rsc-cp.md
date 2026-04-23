---
id: paper:2014islam-venue-rsc-cp
type: paper
title: "ReaxFF molecular dynamics simulations on lithiated sulfur cathode materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:sulfur-cathode
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1039/c4cp04532g"
year: 2014
authors:
  - "Islam, Md Mahbubul"
  - "Ostadhossein, Alireza"
  - "Borodin, Oleg"
  - "Yeates, A. Todd"
  - "Tipton, William W."
  - "Hennig, Richard G."
  - "Kumar, Nitin"
  - "van Duin, Adri C. T."
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "a6eb8426d591361076de046dcaa442d73ae36a05293745fbfe67bcd5ee86a358"
pdf_path: "papers/Islam_PCCP_LiS_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014islam-venue-rsc-cp -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Corpus note:** this slug registers the **RSC author-proof PDF** (`papers/Islam_PCCP_LiS_proof.pdf`). Maintainer mapping of **proof vs VOR** PDFs: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md). The **same scientific article** is summarized in full on **`[[2014islam-physical-che-reaxff-molecular]]`**, which uses the **journal article PDF** (`papers/Islam_PCCP_LiS_2014.pdf`). The work develops a **ReaxFF** parametrization for **Li–S** chemistry to run **MD** of **amorphous lithiated sulfur** (**a-Li\(_x\)S**) and relate **lithiation** to **mechanical moduli** (**ultimate stress**, **yield**, **Young’s modulus**) and **ionic transport**. It combines **diffusion** data for **Li** and **S**, **GCMC**-based **open-circuit voltage** trends, and **genetic-algorithm**-assisted **binary phase diagram** construction to frame **Li–S cathode** thermodynamics and mechanics at the atomistic level.

## Methods

Canonical **protocol** detail lives on **`[[2014islam-physical-che-reaxff-molecular]]`** (journal PDF); this **proof** ingest should not be used to invent **SI** locators not visible in the **proof** text.

### Force-field training / reactive MD (same article as VOR)

- **New ReaxFF** terms for **Li–S** interactions trained against **QM** benchmarks summarized in **PCCP** (see VOR Methods/ESI).
- **MD** on **amorphous lithiated sulfur** (**a-Li\(_x\)S**) for **mechanical** stress–strain curves and **Li/S diffusion** statistics vs **lithiation**.

### Electrochemical / thermodynamic modeling

- **GCMC** scheme to construct **open-circuit voltage** trends along discharge (abstract framing).
- **Genetic-algorithm**-based workflow to assemble a **Li–S binary phase diagram** (as described in the article body).

### Integration settings

- **Ensemble, timestep, thermostat, electrostatic cutoffs:** follow the **final PCCP** article and **ESI** on **`[[2014islam-physical-che-reaxff-molecular]]`**—**N/A — not duplicated from this proof-ingest page**.

### 1 — MD application

- **Protocol detail:** same **PCCP** study as **`[[2014islam-physical-che-reaxff-molecular]]`**; **N/A — engine/timestep/thermostat not transcribed from `papers/Islam_PCCP_LiS_proof.pdf` here** (use VOR Methods).
- **System size & composition:** **a-Li\(_x\)S** **supercells** for mechanical/transport sampling as described in **PCCP**; **exact atom counts** are **N/A — not duplicated on this proof-ingest page** (VOR Methods).
- **Boundaries / periodicity:** **3D PBC** bulk framing is implied for **a-Li\(_x\)S** **MD** in this article class; **N/A — explicit PBC statement not re-keyed from the proof PDF here**.
- **Ensemble / timestep / thermostat:** **N/A — not re-keyed from the proof PDF here** (VOR Methods/ESI).
- **Duration / stages (equilibration vs production):** **N/A — not re-keyed from the proof PDF here** (VOR Methods).
- **Barostat / hydrostatic pressure control:** **N/A — not re-keyed from the proof PDF here** (confirm NVT vs NPT on VOR page).
- **Temperature:** **N/A — explicit thermostat/set points not re-keyed from the proof PDF here** (VOR Methods).
- **Electric field:** **N/A — not indicated** in the abstract-level summary used for this duplicate ingest.
- **Replica / enhanced sampling (MD):** **N/A — not indicated** in the abstract-level summary; **GCMC** is used separately for **OCV**.

### 2 — Force-field training

- **Scope:** **Li–S ReaxFF** development against **QM** references as in **PCCP**; **N/A — training tables not re-keyed from the proof PDF** (see VOR page).

## Findings

### Outcomes and mechanisms

- **Mechanical:** **ultimate strength**, **yield**, and **Young’s modulus** vs **lithiation** show **nonlinear strengthening** with **Li** content in the **a-Li\(_x\)S** models (same narrative as the VOR page).
- **Transport:** **Li** and **S** **diffusivities** vary with **Li** loading, linking **diffusion** to cathode rate limitations in the abstract framing.
- **Voltage / phase space:** **GCMC**-derived **OCV** trends and a compiled **binary phase diagram** contextualize **discharge** thermodynamics alongside the **MD** structural results.

### Comparisons

This **proof** ingest is the **same DOI** as **`[[2014islam-physical-che-reaxff-molecular]]`**; **numerical** comparisons to experiment or alternate models should be taken from the **version-of-record** **PDF** figures/tables, not inferred from **proof** typography.

### Sensitivity

**Li loading** is the central composition knob in the **abstract** narrative for **mechanics** and **transport**; **temperature** dependence and other sweeps—**N/A — not summarized on this duplicate-ingest page** (VOR article).

### Limitations and outlook

**Proof** PDFs can differ in **pagination** and minor **typesetting**; prefer the **VOR** page for scholarly citation strings and final figure labels.

### Corpus honesty

Quantitative **moduli**, **diffusivities**, and **OCV** values should be quoted from **`papers/Islam_PCCP_LiS_2014.pdf`** via **`[[2014islam-physical-che-reaxff-molecular]]`**; this **`papers/Islam_PCCP_LiS_proof.pdf`** slug exists for **manifest** provenance and **hash** tracking.

## Limitations

This **proof** PDF is useful for **provenance** in the corpus; **pagination**, **figures**, and **editorial fixes** follow the **final PCCP** issue. Prefer **`[[2014islam-physical-che-reaxff-molecular]]`** for primary curation and stable **figure** references.

## Relevance to group

Duplicate proof bundle for the **Li–S ReaxFF** parameterization paper co-led by **van Duin**.

## Citations and evidence anchors

- DOI **10.1039/c4cp04532g** — same as **`[[2014islam-physical-che-reaxff-molecular]]`**.
- Proof path: `papers/Islam_PCCP_LiS_proof.pdf`; VOR path: `papers/Islam_PCCP_LiS_2014.pdf`.

## Related topics

- [[2014islam-physical-che-reaxff-molecular]]
- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]

## Reader notes (navigation)

For **battery** **MAS** retrieval, prefer **`[[2014islam-physical-che-reaxff-molecular]]`** for **OCV** curves and **phase** **diagram** **figures**; keep this **proof** slug for **PDF** **hash** provenance and **bibliographic** checks against the **PCCP** **issue** PDF. **Diffusivity** **numbers** and **mechanical** **modulus** **trends** should be quoted from the **final** **PDF** tables to avoid **proof**-specific **typography** errors. **GA** **phase** **diagram** **construction** details and **GCMC** **electrode** **potentials** are part of the **published** **methods** and should not be reconstructed from this wiki page alone.
