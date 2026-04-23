---
id: paper:2013raju-venue-jp402139h
type: paper
title: "ReaxFF Reactive Force Field Study of the Dissociation of Water on Titania Surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:oxides-ceramics
  - material:oxide
  - method:reaxff
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp402139h"
year: 2013
authors:
  - "Raju, Muralikrishna"
  - "Kim, Sung-Yup"
  - "van Duin, Adri C. T."
  - "Fichthorn, Kristen A."
venue: "Journal of Physical Chemistry C"
pdf_sha256: "d83481ec63778cddf80bfd11c3468c8738525b0d04cf43387d57ffd59383f8f9"
pdf_path: "papers/Raju_TiO2_water_JPC_C_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013raju-venue-jp402139h -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Water–**titania** interactions underpin **photocatalysis**, **solar cells**, **sensors**, and **biomaterials**, yet **atomistic** models must balance **reactivity** with **system size** for **wet** interfaces. This *J. Phys. Chem. C* study—duplicated in the corpus as **`paper:2013raju-venue-jp-2013-02139h`** under a distinct PDF filename—uses a **Ti/O/H ReaxFF** parametrization to simulate **adsorption** and **dissociation** of **water** at **300 K** on **anatase (101), (100), (112), (001)** and **rutile (110)** surfaces across **multiple coverages**. The authors compare **molecular** versus **dissociative** arrangements against **DFT** and **experiment**, then quantify **dissociation extent** as a function of **facet** and **coverage**, relating trends to **hydrogen-bond** coupling between **adsorbed** and **outer** water layers.

## Methods

Grounding: `papers/Raju_TiO2_water_JPC_C_2013.pdf`; `normalized/extracts/2013raju-venue-jp402139h_p1-2.txt` (abstract + early Methods; overlaps DOI `10.1021/jp402139h` with [[2013raju-venue-jp402139h-2]]).

### 1 — MD application (same article text as [[2013raju-venue-jp402139h-2]])

For **numerical MD settings** (ensemble, timestep, thermostat coupling, segment lengths, ML definitions, and coverage grid), this wiki’s most explicit excerpt-backed summary lives on **`paper:2013raju-venue-jp402139h-2`** (`normalized/extracts/2013raju-venue-jp402139h-2_p1-2.txt`). At a high level, the work studies **water at 300 K** on **anatase (101), (100), (112), (001)** and **rutile (110)** with **multiple coverages** using a **recently developed Ti/O/H ReaxFF** reactive model (abstract).

- **Engine / code:** **Molecular dynamics** with **ReaxFF** as in the abstract; **software packaging** is specified on the continued Methods pages—see [[2013raju-venue-jp402139h-2]] (**ADF ReaxFF implementation** there).
- **System size & composition:** **Water + periodic TiO\(_2\) slab** interfacial cells with **random** initial water placements at **0.50–3.0 ML** coverages (ML defined vs **Ti\(_{5c}\)** sites) as detailed on [[2013raju-venue-jp402139h-2]]; explicit **atom counts** are **not copied** onto this duplicate-PDF wiki page—read `pdf_path` tables.
- **System / boundary / ensemble / timestep / thermostat / duration / coverage:** See [[2013raju-venue-jp402139h-2]] for excerpt-backed values (**NVT**, **0.25 fs**, **Berendsen 100 fs**, **500 ps** protocol, **0.50–3.0 ML** grid).
- **Barostat:** N/A — **NVT** as on [[2013raju-venue-jp402139h-2]].
- **Temperature:** **300 K** (abstract).
- **Pressure:** N/A.
- **Electric field:** N/A.
- **Replica / enhanced sampling:** N/A.

### 2 — Force-field training

N/A — **application/validation** of a published **Ti/O/H ReaxFF** parameterization with extensive ReaxFF methodology exposition (extract), not a new parametrization paper.

## Findings

- **Outcomes & mechanisms:** Abstract-level results match [[2013raju-venue-jp402139h-2]]: **facet- and coverage-dependent** water structuring, **dissociation extents** broadly consistent with **prior DFT/experiment**, and a demonstrated **correlation** between **dissociation** and **H-bonding** to **non-adsorbed** water via **O–H stretch red shifts** for adsorbed water.
- **Comparisons:** Explicit comparisons to **prior DFT** catalogs and **experimental** adsorption/dissociation literature are claimed in the abstract.
- **Sensitivity / design levers:** **Facet** and **coverage** are the primary knobs in the abstract framing; **temperature** is fixed at **300 K** in the abstract statement.
- **Limitations & outlook:** N/A — not captured on p1–2 extract for this slug; consult full PDF.
- **Corpus honesty:** **Duplicate PDF filename variant** in the corpus for the same article; use **`paper:2013raju-venue-jp402139h-2`** when you need **Methods numbers** from a shorter, operator-indexed extract.

## Limitations

Duplicate corpus path for the same article generation; full quantitative tables appear beyond the p1–2 extract.

## Relevance to group

Core oxide–electrolyte interface science with van Duin authorship; feeds later TiO₂ nanocrystal aggregation and battery-adjacent interface work in the corpus.

## Citations and evidence anchors

- Footer: J. Phys. Chem. C 2013, 117, 10558–10572 and DOI `10.1021/jp402139h` (extract page 2).
- Abstract (extract page 1).

## Related topics

- [[reaxff-family]]
