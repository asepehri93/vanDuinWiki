---
id: paper:2009liang-venue-paper
type: paper
title: "Parametrization of a reactive many-body potential for Mo–S systems"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reactive-md
  - keyword:tribology
  - keyword:2d-materials
  - keyword:classical-ff
  - keyword:dft-static
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - material:tmd
  - method:reactive-md-generic
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.79.245110"
year: 2009
authors:
  - "Tao Liang"
  - "Simon R. Phillpot"
  - "Susan B. Sinnott"
venue: "Physical Review B 79, 245110 (2009)"
pdf_sha256: "b92e0963952f0e241556dd26c816046abcda8f79c54567df1aca260c6e1beae5"
pdf_path: "papers/Others/Liang_MoS2_PRB_2009.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2009liang-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    This page summarizes the **Phys. Rev. B** article by `doi`. The potential is **second-generation REBO-style**, not ReaxFF.

## Summary

The authors introduce a **reactive many-body Mo–S potential** using the **second-generation reactive empirical bond-order** formalism, augmenting the bond-order term with a **coordination-dependent** analytic function. Fitting uses weighted nonlinear least squares with curated training sets (functions, databases, initial guesses, residual weights). The abstract reports agreement for **Mo clusters**, **2D Mo**, **3D Mo crystals**, **small S molecules**, and **binary Mo–S crystals**, and demonstrates **friction between MoS\(_2\) layers** consistent with prior **DFT** static surface calculations.

## Methods


The potential follows the **second-generation reactive empirical bond-order (REBO)** formalism for **Mo–S**: a parametrized **bond-order** factor multiplies pairwise interactions, augmented by an **analytic coordination-dependent function** on the bond-order term to capture how **coordination** modulates **binding energy**. **Lennard–Jones** terms are included for **van der Waals** interactions between **S–Mo–S trilayers** as developed in the paper. Parameters are obtained by **weighted nonlinear least squares** with explicit control of **analytic forms**, **training databases**, **initial guesses**, and **residual weights** (the four fitting levers highlighted in the abstract).

**1 — MD application (friction showcase).** After fitting, the authors illustrate the potential with **molecular dynamics** of **friction between MoS\(_2\)** layers (**Section III** in the PRB article). **N/A —** MD **engine**, **ensemble**, **timestep**, **thermostat/barostat**, **temperature**, **normal load**, **shear rate**, **system sizes**, and **PBC** details are **not stated** in `normalized/extracts/2009liang-venue-paper_p1-2.txt`—use **`pdf_path`** for executable protocol text.

**2 — Force-field training.** **Parent / form:** second-generation **REBO-class** Mo–S potential with explicit **coordination function** on bond order plus **LJ** interlayer vdW. **QM reference:** the abstract states agreement with **DFT** for the authors’ **prior static potential-energy surfaces** used to contextualize the friction MD; **N/A —** full DFT code/functional/basis/\(k\)-mesh listing from the short excerpt alone. **Training set:** **Mo** clusters, **2D Mo**, **3D Mo crystals**, **small S molecules**, and **binary Mo–S crystals** (abstract). **Optimization:** **weighted nonlinear least squares** with the four levers above. **Reference data:** **QM/DFT** and structural/energetic targets as described in the paper beyond the excerpt.

**Checklist closure (indexed pages).** **System / composition:** **MoS\(_2\)** **sliding** **surfaces** (binary **Mo–S** **composition**); per-cell **atom** counts: **N/A —** not stated in the short extract. **Ensemble:** **N/A — NVT**/**NPT**/**NVE** not stated on pp. 1–2. **Duration / stages:** **N/A — production** run lengths not stated on pp. 1–2. **Pressure:** **N/A — pressure** / normal load for the friction MD not stated in the excerpt.

## Findings

**Fitting performance.** The fitted potential is reported to yield **good agreement** with **structures and energetics** for **Mo** clusters, **2D Mo**, **3D Mo crystals**, **small sulfur molecules**, and **binary Mo–S crystals** in the training set enumerated in the abstract.

**Application: MoS\(_2\) friction MD.** **Shearing** **MoS\(_2\)** **layers** with the new potential produces **friction** results described as **consistent with** the authors’ **previous static DFT potential-energy surfaces**, motivating reactive MD at scales **ab initio MD** cannot reach (as claimed in the abstract).

**Comparisons.** The indexed excerpt emphasizes **comparison to the authors’ own prior DFT surfaces** for the friction illustration; broader **experimental** tribology benchmarks are **N/A —** not summarized on the indexed pages.

**Corpus honesty.** `extraction_quality` is **partial**; numerical friction traces, contact geometry, and sensitivity studies are in **`pdf_path`**, not the short extract.

## Limitations

REBO differs from ReaxFF in functional form and fitting philosophy; parameters are not transferable between frameworks without retraining. `extraction_quality` is **partial**; final parameter tables and benchmarks live in the PDF.

## Relevance to group

Methodological neighbor: **reactive bond-order MD** for **TMD tribology**—useful contrast case when scoping **ReaxFF** applications to sulfide/metal-oxide chemistry.

## Citations and evidence anchors

- DOI: `10.1103/PhysRevB.79.245110`.
- PDF: `papers/Others/Liang_MoS2_PRB_2009.pdf`.
- Extract: `normalized/extracts/2009liang-venue-paper_p1-2.txt`.

## Related topics

- [[material:tmd]]
- [[themes-index]]
