---
id: paper:2023krstic-venue-jap23-ps-00954-aq
type: paper
title: "Author query form (AIP proof): Krstic et al., J. Appl. Phys. (JAP23-PS-00954)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:methods-software
  - task:application
paper_keywords:
  - keyword:supporting-information
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: ""
year: 2023
authors:
  - "P. S. Krstic"
  - "E. T. Ostrowski"
  - "S. Dwivedi"
  - "S. Abe"
  - "A. Maan"
  - "A. C. T. van Duin"
  - "B. E. Koel"
venue: "AIP (proof artifact)"
pdf_sha256: "95b8f86ad97c4fd580a89f248c95b25b2ef75963092dd39d3d697d067551dc5f"
pdf_path: "papers/Krstic_JAP_2023_H_Li_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023krstic-venue-jap23-ps-00954-aq -->

## Summary

Some corpus paths register **publisher workflow PDFs**—author query forms, proof cover sheets, or production tickets—rather than the scientific article text. This entry documents an **AIP author-query / proof** artifact tagged internally as **JAP23-PS-00954** for a **Journal of Applied Physics** submission on **low-energy hydrogen irradiation of lithium and lithium-compound surfaces** studied with **ReaxFF combined with electronegativity equalization in LAMMPS**, in a fusion plasma–material interaction context. The file’s primary purpose in `papers/` is editorial: ORCID checks, affiliation formatting, reference DOI hygiene, and similar queries **do not constitute Methods** for the underlying science. The **`doi`** field is intentionally empty here because this PDF is not the bibliographic record of the published article; operators should populate it from the version of record when synchronized. Fusion devices expose first-wall materials to low-energy hydrogen isotopes; lithium conditioning layers motivate the scientific topic even though this PDF only records production metadata.

## Methods

### File type (publisher workflow, not article text)

**AIP author-query / proof** artifact (**JAP23-PS-00954**)—**ORCID**, **affiliations**, **reference** checks—not **simulation** protocols.

### Where science Methods live

**ReaxFF+EEM**, **Li\(_2\)O/LiOH** **amorphous** slabs, **H** **1–100 eV** impacts, **~10³** trajectories, **reflection/retention/sputtering** analysis: **`[[2023krstic-j-appl-phys-detailed-studies]]`** (**DOI** `10.1063/5.0149502`).

Mirroring the **VOR** page for retrieval: simulations use **LAMMPS** with **ReaxFF** plus **electronegativity equalization** so **atomic charges** evolve during **collision cascades**; **amorphous** **Li\(_2\)O** and **LiOH** surfaces are prepared from **fluorite** **Li\(_2\)O** starting points via **melt/quench**-style **cycles**, then bombarded by **H** at **1–100 eV** and **multiple incidence angles** with **~0.25 fs** timesteps and **thousands** of impacts accumulated for **statistics**—see **`[[2023krstic-j-appl-phys-detailed-studies]]`** for **cell sizes** and **analysis** definitions.

### Citation practice

Cite **J. Appl. Phys.** **VOR** for pagination—**not** this query PDF.

**Operator workflow:** when **merging** manifests, preserve this row if **publisher** **workflow** PDFs must remain **auditable**, but ensure **`paper_id`** **`[[2023krstic-j-appl-phys-detailed-studies]]`** carries the **bibliography** and **DOI** consumers should cite.

### 4 — Author-query / non-article (no simulation on this `pdf_path`)

**N/A** for **all** **MD/DFT** **checklist** items—this **PDF** is a **publisher** **workflow** artifact, not the **J. Appl. Phys.** **text**. **Simulation** **protocols** and **findings** live on **`[[2023krstic-j-appl-phys-detailed-studies]]`**.

## Findings

**No** **scientific** **reaction** **kinetics** or **plasma**–**material** **results** in this **author**-**query** **PDF**—treat that **content** as **N/A** here. **Compared** to any **J. Appl. Phys.** **reprint**, this file’s **sensitivity** to **pagination** and **affiliation** **flags** is an **operational** concern only, not a **physical** **limitation** of the **H**+**Li\(_2\)O/LiOH** **work** itself, which is summarized under **`[[2023krstic-j-appl-phys-detailed-studies]]`**. For **outlook** and **future** **citations** of the **H**-beam **sputtering** **kinetics** (e.g. **Coulombic** **focusing**, **EEM**), use the **published** **DOI** **10.1063/5.0149502**; this **AIP** **form** is **duplicative** and should not appear as **evidence** in a **bibliography** **line**.



## Limitations

Mixing workflow PDFs with primary literature in retrieval indices can confuse embeddings; navigation sections explicitly point readers to the VOR wiki entry. A separate manifest note documents slug migration for **`2023krstic-venue-paper` → `2025krstic-venue-paper`** in **`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`**; this file is distinct from that retirement.

## Relevance to group

Workflow artifact for van Duin-co-authored fusion PMI modeling with Princeton / Stony Brook collaborators.

## Citations and evidence anchors

- Article: [[2023krstic-j-appl-phys-detailed-studies]] — DOI [10.1063/5.0149502](https://doi.org/10.1063/5.0149502)

## Reader notes (navigation)

- Full narrative: [[2023krstic-j-appl-phys-detailed-studies]]  
- Force-field context: [[reaxff-family]]

## Related topics

- [[reaxff-family]]
- [[2023krstic-j-appl-phys-detailed-studies]]
