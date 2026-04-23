---
id: paper:2016page-venue-paper
type: paper
title: "Publisher proof fragment — ACS Applied Materials & Interfaces TOC graphic (non-article PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - task:software
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2016
authors: []
venue: "ACS (publisher workflow artifact)"
pdf_sha256: "d171f64cbd21c0aaf21b7e610a9f0f753ed9f74963636452e5c8de41df05d4d2"
pdf_path: "papers/Page proof- TOC.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2016page-venue-paper -->

## Summary

Publisher workflows sometimes emit **partial** **proof** bundles during production; such files are **valuable** only for **typesetting** QA and should not enter literature **summaries** as if they were **peer-reviewed** content. The machine-readable text in `normalized/extracts/2016page-venue-paper_p1-2.txt` is limited to the ACS Applied Materials & Interfaces masthead, the manuscript code `Msc: am6b01490`, and a statement that an accompanying graphic is slated for the table of contents, confirming that no scientific abstract or methods section exists in this ingest. The corpus file **`papers/Page proof- TOC.pdf`** is **not** a research article. As documented in [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (section B, publisher workflow artifacts), it is a **short publisher proof** fragment showing an **ACS Applied Materials & Interfaces** **table-of-contents** banner. The machine extract lists **`Msc: am6b01490`**, identifying the **manuscript** associated with the TOC graphic—this corresponds to the **same DOI family** as the **ACS AMI** article curated on **`[[2016osti-venue-am6b01490]]`** (**K⁺ intercalation / MXene / confined water**, DOI `10.1021/acsami.6b01490`). **No Methods, numerical results, or scientific prose** are present in this PDF; the wiki retains the slug solely to record **ingest provenance** and prevent mistaken **semantic indexing** of the banner as standalone science.

## Methods

The ingested file is a publisher table-of-contents workflow fragment (`papers/Page proof- TOC.pdf`). Machine text lists manuscript code **am6b01490**, matching the ACS Applied Materials & Interfaces letter on [[2016osti-venue-am6b01490]] (DOI `10.1021/acsami.6b01490`). There is no authored Methods section—only layout and production metadata—so MD, force-field training, static QM, experiments, and literature review blocks do not apply to this PDF. Downstream indexing should treat the slug as corpus packaging, not a primary chemistry source; protocol text lives on the canonical article and SI pages.

## Findings

This workflow **PDF** is not a scientific study: it records how a publisher table-of-contents graphic was linked to manuscript code **am6b01490**, which maps to the MXene + confined-water letter summarized on [[2016osti-venue-am6b01490]] (DOI `10.1021/acsami.6b01490`). There is therefore **no** primary **mechanism**, kinetics, or **interface** chemistry to report from the fragment itself—any discussion of **oxidation**, gallery **diffusion**, or **reactive** **MD** would be imported from the **version-of-record** article, not authored here. **Compared** to a normal paper page, the only meaningful benchmark is consistency with that **canonical** slug and its **DOI**; numerics, figures, and **experimental** versus **simulation** agreement live on the parent entry and its **SI** ([[2016osti-venue-microsoft-word]]). **Sensitivity** to laboratory humidity, intercalation stoichiometry, or **temperature** history cannot be read from this file because those **levers** never appear. **Limitations** are structural: **proof**-stage packaging can lag the issue **PDF**, and operators should treat this slug as manifest metadata only. For retrieval honesty, cite the **PDF** bundle that contains full Methods and **Findings**, not this banner fragment.

## Limitations

Maintainers who discover a **full-length** AMI PDF for **`am6b01490`** should attach it under the **canonical** slug **`[[2016osti-venue-am6b01490]]`** rather than repurposing this fragment. Operators must **not** cite **scientific conclusions** from this file. If the TOC was bundled accidentally during ingest, **treat** this slug as **workflow metadata**. **`extraction_quality: partial`** reflects **non-article** nature, not missing abstract text.

**Confidence rationale:** `med`—the page is **complete** as a **corpus registry** entry; scientific confidence is **not applicable**, so we mark **`med`** with explicit **non-primary** scope rather than **`high`**, which would falsely imply a peer-reviewed article summary.

## Reader notes (navigation)

If **manifest** cleanup ever **retires** this slug, **redirect** tooling should preserve the **`am6b01490`** pointer so **historical** **links** do not **404**. **Canonical article for `am6b01490`:** [[2016osti-venue-am6b01490]]
- [NON_PRIMARY catalog](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md)
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

Corpus **lint** rules should continue to **flag** **`doi: ""`** here as **intentional** unless a **separate** DOI is minted for **TOC** fragments (unlikely). **Related:** [[2016osti-venue-am6b01490]]
