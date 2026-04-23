---
id: paper:2023zhu-nat-step-engineering
type: paper
title: "Step engineering for nucleation and domain orientation control in WSe2 epitaxy on c-plane sapphire"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - task:experiment-integrated
  - method:dft-static
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:oxide-surface
  - keyword:validation-experiment
candidate_tags:
  - "MOCVD-TMD"
source_refs: []
doi: "10.1038/s41565-023-01456-6"
year: 2023
authors:
  - "Haoyue Zhu"
  - "Nadire Nayir"
  - "Tanushree H. Choudhury"
  - "Anushka Bansal"
  - "Benjamin Huet"
  - "Kunyan Zhang"
  - "Alexander A. Puretzky"
  - "Saiphaneendra Bachu"
  - "Krystal York"
  - "Thomas V. McKnight"
  - "Nicholas Trainor"
  - "Aaryan Oberoi"
  - "Ke Wang"
  - "Saptarshi Das"
  - "Robert A. Makin"
  - "Steven M. Durbin"
  - "Shengxi Huang"
  - "Nasim Alem"
  - "Vincent H. Crespi"
  - "Adri C. T. van Duin"
  - "Joan M. Redwing"
venue: "Nature Nanotechnology"
pdf_sha256: "782dc53a1c16d3cbdaf7d7d2d38e85350a0399488d33186cb568c0c5e2d7c31d"
pdf_path: "papers/Zhu_Nayir_step_engineer_Nature_Nanotech_2023_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023zhu-nat-step-engineering -->

!!! note "Corpus note"
    The corpus PDF is a **galley**; prefer the **Nature Nanotechnology** version-of-record for citation.

## Summary

**Epitaxial** growth of **two-dimensional transition metal dichalcogenides** on **sapphire** is a leading strategy toward **wafer-scale** films with controlled **orientation**, because **atomic steps** on the substrate can both **anchor nucleation** and bias **in-plane** alignment, thereby reducing **mirror-twin** grain boundaries that degrade devices. This article reports **metal–organic chemical vapour deposition (MOCVD)** of **monolayer WSe\(_2\)** on **c-plane sapphire** and argues that **step engineering** must be understood together with **sapphire surface chemistry**: changing growth conditions alters the **chemistry** of the **Al\(_2\)O\(_3\)** surface, which in turn controls **where** **WSe\(_2\)** nucleates along **steps** and whether domains adopt a **0°** or **60°** orientation relative to the substrate lattice. **Adri C. T. van Duin** appears among the co-authors alongside experimental and theory groups at Penn State and partner institutions, reflecting joint **growth**, **characterization**, and **computational** interpretation.

## Methods

### MOCVD experiments (epitaxy)

**c-plane α-Al\(_2\)O\(_3\)** with **~0.2°** miscut producing **terrace–step** structure; tune **T**, **precursor** delivery, and **surface prep** to vary **sapphire** **termination**/adsorbates and **step-edge** reactivity.

### Characterization mapping

**Wafer-scale** **orientation** maps + **microscopy** tie **domain** orientations to **step** distributions (**SI** for details).

### Electronic-structure support (C)

**DFT**-class calculations (inputs in **VOR/SI**) link **step-edge nucleation** to **0° vs 60°** **registry** selection.

**Growth-parameter space (summary level).** The experimental program varies **MOCVD** **temperature**, **precursor** **partial pressures**, and **substrate** **preparation** to change **sapphire** **surface** **termination** and **step** **morphology** on **c-plane** **Al\(_2\)O\(_3\)** with ~**0.2°** miscut. **Wafer-scale** **orientation** mapping then connects **domain** statistics to these **growth** knobs, supporting the claim that **surface chemistry** and **steps** must be engineered together—not **miscut** alone—to select **0°** versus **60°** **WSe\(_2\)** alignment.

**Static QM / DFT (supporting calculations).** The article uses **density-functional theory** to connect **DFT**-level models of **step-edge nucleation** to **0°** versus **60° in-plane** registry; **functional**, **dispersion** correction (e.g. **DFT-D**), **plane-wave**/**PAW** or **localized basis**, and **k-point** sampling are given in the **version-of-record** and **SI**—**N/A** to duplicate those tables on this page. **Structures** treat **WSe\(_2\)** on **c-plane** **sapphire** step motifs; **properties** compared include relative **stabilities** and **nucleation** preferences as in the **figures** (**N/A**—full **barrier** tables not transcribed here).

**MD application.** This work is **not** a production **molecular-dynamics** study: **N/A** — no **MD** **engine**, **timestep**, or **NVT**/**NPT** trajectories.

## Findings

### Orientation control mechanism

**Unidirectional WSe\(_2\)** alignment follows **growth-condition-dependent** **sapphire surface chemistry**, not **steps alone**—setting **0°** vs **60°** registry via **step-edge** nucleation.

### Defect reduction narrative

Intended to suppress **mirror twins**/**IDBs** from coalescing **60°**-rotated islands.

### Materials context

**Monolayer WSe\(_2\)** cited ~**1.65 eV** gap (intro) for **opto/spin** device framing; **wafer-scale** orientation tied to uniform **transport/optics**.

**Comparisons and parameters.** The authors connect **MOCVD** knobs, **imaging**/**mapping**, and **DFT**-guided **registry** arguments to one another; **sensitivity** of **0°/60°** selection to **temperature** and **chemistry** is in the full **version-of-record** and **SI**. **Corpus honesty:** the repo **galley** may differ in **pagination** and figure placement from the **DOI** **version-of-record**; cite **10.1038/s41565-023-01456-6** for final locators.

## Limitations

The repository **`pdf_path`** points at a **galley** PDF (`Zhu_Nayir_step_engineer_Nature_Nanotech_2023_galley.pdf`); **pagination**, **final figure quality**, and **copy edits** may differ from the **Nature Nanotechnology** version-of-record at DOI **10.1038/s41565-023-01456-6**. Detailed **reactor** recipes, **precursor** partial pressures, and full **characterization** parameters should be taken from the **published article** and **SI**, not inferred here.

## Relevance to group

Positions **van Duin-group** theory alongside **experimental epitaxy** of **2D semiconductors**, linking **surface chemistry** to **nucleation control**.

## Citations and evidence anchors

- DOI: `10.1038/s41565-023-01456-6`

## Related topics

- [[reaxff-family]]
