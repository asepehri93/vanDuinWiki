---
id: paper:2021nayir-venue-paper
type: paper
title: "Theoretical modeling of edge-controlled growth kinetics and structural engineering of 2D-MoSe2 (publisher proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - material:tmd
  - task:parameterization
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1016/j.mseb.2021.115263"
year: 2021
authors:
  - "Nadire Nayir"
  - "Yuanxi Wang"
  - "Yanzhou Ji"
  - "Tanushree H. Choudhury"
  - "Joan M. Redwing"
  - "Long-Qing Chen"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
venue: "Mater. Sci. Eng. B (proof); same work as DOI above"
pdf_sha256: "9f8b966750db6dfb7cdb7d560145fdbd0dd16abcade99ad939849cde91fbdbdc"
pdf_path: "papers/Nayir_MoSe2_MatSciEngB_2021_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2021nayir-venue-paper -->

!!! note "Corpus note"
    **`papers/Nayir_MoSe2_MatSciEngB_2021_galley.pdf`** is a **publisher proof/galley**. The **version-of-record** page is [[2021nayir-materials-sc-theoretical-modeling]] (`Nayir_MoSe2_MatSciEngB_2021.pdf`). See [`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Summary

**MoSe₂** **MOCVD** and related **CVD** routes can yield **triangular** or **hexagonal** **islands** whose **shapes** reflect **edge**-energy anisotropy; connecting **atomistic** **energies** to **mesoscale** **morphology** is a central modeling goal. The Materials Science and Engineering B abstract text states that the reported ReaxFF for Mo/Se/H interactions is trained primarily on first-principles energetics for periodic and non-periodic data, captures the structural transition between metallic and semiconducting phases, reports defect energetics and selenium-vacancy migration barriers, and couples a Wulff-type model to observed morphology evolution of two-dimensional MoSe₂ domains during growth. The **Materials Science and Engineering B** article (DOI `10.1016/j.mseb.2021.115263`) develops a **ReaxFF** description of **Mo/Se/H** chemistry informed by **first-principles** data, applies **MD** to **defects**, **phase** behavior, and **Se-vacancy** migration, and couples **continuum** **Wulff**-type constructions to **edge** energies to interpret **2D MoSe₂** **domain** morphologies during growth. This ingest tracks a **galley** PDF with potentially **non-final** figures and pagination; **scientific narrative**, **methods detail**, and **bibliography** should be taken from **`[[2021nayir-materials-sc-theoretical-modeling]]`**.

## Methods

This `pdf_path` is the **Elsevier proof** (`Nayir_MoSe2_MatSciEngB_2021_galley.pdf`). **Citable** **DFT** **convergence**, **ReaxFF** **table** **text**, **LAMMPS** **(fs) timestep**, **K**-listed **NVT** **Nosé–Hoover**-class **thermostat** settings, and **Wulff** **inputs** may differ in **pagination** or **figure** **quality** from the **VOR**—use **[[2021nayir-materials-sc-theoretical-modeling]]** and the **ScienceDirect** VOR+SI for **authoritative** **details**.

**Same work, summary only (see VOR for all numbers):** a **Mo/Se/H** **ReaxFF** is **trained** on **DFT** **data**; **ReaxFF** **molecular** **dynamics** on **defects** and **phases** uses **NVT** **PBC** **supercells** with **temperatures** in **K** and **ps**–**ns**-scale **equilibration**/**production** as **in** the **MSE** **B** **VOR**; **CVD** **furnace** **~1** **bar** is a **laboratory** **boundary** **(bar)** **outside** the **MD** **box** for the **reactor** **modeling** **discussed** in the **article**, not automatically the same as an **NPT** **barostat** in every **MD** **segment**. **Hydrostatic** **pressure** in **(bar) — N/A** to **re-key** for this **proof**; see **VOR** for any **NPT** **stanzas**. **N/A** to re-type the **ReaxFF** / **Wulff** **block** from this **galley**; **deferred** to **`[[2021nayir-materials-sc-theoretical-modeling]]`**.

**MD/DFT line-by-line: N/A on this slug**—open the VOR and **SI** via **`[[2021nayir-materials-sc-theoretical-modeling]]`**.

## Findings

**Corpus / operator finding.** The **proof** and **VOR** **PDFs** have **different** **`pdf_sha256`**; **use** the **VOR** **page** and **file** for **bibliography**, **automation**, and **hash**-**keyed** **extracts**. **Scientific** **conclusions** (**ReaxFF** **fit**, **Wulff** **morphology** **trends**, **defect** **kinetics**) are **narrated** on **`[[2021nayir-materials-sc-theoretical-modeling]]`**; **N/A** to **re-figure** from **galley** here.

**Comparisons. N/A** on this **ingest** — see **VOR** **for** **experiment/DFT** **benchmarks**.

## Limitations

**Growth** **kinetics** **coupling** to **Wulff** **shapes** depends on **supersaturation**, **temperature**, and **carrier gas** details that appear in the **full** **MSE B** article; this **proof** ingest does not duplicate those **tables**. If you need **parameter** tables for the **Mo/Se/H** fit, open the **journal SI** attached to the VOR rather than relying on any **proof** copy. **Proof** files may show **layout queries** and **low-resolution** images. **Citations** should not use galley **page numbers**.

**Confidence rationale:** `med`—proof duplicate with delegated science.

## Citations and evidence anchors

Elsevier **ScienceDirect** provides the **version-of-record** PDF, **recommended** citation snippet, and **supplementary** downloads for DOI `10.1016/j.mseb.2021.115263`; use that portal when reconciling **page** numbers against any **proof** file in `papers/`.

## Reader notes (navigation)

The **MoSe₂** **ReaxFF** line also intersects **MOCVD** **gas-phase** modeling (**[[2019xuan-journal-of-c-multi-scale-modeling]]**) and **WS₂** **microscopy** studies—cross-link those pages when curating **2DCC**-related **benchmarks**.

- **Canonical article:** [[2021nayir-materials-sc-theoretical-modeling]]
- [[theme-2d-epitaxy-growth]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2021nayir-materials-sc-theoretical-modeling]]
- [[reaxff-family]]
