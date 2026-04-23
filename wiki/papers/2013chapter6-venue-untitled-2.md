---
id: paper:2013chapter6-venue-untitled-2
type: paper
title: "Computational Catalysis (RSC book): Chapter 6 proof (annotated) — production queries"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:methods-software, domain:catalysis-surfaces, task:review, scale:atomistic]
candidate_tags: []
source_refs: []
doi: ""
year: 2013
authors: []
venue: "RSC Publishing (book proof)"
pdf_sha256: "5463c86f5c674dbf3a310e43d02b3ab9d3533ab6b11e2f1af40ca8e209c4739a"
pdf_path: "papers/Chapter6_water_annotated.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013chapter6-venue-untitled-2 -->

## Evidence and attribution

!!! note "NON_PRIMARY placeholder (AGENTS + docs/corpus)"

    This slug is documented in **`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`** as a **duplicate placeholder** book-chapter proof path. The ingested **`normalized/extracts`** text contains **publisher production queries** (reference formatting, figure permissions, acronym checks), **not** the scientific chapter body. The wiki therefore cannot restate chapter **Methods** or **Findings** from the local PDF; operators need a **final chapter PDF** or publisher download for authoritative content.

Per [`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md), the sibling `2013chapter6-venue-untitled` shares the same placeholder lineage.

## Summary

The file `papers/Chapter6_water_annotated.pdf` is an **annotated proof** fragment associated with the RSC *Computational Catalysis* book series. Pages captured in `normalized/extracts/2013chapter6-venue-untitled-2_p1-2.txt` list typesetting questions (e.g., reference DOI completion, Supporting Information packaging) rather than scientific sections. The intended chapter concerns computational catalysis topics involving water-related modeling, but **no faithful Summary of results** can be extracted from the proof queries alone without the final chapter text.

## Methods

The file **`papers/Chapter6_water_annotated.pdf`** is an **annotated RSC proof** fragment; `normalized/extracts/2013chapter6-venue-untitled-2_p1-2.txt` records **production queries** (reference formatting, **Supporting Information** packaging, figure permissions), not the **Chapter 6** scientific **Methods** text.

**1 — MD application.** **N/A —** no **engine**, **supercell**/**stoichiometry**, **PBC** description, **ensemble**, **timestep**, **duration**, **thermostat**, **barostat**, **temperature** program, **pressure**, **electric field**, or **enhanced sampling** protocol appears in the indexed **query** pages.

**2 — Force-field training.** **N/A —** no **ReaxFF** (or other) **parameterization** narrative is extractable from the snippet.

**3 — Static QM / DFT.** **N/A —** no **DFT**/**QM** setup is extractable from the snippet.

**4 — Reviews / book chapter (intended role vs this file).** The **intended** chapter is book-level **review** prose on **ReaxFF** **water** (see **`[[2013ch006-venue-ch006]]`** for a DOI-aligned chapter ingest). **This PDF path** cannot support AGENTS-style protocol extraction until a full-text chapter PDF replaces or supplements the proof bundle.

When a final chapter PDF becomes available, update **`pdf_path`** / hashes per ingest policy and rewrite **Methods** from the published chapter with evidence-backed numerical lines.

## Findings

**1 — Outcomes & mechanisms.** **N/A —** no **reaction**/**interface** **Results** are present in `normalized/extracts/2013chapter6-venue-untitled-2_p1-2.txt`.

**2 — Comparisons.** **N/A —** no **experiment**/**QM** comparisons appear in the indexed **proof** fragment.

**3 — Sensitivity / design levers.** **N/A —** no simulation **knobs** (e.g., **temperature** sweeps) are reported in the placeholder text.

**4 — Limitations & outlook.** The indexed pages are **publisher workflow** artifacts; the **outlook** for KB use is to ingest rights-cleared chapter text or deduplicate to **`[[2013ch006-venue-ch006]]`**.

**5 — Corpus honesty.** **`confidence: low`** reflects missing primary scientific text in the corpus extract for this path, not uncertainty about unrelated chemistry. Do not cite this slug as a scientific authority in theme hubs; use it as a **file pointer** only.

## Limitations

This record exists for **manifest completeness** and **provenance** only. **`confidence: low`** reflects missing primary scientific text in the corpus extract, not uncertainty about unrelated work.

Maintainers should avoid linking this slug from theme hubs as a scientific authority; use it only as a **file pointer** inside ingest documentation. When a final PDF arrives, replace the placeholder prose with extract-backed summaries and raise `confidence` accordingly.

## Corpus notes

Append future `normalized/extracts/*_p1-2.txt` snippets to the manifest notes when reprofiling so operators can see whether scientific text has landed without opening binary PDFs manually across case-sensitive volumes.

Book chapters sometimes arrive under multiple ISBNs; if the corpus later ingests a differently named PDF for the same chapter, prefer DOI-based deduplication rules in `raw/MANIFEST.jsonl` rather than filename heuristics alone.

Until the chapter body is present, avoid tagging this slug with `paper_keywords` that imply specific catalytic chemistry beyond what `AGENTS.md` allows without extract support.

## Relevance to group

Book-proof bookkeeping; no standalone research article.

## Citations and evidence anchors

- Proof query extract: `normalized/extracts/2013chapter6-venue-untitled-2_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[2013chapter6-venue-untitled]]
