---
id: paper:2020hyunguk-kwon-j-phys-chem-jp0c03355
type: paper
title: "Reactive Molecular Dynamics Simulations and Quantum Chemistry Calculations To Investigate Soot-Relevant Reaction Pathways for Hexylamine Isomers"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - method:dft-static
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.0c03355"
year: 2020
authors:
  - "Hyunguk Kwon"
  - "Brian D. Etz"
  - "Matthew J. Montgomery"
  - "Richard Messerly"
  - "Sharmin Shabnam"
  - "Shubham Vyas"
  - "Adri C. T. van Duin"
  - "Charles S. McEnally"
  - "Lisa D. Pfefferle"
  - "Seonah Kim"
  - "Yuan Xuan"
venue: "J. Phys. Chem. A 124:4290-4304 (2020)"
pdf_sha256: "c63e9df678f8aec7347345bbd4ca7942cc3f0a2f1d70033b96fe7c83bdfbd7e9"
pdf_path: "papers/Kwon_JPC_2020_Soot_growth.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:qm-training-data
  - keyword:validation-experiment
---

<!-- id:paper:2020hyunguk-kwon-j-phys-chem-jp0c03355 -->

## Summary

Recent yield sooting index (YSI) experiments for nitrogen-containing hydrocarbons provide a quantitative ordering of particulate tendency in doped methane/air diffusion flames, but detailed elementary pathways for larger amines are often incomplete in kinetic models. Building on those YSI measurements, this work studies three C6H15N isomeric amines—dipropylamine (DPA), diisopropylamine (DIPA), and 3,3-dimethylbutylamine (DMBA)—with ReaxFF MD at 1400, 1600, and 1800 K (temperatures where soot formation is identified in the YSI experiment) plus quantum-mechanical refinement of reaction networks. The reactive trajectories use a methane-rich radical-pool framework in which test fuel molecules interact with radicals and intermediates generated from rich methane combustion, as described in the article, so the chemistry is explicitly embedded in a co-combustion context rather than isolated gas-phase pyrolysis of a single amine. ReaxFF ranks reactivity DIPA > DPA > DMBA across those temperatures. Major nonaromatic soot precursors differ by isomer (C2H4-, C3H6-, and C4H8-type product families in the authors’ classification); combined ReaxFF and QM sooting tendency order matches experimental YSI trends, and the authors highlight agreement between the two theoretical methods on reactivity, major intermediates, and major nonaromatic precursors.

## Methods

**1 — MD application (ReaxFF).** **ReaxFF** **NVT** molecular dynamics in **LAMMPS** on **C\(_6\)H\(_{15}\)N** isomers (**dipropylamine** DPA, **diisopropylamine** DIPA, **3,3-dimethylbutylamine** DMBA) at **1400, 1600, and 1800 K** within a **methane-rich radical-pool** setup (species definitions and **supercell** construction in the article). **NVT** uses a **thermostat** to hold each target **temperature**; **N/A — NPT** / **barostat** in the main production MD; **N/A — electric field**; **N/A — umbrella** or **metadynamics** (standard ReaxFF MD). **PBC**; **femtosecond** **timestep**; **ns**-scale or long **ps** **production** per article. **Hydrostatic** **GPa** **pressure**: **N/A** in typical **NVT** **gas**-like **boxes**.

**3 — Static QM (DFT).** **DFT** refines **reaction pathways** and **barriers/energetics** for key intermediates after ReaxFF screening (functional, basis, and **NEB**/path details per paper).

**FF training — N/A —** application paper using an **existing** ReaxFF training for hydrocarbon/amine–type chemistry, not a new public parameter fit documented as the main result here.

## Findings

**ReaxFF** ranks **relative reactivity** as **DIPA > DPA > DMBA** across the temperatures sampled. **Major nonaromatic soot precursors** differ by isomer (families involving **C\(_2\)H\(_4\)**, **C\(_3\)H\(_6\)**, **C\(_4\)H\(_8\)**-type products in the authors’ classification). Combined **ReaxFF** and **QM** trends for **sooting propensity** align with the **YSI** ordering reported experimentally for these amines.

## Limitations

Isomer subset only; nitrogen chemistry under real flame conditions is richer than the modeled gas-phase subset. **Exact** **barriers** and **reaction** **graphs** are in the **JCP** **text** and **SI**; this page **paraphrases** the **publication** only.

## Relevance to group

Penn State combustion collaboration tying ReaxFF to biomimetic/bio-derived fuel nitrogen chemistry and YSI metrics.

## Citations and evidence anchors

`papers/Kwon_JPC_2020_Soot_growth.pdf` — abstract (fuels, temperatures, reactivity order, precursor species). https://doi.org/10.1021/acs.jpca.0c03355

## Reader notes (navigation)

- Combustion/soot context: [[theme-pyrolysis-combustion-organics]]; related Penn State work: [[2019kwon-fuel-correct-numerical-simulations]].

## Related topics

- [[2019kwon-fuel-correct-numerical-simulations]]
- [[reaxff-family]]
