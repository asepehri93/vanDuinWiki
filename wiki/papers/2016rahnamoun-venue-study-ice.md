---
id: paper:2016rahnamoun-venue-study-ice
type: paper
title: "Study of ice cluster impacts on amorphous silica using the ReaxFF reactive force field molecular dynamics simulation method"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:silicate-glass
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4942997"
year: 2016
authors:
  - "A. Rahnamoun"
venue: "J. Appl. Phys."
pdf_sha256: "6d98de3d50f6099e3101f965173da0fc23186c21b93c454939a2cc113f1b7772"
pdf_path: "papers/Rahnamoun_JAP_2016.pdf"
extraction_quality: good
group_affiliation: false
---

<!-- id:paper:2016rahnamoun-venue-study-ice -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF MD** is used to simulate **high-velocity impacts of ice clusters** onto **amorphous silica** substrates, targeting **mechanochemical damage** and **hydrogen-bond-mediated contact mechanics** relevant to **icy-body impacts**, **cryogenic engineering**, or **tribological** scenarios involving **water ice + silica**. The publication analyzes **energy dissipation**, **substrate disruption**, and **reactive events** enabled by the **reactive force field** that would be invisible to **fixed-bond silica models**.

## Methods

- **Reactive MD (ReaxFF)** with **cluster impact** initial conditions (mass, velocity, and cluster construction as specified in the article).
- Post-processing of **local densification**, **bond-breaking**, and **ejecta** statistics.

## Findings

- The article documents how **ice cluster impacts** drive **non-trivial chemistry and mechanical modification** of **a-SiO2** in the simulated parameter ranges (see paper for threshold velocities and damage morphologies).

## Limitations

- **Classical reactive** treatment of **ice** and **proton disorder** omits **full nuclear quantum effects** unless separately augmented.
- **Cluster geometry / crystallinity** strongly affects outcomes.

## Relevance to group

Corpus **ReaxFF application** connecting **water/ice** chemistry with **silica mechanics**, useful alongside **Langmuir tribochemistry** and **geochemical interface** entries.

## Citations and evidence anchors

- Bibliographic metadata in `normalized/papers/2016rahnamoun-venue-study-ice.json` and abstract in `papers/Rahnamoun_JAP_2016.pdf`; **DOI:** `10.1063/1.4942997`.

## Related topics

- [[reaxff-family]]
