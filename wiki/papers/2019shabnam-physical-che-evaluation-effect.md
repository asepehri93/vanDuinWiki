---
id: paper:2019shabnam-physical-che-evaluation-effect
type: paper
title: "Evaluation of the effect of nickel clusters on the formation of incipient soot particles from polycyclic aromatic hydrocarbons via ReaxFF molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:catalysis-surfaces
  - domain:reactive-md
  - method:reaxff
  - material:metal-surface
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1039/C9CP00354A"
year: 2019
authors:
  - "Sharmin Shabnam"
  - "Qian Mao"
  - "Adri C. T. van Duin"
  - "K. H. Luo"
venue: "Phys. Chem. Chem. Phys. 21:9865-9875 (2019)"
pdf_sha256: "7329f8a1300deec0579b23731e09b8e154eb42f162a25d3d1dbf5dd3587c7b78"
pdf_path: "papers/Shabnam_PCCP_Ni_soot_2019.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019shabnam-physical-che-evaluation-effect -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

ReaxFF NVT simulations probe how a Ni13 cluster promotes growth of nascent soot from PAH monomers (naphthalene through circumcoronene) from 400–2500 K. At low temperature, PAHs stack and bind around Ni, forming larger clusters earlier than in homogeneous systems. Between roughly 1200–1600 K chemisorption on Ni appears; near 2000 K “chemical nucleation” produces stable soot-like growth facilitated by Ni-assisted dehydrogenation. At 2500 K Ni accelerates ring-opening and fullerene-like soot growth versus Ni-free runs.

## Methods

ReaxFF molecular dynamics; single Ni13 cluster + one PAH species per study; broad temperature sweep.

## Findings

Metal cluster clearly alters nucleation and growth pathways across the temperature ladder; homogeneous vs Ni-catalyzed regimes are distinguished in the abstract’s qualitative mechanisms.

## Limitations

Cluster size and metal identity are fixed; gas-phase equivalence to flame chemistry is approximate. ReaxFF uncertainty for organometallic Ni–C edge cases should be kept in mind.

## Relevance to group

Penn State–led study coupling catalytic metals to PAH/soot chemistry using ReaxFF, aligned with fuels and emissions research threads.

## Citations and evidence anchors

`papers/Shabnam_PCCP_Ni_soot_2019.pdf` — abstract (temperature stages, Ni13, PAH list). https://doi.org/10.1039/C9CP00354A

## Related topics

- [[reaxff-family]]
