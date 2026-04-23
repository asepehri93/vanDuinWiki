---
id: paper:2016correction-venue-ultrafine-jagged
type: paper
title: "Ultrafine jagged platinum nanowires enable ultrahigh mass activity for the oxygen reduction reaction"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - material:metal-surface
  - task:experiment-integrated
  - method:dft-static
  - scale:atomistic
paper_keywords:
  - keyword:validation-experiment
  - keyword:batteries-interfaces
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1126/science.aaf9050"
year: 2016
authors: "Mufan Li, Zipeng Zhao, Tao Cheng, Alessandro Fortunelli, Chih-Yen Chen, Rong Yu, Qinghua Zhang, Lin Gu, Boris Merinov, Zhaoyang Lin, Enbo Zhu, Ted Yu, Qingying Jia, Jinghua Guo, Liang Zhang, William A. Goddard III, Yu Huang, Xiangfeng Duan"
venue: "Science"
pdf_sha256: "6400c334800d813fe557dd91d14b17f0a9c8d14d2a9af1c4746ee5f1457e0ae0"
pdf_path: "papers/ReaxFF_others/Pt_Nanowire_Goddard_Science2016.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2016correction-venue-ultrafine-jagged -->

## Summary

This **Science** report presents **ultrafine jagged platinum nanowires (J-PtNWs)** as **electrocatalysts** for the **acid oxygen reduction reaction (ORR)** with exceptionally high **mass activity** and **electrochemically active surface area (ECSA)** relative to conventional **Pt/C** benchmarks. The **jagged** morphology is argued to expose a high density of **under-coordinated** / **high-index-like** **Pt** sites while maintaining favorable **surface-area-to-mass** ratio compared with bulkier **nanoparticle** morphologies. The work integrates **solution synthesis** of **Pt/NiO core/shell nanowires**, **thermal annealing** to **PtNi alloy** wires, **electrochemical dealloying** to **pure jagged Pt**, **microscopy**, **electrochemistry**, and **reactive molecular dynamics** (Caltech co-authors) used to relate **highly stressed, rhombohedral-rich, under-coordinated** surface motifs to **ORR** activity (Science text).

The abstract highlights ORR performance metrics at **0.9 V vs RHE**, including **specific activity** and **ECSA** values that combine to a **mass activity** substantially above **commercial Pt/C** and prior record catalysts cited in the article.

## Methods

**Synthesis, microscopy, and electrochemistry:** **Pt/NiO core/shell nanowires** are grown from **Pt(acac)\(_2\)** and **Ni(acac)\(_2\)** in **1-octadecene** with **oleylamine**. **TEM** shows core/shell contrast with typical diameters **~5 nm or less** and lengths **~250–300 nm**; **HRTEM** resolves **NiO (111)** shell fringes (**~0.24 nm**) and **Pt (111)** in the core (**~0.23 nm**). **Annealing** in **Ar/H\(_2\) (97/3) at 450 °C** converts the wires to **uniform PtNi alloy** while preserving overall morphology; **EDS** gives **Pt/Ni ~15/85** before and after annealing. **Electrochemical dealloying** leaches **Ni** to yield **jagged Pt nanowires**. **ORR** is evaluated at **0.9 V vs RHE** as in **Findings**.

**MD application (supporting atomistic modeling):** The article cites **reactive molecular dynamics** to argue that **highly stressed, rhombohedral-rich, under-coordinated** surface motifs on **jagged** wires favor **ORR** relative to more relaxed surfaces. **Code, timestep, ensemble, thermostat/barostat, system size, trajectory length, and electrostatic settings for those runs:** **N/A — not given in the corpus text slice used here**; see the **Science** article and **SI** for full simulation metadata.

**Force-field training:** **N/A — not a force-field fitting paper.**

**Static QM / DFT:** This page’s indexed text centers on **synthesis, microscopy, electrochemistry**, and **supporting reactive MD**; any standalone **periodic DFT** benchmarks in the full article are **not transcribed here**. **DFT functional / hybrid level:** **N/A — not stated in the indexed extract.** **Dispersion correction (DFT-D / vdW):** **N/A — not stated in the indexed extract.** **Basis set or plane-wave / PAW settings:** **N/A — not stated in the indexed extract.** **k-point / k-mesh sampling:** **N/A — not stated in the indexed extract** for any periodic QM tables. **Structures / pathways (QM):** **N/A — not summarized here** beyond the experimental nanowire narrative. **QM properties tabulated (energies, barriers, DOS, …):** **N/A — see Science/SI** if the full paper reports them.

## Findings

At **0.9 V vs RHE**, the authors report **specific activity ~11.5 mA/cm²**, **ECSA ~118 m²/g Pt**, and **mass activity ~13.6 A/mg Pt**—about **50×** the mass activity of **commercial Pt/C** cited as state of the art and nearly **twice** prior record values (**6.98 A/mg Pt** and **5.7 A/mg Pt** references in the abstract). The **jagged** morphology is linked to high **surface-area-to-mass** and **under-coordinated**, **rhombohedral-rich** surface character. **Reactive MD** supports the qualitative picture that **stressed** surfaces on these wires outperform relaxed ones; **quantitative MD-derived barriers or coordination statistics** are **not** summarized on this page—use **SI** with the **PDF**.

## Limitations

This is primarily an **experimental catalysis** paper; **MD/DFT** details are supporting evidence. **Durability** under **fuel-cell** **load cycles**, **ionomer** effects, and **operando** restructuring extend beyond the abstract claims. **Reactive MD** parameters and **DFT** functionals have known approximations for **electrified interfaces**.

## Relevance to group

**Caltech Goddard** collaboration thread on **electrocatalysis** with **atomistic** modeling—adjacent to **fuel-cell** and **battery-interface** literature in the broader corpus, though not a **ReaxFF parameterization** paper.

## Citations and evidence anchors

- DOI [10.1126/science.aaf9050](https://doi.org/10.1126/science.aaf9050).
- Excerpt alignment: `normalized/extracts/2016correction-venue-ultrafine-jagged_p1-2.txt`.

## Related topics

- [[reaxff-family]]
