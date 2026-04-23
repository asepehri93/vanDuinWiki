---
id: paper:2013vanduin-venue-paper
type: paper
title: "Reactive force fields: concepts of ReaxFF and applications to high-energy materials"
updated: "2026-04-20"
confidence: low
canonical_tags:
  - domain:reaxff-lineage
  - domain:reactive-md
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:review
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2013
authors:
  - "van Duin, Adri"
  - "Verners, Osvalds"
  - "Shin, Yun-Kyung"
venue: "International Journal of Energetic Materials and Chemical Propulsion"
pdf_sha256: "fa4277dfa5e1ce5a7705c3a0446f3ef98c1095d7731c720c20e51441d3fe96f0"
pdf_path: "papers/vanDuin_IJEMCP_2013_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013vanduin-venue-paper -->

!!! note "NON_PRIMARY catalog"

    **`papers/vanDuin_IJEMCP_2013_galley.pdf`** is **editorial / production correspondence** rather than a standalone research article PDF in the corpus interpretation. See [`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section **F**. Use the sibling journal PDF **`paper:2013ijemcp1202-1-5739-venue-paper`** (`papers/IJEMCP1202(1)-5739.pdf`) for article text when curating prose.

## Evidence and attribution

!!! note "Authority of statements"

    This page documents **ingest provenance** and **navigation** between **galley** fragments. Detailed tutorial content should be verified against the **full** IJEMCP article PDF, not only **`p1–2`** extracts.

## Summary

The corpus associates **`paper:2013vanduin-venue-paper`** with a **Begell House galley** PDF whose early pages are dominated by **publisher instructions** and **production correspondence**, which makes automated extraction a poor primary source for the scientific text. The embedded bibliographic hints nonetheless point to a **review-style** article titled **“Reactive force fields: concepts of ReaxFF and applications to high-energy materials,”** authored by **Adri van Duin**, **Osvalds Verners**, and **Yun-Kyung Shin**, aimed at **energetic materials** and **chemical propulsion** readership. A parallel ingest with a cleaner article path exists as **`paper:2013ijemcp1202-1-5739-venue-paper`**, sharing the same conceptual purpose: explain **ReaxFF** concepts (bond order vs distance, charge equilibration, training philosophy) and illustrate applications to **nitramines**, **binders**, and **metallic** energetic formulations.

## Methods

**4 — Reviews / perspectives (non-simulation primary on this slug).** This **`pdf_path`** (`papers/vanDuin_IJEMCP_2013_galley.pdf`) is catalogued as **non-primary**: the normalized extract is dominated by **Begell House production correspondence** and proofing instructions (`normalized/extracts/2013vanduin-venue-paper_p1-2.txt`), not typeset article **Methods**. Operators should treat **[[2013ijemcp1202-1-5739-venue-paper]]** (`papers/IJEMCP1202(1)-5739.pdf`) as the location for any **peer-reviewed** exposition of how **ReaxFF** concepts (bond order vs distance, charge equilibration, training philosophy) are tied to **energetic materials** case studies.

**1 — MD application.** **N/A —** no reproducible production **MD** protocol (engine, timestep, thermostat, barostat, **T/P** schedules) can be read from the **correspondence** PDF/extract on this slug.

**2 — Force-field training.** **N/A —** same reason; any **parameterization** workflow text must be taken from the **article** PDF sibling, not from publisher front matter here.

**3 — Static QM / DFT-only.** **N/A —** not recoverable as a standalone **DFT** methods report from this ingest path.

## Findings

**Corpus honesty.** **Findings**, benchmarks, and tutorial-style conclusions for **“Reactive force fields: concepts of ReaxFF and applications to high-energy materials”** are **not** excerptable from **`papers/vanDuin_IJEMCP_2013_galley.pdf`**. For the article’s intended **review** outcomes—contrasting **QM** vs **classical** modeling for **energetic materials**, discussing **reactivity** sensitivity to **parameterization**, and stating **limitations** of **bond-order** reactive models—use **`paper:2013ijemcp1202-1-5739-venue-paper`** and its **`pdf_path`**.

**Outcomes & mechanisms / comparisons / sensitivity / limitations (authored).** **N/A on this slug** beyond navigation: the galley fragment does not carry stable **Results** text; do not paraphrase **OCR** boilerplate as science.

## Limitations

**DOI** is not recorded in frontmatter from garbled OCR lines—do not fabricate. **`extraction_quality: partial`** reflects **non-article** front pages. Automated **DOI** extraction from **OCR**-noisy lines is **disallowed** by project policy; add **`doi`** only from publisher metadata you can **verify**.

## Reader notes (navigation)

This slug exists because **`paper_id`** stability matters more than filename aesthetics; when editors need tutorial prose, use [[2013ijemcp1202-1-5739-venue-paper]] and keep this page as a **pointer** for **galley** provenance. Refresh **`source_refs`** only when new **peer-reviewed** anchors appear—do not mirror long narratives into **`normalized/`** JSON.

## Relevance to group

**Operator record** for a **non-primary** galley path; canonical teaching content is cross-linked to [[2013ijemcp1202-1-5739-venue-paper]].

## Citations and evidence anchors

- Extract pointers: `normalized/extracts` for this slug (production text), plus [[2013ijemcp1202-1-5739-venue-paper]] title page.

## Related topics

- [[reaxff-family]]
- [[2013ijemcp1202-1-5739-venue-paper]]
