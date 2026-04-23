---
id: paper:2024baksa-adv-elect-ma-strain-fluctuations
type: paper
title: "Strain Fluctuations Unlock Ferroelectricity in Wurtzites"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - material:oxide
  - method:dft-static
  - task:application
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1002/aelm.202400567"
year: 2024
authors:
  - "Steven M. Baksa"
  - "Simon Gelin"
  - "Seda Oturak"
  - "R. Jackson Spurling"
  - "Alireza Sepehrinezhad"
  - "Leonard Jacques"
  - "Susan E. Trolier-McKinstry"
  - "Adri C. T. van Duin"
  - "Jon-Paul Maria"
  - "Andrew M. Rappe"
  - "Ismaila Dabo"
venue: "Adv. Electron. Mater. 2400567 (2024)"
pdf_sha256: "51810029d298a3f3d46d20cf328303cd69904f174818a6f34bbd4114708de54d"
pdf_path: "papers/Baksa_Adv_Elec_Mat_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024baksa-adv-elect-ma-strain-fluctuations -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Explains how **wurtzite (Zn,Mg)O**-class films can exhibit **switchable polarization** aided by **large local strain fluctuations** that **lower ferroelectric switching barriers** (claimed reductions **>40%** in the abstract narrative) and provides **joint experimental + computational** evidence using **ZnO/(Zn,Mg)O/ZnO** heterostructures with **interfacial strain gradients**. The study frames **strain heterogeneity** as a design knob for **scalable ferroelectrics** outside traditional perovskite or fluorite channels—relevant to **thin-film nonvolatile memory** where thickness scaling has been limiting. Conceptually, the work argues that spatially varying elastic fields can unlock polarization reversal even when uniform biaxial strain alone would leave coercive barriers too high for practical switching.

## Methods

### Epitaxial films and strain engineering (experiment)

**ZnO/(Zn,Mg)O/ZnO** heterostructures—**interfacial** **strain gradients** characterized per article (**open-access** **Adv. Electron. Mater.**).

### Static DFT barrier mapping (C)

**DFT** evaluates **polarization reversal barriers** vs **biaxial strain** and ties **local strain fluctuations** to **barrier** reductions (**Computational Details** + figures in **`papers/Baksa_Adv_Elec_Mat_2024.pdf`**).

**Strain-field construction (conceptual).** The heterostructure design creates **gradients** across **ZnO/(Zn,Mg)O** stacks so that **local** **biaxial** strain differs from **wafer-average** strain; **DFT** nudged-elastic-band or **climbing-image** pathways (as specified in the article) map how those **local** strains modify **coercive** barriers for **wurtzite** **polarization** reversal relative to **uniform** **strain** baselines.

**Static QM / DFT.** **Density functional theory** with **PBE**-class or as named in **Computational Details**; **Grimme**-style or **DFT-D**-type **vdW** corrections when included in the paper (**N/A** here if the wiki does not list the exact D3 flag). **Plane-wave**+**PAW** (or the article’s **basis**/**cutoff** convention) and a **k-point** mesh for **2D**/**bulk** subcells as tabulated. **NEB**/**CI-NEB** **reaction** paths and **formation** **energies** for **polarization** **barriers** versus **biaxial** **strain**—**properties** include **barrier** **heights**; **N/A** to duplicate full **DOS**/**band gap** tables on this page.

**MD application.** The publication is **DFT**+**experiment**-centric for **ferroelectric** **oxides**; **N/A**—no reported **NVT**/**NPT** **molecular-dynamics** production trajectories in the abstract-level summary (see **nudged-elastic** **band** **pathways** under **static** **QM**).

## Findings

Strain-gradient engineering can unlock measurable **polarization switching** pathways where uniform strain would retain higher barriers; fluctuations correlate with locally reduced barriers in the modeling presented, supporting the interpretation that engineered heterogeneity—not only chemistry—can enable wurtzite ferroelectric response.

**Comparisons, sensitivity, outlook.** The **Adv. Electron. Mater.** article **compares** **theory** and **epitaxial** **stacks** to expectations from uniform **biaxial** **strain**; **sensitivity** to **thickness** and local **strain** is central. **Open questions** include broader **wurtzite** chemistries, **defects**, and **frequency**-dependent switching—see **## Limitations**.

## Limitations

Materials-specific generality (other wurtzites, defect chemistry, frequency-dependent switching) requires case-by-case validation; quantitative coercive fields in devices depend on microstructure not fully captured in idealized models. The collaboration’s DFT emphasis also means domain walls, pinning, and leakage paths that appear in polycrystalline films are outside the scope of the ideal heterostructure story summarized here. **Open-access** **Wiley** formatting helps verify **strain** **maps** and **barrier** **estimates** against the **experimental** **ZnO/(Zn,Mg)O** **stacks** described in the article’s **Methods**.

## Relevance to group

**Van Duin** co-authorship links the group’s **atomistic modeling** muscle to a **ferroelectric oxide device** collaboration spanning Penn State, CMU, and Northwestern participants.

## Citations and evidence anchors

https://doi.org/10.1002/aelm.202400567 — Open-access Wiley article; Abstract/Introduction state the strain-fluctuation thesis.

## Reader notes (navigation)

- **DFT-forward** ferroelectric oxide study (not ReaxFF); use for cross-links from [[theme-2d-epitaxy-growth]] and device-oriented oxide hubs. Reactive MD lineage: [[reaxff-family]].

## Related topics

- [[reaxff-family]]
