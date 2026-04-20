---
id: paper:2013huang-venue-paper
type: paper
title: "Lithiation induced corrosive fracture in defective carbon nanotubes"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:batteries-electrochemistry, material:graphene-carbon-nano, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1063/1.4824418"
year: 2013
authors: ["Huang, Xu", "Yang, Hui", "Liang, Wentao", "Raju, Muralikrishna", "Terrones, Mauricio", "Crespi, Vincent H.", "van Duin, Adri C. T.", "Zhang, Sulin"]
venue: "Applied Physics Letters"
pdf_sha256: "8fdf462fbe6178ea940a2f7ef78d2f09bba5bd68e195b4e5d8816740a050325d"
pdf_path: "papers/Huang_APL_2013_LiCNT.pdf"
extraction_quality: partial
group_affiliation: true
---

<!-- id:paper:2013huang-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Reactive MD examines **chemo-mechanical fracture** of **defective zigzag (18,0) single-walled carbon nanotubes** under **uniaxial strain** at **300 K** using **ReaxFF**, with **Li** placed on the outer surface at varying **Li:C** ratios (**0, 1:36, 1:12, 1:6**). Two defect types are considered: a **single vacancy** and a **10-carbon hole**. The abstract/intro distinguishes **abrupt** fracture (including **Li-assisted weakening** at the crack tip or Li-absent fast failure) vs **retarded** **“wait-and-go”** propagation where the crack arrests until **Li diffusion** weakens the tip region. Motivation ties to **Li-ion battery** electrode mechanics and prior **in situ TEM** observations of **embrittlement** in multi-walled CNTs.

## Methods

- **ReaxFF** for **Li–C** systems; **Nosé–Hoover** thermostat; **periodic axial** boundary conditions; constant **strain rate 0.01 Å/ps** until failure.

## Findings

- Fracture mode maps (abrupt vs retarded) as a function of **defect size** and **Li concentration** in the opening discussion; full quantitative curves may extend beyond the partial extract.

## Limitations

- Extraction **partial**; also note companion proof PDF slug `2013huang-venue-paper-2` overlaps content.

## Relevance to group

Demonstrates **ReaxFF** for **Li–nanocarbon** failure—directly relevant to **battery electrode** mechanical reliability.

## Citations and evidence anchors

- Title page + introduction + methods opening (Appl. Phys. Lett. 103, 153901 (2013); PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
