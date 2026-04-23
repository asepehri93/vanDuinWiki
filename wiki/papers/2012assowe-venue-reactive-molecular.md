---
id: paper:2012assowe-venue-reactive-molecular
type: paper
title: "Reactive molecular dynamics of the initial oxidation stages of Ni(111) in pure water: Effect of an applied electric field"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:batteries-electrochemistry, domain:oxides-ceramics, method:reaxff, task:application, material:metal-surface]
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:metallic-systems
  - keyword:reactive-md
source_refs: []
doi: "10.1021/jp306932a"
year: 2012
authors: ["Assowe, O.", "Politano, O.", "Vignal, V.", "Arnoux, P.", "Diawara, B.", "Verners, O.", "van Duin, A. C. T."]
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "96cbf53e6749b343efdfc44c0dc05077578aa756e14b69539b0bdb2118e620e5"
pdf_path: "papers/Assowe_JPCA_2012.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2012assowe-venue-reactive-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study applies **ReaxFF MD** to **Ni(111)** in contact with **liquid water** (~480 H₂O molecules, ρ ≈ 0.99 g/cm³, **300 K**). The question is how an atomistic metal–water interface evolves under field-free versus strongly biased conditions relevant to corrosion and electrochemistry-inspired modeling. Without an external field, water **does not dissociate**, but the excerpt reports a **charged double layer** (positive Ni surface vs negative first water layer). With an imposed **electric field (10–20 MV/cm)**, **anodic oxidation** proceeds: oxide growth is analyzed via **anion ingress** and **Ni outward migration**, with **thickness scaling approximately linearly** with field strength and faster corrosion at higher field, supporting a picture in which classical field magnitudes map to accelerated oxide propagation in these reactive simulations.

## Methods

### 1 — MD application (atomistic dynamics)

**Reactive molecular dynamics** using **ReaxFF** investigates a **Ni(111)** surface in contact with liquid-like water at **300 K** (`normalized/extracts/2012assowe-venue-reactive-molecular_p1-2.txt`).

- **Engine / code:** **ReaxFF MD** (Abstract + Sec. 2 opening); **N/A —** MD engine/package not named on the indexed excerpt pages.
- **System size & composition:** **480 H₂O** molecules at **ρ ≈ 0.99 g·cm⁻³** interacting with **Ni(111)** (Abstract, extract).
- **Boundaries / periodicity:** **N/A —** explicit **PBC** / slab thickness details are not stated on the indexed excerpt pages.
- **Ensemble / timestep / duration / thermostat / barostat:** **N/A —** **NVT**/**NPT**/**NVE** labels, timestep sizes, **production run** lengths, and thermostat/barostat algorithms are not stated on the indexed excerpt pages.
- **Temperature:** **300 K** (Abstract + Sec. 2 opening, extract).
- **Pressure / stress:** **N/A —** not stated on the indexed excerpt pages.
- **Electric field:** An external **electric field** between metal and solution is used for oxidation studies; the abstract reports intensities **10–20 MV/cm** (note: the ACS PDF extract shows a likely typo “MeV/cm” on p. 1; interpret as **MV/cm** in line with standard electrochemical modeling units—verify **`pdf_path`** for the authors’ intended notation).
- **Replica / enhanced sampling:** **N/A —** not stated on the indexed excerpt pages.

### 2 — Force-field training

**N/A —** application of an existing **ReaxFF** parameterization for **Ni–water** chemistry (Sec. 2 opening frames it as adopting the **van Duin** reactive FF approach, extract).

### 3 — Static QM / DFT-only

**N/A —** not the primary methodology on pp. 1–2 beyond contextual citations in the introduction (extract).

## Findings

**Outcomes and mechanisms (field-free):** A water “**bilayer**” adsorbs on **Ni(111)** at **300 K**; **no water dissociation** is observed without an applied field; surface **Ni** is charged positive and the first water layer negative, indicating an **electric double layer** (Abstract, extract).

**Outcomes and mechanisms (with field):** With an applied **electric field**, **oxidation** occurs; the abstract describes **oxide film** structural/morphological changes and interprets growth in terms of **anion ingress** into the metal and **Ni outward migration** toward the free surface (Abstract, extract).

**Sensitivity and design levers:** The abstract reports **faster corrosion** and **approximately linear oxide thickness vs field intensity** when increasing the field within the **10–20 MV/cm** range studied (Abstract, extract).

**Comparisons / limitations:** The introduction discusses experimental challenges in observing **earliest-stage oxidation** and positions atomistic modeling as complementary; it also notes challenges in first-principles electrochemical potential control for long passive-film growth (Introduction, extract).

**Corpus / KB honesty:** Detailed trajectory lengths, thermostat algorithms, and quantitative oxide stoichiometry profiles are **not** on the pp. 1–2 extract—verify **`pdf_path`** for full results sections.

## Limitations

- Field magnitudes and simulation times are model-specific; quantitative comparison to experiment needs careful mapping of **electrode potential** to **classical field** protocols. The finite water slab and short production segments capture early oxidation trends more readily than long-time passive film evolution or pH-dependent ion adsorption that laboratory electrochemistry couples to oxide growth.

## Relevance to group

Illustrates **ReaxFF for aqueous metal oxidation** and **electrochemical interface** modeling—adjacent to corrosion and battery interface themes.

## Citations and evidence anchors

- Abstract and introduction: Ni(111)–water setup, field strengths, double-layer and oxidation observations (J. Phys. Chem. A 2012, 116, 11796–11805; PDF pp. 1–2 per extract).

## Reader notes (navigation)

- Electrified Ni–water oxidation precedes many later [[batteries-interfaces-reaxff]] papers; compare [[2017ai-the-journal-reactive-force]] (Ni in supercritical water).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
