---
id: paper:2018raju-scientific-r-phase-transitions
type: paper
title: Phase transitions of ordered ice in graphene nanocapillaries and carbon nanotubes
updated: "2026-04-20"
confidence: med
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
venue: Scientific Reports
pdf_sha256: ec902be90db466b011b996e35bb9e38acf678e690fabc2c6ae6c33074f0b1d80
pdf_path: papers/Raju_Scientific_Reports_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018raju-scientific-r-phase-transitions -->

## Summary

ReaxFF molecular dynamics maps phase behavior of confined water in graphene nanocapillaries and single-walled carbon nanotubes, emphasizing AA-stacked multilayer square ice, first-order vs continuous melting signatures, elevated freezing temperatures in narrow CNTs, and fast proton/hydroxyl transport relative to bulk water. The study is motivated by ongoing debates about **structure** and **melting** of water under extreme nanoconfinement, where dimensionality and template chemistry can stabilize ice polymorphs not seen in bulk.

## Methods
**1 — MD application (confined water + ice).** **Grand-canonical Monte Carlo (GCMC)** at fixed **liquid-water chemical potential** initializes confined structures (**SI** details). Production runs use **ReaxFF** **molecular dynamics** with **0.10 fs** timestep and **Nosé–Hoover** thermostat (**10 fs** coupling) under the **constant-volume** protocols described in *Sci. Rep.* (the article quotes **1 atm** target conditions while keeping cell metrics fixed during heating/melting segments—treat as the paper’s documented **NVT-like** melting workflow rather than inventing a separate barostat here). **PBC:** **three-dimensional PBC** for **graphene nanocapillaries** and **CNT** confinement models. **System sizes / atom counts:** follow **figure/table** construction in the article (**SI** for exact counts). **Temperature:** melting scans span **230–400 K** continuous regimes discussed for certain **square-ice** stacks, include **300 K** transport analyses for confined **1D/2D** ice, and use broader heating windows tabulated in *Sci. Rep.* figures. **Duration:** **nanosecond-class** cumulative sampling is referenced for selected melting scans in the article/SI (use the **PDF** for exact segment lengths). **Barostat during melting sweeps:** **N/A —** not separated as **NPT** production in the excerpted description. **Pressure / stress control:** **1 atm** referenced for thermostatized melting studies; no external **electric field**. **Enhanced sampling:** **N/A —** aside from **GCMC** pre-equilibration.

**2 — Force-field training.** **N/A —** uses published **ReaxFF** water/carbon chemistry.

**3 — Static QM.** **N/A —** not an AIMD-first study.

## Findings
**Outcomes / mechanisms:** **ReaxFF** reproduces **AA-stacked** multilayer **square ice** in **graphene nanocapillaries** with **interlayer H-bonds**, contrasting some older **AB-stacked** classical pictures. **Melting signatures** differ: **bilayer hexagonal** ice shows **first-order**-like jumps, whereas some **square-ice** stacks show **continuous** energy evolution over **~230–400 K** windows discussed in the text. **CNT** confinement raises **melting temperatures** above **273 K**, discussed alongside **Raman** literature constraints. **Proton/hydroxyl** mobilities can exceed **bulk** by up to several-fold at **300 K** in ordered confinement.

**Comparisons:** stacking and melting behavior are compared to **prior classical models** and selected **experiments** cited in the paper.

**Sensitivity:** **confinement geometry** (**2D slit** vs **1D tube**) steers polymorph selection and **melting** classification.

**Limitations:** **ReaxFF** bulk-water errors propagate to **phase boundaries**; sampling length affects sharp vs gradual melting.

**Corpus honesty:** quantitative factors follow **`papers/Raju_Scientific_Reports_2018.pdf`**; confirm against any updated **SI**.

## Limitations

ReaxFF water properties deviate from experiment and ab initio reference data in some bulk limits; phase boundaries remain sensitive to confinement model and sampling length.

## Relevance to group

Adri van Duin is a co-author; study extends ReaxFF investigations of nanoconfined water and ice on carbon.

## Citations and evidence anchors

- DOI: [10.1038/s41598-018-22201-3](https://doi.org/10.1038/s41598-018-22201-3)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
