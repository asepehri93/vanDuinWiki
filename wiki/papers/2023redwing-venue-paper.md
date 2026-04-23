---
id: paper:2023redwing-venue-paper
type: paper
title: "Supporting information: step-engineered MOCVD growth of WSe2 on sapphire (Nature Nanotechnology)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:methods-software
  - task:application
paper_keywords:
  - keyword:supporting-information
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1038/s41565-023-01456-6"
year: 2023
authors:
  - "Haoyue Zhu"
  - "Nadire Nayir"
  - "Tanushree H. Choudhury"
  - "Anushka Bansal"
  - "Benjamin Huet"
  - "Kunyan Zhang"
  - "Alexander A. Puretzky"
  - "Saiphaneendra Bachu"
  - "Krystal York"
  - "Thomas V. McKnight"
  - "Nicholas Trainor"
  - "Aaryan Oberoi"
  - "Ke Wang"
  - "Saptarshi Das"
  - "Robert A. Makin"
  - "Steven M. Durbin"
  - "Shengxi Huang"
  - "Nasim Alem"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
  - "Joan M. Redwing"
venue: "Nat. Nanotechnol. (Supporting Information)"
pdf_sha256: "c4604f7d07fe7bee2bdfd9874d4153d46954d1bf258d371c90eca836eaeb4016"
pdf_path: "papers/Zhu_Nayir_step_engineer_Nature_Nanotech_2023_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2023redwing-venue-paper -->

!!! note "Non-primary PDF"

    **Supporting Information** PDF for **Zhu *et al.*, *Nature Nanotechnology*** on **step-engineered MOCVD** growth of **WSe\(_2\)** on **miscut c-plane sapphire** (2DCC / Penn State network). The **article narrative, abstract, and main-text figures** are curated under **`[[2023zhu-nat-step-engineering]]`** (DOI **10.1038/s41565-023-01456-6**). This slug exists to register **SI bytes** and hashes for provenance.

## Summary

The SI package complements the parent **Nature Nanotechnology** paper with extended **sample metadata**, **crystallographic** orientation relations between **WSe\(_2\)** and **α-Al\(_2\)O\(_3\)**, **multi-step MOCVD** recipes, **temperature** and **orientation** studies, **kink-flow** growth imaging, **passivation** strategies, and appendices for **Raman**, **photoluminescence**, **field-effect transistors**, **second-harmonic generation**, and **transmission electron microscopy**. **DFT** supplementary results and movies referenced from the main text typically appear here. Qualitative scientific conclusions and experimental interpretation belong to the **VOR article**, not to this SI file alone.

Readers should treat this PDF as a **procedural and data appendix**: it exists so that growth recipes, extended micrographs, diffraction or orientation analyses, and supplementary device or spectroscopy plots can be inspected without cluttering the main article. For **MAS retrieval**, the stable scientific claims about **step-engineered** sapphire, **WSe\(_2\)** **domain** structure, and collaboration with **theory** (**van Duin**, **Crespi**, **Alem**) remain anchored on **`[[2023zhu-nat-step-engineering]]`**; this page records **hashes**, **file role**, and **cross-links** only.

## Methods

### Role (SI / supplemental ingest)

Extra **experimental** + **characterization** detail for **`[[2023zhu-nat-step-engineering]]`** (**MOCVD** **WSe\(_2\)** on **sapphire**).

### Protocol recovery

Follow **Methods**/captions on the **parent** wiki page, then **SI** for **precursor** flows, **P–T** tables, **hold times**, **miscut**, **TEM**/**Raman**/**FET** parameters.

### Theory settings in SI

**DFT** **supercells**, **k-mesh**, **functional**—match these for any downstream **ReaxFF**/continuum comparisons.

**N/A (owned LAMMPS/ReaxFF protocol on this SI-only page).** The **SI** is **appendix** material for **`[[2023zhu-nat-step-engineering]]`**; **N/A** here for a **full** **MOCVD+theory** **Methods** **narrative** or a **standalone** **RMD** **recipe**—use the **VOR** **article** **+** **SI** **for** **precursor** **flows**, **T**/**P** **tables**, **and** **any** **DFT** **settings** **the** **group** **published**. **N/A** for **E-field** **or** **metadynamics** **as** **new** **content** **in** this **SI-****ingest** **wiki** **(the** **parent** **owns** **simulation** **when** **present**).

## Findings

The SI provides **tables, extended figures, and procedural detail** backing the parent paper’s claims about **nucleation**, **domain orientation**, and **epitaxial** relationships on **step-engineered** substrates. It does not replace the main text for citing scientific conclusions in external publications.

In corpus terms, the **finding** of this ingest is **documentary**: the SI **substantiates** that the experimental group archived sufficient **metadata** and **extended characterization** to support peer review of a complex **MOCVD** + **microscopy** study. Operators should not treat isolated SI figures as standalone publications; instead, cite the **journal article** for interpretive statements and use the SI for **reproducing** growth conditions and **auditing** extended data panels.

## Limitations

**SI-only** ingest: always pair with **`[[2023zhu-nat-step-engineering]]`**. `extraction_quality: partial` reflects corpus profiling state for the SI PDF; operators may deepen section-level notes after full SI read-through.

## Relevance to group

**2DCC** / **Redwing** experimental materials with Penn State **theory** collaboration (**van Duin**, **Crespi**, **Alem**).

## Citations and evidence anchors

- Parent article: **`[[2023zhu-nat-step-engineering]]`** — **DOI** [10.1038/s41565-023-01456-6](https://doi.org/10.1038/s41565-023-01456-6).
**SI pairing.** Cross-reference section numbers and extended figures with `[[2023zhu-nat-step-engineering]]` (DOI 10.1038/s41565-023-01456-6); the SI does not stand alone for scholarly citation.

## Reproducibility and corpus locators

This note documents **where** to find primary evidence in-repo; it does **not** add new scientific claims beyond the cited publication.

**Normalized layer.** When present, `normalized/papers/{slug}.json` mirrors manifest hashes, bibliography fields, and extraction pointers; if `pdf_path` or PDF bytes change, follow `AGENTS.md` and `docs/PHASE3_RUNBOOK.md` to re-profile rather than editing PDFs in place.

**Authority chain.** For numerical settings (cutoffs, timesteps, ensembles, kinetics), use the peer-reviewed PDF (and publisher Supporting Information) as the authoritative source; this wiki summarizes for navigation and retrieval.

## Related topics

- [[theme-2d-epitaxy-growth]]
