---
id: paper:2020liu-venue-paper
type: paper
title: "Searching for correlations between vibrational spectral features and structural parameters of silicate glass network"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - material:silicate-glass
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:silica-silicate
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1111/jace.17036"
year: 2020
authors:
  - "Hongshen Liu"
  - "Seung Ho Hahn"
  - "Mengguo Ren"
  - "Mahadevan Thiruvillamalai"
  - "Timothy M. Gross"
  - "Jincheng Du"
  - "Adri C. T. van Duin"
  - "Seong H. Kim"
venue: "Journal of the American Ceramic Society (publisher author-query / proof PDF)"
pdf_sha256: "5bc396c9dc3d6eef8a042d7472b96162df9389e66bcfb2cf1d22f71c97dbba8c"
pdf_path: "papers/Liu_JAmCerSoc_2020_vibrations_glass_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2020liu-venue-paper -->

??? info "PDF role"
    Wiley **author query** PDF (`normalized/extracts/2020liu-venue-paper_p1-2.txt` is query forms). Article text: [[2020liu-journal-of-t-searching-correlations]].

## Summary

The galley PDF `papers/Liu_JAmCerSoc_2020_vibrations_glass_galley.pdf` is associated with the *Journal of the American Ceramic Society* article DOI `10.1111/jace.17036` comparing experimental infrared and Raman spectra of sodium silicate glasses with atomistic models using **Teter** (fixed partial charges), **MGFF** (diffuse charges), and **ReaxFF** potentials. The automated extract (`normalized/extracts/2020liu-venue-paper_p1-2.txt`) is an **Author Query Form** for manuscript **17036** in **JACE**, not the article body: it asks authors to return page-charge forms, confirm blue/vermilion given-name versus surname coloring, verify ORCIDs, define **FWHM**, harmonize phrasing around “sodium modifier ion” versus “sodium-modifier ion,” and complete or correct multiple references (including publisher details and missing volume data). The version-of-record page [[2020liu-journal-of-t-searching-correlations]] documents synthesis of glasses with composition [Na₂O]ₓ[Al₂O₃]₂[SiO₂]₉₋ₓ for x = 7, 12, 17, and 22 mol%, parallel MD at matching compositions, integration timesteps of **1.0 fs** for classical potentials and **0.25 fs** for ReaxFF, and the conclusion that ReaxFF best tracks composition-dependent infrared trends while several textbook spectral-assignment schemes disagree with ReaxFF structural statistics.

## Methods

**Corpus / PDF role.** The file at `pdf_path` is a **Wiley author-query / proof** style PDF; the useful **automation** **extract** is **administrative** text (see `normalized/extracts/2020liu-venue-paper_p1-2.txt`), **not** a **Methods** **section** for **science** **protocols**. **Reproducible** **reactive** and **classical** **molecular** **dynamics** ( **LAMMPS**; **PBC** **sodium** **aluminosilicate** **glass** **supercells**; **atom** **counts** **O(10⁴)** **scale**; **~300** **K** **target** **temperature** **(thermostat** **equilibration**); **1.0** **fs** or **0.25** **fs** **time** **steps**; **production** **windows** in **ps** / **ns**; **NVT**-**like** **constant**-**volume** **sampling** for **vibrational** **postprocessing**; **N/A** for **E**-**field**-**driven** **dynamics**; **N/A** for **umbrella** / **replica** / **metadynamics** in the **JACE** **line** of **this** **work**) is **documented** on **`[[2020liu-journal-of-t-searching-correlations]]`** with **VOR** **`papers/Liu_JAmCerSoc_2020_vibrations_glass.pdf`**. For this **slug** **only**: treat **all** **detailed** **NPT** / **barostat** / **1** **atm** **(bar)** **hydrostatic** **pressure** **(GPa** **or** **bar)**, and **tuning** of **rare**-**event** **(CVHD,** **hyperdynamics)**, as **N/A** **(query**-**form** **PDF** **only**; **if** the **VOR** **sibling** **lists** **NPT** **or** **pressure** **for** a **substep**, follow **that** **file**). **2 —** **de** **novo** **ReaxFF** **force**-**field** **fit** **in** this **Wiley** **ingest:** **N/A** **(see** **VOR**)**. **3 —** **static** **DFT**-**only** **as** the **result:** **N/A** **(see** **VOR** for any **DFT** **citations**).**

## Findings

The sibling page states that traditional correlations linking IR peak positions to Si–O–Si angles, Raman deconvolutions to Qₙ fractions, and low-frequency Raman bands to ring sizes are inconsistent with the ReaxFF-generated glass networks, motivating revised interpretations; detailed evidence and plots live there. The author-query extract for this slug confirms the local PDF path is unsuitable for extracting numerical spectroscopic results because it captures **copydesk questions** (for example, clarifying a sentence about vibrational techniques and glass composition) rather than data tables. That administrative content is useful for corpus governance—proving which workflow file was ingested—but it is not a substitute for the article body on [[2020liu-journal-of-t-searching-correlations]].

## Limitations

Author-query PDFs are poor primary sources; use the final article for all locators.

## Relevance to group

Penn State collaboration (van Duin, Kim, Liu, Hahn) on silicate spectroscopy and ReaxFF validation with Corning and UNT partners.

Benchmark questions that ask about “traditional silicate Raman assignments” should retrieve [[2020liu-journal-of-t-searching-correlations]] rather than this query PDF, because only the VOR article contains the full argumentation and plots testing those assignments against ReaxFF networks.

## Reader notes (navigation)

- [[2020liu-journal-of-t-searching-correlations]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: [10.1111/jace.17036](https://doi.org/10.1111/jace.17036)
