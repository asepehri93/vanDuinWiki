---
id: paper:2015verners-corrosion-sc-comparative-molecular-3
type: paper
title: "Comparative molecular dynamics study of fcc-Al hydrogen embrittlement (author proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:aluminum
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.corsci.2015.05.008"
year: 2015
authors:
  - "Osvalds Verners"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
venue: "Corrosion Science (Uncorrected Proof)"
pdf_sha256: "422a1d3bf29890a4fe5c7e038f8130daeefca00b627c79921ddf2de010fafcad"
pdf_path: "papers/Verners_AlH_CorrosionScience_2015_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015verners-corrosion-sc-comparative-molecular-3 -->

## Evidence and attribution

!!! note "Authority of statements"

    This **proof** PDF begins with **Elsevier author-query** boilerplate; **highlights** and **article** text follow. Scientific content matches [[2015verners-corrosion-sc-comparative-molecular]] (**DOI** `10.1016/j.corsci.2015.05.008`). The opening query sheet asks authors to confirm names, corresponding-author fax, **ReaxFF** keyword compliance with the journal list, sponsor formatting, duplicate references (noting **[40, 45]** merged and renumbered), and figure color policy (**Figs. 4–6, 13** print B/W, web color).

## Summary

This corpus file is an **uncorrected proof** of the **Corrosion Science** article on **fcc-Al hydrogen embrittlement** studied with **ReaxFF molecular dynamics** (same DOI as the **version-of-record** PDF tracked under [[2015verners-corrosion-sc-comparative-molecular]]). The proof begins with Elsevier’s **AUTHOR QUERY FORM** (article **CS 6295**) before the **Article in Press** manuscript pages. The **Highlights** block states that **bulk-distributed hydrogen** favors **brittle intergranular** fracture motifs; **vacancy-distributed hydrogen** favors **void-assisted**, locally **plastic** fracture; **H-containing** systems show **reduced failure strain** and **tensile toughness**; **finite temperature** and **strain-rate** effects are tied to **structural relaxation**; and **hydrogen diffusivity** depends on **microstructure** evolution during **plastic** deformation. For the full scientific narrative—**slab** construction, **H** loading schemes, **ReaxFF** training context, and discussion of **dislocations**, **voids**, and **interface** response—the curated **published-PDF** page should be treated as primary.

## Methods

This **uncorrected proof** PDF matches the **LAMMPS/ReaxFF** protocol on **`[[2015verners-corrosion-sc-comparative-molecular]]`**: a **3D periodic supercell** of oxidized notched **fcc Al**, **162 H** in vacancy-paired vs random-bulk arrangements, **573 K**, **0.2 fs**, **NPT** tensile cycling with fixed tensile axis and **0 Pa** lateral stress via **Nosé–Hoover** thermostat (**100 fs**) and barostat (**10,000 fs** damping), **0.25%/0.5 ps** strain steps and **2.5 ps** relaxations. **Force-field training:** **VASP PBE**-augmented **Al/H** data merged into published **Al/O/H** ReaxFF subsets as on the canonical page. **Static QM:** same bulk reference calculations tabulated with ReaxFF in the VOR article.

## Findings

The proof **Highlights** state that **bulk-distributed H** and **vacancy-distributed H** favor different fracture motifs, that **H** reduces **failure strain** and **tensile toughness**, and that **finite temperature** and **strain rate** couple to structural relaxation during plastic flow while **H diffusivity** depends on evolving microstructure. Full mechanistic narrative, figures, and quantitative stress–strain data should be read from **`[[2015verners-corrosion-sc-comparative-molecular]]`** and `papers/Verners_AlH_CorrosionScience_2015.pdf`, not from this proof alone.

## Limitations

**Proof**/**query** PDFs are **not** preferred for **bibliography** or figure reproduction—use the **published Corrosion Science** issue when available. Keyword and reference renumbering called out in the query form may differ from earlier manuscript versions.

## Relevance to group

Duplicate **workflow** artifact for the **Al/H** **ReaxFF** **Corrosion Science** study; retained so clones that only hold the proof file still resolve **manifest** provenance.

## Citations and evidence anchors

- **DOI:** `10.1016/j.corsci.2015.05.008` — proof PDF: `papers/Verners_AlH_CorrosionScience_2015_proof.pdf`; primary article PDF: `papers/Verners_AlH_CorrosionScience_2015.pdf` ([[2015verners-corrosion-sc-comparative-molecular]]).

## Related topics

- [[2015verners-corrosion-sc-comparative-molecular]]
- [[reaxff-family]]

## Reader notes (navigation)

Canonical curated body: **`2015verners-corrosion-sc-comparative-molecular`**.
