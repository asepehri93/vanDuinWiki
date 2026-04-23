---
id: paper:2018judith-a-harrison-applied-phys-review-force
type: paper
title: "Review of force fields and intermolecular potentials used in atomistic computational materials research"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:classical-ff-specialized
  - domain:methods-software
  - domain:reactive-md
  - domain:reaxff-lineage
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:classical-ff
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1063/1.5020808"
year: 2018
authors:
  - "Judith A. Harrison, J. David Schall, Sabina Maskey, Paul T. Mikulski, M. Todd Knippenberg, Brian H. Morrow"
venue: "Applied Physics Reviews 2018.5:031104"
pdf_sha256: "5cf16a61dbb01700e2624f388263bfcdee88910f5855830a28825978950c0c8a"
pdf_path: "papers/ReaxFF_others/Harrison_review_APL_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018judith-a-harrison-applied-phys-review-force -->

## Summary

Atomistic materials modeling relies on a zoo of interatomic potentials ranging from pairwise Lennard-Jones liquids to chemically reactive bond-order models and, increasingly, machine-learned surfaces fit to electronic-structure data. This *Applied Physics Reviews* survey organizes analytic potentials by functional complexity, typical accuracy envelopes, and computational cost, with dedicated coverage of classical fixed-charge force fields (AMBER, CHARMM, OPLS-AA, GROMOS, TraPPE), polarizable and embedded approaches, empirical metal potentials (EAM/MEAM), carbon and hydrocarbon bond-order models (REBO, AIREBO, COMB, qAIREBO), ReaxFF-style reactive chemistry, and machine-learning potentials that interpolate quantum energies. The pedagogical goal is to help practitioners match models to phenomena—mechanical properties, transport, chemistry at interfaces—without overfitting complexity where simpler models suffice.

## Methods

**Reviews and perspectives (non-simulation primary data).** This *Applied Physics Reviews* entry is a **survey**, not a single-system **benchmark** trajectory study. Its **Methods** are the authors’ **literature scope** and **taxonomy**: they organize **interatomic potentials** for **atomistic materials** modeling using **equations** and **primary citations** rather than prescribing one **MD** protocol for readers to reproduce wholesale.

**Coverage.** The review surveys **fixed-charge** biomolecular/organic fields (**AMBER**, **CHARMM**, **OPLS-AA**, **GROMOS**, **TraPPE**); **polarizable** and **embedded-atom** approaches; **EAM/MEAM** metals; **carbon/hydrocarbon** bond-order models (**REBO**, **AIREBO**, **COMB**, **qAIREBO**); **ReaxFF**-class **reactive** chemistry; and **machine-learning** potentials fit to **electronic-structure** data.

**How to use this page.** Map a **phenomenon** (mechanics, transport, **interface** chemistry) to an appropriate **potential family** using the review’s section headings, then follow **primary** literature for **parameters** and **validation**—do not treat this survey as a substitute for **system-specific** **ReaxFF** or **classical** **benchmarks** in the van Duin corpus.

**Literature comparison protocol.** Subsections cite **benchmark** studies where **experiment** or **high-level** **QM** disagrees with inexpensive **FF** choices, highlighting when **ReaxFF** or **ML** potentials are preferable to fixed-bond models for **oxidation** or **fracture** problems.

**MD / DFT production blocks.** **N/A —** the article does not center on one **LAMMPS**/**VASP** **timestep**, **ensemble**, or **production** **nanosecond** trajectory; per **AGENTS.md**, those slots are **not applicable** as a single numbered protocol here.

## Findings

Across categories, the review stresses that accuracy, transferability, and simulation speed form a triangle of competing objectives: richly parameterized nonreactive fields can improve thermodynamic fits for specific phases but may fail outside training manifolds, whereas bond-order reactive models encode chemistry at the cost of more elaborate functional forms and parameter training workflows. ReaxFF is positioned within the reactive bond-order lineage as a widely used option for bond formation and rupture in oxides, organics, and metals when quantum molecular dynamics is too expensive. Machine-learning sections emphasize promise and pitfalls—high accuracy near training distributions but careful data governance required for extrapolation.

**Sensitivity and outlook.** Practitioners must match **temperature**, **pressure**, and **phase** to the **FF** training manifold; **future work** in the review points to tighter **validation** loops as **ML** potentials proliferate.

**Corpus honesty.** This page summarizes the **Applied Physics Reviews** survey (`pdf_path`); it does not reproduce tabulated **benchmark** numbers from underlying **literature**.

## Limitations

Survey articles cannot replace application-specific validation; numerical comparisons are illustrative rather than exhaustive, and rapidly evolving ML potential literature may outdate specific benchmarks soon after publication.

## Relevance to group

The review gives external framing for where ReaxFF sits among empirical and machine-learned alternatives, supporting curriculum-style linking from the knowledge base to broader methods discourse.

## MAS / retrieval notes

Treat this entry as a methods survey rather than a single-system benchmark: cite the review’s internal section headings when users ask which potential class fits ceramics, polymers, or metals, and defer quantitative parameters to primary literature referenced there. Stable locator: DOI `10.1063/1.5020808`; page numbers should be copied from the *Applied Physics Reviews* PDF because pagination can differ across mirrors.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1063/1.5020808](https://doi.org/10.1063/1.5020808)

## Related topics

- [[reaxff-family]]
