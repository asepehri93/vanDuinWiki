---
id: paper:2013epoxide-venue-paper
type: paper
title: "Stability of Si epoxide defects in Si nanowires: a mixed reactive force field/DFT study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - method:dft-static
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:reactive-md
  - keyword:oxide-surface
source_refs: []
doi: "10.1039/c3cp51621k"
year: 2013
authors:
  - "Schoeters, Bob"
  - "Neyts, Erik C."
  - "Khalilov, Umedjon"
  - "Pourtois, Geoffrey"
  - "Partoens, Bart"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "a29d654b7dbefac0e5f222db468ab92e48f4051b4f34f73c20ac364cfc343930"
pdf_path: "papers/ReaxFF_others/Epoxide_Neyts_et_al_PCCP_2013_proof.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2013epoxide-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Bibliographic grounding follows **Crossref** for DOI `10.1039/c3cp51621k`. The corpus PDF is an **RSC accepted-manuscript / proof** class file; automated text extraction captured **publisher front-matter**, so on-disk `extraction_quality` remains **partial** until a clean full-text extract exists.

## Summary

**Si nanowire** models containing **epoxide-like** oxygen defects are studied with a **mixed ReaxFF + DFT** protocol to quantify **defect stability** and structural response. The PCCP article (2013) frames **oxygen-decorated** Si nanostructures as relevant to oxidation and surface chemistry in nanoscale silicon systems, using **ReaxFF** for large-scale configurational sampling coupled to **DFT** checks where reported in the paper.

## Methods

The corpus PDF is an **RSC accepted manuscript / proof** (`pdf_path`); the short extract `normalized/extracts/2013epoxide-venue-paper_p1-2.txt` contains **publisher front matter** plus the **Communication** opening paragraphs, not the full **Computational** section table.

**1 — MD application (atomistic dynamics).** **Engine / code:** **Reactive force field based molecular dynamics** is described in the extract as the tool used to study **Si nanowire** oxidation motifs (**ReaxFF**-class workflow; confirm the explicit **MD** engine string in **`pdf_path`**). **System size & composition:** **Si nanowire** models with **epoxide**-like **O** defects (diameters and **atom** counts in **`pdf_path`** **Methods**). **Boundaries / periodicity:** **N/A —** boundary treatment not stated in the indexed excerpt (likely **PBC** nanowire supercells in the published article—confirm). **Ensemble / timestep / duration / thermostat / barostat / temperature / pressure:** **N/A —** not stated in the indexed excerpt; read **`pdf_path`** for **NVT**/**NPT** choices, **timestep**, **thermostat**, and run lengths. **Electric field:** **N/A —** not stated. **Replica / enhanced sampling:** **N/A —** not stated.

**2 — Force-field training.** **N/A —** application/fitting of an established **ReaxFF** description for **Si**/**O**/**H** chemistry as used in the study (not a new parameterization tutorial).

**3 — Static QM / DFT.** **DFT** is used to support stability arguments for **epoxide** defects on **curved** vs **flat** **Si** motifs (extract + title). **Functional / basis / k-mesh / dispersion:** **N/A —** not stated in the indexed **p1–2** text; copy from the **version-of-record** **PCCP** **Computational** section when quoting details externally.

## Findings

**1 — Outcomes & mechanisms.** The **abstract** argues **epoxide** formation occurs at both **Si/SiOₓ**-like interfaces and **nanowire** surfaces, whereas on **flat** surfaces analogous defects are tied to **stress** in prior work; **curvature** is proposed to **stabilize** **epoxide** at the **surface**, with **DFT** support referenced in the article. **Gap**-related **electronic** consequences are discussed at qualitative level.

**2 — Comparisons.** The text connects modeling predictions to prior **experimental** literature on **Si** oxidation/defects as cited in the **Introduction** (**pdf_path**).

**3 — Sensitivity & design levers.** **Hydrogenation** is discussed as a route to remove **epoxide** defects, with difficulty increasing as **nanowire** diameter shrinks (**abstract** claim).

**4 — Limitations & outlook.** **Accepted manuscript** status and **partial** extraction imply figure/table numbering may change; cite the final **PCCP** layout for external scholarship.

**5 — Corpus honesty.** **`extraction_quality: partial`** reflects **publisher** boilerplate in the extract; do not infer computational parameters not printed in **`pdf_path`**.

## Limitations

- Proof PDF / poor extract in corpus: prefer the **final PCCP** PDF for figures and exact numerical tables.

## Relevance to group

Connects **Neyts**-line **ReaxFF** work on **oxide/epoxide** defect chemistry in **Si** nanostructures—useful cross-link to plasma/oxidation themed corpus notes.

## Citations and evidence anchors

- Volume **15**, pp. **15091**… (PCCP; DOI above).

## Related topics

- [[reaxff-family]]
- [[2013u-khalilov-j-phys-chem-new-mechanisms]]
