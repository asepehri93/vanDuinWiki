---
id: paper:2014vendelbo-nat-visualization-oscillatory
type: paper
title: "Visualization of oscillatory behaviour of Pt nanoparticles catalysing CO oxidation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - method:dft-static
  - method:continuum-or-mesoscale
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:catalysis-surface
  - keyword:combustion
  - keyword:validation-experiment
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1038/nmat4033"
year: 2014
authors:
  - "S. B. Vendelbo"
  - "C. F. Elkjaer"
  - "H. Falsig"
  - "I. Puspitasari"
  - "P. Dona"
  - "L. Mele"
  - "B. Morana"
  - "B. J. Nelissen"
  - "R. van Rijn"
  - "J. F. Creemer"
  - "P. J. Kooyman"
  - "S. Helveg"
venue: "Nat. Mater."
pdf_sha256: "efaefa8f6d66e88cb22d6304cc0a0d299f264fba9c620d0eddc5f9d40fe26566"
pdf_path: "papers/Others/Vendelbo_nmat_2014_Pt_oscillation.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014vendelbo-nat-visualization-oscillatory -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present), not this page alone.

## Summary

**Operando** **electron microscopy** in a **MEMS nanoreactor** at near **1 bar** and **relevant temperatures** ties **time-resolved** **CO oxidation** **turnover** oscillations on **Pt** **nanoparticles** to **periodic** **particle** **refacetting**. **Mass spectrometry** and **calorimetry** alongside **HR-TEM** show that **conversion** swings co-vary with **facet** rearrangements: higher conversion associates with more **close-packed** terminations and lower conversion with more **stepped** / **high-index** character (as summarized in the article). **DFT** plus **transport-aware** modeling argues that **refacetting** is needed to explain the oscillations beyond **adsorbate** / **kinetic** bistability alone.

## Methods

**Local sources:** the PDF at `papers/Others/Vendelbo_nmat_2014_Pt_oscillation.pdf` is present in this workspace and is the primary reading copy. No `normalized/extracts/2014vendelbo-nat-visualization-oscillatory_*.txt` file is in this clone; the protocol below is taken from the **PDF** (DOI **10.1038/nmat4033**, *Nat. Mater.* **13**, 889–893 (2014)).

The study uses a **MEMS nanoreactor** with a **unidirectional gas channel**, a **heated reaction zone** at **\(\sim\)1 bar** and **temperatures** representative of **automotive exhaust catalysis**, and **electron-transparent windows** for **high-resolution TEM** of **Pt** nanoparticles supported on the window. **Steady-state gas-flow simulations** of **CO** partial pressure inside the reactor (Fig. 1d–e, Supplementary material) use inlet compositions stated as **1.0 bar** total of **CO/O\(_2\)/He** at **4.2% / 21.0% / 74.8%** with geometry from Supplementary Tables 1–2. **Time-resolved** measurements couple **HR-TEM** of **particle** **shape/facets**, **mass spectrometry** of the **effluent**, and **reaction calorimetry**. **DFT** supplies **site-dependent** **CO** **adsorption** and **oxidation** inputs, combined with **mass-transport** calculations, to test whether **kinetic bistability** plus **transport** suffices or **facet refacetting** must be included.

**Static QM / DFT (supporting calculations).** **DFT** supplies **site-dependent** **CO** adsorption/oxidation inputs combined with **mass-transport** modeling to test whether **kinetic bistability** plus **transport** alone can explain oscillations versus requiring **facet refacetting**. Full **functional**, **dispersion**, **basis**/**plane-wave** settings, **k-mesh** choices, slab models, and energy tables are **N/A** on this wiki page—see **`papers/Others/Vendelbo_nmat_2014_Pt_oscillation.pdf`** and **Supplementary Information**.

**MD application.** **N/A**: the paper is not an atomistic **MD** methods study; “dynamics” here are **experimental** nanoparticle **refacetting** plus **continuum/transport** and **DFT**-informed modeling.

## Findings

The work demonstrates **time-resolved**, **operando** visualization of **CO oxidation** turnover **oscillations** on **Pt** nanoparticles while correlating **gas-phase** conversion with **particle-level** structural dynamics. The authors argue that **periodic refacetting**—cycling between **more close-packed** facet terminations at **higher** conversion and **more open/stepped** terminations at **lower** conversion—provides a **structural periodicity** aligned with the **rate oscillations**, supporting a picture where **nanoparticle** **morphology dynamics** can couple to **catalytic** bistability/oscillations in ways that differ from classical **extended single-crystal** **surface** oscillation scenarios.

Quantitative turnover/facet correlations, **DFT**/**transport** sensitivity tests, and discussion caveats are in **papers/Others/Vendelbo_nmat_2014_Pt_oscillation.pdf** and **SI**.

## Limitations

- **Electron-beam** effects and **near-atmospheric** **TEM** constraints still bound **quantitative** turnover interpretation; **DFT** covers **idealized** **facets** vs **real** **particle** **shapes**.

## Relevance to group

Demonstrates **in situ** **structure-activity** coupling for **oxidation catalysis**, complementary context to **ReaxFF** **surface** simulation papers that also target **dynamic** **oxide** / **metal** interfaces.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1038/nmat4033 - *Nat. Mater.* **13**, 889-893 (2014).

## Related topics

- [[reaxff-family]]
