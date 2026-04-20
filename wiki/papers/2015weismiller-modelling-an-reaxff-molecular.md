---
id: paper:2015weismiller-modelling-an-reaxff-molecular
type: paper
title: "ReaxFF molecular dynamics simulations of intermediate species in dicyanamide anion and nitric acid hypergolic combustion"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1088/0965-0393/23/7/074007"
year: 2015
authors:
  - "Michael R. Weismiller"
  - "Adri C. T. van Duin"
venue: "Modelling Simul. Mater. Eng. Sci."
pdf_sha256: "89b92dfd300d2dd0ee3824ef710f01eefbad00a8630b7629024c531a9976096c"
pdf_path: "papers/Weismiller_DCA_MSME_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015weismiller-modelling-an-reaxff-molecular -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF MD** is used to interrogate **hypergolic ignition chemistry** between **dicyanamide (DCA−)** and **nitric acid**, focusing on **transient intermediates** and **reaction networks** that couple **proton transfer**, **NOx formation**, and **carbon/nitrogen-rich fragments** at high temperature/density conditions relevant to **ionic-liquid propellants**. The study situates simulation snapshots within the broader literature on **hypergolic pairings** where **atomistic detail** is difficult to obtain experimentally.

## Methods

- **Reactive MD** with an established **CHO/N ReaxFF** parameterization (as cited in the article) under **elevated-temperature** condensed-phase-like initial geometries described in the paper.

## Findings

- The article traces **time-resolved populations** of key **intermediate species** linking **acid–base chemistry** to **oxidizer-rich decomposition** channels (consult PDF figures for quantitative timelines).
- **Mechanistic narratives** emphasize how **ReaxFF** captures **bond rearrangements** absent in fixed-bond combustion models.


## Limitations

- **Ignition** is sensitive to **initial mixing morphology** and **quantum effects** not included in classical ReaxFF.
- **Quantitative barrier heights** should be spot-checked with **QM** along select reaction coordinates.

## Relevance to group

Shows the group’s **ReaxFF portfolio in reactive propellant chemistry**, adjacent to **combustion and safety** modeling use cases.

## Citations and evidence anchors

- Title/author block and abstract in `papers/Weismiller_DCA_MSME_2015.pdf`; **DOI:** `10.1088/0965-0393/23/7/074007`.

## Related topics

- [[reaxff-family]]
