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
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013huang-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Reactive MD examines **chemo-mechanical fracture** of **defective zigzag (18,0) single-walled carbon nanotubes** under **uniaxial strain** at **300 K** using **ReaxFF**, with **Li** placed on the outer surface at varying **Li:C** ratios (**0, 1:36, 1:12, 1:6**). Two defect types are considered: a **single vacancy** and a **10-carbon hole**. The abstract/intro distinguishes **abrupt** fracture (including **Li-assisted weakening** at the crack tip or Li-absent fast failure) vs **retarded** **“wait-and-go”** propagation where the crack arrests until **Li diffusion** weakens the tip region. Motivation ties to **Li-ion battery** electrode mechanics and prior **in situ TEM** observations of **embrittlement** in multi-walled CNTs. The Letter frames defects as more than structural flaws: they can shorten **Li** diffusion paths into the tube wall and generate stress fields that steer **Li** toward the defect, where accumulated **Li** is described as weakening **C–C** bonds and “corrosively” biasing crack nucleation and growth.

## Methods

**1 — MD application** (from **`papers/Huang_APL_2013_LiCNT.pdf`** and `normalized/extracts/2013huang-venue-paper_p1-2.txt`). **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** for **Li–C** (bond-order energetics plus geometry-dependent charges); integration software **N/A** — not named on indexed **pp. 1–2** (confirm in full **PDF**). **System size & composition:** **(18,0)** zigzag **SWCNT** **~7.2 nm** long (**~1200 carbon atoms**); **Li** randomly on the **outer** surface at **Li:C = 0, 1:36, 1:12, 1:6** (Fig. 1). **Boundaries / periodicity:** **PBC** along the tube **axial** direction. **Ensemble:** tensile runs at fixed **temperature** are described with **Nosé–Hoover** control at **300 K**, consistent with **NVT**-style sampling (**NPT** **N/A** — not stated on excerpt). **Timestep:** **N/A** — not stated on **p1–2** extract; confirm **fs** integration settings in the **PDF**. **Duration / stages:** pre-load **equilibration** toward a low-energy state, then **uniaxial** extension at **0.01 Å/ps** until rupture (**ps**-scale segments as tabulated in the article). **Thermostat:** **Nosé–Hoover** at **300 K**. **Barostat:** **N/A** — no **hydrostatic pressure** / **NPT** barostat on excerpt. **Pressure / stress:** uniaxial **stress**–**strain** loading only; bulk **pressure** control **N/A**. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

**2 — Force-field training.** **N/A** — application of published **ReaxFF** **Li/C** validation references, not a new fit in this Letter.

**3 — Static QM.** **N/A** — not the reported methodology on the indexed pages.


## Findings

**Outcomes & mechanisms:** **Defect size** and **Li** **concentration** set **abrupt** vs **retarded** fracture under the same **uniaxial** load. **Abrupt** failure either involves **Li** weakening the moving crack tip or proceeds with little **Li** participation; **retarded** (“wait-and-go”) propagation **arrests** until **diffusing Li** reaches the tip and enables further **extension**—**corrosive** **C–C** weakening at defects is central to the picture in the Letter.

**Comparisons:** Motivation cites **in situ TEM** on **MWCNT** embrittlement vs more ductile pristine tubes; simulation **mode** maps are tied to those **experimental** observations at the narrative level in the **PDF**.

**Sensitivity / design levers:** **Li:C** ratio and defect class (single vacancy vs **10-carbon** hole) move the system between regimes at fixed **300 K** loading protocol.

**Limitations & outlook:** **Mechanical** response of **SWCNT** models may not capture all **MWCNT** **experimental** conditions; **strain rate** and **electrochemical** environment effects follow the authors’ discussion in the article.

**Corpus honesty:** **`extraction_quality: partial`**; quantitative kinetics beyond the abstract/Letter opening should be verified in the full **`pdf_path`** (not only `normalized/extracts/2013huang-venue-paper_p1-2.txt`).

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
