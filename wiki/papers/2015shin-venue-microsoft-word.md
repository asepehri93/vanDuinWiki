---
id: paper:2015shin-venue-microsoft-word
type: paper
title: "Supporting information — Fe/Cr/O/S ReaxFF; butane oxidation on Cr₂O₃ and pyrite-modified Cr₂O₃"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - material:oxide
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:lammps
  - keyword:reactive-md
  - keyword:combustion
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1021/acscatal.5b01766"
year: 2015
authors:
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
venue: "ACS Catalysis (Supporting Information)"
pdf_sha256: "1e3a445d1ab1488c3900dd0807112231ea3cad955d445f5e19ca86aa6ed65080"
pdf_path: "papers/Shin_ACS_Catalysis_2015_SI.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015shin-venue-microsoft-word -->

## Evidence and attribution

!!! note "Authority of statements"

    This page registers an **SI PDF** (`pdf_path`). Integrated scientific narrative, full **Computational Methods**, and bibliography for the study belong on the **main article** page [[2015shin-venue-research-2]] (and the alternate main-PDF slug [[2015shin-venue-research]]). Below summarizes **SI-visible** figure-caption content in this workspace’s short extract.

## Summary

Supporting Information for the **ACS Catalysis** article (DOI `10.1021/acscatal.5b01766`) packages **initial configurations**, **equations-of-state** checks for **Cr** crystal phases, and **NVT-MD** figure series tracking **oxidation product counts**, **hydroxyl** formation, **low-coordination Cr**, **reactive oxygen**, and **sulfur release** for **butane** oxidation scenarios on **Cr₂O₃** with and without **pyrite (FeS₂)**. The SI captions tabulate **temperatures** such as **2500 K** product evolution for **C₄H₁₀/O₂**, **1000 K** snapshots for **dehydrogenation on Cr-oxide**, **1600 K** time series comparing **clean** versus **pyrite-modified** oxide, and a **2000 K** **sulfur-release** panel for **pyrite dehydrogenation without O₂**.

## Methods

**What the SI documents (caption-level).** **Figure S1** defines **initial geometries** for **(a) C₄H₁₀/O₂**, **(b) C₄H₁₀/O₂/Cr₂O₃**, and **(c) C₄H₁₀/O₂/Cr₂O₃/FeS₂** with element color coding. **Figure S2** reports **0 K equations of state** for **bcc/fcc/a15 Cr**; **bcc Cr cohesive energy** is **93.7 kcal/mol** in **ReaxFF** versus **94.6 kcal/mol** experiment and **93.9 kcal/mol** QM in the caption text. **Figures S3–S9** summarize **NVT-MD** observables at the **temperatures stated in each caption** (e.g., **2500 K** product counts; **1000 K** dehydrogenation illustration; **1600 K** hydroxyl / carbon-bound intermediates / reactive oxygen / coordination statistics; **2000 K** sulfur release without **O₂**).

**MD application (SI-visible protocol hooks).** **Engine:** the parent **ACS Catalysis** article documents the **molecular dynamics** software used for these **ReaxFF** trajectories (see [[2015shin-venue-research-2]] and **`pdf_path`**). **System composition:** **atomistic** **C₄H₁₀/O₂** gas cells plus **Cr₂O₃** and **FeS₂/Cr₂O₃** **slab** supercells as illustrated in **Figure S1** (atom counts on **`pdf_path`**). **Boundaries:** **three-dimensional periodic boundary conditions (PBC)** for the **slab** models as in the main **Computational Methods**. **Ensemble:** **NVT** in the captioned **MD** panels. **Duration:** captioned runs accumulate statistics over **production** segments whose **lengths** (ps/ns) are defined in the main text/SI tables, not on this caption-only extract. **Thermostat:** **NVT** implies a thermostat implementation specified in **`pdf_path`**. **Timestep:** **fs** timestep values appear in the main article/SI parameter tables. **Barostat:** **N/A** for the **NVT** SI panels summarized here. **Pressure:** **N/A** — **NVT** gas/surface runs without stated **hydrostatic pressure** control in the SI caption excerpt. **Electric field / enhanced sampling:** **N/A** unless the full SI documents them.

**Force-field training narrative:** SI points to **Fe/Cr/O/S ReaxFF** parameter tables and validation plots alongside these figures; the **QM training level** and **optimization workflow** are described in the **main text**, not replaced here.

**Static QM / DFT production:** **N/A** for the SI package itself (QM enters as training reference in the parent article).

## Findings

**Validation against reference data:** **Figure S2** reports **0 K equations of state** for **bcc**, **fcc**, and **a15 Cr**; the SI caption quotes a **bcc Cr cohesive energy** of **93.7 kcal/mol** from **ReaxFF**, compared with **94.6 kcal/mol** experiment and **93.9 kcal/mol** **QM** in the same caption text—serving as a compact **benchmark** of the **Fe/Cr/O/S** parameterization alongside the plots.

**Oxidation and surface chemistry (caption-level):** Time series and snapshots in **Figures S3–S9** track **oxidation product counts**, **hydroxyl** formation, **low-coordination Cr**, **reactive oxygen**, and **sulfur release** for **butane**-related setups on **Cr₂O₃** with and without **pyrite (FeS₂)**. The SI therefore documents how **surface oxygen** participates in **dehydrogenation** and subsequent **C–O** coupling at the **atomistic** level, complementing the narrative conclusions stated in the **main article** abstract.

**Comparisons across panels:** Captions contrast **clean** versus **pyrite-modified** chromia under matched **NVT** protocols, highlighting increased **SOH**-related signatures and **sulfur release** on the **modified** surface relative to **clean** **Cr₂O₃** in the illustrated trajectories.

**Sensitivity to temperature and stoichiometry:** The SI calls out representative **temperature** windows such as **2500 K** product evolution for **C₄H₁₀/O₂**, **1000 K** snapshots for **dehydrogenation on Cr-oxide**, **1600 K** time series comparing **clean** versus **pyrite-modified** oxide, and **2000 K** **sulfur-release** behavior for **pyrite dehydrogenation without O₂**—showing how the authors scan **thermal** conditions to expose different **reaction** branches.

**Limitations of an SI-only digest:** This wiki page cannot restate every **figure** panel or **time** axis; quantitative counts and full **mechanistic** claims require the **PDF** figures and the **version-of-record** article discussion, not caption fragments alone.

## Limitations

This page is **SI-only**; figure captions are not a substitute for the **peer-reviewed main article** mechanism discussion on [[2015shin-venue-research-2]]. **SI** is not a substitute for **integrated** interpretation in the **main text**. **High-temperature** panels probe **kinetically dominated** channels that may differ from **low-temperature catalytic steady states**. **Ideal slab** models may omit **particle** and **support** complexity.

## Relevance to group

**Penn State / CFDRC** **Fe/Cr/O/S ReaxFF** work on **coal-relevant** **sulfur** chemistry at **oxide** catalyst interfaces.

## Citations and evidence anchors

- Parent article DOI `10.1021/acscatal.5b01766`; SI: `papers/Shin_ACS_Catalysis_2015_SI.pdf`.
- `normalized/extracts/2015shin-venue-microsoft-word_p1-2.txt`.

## Related topics

- [[2015shin-venue-research-2]]
- [[reaxff-family]]
