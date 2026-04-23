---
id: paper:2018raju-scientific-r-phase-transitions-2
type: paper
title: Phase transitions of ordered ice in graphene nanocapillaries and carbon nanotubes
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:water-silica-geo
- domain:reactive-md
- material:graphene-carbon-nano
- method:reaxff
- task:application
- scale:atomistic
paper_keywords:
- keyword:water-interfaces
- keyword:graphene-carbon
- keyword:reaxff-application
- keyword:reactive-md
candidate_tags: []
source_refs: []
doi: 10.1038/s41598-018-22201-3
year: 2018
authors:
- Muralikrishna Raju
- Adri van Duin
- Matthias Ihme
venue: Scientific Reports 8, 3851 (2018)
pdf_sha256: 7027d25120b661c3a6269473b5c14368241376b6712368587a2fdcfd29d6ab46
pdf_path: papers/Raju_Scientific_Reports_2018_online.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018raju-scientific-r-phase-transitions-2 -->

## Summary

**ReaxFF** molecular dynamics, following **grand-canonical Monte Carlo** initialization of confined water, maps **ice and water** in **graphene nanocapillaries** and **single-walled carbon nanotubes**. The work emphasizes **AA-stacked** multilayer **square ice** with **interlayer hydrogen bonding**, **first-order** versus **continuous** melting (and **critical-point-like** behavior) depending on density and layer count, **elevated** solid–liquid transition temperatures in **CNTs** compared with **273 K**, and **enhanced proton/hydroxyl transport** (up to roughly **several-fold** over bulk at **300 K** in ordered confinement).

## Methods
**1 — MD application (confined water + ice).** **Grand-canonical Monte Carlo (GCMC)** at fixed **liquid-water chemical potential** initializes confined structures (**SI** details). Production runs use **ReaxFF** **molecular dynamics** with **0.10 fs** timestep and **Nosé–Hoover** thermostat (**10 fs** coupling) under the **constant-volume** protocols described in *Sci. Rep.* (the article quotes **1 atm** target conditions while keeping cell metrics fixed during heating/melting segments—treat as the paper’s documented **NVT-like** melting workflow rather than inventing a separate barostat here). **PBC:** **three-dimensional PBC** for **graphene nanocapillaries** and **CNT** confinement models. **System sizes / atom counts:** follow **figure/table** construction in the article (**SI** for exact counts). **Temperature:** melting scans span **230–400 K** continuous regimes discussed for certain **square-ice** stacks, include **300 K** transport analyses for confined **1D/2D** ice, and use broader heating windows tabulated in *Sci. Rep.* figures. **Duration:** **nanosecond-class** cumulative sampling is referenced for selected melting scans in the article/SI (use the **PDF** for exact segment lengths). **Barostat during melting sweeps:** **N/A —** not separated as **NPT** production in the excerpted description. **Pressure / stress control:** **1 atm** referenced for thermostatized melting studies; no external **electric field**. **Enhanced sampling:** **N/A —** aside from **GCMC** pre-equilibration.

**2 — Force-field training.** **N/A —** uses published **ReaxFF** water/carbon chemistry.

**3 — Static QM.** **N/A —** not an AIMD-first study.

**Duplicate PDF note:** this slug mirrors **[[2018raju-scientific-r-phase-transitions]]** with an alternate **`pdf_path`** (`papers/Raju_Scientific_Reports_2018_online.pdf`).

## Findings
**Outcomes / mechanisms:** **ReaxFF** reproduces **AA-stacked** multilayer **square ice** in **graphene nanocapillaries** with **interlayer H-bonds**, contrasting some older **AB-stacked** classical pictures. **Melting signatures** differ: **bilayer hexagonal** ice shows **first-order**-like jumps, whereas some **square-ice** stacks show **continuous** energy evolution over **~230–400 K** windows discussed in the text. **CNT** confinement raises **melting temperatures** above **273 K**, discussed alongside **Raman** literature constraints. **Proton/hydroxyl** mobilities can exceed **bulk** by up to several-fold at **300 K** in ordered confinement.

**Comparisons:** stacking and melting behavior are compared to **prior classical models** and selected **experiments** cited in the paper.

**Sensitivity:** **confinement geometry** (**2D slit** vs **1D tube**) steers polymorph selection and **melting** classification.

**Limitations:** **ReaxFF** bulk-water errors propagate to **phase boundaries**; sampling length affects sharp vs gradual melting.

**Corpus honesty:** this slug is an **alternate publisher PDF** for the same *Scientific Reports* article as [[2018raju-scientific-r-phase-transitions]] (`papers/Raju_Scientific_Reports_2018.pdf`); scientific content matches that entry. Confirm numbers against whichever **VOR/SI** PDF you cite externally.

## Limitations

**ReaxFF** bulk-water benchmarks deviate from **experiment** and **ab initio** references in some limits; **phase boundaries** depend on **confinement** geometry, **water model**, and **sampling** length. Maintaining **two** article PDFs in the corpus is for **manifest** convenience only.

## Relevance to group

**Adri van Duin** co-authorship; extends **ReaxFF** studies of **nanoconfined water** on **carbon** for retrieval alongside [[2018raju-scientific-r-phase-transitions]].

## Citations and evidence anchors

- DOI: [10.1038/s41598-018-22201-3](https://doi.org/10.1038/s41598-018-22201-3)
- `normalized/extracts/2018raju-scientific-r-phase-transitions-2_p1-2.txt`

## Reader notes (navigation)

- Duplicate PDF for [[2018raju-scientific-r-phase-transitions]]; confined water: [[graphene-nanocarbon]], [[reaxff-family]].

## Related topics

- [[2018raju-scientific-r-phase-transitions]]
- [[reaxff-family]]
- [[graphene-nanocarbon]]
