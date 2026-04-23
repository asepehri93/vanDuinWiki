---
id: paper:2014guang-yue-li-energy-fuels-ef501156b
type: paper
title: "Pyrolysis mechanism of metal-ion-exchanged lignite: a combined reactive force field and density functional theory study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:dft-static
  - keyword:reactive-md
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: "10.1021/ef501156b"
year: 2014
authors:
  - "Li, Guang-Yue"
  - "Xie, Quan-An"
  - "Zhang, Hang"
  - "Guo, Rui"
  - "Wang, Feng"
  - "Liang, Ying-Hua"
venue: "Energy & Fuels"
pdf_sha256: "332abea46d19736b7013fa396d4f06bc84d81c99a435b0641cb31f224c287b69"
pdf_path: "papers/ReaxFF_others/Li_Ca_pyrolysis_Energy_Fuels_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014guang-yue-li-energy-fuels-ef501156b -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

**Ion-exchanged lignites** pyrolyze differently from **H-form** coals because **Ca²⁺** and **hydroxides** redirect **proton-transfer** sequences that gate **carboxyl** and **phenolic** chemistry. The **Energy & Fuels** framing targets **low-rank** **coal** **utilization** questions where **ion** **content** is **technologically** **controlled** through **washing** or **mineral** **additives**, making **Ca(OH)\(_2\)** a **pragmatic** **proxy** for **field** **samples** rather than an **exotic** **academic** **constraint**. **Li** et al. compare **three-dimensional Wender-type lignite** models **without** versus **with Ca(OH)\(_2\)** using **ReaxFF MD** at **1000–2000 K** for **300 ps** trajectories that capture **early-stage** bond cleavage. **DFT** on **representative fragments** distinguishes **homolytic** versus **heterolytic** **O–H** and **C–O** scission promoted by **Ca**-coordinated **bases**, rationalizing why **metal addition** **accelerates** pyrolysis relative to the **base** macromolecule.

## Methods

### Structural models (lignite surrogates)

- **Three-dimensional Wender-type lignite** models are built with **oxygen-rich** **aliphatic** and **aromatic** motifs representative of **low-rank** coals, comparing **H-form** vs **Ca(OH)\(_2\)**-containing variants (**Summary**).

### Reactive MD (ReaxFF)

- **ReaxFF MD** runs **300 ps** trajectories at **1000–2000 K** in **NVT**-style segments (timestep/thermostat per **Energy & Fuels** Computational details) to capture **early-stage** bond cleavage and **volatile** release chemistry (**Summary**).

### Static QM benchmarks (DFT)

- **DFT** with **hybrid** functionals and basis sets documented in the article evaluates **bond dissociation energies** and **product** stabilities for **carboxylate**, **phenoxide**, and **ether** fragments sampled from **MD** snapshots (**Summary**).

### Scope limits

- The **300 ps** window emphasizes **early pyrolysis** rather than **long-time char maturation**; **minerals** beyond the **Ca** proxy are not represented.

### 1 — MD application (ReaxFF pyrolysis)

- **Engine / code:** **LAMMPS** **molecular dynamics** with **ReaxFF** as described in **Energy & Fuels** (confirm exact engine string in **`pdf_path`**).
- **System size & composition:** **3D Wender-type lignite** macromolecular assemblies with and without **Ca(OH)\(_2\)**; atom totals are given in the Computational details (**thousands of atoms** typical for such reactive cells—confirm in PDF).
- **Temperature / duration:** **300 ps** segments at **1000–2000 K** (summary bullets above).
- **Boundaries / periodicity:** **3D PBC** cells are standard for these bulk **pyrolysis** models—confirm in **`pdf_path`**.
- **Ensemble / thermostat / timestep / barostat:** **NVT** **molecular dynamics** is stated for the **MD** portion; thermostat and **Δt** are in Computational details (**N/A here** beyond the **NVT** label).
- **Pressure / stress control:** **N/A — hydrostatic pressure** control is **not** summarized in the excerpt used here; confirm if any **NPT** segments appear in the PDF.
- **Electric field / metadynamics:** **N/A —** not used in the summarized protocol.

### 2 — Force-field training

**N/A —** applies an existing **ReaxFF** description to **lignite** models (parameter lineage in the article).

### 3 — Static QM (DFT benchmarks)

- **DFT** on **representative fragments** from **MD** snapshots evaluates **BDEs** and **product** stabilities for **carboxylate**, **phenoxide**, and **ether** motifs (**Summary**); full functional/basis settings are in the article.

## Findings

### 1 — Outcomes and mechanisms

**Decarboxylation** and **bridged C–O** cleavage dominate **first-picosecond** chemistry in both models, consistent with the **high oxygen** content of the **Wender** construction. **Ca(OH)\(_2\)** facilitates **deprotonation** of **carboxylic** and **phenolic** sites, steering scission from **radical** pathways toward **heterolytic** channels with **lower** **BDEs** and **stabilized** **ionic** products. The combined **MD + DFT** argument explains **accelerated** **mass loss** in **Ca-exchanged** simulations without invoking new **elementary** steps absent from the **H-form** model—only **lower** **barriers** and **shifted** **branching** ratios.

### 2 — Comparisons

- **Ca-containing** vs **H-form** **Wender** models; **DFT** interprets **homolytic** vs **heterolytic** channels (**Summary**).

### 3 — Sensitivity

- **Temperature** window **1000–2000 K** for the **300 ps** **ReaxFF** trajectories (summary).

### 4 — Limitations / outlook

- **Wender** structural simplification vs real **mineral** matter; see **## Limitations**.

### 5 — Corpus / KB honesty

- **TGA**-level validation and quantitative **mass-loss** traces must be taken from **`pdf_path`**, not this summary alone.

## Limitations

Coarse-grained structural models omit full mineral matter complexity; ReaxFF does not resolve electronic structure explicitly.

## Citations and evidence anchors

- DOI `10.1021/ef501156b` (extract footer).
- Abstract (extract page 1).

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
