---
id: paper:2013joshi-venue-research
type: paper
title: "Connectivity-based parallel replica dynamics for chemically reactive systems: From femtoseconds to microseconds"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:organics-polymers-pyrolysis, domain:methods-software, method:reaxff, task:method-development, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1021/jz4019223"
year: 2013
authors: ["Joshi, Kaushik L.", "Raman, Sumathy", "van Duin, Adri C. T."]
venue: "The Journal of Physical Chemistry Letters"
pdf_sha256: "548b25f15a12b90ad445d0e0d8dae0e61bd822f87e64e58e5167fa603ff88689"
pdf_path: "papers/Joshi_PRD_JPC_Letter_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013joshi-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The paper introduces **Reactive Parallel Replica Dynamics (RPRD)**: a **connectivity-change** event detector for **ReaxFF** simulations that enables **parallel replica** acceleration of rare reactive events, pushing accessible times toward **microseconds**. **1-heptene pyrolysis** is used as a benchmark at temperatures as low as **1350 K** for up to **1 μs** with **40 heptene molecules**. The abstract reports **reasonable agreement** between the **RPRD product distribution/mechanism** and **shock tube experiments**, and positions the approach as addressing the timescale gap of standard RMD.

## Methods

- **PRD** adapted to **reactive** systems by defining transitions via **bond connectivity** changes (vs prior nonreactive PRD literature surveyed).
- **ReaxFF** integration within an accelerated MD framework; discussion of why naive high-temperature sampling distorts branching ratios.

## Findings

- Demonstrates **long-time reactive trajectories** for a hydrocarbon pyrolysis case with experimental comparators mentioned.

## Limitations

- Acceleration assumptions (first-order escape kinetics, event detection correctness) must be validated per system.

## Relevance to group

Methodological bridge between **ReaxFF chemistry** and **rare-event sampling**—important for pyrolysis/combustion and other activated processes.

## Citations and evidence anchors

- Abstract and introduction: RPRD definition, 1-heptene case, PRD background (J. Phys. Chem. Lett. 2013, 4, 3792–3797; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
