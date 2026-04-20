---
id: paper:2018overbury-j-am-chem-so-complexity-intercalation
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
pdf_sha256: "42a24a3169f9736e5dc3ada97a96845d147a3b086dba228ea57d75cff07c3f8d"
pdf_path: "papers/Overbury_JACS_2018.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2018overbury-j-am-chem-so-complexity-intercalation -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This **JACS** article combines **inelastic neutron scattering**, **infrared spectroscopy**, and **ReaxFF reactive molecular dynamics** to study **urea** in **Ti₃C₂Tₓ MXene** interlayers. The central experimental conclusion is that **urea is chemically destabilized** under conditions relevant to intercalation, producing **fragments such as ammonium** (seen with INS) and **CO₂** (IR), rather than behaving as a passive intercalated molecule. **ReaxFF** simulations are used to propose **atomistic pathways and energetics** consistent with the measurements, highlighting how **guest chemistry** in **MXene galleries** can diverge from naive “insert a molecule” pictures—important for **electrochemical storage**, **sensing**, and **water-related** uses of MXenes.

## Methods

- **INS** and **IR** measurements with reference materials to interpret **vibrational** signatures of intercalated species.
- **ReaxFF MD** for **reactive pathways** involving **urea**, **water**, and **MXene surface terminations**.

## Findings

- **Urea decomposition** upon interaction/intercalation with **Ti₃C₂Tₓ** is supported by **spectroscopic** evidence and interpreted with **atomistic** models.
- **Ammonium-like** species appear as a **stable intercalation product** in the experimental INS comparison framework described in the paper.
- **Reactive MD** links **microscopic events** (bond breaking, proton transfer, decarboxylation channels as analyzed in the article) to **macroscopic observables**.


## Limitations

- **Termination disorder** and **water activity** strongly affect interlayer chemistry; quantitative rates may depend on **sample-specific** details.
- **Force-field** accuracy for **N–C–O** chemistry next to **Ti–C–O/H** motifs should be checked when extending to **other MXenes** or **electrochemical potentials**.

## Relevance to group

Coauthored by **Adri C. T. van Duin**; demonstrates **ReaxFF** as a partner tool to **neutron spectroscopy** on **2D energy materials**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/jacs.8b05913` (`papers/Overbury_JACS_2018.pdf`).

## Related topics

- [[reaxff-family]]