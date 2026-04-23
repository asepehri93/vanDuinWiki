---
id: paper:2015verners-venue-paper
type: paper
title: "α-Al₂O₃ nanoslab fracture and fatigue (Elsevier proof / author query)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:oxides-ceramics
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2015.02.048"
year: 2015
authors:
  - "Osvalds Verners"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
venue: "Computational Materials Science (proof)"
pdf_sha256: "40e8d0fce98ddf51d927a5ee54ce4fddd10e7fa8c2640ce364a36e92d216cf31"
pdf_path: "papers/Verners_CompMatSci_2015_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2015verners-venue-paper -->

## Evidence and attribution

!!! note "Corpus role"

    The file `papers/Verners_CompMatSci_2015_proof.pdf` is an **Elsevier author-query / proof** workflow PDF. Local **`normalized/extracts`** text for this slug is **not** a clean article body. All **scientific** summary below is aligned to the **peer-reviewed article** curated as **`[[2015verners-computationa-al2o3-nanoslab]]`** (`papers/Verners_CompMatSci_2015.pdf`).

## Summary

This slug exists to register **manifest** provenance for a **proof**/**author-query** PDF tied to **DOI [10.1016/j.commatsci.2015.02.048](https://doi.org/10.1016/j.commatsci.2015.02.048)**—the **Computational Materials Science** study on **α-Al₂O₃** **nanoslab** **fracture** and **fatigue** using **ReaxFF** reactive MD and related **static** loading workflows. The **peer-reviewed** publication (see primary page) compares **finite-temperature dynamic** failure with **incremental static** pathways for **single-crystalline** slabs under **monotonic** and **cyclic** loading, examining **strain rate**, **lateral pre-strain**, and **size** effects on **failure strain**, **crack healing** versus **branching**, and **amorphization** ahead of cracks, with selected **DFT** context for bulk-like behavior. **Low-cycle fatigue**-relevant conclusions include **shakedown-like** elastic responses after repeated loading in some regimes. Because this corpus path is a **proof** artifact, automated **extract** snippets may contain **author-query** boilerplate, **watermarks**, or incomplete figure captions; always reconcile numerical stress–strain details and **ReaxFF** parameter notes against the **journal** PDF on the primary page before using values in downstream **MAS** records.

## Methods

`papers/Verners_CompMatSci_2015_proof.pdf` is an **Elsevier author-query / proof** workflow file for DOI **10.1016/j.commatsci.2015.02.048**. The simulation setup matches **`[[2015verners-computationa-al2o3-nanoslab]]`** (`papers/Verners_CompMatSci_2015.pdf`): **LAMMPS ReaxFF** on **3D periodic α-Al₂O₃ nanoslabs**; dynamic **NPT** tensile segments at **300 K**, **0.2 fs**, **0.25% / 0.5 ps** strain pulses with **5 ps** relaxations, **Nosé–Hoover** thermostat (**100 fs**) and barostat (**5000 fs**) driving lateral **0 Pa**; parallel **static** strain-plus-minimization branches; **VASP PBE** bulk checks as in the journal article. Query-sheet layout here can obscure tables—use the **journal** PDF for definitive parameters.

## Findings

Qualitative **mechanisms** match **`[[2015verners-computationa-al2o3-nanoslab]]`**: **dynamic** loading gives **lower failure strains** than incremental **static** loading; **pre-strain** and **volume pre-relaxation** shift **crack branching**, **healing**, and **elastic shakedown**; **amorphization** ahead of cracks supports **small-strain plasticity**. **Sensitivity** to **strain rate** and preparation path is discussed on the primary page relative to **temperature**-controlled **NPT** segments. **Limitations** of this **proof PDF** include query-sheet layout and possible table splits; however, the science should be read from the **version-of-record** **PDF** (`papers/Verners_CompMatSci_2015.pdf`) rather than inferred from workflow duplicates alone. **Comparisons** of **ReaxFF** moduli and fracture metrics to **DFT** and **experiment** appear in the journal article’s tables, not in this file.

## Limitations

**Proof** PDFs are **workflow artifacts**—may lack final pagination, figures, or copy-editing. **Nanoscale** slabs omit **grain boundaries** and **environmental** chemistry; **ReaxFF** validity is limited by its **QM** training envelope. For **fatigue** cycle counts and **stress** amplitudes, use tabulated simulation parameters from the **journal** PDF because the **query** layout may split tables across pages awkwardly.

## Relevance to group

**Penn State** collaboration on **ReaxFF** for **ceramic** **fracture** and **fatigue** and mechanical reliability.

## Citations and evidence anchors

- **DOI:** [10.1016/j.commatsci.2015.02.048](https://doi.org/10.1016/j.commatsci.2015.02.048) — proof artifact: `papers/Verners_CompMatSci_2015_proof.pdf`; article: `papers/Verners_CompMatSci_2015.pdf`.

## Reader notes (navigation)

- Peer-reviewed PDF: [[2015verners-computationa-al2o3-nanoslab]]

## Related topics

- [[2015verners-computationa-al2o3-nanoslab]]
- [[reaxff-family]]
