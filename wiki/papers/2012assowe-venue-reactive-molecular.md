---
id: paper:2012assowe-venue-reactive-molecular
type: paper
title: "Reactive molecular dynamics of the initial oxidation stages of Ni(111) in pure water: Effect of an applied electric field"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:batteries-electrochemistry, domain:oxides-ceramics, method:reaxff, task:application, material:metal-surface]
candidate_tags: []
source_refs: []
doi: "10.1021/jp306932a"
year: 2012
authors: ["Assowe, O.", "Politano, O.", "Vignal, V.", "Arnoux, P.", "Diawara, B.", "Verners, O.", "van Duin, A. C. T."]
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "96cbf53e6749b343efdfc44c0dc05077578aa756e14b69539b0bdb2118e620e5"
pdf_path: "papers/Assowe_JPCA_2012.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2012assowe-venue-reactive-molecular -->

## One-paragraph summary

The authors apply **ReaxFF MD** to **Ni(111)** in contact with **liquid water** (~480 H₂O molecules, ρ ≈ 0.99 g/cm³, **300 K**). Without an external field, water **does not dissociate**, but the excerpt reports a **charged double layer** (positive Ni surface vs negative first water layer). With an imposed **electric field (10–20 MV/cm)**, **anodic oxidation** proceeds: oxide growth is analyzed via **anion ingress** and **Ni outward migration**, with **thickness scaling approximately linearly** with field strength and faster corrosion at higher field.

## Methods

- **Reactive MD (ReaxFF)** for **Ni–O–H** chemistry at a metal–water interface with applied electric field to mimic electrochemical driving.

## Findings

- Field-free interface: stable water bilayer-like adsorption and **no water dissociation** in the reported conditions.
- With field: **oxide film growth** with mechanistic interpretation based on ion transport and trajectory analysis.

## Limitations

- Field magnitudes and simulation times are model-specific; quantitative comparison to experiment needs careful mapping of **electrode potential** to **classical field** protocols.

## Relevance to group

Illustrates **ReaxFF for aqueous metal oxidation** and **electrochemical interface** modeling—adjacent to corrosion and battery interface themes.

## Citations and evidence anchors

- Abstract and introduction: Ni(111)–water setup, field strengths, double-layer and oxidation observations (J. Phys. Chem. A 2012, 116, 11796–11805; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
