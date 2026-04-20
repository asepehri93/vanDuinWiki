---
id: paper:2013afif-venue-paper
type: paper
title: "A reactive force field for zirconium and hafnium di-boride"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:reaxff-lineage, domain:mechanics-tribology, method:reaxff, task:parameterization, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2012.12.038"
year: 2013
authors: ["Gouissema, Afif", "Fan, Wu", "van Duin, Adri C. T.", "Sharma, Pradeep"]
venue: "Computational Materials Science"
pdf_sha256: "59d399dccb15b4ae30ba5837c0941dd352c391e36fa86fb72de1a46c7cefe895"
pdf_path: "papers/Afif_CompMatSci_2013.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2013afif-venue-paper -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

The paper develops **ReaxFF potentials for ZrB₂ and HfB₂**, motivated by **ultra-high-temperature ceramic (UHTC)** applications (hypersonics, thermal protection). Parameters are fit to **QM** data on **clusters and crystal structures** (Quantumwise for periodic phases; Gaussian09 for **Zr(BH₂)₂ / Hf(BH₂)₂** PECs per excerpt). The ReaxFF energy expression is specialized (e.g., **torsions/conjugation** omitted in the reduced form shown) while retaining **bond order**, **over/under-coordination**, **vdW**, and **Coulomb** terms. The excerpt motivates future **oxidation, creep, grain boundary** modeling once reactive potentials exist.

## Methods

- **QM training sets** for geometries/energies/charges; **ReaxFF optimization**; outline of **MD validation** (Sec. 5 referenced).

## Findings

- States successful **parameter derivation** within ReaxFF for the boride systems per abstract; detailed numeric validation is beyond the partial extract.

## Limitations

- Extraction **partial**; full validation metrics and failure modes require the complete article.

## Relevance to group

Expands **ReaxFF** into **refractory boride** chemistry relevant to extreme-environment materials modeling.

## Citations and evidence anchors

- Title/abstract and Secs. 2–3 overview (Comput. Mater. Sci. 70 (2013) 171–177; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
