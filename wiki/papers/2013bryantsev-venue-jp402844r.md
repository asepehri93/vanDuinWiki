---
id: paper:2013bryantsev-venue-jp402844r
type: paper
title: "Investigation of fluorinated amides for solid-electrolyte interphase stabilization in Li–O₂ batteries using amide-based electrolytes"
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
pdf_sha256: "6a697d18b1a8bb1cfef1a042684ae6b06d667c5e80e392722a52389783a51670"
pdf_path: "papers/Bryantsev_FluorAmides_JPC_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013bryantsev-venue-jp402844r -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

**N,N-dialkyl amides** such as **DMA** are attractive solvents for **Li–O₂** cathode chemistry relative to carbonates/glymes, but they do not inherently passivate **Li metal** against sustained electrolyte reaction. This study benchmarks **fluorinated amide** formulations (notably **N,N-dimethyltrifluoroacetamide, DMTFA**) using **symmetric Li/electrolyte/Li cells**, **EIS**, and cycling, combined with **QM** arguments and **XPS**. **α-Fluorinated amides** are argued to reduce toward **LiF-rich SEI** components; **XPS** supports **LiF** after DMTFA exposure. A **2% DMTFA** additive in **LiTFSI/DMA** is reported to improve **Li anode** behavior in a rechargeable **Li–O₂** demonstration context.

## Methods


- **Electrochemistry:** **symmetric Li / electrolyte / Li** cells with **electrochemical impedance spectroscopy (EIS)** and **galvanostatic** **Li stripping–plating** to compare **interfacial impedance** and **polarization** across **fluorinated N,N-dialkyl amide** solvents relative to **N,N-dimethylacetamide (DMA)** baselines; electrolytes use **LiTFSI** (and **LiClO₄** where noted in the Experimental section) at concentrations stated in the article.
- **Electronic structure:** **quantum chemistry** calculations of **reduction** pathways for **α-fluorinated amides** on Li surfaces to identify low-barrier routes to **LiF**-forming chemistry.
- **Surface analysis:** **X-ray photoelectron spectroscopy (XPS)** of **Li** foils exposed to selected **amide** electrolytes to probe **F**-containing **SEI** components.

### Static QM / DFT (reduction of fluorinated amides)

**Functional:** **N/A —** explicit **DFT functional** not stated in `normalized/extracts/2013bryantsev-venue-jp402844r_p1-2.txt`; see **Computational** details in **`pdf_path`**.

**Dispersion:** **N/A —** not stated in the excerpt.

**Basis:** **N/A —** basis / **plane-wave** settings not stated in the excerpt.

**k-sampling:** **N/A —** **k**-point / **k**-mesh / **Brillouin** sampling not stated in the excerpt.

**Structures / pathways:** **Quantum chemical** models address **reduction** of **α-fluorinated amides** on **Li** surfaces along pathways that form **LiF** with **little or no activation energy** (abstract).

**Properties computed:** **Reaction energetics** / **barrier** estimates for **initial decomposition** leading to **LiF** (abstract).

### MD application

**N/A —** this work is **not** centered on **production AIMD** trajectories in the abstract/excerpt; any finite-temperature **MD** mention in **`pdf_path`** should be read there.

## Findings

- Among the fluorinated amides examined, **LiTFSI** in **N,N-dimethyltrifluoroacetamide (DMTFA)** shows the **smallest interfacial impedance** and the **lowest polarization** for Li dissolution/deposition in the symmetric-cell screening.
- **α-Fluorinated amides** are computed to reduce on Li with **little or no activation barrier** toward **LiF**, and **XPS** on **DMTFA**-exposed Li supports **fluoride**-rich interfacial composition consistent with that pathway.
- A practical **additive** formulation (**0.5 M LiTFSI** in **98% DMA / 2% DMTFA**) is reported to **stabilize** **Li** cycling in a **rechargeable Li–O₂** demonstration relative to **DMA** alone, while retaining an **amide**-based catholyte choice.

The combined electrochemical and spectroscopic thread supports a practical design rule: **low concentrations** of **α-fluorinated amide** can steer **SEI** chemistry toward **fluoride-rich** films without abandoning **amide** solvents chosen for **cathode** oxygen electrochemistry.

## Limitations

- Cell chemistries and interfacial evolution are complex; long-cycle statistics and full gas-phase cathode chemistry are broader than any single interfacial study.

## Relevance to group

**Adri C. T. van Duin** is a co-author; the work couples **electrolyte/SEI chemistry** with **QM** reasoning familiar to reactive force-field development contexts.

## Citations and evidence anchors

- Abstract and experimental sections: EIS/XPS/QM claims (J. Phys. Chem. C; DOI above).

## Reader notes (navigation)

- Galley duplicate PDF: [[2013bryantsev-venue-research]].

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
