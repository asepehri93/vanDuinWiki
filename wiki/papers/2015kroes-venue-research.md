---
id: paper:2015kroes-venue-research
type: paper
title: "Atom vacancies on a carbon nanotube: to what extent can we simulate their effects?"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:carbon-hydrocarbon
  - method:reaxff
  - method:dft-static
  - task:validation
  - material:graphene-carbon-nano
  - scale:atomistic
source_refs: []
doi: "10.1021/acs.jctc.5b00292"
year: 2015
authors:
  - "Jaap M. H. Kroes"
  - "Fabio Pietrucci"
  - "Adri C. T. van Duin"
  - "Wanda Andreoni"
venue: "Journal of Chemical Theory and Computation (see DOI; ASAP header in extract)"
pdf_sha256: "660d367b29ad38918cbf1afd9bf0533552ee1a069f8c19c7fc7fa976650c734c"
pdf_path: "papers/Kroes_JCTC_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015kroes-venue-research -->

??? info "Curators"
    Duplicate **ASAP** PDF lineage for the same **JCTC** article as [[2015kroes-venue-ct5b00292]]; cite that page for integrated protocol text if this proof/header layout is confusing.

## Summary

Kroes *et al.* benchmark **single- and double-vacancy** physics in a **(10,0) zigzag carbon nanotube** across **DFT** (PBE, BLYP, partial PBE0 repeats) and several **classical** potentials (**AIREBO**, **LCBOP**, **ReaxFF15**, **Tersoff**, with **REBO** mentioned for SI). Quantities compared include **formation energies**, **relaxed structures**, and **barriers** for **reconstruction**, **migration**, and **vacancy coalescence**. The abstract warns that **characterization of these processes differs markedly** across methods, motivating cautious use of classical carbon models when building **DFT-informed** parametrizations. **ReaxFF15** is highlighted as a modern reactive carbon parametrization included in the comparison suite.

## Methods

This **ASAP** PDF (`papers/Kroes_JCTC_2015.pdf`) is a second corpus upload of the same **JCTC** article as [[2015kroes-venue-ct5b00292]] (DOI `10.1021/acs.jctc.5b00292`). The manuscript’s **Methods** are unchanged: **spin-polarized** **plane-wave DFT** in **CPMD** with **PBE** and **BLYP** (selected **PBE0** checks), **Γ-only** sampling, and **classical** energy benchmarks on **(10,0)** zigzag **single-wall** **CNT** models with **single** and **double** vacancies using **AIREBO**, **LCBOPI**, **ReaxFF15**, **REBO** (mostly **SI**), and **Tersoff** (also largely **SI**), with **formation energies** referenced to the **carbon chemical potential** defined in the paper. **ReaxFF15** enters through **static** energies and **barriers** on the **small tetragonal PBC** supercells (**~359–598** atoms depending on defect), not long **finite-temperature ReaxFF MD**; the separate **~100,000-atom** **high-temperature AIREBO MD** plus **annealing** is only used to propose motifs that are then **relaxed** in **DFT**. **Finite-temperature NVT/NPT production for the small-cell ReaxFF15 benchmarks:** **N/A —** those rows are **static** energies and **barrier** workflows, not thermostatted **NVT** trajectories on the **(10,0)** defect cells. **Hydrostatic pressure targets during those static evaluations:** **N/A —** not reported as **NPT** **pressure** control for the **ReaxFF15** comparison path (see [[2015kroes-venue-ct5b00292]] for timestep/thermostat detail on the exploratory **AIREBO** scouting MD).

## Findings

- Some **long-ranged relaxations** require large cells for both **DFT** and **ReaxFF** in specific double-vacancy configurations described in the extract.
- The abstract warns that **barriers** and **reconstruction** sequences for **single-** and **double-vacancy** **CNT** defects are **not** consistent across **empirical** **carbon** models, so **ReaxFF**-trained **kinetic** **Monte Carlo** or **coarse** **models** must inherit this **uncertainty** unless re-parameterized against **QM** for the specific **defect** **class**.

## Limitations

- Benchmark scope is a **single chirality/diameter** nanotube; transferability of conclusions to **metallic** tubes or **wide** diameter regimes is not established here.
- ASAP header placeholders appear in the extract; use **DOI** for bibliographic certainty.
- **Curvature** **strain** in **small-diameter** **CNTs** can amplify **defect** **energies** relative to **planar** **graphene**; **kinetic** **models** calibrated here should be **re-tested** on **larger-diameter** **tubes** before **composite** **applications**.
- **Interstitial** **dopants** and **endohedral** **species** can pin **vacancies** differently than **pristine** **(10,0)** **supercells** modeled in the **JCTC** benchmark.

## Relevance to group

**Adri C. T. van Duin** co-authorship ties the benchmark to **ReaxFF carbon** quality control and cross-method uncertainty quantification important for downstream **reactive carbon** applications.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jctc.5b00292](https://doi.org/10.1021/acs.jctc.5b00292)

## Related topics

- [[reaxff-family]]
