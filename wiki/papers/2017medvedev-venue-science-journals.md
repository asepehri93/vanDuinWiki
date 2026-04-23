---
id: paper:2017medvedev-venue-science-journals
type: paper
title: "Density functional theory is straying from the path toward the exact functional"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:dft-static
  - task:application
paper_keywords:
  - keyword:dft-static
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1126/science.aah5975"
year: 2017
authors:
  - "Michael G. Medvedev"
  - "Ivan S. Bushmarinov"
  - "Jianwei Sun"
  - "John P. Perdew"
  - "Konstantin A. Lyssenko"
venue: "Science"
pdf_sha256: "0bd64e1e4f112f1dad4791c1f43da4e591025b2ff209cb5dd8bc7b306e8dacb9"
pdf_path: "papers/Others/Medvedev et al. - 2017 - Density functional theory is straying from the pat.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017medvedev-venue-science-journals -->


!!! abstract
Atomic and cationic electron densities from 128 DFT exchange–correlation functionals are compared to CCSD-full references, showing historical density fidelity improved until the early 2000s and then worsened for some highly empirical modern functionals.

## Summary

This *Science* report benchmarks **128 DFT functionals** (Gaussian 09 and GAMESS-US keyword families plus hybrid combinations) against **CCSD-full** reference densities for selected **atoms and atomic cations** with nondegenerate ground states (Be⁰, B³⁺, B⁺, C⁴⁺, C²⁺, N⁵⁺, N³⁺, O⁶⁺, O⁴⁺, F⁷⁺, F⁵⁺, Ne⁸⁺, Ne⁶⁺, Ne⁰). Anions are excluded to avoid basis-set-dominated density errors. The study contrasts decades of energy-focused parametrization with fidelity of the **energy-minimizing density** to the exact density, plotting trends in density error vs time and comparing energy vs density error metrics. Meta-GGAs such as MS0/MS1/MS2/MVS/SCAN are included among tested rungs (LDA, GGA, meta-GGA, hybrid).

## Methods

**Force-field training / fitting.** **N/A —** this work benchmarks **exchange–correlation** **functionals** in **DFT**, not **classical** or **reactive** force fields.

**Molecular dynamics / sampling.** **N/A —** no **MD** or **AIMD** trajectories are central to the benchmark.

**Static QM / DFT.** The authors compare **energy-minimizing electron densities** from **128 historical and modern DFT functionals** (implemented in **Gaussian 09** revision **D.01** and **GAMESS-US** 2013 R1, including **hybrid** combinations) to **CCSD-full** reference densities for a set of **atoms and atomic cations** with **nondegenerate ground states** (**Be** through **Ne** in selected charge states; **anions** are excluded to reduce basis-set-dominated density errors). **Functional / rung coverage** spans **LDA**, **GGA**, **meta-GGA** (including **MS0/MS1/MS2/MVS/SCAN** among others), and **hybrid** functionals as reported in the article. **Dispersion corrections (DFT-D / vdW):** **N/A —** the *Science* summary does not restate per-functional **Grimme-style** dispersion settings on this page; see the paper and SI for software-specific keywords. **Basis sets and k-sampling:** **N/A —** these benchmarks are **atomic** **finite-system** calculations in **Gaussian**/**GAMESS** conventions rather than periodic **plane-wave** **k-mesh** studies; detailed basis choices appear in the publication. **Structures / pathways:** **N/A —** the focus is **self-consistent ground-state densities** on fixed **atomic** configurations, not **reaction pathways** or **solid-state** relaxations. **Properties computed** include **density** (and **density-derivative**) error metrics relative to **CCSD-full**, compared alongside **energy** errors, and trends vs **publication decade** and **functional rung**.

**Review / non-simulation framing.** **Primary** *Science* **Research Report** (**DOI 10.1126/science.aah5975**); it is **not** a broad narrative review of applications.

## Findings

**Outcomes and mechanisms.** For a long span of functional development, **approximate DFT densities** tracked **closer** to **CCSD-full** references as **energetic** performance improved—until roughly the **early 2000s**, after which some **highly flexible**, **empirically** tuned functionals can **worsen densities** while still fitting **energies**. The authors argue that **pure energy fitting** therefore does **not** guarantee movement toward the **exact functional**; faithful **densities** matter because the **exact** theory ties **energy** to the **exact density**.

**Comparisons.** Densities and energies are compared **across functionals** and against **CCSD-full** references; **experimental** data are not the primary comparator in this benchmark design.

**Sensitivity / design levers.** Trends are organized vs **time** (decade of introduction) and **Jacob’s-ladder-style** **rung** (LDA → hybrid), highlighting how **empirical flexibility** and **constraint-based** design philosophies correlate with **density fidelity**.

**Limitations and outlook (as authored).** The **atomic/cationic** test set **excludes anions** and does not address **condensed-phase** chemistry or **dynamics**; the conclusions concern **parametrization culture** and **benchmark design**, not every functional in every context.

**Corpus honesty.** This page summarizes the **indexed PDF**; use the **DOI-linked** article for **tables** and **SI** detail.

## Limitations

Atomic/cationic set excludes anions; focuses on ground-state densities, not condensed-phase chemistry or dynamics. The reported **historical trend** (density fidelity improving until the early 2000s, then worsening for some modern functionals) is a **benchmarking statement** about parametrization culture—not a blanket verdict on every functional in a given software release.

## Relevance to group

Provides QM context for judging when DFT training data or density fidelity matter for force-field fitting pipelines that use DFT references. When selecting **DFT** levels for **ReaxFF** training sets, treat **energy accuracy** and **density fidelity** as distinct criteria that do not always improve together across functional families.

## Citations and evidence anchors

- DOI: `10.1126/science.aah5975`

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- PDF filename in corpus reflects a downloaded HTML/Science wrapper; article content is the *Science* report above.
