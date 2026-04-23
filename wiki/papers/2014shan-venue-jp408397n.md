---
id: paper:2014shan-venue-jp408397n
type: paper
title: "Development of a ReaxFF reactive force field for ammonium nitrate and application to shock compression and thermal decomposition"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
source_refs: []
doi: "10.1021/jp408397n"
year: 2014
authors:
  - "Tzu-Ray Shan"
  - "Adri C. T. van Duin"
  - "Aidan P. Thompson"
venue: "Journal of Physical Chemistry A 2014, 118, 1469–1478"
pdf_sha256: "9b9c494a43d290eff4af24e4ce0d3e41b1ca2ecf67350d9bff8982c2b32eb5cd"
pdf_path: "papers/Shan_Thompson_AN_JPCA_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014shan-venue-jp408397n -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Shan, van Duin, and Thompson report a **ReaxFF** reparameterization for **ammonium nitrate (AN)** starting from an existing **nitramine/TATB** description, training against **electronic-structure** data for **barriers**, **heats of formation**, and **crystal** properties of AN phases. Applications shown in the abstract include **isothermal compression** of phase-IV AN (claimed agreement with DFT/experiment within about **10%** over the studied compression range), **unreacted principal Hugoniot** states (noted as stiffer than experiment by about **17%** in the abstract statement), and **thermal decomposition** simulations up to **2500 K** with pathways said to align with experimental findings. Simulations are executed in **LAMMPS** using the group's ReaxFF workflow.

AN is a foundational energetic oxidizer whose phases and shock response are sensitive to hydrogen bonding and ion ordering; the parameterization aims to unify solid-state mechanics with reactive chemistry.

## Methods

**Force-field training (ReaxFF for ammonium nitrate).** The authors extend an existing **nitramine/TATB** **ReaxFF** description and **reoptimize** bonded and nonbonded terms so **NH\(_4\)NO\(_3\)** matches **electronic-structure** targets for **dissociation barriers**, **heats of formation**, and **crystal** properties of **AN** phases (abstract). Optimization is carried out with the **standalone ReaxFF code**; **production MD** uses **LAMMPS** (Introduction). Program choices for QM reference data, basis/cutoff conventions, and the full training-set listing are in **Section 2** of `papers/Shan_Thompson_AN_JPCA_2014.pdf` and the **Supporting Information**—not transcribed here. For a sibling reading copy with overlapping DOI text and more protocol detail extracted in-repo, see **`[[2014shan-venue-research]]`**.

**MD application (EOS, Hugoniot, thermal decomposition).** The fitted field is applied to **phase-IV** solid **AN** for **isothermal P–V** curves, **unreacted principal Hugoniot** states, and **thermal decomposition** heated to **2500 K** (abstract), using **LAMMPS** with **ReaxFF** as stated in the article. Supercell sizes, **PBC** vectors, ensemble staging (**NVT**/**NPT** as appropriate), timestep, **equilibration**/**production** segment **durations** (**ps**/**ns** in the article), and thermostat/**barostat** parameters are given in **Section 2** and the **SI** rather than in the short in-repo extract used here—**N/A** to transcribe numerically on this page. **Electric fields**, **shock pistons**, and **enhanced sampling** are **N/A** for the validation cases summarized from the abstract.

**Static QM.** **DFT** supplies reference energies and equations of state for parametrization and static benchmarks; the headline applications in the abstract are **ReaxFF MD**, not production **AIMD** trajectories (**N/A** for standalone AIMD application block).

## Findings

For **phase IV**, the **isothermal P–V** curve from the model agrees with **DFT** and **experiment** within about **10%** over the compression range quoted in the abstract. The **unreacted principal Hugoniot** is nevertheless roughly **17% stiffer** than experiment in the abstract’s summary—consistent with the introduction’s discussion of scatter across literature **US–uP** parametrizations for AN. **Thermal decomposition** trajectories to **2500 K** are described as agreeing with **experimental** pathways at a qualitative level (article body for species-resolved detail). The abstract’s message is explicitly **validation-sensitive**: good **isothermal** agreement does not guarantee satisfactory **Hugoniot** response for this parameterization.

## Limitations

- Hugoniot-level agreement is explicitly imperfect in the abstract; users should treat **shock** observables as **validation-sensitive** outputs.
- Full **training-set** tables, additional **phases**, and **species-resolved** timelines are in the **J. Phys. Chem. A** article + **SI** rather than a short extract-backed note.
- Extract is early pages only; quantitative plots and full barrier sets require the PDF body.

## Relevance to group

**Adri C. T. van Duin** co-authorship ties this to **ReaxFF** development for **energetic nitrogen/oxygen** chemistry used across combustion and initiation modeling threads.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/jp408397n](https://doi.org/10.1021/jp408397n)

## Related topics

- [[reaxff-family]]
