---
id: paper:2019xuan-venue-paper
type: paper
title: "Multi-scale modeling of gas-phase reactions in metal-organic chemical vapor deposition growth of WSe₂ (uncorrected proof)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - method:reaxff
  - method:continuum-or-mesoscale
  - task:application
  - material:tmd
  - scale:multiscale
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:reactive-md
source_refs: []
doi: "10.1016/j.jcrysgro.2019.125247"
year: 2019
authors:
  - "Yuan Xuan"
  - "Abhishek Jain"
  - "Suhaib Zafar"
  - "Roghayyeh Lotfi"
  - "Nadire Nayir"
  - "Yuanxi Wang"
  - "Tanushree H. Choudhury"
  - "Samuel Wright"
  - "John Feraca"
  - "Leonard Rosenbaum"
  - "Joan M. Redwing"
  - "Vincent Crespi"
  - "Adri C. T. van Duin"
venue: "Journal of Crystal Growth (uncorrected proof)"
pdf_sha256: "c15d84a0b0b3c5bc885d28b44033ce1503bacc47fc407fe6da9575b1f3306a3a"
pdf_path: "papers/Xuan_J_Cryst_growth_WSe2_multiscale_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2019xuan-venue-paper -->

## Summary

This page documents an **uncorrected proof** PDF (`papers/Xuan_J_Cryst_growth_WSe2_multiscale_proof.pdf`) for the *Journal of Crystal Growth* article (DOI `10.1016/j.jcrysgro.2019.125247`) on **multi-scale modeling** of **gas-phase** chemistry during **metal–organic chemical vapor deposition (MOCVD)** growth of **tungsten diselenide** from **tungsten hexacarbonyl** and **hydrogen selenide** precursors, with **Adri C. T. van Duin** among the co-authors. The scientific program—as fully curated on the **version-of-record** page [[2019xuan-journal-of-c-multi-scale-modeling]]—combines **density functional theory** to identify reaction classes and train **ReaxFF** for **W/H/C/O/Se**, **ReaxFF molecular dynamics** to extract **pathways** and **activation energies** feeding **Arrhenius** parameters, and **reacting computational fluid dynamics** of a **cold-wall** reactor to connect **chemistry** with **mass and heat transport**. The proof file exists in the corpus alongside the **final-layout** PDF to preserve **publisher-state** provenance during ingest; readers should assume **figures**, **pagination**, and minor **wording** may differ from the **journal** PDF until cross-checked.

## Methods

Methodologically, the workflow is identical to [[2019xuan-journal-of-c-multi-scale-modeling]]: **QM** provides reference data for **gas-phase** bond rearrangements and **thermochemistry**, **ReaxFF** supplies an empirical reactive model consistent with those references at MD-accessible cost, and a **compiled kinetic mechanism** is embedded in a **CFD** solver capturing **inlet** conditions, **buoyancy**, **heating**, and **species transport** in the **MOCVD** chamber used experimentally. **Validation** emphasizes comparing **gas-phase** concentrations of **tungsten-containing chalcogenide** species near the **substrate** to **spatial** trends in measured **film thickness**, treating those species as **effective** **growth feedstock** proxies. Because this slug tracks **proof** bytes, the authoritative **Methods** section numbering, **supplementary** pointers, and **figure** labels should be read from the **VOR** wiki page and its PDF rather than from the proof PDF alone.

**ReaxFF + DFT + CFD (same science as the VOR).** **Engine:** **LAMMPS**-style **reactive** **molecular** **dynamics** for **W/H/C/O/Se** **gas** **chemistry** in **periodic** **cells**; **DFT** **reference** data for **training**; **CFD** for **cold-wall** **reactor** **transport**. **System:** **gas-phase** **precursor** **mixtures** with **W(CO)₆** and **H₂Se**-derived **species**; **N/A** for full **stoichiometry** **tables** on this **proof** page. **Ensemble:** **NVT**-like **ReaxFF** **MD** with **Nose–Hoover**-class **thermostat** when **NVT** is used (per VOR), plus **NVE**-like **segments** if the article uses them; **timestep** and **ns**-scale **duration** in the **VOR** **Methods**. **Temperature** **fields** follow **reactor** **heating** in **CFD**; **atomistic** **K** for **ReaxFF** are in the main text. **Barostat** for **non-periodic** **open** **reactor** **flow:** **N/A** in the **MD** **leg**; **CFD** handles **pressure** **gradients**. **Shear/strain, electric field, umbrella sampling:** **N/A** for the **MOCVD** **gas** **chemistry** **focus** in the **abstract**-level **summary**. **Detail source:** **[[2019xuan-journal-of-c-multi-scale-modeling]]** and the final **J. Cryst. Growth** PDF, not the **uncorrected** **proof** **bytes** alone.

## Findings

The published study reports that the **coupled gas-phase model** reproduces **experimental** trends linking **precursor** transport and **local** **chalcogenide** availability to **deposited** **WSe₂** **thickness** across the wafer, supporting the paper’s argument that **full-chamber** **chemistry–transport** coupling is necessary when **experimental** gas-phase maps are sparse. The authors also position the framework as **transferable** to other **CVD** chemistries by swapping **mechanism** blocks while retaining the **ReaxFF → kinetics → CFD** pipeline. For this **proof-ingest** page, the wiki does not restate every numerical comparison; instead, it directs readers to **[[2019xuan-journal-of-c-multi-scale-modeling]]** for **sentence-level** findings and **quantitative** benchmarks aligned with the **final** article text. **Corpus honesty:** this file is for **provenance** of the **uncorrected proof** PDF; cite **VOR** figures and tables in downstream work.

## Limitations

**Uncorrected proofs** may include **watermarks**, **layout** differences, and non-final **figure** resolution; citations requiring stable **page** or **figure** numbers should use the **version-of-record** path. **Surface** **growth** chemistry itself is not resolved atomistically in the **CFD** layer—**gas-phase** **fluxes** supply **boundary** conditions to continuum growth interpretations rather than a fully coupled **ReaxFF-on-surface** multiscale loop.

## Relevance to group

**Multiscale ReaxFF + CFD** workflow for **2D TMD** **MOCVD** (van Duin co-author); this page is **ingest provenance** for the proof file.

## Citations and evidence anchors

DOI: [10.1016/j.jcrysgro.2019.125247](https://doi.org/10.1016/j.jcrysgro.2019.125247)

## Reader notes (navigation)

- [[2019xuan-journal-of-c-multi-scale-modeling]]

## Related topics

- [[reaxff-family]]
