---
id: paper:2018zhang-j-phys-chem-improvement-reaxff
type: paper
title: Improvement of the ReaxFF Description for Functionalized Hydrocarbon/Water
  Weak Interactions in the Condensed Phase
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:reaxff-lineage
- domain:batteries-electrochemistry
- method:reaxff
- task:parameterization
- domain:organics-polymers-pyrolysis
- scale:atomistic
paper_keywords:
- keyword:reaxff-parameterization
- keyword:qm-training-data
- keyword:water-interfaces
- keyword:polymer
- keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcb.8b01127
year: 2018
authors:
- Weiwei Zhang and Adri C. T. van Duin
venue: J. Phys. Chem. B 2018.122:4083-4092
pdf_sha256: 13375a09acad8a8c5d504f710f67deb945f0885a9d52e2649acdd04d69a77589
pdf_path: papers/Zhang_JPCB_Weak_Interactions_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018zhang-j-phys-chem-improvement-reaxff -->

## Summary

The work introduces **CHON-2017_weak**, a **ReaxFF** reparameterization built on the **protein-2013** parameter set to fix **condensed-phase densities** and **weak C/H/O/N interactions** for **functionalized hydrocarbons with water**. Validation spans **pure liquids and mixtures** (including **hexane–water** demixing, **ethanol** and **tetramethylammonium (TMA)** in water), plus **AEM-relevant** simulations of **TMA structure and base-induced degradation** in alkaline solution, where an **alternate degradation pathway** is proposed relative to prior **QM** pictures. The **J. Phys. Chem. B** article is positioned as a **practical** **fix** for **aqueous** **organic** **density** and **demixing** errors that otherwise propagate into **membrane** **degradation** **studies**.

## Methods

**1 — MD application.** **Engine / code:** **ReaxFF** **molecular dynamics** is carried out with **LAMMPS** (cited in §2.2 together with the standalone **ReaxFF** code for development tasks). **System size & composition:** validation cells include, e.g., **500**-molecule **liquid water** boxes, **200**-molecule **n-alkane** periodic samples, **hexane–water** mixtures, **ethanol** and **TMA** in water, and **crystal** **amino acid** cells for selected properties; **atom** counts and box preparation (low-density start, compression, **NPT** density equilibration) follow §2.2. **Boundaries / periodicity:** **3D PBC** throughout. **Ensemble:** **NPT** **MD** at **room temperature** (plus **100 K** **NPT** for **amino acid crystals** to limit thermal disorder) to equilibrate **liquid** **density**—**500 ps** total with **density** averaged over the **last 400 ps** after box compression from **0.1 g/cm³**; separate **500 ps NVT** **MD** trajectories provide **RDF**/**MSD** for **liquid water** and **TMA/OH⁻/water** mixtures. **Timestep:** **0.25 fs** for all **ReaxFF MD** segments reported in §2.2. **Thermostat / barostat:** **Berendsen** **thermostat** with **temperature** damping **100 fs** for **NVT** runs and **Berendsen** **barostat** with **pressure** damping **2500 fs** for **NPT** runs. **Duration / stages:** **500 ps** per production block for the **liquid**/**mixture** protocols above after **NPT** equilibration. **Temperature:** **~298 K** “**room temperature**” liquid runs; **100 K** **NPT** for **crystal** examples; small-molecule **reaction mechanism** comparisons at **0.1 K** in the **ReaxFF** driver to match **0 K** **QM** references. **Pressure:** **NPT** **hydrostatic** control only where **NPT** is used; **NVT** blocks are **constant volume**. **Electric field:** **N/A —** not used in the validation suite summarized in §2.2. **Enhanced sampling:** **N/A —** not reported (standard **NVT**/**NPT** **MD**). **Shear / shock / AIMD:** **N/A —** not part of this parameterization study.

**2 — Force-field training.** **Parent FF / elements:** **protein-2013** (aqueous branch) with **C/H/O/N** **van der Waals** and **hydrogen-bond**-related terms reoptimized to form **CHON-2017_weak** (§2.1). **QM reference:** **DFT** (and related **QM**) data enter the **training** and **reaction**-scan comparisons as cited in the article; full levels and data sets are tabulated in the main text and **SI**. **Training set / targets:** **liquid** **densities**, **RDFs**, **hexane–water** **demixing**, **TMA** structural and **degradation** chemistry, and small-molecule **reaction** benchmarks. **Optimization / software:** **ReaxFF** **parameter** **optimization** (successive / least-squares style updates) as described in §2.1, implemented with the standalone **ReaxFF** code for development and **LAMMPS** for large **MD** validation. **Reference data / validation:** **experimental** **densities** and **RDF**/**MSD** benchmarks for water and organics, plus **QM** pathways for the **TMA** discussion.
## Findings

- **CHON-2017_weak** reproduces **experimental density trends** for the tested **pure and mixed** CHON systems substantially better than **protein-2013** for the weak-interaction issues highlighted in the abstract.
- The force field captures **macrophase separation** for **hexane + water** and sensible **solvation** behavior for **ethanol** and **TMA** in water (abstract).
- For **TMA degradation** in base, simulations motivate an **additional pathway** that is **more favorable energetically** than the **dominant QM-predicted** route in the prior literature (abstract—see article for structures and energetics).

The **discussion** stresses that **weak**-interaction **fixes** should be **regression-tested** on **reactive** **benchmarks** relevant to each **new** **application** because **van der Waals** **reoptimization** can perturb **barriers** outside the **training** **window**.

## Limitations

Weak-interaction fits can trade accuracy against reactive channels not included in the training set; confirm any new chemistry against **QM** or experiment before high-stakes predictions. Parameter files and full validation tables are detailed in the article and **Supporting Information**.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

Defines **CHON-2017_weak**, a widely reused **aqueous-organic** ReaxFF branch for **membrane** and **solution chemistry** in the group.

## Citations and evidence anchors

- DOI: `10.1021/acs.jpcb.8b01127`

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
