---
id: paper:2020akbarian-venue-total-number
type: paper
title: "Atomistic-scale insight into the polyethylene electrical breakdown: An eReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - method:ereaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:polarizable-ff
  - keyword:charge-equilibration
  - keyword:polymer
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1063/5.0033645"
year: 2021
authors:
  - "Akbarian, Dooman"
  - "Ganeshan, Karthik"
  - "Woodward, W. H. Hunter"
  - "Moore, Jonathan"
  - "van Duin, Adri C. T."
venue: "J. Chem. Phys."
pdf_sha256: "2b73f0bdd7038db9d9b46cc42c04c65f66eb4f27746247267e9b000cfe7e78da"
pdf_path: "papers/Akbarian_JCP_2020_eReaxFF_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020akbarian-venue-total-number -->

!!! note "Corpus note"

The ingested PDF is an AIP author proof (queries and placeholder pagination appear in the extract). The article title above matches the proof body; prefer the version of record for bibliographic details.

## Summary

Cross-linked polyethylene is widely used as a high-voltage cable insulator, yet atomistic roles of manufacturing by-products, density, and void space in electrical breakdown remain poorly understood. The study introduces an eReaxFF-based molecular dynamics framework with explicit electronic degrees of freedom, parameterized against density-functional benchmarks, to simulate time-dependent dielectric breakdown trends in polyethylene as functions of mass density, void content, and electrophilic by-products such as acetophenone.

## Methods

**eReaxFF / electronic DOFs.** **eReaxFF** extends ReaxFF with an **explicit electron** description so **charge** redistribution and **field-driven** **electron** **dynamics** can be followed alongside **atomic** motion for **dielectric** **breakdown** chemistry without full **QM** on the whole cell.

**QM verification.** **Electronic** and **energetic** benchmarks are checked against **density-functional** **theory** data in the parameterization/validation discussion.

**Systems.** **Polyethylene** models span varied **mass density** and **void** **morphology**; **acetophenone** is introduced as a **by-product** surrogate in **neutral** and **radical** **anion** forms to probe **electron affinity** effects.

**Observables.** Trajectories report **time-to-dielectric-breakdown (TDDB)** trends and **electron** **migration** paths between **electrodes**, including **preferential** **channeling** through **void** space. **XLPE**-like **cross-linked** **networks** target **cable** **insulation** microstructures rather than **single-chain** melts.

**MD / eReaxFF protocol (additional slots).** Molecular dynamics with **eReaxFF** on **polyethylene** **supercells** (order **~10^3+** **atoms** with **voids** and **additives** as modeled); **3D** **PBC** between **anode**/**cathode**-like **boundary** conditions per *J. Chem. Phys.* **NVT**-like or **NVE**-like legs may appear; **Nose–Hoover**-type **thermostat** for 300 K–elevated **T** as in the **proof** (exact **K** **table** in VOR). **N/A —** **fs** **timestep** and **production** **ps**/**ns** totals: see AIP **proof**/VOR. **N/A —** **NPT** **barostat**; **N/A —** **1 bar** **reference** **pressure** in **NVT** **simulations**. **N/A —** **replica** **exchange** / **umbrella**. **Electric** **field** magnitudes and **ramp** protocols drive **breakdown** as in the article; **N/A** for a single universal **E**-field table on this page.

**FF training (block 2).** **eReaxFF** is **fit** to **DFT** **energies** and **electronic** **structure** in the JCP parameterization text; **N/A** to duplicate the **entire** **objective** here.

**Static QM (block 3).** **N/A** — the production study is **eReaxFF**-based, not a standalone DFT **application** paper.

## Findings

**Density.** Higher **PE** **density** **increases** **TDDB** in the simulations summarized in the abstract.

**Impurities.** **Acetophenone** (especially species with **positive** **electron affinity**) can **shorten** **TDDB**; the **radical anion** **lowers** **barriers** and **reaction** **energies** for **secondary** chemistry vs **neutral** acetophenone in the authors’ comparison.

**Voids.** During **breakdown**, **electrons** tend to **route** through **voids** between **anode** and **cathode**, implicating **void** **percolation** as an accelerator of **failure**.

**Sensitivity.** Small **impurity** loads can **disproportionately** alter **breakdown** statistics when **affinity** and **radical** chemistry couple to **field**-driven **electron** flux.

**Corpus honesty (proof).** The **AIP** file is an **author** **proof**; use the **JCP** **VOR** for **bibliography** and **any** line-numbered **revisions**.

## Limitations

Proof-stage metadata in the corpus (including the prior placeholder title) should be superseded by the official J. Chem. Phys. volume/page assignment; eReaxFF parameters may require recalibration for additives outside the training set. **High-voltage** **cable** **failure** in service also involves **partial** **discharge**, **space-charge** **buildup**, and **mechanical** **voiding** that extend beyond **atomistic** **eReaxFF** **trajectories** alone. **Field** **enhancement** at **electrode** **asperities** and **impurity** **clusters** can dominate **breakdown** **statistics** even when **bulk** **polyethylene** **models** appear stable in **MD**. **eReaxFF** **timestep** and **electronic** **mass** **rescaling** choices must match the **article** when reproducing **time-to-failure** **trends**. **J. Chem. Phys.** **methods** sections document **electrode** **boundary** **conditions** applied in **dielectric** **breakdown** trajectories. Consult those sections before **scaling** **simulation** **cells** to larger **polymer** **domains**.

## Relevance to group

Demonstrates eReaxFF for polymer dielectric breakdown in collaboration with Dow, extending polarizable ReaxFF capabilities maintained at Penn State.

## Citations and evidence anchors

- https://doi.org/10.1063/5.0033645

## Related topics

- [[reaxff-family]]
