---
id: paper:2019aniruddh-vashisth-nanoscale-20-mechanical-size
type: paper
title: 'Mechanical size effects of amorphous polymer-derived ceramics at the nanoscale:
  experiments and ReaxFF simulations'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:oxides-ceramics
- domain:mechanics-tribology
- material:silicate-glass
- method:reaxff
- task:parameterization
- task:experiment-integrated
- scale:atomistic
candidate_tags: []
paper_keywords:
- keyword:reaxff-parameterization
- keyword:qm-training-data
- keyword:polymer
- keyword:oxide-surface
- keyword:validation-experiment
source_refs: []
doi: 10.1039/c9nr00958b
year: 2019
authors:
- Aniruddh Vashisth, Sumit Khatri, Seung Ho Hahn, Weiwei Zhang, Adri C. T. van Duin,
  Mohammad Naraghi
venue: Nanoscale (2019), 11, 7447-7456, doi:10.1039/c9nr00958b
pdf_sha256: 2ac524a5522eec1b9ddb15034220fd3fa59b6d701c85b417051ca32e4bed8836
pdf_path: papers/Vashisth_Nanoscale_2019_SiOC.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2019aniruddh-vashisth-nanoscale-20-mechanical-size -->

## Summary

Silicon oxycarbide (SiOC) polymer-derived ceramic (PDC) micro- and nanofibers are fabricated without fillers; reducing fiber diameter from about 1.1 um to about 630 nm is reported to increase tensile strength from about 1 GPa to about 3.3 GPa, beyond what the Griffith scaling picture alone would suggest, motivating a defect-size picture tied to pyrolysis degassing. A Si/O/C/H/N ReaxFF parameterization is developed and used to model "flawless" PDC structures so that simulated elastic response can be compared with experiment and failure can be tied to bond-breaking chemistry (C-C failure as a limiting mechanism in the simulations).

## Methods

**Experiments (SiOC PDC fibers).** **Polymer-derived ceramic (PDC)** **SiOC** **micro- and nanofibers** are fabricated **without fillers** and tensile-tested on **MEMS** fixtures. The manuscript reports a strong **diameter dependence** of **strength** in the examined window (abstract/introduction cites testing down to about **610 nm** diameter and compares against **Griffith-type** scaling expectations). **Nominal strain rate** in fiber tests is on the order of **~60 με s⁻¹** as stated in the article.

**Reactive force-field development (Si/O/C/H/N).** The authors develop a **new ReaxFF** parameter set for **Si/O/C/H/N** by **combining and re-optimizing** the **CHON-2017_weak** parameterization with training sets for **Si/O/H** (**Pitman et al.**) and **C/O/Si** (**Newsome et al.**), targeting both **polymer** densities/morphology and **ceramic** stress response (see **Table S1**/**ESI** discussion in the paper). **QM reference data** used in the fit are summarized via **energy-profile comparisons** in the **ESI** (e.g., **Fig. S1** referenced in the main text).

**MD application (virtual mechanical testing, LAMMPS + ReaxFF).** **Engine / code:** **LAMMPS** is used for **virtual mechanical testing** with the developed **ReaxFF** potential (**Nanoscale** computational details). **System size & composition:** simulations start from a **cross-linked SiOC** geometry adapted from prior work (**Gao et al.**), energy-minimized with the new field to yield a **cubic** cell about **~2 nm** per side. **Boundaries / periodicity:** **three-dimensional periodic** boundaries are used in the MD workflow described in the article. **Ensemble / pressure:** **tensile modulus** runs use an **NPT** ensemble with a **cuboidal** constraint so **Poisson contraction** is represented (four faces parallel to the loading axis are free to move accordingly). **Timestep:** **0.1 fs** for the reported **modulus / Poisson ratio** virtual tests. **Thermostat:** thermostat **damping parameter** reported as **10 fs** alongside the **NPT** modulus protocol. **Strain rate / loading:** **tensile modulus** is evaluated across **strain rates** from about **10¹⁰ to 10¹² s⁻¹**; **modulus and Poisson ratio** fits use the **linear** regime up to about **~2% strain** at **300 K**, with additional **temperature-dependent** tests reported at **500 K**, **800 K**, and **1000 K** at **10¹² s⁻¹**. **Electric fields / enhanced sampling:** **N/A — not part** of the mechanical testing narrative summarized above. **Duration / stages:** the workflow includes energy minimization, **NPT equilibration**, and strain-controlled **production** segments for modulus and temperature sweeps; cumulative trajectory lengths in **ps**/**ns** are tabulated in the **Nanoscale** **Methods**/**SI** rather than duplicated line-by-line here.
## Findings

**Outcomes / mechanisms (experiments).** Decreasing **fiber diameter** from about **1.1 µm** to about **630 nm** is reported to **nearly triple** **tensile strength** (from about **~1 GPa** to about **~3.3 GPa** in the abstract framing), with a **stronger-than-Griffith** diameter scaling (the article discusses a scaling closer to **σ_f ∝ d^−1.68** vs a **d^−0.5** Griffith expectation when flaws are capped by diameter). The interpretation emphasized in the paper is **size-dependent flaw populations** during **pyrolysis/degassing** (voids/microcracks), where thinner fibers provide shorter diffusion paths for volatile escape.

**Outcomes / mechanisms (ReaxFF “flawless” models).** **MD** reproduces an **experimental elastic modulus** near **107 ± 16 GPa** with simulation averages near **102 ± 16 GPa** (with per-realization spreads quoted in the article) and reports **Poisson’s ratio** near **0.338 ± 0.039** and **shear modulus** near **38 ± 8 GPa** from the **dense** models. The simulations quote an **upper-bound strength** near **~8.5 GPa** for an idealized **void-free** structure, with **C–C** bond failure highlighted as the **limiting rupture channel** in the **RDF/bond-break** analysis.

**Comparisons.** **Simulated moduli** are described as **insignificantly dependent** on the **ultrahigh strain rates** used (**10¹¹–10¹³ s⁻¹** window in the modulus discussion), while still matching the **experimental modulus** within quoted uncertainty.

**Sensitivity / design levers.** **Temperature** is explored in MD for mechanical softening: a **modest** modulus drop when heating from **300 K** toward **500 K**, but a **large** drop by **800 K** (article quotes about **45%** reduction by **800 K**), with **yield strain** also shifting with temperature.

**Limitations / corpus honesty.** Real fibers contain **disorder** and **voids** that are deliberately removed in the “flawless” limit; **ReaxFF** accuracy is bounded by training scope. Ultra-high **strain rates** in MD are not equivalent to MEMS **fiber** strain rates, so strength numbers are **model-relative** upper bounds unless mapped via the authors’ extrapolation discussion.
## Limitations

Real PDCs contain **disorder**, **voids**, and processing variability not captured by idealized cells; **ReaxFF** remains a **classical reactive** approximation with accuracy bounded by its **training scope** and by the **ultrahigh strain-rate** MD protocol used for modulus/strength probing.

## Relevance to group

Co-authored by Adri C. T. van Duin; couples experimental PDC processing and mechanics with ReaxFF development for Si-O-C-H-N ceramics.

## Citations and evidence anchors

https://doi.org/10.1039/c9nr00958b

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
