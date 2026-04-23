---
id: paper:2015psofogiannakis-venue-jp5b00699
type: paper
title: "ReaxFF reactive molecular dynamics simulation of the hydration of Cu-SSZ-13 zeolite and the formation of Cu dimers"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - method:reaxff
  - material:zeolite-porous
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b00699"
year: 2015
authors:
  - "George M. Psofogiannakis"
  - "John F. McCleerey"
  - "Eugenio Jaramillo"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "18feeef1f056fe0036c3209080ba474780c732df7289a731b4575f231b600d2c"
pdf_path: "papers/Psofogiannakis_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015psofogiannakis-venue-jp5b00699 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This study develops a **Cu/Si/Al/O/H ReaxFF** parameterization and applies it in reactive MD to follow **hydration and speciation of Cu in Cu-SSZ-13**, a zeolite central to selective catalytic reduction (SCR) of NOx. Simulations report that near-room-temperature water drives **framework-detached, fully hydrated Cu** that can migrate through pore windows, while at higher temperature the work highlights **OH-bridged Cu dimers** (for example Cu2OH and Cu2(OH)2) whose stability and pore-blocking placement are tied to framework composition (Cu/Al loading and stabilization of [CuOH]+). The discussion connects these atomistic pathways to **SCR and NO oxidation** phenomenology where extra-framework Cu speciation and transport matter.

## Methods

### Force-field training

A **Cu/Si/Al/O/H ReaxFF** parameter set is **developed** for **Cu-exchanged SSZ-13** chemistry (abstract), with **DFT** reference data on **Cu–O**, **Cu–OH**, and **framework** motifs and an optimization workflow documented in **J. Phys. Chem. C** and **SI** (not on the short local `p1–2` extract).

### MD application (atomistic dynamics)

**Reactive molecular dynamics** in **LAMMPS** follows **hydration** of **Cu-SSZ-13** zeolite **supercells** containing **extra-framework Cu**, **framework Si/Al/O**, and **explicit water** under **three-dimensional periodic boundary conditions** in the **orthorhombic** (or closely related) **unit cell** defined in **Computational Methods** (*J. Phys. Chem. C*). Simulations use **NVT**-style **canonical** control for the reported hydration trajectories, with **timestep**, **thermostat** coupling, **temperature (K)** ramps, and **equilibration** plus **production** segments whose lengths are quoted in **ns** in the article (not on the short local extract). **Barostat / NPT:** **N/A —** the abstract-framed study is **constant-volume** zeolite **hydration** rather than a **pressure**-scanning campaign. **Hydrostatic pressure / stress tensor:** **N/A —** not reported as an independent control variable in the abstract summary.

**Electric field / umbrella or metadynamics:** **N/A** in the protocol summarized from the abstract.

## Findings

The new field supports **MD** trajectories in which **near-room-temperature water** fully **hydrates** **Cu** species—including those initially at **d6r** faces—leading to **framework detachment** and **diffusion** of hydrated cations through **pore windows**. **Higher temperatures** favor **OH-bridged Cu dimers** (**Cu\(_2\)OH**, **Cu\(_2\)(OH)\(_2\)**); the **dimerization temperature** shifts with composition in the direction expected when **[CuOH]\(^+\)** is stabilized (**higher Cu**, **lower Al** in the abstract’s framing). **Stable dimers** preferentially sit near **8-member rings** beside **large cages** in geometries that **block pore openings**, with discussion links to **SCR** and **NO oxidation** phenomenology where the paper cites prior work.

## Limitations

**ReaxFF** fidelity is limited by the **QM training manifold** and bond-order approximations; **finite cells** and **nanosecond** horizons may miss rare **clustering** events in real zeolite crystallites.

## Relevance to group

Direct **ReaxFF parameterization for microporous Cu zeolites** with Penn State authorship; connects reactive FF development to **environmental catalysis** problems (NOx abatement) that motivate much of the group’s heterogeneous catalysis portfolio.

## Citations and evidence anchors

- Abstract and introduction in the PDF (`papers/Psofogiannakis_JPCC_2015.pdf`) state the force-field scope, hydration/detachment behavior, dimer chemistry, and SCR framing; **DOI:** `10.1021/acs.jpcc.5b00699`.

## Related topics

- [[reaxff-family]]
- Zeolite / Cu-zeolite themes: no dedicated `materials/zeolite-porous.md` page yet; search paper notes for *zeolite*.
