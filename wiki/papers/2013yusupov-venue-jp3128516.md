---
id: paper:2013yusupov-venue-jp3128516
type: paper
title: "Plasma-induced destruction of bacterial cell wall components: A reactive molecular dynamics simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:nvt-simulation
source_refs: []
doi: "10.1021/jp3128516"
year: 2013
authors:
  - "Maksudbek Yusupov"
  - "Annemie Bogaerts"
  - "Stijn Huygh"
  - "Ramses Snoeckx"
  - "Adri C. T. van Duin"
  - "Erik C. Neyts"
venue: "J. Phys. Chem. C"
pdf_sha256: "9b4eab27c76ab94b31619be3b7dce1dcfacbbbb883e4ec927df681b18381bb75"
pdf_path: "papers/Yusupov_Plasma_BacterialWall_JPCC_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013yusupov-venue-jp3128516 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. For species-specific bond-breaking pathways and rates, use the article and SI.

## Summary

**Reactive molecular dynamics (ReaxFF)** probes how plasma-relevant species (**OH**, **O**, **O₃**, **H₂O₂**, plus **O₂** and **H₂O**) interact with a **Staphylococcus aureus** peptidoglycan model. The paper reports that **OH**, **O**, **O₃**, and **H₂O₂** can rupture structurally important **C–O**, **C–N**, and **C–C** bonds, whereas **H₂O** and **O₂** do not break those backbone bonds in the same sense; mechanisms and effectiveness are **species-dependent** (abstract and computational details in `papers/Yusupov_Plasma_BacterialWall_JPCC_2013.pdf`).

## Methods

**Force-field training:** **N/A —** the study applies an existing **ReaxFF** parameter set (**C/H/O/N glycine/water** parameters of **Rahaman et al.** cited in the article), not a new fit.

**Static QM / DFT-only:** **N/A —** central results are **ReaxFF** trajectories, not a standalone DFT benchmark paper.

**1 — MD application (atomistic dynamics).** **Engine / code:** **Reactive MD** with **ReaxFF** as described in the **J. Phys. Chem. C** article; the integrator package (e.g. **LAMMPS**) is **N/A — not named on pages 1–2** of `normalized/extracts/2013yusupov-venue-jp3128516_p1-2.txt` (confirm in the PDF/SI if reproducing runs). **System size and composition:** **S. aureus** peptidoglycan in a simulation box of roughly **75 × 88 × 51 Å** without solvent bulk beyond the projectile species. **Boundaries / periodicity:** **Nonperiodic** cell (**no PBC** per computational details). **Ensemble:** impact trajectories after **300 K** equilibration of the PG; the article does not spell out a named thermostat for the **300 ps** impact segments on the excerpted pages—**N/A — thermostat family for production impacts not restated in the p1–2 extract** (see full text). **Timestep:** **0.1 fs**. **Duration / stages:** **300 ps** per trajectory; **50** runs per impinging species, each starting with **10** incident particles placed **≥10 Å** apart with **room-temperature**-sampled speeds and random directions. **Thermostat:** **N/A —** beyond pre-impact **300 K** PG equilibration, explicit damping constants for the impact segment are **not in the p1–2 extract**. **Barostat:** **N/A —** not an **NPT** bulk simulation. **Temperature:** **300 K** PG equilibration; incident speeds sampled for **room temperature**. **Pressure:** **N/A —** no hydrostatic pressure control described for this open-boundary impact setup. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

## Findings

- **H₂O** and **O₂** impacts **do not break** the **C–O / C–N / C–C** “backbone” bonds flagged as structurally important; molecules mainly **adsorb** via **H-bonding** to PG.
- **OH, O, O₃, and H₂O₂** can **rupture** those **key** bonds, but **pathways differ strongly** with species (hydrogen abstraction, direct oxidation, etc., as detailed per species in the Results).
- Because **mechanisms and bond targets differ**, the **relative effectiveness** of **wall disruption** is **species-dependent**, matching the abstract’s emphasis on **nonuniform** plasma-oxidant reactivity.
- **Compared to controls:** **H₂O** and **O₂** are summarized as **non-scissile** for the highlighted **backbone** bonds, contrasting **OH / O / O₃ / H₂O₂** (**Findings**).
- **Sensitivity:** outcomes depend on **impinging species identity** and **collision geometry** (**50 × 10** run protocol).
- **Limitations / outlook:** the **model peptidoglycan** and **simplified** plasma proxy omit **fields**, **solvation**, and **live-cell** complexity (**## Limitations**).
- **Corpus note:** bond-level **mechanism** tables live in the **PDF/SI**—this page does not duplicate every **species-resolved** pathway.

## Limitations

- **Model** peptidoglycan and **gas-phase/surface** approximations of **plasma–bio** interaction; **full** plasma environments include **fields**, **fluxes**, and **solvation** beyond the MD scope summarized here.

## Relevance to group

**Adri C. T. van Duin** (Penn State) coauthors with **Antwerp** plasma modeling colleagues; extends **ReaxFF** into **plasma–biomaterial** reactivity.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/jp3128516` (`papers/Yusupov_Plasma_BacterialWall_JPCC_2013.pdf`).

## Related topics

- [[reaxff-family]]
