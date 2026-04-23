---
id: paper:2017kowalik-venue-bez-tytu
type: paper
title: "Multi-step mechanism of carbonization in templated polyacrylonitrile derived fibers: ReaxFF model uncovers origins of graphite alignment"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:graphene-carbon
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2015.07.048"
year: 2015
authors:
  - "Biswajit Saha"
  - "Al'ona Furmanchuk"
  - "Yuris Dzenis"
  - "George C. Schatz"
venue: "Carbon"
pdf_sha256: "cea9801a39669775c2bb6c3ec5a3f2ba2d4d52a0e2092c47764d371792906e09"
pdf_path: "papers/ReaxFF_others/Saha_Carbon_PAN_2015.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2017kowalik-venue-bez-tytu -->

Reactive molecular dynamics with **ReaxFF** is used to interpret how **in situ** templating by double-walled carbon nanotubes versus graphitic nanoplatelets steers **polyacrylonitrile (PAN)** carbonization and graphitic alignment in nanofibers, with discussion tied to experimental electron-diffraction–style observables in the publication.

## Summary

Carbon fiber performance depends on graphitic order formed during multi-step carbonization of PAN-based precursors. Saha et al. simulate templated carbonization in models inspired by electrospun fibers that incorporate low loadings of **double-walled CNTs** or **graphitic nanoplatelets**. Depending on carbonization temperature, the dominant template–medium interaction shifts between **physisorption** (physical templating) and **chemisorption** (chemical templating). Strong template coupling yields **aligned graphitic structures**; in their simulations, **nanotube templates** produce **more robust** alignment than **graphite nanoparticle** templates. The study emphasizes quantitative comparison between atomistic structure (e.g., ring-density–related measures) and diffraction-related data for the experimental fiber systems.

## Methods

**1 — MD application (ReaxFF carbonization in LAMMPS).** **Saha et al.** simulate **templated PAN-derived carbonization** using **ReaxFF as implemented in LAMMPS** (*Carbon* **94** (2015) Methods). **Starting chemistry** is a **stabilized PAN precursor (SPP)** represented as **C\(_{14}\)H\(_8\)N\(_4\)**, with **500 SPP molecules** arranged around either a **hydrogen-terminated (5,5)@(10,10) double-walled CNT** (**26 Å** length, **~6.2 wt.%** filler) or an **AB-stacked double-layer graphene (DLG)** template (**26 Å × 24 Å**, **~4.6 wt.%**), giving **13 690** atoms (SPP/DWCNT) or **13 540** atoms (SPP/DLG). **Periodic boundary conditions** are applied in **all three directions**; the simulation cell is sized for initial composite densities of **~1.41 g cm⁻³** (SPP/DWCNT) and **~1.40 g cm⁻³** (SPP/DLG). **Equilibration** runs **~160 ps at 300 K**; **three independent trajectories** are branched from the **last 40 ps** of equilibration for statistics. **Carbonization** uses **NVT** MD with **heating rate 10 K ps⁻¹** in **three stages**: heat to **2200 K** then **anneal 2 ns**; heat to **2500 K** then **anneal 500 ps**; heat to **2800 K** then **anneal 750 ps**. **Nosé–Hoover** thermostat with **\(T_\text{damp}\) = 25 fs**; **time step 0.25 fs**. **Volatile gases** (**N\(_2\)**, **H\(_2\)**, **HCN**, **NH\(_3\)**) are **removed every 100 ps** during annealing to mimic experimental **byproduct purge**. **Total NVT annealing** time available for analysis is **3.25 ns** (three averaged runs). **N/A — barostat / external stress control**: protocol is **constant-volume NVT** with **no** stated **NPT** stage during the reported annealing ladder. **N/A — electric field**: not part of the described setup.

**2 — Force-field training.** **N/A — new parameterization in this article**: the authors use **published ReaxFF parameters** for **C/H/N/O** systems validated against **DFT/DFTB** in prior work, as summarized in their Methods section.

**3 — Static QM / DFT.** **N/A — production QM**: **DFT** appears as **prior validation literature** for the **ReaxFF** choice, not as the dynamics engine.

**4 — Review / non-simulation framing.** **N/A**: **primary** templating / carbonization study.

## Findings

**Outcomes and mechanisms.** Depending on **temperature** and **template chemistry**, the authors distinguish **physisorption-driven physical templating** versus **chemisorption-driven chemical templating**; **strong template–medium coupling** promotes **aligned graphitic** motifs in the fiber medium. **DWCNT templates** produce **more robust alignment** than **DLG (graphitic nanoplatelet)** templates under the simulated carbonization ladder, consistent with the **narrower high-ordering region** at the nanotube walls versus the broader, more fluctuating graphene stacks in their **ring-population** maps.

**Comparisons.** The manuscript links **atomistic ring statistics**, **radial distribution functions**, **hybridization**, and **interface density profiles** to **electron diffraction–style** observables for the **experimental** electrospun fibers discussed in the article.

**Sensitivity and design levers.** **Template topology** (DWCNT vs DLG), **distance from the filler surface** (they emphasize strong templating within **~4 Å** on the simulated timescales), and the **multi-stage temperature program** control whether **physical stacking** or **chemical coupling** dominates and how **six-membered** carbon rings accumulate near the filler.

**Limitations and outlook (as authored).** The authors note that **real carbonization** occurs over **hours** with **lower** temperatures than the **accelerated** MD program; **volatile removal** and **temperature ramps** are **emulations**, not identical reactor protocols.

**Corpus / PDF honesty.** The stable `paper_id` **`2017kowalik-venue-bez-tytu`** is a **legacy manifest slug**; the ingested PDF is **Saha et al., *Carbon* 2015** (DOI above). **`extraction_quality: partial`** in front matter reflects **short local extracts**; **tables, SI parts, and quantitative plots** should be read from the **PDF/SI** when extending beyond this summary.


## Limitations

ReaxFF remains an empirical reactive model: transferability across full industrial carbonization schedules and exact quantitative agreement with experiment are limited by force-field and sampling constraints, as in any large-scale pyrolysis simulation. Repository automation maps this stable `paper_id` to `normalized/papers/2017kowalik-venue-bez-tytu.json` and the repo-relative `pdf_path`. Where `extraction_quality` is partial, the tracked PDF and DOI remain the quantitative authority over short local extracts.

## Relevance to group

Demonstrates **ReaxFF** application to **carbonization / polymer pyrolysis** and **nanocarbon templating**, adjacent to broader reactive MD on carbon materials and interfaces in the corpus.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2015.07.048](https://doi.org/10.1016/j.carbon.2015.07.048) — *Carbon* **94** (2015) 694–704.

## Reader notes (navigation)

The stable `paper_id` **`paper:2017kowalik-venue-bez-tytu`** reflects a **legacy manifest slug**; the ingested PDF is **Saha et al., *Carbon* 2015**, not a 2017 “bez tytułu” placeholder. Maintainer corpus records document legacy slug-to-PDF pairings; the bibliography and DOI above identify Saha et al., *Carbon* (2015).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
