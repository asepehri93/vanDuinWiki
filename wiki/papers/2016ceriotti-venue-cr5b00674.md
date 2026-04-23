---
id: paper:2016ceriotti-venue-cr5b00674
type: paper
title: "Nuclear quantum effects in water and aqueous systems: Experiment, theory, and current challenges"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:pimd
  - task:review
  - scale:atomistic
paper_keywords:
  - keyword:review-or-perspective
  - keyword:aimd
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemrev.5b00674"
year: 2016
authors:
  - "Michele Ceriotti"
  - "Wei Fang"
  - "Peter G. Kusalik"
  - "Ross H. McKenzie"
  - "Angelos Michaelides"
  - "Miguel A. Morales"
  - "Thomas E. Markland"
venue: "Chem. Rev."
pdf_sha256: "0472052f9b34e0548be4a4b0ddc872e694d376b5f47e45bc0f94da37284833cd"
pdf_path: "papers/Others/Ceriotti_PIMD_ChemRev_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016ceriotti-venue-cr5b00674 -->

## Summary

Liquid **water** is often simulated classically or with **ab initio molecular dynamics** treating nuclei as classical point particles, yet **nuclear quantum effects (NQEs)**—zero-point motion, tunneling, and isotope-dependent structure—can materially change structure, dynamics, and spectroscopy, especially for hydrogen-bonded networks. This **Chemical Reviews** article synthesizes **experiment**, **path-integral** simulation methodology, and **electronic-structure** advances to explain where NQEs matter for water and aqueous environments, and why apparent contradictions appear across observables. A central conceptual thread is the **principle of competing quantum effects**: different NQEs can partially cancel, producing small net isotope shifts in some properties even when individual contributions are large. The review also covers interfaces, solvation, and algorithmic developments that make **ab initio potentials on the fly** compatible with quantized nuclei in selected settings.

## Methods

This **Chemical Reviews** article is a **methods-and-literature survey**, not a single new simulation study.

### Literature scope and comparison protocol

The review organizes **experimental probes** (including **deep inelastic neutron scattering** and related techniques for proton momentum distributions) alongside **path-integral molecular dynamics / Monte Carlo**, **ring-polymer** instanton and contraction formulations, **Langevin**-type stochastic dynamics tricks used in some PIMD workflows, and **dynamics-oriented** extensions beyond purely static structural estimators. It maps these tools to **bulk water**, **ice**, **confined water**, and **solvated ions**, with pointers to benchmark studies and known failure modes of **classical-nuclei** models. **Barostat / controlled pressure:** **N/A —** not applicable to the review as a single simulation study. **External electric fields:** **N/A —** not a focus of this survey.

### MD application (atomistic dynamics)

**N/A — no single canonical production MD protocol** is defined for the review itself; MD settings appear only as **cited primary literature**.

### Force-field training

**N/A — not applicable** to the review as a standalone artifact.

### Static QM / DFT

**N/A as a unified “one paper” QM study**; individual cited works span many functionals and basis sets. Use the **original studies** referenced in the review when you need concrete **DFT/AIMD** parameters.

## Findings

NQEs are **not** a uniform “add zero-point energy” correction: they can dominate some spectroscopic signatures while leaving others nearly classical, depending on temperature, phase, and whether competing quantum contributions cancel. Modern path-integral algorithms and on-the-fly electronic structure have pushed fully quantum-nuclear simulations of water into regimes that were impractical a decade earlier, but **cost** and **potential-energy surface accuracy** remain limiting for large-scale reactive chemistry. The review’s value for practitioners is an annotated map of when to invest in **PIMD**-class methods versus when cheaper classical water models may suffice. Link this review when benchmarking **isotope effects** or **vibrational spectroscopy** of water near oxide interfaces, where classical MD can be misleading even if structure looks reasonable.

- **Comparisons:** The review synthesizes **experiment** vs **simulation** disagreements that motivated new **DINS**-class measurements and improved **PIMD** estimators; cite the underlying primary papers for any quantitative claim.
- **Sensitivity:** Observable-by-observable guidance depends strongly on **temperature**, **phase** (ice vs liquid vs confined), and whether the property probes **hydrogen-bond** symmetrization vs **diffusion**.
- **Limitations / outlook:** Even state-of-the-art **path-integral** workflows remain **expensive** when coupled to **DFT** forces; **future work** in the field trends toward better **contracted ring-polymer** methods and cheaper **machine-learned** potentials—still requiring careful validation at interfaces.
- **Corpus honesty:** This page is a **review** summary; do not treat it as a **PDF** substitute for equations, citations, or numerical benchmarks.

## Limitations

This entry summarizes a **review**, not primary data; quantitative benchmarks should be taken from the **original studies** cited within the review for the target observable. For **oxide–water** or electrolyte interfaces elsewhere in the corpus, use the review as a **decision guide** on when **PIMD**-class nuclear quantization matters versus when classical nuclei may suffice—the text stresses **competing quantum effects** (small net isotope shifts despite large underlying contributions), common failures of classical nuclei for **diffusion** and **vibrational** lineshapes, and the **cost** and **PES** accuracy limits of path-integral methods coupled to **on-the-fly** **DFT**.

## Relevance to group

Foundational context for **water interfaces**, quantization adjacent to classical and **ReaxFF** workflows used throughout the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.chemrev.5b00674](https://doi.org/10.1021/acs.chemrev.5b00674)

## Related topics

- [[theme-water-silica-geo]]
