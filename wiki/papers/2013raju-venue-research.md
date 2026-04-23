---
id: paper:2013raju-venue-research
type: paper
title: "ReaxFF reactive force field study of the dissociation of water on titania surfaces (galley PDF)"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:water-interfaces
  - keyword:galley-or-proof-pdf
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp402139h"
year: 2013
authors:
  - "Muralikrishna Raju"
  - "Sung-Yup Kim"
  - "Adri C. T. van Duin"
  - "Kristen A. Fichthorn"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "0e482ee89dbfdb2c02f08b6494f20452974372e3a89eb86fcd6c9090834ad8ad"
pdf_path: "papers/Raju_TiO2_water_JPC_C_2013_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013raju-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    This slug registers a **galley** PDF for the JPCC article summarized on [[2013raju-venue-jp402139h-2]].

## Summary

This galley-backed slug captures the same scientific article summarized on [[2013raju-venue-jp402139h-2]]: a **ReaxFF reactive MD** study of water adsorption and dissociation on key **anatase** and **rutile** TiO\(_2\) facets at **300 K**. The scientific question is not simply whether water adsorbs, but how the **balance between associative and dissociative adsorption** changes with surface structure and coverage, and which interfacial interactions control that balance.

In the extract-backed abstract, the authors compare **anatase (101), (100), (112), (001)** and **rutile (110)** across multiple coverages. ReaxFF is reported to reproduce both molecular and dissociated motifs in line with prior theory/experiment. The article emphasizes that water behavior is controlled by an interplay among: (i) spacing and arrangement of under-coordinated Ti/O adsorption sites, (ii) water-surface bonding, and (iii) water-water hydrogen-bond networking above the first layer.

A key interpretation in the abstract is a correlation between water dissociation extent and hydrogen-bond strength between adsorbed water and outer-layer water, reflected by **red shifts in adsorbed O-H stretching modes**. That coupling between first-layer chemistry and overlayer hydration is the main mechanistic takeaway surfaced in p1-2 text. As this slug is a galley ingest, stable figure/table pagination is better taken from the canonical reduced PDF slug.

Readers should verify fine-grained numerical values and panel-level references against the canonical publication copy and supporting files when available.

## Methods

This slug is the **galley** PDF bytes at `papers/Raju_TiO2_water_JPC_C_2013_galley.pdf` for the same *J. Phys. Chem. C* article as [[2013raju-venue-jp402139h-2]]. The **protocol numbers** below are taken from the **shared article text** excerpted on **`paper:2013raju-venue-jp402139h-2`** (`normalized/extracts/2013raju-venue-jp402139h-2_p1-2.txt`), not from galley-specific differences.

### 1 — MD application

- **Engine / code:** **Molecular dynamics** with **ReaxFF in ADF** (shared Methods excerpt; see [[2013raju-venue-jp402139h-2]]).
- **System / periodicity:** **Periodic TiO\(_2\)** slabs with interfacial **water** for **anatase (101), (100), (112), (001)** and **rutile (110)** (abstract).
- **Ensemble / timestep / thermostat / duration / coverages:** **NVT**, **0.25 fs**, **Berendsen** (**100 fs** coupling), **500 ps** (**100 ps** equilibration + **400 ps** production), **0.50–3.0 ML** grid (definitions as in paper) — see [[2013raju-venue-jp402139h-2]] excerpt.
- **Barostat:** N/A — **NVT**.
- **Temperature:** **300 K** (abstract).
- **Pressure:** N/A.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training

N/A — **application** of a **Ti/O/H ReaxFF** parameterization (same article as [[2013raju-venue-jp402139h-2]]).

### 3 — Static QM / DFT-only

N/A — the local extract positions DFT and other ab initio methods as prior-literature comparators, not as the primary engine for the new dataset.

## Findings

Same abstract-level **findings** as [[2013raju-venue-jp402139h-2]]: **facet/coverage-dependent** water structuring, **dissociation extents** broadly consistent with **prior DFT/experiment**, and the **dissociation vs outer-layer H-bonding** correlation supported by **O–H red shifts** (abstract).

- **Outcomes and mechanisms:** The article treats dissociation as a dynamic equilibrium between molecularly adsorbed and dissociated states on TiO\(_2\), where proton transfer to bridging oxygen is modulated by local hydrogen-bond network structure.
- **Comparisons:** ReaxFF motif predictions are reported as consistent with earlier theoretical and experimental observations, supporting use of reactive MD for larger-scale wet-interface sampling than typical first-principles trajectories permit.
- **Sensitivity:** Surface polymorph/facet identity and water coverage are the principal levers examined in the extract-backed framing.
- **Limitations from corpus view:** Precise quantitative dissociation fractions and vibrational shifts by facet/coverage are not fully enumerated in the local p1-2 extract and should be cited from the full article tables/figures.

- **Corpus honesty:** **Galley PDF** provenance only; prefer **`paper:2013raju-venue-jp402139h-2`** + `papers/Raju_TiO2_water_JPC_C_2013_reduced.pdf` for stable **pagination** and **figure** references.

## Limitations

Galley formatting; prefer the canonical PDF slug for stable pagination when available.

## Relevance to group

Duplicate ingest; primary narrative: [[2013raju-venue-jp402139h-2]].

## Citations and evidence anchors

- DOI: [10.1021/jp402139h](https://doi.org/10.1021/jp402139h)
- Extract: `normalized/extracts/2013raju-venue-research_p1-2.txt`

## Related topics

- [[2013raju-venue-jp402139h-2]]
- [[reaxff-family]]
