---
id: paper:20192019-venue-paper
type: paper
title: '2D Metal Carbides and Nitrides (MXenes): Structure, Properties and Applications
  (book)'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:2d-layered
- task:review
- scale:multiscale
paper_keywords:
- keyword:review-or-perspective
- keyword:2d-materials
candidate_tags: []
source_refs: []
doi: ''
year: 2019
authors:
- Babak Anasori
- Yury Gogotsi
venue: Springer (2019)
pdf_sha256: 2079ab0a9db9b31da4fa5ef054e36bf3d0ae417efbc3013adf4ed65a364cbfe1
pdf_path: papers/2019_Book_2DMetalCarbidesAndNitridesMXen.pdf
extraction_quality: partial
group_affiliation: false
---
<!-- id:paper:20192019-venue-paper -->

## Summary

This corpus PDF is the **Springer** edited volume **“2D Metal Carbides and Nitrides (MXenes): Structure, Properties and Applications”** (**2019**), with **Babak Anasori** and **Yury Gogotsi** as editors. The `normalized/extracts/20192019-venue-paper_p1-2.txt` snippet records the **title page** (series subtitle: **Structure, Properties and Applications**). The book is a **multi-chapter reference** on **MXene** chemistry, **synthesis**, **structure**, **processing**, **properties** (electronic, optical, mechanical), and **applications** (energy storage, coatings, and related topics)—not a single peer-reviewed **research article**. It sits alongside other corpus fragments such as [[2019mxenes-venue-paper]], which preserves an **uncorrected proof table of contents** for the same Springer line and can help locate **chapter titles** and **authors** when navigating the full PDF. This wiki entry does **not** substitute reading individual **chapters** for technical claims: each chapter has its own methods, code, and level of theory. For **retrieval** systems, treat **`paper:20192019-venue-paper`** as a **container** node: link **downstream** **paper** pages for any chapter that receives full **Phase 4** curation, and keep **canonical_tags** focused on **2D** **MXene** **literature** rather than on one **simulation** code.

## Methods

This Springer **2019** edited volume is a **review**/**reference** compilation, not one **Methods** section for a single study. Chapters mix **experiment** (synthesis, processing, characterization), **DFT** and other **QM** routes, **continuum** models, and occasional **molecular dynamics** with **ab initio** or **empirical** **potentials**; timesteps, **basis** **sets**, **k-point** meshes, **ensembles** (**NVE**/**NVT**/**NPT**), and software stacks differ by chapter. Operators must open the relevant **chapter** (or its DOI) before attributing **ReaxFF** vs **DFT** vs device modeling—do not infer a single **force field** for the whole book from this landing page. The corpus retains the full-book **PDF** for keyword search; `normalized/extracts/` currently holds only a **short** **title-page** **snippet**, so detailed **protocol** tables are **N/A** on this stub.
## Findings

**N/A as a unified experimental outcome.** Each **chapter** states its own **mechanisms**, **property** trends, and **comparisons** to **experiment** or **literature**; this **container** page does not synthesize new chemistry across chapters. For **retrieval**, the defensible **corpus** facts are: a searchable **MXene** monograph **PDF** exists at `pdf_path`, while **`normalized/extracts`** holds only a **title-page** **snippet**, so quantitative **barriers**, **conductivity** numbers, or **synthesis** yields are **not** asserted here—follow the cited **chapter** DOIs instead. **Limitations** and **future work** likewise live at **chapter** scope; KB **gaps** (missing **chapter** stubs) are operator metadata, not claims about the book’s contents.
## Limitations

**Partial text extract** in `normalized/extracts/` relative to the full monograph. **No DOI** is stored in frontmatter for the whole volume in this record—assign **chapter-level** or **publisher** identifiers when curating downstream. The wiki’s **paper** model is optimized for **journal articles**; **books** are retained for **context** and **retrieval** hooks.

## Relevance to group

Background on **2D carbides/nitrides** that often appear next to **graphene** and **TMD** materials in **interface** and **energy** simulation literature; **group-adjacent** chapters (for example **MD** of **MXenes** in the broader Springer line) may be cross-linked when those chapters have dedicated **paper** stubs.

## Citations and evidence anchors

- PDF: `papers/2019_Book_2DMetalCarbidesAndNitridesMXen.pdf`.
- Navigation aid (TOC fragment): [[2019mxenes-venue-paper]].

## Related topics

- [[2019mxenes-venue-paper]]
- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
