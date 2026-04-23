---
id: paper:2018mao-venue-paper
type: paper
title: "Dynamics and kinetics of reversible homo-molecular dimerization of polycyclic aromatic hydrocarbons"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1063/1.5000534"
year: 2017
authors:
  - "Qian Mao"
  - "Yihua Ren"
  - "K. H. Luo"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys. 2017, 147, 244305"
pdf_sha256: "fb5d2d5a55c0654125cf644f46435ee3699f31991e8aded19941bafb1f0d660a"
pdf_path: "papers/Mao_Qian_JCP_2017_vol_147_iss_24_244305.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2018mao-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    The stable `paper_id` uses an `2018…` slug while the **version-of-record** is **J. Chem. Phys.** **147**, **244305** (**2017**).

## Summary

Soot nucleation models often invoke physical clustering of polycyclic aromatic hydrocarbons (PAHs) as a precursor step, but collisional stabilization depends on temperature, relative orientation, and whether dimers survive long enough to undergo subsequent chemistry. **ReaxFF molecular dynamics** is used to study **homogeneous collisions** of selected **PAHs** across **temperatures**, **impact parameters**, and **orientations**, quantifying **dimerization enhancement** factors and **dimer lifetimes** within a **capture radius** defined in the article, then extracting **forward/reverse rate constants** to build a **reversible** **kinetic** model that treats dimerization and redissociation on equal footing. The authors compare model predictions to **pyrene dimerization** experiments cited in the paper and argue **physical dimerization** is not a dominant channel under **typical flame** temperatures, i.e., the reversible kinetic picture suggests other pathways dominate soot precursor flux under high-temperature combustion conditions even when PAH–PAH collisions occur. Because the stable wiki slug uses an `2018…` prefix while the bibliographic year in the front matter is **2017**, operators should cite **`doi`** and **`venue`** fields when linking externally.

## Methods

### A — Force-field / interaction model

- **ReaxFF** parameterization appropriate for **hydrocarbon** **C/H** chemistry of **PAH** species (training scope and element coverage per **J. Chem. Phys.** **Methods**/**SI**).

### B — Molecular dynamics (bimolecular collisions)

- **Engine:** **LAMMPS** **ReaxFF MD** sampling **homomolecular** **PAH–PAH** **collisions** across **temperatures**, **relative** **orientations**, and **impact parameters** (full grid in the article).
- **Analysis:** **dimerization** **enhancement** factors vs **\(T\)** and **PAH** size; **dimer** **lifetimes** within a **capture-radius** construction defined in the paper; statistics vs **impact parameter**.

### C — Kinetic model calibration

- **Forward/reverse** **rate constants** extracted from **MD** feed a **reversible** **dimerization** framework; compared against **experimental** **pyrene** **dimerization** references cited by the authors.

### D — Experiments (literature)

- **Experimental** comparison points come from **published** **pyrene** data referenced in the article—not new laboratory work in this **JCP** paper.

### MD application (collision kinetics)

**Engine / code:** **LAMMPS** **ReaxFF MD** of **bimolecular PAH–PAH** encounters. **System & composition:** homomolecular **PAH** pairs spanning the size/temperature grids in **Methods** (**atom** counts per collision complex in the article). **Ensemble:** **NVE**/**NVT**-style collision sampling as defined for the bimolecular encounter protocol in **Methods** (exact label per stage in **PDF**). **PBC / timestep / thermostat / barostat / electric field:** **N/A — not transcribed** in this excerpt-based note—import from **J. Chem. Phys.** **147**, **244305** (2017) **Methods** (`papers/Mao_Qian_JCP_2017_vol_147_iss_24_244305.pdf`). **Temperature:** scanned across the **temperature** grid used to extract **forward/reverse** rate constants (see article tables). **Duration:** collision sampling staged to capture **dimer** formation and **redissociation** within the **capture-radius** construction defined in the paper. **Pressure:** **N/A — gas-phase collision** setup without external **hydrostatic** control in the abstract framing. **Enhanced sampling:** **N/A — not indicated** for the collision workflow summarized in the abstract.
## Findings

- **Enhancement factors** for **homomolecular dimerization** are **larger** at **lower T** and for **smaller** PAHs (not **size-independent** in the reported fits).
- **Dimer lifetime** within the **capture** framework **decreases** as **impact parameter** increases.
- The derived **reversible** model matches the **qualitative** **experimental** **trend** cited for **pyrene**, and the authors conclude **physical dimerization** is unlikely to dominate at **high flame** temperatures.

**Comparisons.** The **reversible kinetic** model is cross-checked against literature **pyrene dimerization** experiments cited in the paper (J. Phys. Chem. Lett. reference in the abstract).

**Sensitivity.** **Enhancement factors** grow at **lower T** and for **smaller PAHs**; **dimer lifetime** within the **capture radius** falls as **impact parameter** increases—both are explicit **parameter** trends in the abstract.

**Outlook / limitations.** The abstract argues **physical dimerization** cannot dominate under **typical flame** conditions, implying **chemical** routes carry more of the soot-precursor flux.

**Corpus honesty.** Stable wiki slug uses **`2018…`** while the **VOR** is **2017**—cite **`doi`/`venue`** externally; consult the **PDF** for any quantities not reproduced here.
## Limitations

- **Extract coverage** in `normalized/extracts` is **partial**; consult the **PDF** for **full** numerical tables and **additional** PAHs.

## Relevance to group

**Group-linked** **ReaxFF** application to **soot**/**PAH** **clustering** **kinetics** relevant to **combustion** modeling.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1063/1.5000534](https://doi.org/10.1063/1.5000534)

## Reader notes (navigation)

- PAH/soot kinetics: [[theme-pyrolysis-combustion-organics]]; slug note: **JCP 2017** article registered under `2018…` filename—see front matter venue/year.

## Related topics

- [[reaxff-family]]
