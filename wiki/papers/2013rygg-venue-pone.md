---
id: paper:2013rygg-venue-pone
type: paper
title: "Molecular Dynamics Simulations of Water/Mucus Partition Coefficients for Feeding Stimulants in Fish and the Implications for Olfaction"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - method:classical-md
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1371/journal.pone.0072271"
year: 2013
authors:
  - "Rygg, Alex D."
  - "van Duin, Adri C. T."
  - "Craven, Brent A."
venue: "PLoS ONE"
pdf_sha256: "46ad69e287bdebb6c54184165391ac59f21a333f0e19b0d7341e31ba7932b657"
pdf_path: "papers/Rygg_PLOSone_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013rygg-venue-pone -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

All-atom molecular dynamics on a simplified mucus model estimates water/mucus partition coefficients for amino-acid feeding stimulants (alanine, glycine, cysteine, valine) in fresh versus salt water. Fresh water favors mucus partitioning for all four acids with ordering linked to hydrophobicity; salt reverses preference (except glycine) through ion-mediated interactions. Partition coefficient variation stays ~one order of magnitude, much narrower than air/mucus spans in mammals, arguing against strong spatial chromatography for fish olfaction (abstract; introduction, extract pages 1–2).

## Methods

Grounding: `papers/Rygg_PLOSone_2013.pdf`; `normalized/extracts/2013rygg-venue-pone_p1-2.txt` (abstract + start of Methods / model description).

### 1 — MD application (all-atom MD; simplified mucus model)

- **Engine / code:** **Molecular dynamics simulations** are used (abstract). The **MD package** is **not named** on the indexed excerpt pages (`normalized/extracts/2013rygg-venue-pone_p1-2.txt`).
- **System size & composition:** The study uses a **simplified molecular model of olfactory mucus** to compute **water/mucus partition coefficients** for **alanine, glycine, cysteine, and valine** feeding stimulants (abstract). **Atom counts** are **not stated** on p1–2.
- **Electrolyte / environment:** Both **fresh water** and **salt water** environments are considered (abstract). The introduction discusses **ion-mediated interactions** between **salt ions**, **odorants**, and **mucin** as part of the partitioning story (extract).
- **Boundaries / periodicity:** N/A — **PBC details** are **not stated** on the indexed excerpt pages.
- **Ensemble:** **NVT** equilibration at **300 K** followed by **NPT** equilibration at **1 bar** and **300 K**, then production **NPT** at **1 bar** and **300 K** (`papers/Rygg_PLOSone_2013.pdf`, Methods excerpt extracted from PDF text).
- **Timestep:** N/A — **not stated** on the indexed excerpt pages.
- **Duration / stages:** N/A — **not stated** on the indexed excerpt pages.
- **Thermostat / barostat:** N/A — **not stated** on the indexed excerpt pages.
- **Temperature:** N/A — explicit **simulation temperature(s)** are **not stated** on the indexed excerpt pages.
- **Pressure:** N/A.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training

N/A — **classical all-atom MD** with a **reduced mucus model** (not a ReaxFF parametrization paper).

## Findings

- **Outcomes & mechanisms:** In **fresh water**, all four amino acids **prefer mucus over bulk water**, with partition coefficient trends linked to **hydrophobicity** (abstract). In **salt water**, partitioning **reverses** so stimulants (**except glycine**) prefer **water over mucus**, attributed to **ion–odorant** and **ion–mucin** interactions (abstract).
- **Comparisons:** Contrasts **water/mucus** partitioning spreads (**~one order of magnitude**) with **air/mucus** spans that can reach **~six orders of magnitude** in mammalian discussions (abstract).
- **Sensitivity / design levers:** **Fresh vs salt** solvent environment is the primary comparative axis in the abstract framing.
- **Limitations & outlook:** The abstract argues this argues against **strong spatial chromatography** for fish olfaction versus terrestrial nasal chromatography narratives, consistent with reported **lack of spatial ORN organization** in fish epithelium (abstract).
- **Corpus honesty:** Indexed excerpt includes **model formulation start** but not full **force field, thermostat, or run-length** tables; read **`pdf_path`** Methods for reproducibility.

## Limitations

Mucus chemistry is simplified; receptor-level biology and fluid advection (CFD) are outside the MD core reported in the opening pages.

## Relevance to group

van Duin coauthorship connects biomolecular MD modeling traditions at Penn State alongside reactive materials work.

## Citations and evidence anchors

- PLoS ONE 8(9): e72271; DOI `10.1371/journal.pone.0072271` (abstract metadata in extract).
- Abstract partition-coefficient narrative (extract page 1).

## Related topics

- [[reaxff-family]]
