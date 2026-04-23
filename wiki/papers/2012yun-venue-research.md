---
id: paper:2012yun-venue-research
type: paper
title: "Development and validation of a ReaxFF reactive force field for Fe/Al/Ni alloys: molecular dynamics study of elastic constants, diffusion, and segregation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reaxff-lineage
  - material:alloy-bulk
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:metallic-systems
  - keyword:validation-experiment
  - keyword:npt-simulation
  - keyword:berendsen-thermostat
source_refs: []
doi: "10.1021/jp308507x"
year: 2012
authors:
  - "Shin, Yun Kyung"
  - "Kwak, Hyunwook"
  - "Zou, Chenyu"
  - "Vasenkov, Alex V."
  - "van Duin, Adri C. T."
venue: "Journal of Physical Chemistry A"
pdf_sha256: "f88093d63a9ceec5595aabf408634831a1beec823a68a942dddb7e714601bf5e"
pdf_path: "papers/Yun_JPCA_2012_Alloys_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012yun-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and `pdf_path`. The PDF is a **galley**; verify **pagination** against the **version of record**.

## Summary

A **ReaxFF** parametrization for **Fe/Al/Ni** **binary** **alloys** uses **QM** **training** on **bulk** phases and **(100)/(110)/(111)** **surface** energies and **adatom** **binding**. **Validation** includes **elastic** **constants** (**300–1100 K**) for **FeAl**, **FeNi₃**, **Ni₃Al** (abstract: **trends** vs **experiment**), **Al**/**Ni** **diffusivity** in **composition-gradient** **layers** at **1000 K** (abstract contrasts **trace** vs **pure-metal** ends), and **surface** **segregation** in **L1₂** **clusters** at **2500 K** (**Al** strongest in **Fe₃Al**, weakest in **Ni₃Al**; **depletion** layers adjacent to **segregation**).

## Methods

### Force-field training

**Parent field / elements:** **ReaxFF** for **Fe/Al/Ni** binaries, extending prior **metallic alloy** parameterization practice described in the article.

**QM reference & training set:** **Fe–Al**, **Fe–Ni**, and **Ni–Al** **unlike-pair** terms are fit to **QM equation-of-state** curves for **B2**, **L1₂**, **DO₃**, and **L1₀** phases across **25–75 at.%** composition sweeps, augmented by **(100)/(110)/(111)** **surface energies** and **adatom binding** data (**Section III.A**; `papers/Yun_JPCA_2012_Alloys_galley.pdf` / extract).

**Optimization & validation split:** Parameters are optimized against that **QM** training set; **MD** simulations below are **validation** trajectories of the fitted field.

### MD application (atomistic dynamics)

**Engine / code:** **ADF/ReaxFF** for the reported workflows (Methods in **`pdf_path`**).

**Elastic constants (finite-T):** **NPT** molecular dynamics with **Δt = 0.25 fs**, **Berendsen** thermostat (**100 fs** coupling) and **barostat** (**500 fs** coupling). Supercells: **(5×5×5)** (**500 atoms**) and **45°-rotated** **512-atom** cells for **L1₂ Ni₃Al** and **FeNi₃**; **(6×6×6)** (**432 atoms**) plus a **rotated 500-atom** cell for **B2 FeAl**. **>1 ps** production averaging after **equilibration** (article Methods).

**Diffusion:** **fcc Ni** matrix in **(4×4×11)** unit cells with a **linear Al composition gradient** **(n−1)/10** per layer, **open x/z surfaces** with **~30 Å vacuum**, **1000 K**, **Berendsen** thermostat **100 fs**, **Δt = 0.25 fs**, **1 ns** trajectory with sampling **every 0.25 ps**.

**Surface segregation:** **(10×10×10)** **L1₂** supercells (**4000 atoms**) with **~11 nm vacuum** padding; **300 K** equilibration **5 ps**; **300 → 2500 K** ramp at **0.05 K/step**; **2500 K** hold **60 ps**; cool to **300 K** at **−0.0125 K/step**.

**Boundaries / periodicity:** **3D PBC** in **bulk** elastic runs; **slab-like** **open surfaces** normal to **z** in the diffusion geometry; **vacuum-padded** **clusters** for segregation (**Methods**).

**Ensemble:** **NPT** for elastic constants; diffusion and segregation blocks use **constant-temperature** MD as specified (**NPT** where stated for elastic block; verify labels for diffusion in **`pdf_path`**).

**Pressure:** **NPT** elastic runs imply **hydrostatic** coupling; **N/A —** target **pressure** value not transcribed here—confirm in PDF.

**Electric field / enhanced sampling:** **N/A —** not used.

## Findings

**Outcomes:** **Cᵢⱼ(T)** for **FeAl**, **FeNi₃**, and **Ni₃Al** **soften** with increasing **T** from **300 K** to **1100 K**, tracking **experimental** trends for **C₁₁**, **C₁₂**, and **C₄₄** (abstract). **Al diffusivity** at **1000 K** rises by roughly **two orders of magnitude** from **trace** layers to the **Al-rich** end of an **Al/Ni** gradient, whereas **Ni** diffusivity changes only modestly between trace and **pure-Ni**-like regions at **T** far below **Ni melting** (abstract). **L1₂** **Fe₃Al**, **Fe₃Ni**, and **Ni₃Al** clusters at **2500 K** show **Al** segregation strongest in **Fe₃Al** and weakest in **Ni₃Al**, with **depletion zones** adjacent to segregating species (**Al** in **Fe₃Al**/**Ni₃Al**, **Ni** in **Fe₃Ni**) as in the abstract’s summary.

**Comparisons:** Elastic and segregation patterns are compared to **experimental literature** cited in the article.

**Sensitivity:** Results depend on **temperature**, **stoichiometry**, and **composition-gradient** endpoint vs trace placement.

**Limitations / outlook:** **Galley** PDF (`papers/Yun_JPCA_2012_Alloys_galley.pdf`); confirm pagination against the **version of record** **`[[2012yun-venue-jp-2012-08507x]]`**. **2500 K** segregation is an aggressive thermal stress test—interpret alongside experimental windows cited in the paper.

**Corpus honesty:** Numerics above are taken from the **galley Methods** text in-repo; if **`pdf_path`** is updated to the **ASAP** PDF only, re-verify identical protocol wording.

## Limitations

**Galley** PDF; **high-T segregation** simulations are extreme compared to many laboratory conditions; **ReaxFF** alloy accuracy is limited by the **QM** training scope. For pagination and any publisher updates, compare with **`[[2012yun-venue-jp-2012-08507x]]`** (same DOI).

## Relevance to group

**Adri C. T. van Duin** senior author line on **metallic** **ReaxFF** **validation** (**NETL**-**PSU** collaboration).

## Citations and evidence anchors

- DOI **10.1021/jp308507x** — *J. Phys. Chem. A* (volume/pages per final issue).
- PDF: `papers/Yun_JPCA_2012_Alloys_galley.pdf`; extract: `normalized/extracts/2012yun-venue-research_p1-2.txt`.

## Related topics

- [[reaxff-family]]
