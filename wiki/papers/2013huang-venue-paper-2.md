---
id: paper:2013huang-venue-paper-2
type: paper
title: "Lithiation induced corrosive fracture in defective carbon nanotubes"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:batteries-electrochemistry, material:graphene-carbon-nano, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1063/1.4824418"
year: 2013
authors: ["Huang, Xu", "Yang, Hui", "Liang, Wentao", "Raju, Muralikrishna", "Terrones, Mauricio", "Crespi, Vincent H.", "van Duin, Adri C. T.", "Zhang, Sulin"]
venue: "Applied Physics Letters (author proof)"
pdf_sha256: "894b007d5f43942bf42bd828be1586aedb5da5b578af9969c12c1aa205d18ebe"
pdf_path: "papers/Huang_APL_2013_LiCNT_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013huang-venue-paper-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This corpus entry registers an **AIP author proof** PDF for the same **Applied Physics Letters** article as **`paper:2013huang-venue-paper`** (DOI **10.1063/1.4824418**). The scientific content matches the published Letter: **ReaxFF molecular dynamics** is used to study **chemo-mechanical fracture** of **defective zigzag (18,0) single-walled carbon nanotubes (SWCNTs)** under **uniaxial tension** at **300 K**. Lithium is loaded on the **outer surface** at several **Li:C** stoichiometries (**0**, **1:36**, **1:12**, **1:6**), and two defect classes are compared: a **single vacancy** versus a **hole-like defect** formed by removing **10 carbon atoms**. The abstract frames two qualitative fracture regimes—**abrupt** versus **retarded** failure—and links them to whether lithium participates directly at the moving crack tip or arrives by **diffusion** during **“wait-and-go”** crack advance.

The introduction motivates the study from **lithium-ion battery** electrode mechanics and cites **in situ transmission electron microscopy** observations that **lithiation can embrittle multi-walled CNTs**, producing sharp fracture edges and apparently reduced ductility relative to pristine tubes. The authors argue that **defects** can both **shortcut lithium transport** into the tube interior and generate **stress and chemical-potential gradients** that drive lithium toward defect cores, where accumulated lithium is described as **weakening C–C bonding** and thereby modulating **crack nucleation and propagation** in a corrosive-fracture picture.

## Methods

**1 — MD application** (proof text + `normalized/extracts/2013huang-venue-paper-2_p1-2.txt`; align numbers with **[[2013huang-venue-paper]]**). **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** for **Li–C**; MD package name **N/A** on indexed proof pages. **System:** **(18,0)** **SWCNT** **~7.2 nm** (**~1200 carbon atoms**); **Li** on the **outer** surface at **Li:C = 0, 1:36, 1:12, 1:6**; **atoms** randomly placed then **equilibrated**. **Boundaries:** **PBC** along the tube **axial** direction. **Ensemble:** **NVT**-like thermal control via **Nosé–Hoover** at **300 K** during tensile loading (Letter content mirrored on proof). **Timestep:** **N/A** on proof excerpt—confirm **fs** settings in **VOR** **PDF**. **Duration:** **equilibration** then **uniaxial** pull at **0.01 Å/ps** until failure (**ps**-scale segments per article). **Thermostat:** **Nosé–Hoover**, **300 K**. **Barostat:** **N/A** — excerpt does not define **NPT** **pressure** coupling. **Pressure:** **N/A** for bulk hydrostatic control; mechanical **stress** from **strain** only. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

**2 — Force-field training.** **N/A** — published **ReaxFF** **Li/C** field as in the Letter.

**3 — Static QM.** **N/A** — not the focus on excerpted proof pages.

The proof PDF contains **production queries**; use **`papers/Huang_APL_2013_LiCNT.pdf`** on [[2013huang-venue-paper]] for **version-of-record** layout.


## Findings

**Outcomes & mechanisms:** **Defect size** and **lithium concentration** select **abrupt** vs **retarded** fracture. **Abrupt** cases include tip weakening by **Li** or failure with **little lithium participation**; **retarded** **“wait-and-go”** advance **arrests** until **diffusing lithium** weakens the tip (**corrosive** **C–C** weakening narrative on proof/abstract pages).

**Comparisons:** Same qualitative claims as the **VOR** Letter (**DOI** `10.1063/1.4824418`); **TEM**-motivated **battery** context matches [[2013huang-venue-paper]].

**Sensitivity / design levers:** **Li:C** ratio and defect type (single vacancy vs **10-carbon** hole) in Fig. 1 map referenced on opening pages.

**Limitations & outlook:** Proof-stage figures/text may differ from final **AIP** publication; **strain rate** and **electrode** realism per authors’ full discussion.

**Corpus honesty:** **Galley/proof** **`pdf_path`**; detailed **stress–strain** and movies live on **VOR** **PDF**—not re-derived here from queries-only pages.

## Limitations

The registered file is an **author proof**, not the publisher’s final layout. **Extraction_quality** is **partial** for this slug because the corpus snippet emphasizes front matter and introduction. Reactive MD at **finite strain rate** and **nanometer-scale** tubes may not capture all experimental **MWCNT** conditions cited for motivation.

## Relevance to group

Duplicate **manifest provenance** for a **van Duin**-coauthored **ReaxFF** study connecting **Li transport**, **defect chemistry**, and **mechanical failure** in **nanocarbon** electrodes.

## Citations and evidence anchors

- Proof header, abstract, and introduction start (DOI **10.1063/1.4824418**; see `normalized/extracts/2013huang-venue-paper-2_p1-2.txt`).

## Reader notes (navigation)

- Primary non-proof page: [[2013huang-venue-paper]]

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[graphene-nanocarbon]]
