---
id: paper:20180000-0002-5137-3961-x-complexity-intercalation
type: paper
title: "Complexity of Intercalation in MXenes: Destabilization of Urea by Two-Dimensional Titanium Carbide"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:batteries-electrochemistry
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jacs.8b05913"
year: 2018
authors:
  - "Steven H. Overbury"
  - "Alexander I. Kolesnikov"
  - "Gilbert M. Brown"
  - "Zhiyong Zhang"
  - "Gokul S. Nair"
  - "Robert L. Sacci"
  - "Roghayyeh Lotfi"
  - "Adri C. T. van Duin"
  - "Michael Naguib"
venue: "J. Am. Chem. Soc."
pdf_sha256: "5c684258b036f1d88a0b0bc2c32e44101fda2cbf3c251b761911259a052ad66a"
pdf_path: "papers/Overbury_JACS_2018_proof.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:20180000-0002-5137-3961-x-complexity-intercalation -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**One-paragraph summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## One-paragraph summary

This **Journal of the American Chemical Society** study probes **urea intercalation** in **Ti₃C₂Tₓ MXene** using **inelastic neutron scattering (INS)**, **infrared spectroscopy**, and **ReaxFF reactive molecular dynamics**. Experiments indicate that urea is not stable as intact intercalant under intercalation-relevant conditions: **decomposition** leads to species such as **ammonium** in the gallery, with **CO₂** evolution detectable spectroscopically. **ReaxFF MD** supplies **atomistic reaction pathways and energetics** consistent with the experimental picture, with implications for how **small-molecule intercalants** behave in **layered carbide MXenes** used in **energy storage** and related applications. The corpus PDF here is an **ACS author proof** variant of the same article also archived as `papers/Overbury_JACS_2018.pdf` (`paper:2018overbury-j-am-chem-so-complexity-intercalation`).

## Methods

- **INS** and **IR** on MXene samples with urea-related intercalation chemistry (see article for sample protocols and control comparisons).
- **ReaxFF reactive MD** to explore **decomposition pathways**, **interlayer species**, and **bonding** at the atomistic level.

## Findings

- **Urea** under intercalation conditions **decomposes** rather than persisting as a simple molecular guest; **INS** signatures support **intercalated ammonium**-type species after transformation.
- **CO₂** is observed **experimentally**, aligning with **oxidation / decomposition** channels discussed in the paper.
- **ReaxFF** simulations provide **mechanistic context** (pathways and relative energetics) for how **guest–MXene** interactions drive **chemical change** in the interlayer.

## Limitations

- **MXene termination** (mix of −OH, −F, oxo groups) sensitively affects chemistry; models must match the **synthetic history** of the sample.
- **ReaxFF** conclusions should be read alongside **QM benchmarks** for any **new bond-making/breaking** channels emphasized quantitatively.

## Relevance to group

**Adri C. T. van Duin** is a coauthor; the work is a flagship example of **ReaxFF** paired with **neutron and optical spectroscopy** on **MXene intercalation chemistry**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/jacs.8b05913` (see first pages of `papers/Overbury_JACS_2018_proof.pdf`).

## Related topics

- [[reaxff-family]]
