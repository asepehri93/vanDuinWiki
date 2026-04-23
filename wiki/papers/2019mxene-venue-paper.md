---
id: paper:2019mxene-venue-paper
type: paper
title: "Molecular Dynamics Simulations of MXenes: Ab Initio, Reactive, and Non-reactive Empirical Force Fields"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:2d-materials
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: ""
year: 2019
authors:
  - "Roghayyeh Lotfi"
  - "Dundar E. Yilmaz"
  - "Lukas Vlcek"
  - "Adri C. T. van Duin"
venue: "2D Metal Carbides and Nitrides (MXenes) (Springer)"
pdf_sha256: "f03d72d6805cf78e91c3a5d6aefd6fe005113f74fc40c0ee1419b9f3103db4b2"
pdf_path: "papers/MXene_Chapter_Yilmaz_Lotfi_Vlcek_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019mxene-venue-paper -->

## Summary

This wiki entry tracks a **Springer** book-chapter **proof** PDF (`papers/MXene_Chapter_Yilmaz_Lotfi_Vlcek_proof.pdf`) for a survey chapter co-authored by **Adri C. T. van Duin** on molecular dynamics of **MXenes** (two-dimensional **metal carbides/nitrides**). The chapter summarizes how **ab initio molecular dynamics**, **ReaxFF reactive molecular dynamics**, and **non-reactive empirical** force fields have been deployed across **energy storage**, **adsorption and intercalation**, **catalysis**, **exfoliation**, and **photocatalytic water splitting**-related contexts. The proof filename implies **pre-publication** layout; for final pagination and publisher metadata, prefer the released chapter bundle or the duplicate ingest **`[[2019chapter9-venue-paper]]`** / **`[[2019chapter9-venue-paper-2]]`** when DOI-linked.

## Methods

The chapter is organized as a **methods review**: it classifies when **AIMD** is necessary (short times, barrier-sensitive chemistry, validation of local coordination), when **ReaxFF** is appropriate (bond formation/cleavage in solvents, intercalants, and tribological contacts), and when **fixed-bond classical** models are the pragmatic choice (large supercells, slow charging dynamics, or problems dominated by electrostatics and packing rather than bond rearrangement). Representative studies cited in the PDF provide worked examples of each tier; readers should use the chapter bibliography for authoritative references.

## Findings

Across the surveyed literature, **non-reactive MD** trades chemical explicitness for throughput on large MXene stacks and **electrochemical double-layer** setups where the MXene backbone remains topologically fixed. **ReaxFF** is positioned where **explicit chemistry** matters for **intercalation pathways**, **water** transport and reaction, and **tribological** response. **AIMD** supplies validation data and stability windows that constrain lower-cost models. These role divisions are complementary rather than competitive: practical workflows often cascade from AIMD benchmarks to ReaxFF production runs to classical scaling.

**Comparisons** in the review sense are between **model tiers** (AIMD vs ReaxFF vs fixed-bond) rather than a single “best” potential: the chapter’s **literature** **comparisons** are only as strong as the **cited** application papers, and **experimental** agreement is **not** claimed at the chapter level without those primary sources. **Sensitivity** to **temperature**, **intercalant concentration**, **electrode** **electrostatics**, and **MXene** **termination** (–O, –F, –OH) enters through the **cited** **case** **studies**; readers should not extrapolate a **universal** **protocol** from the **schematic** **workflow** **advice** alone. **Limitations** of a **proof**-stage **PDF** for **locators** and **final** **wording** are **not** **intrinsic** **to** the **science** but **do** **affect** how **this** **wiki** **page** can be **cited** **as** a **bibliography**—prefer **`[[2019chapter9-venue-paper]]`** for **version-of-record** **chapter** **text** when available. **Corpus** **honesty:** this **entry** is a **provenance** **pointer** to a **group** **survey** **chapter**; it **does** **not** **independently** **reproduce** every **cited** **MD** **table** **in**-**wiki** **form**. **Comparisons** in the **chapter** **bibliography** should be **treated** as **(i)** **capability** **vs** **cost** **and** **(ii)** **bond**-**making** **need** **,** not **as** a **universal** **ranking**; **see** the **cited** **primary** **papers** **per** **application** **(MXene** **termination** **and** **stoichiometry** **vary** **by** **synthesis**). **Version-of-record** **pagination** and **any** **chapter** **DOI** **should** be **taken** from **the** **published** **Springer** **entry**—**this** **proof** **ingest** **may** **differ** **(corpus** **honesty**).

## Limitations

As a **proof** PDF, author queries and metadata lines may differ from the final Springer chapter; **`doi`** may be absent in front matter until harmonized with the publisher record—use **`[[2019chapter9-venue-paper]]`** for DOI-first navigation when available.

## Reproducibility notes

Chapter-level guidance should be translated into explicit simulation checklists: **intercalant concentration**, **electrode boundary conditions**, **water dissociation** handling, and **ReaxFF** parameter lineage (**Ti–C–O–H** subsets) must match the cited application papers. For MXene tribology or water exposure, prefer **ReaxFF** when bond breaking is plausible; otherwise document why a **fixed-bond** model is adequate.

When the chapter cites **LAMMPS** input fragments, treat them as **illustrative** unless explicitly validated for your stoichiometry: MXene compositions and terminations vary between synthesis routes, and mis-assigned **atom types** are a frequent source of silent error.

## Relevance to group

Group-authored survey connecting ReaxFF and broader MD ecosystem to MXene applications.

## Citations and evidence anchors

- Chapter DOI (duplicate-tracked): [10.1007/978-3-030-19026-2_9](https://doi.org/10.1007/978-3-030-19026-2_9) via **`[[2019chapter9-venue-paper]]`**.

## Related topics

- [[2019chapter9-venue-paper]]
- [[reaxff-family]]
