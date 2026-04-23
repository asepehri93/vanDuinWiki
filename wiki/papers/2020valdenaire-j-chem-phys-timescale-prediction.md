---
id: paper:2020valdenaire-j-chem-phys-timescale-prediction
type: paper
title: "Timescale prediction of complex multi-barrier pathways using flux sampling molecular dynamics and 1D kinetic integration: Application to cellulose dehydration"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - method:enhanced-sampling
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:enhanced-sampling
  - keyword:lammps
  - keyword:npt-simulation
  - keyword:reaxff-application
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1063/1.5126391"
year: 2020
authors:
  - "Pierre-Louis Valdenaire"
  - "Roland J. M. Pellenq"
  - "Franz J. Ulm"
  - "Adri C. T. van Duin"
  - "Jean-Marc Leyssale"
venue: "J. Chem. Phys. 152, 024123 (2020)"
pdf_sha256: "d6266888ef6c8b703d353f0dc7b2a606a87a22be603e84f383f76855b511fa97"
pdf_path: "papers/Valdenaire_JCP_2020_cellulose_dehydrogenation.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020valdenaire-j-chem-phys-timescale-prediction -->

The authors combine **flux sampling** on a **1D reaction coordinate** with **kinetic integration** to extrapolate **rare-event kinetics** for **ReaxFF-based** **reactive MD** beyond brute-force time scales. The showcase is **crystalline cellulose dehydration/decomposition** at **1500–1900 K**, comparing product distributions to **replica-exchange MD** and fitting an **Arrhenius** regime with **Eₐ ≈ 93 kcal mol⁻¹** and **k₀ ≈ 9×10¹⁹ s⁻¹**, while noting **breakdown** of simple Arrhenius behavior when the **order parameter** becomes inadequate at lower temperature.

## Summary

Reactive MD with **ReaxFF** can show **multi-step pyrolysis** chemistry, but direct MD cannot cover **slow** **events** near **moderate T**. **Flux sampling** plus **1D kinetic integration** **bridges** time scales. For **I-β cellulose**, the protocol yields **H₂O**, **CO**, and **CO₂** product patterns consistent with **replica-exchange** results where decomposition completes, and an **Arrhenius** form with parameters **larger** than some **experiments**—a hint of **FF** or **path** limits. At **1500 K**, full **decomposition** is not reached in the runs **summarized**; **low-T** kinetics can **deviate** from a single **Arrhenius** line when the **order** **parameter** fails to capture **multi-barrier** kinetics.

## Methods

**1 — MD application.** **LAMMPS** with the **2013** **C–C** **Reaxff** parameters cited in the paper. **I-β cellulose** **supercell** with **PBC** (three-dimensional **periodic** cell as in the article); **NPT** targeting **~2.5 GPa** **isotropic** **hydrostatic** **pressure** (density matched to **1900 K** **REM** reference behavior). **Time step 0.1 fs**. **Flux** **sampling** on milestones along a **reaction** **coordinate** (released **gas** **molecules** counted); **10 ps** **MD** **segments** for each **flux** estimate; **kinetic** **integration** of **forward/backward** **rates** along the coordinate (Sections 2–3). **T** sweeps **1500–1900 K** in **100 K** steps. **N/A** — static external **electric** **field**; **N/A** — umbrella in the sense of traditional bias potentials (the method is **flux** **sampling**; confirm wording in PDF). **Thermostat** and **barostat** families are given in the article for the **NPT** **stages**—see **## Limitations** if a label is not copied in one line here. **N/A** if **NVE** **brute-force** segments: **not** the **dominant** method—**flux** **sampling** **windows** are **short** **NPT**-style as stated.

**2 — Force-field training.** **N/A** — the manuscript **uses** a **published** **Reaxff** for **cellulose**-relevant **C–O**/**H** chemistry; **N/A** for a **de novo** **GA** **refit** in this article.

**3 — Static QM.** **N/A** for standalone DFT in the main workflow; **Reaxff** is empirical.

**4 — Review or non-simulation.** **N/A** — method + application article.

## Findings

**Outcomes and mechanisms.** **Flux** **sampling** **+** **kinetic** **integration** **extends** **reachable** time scales for **rare** **rearrangements** vis-à-vis **brute-force** **MD** at **comparable** cost in this problem class. **H₂O**/**CO**/**CO₂** **distributions** align with **REM**-based reference where **full** **pyrolysis** completes. An **Arrhenius** **fit** yields **Eₐ ≈ 93 kcal mol⁻¹** and **k₀ ≈ 9×10¹⁹ s⁻¹**, **larger** than typical **experiments** as noted. **Decomposition** **incomplete** at **1500 K** in the **stated** **protocol**. **Arrhenius** **breakdown** at **lower T** is tied to the **reaction** **coordinate** not capturing the **true** **multi-barrier** **manifold**—a **method** **limit** as the authors **discuss**.

**Comparisons and sensitivity.** **Brute-force** **MD** **benchmarks** at high **T**; **T**-dependent **kinetics**; **pressure** via **NPT** **2.5 GPa** design.

**Authored limitations and outlook.** **Order-parameter** **error** and **Reaxff** **accuracy** near **pyrolysis** chemistry; see **## Limitations** on the page.

**Corpus honesty.** **Figures** **(e.g.** **Figure 8**)** in `pdf_path` for **quantitative** **flux** and **brute-force** **comparisons**.

## Limitations

**Order-parameter** sensitivity is explicit: **incorrect** or **too coarse** coordinates can **distort** inferred **rates**. **ReaxFF** chemistry for **pyrolysis** remains **approximate** relative to **QM**.

## Relevance to group

**van Duin** co-authorship; couples **ReaxFF pyrolysis** with **enhanced sampling** / **kinetic** **integration** methodology.

## Citations and evidence anchors

- DOI: `10.1063/1.5126391`

## Related topics

- [[reaxff-family]]
- [[2020valdenaire-j-chem-phys-timescale-prediction-2]]
