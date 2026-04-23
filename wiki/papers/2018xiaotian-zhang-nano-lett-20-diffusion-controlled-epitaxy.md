---
id: paper:2018xiaotian-zhang-nano-lett-20-diffusion-controlled-epitaxy
type: paper
title: Diffusion-Controlled Epitaxy of Large Area Coalesced WSe2 Monolayers on Sapphire
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:2d-layered
- material:tmd
- scale:atomistic
- task:experiment-integrated
paper_keywords:
- keyword:2d-materials
- keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: 10.1021/acs.nanolett.7b04521
year: 2018
authors:
- Xiaotian Zhang
- Tanushree H. Choudhury
- Mikhail Chubarov
- Yu Xiang
- Bhakti Jariwala
- Fu Zhang
- Nasim Alem
- Gwo-Ching Wang
- Joshua A. Robinson
- Joan M. Redwing
venue: Nano Lett.
pdf_sha256: 453560d83d6720d1db864c66a6f09dd108afb072b1bbf9805c0d4174f8e89739
pdf_path: papers/Others/Zhang_Choudhury_WSe2_sapphite_epitaxy_NanoLett_2018.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018xiaotian-zhang-nano-lett-20-diffusion-controlled-epitaxy -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the Nano Letters article identified by `doi`, `title`, and `pdf_path`.

## Summary

**Gas-source CVD** on **c-plane sapphire** uses a **multi-step diffusion-mediated** recipe: a **nucleation** stage, **H\(_2\)Se** anneal to ripen **oriented** islands, then **growth** conditions that suppress new nucleation while **laterally** enlarging domains until **full monolayer coalescence** in **<1 h**. Post-growth **STEM/LEED**-style characterization (details in paper) shows **epitaxial** alignment with the substrate but **antiphase boundaries** where **0°** and **60°** domains merge. **Domain ripening** kinetics support **2D Ostwald**-type scaling, used to estimate **W-species** surface **diffusivity**; lateral growth rate is **weakly temperature-dependent** over **700–900 °C**, consistent with **mass-transport** control, while **domain shape** (triangular vs truncated) varies with **Se/W** ratio. The work positions **separating nucleation, ripening, and lateral growth** as a practical route to **large single-crystal-like** **monolayers** with **fast coalescence**, addressing persistent **CVD** challenges for **TMD** electronics.

## Methods

- **CVD:** **W** and **Se** precursors per gas-source configuration in §2; **H\(_2\)Se** exposure steps for ripening; temperature windows **700–900 °C** for lateral growth.
- **Characterization:** **SEM/AFM** (or equivalent) for domain size/density vs time; **atomic-resolution** imaging and diffraction for **orientation** and **boundary** structure; **Raman/PL** as cited to confirm monolayer character.
- **Kinetic analysis:** **Island-size** vs **time** scaling interpreted via **2D ripening** frameworks to extract **effective** **surface diffusivities** for **W-containing** species; lateral **growth velocities** analyzed for **temperature** dependence and **mass-transport** hypotheses.

## Findings

- **Process:** Separating **nucleation**, **ripening**, and **lateral growth** enables **large single-crystal-like** monolayers with controlled **defect density** and **fast** coalescence.
- **Kinetics:** **Island size** vs anneal time follows **2D ripening**, yielding **diffusivity** estimates for **tungsten-containing** surface species.
- **Growth regime:** **Nearly T-independent** lateral velocity over the studied window implies **mass-transport-limited** kinetics; **morphology** still varies with **Se:W** adatom balance.

- **Limitations (as stated or implied):** **CVD** recipes are **reactor-specific**; **kinetic** arguments are **phenomenological** (no atomistic **MD** in this paper); **antiphase** boundaries between **0°**/**60°** domains may limit electronic quality even at full **monolayer** coverage.

- **Corpus honesty:** Kinetic prefactors, **SEM** image statistics, and **diffraction** evidence should be read from **`papers/Others/Zhang_Choudhury_WSe2_sapphite_epitaxy_NanoLett_2018.pdf`** (and any publisher **SI**); this page is not a substitute for those tables.
## Limitations

Empirical **CVD** windows are **reactor-specific**; **atomistic** reaction pathways are **not** simulated with **MD** here—**kinetic** arguments are **phenomenological** fits to **SEM/AFM** island statistics and **diffraction** data. **Substrate** miscut and **precursor** purity can shift **nucleation** outside the reported windows. **Antiphase** **boundaries** between **0°** and **60°** **domains** may **degrade** **electronic** **quality** even when **monolayer** **coverage** is complete—evaluate **device** relevance with **local** **STEM** metrics from the **paper**.

## Relevance to group

**Penn State** (**Redwing**, **Robinson**, **Alem**, **Crespi-adjacent** 2DCC context) **experimental** **WSe₂** **CVD** paper—useful for **2D TMD** theme hubs and cross-links from **computational growth** reviews such as **`[[2020momeni-npj-computat-multiscale-computational]]`**.

## Citations and evidence anchors

- DOI `10.1021/acs.nanolett.7b04521` — *Nano Lett.* **2018**; `papers/Others/Zhang_Choudhury_WSe2_sapphite_epitaxy_NanoLett_2018.pdf`; extract `normalized/extracts/2018xiaotian-zhang-nano-lett-20-diffusion-controlled-epitaxy_p1-2.txt`.

## Related topics

- [[theme-2d-epitaxy-growth]]
- [[2020momeni-npj-computat-multiscale-computational]]
