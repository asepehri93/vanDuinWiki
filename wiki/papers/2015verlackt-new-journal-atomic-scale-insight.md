---
id: paper:2015verlackt-new-journal-atomic-scale-insight
type: paper
title: "Atomic-scale insight into the interactions between hydroxyl radicals and DNA in solution using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1088/1367-2630/17/10/103005"
year: 2015
authors:
  - "C. C. W. Verlackt"
  - "E. C. Neyts"
  - "T. Jacob"
  - "D. Fantauzzi"
  - "M. Golkaram"
  - "Y.-K. Shin"
  - "A. C. T. van Duin"
  - "A. Bogaerts"
venue: "New J. Phys."
pdf_sha256: "6ef38a20f390e494e1218c7d79b95f941e2597d3370307c9bfc207cc3351fb35"
pdf_path: "papers/Verlackt_njp_DNA_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015verlackt-new-journal-atomic-scale-insight -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Plasma-medicine-motivated reactive MD** with **ReaxFF** is used to follow **·OH attack on DNA** in explicit **aqueous solution**, focusing on **bond-making/breaking events** that are inaccessible to non-reactive force fields. The publication frames **reactive oxygen species (ROS)** chemistry at **atomistic resolution** and connects simulation observables to **plasma–liquid interface** contexts where hydroxyl radicals are abundant. Penn State contributors (**Shin, Golkaram, van Duin**) anchor the **ReaxFF methodology** side of an international collaboration led by **Antwerp**-based groups.

## Methods

- **ReaxFF molecular dynamics** of DNA fragments solvated with explicit water, with radical species introduced consistent with the article’s protocol sections.
- Validation and parameter scope are described relative to **QM benchmarks** in the original paper.

## Findings

- The work documents **radical-induced bond cleavage / modification pathways** on DNA building blocks and discusses mechanistic implications for **ROS damage** scenarios (see article body for specific reaction channels and statistics).

## Limitations

- **Force-field bias** in rare reaction channels; statistical sampling over **long biological times** remains approximate.
- **DNA sequence / secondary structure** dependence is only partially explored in any single study.

## Relevance to group

Demonstrates **ReaxFF deployment outside traditional materials catalysis**—here **soft matter + plasma chemistry**—with direct **van Duin group** authorship.

## Citations and evidence anchors

- Title page and abstract in `papers/Verlackt_njp_DNA_2015.pdf`; **DOI:** `10.1088/1367-2630/17/10/103005`.

## Related topics

- [[reaxff-family]]
