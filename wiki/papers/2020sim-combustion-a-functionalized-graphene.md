---
id: paper:2020sim-combustion-a-functionalized-graphene
type: paper
title: "Functionalized graphene sheet as a dispersible fuel additive for catalytic decomposition of methylcyclohexane"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:berendsen-thermostat
  - keyword:combustion
  - keyword:graphene-carbon
  - keyword:nvt-simulation
  - keyword:reaxff-application
  - keyword:thermal-decomposition
candidate_tags: []
source_refs: []
doi: "10.1016/j.combustflame.2020.04.002"
year: 2020
authors:
  - "Hyung Sub Sim"
venue: "Combustion and Flame, 217 (2020) 212–221"
pdf_sha256: "458963baedd08fdf55baac1f8ba645f75af223fcc359bb18a6214c6233d483c8"
pdf_path: "papers/Sim_CombFlame_2020_graphene_mecyhex.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020sim-combustion-a-functionalized-graphene -->

**Methylcyclohexane (MCH)** pyrolysis in a **high-pressure flow reactor** under **supercritical** conditions (**4.72 MPa**, **780–825 K**) is **accelerated** by suspended **functionalized graphene sheets (FGS)** at **50 ppmw**, with matching **ReaxFF reactive MD** at **1700–1900 K** used to interpret **oxygen-functional-group–mediated** fuel–surface chemistry and **radical** formation.

## Summary

Experiments show higher **MCH conversion** and **C₁–C₂ product yields** with **FGS** at **820 K** (increases **~43.3%** and **~62.1%** vs the no-FGS case quoted in the abstract for **50 ppmw FGS**). ReaxFF MD highlights **oxygen-containing groups** on FGS in **heterogeneous dehydrogenation** of MCH to a **C₇H₁₃** radical and subsequent **H**, **CH₃**, and **C₂H₅** production that promotes **H-abstraction** and **hydrogenation** at early conversion. The paper argues that **ppm-level** additives can shift **cracking** **selectivity** without changing **macroscopic** **reactor** severity, motivating **atomistic** **surface** chemistry explanations.

## Methods

**1 — MD application (reactive).** The authors use **reactive MD** with **ReaxFF** **C/H/O** chemistry in **AMS/ADF** for MCH in contact with FGS. **NVT** ensemble, **Berendsen** thermostat, **0.25 fs** time step, fluid density **~0.31 g cm⁻³**, and **1700, 1800, and 1900 K** production temperatures with **multi-ns** trajectory segments (Section 3 of the article; ~5–6 ns segments in the text). **N/A —** replica exchange, umbrella sampling, or metadynamics. **N/A —** external electric field. System composition (MCH, FGS oxygenated surface sites, and periodic cell) follows Section 3. **N/A —** NPT or barostat: the MD protocol is NVT. **N/A —** Ewald/cutoff detail beyond what is stated in the VOR—confirm `pdf_path` for full electrostatic settings.

**2 — Force-field training.** The work applies a **published** ReaxFF **C/H/O** model for fuel/surface chemistry; the manuscript does **not** report a new parameter fit here (**N/A** for in-paper reoptimization).

**3 — High-pressure flow reactor (experiment, coupled interpretation).** **Supercritical** MCH at **4.72 MPa** and **780–825 K** with **50 ppmw** suspended FGS; product identification by **GC/MS** and reactor protocol as in the article (Section 2–3).

**4 — Static QM / DFT (standalone).** **N/A** — the paper does not present a separate DFT block; it uses ReaxFF for dynamics.

**5 — Review or perspective.** **N/A** — primary research article with experiment + MD.

## Findings

**Outcomes and mechanisms.** With **50 ppmw FGS** at **820 K**, the abstract reports **+43.3%** MCH conversion and **+62.1%** C₁–C₂ yield relative to the baseline. ReaxFF trajectories support **oxygenated** FGS groups in catalyzing MCH **decomposition** via **heterogeneous dehydrogenation** to **C₇H₁₃** and early radicals (**H**, **CH₃**, **C₂H₅**) that feed **H-abstraction** and **hydrogenation** pathways.

**Comparisons and sensitivity.** The experiment links additive loading and temperature in the **supercritical** window; the MD leg spans **1700–1900 K** as a high-temperature mechanistic window.

**Authored limitations and transfer.** A large **temperature gap** between **MD** (**~1700–1900 K**) and the **reactor** (**~780–825 K**) means **qualitative** mechanistic use of MD, not direct rate prediction. **Flow** kinetics, **wall** effects, and **soot** pathways are outside the small **cluster/slab** models.

**Corpus honesty.** **Numerical** protocol and figure detail should be verified in the version-of-record PDF at `pdf_path`.

## Limitations

Large **temperature gaps** between **MD** windows (**~1700–1900 K**) and **reactor** conditions (**~780–825 K**) require **qualitative** transfer of mechanistic insight; absolute rates from MD are not direct predictions of reactor performance. **Flow** **reactor** **kinetics** also depend on **mixing**, **wall** **effects**, and **soot** **formation** pathways not represented in **cluster** or **slab** **ReaxFF** models. **Supercritical** **fluid** **properties** (density, **diffusivity**) set **effective** **reactant** **flux** to **FGS** surfaces and must be taken from **experimental** **equation-of-state** data for the **stated** **pressure** **window**. **ReaxFF** **radical** **counts** in **MD** are **diagnostic** **populations**, not **calibrated** **concentrations** for **plug-flow** **reactor** **models** without additional **kinetic** **post-processing**. **Combustion and Flame** **Section 3** ties **experimental** **conversion** metrics to **reported** **reactor** **residence** **times**.

## Relevance to group

**van Duin** co-authorship; **combustion / endothermic fuel cracking** application of **ReaxFF** with **experimental** validation.

## Citations and evidence anchors

- DOI: `10.1016/j.combustflame.2020.04.002`

## Related topics

- [[reaxff-family]]
- [[2020sim-acs-enhanced-fuel]]
