---
id: paper:2019kwon-fuel-correct-numerical-simulations
type: paper
title: "Numerical simulations of yield-based sooting tendencies of aromatic fuels using ReaxFF molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.fuel.2019.116545"
year: 2019
authors:
  - "Hyunguk Kwon"
  - "Sharmin Shabnam"
  - "Adri C. T. van Duin"
  - "Yuan Xuan"
venue: "Fuel (2019), corrected proof, article 116545"
pdf_sha256: "8c7353e44798d865ca22090ecbec03d6cfa40a400f308afc2fede75c1ecb5662"
pdf_path: "papers/Kwon_Fuel_2019_online.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019kwon-fuel-correct-numerical-simulations -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The work presents a ReaxFF molecular dynamics workflow to compute the experimental Yield Sooting Index (YSI) for fuels, using a multi-stage procedure designed to mirror how YSI is obtained experimentally and in continuum models. Toluene and phenol are used as proof-of-concept aromatics with relatively well-characterized chemistry. Simulations capture key growth pathways expected from kinetics (toluene retaining and growing aromatic rings; phenol involving carbon-loss pathways with CO release). A quantitative YSI construction from ReaxFF output is compared to measurements with reasonable agreement, arguing that the approach can rank sooting tendency when detailed kinetic mechanisms are unknown. The introduction contrasts **kinetic-model** YSI workflows (accurate but mechanism-dependent) with **group-additivity** estimators (fast but weak when carbon types are underrepresented), positioning **ReaxFF** as a middle path for **unknown** fuel chemistry.

## Methods

This slug uses the **text-layer** *Fuel* file **`papers/Kwon_Fuel_2019_online.pdf`**. **Methods** and **citable** **numerical** **settings** are **in** *Fuel* **Sec. 2–4**; the **brief** **below** **paraphrases** the **VOR** **(DOI** in **front** **matter**)**.

### 1 — MD application (ReaxFF, multi-stage NVT)

**ReaxFF** with the **CHO-2016** **field** **([39]**, *Fuel* **Sec. 2**). **System (stage 1):** **3D** **PBC** **cubic** **~38.6** **Å** with **~2300+** **atoms** **(CH₄**/**O₂,** **ρ=0.28** **kg/dm³,** **equivalence** **ratio** **3.5,** *Fuel* **Sec. 2**)**. **NVT** **stages** **(temperatures):** **1500** **K** **(25** **ps)**; **3000** **K** **(Berendsen,** **100** **fs** **damping)** **until** **max** **radical** **count**; then **doped** **pools** **~2308** or **~2224** **atoms** **(ρ** **~0.39** **kg/dm³)** with **42** **benzyl** or **phenoxy**; **final** **NVT** at **2200 K, 2400 K, 2600** **K** **(five** **replicas**). **Production** **durations** **(Sec. 4.1):** **e.g. ~6** **ns** @ **2200** **K**, **~3.5** **ns** @ **2400** **K**, **~2** **ns** @ **2600** **K** **(plateau** **criterion** **in** **Sec. 4.1**)**. **Time step (fs):** **N/A** in the **PDF** text extracted here; use the **VOR** **Methods** (or **SI** if any) for **reproduction**-**grade** **integration** **settings**. **MD program name:** **N/A** in our **string** **search** of the **local** **PDF** (no **explicit** **“LAMMPS”** in **that** **extract**). **Barostat** / **NPT** **(mean** **hydrostatic** **stress)**: **N/A** for the **NVT-**staged **YSI** **RMD** **(Sec. 2).** **Electric** **field** / **replica** / **metadynamics:** **N/A**.

### 2 — Force-field training

**N/A**—the paper **uses** **CHO-2016** **([39]**; **improvement** on **CHO-2008** **per** **Sec. 2** **narration**) and does **not** **re-fit** a **new** **field** **in** **this** **article**.

### 3 — Static QM / DFT

**N/A**—**atomistic** **chemistry** is **ReaxFF**-**only**; **prior** **kinetic** **literature** is **cited** for **phenol** / **aromatic** **mechanism** **context** **(Sec. 1** **&** **4**)**.

## Findings

### Mechanisms

**Toluene** pathways emphasize **aromatic** **growth** while **retaining** rings; **phenol** shows **aromatic** growth with **CO**-forming **carbon-loss** channels—aligned with **prior** **kinetic** understanding quoted in the paper.

### Quantitative outcome

**ReaxFF YSI** values match **experimental** YSI **reasonably** for the **proof-of-concept** set—the article positions this as a **first** **quantitative** **YSI** framework from **ReaxFF** **MD**.

### Future directions (from abstract)

Extension toward **fuels** with **unknown** or **poorly known** **detailed** **kinetics** (e.g. complex **transportation** or **bio-derived** streams) is the stated motivation.

### Sensitivity and cross-checks

**Relative** **sooting** **ranking** depends on how **trajectory** **cuts** map to the **YSI** **scalar**; the **paper** compares **ReaxFF** **YSI** to **tabulated** **experimental** **YSI** for **toluene** and **phenol** (**agreement** described as **reasonable** in the **abstract**). **Temperature** and **stage** **duration** are **levers** in **high-temperature** **RMD**; **numeric** **values** belong in the **Methods** **tables** of the **PDF**, not invented here.

### Corpus note

Use this **online** **PDF** slug for **reproducibility**; **proof** **PDF** **sibling** **[[2019kwon-venue-paper]]** may differ in **pagination** (**version-of-record** **integrity**).
## Limitations

Demonstration is limited to two aromatic compounds; extension to broader fuel spaces, blend effects, and quantitative error bars requires further validation. YSI mapping from atomistic trajectories introduces modeling choices that may not transfer unchanged to all fuel classes.

## Relevance to group

Co-authored from Penn State mechanical engineering; extends group capabilities in ReaxFF-based combustion and soot precursor chemistry relevant to fuels and emissions modeling.

## Citations and evidence anchors

Primary locator: `papers/Kwon_Fuel_2019_online.pdf` — abstract and methods for YSI protocol and toluene/phenol results. DOI: https://doi.org/10.1016/j.fuel.2019.116545

## Related topics

- [[2019kwon-venue-paper]] (uncorrected proof PDF of the same article)
- [[reaxff-family]]
