---
id: paper:2022mao-venue-paper
type: paper
title: "Nanoscale author proof (d2nr00203e) — PAN blend carbon fiber precursors"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1039/d2nr00203e"
year: 2022
authors:
  - "Qian Mao"
  - "Siavash Rajabpour"
  - "Mahdi Khajeh Talkhoncheh"
  - "Jiadeng Zhu"
  - "Malgorzata Kowalik"
  - "Adri C. T. van Duin"
venue: "Nanoscale (proof PDF)"
pdf_sha256: "24cfa3e059c87aa0d58061674288fa1255a23d4a5e19a82d725e26b334e7422a"
pdf_path: "papers/Mao_Nanoscale_CarbonBlend_2022_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2022mao-venue-paper -->

## Summary

This corpus row stores a **Nanoscale author proof** PDF for **Qian Mao et al.**, *Nanoscale* **2022**, DOI **`10.1039/d2nr00203e`**, on **cost-effective polyacrylonitrile (PAN)-based blend precursors** for **carbon fibers**. Author proofs are pre-publication layout files that may still carry publisher queries, non-final figure captions, or pagination that differs from the issue PDF. For figures, supporting information pointers, and editorially finalized text, use **`[[2022mao-venue-d2nr00203e]]`**, which references the version-of-record PDF path in this repository. The scientific content, as summarized on that page, combines **ReaxFF** reactive molecular dynamics of **carbonization** with **Raman spectroscopy** and **transmission electron microscopy** on blends that include neat and oxidized PAN, PAN/nylon 6,6, and PAN/cellulose, interpreting ring formation, heteroatom species, and graphitic character during pyrolytic conversion. Carbon fiber manufacturing depends on how precursor chemistry translates to turbostratic graphitic domains; the article positions simulations as a way to rationalize why certain blends yield higher apparent crystallinity after pyrolysis when experiments are compared side by side.

## Methods

This corpus page registers the **Nanoscale author proof** bytes only; the **version-of-record** article with finalized layout, **ReaxFF** + **RDF** + **Raman**/**TEM** protocols, and numerical **tables** is [[2022mao-venue-d2nr00203e]] (`papers/Mao_Nanoscale_PAN_blend_carbonfibers_2022.pdf`). **Do not** re-cite **timestep**, **supercell sizes**, or **Raman** peak positions from the **proof** alone.

**MD application (ReaxFF pyrolysis):** **N/A in this file** — the peer-reviewed **Methods** in **`[[2022mao-venue-d2nr00203e]]`** list **LAMMPS**-based **reactive** **MD**, **NVT**-style **heating** programs, and **slab/periodic** models for **PAN**-blend **carbonization**; the proof PDF is not the citation-stable source for those **numbers**.

**Force-field and QM training:** **N/A in this file** — **parameter** lineage, **DFT**/**QM** **training** sets, and **refinement** cycles are on the **VOR** page and its **SI**.

**Experiments:** **Raman** and **TEM** on **pyrolyzed** **fibers**; full **sample** history, **furnace** program, and **Raman** assignments: **VOR** **Methods**/**SI** — **N/A** to re-derive from this **proof** slug.

**MD slot coverage (proof file — defer to VOR for numbers):** **N/A** **duration** in **ps**/**ns** on this page — **equilibration** and **production** **lengths** are in **`[[2022mao-venue-d2nr00203e]]`**. **N/A** **thermostat** **(Nose–Hoover** / **Langevin)** **damping** — use **VOR** **/ **SI**. **N/A** **independent** **hydrostatic** **pressure** **control** for the **NVT** **ramp** **(see** **VOR)**. **N/A** **exact** **temperature** **(K)** **timetables** **here** — the **VOR** **Methods** list **RDF**-based **T** **programs** for **ReaxFF** **pyrolysis**.
## Findings

**Outcomes / mechanisms (defer to VOR):** The **VOR** page summarizes **ReaxFF** **carbonization** of **PAN**-blend **models** and links **RDF**/**sp**\(^2\)**-proxy** **trends** to **Raman**/**TEM** on **fibers** after **pyrolysis** — the **version-of-record** **PDF** is the **citation** **source** (not the **author** **proof**). **Comparisons:** The **manuscript** **compares** **neat** **and** **oxidized** **PAN,** **PAN**/**nylon,** and **PAN**/**cellulose** in **Raman**/**TEM** **space**; **sensitivity** to **blend** **composition** and **T**-**time** in **furnace** **protocols** is in **the** **full** **article** **(not** **repeated** **here**)**. **Limitations / outlook:** This **page** is **not** a **version-of-record**; **uncertainties** in **D:G**-ratio **inference** and **Raman** **peak** **fits** are **on** the **VOR** **(see** `[[2022mao-venue-d2nr00203e]]` **)**. **Corpus** **honesty:** The **local** **pdf_path** is a **proof** **PDF** **duplicate** **—** use **VOR** **for** **pagination,** **SI,** and **repro** **reactive**-**MD** **settings.**
## Limitations

Proof PDFs can lack final copy edits and may not reflect the same figure resolution as the published issue. Cite **`[[2022mao-venue-d2nr00203e]]`** for stable scholarly references. Automated pipelines should not treat author-query banners as scientific content when building retrieval chunks. Supplementary Raman peak assignments live on the VOR page’s SI references.

## Relevance to group

Workflow duplicate for van Duin-co-authored Nanoscale ReaxFF pyrolysis and carbonization work.

## Reader notes (navigation)

- Canonical article: [[2022mao-venue-d2nr00203e]]

## Citations and evidence anchors

- DOI: [10.1039/d2nr00203e](https://doi.org/10.1039/d2nr00203e)

## Related topics

- [[reaxff-family]]
