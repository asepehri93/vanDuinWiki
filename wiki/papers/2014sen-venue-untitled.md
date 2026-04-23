---
id: paper:2014sen-venue-untitled
type: paper
title: "Oxidation-assisted ductility in aluminium nanowires (Nature Communications proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - scale:atomistic
source_refs: []
doi: "10.1038/ncomms4959"
year: 2014
authors:
  - "Fatih G. Sen"
  - "Ahmet T. Alpas"
  - "Adri C.T. van Duin"
  - "Yue Qi"
venue: "Nature Communications (proof PDF; same DOI as published article)"
pdf_sha256: "8200699412a1f23215d94cf35dc1ac590214ca110c45b23aae50f5d57065c892"
pdf_path: "papers/Sen_Nature_Comm_2014_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014sen-venue-untitled -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This corpus entry points at an **author proof PDF** for the same **Nature Communications** study as **`[[2014sen-nat-oxidation-assisted-ductility]]`** (DOI **10.1038/ncomms4959**). The scientific content matches the published narrative: **ReaxFF** reactive MD on **oxidized aluminium nanowires** under **tensile** loading, addressing how a **thin amorphous oxide shell** couples to **plasticity** in the **metallic core**. The work argues for **oxidation-assisted ductility** relative to bare **Al**, with mechanisms tied to **dislocation nucleation** statistics in the core and **time-dependent** **oxygen** transport that can **heal** **Al–O** bond rupture in the shell when **strain rate** and **oxidation rate** remain in a compatible regime—motivated by **TEM**-informed **core–shell** morphologies from **hot-formed** debris. Maintainer mapping of **proof vs VOR** PDFs: [NON_PRIMARY_ARTICLE_PAPER_SLUGS.md](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Methods

This slug’s **proof** PDF duplicates **`[[2014sen-nat-oxidation-assisted-ductility]]`** (DOI **10.1038/ncomms4959**); Methods mirror the published article—use the **version-of-record** PDF for pagination.

### Reactive MD (Al/O ReaxFF)

- **ReaxFF** simulations model **oxidized** **Al** **nanowires** under **tensile** loading in **vacuum** versus **oxygen**-containing environments, capturing **bond rearrangement** and **oxygen transport** in an **amorphous oxide shell** around a **metallic core** (**Summary**).

### Structural inspiration from experiment

- **Core–shell** morphologies are motivated by **TEM** observations of **nanowire debris** from **hot forming** (**Summary**).

### Timescale / rate scaling

- **Oxidation** is **accelerated** relative to laboratory conditions to fit **MD** accessible times; the article discusses how **oxidation rate** vs **mechanical strain rate** are scaled to preserve **physically meaningful competition** (**Summary**).

### Numerical settings

- **Timestep, thermostat, system sizes:** follow **Nat. Commun.** Methods/SI—not duplicated on this proof-oriented wiki page.

### 1 — MD application (proof PDF; same article as VOR)

**ReaxFF** **reactive molecular dynamics** duplicates the protocol narrative on **`[[2014sen-nat-oxidation-assisted-ductility]]`**. **Engine, atom counts, PBC, timestep (fs), thermostat, ns-scale equilibration/production, barostat:** **N/A —** not retyped from **`papers/Sen_Nature_Comm_2014_proof.pdf`** on this manifest-only page—use the **version-of-record** sibling for integrated Methods text. **Ensemble:** **NVT** staging is typical for the cited **ReaxFF** tensile/oxidation workflow but **N/A —** confirm per-stage labels in the **published** PDF. **Pressure / stress:** **stress–strain** metrics appear in the article; **hydrostatic pressure** servo details — **N/A —** confirm in **`pdf_path`**. **Electric field / enhanced sampling:** **N/A —** not used in the summarized protocol class.

## Findings

The study reports **oxidation-assisted** **ductility** for **oxidized** **Al** **nanowires** versus expectations for more **brittle** oxide-covered metals in some regimes. **Nucleation** of **plasticity** shifts to **lower** **flow stress** when **oxide** chemistry provides **additional** **defect** sources and **activation** volumes differ from bulk **Al**. **Oxide** **shell** behavior can become **superplastic-like** when **oxygen** **diffusion** **repairs** **bond** breaking during **deformation** below a **critical** **strain rate**, whereas faster straining can outpace **healing** and change the **failure** mode. These trends are summarized from the **published** abstract and main text; prefer the **VOR** PDF for **pagination** and **figure** numbering.

## Limitations

- This file is tied to a **proof** PDF; typography and some text fragments in the extract differ slightly from the final **Nature Communications** layout.
- Page-level anchoring and any proof-specific queries should be checked against the **version-of-record PDF** where possible; canonical sibling wiki page: **`[[2014sen-nat-oxidation-assisted-ductility]]`**.

## Relevance to group

Duplicate source variant for the same scientific contribution; useful for **provenance tracking** when the proof PDF is the file present on disk.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1038/ncomms4959](https://doi.org/10.1038/ncomms4959)

## Related topics

- [[reaxff-family]]
