---
id: paper:2014han-venue-supporting-information
type: paper
title: "Supporting information: atomistic observation of the lithiation and delithiation behaviors of silicon nanowires using reactive molecular dynamics simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:batteries-interfaces
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: ""
year: 2014
authors:
  - "Han, Sang Soo"
venue: ""
pdf_sha256: "d52282ef04a5a1c5f4ddfcff96a36b0ae1fa68bae075a8658db4c4f18842d652"
pdf_path: "papers/ReaxFF_others/Han_LiSi_JPC_2015_SI.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014han-venue-supporting-information -->

## Evidence and attribution

!!! note "Authority of statements"

    This slug registers **supporting information** PDF bytes. Narrative claims about the main study should be checked against the **primary article PDF**, not SI alone.

## Summary

SI documents development of a Li–Si ReaxFF parametrization: DFT training on Li₄Si clusters and several LiₓSi crystals; B3LYP/6-311G** cluster data in Q-Chem; periodic PBE (VASP) equations of state and Bader charges for charge-fitting; successive one-parameter search optimization. Parameters build on prior Si and Li ReaxFF sets with new Li–Si bond terms (extract section S1).

## Methods

Section **(S1)** documents **ReaxFF optimization for Li–Si** against a **DFT training set**: **cluster** data for a **Li\(_4\)Si** molecule (**B3LYP/6-311G** in **Q-Chem**) and **periodic PBE (VASP)** **equations of state** and **Bader charges** for several **thermodynamically stable Li\(_x\)Si** crystals (**Li\(_{21}\)Si\(_5\)**, **Li\(_{15}\)Si\(_4\)**, **Li\(_{13}\)Si\(_4\)**, **Li\(_7\)Si\(_3\)**, **Li\(_{12}\)Si\(_7\)**, **LiSi**). **Plane-wave PBE** calculations use a **400 eV** cutoff and **11×11×11** **Monkhorst–Pack** **k**-mesh for energy convergence. **Coulomb-related ReaxFF terms** are fitted using **Bader charges** from the **DFT** densities. Optimization uses a **successive one-parameter search**. The Li–Si development **starts from** existing **Si** (**van Duin et al.**) and **Li** (**Han et al.**) ReaxFF subsets, but **Li–Si bond parameters are newly derived** for this work; parameters appear in **Table S1** (SI pages S1–S2; extract).

### 1 — MD application (parent-article nanowire simulations)

- **Engine / code:** **N/A in this SI excerpt**; the parent article’s **Si nanowire lithiation** **ReaxFF** trajectories are described on **`[[2015han-venue-atomistic-observation]]`** using **LAMMPS** **molecular dynamics** workflows (`papers/ReaxFF_others/Han_LiSi_JPC_2015.pdf`).
- **System size & composition:** **N/A in SI §S1** for nanowire **atom** counts; SI focuses on **Li–Si** **QM** training cells (**Li\(_4\)Si** **cluster** and **Li\(_x\)Si** crystals) containing **tens to hundreds of atoms** per formula unit stack (extract).
- **Boundaries / periodicity:** **3D PBC** for **VASP** **PBE** **EOS** grids on **Li\(_x\)Si** crystals (extract).
- **Ensemble (production MD):** **N/A —** not specified in SI §S1; see parent article for **NVT**/**NPT** choices.
- **Timestep / duration / thermostat (production MD):** **N/A —** not specified in SI §S1; see parent article for **fs** timestep and **ps**/**ns** segments.
- **Barostat / pressure (production MD):** **N/A — hydrostatic pressure** control is **not** described in SI §S1; confirm in parent article.
- **Temperature (production MD):** **N/A —** not described in SI §S1; parent article lists operating **temperatures**.
- **DFT reference temperature:** **PBE** **EOS** energies are **0 K** **DFT** total energies on **k**-meshed **Brillouin-zone** samples (extract).

### 2 — Force-field training (Li–Si ReaxFF extension)

- **Parent FF / elements:** extends prior **Si** (**van Duin et al.**) and **Li** (**Han et al.**) **ReaxFF** subsets with **new Li–Si bond parameters** (SI §S1).
- **QM reference (clusters):** **B3LYP/6-311G** in **Q-Chem** on **Li\(_4\)Si** (extract).
- **QM reference (periodic):** **PBE** **plane-wave** **VASP** **EOS** and **Bader charges** for listed **Li\(_x\)Si** crystals; **400 eV** cutoff, **11×11×11** **Monkhorst–Pack** **k**-mesh (extract).
- **Training observables:** **EOS** energies/charges for crystals; cluster data for **Li–Si** bonding (extract).
- **Optimization:** **successive one-parameter search** updating **ReaxFF** parameters (extract).
- **Tables:** **Table S1** lists fitted coefficients (SI).

## Findings

### 1 — Outcomes (SI scope)

The SI states explicitly that **Si** and **Li** parameters from prior fits were reused as a base, while **terms governing Li–Si bonds were newly trained** to support the **nanowire lithiation/delithiation** reactive MD study in the parent article (SI text; extract pages S1–S2).

### 2 — Comparisons

- **Bader-charge**-guided **Coulomb** terms are tied to **DFT** **Bader** analysis so **Li–Si** **bond-order** parameters track **QM** without refitting the entire **Si**/**Li** subsets (extract).

### 3 — Sensitivity

**N/A —** not applicable at SI parameter-documentation level.

### 4 — Limitations / outlook

SI documents **QM fits**, not full **device-scale** **electrode** workflows—see parent article.

### 5 — Corpus / KB honesty

This page summarizes **SI** pages **S1–S2** only (`normalized/extracts/2014han-venue-supporting-information_p1-2.txt`); do not treat it as the **version-of-record** article record.

## Limitations

SI is not a standalone experimental or methods paper; figures and tables are auxiliary to the parent article. **Nanowire** **lithiation** **simulations** in the **parent** work may use additional **electrode** **boundary** **conditions** beyond the **parameter** **development** excerpts summarized here; treat this page as **QM-fit** documentation, not a substitute for the **full** **reactive** **MD** **protocol** in the **main** **PDF**. **Table S1** **coefficients** must be copied **verbatim** into **input** **decks** with **consistent** **units** for your **ReaxFF** **software** **flavor**.

## Reader notes (navigation)

Primary article PDF in this corpus: [[2015han-venue-atomistic-observation]] (`papers/ReaxFF_others/Han_LiSi_JPC_2015.pdf`).
- Maintainer catalog (SI-first ingests): [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) section **A** (analogous SI roles).

## Citations and evidence anchors

- `normalized/extracts/2014han-venue-supporting-information_p1-2.txt` (SI pages S1–S2).

## Related topics

- [[2015han-venue-atomistic-observation]]
- [[reaxff-family]]
