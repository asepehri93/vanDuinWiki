---
id: paper:2015srinivasan-venue-research
type: paper
title: "Development of a ReaxFF Potential for Carbon Condensed Phases and Its Application to the Thermal Fragmentation of a Large Fullerene"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:thermal-decomposition
  - keyword:graphene-carbon
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/jp510274e"
year: 2015
authors:
  - "Sriram Goverapet Srinivasan"
  - "Adri C. T. van Duin"
  - "P. Ganesh"
venue: "J. Phys. Chem. A"
pdf_sha256: "17b695dbe00c42780e109bdb61a902db5480ac69bf11a59eec2909a2484e1adc"
pdf_path: "papers/Srinivasan_JPC_graphene_2015_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015srinivasan-venue-research -->

??? info "PDF variant"
    This slug points to an ACS **proof** PDF. The same scientific text appears in the journal-layout PDF on [[2015srinivasan-venue-jp-2014-10274e]] (`papers/Srinivasan_JPC_graphene_2015.pdf`).

## Summary

This article develops **ReaxFF C-2013** by reparametrizing the **ReaxFF CHO** carbon subset using **DFT** equations of state for **graphite** and **diamond**, formation energies of **graphene defects** and **amorphous** regions derived from **fullerenes**, and related benchmarks. The abstract reports that **ReaxFF C-2013** reproduces the **graphite atomization energy**, the **DFT graphite–diamond energy difference** and **graphite→diamond** barrier, and the **DFT Stone–Wales** barrier in **C₆₀(Ih)** via concerted **C₂** rotation. **MD** of **C₁₈₀** shows **exponential-in-time** fragmentation; an **Arrhenius** fit gives **7.66 eV** for **carbon loss**, with **C₂** elimination dominant and **larger fragments** increasingly probable at higher **temperature**. Motivation includes **coal pyrolysis**, **soot incandescence**, **graphitic nozzle erosion**, and **spacecraft ablation**.

## Methods

**Force-field training** follows the same **DFT → ReaxFF C-2013** protocol described on [[2015srinivasan-venue-jp-2014-10274e]]: **graphite/diamond EOS**, **graphene-defect** and **amorphous-carbon** formation energies tied to **fullerene** motifs, plus **Stone–Wales** and **phase** benchmarks (abstract).

**Static QM / DFT** uses that **DFT** database for **fit targets** and **post-fit** verification (abstract).

**MD application** applies **ReaxFF C-2013** in **NVT** **reactive MD** to a gas-phase **C₁₈₀** fullerene (**180** carbon **atoms**), scanning elevated **temperatures** for **Arrhenius** analysis of **fragmentation** rates (abstract). **Boundaries:** isolated gas-phase fullerene with vacuum padding or large-box **PBC** as defined in **Computational methods** on **`pdf_path`**. **Engine**, **timestep**, **thermostat**, and **production** trajectory **durations** (**ps**/**ns**) are tabulated on **`pdf_path`**; for pagination-sensitive citations prefer the journal-layout sibling **`[[2015srinivasan-venue-jp-2014-10274e]]`**. **Barostat / hydrostatic pressure:** **N/A**. **Electric field / enhanced sampling:** **N/A**.

## Findings

**Benchmarks:** **ReaxFF C-2013** reproduces the **DFT** targets quoted in the abstract for **graphite/diamond** thermochemistry and the **C₆₀ Stone–Wales** barrier.

**C₁₈₀ kinetics:** Fragmentation decay is **exponential** in time; an **Arrhenius** fit yields **7.66 eV** for **carbon loss**; **C₂** units dominate while **larger fragments** become more probable at higher **temperature** (abstract).

**Comparisons:** The introduction situates results within prior **experimental** and **simulation** literature on **fullerene** decomposition channels.

**Sensitivity:** **Temperature** controls which **fragmentation** channels dominate beyond simple **C₂** **shrink-wrap** pictures.

## Limitations

**Proof PDF** layout differs from the **version of record** and can shift pagination relative to [[2015srinivasan-venue-jp-2014-10274e]]. **ReaxFF** accuracy remains case-dependent outside the **fitted** carbon chemistry space.

## Relevance to group

Penn State and ORNL collaboration on **carbon ReaxFF** and **high-temperature fullerene fragmentation**.

## Reader notes (navigation)

- Typeset duplicate: [[2015srinivasan-venue-jp-2014-10274e]]
- [[theme-pyrolysis-combustion-organics]]
- [[reaxff-family]]

## Citations and evidence anchors

- DOI: [10.1021/jp510274e](https://doi.org/10.1021/jp510274e); `papers/Srinivasan_JPC_graphene_2015_proof.pdf`.
- `normalized/extracts/2015srinivasan-venue-research_p1-2.txt` (abstract; proof layout).
