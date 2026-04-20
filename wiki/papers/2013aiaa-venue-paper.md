---
id: paper:2013aiaa-venue-paper
type: paper
title: "Molecular dynamics studies of thermal accommodation on carbon structures"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:carbon-hydrocarbon, material:graphene-carbon-nano, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: ""
year: 2013
authors: ["Mehta, Neil", "Levin, Deborah A.", "van Duin, Adri C. T."]
venue: "AIAA conference abstract / manuscript"
pdf_sha256: "9376825fba2c4db26837f13007552b05f281f87e03df6b0cb7d61f07c64923f8"
pdf_path: "papers/AIAA_Abstract_NeillMehta.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2013aiaa-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This manuscript (AIAA-associated) models **thermal accommodation** of a **nitrogen** gas environment with a **graphene** surface as a stand-in for high-temperature gas interactions relevant to **spore thermal inactivation** modeling. **ReaxFF MD** is used for **gas–surface collisions**, and a **thermal accommodation coefficient** is estimated from simulation (Baule theory is introduced as a classical reference with closed-form limits). The excerpt details **NVE vs NVT** ensembles and a **Berendsen thermostat** formulation for temperature control in broader MD context.

## Methods

- **ReaxFF molecular dynamics** for **N₂–graphene** collisions; energy accounting for accommodation coefficient definitions (per Section II outline).

## Findings

- Provides a framework linking MD collision outcomes to **accommodation coefficient** concepts; numeric results are not fully contained in the pages 1–2 extract.

## Limitations

- Extraction **partial**; conference/abstract PDF may omit peer-review context. No DOI in normalized metadata.

## Relevance to group

Demonstrates **ReaxFF** for **non-reactive-to-reactive gas–surface energy transfer** problems adjacent to aerospace thermal environments.

## Citations and evidence anchors

- Sections I–II: problem statement, Baule expressions, MD ensemble overview (PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
