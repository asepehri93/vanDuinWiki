---
id: paper:2025mirakhory-venue-paper
type: paper
title: "Iodine recombination in xenon solvent: Clusters in the gas to liquid-like state transition"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:dft-static
  - keyword:berendsen-thermostat
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1063/5.0260087"
year: 2025
authors:
  - "M. Mirakhory"
  - "A. Majumdar"
  - "M. Ihme"
  - "A. C. T. van Duin"
venue: "Journal of Chemical Physics"
pdf_sha256: "39ab0826cbfda6d8d79f5f9899fc7b6d8190872058b95b647d451b12f73a3530"
pdf_path: "papers/Mirakhory_XeI_JCP_2025_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2025mirakhory-venue-paper -->

!!! abstract

A Xe/I ReaxFF parameter set is trained on DFT, CCSD, and CASSCF reference data, then used in ReaxFF MD of supercritical xenon with iodine to connect xenon cluster lifetimes and thermodynamic state to iodine geminate recombination; Berendsen NVT controls with 1 fs (pure Xe) or 0.25 fs (iodine recombination) timesteps are reported, with ten replica simulations for averaging.

## Summary

The work targets **iodine recombination in xenon** across **gas-like, liquid-like, and supercritical** conditions, emphasizing **solvent clustering** and the **cage effect**. A **Xe/I ReaxFF** description is fit to quantum data (DFT surfaces for Xe–Xe, Xe–I, I₂ configurations; **CCSD** for Xe–Xe; **CASSCF** for I–I where DFT underbinds; **Gaussian 16** and **ADF/AMS** for specific scans). Reactive MD then probes **xenon cluster** statistics and **iodine recombination** under **NVT** (and variants with multiple thermostats) versus brief **NVE** discussion.

## Methods

### Quantum training data

- **DFT:** **PBE** with **def2-TZVP** and **Grimme D2** dispersion for most dimers; **CCSD** (DGDZVP) for **Xe–Xe**; **CASSCF(6,8)** for **I–I**; additional **PBE/TZP** scans in **ADF/AMS** for I–I–I angles. **Non-periodic** cluster calculations.
- **ReaxFF optimization:** Single-parameter search minimizing weighted squared error between QM energies and ReaxFF (Eq. (2) in the paper).

### ReaxFF MD protocols

**Integration** uses **LAMMPS** as the **molecular** **dynamics** **engine** for the **published** **protocol** (see **JCP** **Methods** for **verbatim** **commands**).

- **Pure xenon validation:** Energy-minimized boxes; sizes **500–10 000 atoms**; states spanning **liquid, supercritical, gas** (**~202.6–636.6 K**, **~58.98–102 bar** in the reported table). **NVT** with **Berendsen** thermostat (**damping 1000 fs**); **1 fs** timestep; **1 ns** duration for solvent characterization. **3D** **PBC** **cubic** **supercells** for the **Xe** **boxes** in these validation runs.
- **Iodine recombination:** **I : Xe ≈ 1 : 40**; **NVT** with **Berendsen** (**1000 fs** damping) or **multi-thermostat NVT** (**Xe** damping **1000 fs**, **I** damping **1×10⁶ fs**). **0.25 fs** timestep; **1 ns** per run; **10** independent replicas **ensemble-averaged**. **N/A** — **NPT** **barostat** in the production runs summarized (constant-volume **NVT** for these cells). **N/A** — external **electric** **field**; **N/A** — **metadynamics** (not the focus of the **reactive** **MD** protocol described here).

## Findings

- **Clusters:** **Xe cluster lifetimes** on the order of **~5–11 ps** are **comparable to** iodine **geminate recombination** timescales in the analysis.
- **Recombination:** Simulations report **higher probability of I₂ formation when xenon clusters** are present, and that **supercritical** conditions show the **highest recombination rate** among the states highlighted in the abstract and discussion. The **AIP** **galley** `pdf_path` should be cross-checked against the **VOR** **JCP** **PDF** for any **page**-level differences.

## Limitations

The corpus PDF is an **AIP author proof** (query form, placeholder page numbers in the header). Software branding for the MD engine is **not** stated explicitly in the extracted text.

## Relevance to group

**A. C. T. van Duin** is a co-author; the paper is **ReaxFF parameterization** for **Xe/I** reactive solvent chemistry.

## Citations and evidence anchors

- DOI: `10.1063/5.0260087` — *J. Chem. Phys.* (galley PDF in corpus).

## Related topics

- [[reaxff-family]]
