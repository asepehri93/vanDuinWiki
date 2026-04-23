---
id: paper:2013ijemcp1202-1-5739-venue-paper
type: paper
title: "Reactive force fields: Concepts of ReaxFF and applications to high-energy materials"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:reaxff-lineage, domain:organics-polymers-pyrolysis, method:reaxff, task:review, scale:atomistic]
candidate_tags: []
source_refs: []
doi: ""
year: 2013
authors: ["van Duin, Adri", "Verners, Osvalds", "Shin, Yun-Kyung"]
venue: "International Journal of Energetic Materials and Chemical Propulsion"
pdf_sha256: "5ab96e9b22843af8a4daba817fab7d2b01ae1c43bad47d75732d705518c14c0c"
pdf_path: "papers/IJEMCP1202(1)-5739.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013ijemcp1202-1-5739-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **review-style** chapter (*International Journal of Energetic Materials and Chemical Propulsion* **12(2)**, **95–118**, **2013**) introduces **reactive force fields** by contrasting **quantum mechanics (QM)** with **classical force fields (FFs)**. QM affords **high accuracy** on **small** systems (the text cites **roughly 100–1000 atoms** as typical accurate QM reach) but becomes prohibitive for **nanosecond dynamics** on **large** assemblies, whereas **nonreactive FFs** enable **large-scale MD** yet normally **cannot** describe **bond breaking and formation**. The authors explain how **bond order versus distance** relationships extend traditional FF concepts so that **connectivity can evolve** during dynamics, using **ReaxFF** as the exemplar line. The stated **keywords** emphasize **ReaxFF**, **molecular dynamics**, **nitramines**, and **metals**, and the abstract promises **applications to energetic materials** including **nitramines**, **binders**, and **metallic** high-energy compositions. The **introduction** sketches a **multiscale ladder**: QM on **~100 atoms** trains an FF that accelerates MD by **~10⁶**, reaching **~10⁹-atom** MD, with a further hop to **mesoscale** descriptions where each element may represent **hundreds–thousands** of atoms toward **10¹²** particles—framing materials design workflows that bridge scales.

## Methods

This **review-style** chapter (*Int. J. Energetic Materials and Chemical Propulsion* **12(2)**, **95–118**, **2013**; **`papers/IJEMCP1202(1)-5739.pdf`**) is **didactic** rather than a single numerical **MD** benchmark paper. On the indexed **`normalized/extracts/2013ijemcp1202-1-5739-venue-paper_p1-2.txt`** pages, the authors contrast **QM** with classical **FFs**, introduce **bond-order**-based reactive formulations (**ReaxFF** as the exemplar), and outline how **EEM-like** charges and **vdW/Coulomb** terms enter reactive Hamiltonians. They also discuss **transferability** across **covalent**, **metallic**, and **ionic** regimes—still at the **conceptual** level on the excerpt.

**Literature scope & comparison protocol (review):** Later sections (not captured in the checked-in **p1–2** extract) reportedly cover **nitramine**, **binder**, and **metallic** energetic examples with their own simulation tables. This wiki does **not** paste those tables: treat every concrete **LAMMPS** **timestep** (**fs**), **NVT**/**NPT** choice, **PBC** **supercell** **atom** counts, **Berendsen**/**Nosé–Hoover** **thermostat** settings, **barostat**/**pressure** targets, **temperature** ramps, **electric field** cases, and **replica**/**enhanced sampling** recipes as **chapter-specific** facts that must be copied from the **full PDF** when needed, not inferred here.

## Findings

The **opening sections** position **ReaxFF** as a bridge between **QM** accuracy on **~100–1000 atoms** and **molecular dynamics** reach on far larger **reactive** systems, emphasizing **bond topology updates** during **decomposition**/**deflagration**-class chemistry relevant to **energetic materials** R&D. The abstract/**Sec. 1** preview **applications** to **nitramines**, **binders**, and **metals**, but those **case studies** are not summarized numerically on this page.

**Comparisons & sensitivity (review-level):** The text argues that **temperature**, **density**, and **composition** levers change how severely **bond-breaking** cascades occur in formulated **energetics**—quantitative trends live in later **PDF** sections. **Limitations & outlook:** The chapter stresses **force-field** **limitations** and the need to validate each **application** against **experiment** or targeted **QM**. **Corpus honesty:** With only **`p1–2`** text under `normalized/extracts/`, this entry cannot quote later **nitramine** benchmarks; reopen **`papers/IJEMCP1202(1)-5739.pdf`** for **version-of-record** details and any **DOI** once registered in metadata.

## Limitations

**Extraction_quality** is **partial** (`normalized/extracts/2013ijemcp1202-1-5739-venue-paper_p1-2.txt` covers **title page and Sec. 1** only). **DOI** is absent in front matter—use **journal bibliographic data** (volume/issue/pages above) for citation until a DOI is registered in metadata.

## Relevance to group

A **didactic** counterpart to primary research papers—useful for teaching and for linking **energetics** workflows.

## Citations and evidence anchors

- Title page and Sec. 1 (Int. J. Energetic Materials and Chemical Propulsion 12(2) 95–118 (2013); PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
