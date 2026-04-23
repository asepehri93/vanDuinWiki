---
id: paper:2017tan-scientific-r-enhancing-oxidation
type: paper
title: "Enhancing the Oxidation of Toluene with External Electric Fields: a Reactive Molecular Dynamics Study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1038/s41598-017-01945-4"
year: 2017
authors:
  - "Shen Tan"
  - "Tao Xia"
  - "Yao Shi"
  - "Jim Pfaendtner"
  - "Shuangliang Zhao"
  - "Yi He"
venue: "Scientific Reports 7, 1710 (2017)"
pdf_sha256: "e9288dd957449c571f1ff900de4388cd1d52ff029943599c4f76f50244b74570"
pdf_path: "papers/ReaxFF_others/Tan_Pfaendter_Scientific_Reports_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017tan-scientific-r-enhancing-oxidation -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **Sci. Rep.** (**DOI** in front matter). Field strengths, temperatures, and comparative rate statements should be verified against the **article** text.

## Summary

The authors use **ReaxFF molecular dynamics** to study **high-temperature oxidation** of **toluene** in periodic simulation cells under **externally applied electric fields**, comparing **field-on** and **field-off** trajectories across a range of **temperatures** and **field magnitudes**. The motivation is **combustion-related** chemistry where **electric fields** can couple to **polar** transition regions and **charged** species, but where **affordable** simulation tools must still capture **bond rearrangement**. The study reports that fields can **accelerate oxidation**, shorten **induction times** before sustained reaction, and enable oxidation at **lower temperatures** than comparable **zero-field** runs—interpreting these trends in terms of **radical** formation and **field-assisted** molecular **polarization** pathways.

## Methods

### 1 — MD application (atomistic dynamics)

**ReaxFF molecular dynamics** in **LAMMPS** studies **high-temperature oxidation** of **toluene** in **periodic** cells with **externally applied electric fields (E-fields)**, comparing **field-on** vs **field-off** trajectories across multiple **temperatures** and **field magnitudes** (*Sci. Rep.* **7**, **1710**; DOI in front matter). The indexed extract `normalized/extracts/2017tan-scientific-r-enhancing-oxidation_p1-2.txt` states qualitative **kinetic** trends but not the full protocol table—confirm **Δt**, **thermostat**, and **run lengths** in **`pdf_path`**.

- **Engine / code:** **LAMMPS** + **ReaxFF** (article text; **reactive MD** terminology in abstract).
- **System size & composition:** **Toluene** + **oxidizer** mixture in **3D periodic** gas-phase cells (stoichiometry and box vectors in article **Methods**).
- **Boundaries / periodicity:** **3D PBC** (standard for homogeneous gas-phase **ReaxFF** oxidation cells).
- **Ensemble:** **NVT-class** thermalized runs as described in the article (exact label on PDF).
- **Timestep:** **N/A** — **Δt (fs)** not stated in the indexed excerpt.
- **Duration / stages:** **N/A** — equilibration vs production **ps/ns** not stated in the indexed excerpt.
- **Thermostat:** **N/A** — not stated in the indexed excerpt.
- **Barostat:** **N/A** — **constant-volume** **NVT** oxidation; no **NPT** barostat summarized on indexed pages.
- **Temperature:** **2100 K** and **2900 K** appear in the abstract’s illustrative **field-on/field-off** comparison; additional **T** sweeps are in the article body.
- **Pressure:** **N/A** — isochoric **NVT** gas-phase runs (no hydrostatic **NPT** control summarized here).
- **Electric field:** **Static / piecewise-static E-fields** applied to accelerate/polarize chemistry; abstract reports stronger fields yield faster oxidation and shorter **induction** times.
- **Replica / enhanced sampling:** **N/A** — brute-force **ReaxFF** trajectories.

### 2 — Force-field training

**N/A** — the study **uses** a published **combustion-oriented ReaxFF** parametrization with **fixed partial charges**; authors note **PQEq-class** polarizable charge refinements as future work for strong-field polarization.

### 3 — Static QM / DFT-only

**N/A** — **QM** is cited for conceptual background on **E-field** effects, not as the production **oxidation** engine.

## Findings

### Outcomes and mechanisms

**E-fields** can **greatly enhance** **toluene oxidation** rates, shorten **induction** times before sustained reaction, and even enable oxidation at **2100 K** that **does not occur** without a field in the same setup; the abstract further states **2100 K** field-on kinetics can resemble **~2900 K** field-off kinetics, interpreted as **boosted initial radical generation** without strongly favoring one oxidation channel.

### Comparisons

Comparisons are primarily **field-on vs field-off** at matched **temperature** and composition, plus **temperature** sweeps implied by the multi-**T** discussion in the article.

### Sensitivity / design levers

**Field magnitude** and **temperature** jointly control **oxidation rate** and **radical** onset; **fixed partial charges** may underrepresent **polarization** under very strong fields—authors highlight **PQEq**-class upgrades as a modeling lever.

### Limitations and corpus honesty

**High-temperature** conditions accelerate chemistry relative to ambient **combustion**; **quantitative** barriers and **species** timelines must be taken from **`pdf_path`**, not the abstract-only excerpt mirrored here.

## Limitations

**Fixed-charge** **ReaxFF** may understate **field-induced** **electronic polarization**; **quantitative** barriers for selected steps should be checked with **QM** where feasible. Elevated **temperatures** accelerate chemistry and may differ from **low-temperature** combustion regimes.

The paper’s explicit mention of **PQEq**-class refinements is important for **operators**: if a user question assumes **strong-field** chemistry in **polar** media, cite this work as precedent for **charge** model upgrades—not as proof that **standard ReaxFF** alone is sufficient.

## Relevance to group

Demonstrates **ReaxFF** applied to **field-modified** **gas-phase** **oxidation** chemistry—useful for connecting **reactive MD** to **plasma**/**electrostatic** perturbation discussions adjacent to **combustion** and **kinetics** themes.

## Citations and evidence anchors

- DOI [10.1038/s41598-017-01945-4](https://doi.org/10.1038/s41598-017-01945-4).
- Excerpt alignment: `normalized/extracts/2017tan-scientific-r-enhancing-oxidation_p1-2.txt`.

## Related topics

- [[reaxff-family]]
