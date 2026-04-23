---
id: paper:2014zou-venue-paper
type: paper
title: "Acta Materialia author proof (registered corpus PDF; article text not in extract)"
updated: "2026-04-20"
confidence: low
canonical_tags:
  - domain:alloys-metallurgy
  - task:application
  - scale:atomistic
source_refs: []
doi: null
year: 2014
authors: []
venue: "Elsevier author proof PDF (`papers/Zou_ActaMater_2014_proof.pdf`)"
pdf_sha256: "0ee9d3295e02079e7ea7ea26fee55140f2e01ac4ee7ba4de6b83430556d8cb82"
pdf_path: "papers/Zou_ActaMater_2014_proof.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014zou-venue-paper -->

!!! note "NON_PRIMARY catalog"

    This slug registers an **Elsevier author proof** PDF, not the recommended **version-of-record** article file. See [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section **D** (`2014zou-venue-paper` ↔ **`2014zou-acta-materia-molecular-dynamics`**).

## Evidence and attribution

!!! note "Authority of statements"

    This page is a **provenance stub**. It does **not** substitute for full-text curation from the **final** **Acta Materialia** PDF. Scientific summaries of the underlying research belong on **`paper:2014zou-acta-materia-molecular-dynamics`** and should be grounded in extracts from **`papers/Zou_ActaMater_2014.pdf`**.

## Summary

The corpus maintains a separate manifest row for **`papers/Zou_ActaMater_2014_proof.pdf`**, associated with **`paper:2014zou-venue-paper`**. The normalized **pages 1–2 extract** for this path contains **Elsevier author-query / proof boilerplate** rather than the article **abstract**, **introduction**, or **results**, so this wiki entry cannot responsibly restate quantitative **ReaxFF** findings, **Ni–O** transport coefficients, or **grain-boundary** oxidation mechanisms from primary sections. Operators should treat the proof file as **bibliographic evidence** that a proof-stage PDF was ingested, while directing readers to the **canonical article record** for the same scientific contribution. The underlying publication—**molecular dynamics simulations of vacancies, diffusion, and oxidation initiation in nickel using ReaxFF**—is curated under **`paper:2014zou-acta-materia-molecular-dynamics`** with **`pdf_path`: `papers/Zou_ActaMater_2014.pdf`**, **DOI `10.1016/j.actamat.2014.09.047`**, and a **good** extraction quality flag.

## Methods

No reliable **methods** text is recoverable from the **proof-front-matter** extract tied to this slug. **Methods** for the scientific article appear in the **final** **Acta Materialia** PDF and are summarized on [[2014zou-acta-materia-molecular-dynamics]].

## Findings

**Outcomes and mechanisms.** **N/A** for this slug: the normalized **extract** tied to the **proof PDF** is Elsevier front matter, not **Results** text describing **Ni** self-**diffusion**, **oxygen** interstitial hopping, **grain-boundary** transport, or void-localized **oxid**ation nucleation. Those **mechanistic** summaries live only where the peer-reviewed sections are available.

**Comparisons.** **N/A** here. The **version-of-record** article on [[2014zou-acta-materia-molecular-dynamics]] is where the authors **benchmark** ReaxFF transport against **literature** values and discuss **versus**-experiment agreement for the Ni–O training and application story.

**Sensitivity and design levers.** **N/A** at proof-ingest resolution: trends with **temperature**, **pressure**, **vacancy** content, or boundary topology are not recoverable from boilerplate pages; read the final PDF for parameter sweeps the authors actually report.

**Limitations and outlook.** This ingest is intentionally a **duplicate PDF** placeholder—**limitations** include lack of DOI in front matter and lack of indexed science text. **Future work** for operators is to keep all quantitative claims on the **canonical** wiki page and refresh manifests if the proof blob changes.

**Corpus honesty.** Treat `papers/Zou_ActaMater_2014_proof.pdf` as **galley**/**proof** provenance only; prefer **`papers/Zou_ActaMater_2014.pdf`** for **PDF**-grounded curation and retrieval chunks.

## Limitations

- **Stub status** is intentional: avoid inventing **DOI**, **page numbers**, or **numerical** results here.
- **Duplicated curation** should not drift: if the proof PDF is retired from the corpus, update **`pdf_path`** and manifests in a controlled ingest operation.

## Reader notes (navigation)

Automation should treat this slug as **manifest bookkeeping** only: downstream **MAS** pipelines must not prefer this page over **`paper:2014zou-acta-materia-molecular-dynamics`** when both exist, because the **proof** PDF lacks reliable **abstract** text for chunking.

## Relevance to group

Maintains **link stability** for a **non-primary** PDF while steering scientific readers to the **VOR** sibling in the same **Ni oxidation** cluster.

## Citations and evidence anchors

- None assigned from the proof-only extract.
- Canonical science: [[2014zou-acta-materia-molecular-dynamics]] (`10.1016/j.actamat.2014.09.047`).

## Related topics

- [[reaxff-family]]
- [[2014zou-acta-materia-molecular-dynamics]]
