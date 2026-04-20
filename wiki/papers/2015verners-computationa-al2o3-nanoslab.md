---
id: paper:2015verners-computationa-al2o3-nanoslab
type: paper
title: "α-Al2O3 nanoslab fracture and fatigue behavior"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - material:oxide
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2015.02.048"
year: 2015
authors:
  - "Osvalds Verners"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
venue: "Comput. Mater. Sci."
pdf_sha256: "b19713853cce68af6cd13b9dfa8dfa6542b795cf3c0f0e20f0f94a8bc1c7ce12"
pdf_path: "papers/Verners_CompMatSci_2015.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2015verners-computationa-al2o3-nanoslab -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

**Reactive MD (ReaxFF)** and complementary **ionic relaxation** workflows are applied to **single-crystalline α-Al2O3 nanoslabs** under **monotonic and cyclic** mechanical loading, comparing **finite-temperature dynamic** failure with **incremental static** pathways. The study emphasizes how **strain rate**, **lateral pre-strain**, and **size effects** change **failure strains**, **crack healing vs. branching**, and **amorphization** ahead of cracks, with selected comparisons to **DFT** for bulk-like responses. Conclusions are framed around **low-cycle fatigue** scenarios where **shakedown-like** elastic responses can emerge after repeated loading.

## Methods

- **ReaxFF MD** for nanoslab fracture under **finite temperature** and **strain-rate** variation.
- **Static relaxation** branches for incremental loading benchmarks.
- **Unit-cell / bulk simulations** to interpret **defect healing** and **phase-change-like** amorphous bands.

## Findings

- **Dynamic loading** lowers failure strains relative to **pure static** relaxation in the comparisons reported.
- **Positive pre-strain** increases **stress triaxiality**, favoring **sharp single-crack** propagation and reducing **healing** likelihood; **volume pre-relaxation** can promote **branching / amorphous bands** that facilitate **healing** and **elastic shakedown**.
- **Amorphization** ahead of cracks is interpreted as a **low-barrier, partially reversible** transformation contributing to **small-strain plasticity**.

## Limitations

- **Nanoscale slabs** omit **grain boundaries** and **environmental chemistry** (humidity) present in engineering alumina.
- **ReaxFF** alumina mechanics must stay tied to the **parameterization’s QM training envelope**.

## Relevance to group

Joint **Penn State** effort on **ReaxFF for ceramic fracture and fatigue**, connecting reactive FF capabilities to **mechanical reliability** questions.

## Citations and evidence anchors

- Abstract and article metadata in `papers/Verners_CompMatSci_2015.pdf`; **DOI:** `10.1016/j.commatsci.2015.02.048`.

## Related topics

- [[reaxff-family]]
