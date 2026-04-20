---
id: paper:2010quenneville-venue-paper
type: paper
title: "Reactive molecular dynamics studies of DMMP adsorption and reactivity on amorphous silica surfaces"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:oxides-ceramics, domain:catalysis-surfaces, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1021/jp104547u"
year: 2010
authors: ["Quenneville, Jason", "Taylor, Ramona S.", "van Duin, Adri C. T."]
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "92ec8b991cdbee2820af8f1e8aaf948a2e9f614fc9936571a2f8ea6b41cf4c78"
pdf_path: "papers/Quenneville_2010_JPC.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2010quenneville-venue-paper -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

The authors use **ReaxFF molecular dynamics** to study **dimethyl methylphosphonate (DMMP)** interacting with **amorphous silica** as a function of surface hydroxylation (reported modeled densities 2.0–4.5 OH/nm²). The introduction frames DMMP as a **nerve-agent simulant** relevant to environmental fate on silica-rich materials. Key qualitative results in the excerpt include: at higher OH coverage, binding involves **vdW + hydrogen bonding**; at lower coverages, **covalent** interaction between the phosphonyl oxygen and **3-coordinate Si defects**; at very low coverage, **fragmentation** is observed. A stated binding energy example is **−4.7 kcal/mol** at **4.5 OH/nm²**, and added water can **displace/hydrolyze** adsorbed DMMP. MP2/DFT cluster calculations are reported as supporting selected ReaxFF predictions.

## Methods

- **ReaxFF MD** on amorphous silica surfaces with varying hydroxyl density; structural characterization of the silica model compared to experiment (per text).
- **QM spot checks:** MP2 and DFT on small silica clusters to validate reactions suggested by MD.

## Findings

- Strong dependence of binding mode on OH density: from vdW/H-bonding dominance at high OH, to defect-mediated covalent attachment at lower OH, to fragmentation at the lowest studied OH density.
- Quantitative example binding energy (−4.7 kcal/mol) and qualitative solvent displacement chemistry with an added water layer.

## Limitations

- Extraction is **partial**; barrier heights, full product distributions, and sensitivity analysis may require the full article.
- Classical reactive FF uncertainty for organophosphate/surface chemistry should be tracked against QM benchmarks.

## Relevance to group

Demonstrates **ReaxFF + QM validation** for **oxide surface chemistry** with organics, a template for adsorption/reactivity studies on amorphous silica and related environmental interfaces.

## Citations and evidence anchors

- Abstract and introduction: DMMP/silica coverage effects, binding energy example, water displacement (J. Phys. Chem. C 2010; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
