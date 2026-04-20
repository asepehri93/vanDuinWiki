---
id: papers:index
type: concept
title: Papers index
updated: "2026-04-20"
confidence: high
canonical_tags: [domain:methods-software]
candidate_tags: []
source_refs: []
supported_by: []
---

# Paper pages

There are **190** curated notes in this folder—**one file per registered publication** (`wiki/papers/<slug>.md`). Each note’s **scientific content** is a **summary of that paper** (see the **Evidence and attribution** section on each page and the DOI in the YAML header). Nothing here replaces reading the **original article** for definitive numbers and figures.

## Find a paper

| Route | Best when… |
|-------|------------|
| [**By publication year**](../concepts/paper-index-by-year.md) | You want a **complete sortable list** (metadata from front matter only). |
| [**By primary domain tag**](../concepts/paper-index-by-domain.md) | You want to browse by **taxonomy** (`domain:*` from each note). |
| **Search** (`/` on the site) | You know an **author**, **keyword**, or **slug fragment**. |
| [**Themes overview**](../concepts/themes-index.md) | You want **topic essays** that link to many papers. |

## Corpus metadata (repository)

- [`raw/MANIFEST.jsonl`](https://github.com/asepehri93/vanDuinWiki/blob/main/raw/MANIFEST.jsonl) — ingest manifest  
- [`outputs/corpus_profile_2026-04.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/outputs/corpus_profile_2026-04.md) — profile snapshot  

## Featured synthesis (entry points, not exhaustive)

- [Themes overview (all clusters)](../concepts/themes-index.md)  
- [ReaxFF family overview](../forcefields/reaxff-family.md)  
- [Batteries & interfaces](../concepts/batteries-interfaces-reaxff.md)  
- [Graphene / nanocarbon](../materials/graphene-nanocarbon.md)  
- [Debates](../debates/transferability-reactive-ff.md) — [ReaxFF vs MLIPs](../debates/reaxff-vs-mlip-accuracy.md)  
- [Parameterization workflow](../protocols/reaxff-parameterization-workflow.md)  

## Maintainer note

Regenerate the **by-year** and **by-domain** listing pages after bulk metadata edits:

`python3 scripts/generate_papers_indexes.py`
