---
id: paper:2017ostadhossein-venue-microsoft-word-3
type: paper
title: "Supporting information (part III): ReaxFF training-set weights and geometries (trainset.in style)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - task:parameterization
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: ""
year: 2017
authors: []
venue: "Supporting information (ACS Publications)"
pdf_sha256: "452dbf3bb65152b56dfff228e08852598fdf9bd65278ecda6bdb3a58dc02afa7"
pdf_path: "papers/Ostadhossein_MoS2_JPC_Letters_2017_SI_III.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017ostadhossein-venue-microsoft-word-3 -->

!!! abstract
Machine-readable ReaxFF training blocks in a `trainset.in`-style layout for Mo–S–H clusters and reactions used in the MoS₂ edge chemistry parametrization described in the parent *J. Phys. Chem. Lett.* article (DOI `10.1021/acs.jpclett.6b02902`).

## Summary

This corpus PDF is **Supporting Information III** for the MoS₂ ReaxFF work by Ostadhossein et al. It does not read as a standalone article; it supplies **weighted training data** for least-squares ReaxFF optimization in a format that lists **CHARGE**, **GEOMETRY**, and **ENERGY** sections. The extract shows **atomic charges** for small species (for example H₂S-like fragments), extensive **bond and angle** targets with per-observable **weights** for Mo–S–H stoichiometries such as **MoS₆**, **MoS₄H₂**, **MoS₃H₂**, **MoS₄H₄**, **Mo₂S₆**, and related fragments, and **linear-combination reaction energies** tying relative stabilities of hydrogenated sulfide and edge-like species together. The file’s role in the knowledge base is to preserve **reproducibility** of which observables and weights entered the fit, alongside human-readable tables in sibling SI files and the narrative validation on [[2017ostadhossein-venue-research]].

## Methods

**Force-field training / fitting.** **`trainset.in`-style** blocks list **CHARGE**, **GEOMETRY**, and **ENERGY** targets with **per-observable weights** for **Mo–S–H** clusters and **reaction-energy ladders** used in the **least-squares ReaxFF optimization** described on **`[[2017ostadhossein-venue-research]]`**.

**MD application (atomistic dynamics).** **N/A —** machine-readable **training listings** only.

**Static QM / DFT.** **QM** reference levels and **DFT** benchmarks for the same observables are given on **SI II** and in the **parent letter**.

**Review / non-simulation framing.** **Supporting Information Part III** (**non-primary**); use **`[[2017ostadhossein-venue-research]]`** for **scientific** narrative and **DOI** grounding.

## Findings

**Outcomes.** The **trainset** shows a **dense set of geometry constraints** (many bonds and angles per cluster) with weights often near **0.02** for looser motifs and up to **~2.5** for angles used to stiffen key **Mo-centered** scaffolding, plus **reaction-energy ladders** tying **dehydrogenation** and **sulfur rearrangement** among **MoS\(_x\)H\(_y\)** fragments.

**Comparisons.** These **weighted observables** are what the **optimizer** matches to **QM** references documented on **SI II** and the **parent letter**—not to **experiment** directly in this raw listing.

**Sensitivity / design levers.** The **relative weights** reveal which **charge**, **angle**, and **reaction-energy** classes dominated the **2017** objective function for this parametrization.

**Limitations / outlook.** **Edge catalysis**, **growth kinetics**, and **agreement with experiment** are reported only on **`[[2017ostadhossein-venue-research]]`**; this PDF is a **fitting artifact** archive.

**Corpus honesty.** **SI-only**; **no DOI** in front matter—link **`[[2017ostadhossein-venue-research]]`** for bibliography.

## Limitations

This entry is **SI-only** (see [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) policy for SI packages). It lacks narrative Methods and Results, and **no DOI** is registered in front matter for the SI file itself. Operators must **not** cite this PDF as if it were peer-reviewed prose. Numerical weights are **fitting artifacts**; downstream users need the **final ReaxFF** and **QM benchmarks** from the parent work.

**Confidence rationale:** `med` because the page is complete for its corpus role but the canonical scientific story lives on the primary article page.

## Reader notes (navigation)

- Parent letter and full context: [[2017ostadhossein-venue-research]]
- Related SI parts: [[2017ostadhossein-venue-microsoft-word-2]]
- Theme hub: [[theme-2d-epitaxy-growth]]
- [[reaxff-family]]
- Benchmarks: [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
