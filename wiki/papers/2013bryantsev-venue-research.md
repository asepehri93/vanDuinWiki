---
id: paper:2013bryantsev-venue-research
type: paper
title: "Investigation of fluorinated amides for solid-electrolyte interphase stabilization in Li–O₂ batteries using amide-based electrolytes (galley proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - material:li-metal-anode
  - method:dft-static
  - task:application
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:batteries-interfaces
  - keyword:dft-static
  - keyword:validation-experiment
source_refs: []
doi: "10.1021/jp402844r"
year: 2013
authors:
  - "Bryantsev, Vyacheslav S."
  - "Giordani, Vincent"
  - "Walker, Wesley"
  - "Uddin, Jasim"
  - "Lee, Ilkeun"
  - "van Duin, Adri C. T."
  - "Chase, Gregory V."
  - "Addison, Dan"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "438c4d38415694e48ccc0464ba21a5df47412f98b0eec86794096c8a09e747d7"
pdf_path: "papers/Bryantsev_FluorAmides_JPC_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013bryantsev-venue-research -->

ACS **galley / line-numbered proof** PDF for the fluorinated-amide Li–O₂ electrolyte and Li-anode SEI study; scientific content matches the version-of-record summarized on [[2013bryantsev-venue-jp402844r]].

## Evidence and attribution

!!! note "Authority of statements"

    This corpus PDF is a **galley proof**. For authoritative pagination and final copy-edited wording, use the **published** article (`doi` above) and [[2013bryantsev-venue-jp402844r]].

## Summary

N,N-dialkyl amides such as DMA are attractive solvents for Li–O₂ cathode chemistry relative to carbonates and glymes, but they do not inherently passivate Li metal against sustained electrolyte reaction. The work benchmarks fluorinated amide formulations—notably N,N-dimethyltrifluoroacetamide (DMTFA)—using symmetric Li/electrolyte/Li cells, electrochemical impedance spectroscopy (EIS), and cycling, combined with quantum-chemistry arguments and XPS. α-Fluorinated amides are argued to reduce toward LiF-rich SEI components; XPS supports fluoride after DMTFA exposure. A 2% DMTFA additive in LiTFSI/DMA is reported to improve Li anode behavior in a rechargeable Li–O₂ demonstration context.

## Methods

**Electrochemistry (symmetric Li cells).** The Experimental section (see `pdf_path`) reports symmetric **Li / electrolyte / Li** cells with **electrochemical impedance spectroscopy (EIS)** and **galvanostatic Li stripping–plating** to compare interfacial impedance and polarization for several **fluorinated N,N-dialkyl amide** solvents against **N,N-dimethylacetamide (DMA)** baselines, using **LiTFSI** and (where noted) **LiClO₄** at concentrations given in the article.

**Surface analysis.** **X-ray photoelectron spectroscopy (XPS)** is used on **Li** foils exposed to selected amide electrolytes to probe **F**-containing **SEI** components, including after **DMTFA** exposure.

**1 — MD application (atomistic dynamics).** **N/A —** this publication’s core evidence is **electrochemistry**, **quantum chemistry**, and **XPS**; no atomistic **MD** production protocol is summarized in the indexed galley excerpt (`normalized/extracts/2013bryantsev-venue-research_p1-2.txt`).

**2 — Force-field training.** **N/A —** not a **ReaxFF** (or other empirical **FF**) parameterization study.

**3 — Static QM / DFT.** The **Abstract** states **quantum chemical calculations** on **reduction** of **α-fluorinated amides** on **Li** toward **insoluble LiF**, described qualitatively as proceeding with **little or no activation energy** (exact **barrier** values and **transition-state** details should be read from the full article PDF). **Functional:** **N/A —** not stated in the **p1–2** galley extract on file. **Dispersion correction:** **N/A —** not stated in the excerpt. **Basis set** (and any **plane-wave**/**PAW** choices): **N/A —** not stated in the excerpt. **k-point** / **k-mesh** sampling: **N/A —** not stated in the excerpt. Confirm all **QM** settings against **`pdf_path`** or [[2013bryantsev-venue-jp402844r]]. **Structures / pathways:** reduction of **α-fluorinated alkyl amides** at **Li** surfaces toward **LiF**-forming chemistry (abstract-level framing in the extract). **Properties computed:** **reduction energetics** / **barrier** estimates as reported in the **Computational** section of the full PDF (not transcribed in the short extract).

**4 — Reviews / non-simulation.** **N/A —** primary article with mixed **experiment + QM**, not a review.

## Findings

Among the fluorinated amides examined, **LiTFSI** in **DMTFA** shows the smallest interfacial impedance and the lowest polarization for **Li** dissolution/deposition in the symmetric-cell screening **compared** to the other solvents tested in the article. **α-Fluorinated amides** are **computed** to reduce on **Li** with little or no activation **barrier** toward **LiF**, and **XPS** on **DMTFA**-exposed **Li** supports **fluoride**-rich interfacial composition **versus** purely organic-fluoride scenarios without **LiF** dominance. A practical additive formulation (**0.5 M LiTFSI** in **98% DMA / 2% DMTFA**) is reported to stabilize **Li** cycling in a rechargeable **Li–O₂** demonstration **relative to** **DMA** alone. **Limitations / outlook:** proof PDFs can differ from the final **version-of-record** text; external citations should follow published pagination on [[2013bryantsev-venue-jp402844r]]. **Corpus honesty:** this slug tracks **`papers/Bryantsev_FluorAmides_JPC_galley.pdf`** as a **galley** duplicate of the same **DOI**; numerical tables and **PDF** locators should be taken from **`pdf_path`** or the sibling **VOR** page, not invented here.

## Limitations

Proof PDFs can differ slightly from the final edited article; cite the published DOI for external scholarship. Full experimental detail and figure numbering align with [[2013bryantsev-venue-jp402844r]].

## Relevance to group

Adri C. T. van Duin is a co-author; duplicate ingest documents acquisition of the galley-stage bytes for the same DOI.

## Citations and evidence anchors

- Published article: [10.1021/jp402844r](https://doi.org/10.1021/jp402844r)

## Reader notes (navigation)

- Primary corpus PDF and curated locators: [[2013bryantsev-venue-jp402844r]].

## Related topics

- [[2013bryantsev-venue-jp402844r]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
