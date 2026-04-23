---
id: paper:2013jacobs-venue-rsc-cy
type: paper
title: "Conformational studies of ligand-template assemblies and the consequences for encapsulation of rhodium complexes and hydroformylation catalysis"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:catalysis-surfaces, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1039/c3cy20665c"
year: 2013
authors: ["Jacobs, Ivo", "van Duin, Adri C. T.", "Kleij, Arjan W.", "Kuil, Mark", "Tooke, Duncan M.", "Spek, Anthony L.", "Reek, Joost N. H."]
venue: "Catalysis Science & Technology"
pdf_sha256: "2a50644ddc6a9ff93517ea28bfce0dc152c36861b59a9aaf3e2099eca223a265"
pdf_path: "papers/Jacobs_CST_2013_proofs.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013jacobs-venue-rsc-cy -->

## Evidence and attribution

!!! note "NON_PRIMARY proof (docs/corpus)"

    [`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) flags **`2013jacobs-venue-rsc-cy`** as a **RSC proof** PDF whose local extract is **production queries**, not the article body. The peer-reviewed **Catalysis Science & Technology** article is identified by **DOI** `10.1039/c3cy20665c`; curated scientific prose should ultimately follow a **final PDF** or publisher HTML—not the proof fragment alone.

## Summary

The published article (title above) addresses supramolecular **ligand–template assemblies** relevant to **hydroformylation catalysis**, including how conformational degrees of freedom in templated ligand frameworks influence **encapsulation of rhodium complexes** and downstream catalytic consequences. Adri C. T. van Duin appears among the coauthors, consistent with computational chemistry support for organometallic systems in the group’s portfolio. The ingested corpus PDF, however, only provides **typesetter queries** on pages captured in `normalized/extracts/2013jacobs-venue-rsc-cy_p1-2.txt` (reference formatting, crystallographic checks), so this wiki cannot responsibly restate specific **computational settings**, **energies**, or **spectroscopic data** from local extracts.

## Methods

**Corpus note:** `normalized/extracts/2013jacobs-venue-rsc-cy_p1-2.txt` and **`papers/Jacobs_CST_2013_proofs.pdf`** contain **RSC proof** boilerplate and queries only—no author **Methods** body is available in this repository snapshot (**DOI** `10.1039/c3cy20665c`).

**1 — MD application (atomistic dynamics).** **Reactive molecular dynamics**/**MD** protocol lines (**LAMMPS**/**CP2K**/other engine, **atom** counts, **PBC**, **NVT**/**NPT**, **timestep** in **fs**, **ps**/**ns** **equilibration**/**production**, **thermostat**, **barostat**, **temperature** **K**, **pressure**, **electric field**, **replica**/**enhanced sampling**) are **N/A** here because the ingested **PDF** fragment does not include the computational **Methods** section.

**2 — Force-field training.** **N/A** from proof fragment—cannot confirm whether **ReaxFF** or other reactive fits appear without the **version-of-record** text.

**3 — Static QM / experiment.** **N/A** from proof fragment—expected **DFT**, **NMR**, crystallography, and catalysis assay details must be lifted from the final *Catal.* *Sci.* *Technol.* article, not from typesetter queries.

**4 — Review / non-simulation framing.** **N/A** — this is not a review; the missing sections are a **PDF** ingestion gap, not a genre choice.

## Findings

**Outcomes & mechanisms:** **N/A** — no **reaction**/**encapsulation**/**catalysis** results are present in the proof-only extract.

**Comparisons:** **N/A** — no **experimental** or computational benchmarks appear in `2013jacobs-venue-rsc-cy_p1-2.txt`.

**Sensitivity / design levers:** **N/A** — **temperature**, **pressure**, **concentration**, and **strain** knobs for catalysis are not extractable from the proof pages.

**Limitations & outlook:** The peer-reviewed article likely contains the substantive science; this wiki entry cannot summarize performance metrics until a **version-of-record** **PDF** replaces or supplements the proof file.

**Corpus honesty:** **`NON_PRIMARY_ARTICLE_PAPER_SLUGS`** flags this slug as **proof**; treat third-party metrics as **unverified** against this repo until full text is ingested.

## Limitations

**Low confidence** reflects missing scientific body text in the corpus snapshot, not a judgment about the underlying peer-reviewed work. Replace this page when a clean PDF is available.

## Corpus notes

If crystallographic CIF files accompany the article, register their hashes in `normalized/papers` records so automated pipelines can link crystal structures to computational setup paragraphs once they are written.

Homogeneous catalysis entries in this knowledge base should cross-link to **`[[reaxff-family]]`** only when the primary text actually uses reactive MD; do not assume from the proof stub alone.

## Relevance to group

Proof retained for **provenance**; van Duin co-authorship links the entry to **homogeneous catalysis** modeling threads.

## Citations and evidence anchors

- DOI: [10.1039/c3cy20665c](https://doi.org/10.1039/c3cy20665c) — proof extract: `normalized/extracts/2013jacobs-venue-rsc-cy_p1-2.txt`

## Related topics

- [[reaxff-family]]
