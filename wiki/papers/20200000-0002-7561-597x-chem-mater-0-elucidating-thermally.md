---
id: paper:20200000-0002-7561-597x-chem-mater-0-elucidating-thermally
type: paper
title: "Elucidating Thermally Induced Structural and Chemical Transformations in Kaolinite Using Reactive Molecular Dynamics Simulations and X-ray Scattering Measurements"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemmater.9b03929"
year: 2020
authors:
  - "Muraleedharan, Murali Gopal"
  - "Asgar, Hassnain"
  - "Mohammed, Sohaib"
  - "Gadikota, Greeshma"
  - "van Duin, Adri C. T."
venue: "Chem. Mater."
pdf_sha256: "b522c1c9dd9c1919e721ae7a155c3c6dfd563d5eb72f421390b7e9682ecba3ed"
pdf_path: "papers/Muraleedharan_ChemMat_2019_kaolinite_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20200000-0002-7561-597x-chem-mater-0-elucidating-thermally -->

!!! abstract "Scope"

Combined ReaxFF molecular dynamics, wide-angle X-ray scattering, and pair-distribution analysis of kaolinite heated from 298 K to 1673 K, linking dehydroxylation, metakaolin formation, and mullite crystallization to atomistic reaction pathways and heating-rate effects.

## Summary

Designing hierarchical oxide materials for extreme environments requires models that capture both atomic rearrangement and measurable scattering signatures. The study heats kaolinite across the dehydroxylation and sintering regimes, comparing ReaxFF-derived pair distribution functions and wide-angle features to in situ experiments, then interprets reaction sequences, intermediates, and barrier estimates from simulations under different heating protocols. Linking **atomistic** bond rearrangement to **diffraction-derived** pair correlations is presented as a practical validation loop for geoceramic processing scenarios where both chemistry and microstructure matter.

## Methods

**Reactive MD (ReaxFF).** Atomistic trajectories span **298–1673 K** following **dehydroxylation**, **Al** coordination evolution, and **high-temperature** chemistry toward **mullite**-forming regimes.

**Scattering validation.** Simulated **pair distribution functions (PDF)** and **wide-angle X-ray scattering (WAXS)** patterns are compared **quantitatively** to **in situ** measurements on **heated kaolinite** to validate **structural** intermediates.

**Heating-rate study.** Multiple **ramp** rates shift **apparent** **onset** temperatures for **dehydroxylation** and **sintering**, enabling a **kinetic** map of how **thermal history** moves **transition** temperatures while preserving the **same** **chemical** sequence in the **atomic** narrative.

**MD application (ReaxFF).** **LAMMPS**-style **ReaxFF** **RMD** on **periodic** **Al–Si–O**–**H** **kaolinite** **supercells** (order **~10^3+** **atoms**); **temperature** **ramps** span **298**–**1673 K** as in the *Chem. Mater.* text, with **multi-ns**-scale (and shorter **ps** sub-segments) trajectories for **heating** **protocols**; **N/A** for an exact **per-segment** **ps**/**ns** log on this page. **N/A —** **fs** **timestep**, **thermostat** implementation, and **NVT**/**NPT** breakdown are not transcribed here. **N/A —** **barostat**; **N/A —** **electric** field. **N/A —** **umbrella** and **replica** **exchange**.

**FF training (block 2).** **N/A** — applies a **clay** **Reaxff**; refit not the emphasis of the abstract-level summary.

**Static QM (block 3).** **N/A** — *ab initio* is not the central engine; **scattering** is **experimental**.

## Findings

**Dehydroxylation (298–873 K).** **Crystalline kaolinite** converts to **semicrystalline metakaolin** with **~90%** **tetrahedral Al** as reported.

**Sintering / mullite (~1055–1673 K).** **Metakaolin** undergoes **sintering** chemistry with **mullite** formation in the high-temperature window described in the article.

**Kinetics.** **Faster** heating moves **dehydroxylation** and **sintering** **onsets** to **lower** apparent **T** (**425 K** / **1055 K**) vs a **10× slower** ramp (**622 K** / **1100 K**) in the authors’ comparison.

**Simulation vs experiment.** Agreement is **strong** below **~1000 K**; **modest** differences appear at **higher T**, signaling limits of **force-field** coverage, **kinetics**, or **long-range** **order** formation in **MD** timescales. The authors summarize this as a **regime map** of where **PDF/WAXS** and **ReaxFF** agree on the **onset** of **atom-scale** reorganization, with **quantitative** match emphasized for **T < 1000 K** in the abstract narrative.

## Limitations

Long-range diffusion and nucleation of crystalline mullite may be incomplete within accessible MD timescales; experimental heating profiles in furnaces differ from simulated rate controls in detail. Where simulation and scattering diverge at the highest temperatures, operators should treat the disagreement as a cue to revisit **training-set coverage**, **finite-size** effects, and **kinetic** accessibility rather than as a single “bad fit” without structural interpretation.

## Relevance to group

Flagship Penn State–Cornell collaboration on coupling ReaxFF with scattering for geoceramic materials, relevant to cementitious and clay chemistry programs.

## Citations and evidence anchors

- https://doi.org/10.1021/acs.chemmater.9b03929

## Related topics

- [[reaxff-family]]
