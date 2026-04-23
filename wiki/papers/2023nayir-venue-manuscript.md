---
id: paper:2023nayir-venue-manuscript
type: paper
title: "Galley PDF: Modulation Effect of Substrate Interactions on Nucleation and Growth of MoS2 on Silica"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:methods-software
  - task:application
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.3c01010"
year: 2023
authors:
  - "Nadire Nayir"
  - "Stephen Bartolucci"
  - "Tao Wang"
  - "Chen Chen"
  - "Joshua Maurer"
  - "Joan M. Redwing"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C (galley)"
pdf_sha256: "faf3c17d7468a223fea17fecbf44661e52cb0f2f0180d0795cbefce5136c21f9"
pdf_path: "papers/Nayir_MoS2_silica_JPCC_2023_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023nayir-venue-manuscript -->

!!! abstract "Corpus role"

    **Galley / line-numbered** **JPCC** PDF for the same article as **`[[2023nadire-nayir-j-phys-chem-modulation-effect]]`** (DOI [10.1021/acs.jpcc.3c01010](https://doi.org/10.1021/acs.jpcc.3c01010)). Use the **online** PDF on the VOR page for stable figures, pagination, and final author proofs.

## Summary

This ingest registers a **pre-publication galley** of Nadire Nayir *et al.*, *J. Phys. Chem. C*, on how **silica hydroxylation** steers **MoO\(_3\)** precursor chemistry and **MoS\(_2\)** **nucleation** and **growth**. The scientific content—**ReaxFF** and **DFT** simulations paired with **CVD** experiments—is curated on **`[[2023nadire-nayir-j-phys-chem-modulation-effect]]`**. In brief, **hydroxylated** SiO\(_2\) surfaces favor thermodynamically and kinetically accessible reactions with **MoO\(_3\)** that seed **molybdenum oxide** nuclei and subsequent **sulfurization** toward **MoS\(_2\)**, whereas more **dehydroxylated** silica remains comparatively **inert** under the highlighted conditions. The substrate’s chemical state therefore modulates **effective growth temperature** and **nucleation density** by opening or closing interfacial reaction channels.

**Galley-specific cautions.** Galley PDFs frequently retain **line numbers**, **editor queries**, or **layout** differences that do not appear in the **issue** PDF. Page numbers and **Supporting Information** cross-references may therefore **not** match library-hosted copies. For any external write-up—manuscript, thesis, or database record—treat **`[[2023nadire-nayir-j-phys-chem-modulation-effect]]`** as the **bibliographic** anchor and use this slug only for **internal** provenance tracking of which **PDF bytes** were ingested.

## Methods

**4 — Non-primary (galley duplicate; same work as the VOR ingest).** This file records **`Nayir_MoS2_silica_JPCC_2023_galley.pdf`**, which is the **pre-publication** **galley** of the *J. Phys. Chem. C* article (DOI `10.1021/acs.jpcc.3c01010`) whose **curation** lives at **`[[2023nadire-nayir-j-phys-chem-modulation-effect]]`**.

**MD / DFT / CVD (N/A as standalone protocol text here).** ReaxFF+DFT+experiment **settings** (e.g. **0.25 fs** timestep, **NVT+Berendsen+ADF/ReaxFF**, PBC, silica prep, MoO\(_3\)/S\(_2\)/H\(_2\)S **stages**, CVD conditions) are **not** re-derived on this duplicate page. Use the **VOR** wiki page and **JPCC** **SI** for the **actual** **Methods** narrative; this slug is a **provenance/duplicate** record only. **N/A** — a **separate** **FF** **or** **E-field** / **metadynamics** method story **not** in the MoS\(_2\)/silica **JPCC** VOR+SI.

## Findings

Qualitative conclusions match the VOR summary: **surface hydroxylation** increases **reactivity** toward **MoO\(_3\)** and enables **substrate-mediated nucleation** pathways that raise MoS\(_2\) coverage relative to passive supports in the authors’ comparison.

The **operational finding** for the knowledge base is that **two PDF registrations** (**galley** versus **online/VOR-class**) coexist for one DOI; downstream **chunk** and **manifest** tooling must keep **`pdf_sha256`** aligned with the file actually on disk. When in doubt, prefer the **VOR** page for **numerical** citations and keep this galley note as a **duplicate-ingest** pointer.

**Scholarly practice.** In reference lists, cite the **journal** article once; mention **galley** duplication only in **supplementary** **provenance** notes or internal **wiki** links, not as if it were a distinct publication.

**MAS note.** Retrieval systems should **deduplicate** embeddings for these two slugs when answering questions about **MoS\(_2\)** on **silica**, routing users to **`[[2023nadire-nayir-j-phys-chem-modulation-effect]]`** for **methods** **numbers** and **figures**.

## Limitations

**Galley** PDFs retain **line numbers**, may differ in **layout** from the **issue PDF**, and can lack final **copy edits** or **figure** tweaks—cite **`[[2023nadire-nayir-j-phys-chem-modulation-effect]]`** for publication references and locators.

## Relevance to group

Workflow duplicate for the **2DCC** / **van Duin** **MoS\(_2\)**-on-**silica** collaboration with **Joan Redwing**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.jpcc.3c01010](https://doi.org/10.1021/acs.jpcc.3c01010)

## Reader notes (navigation)

- Version of record: **`[[2023nadire-nayir-j-phys-chem-modulation-effect]]`**
**Galley vs VOR.** Prefer `[[2023nadire-nayir-j-phys-chem-modulation-effect]]` for stable pagination and final figures when citing MoS\(_2\)/silica growth chemistry.

## Reproducibility and corpus locators

This note documents **where** to find primary evidence in-repo; it does **not** add new scientific claims beyond the cited publication.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, timesteps, ensembles, kinetics), use the peer-reviewed PDF (and publisher Supporting Information) as the authoritative source; this wiki summarizes for navigation and retrieval.

## Related topics

- [[reaxff-family]]
