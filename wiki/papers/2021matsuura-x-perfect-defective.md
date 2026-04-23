---
id: paper:2021matsuura-x-perfect-defective
type: paper
title: "Perfect and defective 13C-furan-derived nanothreads from modest-pressure synthesis analyzed by 13C NMR"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - material:graphene-carbon-nano
  - method:dft-static
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:validation-experiment
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/jacs.1c03671"
year: 2021
authors:
  - "Bryan Matsuura"
  - "Steven Huss"
  - "Zhaoxi Zheng"
  - "Shichen Yuan"
  - "Tao Wang"
  - "Bo Chen"
  - "John V. Badding"
  - "Dirk Trauner"
  - "Elizabeth Elacqua"
  - "Adri C. T. van Duin"
  - "Vincent H. Crespi"
  - "Klaus Schmidt-Rohr"
venue: "J. Am. Chem. Soc. (galley PDF in corpus; confirm VOR pagination)"
pdf_sha256: "ca7303180162f36a61e1fefcc3295d491018da92796cd5ee9dd80ed7d2202027"
pdf_path: "papers/Matsuura_C13furan_NMR_JACS_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021matsuura-x-perfect-defective -->

## Summary

Solid-state **\(^{13}\)C NMR** (including 2D \(^{13}\)C–\(^{13}\)C and \(^1\)H–\(^{13}\)C correlation, spectral editing, CODEX/rotational-echo techniques) characterizes nanothreads obtained by compressing **\(^{13}\)C\(_4\)-labeled furan**. Quantitative bonding statistics show overwhelmingly CH environments, minor CH\(_2\)/C=O/CH\(_3\) defects, trapped furan, and distinct **anti** vs **syn**-thread motifs; highly ordered saturated segments exhibit unusually slow spin exchange, implying extended regular segments (**≥14** bonds). **Quantum-chemical shift calculations** match experimental \(^{13}\)C shifts for **anti**-thread models better than competing complex syn/anti hybrids, supporting anti connectivity as the dominant ordered backbone. The study is primarily **experimental** **NMR** plus **quantum chemistry**, with **van Duin** listed among **computational** contributors for **shift** **assignment** support.

## Methods

This is an **experimental solid-state NMR** study of nanothreads from compressed **\(^{13}\)C\(_4\)-labeled furan**, with **quantum-chemical shift calculations** used to interpret \(^{13}\)C chemical-shift tensors. **MD / reactive MD — N/A** — not used.

**Synthesis and experiments.** The Experimental Section describes slow compression polymerization of labeled furan to a solid nanothread product. Multinuclear **\(^{13}\)C NMR** (including 2D \(^{13}\)C–\(^{13}\)C and \(^1\)H–\(^{13}\)C correlation, spectral editing, CODEX/rotational-echo based methods) characterizes bonding statistics, domain sizes via spin exchange, and dynamics (e.g. T\(_1\), partial inversion recovery to highlight “perfect” segments).

**Static QM / DFT (for NMR assignment).** The article uses **DFT**-based **NMR chemical-shift** methods (GIAO or equivalent) on candidate **anti** vs **syn** thread segment models, compared to measured \(^{13}\)C tensors. **Functional and dispersion** — see article and **Supporting Information** for the exact functional, dispersion treatment (if any), and **basis set**; this wiki note does not duplicate SI tables. **k-sampling:** for periodic DFT cell models, the SI lists **k-point** / **k-mesh** (or **Γ-only**) choices as appropriate to the supercell; **N/A in p1–2** to restate the mesh. **Structures / pathways:** models of **anti** vs **syn** connectivity and related segment geometries underpin shift assignment; this is not a gas-phase reaction-path study. **Properties:** computed **NMR** **shielding** tensors, **chemical** **shift** **tensors**, and **total energy** / **electronic energy** differences between candidate models, plus **NMR**-related **frequency**-domain targets as tabulated, for comparison to experiment; numerical tables in **SI**.

## Findings

**Outcomes and mechanisms.** Quantitative bonding statistics from spectral editing show overwhelmingly **CH** environments, with minor CH\(_2\), C=O, and CH\(_3\) defects, residual furan, and distinct **anti** vs **syn**-thread motifs. Highly ordered saturated segments show unusually slow inter-segment \(^{13}\)C spin exchange, consistent with long regular runs (the article discusses segment lengths on the order of many bonds).

**Comparisons.** **Quantum-chemical** shift calculations match experimental \(^{13}\)C data better for **anti**-thread models than for competing complex **syn**/**anti** hybrid scenarios, supporting **anti** connectivity as the dominant ordered backbone. CODEX-type analysis **rules out** a simple **syn**-tetrad picture with four distinct CH environments.

**Corpus / KB honesty.** The corpus `pdf_path` is a **galley** PDF; for final pagination, figure quality, and any post-galley corrections, use the **version-of-record** *J. Am. Chem. Soc.* article (DOI `10.1021/jacs.1c03671`).

## Limitations

Galley PDF in corpus; cite the journal version of record for final page numbers and any structure revisions. van Duin’s role is computational support alongside DFT/NMR interpretation (not ReaxFF MD in the abstract-level description). **Solid-state** **NMR** **assignments** can shift with **magic-angle** **settings**, **probe** **architectures**, and **sample** **hydration**—compare **experimental** **conditions** before drawing **structure** conclusions from **shift** matching alone. **Nanothread** **products** can be **heterogeneous** at **micron** **scales**; **bulk** **NMR** reports **ensemble** **averages** that may **hide** **minor** **phases**. **JACS** **SI** typically contains **full** **computational** **details** for **shift** **tensors** referenced in the main text. **Experimental** **synthesis** **logs** in **SI** also clarify **pressure** **schedules** that control **thread** **conversion** extent.

## Relevance to group

Carbon nanothread chemistry paper with **van Duin** as co-author on modeling support.

## Citations and evidence anchors

- JACS article DOI **10.1021/jacs.1c03671** — Abstract, Results, Supporting Information for computational detail.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
