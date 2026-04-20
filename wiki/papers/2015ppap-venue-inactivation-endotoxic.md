---
id: paper:2015ppap-venue-inactivation-endotoxic
type: paper
title: "Inactivation of the endotoxic biomolecule lipid A by oxygen plasma species: a reactive molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:reactive-md
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1002/ppap.201400064"
year: 2015
authors:
  - "Maksudbek Yusupov"
  - "Erik C. Neyts"
  - "Christof C. Verlackt"
  - "Umedjon Khalilov"
  - "Adri C. T. van Duin"
  - "Annemie Bogaerts"
venue: "Plasma Processes and Polymers 2015, 12, 162–171"
pdf_sha256: "f0e09561531dd7a348592a5469855314c62f4062b0e79705004477cfecbdef59"
pdf_path: "papers/PPaP_2015_Yusupov-Lipid A.PDF"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015ppap-venue-inactivation-endotoxic -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Yusupov *et al.* perform **ReaxFF reactive MD** to study impacts of **oxygen plasma-derived species** (**OH**, **HO\(_2\)**, **H\(_2\)O\(_2\)**) on **lipid A**, the endotoxic anchor of *E. coli* lipopolysaccharide. The abstract claims these species can **destroy lipid A** and thereby **reduce toxic activity**, with **distinct bond-breaking mechanisms** for **HO\(_2\)**/**H\(_2\)O\(_2\)** versus **OH** impacts, and states qualitative agreement with experimental observations cited in the introduction framing. The introduction surveys **cold atmospheric plasma (CAP)** sterilization motivations and summarizes prior experimental work on **LPS/lipid A** modifications by plasma-generated **radicals** and **VUV**.

## Methods

- **Reactive MD** with **ReaxFF** for ROS–biomolecule collisions/reactions (protocol details in full paper).
- Comparison narrative anchored to experimental **XPS**/**activity** studies referenced in the introduction.

<!-- enrich-from-extract:v2 -->

- Reactive molecular dynamics simulations are performed to study the interaction of reactive oxygen species, such as OH, HO2 and H2O2, with the endotoxic biomolecule lipid A of the gram- negative bacterium Escherichia coli .
- A clear difference is observed in the bond breaking mechanisms upon impact of HO 2 radicals and H 2O2 molecules on one hand and OH radicals on the other hand.


## Findings

- Mechanistic differentiation between **radical classes** is a headline result in the abstract-level summary.
- Contextualizes plasma medicine motivation: **nonthermal** plasmas for **heat-sensitive** materials.

### Additional results (article abstract)

- It is found that the aforementioned plasma species can destroy the lipid A, which consequently results in reducing its toxic activity.
- Our simulation results are in good agreement with experimental observations.


## Limitations

- Biological complexity (membrane context, hydration, salts) is reduced to **atomistic** models; extrapolation to clinical sterilization requires multiscale validation.
- Extract is early pages; quantitative damage metrics appear later.

## Relevance to group

**Adri C. T. van Duin** co-authorship connects the work to **ReaxFF** extensions toward **plasma–biomolecule** interactions pursued with Antwerp **PLASMANT** collaborators.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1002/ppap.201400064](https://doi.org/10.1002/ppap.201400064)

## Related topics

- [[reaxff-family]]
