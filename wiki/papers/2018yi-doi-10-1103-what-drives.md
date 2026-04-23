---
id: paper:2018yi-doi-10-1103-what-drives
type: paper
title: What Drives Metal-Surface Step Bunching in Graphene Chemical Vapor Deposition?
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:carbon-hydrocarbon
- domain:catalysis-surfaces
- material:graphene-carbon-nano
- method:dft-static
- scale:atomistic
- task:experiment-integrated
paper_keywords:
- keyword:graphene-carbon
- keyword:validation-experiment
- keyword:dft-static
candidate_tags: []
source_refs: []
doi: 10.1103/PhysRevLett.120.246101
year: 2018
authors:
- Ding Yi
- Da Luo
- Zhu-Jun Wang
- Jichen Dong
- Xu Zhang
- Marc-Georg Willinger
- Rodney S. Ruoff
- Feng Ding
venue: Phys. Rev. Lett.
pdf_sha256: 2fd79f7b7be965d1581491773064d5918635e1678ab06a8fea87893cd0c0e19f
pdf_path: papers/Others/Cu_Graphene_Ding_PhysRevLett.120.246101.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018yi-doi-10-1103-what-drives -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *Physical Review Letters* article identified by `doi`, `title`, and `pdf_path`.

## Summary

During graphene chemical vapor deposition on copper, metal surfaces often develop **step bunching (SB)**—periodic collections of atomic steps that alter local reactivity and film uniformity. A common explanation ties SB to **compressive strain** in graphene after cooling from growth temperature. Yi *et al.* combine theory and experiment to argue that **compressive strain is not the sole driver**: **fast diffusion of metal adatoms** beneath graphene and **release of graphene bending energy** near surface steps can drive SB even when large compressive strain is absent. Their model aims to rationalize temperature-dependent SB, dependence on graphene thickness, and related CVD observations summarized in the letter.

The paper explicitly contrasts **macroscopic** **step** heights observed after CVD (often **multi-nanometer** **bunches**) with the **sub-nanometer** height of a single **Cu** **atomic** step, motivating a mechanism that couples **graphene** **coverage** to **mass** transport and **elastic** energy rather than thermal contraction alone.

## Methods

**Theory.** The authors develop continuum-elastic or hybrid atomistic models (details and equations in the letter and Supporting Information) for graphene spanning metal steps, including bending contributions, and couple these to kinetics of metal adatoms under the graphene sheet.

**Experiment.** Microscopy and spectroscopy protocols document step heights, thermal history, and film thickness effects on SB under CVD-relevant conditions; see the article for sample preparation on copper foils and in situ or ex situ characterization pipelines.

**Analysis.** Comparisons contrast strain-only scenarios with scenarios that include subsurface adatom transport and step-associated bending relaxation.

**DFT / electronic-structure support.** The letter routes many **first-principles** settings to the **Supporting Information**; this wiki does **not** restate **functional**, **dispersion**, **basis set**, **k-mesh**, or **property** tables here. Readers should pull those details from **`papers/Others/Cu_Graphene_Ding_PhysRevLett.120.246101.pdf`** (and **SI**) when reproducing **DFT** benchmarks referenced alongside the continuum model—specific **exchange–correlation** choices, **vdW** handling, **basis set** / **plane-wave** settings, **Brillouin-zone** sampling, and tabulated **energies**/**barriers** must be read from the **SI** rather than inferred on this page.

**Reproducibility detail.** The letter discusses **cooling** from **~1000 °C** and the **thermal** **expansion** mismatch between **Cu** and **graphene** that can impose **~2%** **compressive** strain in the overlayer under simplified estimates; the new mechanism is demonstrated in part by **in situ** observations during **cooling** where **graphene-covered** regions develop **macrosteps** while adjacent **bare** **Cu** can remain comparatively flat—readers should use the published **Supplemental Material** for **step-height** summaries tied to specific **facets** and **conditions**.
## Findings

Step bunching can occur **without** requiring large compressive strain in the graphene overlayer. **Sub-surface metal transport** and **bending-energy relaxation** of graphene crossing steps play central roles in the proposed mechanism. The framework is argued to match trends of SB with temperature, graphene layer count, and other CVD observables itemized in the abstract.

**Empirical anchors.** The authors connect their model to observations that **SB** tracks **graphene** **coverage** and **pre-existing** **steps**, and they discuss how **film** **thickness** modulates the phenomenon—details appear in the letter’s figure set and supplemental tables.

**Reproducibility pointer.** Supplemental summaries tabulate **macrostep** heights versus **facet** and **processing** conditions; use those tables when comparing simulations to **SEM** images rather than relying on a single representative micrograph.

## Limitations

Quantitative predictions depend on elastic constants, step geometries, and kinetic prefactors for adatom diffusion; the study is **not** a ReaxFF reactive MD paper. Transfer to other metals requires revisiting the parameterization.

## Related topics

- [[graphene-nanocarbon]]
- [[theme-2d-epitaxy-growth]]
