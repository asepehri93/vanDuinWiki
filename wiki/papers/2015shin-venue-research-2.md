---
id: paper:2015shin-venue-research-2
type: paper
title: "Development of a ReaxFF Reactive Force Field for Fe/Cr/O/S and Application to Oxidation of Butane over a Pyrite-Covered Cr₂O₃ Catalyst"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - domain:fuel-combustion
  - method:reaxff
  - material:oxide
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:lammps
  - keyword:reactive-md
  - keyword:combustion
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1021/acscatal.5b01766"
year: 2015
authors:
  - "Yun Kyung Shin"
  - "Hyunwook Kwak"
  - "Alex V. Vasenkov"
  - "Debasis Sengupta"
  - "Adri C. T. van Duin"
venue: "ACS Catalysis"
pdf_sha256: "4069241a22eb7e650a5b19b826941e8380342b1efb22f5300102bb6a9235b811"
pdf_path: "papers/Shin_ACS_Catalysis_2015_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015shin-venue-research-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi` and `pdf_path`. This ingest is an ACS **proof** PDF; prefer **`[[2015shin-venue-research]]`** for the non-proof layout when hashes must match a specific ingest policy.

## Summary

This file is a **proof PDF** for the **ACS Catalysis** article **DOI `10.1021/acscatal.5b01766`**: development of a **Fe/Cr/O/S ReaxFF** parametrization from **QM** data and **reactive MD** application to **butane** oxidation on **Cr₂O₃**, contrasting **clean** chromia with **pyrite-covered** surfaces. The abstract reports **1600 K** simulations in which **surface oxygen** drives **dehydrogenation** and **C–O** coupling, yielding **CH₂O** as a major product on **clean** oxide while **FeS₂** accelerates **CO/CO₂** formation with **SOH** release and proposed **surface reconstruction**.

## Methods

**Force-field training.** **Fe/Cr/O/S ReaxFF** extension with **QM-derived** training sets for **oxide / sulfide / hydrocarbon** interactions (Computational Methods + SI). **Optimization details:** `pdf_path` + [[2015shin-venue-microsoft-word]] tables.

**MD application.** **Engine:** **molecular dynamics** with **ReaxFF** as named in the article’s **Computational Methods**. **System:** **atomistic** **Cr₂O₃** **slab** supercells exposed to **C₄H₁₀** and **O₂**, with parallel **FeS₂**/oxide models (stoichiometries and **atom** counts in **`pdf_path`**). **Boundaries:** **3D PBC** in the surface plane with vacuum or slab padding as defined there. **Ensemble:** **NVT** at the **1600 K** headline oxidation temperature (abstract) unless additional stages are listed in Methods. **Timestep / thermostat / duration:** tabulated in **`pdf_path`** (fs timestep, **production** segment lengths in **ps**/**ns**). **Barostat:** **N/A** for the **NVT** headline trajectories unless Methods add **NPT** segments. **Pressure:** **N/A** — not a hydrostatic **NPT** study in the abstract framing. **Electric field / enhanced sampling:** **N/A**.

**Static QM / DFT production:** **N/A** beyond QM used for parametrization.

## Findings

**Clean Cr oxide:** **Surface oxygen** mediates **dehydrogenation** to **radicals** and **OH**; **CH₂O** is highlighted as a major **partial oxidation** product at **1600 K** in the abstract.

**Pyrite-modified oxide:** **FeS₂** accelerates **complete oxidation** toward **CO** and **CO₂** with **SOH**-related **sulfur** chemistry and inferred **surface reconstruction** (abstract).

**Comparisons:** The abstract contrasts **clean** versus **pyrite-covered** **selectivity**; experimental **coal/slagging** motivation is in the introduction on **`pdf_path`**.

**Sensitivity:** Results are anchored to the **1600 K** simulation window emphasized in the abstract—lower-temperature catalytic regimes are not claimed there.

**Limitations / outlook:** **Proof PDF** layout caveats; **single-surface** models omit **particle**/**support** complexity; detailed **kinetic** barriers require the full text/SI, not this short summary.

## Limitations

**Proof PDF** may differ in **pagination** and **figure embedding** from the **version of record**. Definitive **timesteps**, **run lengths**, and tabulated observables appear in **`pdf_path`** and the SI package [[2015shin-venue-microsoft-word]]. **Single-surface** models omit **particle** and **support** complexity.

## Relevance to group

**Penn State / CFDRC** **Fe/Cr/O/S** **ReaxFF** effort for **coal/slagging-relevant** oxidation chemistry.

## Citations and evidence anchors

- DOI `10.1021/acscatal.5b01766`; `papers/Shin_ACS_Catalysis_2015_proof.pdf`; SI: `papers/Shin_ACS_Catalysis_2015_SI.pdf`.

## Related topics

- [[2015shin-venue-research]]
- [[2015shin-venue-microsoft-word]]
- [[reaxff-family]]
