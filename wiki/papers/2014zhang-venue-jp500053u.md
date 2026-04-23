---
id: paper:2014zhang-venue-jp500053u
type: paper
title: "Site Stability on Cobalt Nanoparticles: A Molecular Dynamics ReaxFF Reactive Force Field Study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
  - keyword:catalysis-surface
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1021/jp500053u"
year: 2014
authors:
  - "Xue-Qing Zhang"
  - "Eldhose Iype"
  - "Silvia V. Nedea"
  - "Antonius P. J. Jansen"
  - "Bartlomiej M. Szyja"
  - "Emiel J. M. Hensen"
  - "Rutger A. van Santen"
venue: "J. Phys. Chem. C 2014, 118, 6882–6886"
pdf_sha256: "1ca7a254cc3c7a6791bfb3c7f8abea6635ffe0d527991c385e1c03160b13462a"
pdf_path: "papers/ReaxFF_others/Zhang_Lype_vanSanten_JPCC_2014_Cobalt.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014zhang-venue-jp500053u -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

## Summary

This Journal of Physical Chemistry C letter investigates the stability of step-edge-type sites on free cobalt nanoparticles as a function of particle size, using newly developed ReaxFF parameters for cobalt in combination with reactive molecular dynamics. The study is motivated by structure sensitivity in catalytic reactions such as ammonia synthesis and Fischer–Tropsch chemistry, where step-edge and B5-type sites are often invoked as especially active motifs. Rather than adsorbate chemistry, the authors isolate intrinsic nanoparticle rearrangements by monitoring how step-edge sites disappear with temperature for three compact Co clusters containing 321, 603, and 1157 atoms, corresponding to sizes of roughly 1.8 nm, 2.2 nm, and 2.9 nm in the figure caption.

## Methods

**MD application (Co nanoparticle step-edge kinetics).** **ReaxFF** **reactive MD** with **velocity-Verlet** **NVT** integration tracks **step-edge disappearance** kinetics versus **temperature**, with **Arrhenius**-style analysis of lifetimes or disappearance rates as defined in the paper. Reported settings include **0.5 fs** timestep, **Berendsen** thermostat (**200 fs** damping), and **1.0 million** force evaluations per production segment (**0.5 ns** simulated time per quoted run). Initial **fcc**-derived clusters contain **321**, **603**, and **1157** **Co** atoms with labeled **step-edge** motifs, including **fcc(311)**-like **B5** sites and **fcc(110)**-like **B5** sites on the largest cluster. **Boundary** treatment for the finite **Co** clusters (**PBC** padding, fixed regions, or vacuum extent) is specified in the letter (**N/A** to transcribe on this page). **Engine** name/version and full construction workflow are **N/A** on this page’s excerpt—see **`papers/ReaxFF_others/Zhang_Lype_vanSanten_JPCC_2014_Cobalt.pdf`**. **Pressure** (**NPT**) control is **N/A** for the summarized cluster protocol. **Electric fields** and **replica** enhanced sampling are **N/A** here.

**Force-field training (new Co ReaxFF).** The letter reports a **newly designed** **ReaxFF** for **Co** nanoparticle rearrangements, with fitting details in **Supporting Information** (**N/A** on this page for QM reference tables, optimization software, and weights).

**Static QM.** **N/A** as headline results: **ReaxFF MD** kinetics dominate; **DFT** may appear as training/validation references in **SI**.

## Findings

**ReaxFF** trajectories resolve two **activation-energy** regimes for losing **step-edge** character. A low barrier near **7 kJ/mol** is tied to **single-atom hop** processes and is reported **insensitive** to particle size within the fitted model. Larger barriers (**28**, **37**, and **22 kJ/mol** for the **321-**, **603-**, and **1157-atom** clusters) correspond to **concerted terrace shifts** whose barriers depend on **particle size**, **terrace** extent, and **facet** structure; **step edges** persist longer on **larger** particles under the sampled conditions. **(111)** **terrace** layer shifts can convert a thin surface region from **fcc**-like stacking toward **hcp**-like character in the model, linking mechanical **terrace** rearrangement to local **stacking** motifs.

**Context (introduction, not new simulation results):** the letter frames **Co** **nanoparticle** topology changes within **structure sensitivity** debates for **ammonia synthesis** and **Fischer–Tropsch** chemistry, noting that beyond **~1.5 nm**, **surface** topology changes—not only **electronic** finite-size effects—often dominate trends, and that **area-normalized** rates can drop steeply below a threshold size with **step-edge** abundance invoked among competing explanations.

## Limitations

**Nanoparticle** models omit **electronic** structure explicitly; **ReaxFF** barriers for **Co** rearrangements should be cross-checked when extrapolating to **catalytic** reaction conditions beyond the **structural** kinetics probed here.

## Relevance to group

**ReaxFF** benchmark for **size-dependent** **Co** **terrace/step** kinetics—useful alongside other **metal-surface** **parameterization** notes in the knowledge base.

## Citations and evidence anchors

- DOI: [10.1021/jp500053u](https://doi.org/10.1021/jp500053u)
- `normalized/extracts/2014zhang-venue-jp500053u_p1-2.txt`

## Reader notes (navigation)

- Co nanoparticle kinetics: [[reaxff-family]]; related validation: [[2015kroes-venue-ct5b00292]] (CNT vacancies).

## Related topics

- [[reaxff-family]]
