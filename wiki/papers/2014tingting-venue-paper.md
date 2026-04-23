---
id: paper:2014tingting-venue-paper
type: paper
title: "A reactive molecular dynamics study on the anisotropic sensitivity in single crystal α-HMX"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:shock-compression
  - keyword:energetic-materials
  - keyword:reaxff-application
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1039/C4RA09943E"
year: 2014
authors:
  - "Ting-Ting Zhou"
  - "Yan-Geng Zhang"
  - "Jian-Feng Lou"
  - "Hua-Jie Song"
  - "Feng-Lei Huang"
venue: "RSC Adv."
pdf_sha256: "a6d57257cfa0bafb8d98913f4094891ce32d2bf11fd5b778bf024feb365a136b"
pdf_path: "papers/ReaxFF_others/Tingting_Zhou_RSC_Advances_HMX_2015.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014tingting-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Compress–shear reactive dynamics (CS–RD)** with **ReaxFF** probes **anisotropic shock sensitivity** of **α-HMX** by varying the **shock normal** among several **low-index** planes. Simulations report **orientation-dependent** **shear stress**, **temperature**, and **chemical** onset during the **dynamical** loading. The authors propose **energy accumulation** while overcoming **shear** barriers as a practical **discriminator** of relative sensitivity, predicting **highest** sensitivity for shock along **(010)**, **intermediate** for **(001)**, and **lower** sensitivity for several other orientations—linking **anisotropy** to **steric** packing and **free volume** for **shear**-accommodating motion around **slip**-related **contacts**.

## Methods

**Local sources:** `papers/ReaxFF_others/Tingting_Zhou_RSC_Advances_HMX_2015.pdf` is present; `normalized/extracts/2014tingting-venue-paper_p1-2.txt` is the **accepted-manuscript** first page only.

**MD application (CS–RD on α-HMX).** The authors use **compress–shear reactive dynamics (CS–RD)**—their **nonequilibrium shock/reactive MD** protocol—with **ReaxFF** on **α-HMX** **single crystals**, varying the **shock normal** among directions associated with **(010), (001), (100), (110), (011), (111),** and **(101)** (abstract). Trajectories monitor **orientation-dependent** **shear stress**, **temperature**, **energy**, and chemical onset during loading (abstract). **Engine** (e.g. **LAMMPS** build), supercell size, **periodic** (**PBC**) boundaries, timestep, **equilibration**/**production** **durations** (**ps**/**ns**), **NVT**/**NPT**/**NVE** staging, thermostat/**barostat**/**pressure** control, and loading-rate details are **N/A** on the indexed first page and must be read from the full **RSC Adv.** article and any **SI**.

**Force-field training.** **N/A**: an existing **ReaxFF** parametrization for nitramine chemistry is applied as cited, not newly fitted in the excerpt used here.

**Static QM.** **N/A** as headline method: the work is **nonequilibrium reactive MD** under **CS–RD**.

## Findings

The authors report **anisotropy** in **thermomechanical** and **chemical** responses during CS–RD loading. They propose that **internal energy accumulated while surmounting shear stress barriers** provides a practical **criterion** to rank **anisotropic sensitivity** across shock orientations. Using that criterion, **α-HMX** is predicted **most sensitive** for shocks normal to **(010)**, **intermediate** for **(001)**, and **relatively insensitive** for shocks normal to **(100), (110), (011), (111),** and **(101)**. They attribute the anisotropy to **steric packing** and **intermolecular free volume** around **slip-plane**-related contacts: sensitive directions encounter **stronger intermolecular contacts** and **less room** for relaxation during shear-driven collisions, increasing **stress buildup** and **heating** that promotes **initial bond scission** and subsequent reactions.

Comparisons to experiment and quantitative stress/temperature thresholds are in **papers/ReaxFF_others/Tingting_Zhou_RSC_Advances_HMX_2015.pdf** and any **SI**.

## Limitations

- **Accepted manuscript** PDF in corpus—prefer **final** **pagination**/**figures** from the **published** **RSC Adv.** article for citations.
- **ReaxFF** uncertainty for **detonation** physics requires comparison to **continuum** **experiments** and **higher-fidelity** **kinetics** when available.

## Relevance to group

**Energetic materials** **ReaxFF** application in the **shock**/**shear** **sensitivity** literature adjacent to other **HMX** studies in the wiki.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1039/C4RA09943E

## Related topics

- [[reaxff-family]]
