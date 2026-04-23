---
id: paper:2011harikumar-nat-directed-long-range
type: paper
title: "Directed long-range molecular migration energized by surface reaction"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:catalysis-surface
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1038/nchem.1029"
year: 2011
authors:
  - "K. R. Harikumar"
  - "John C. Polanyi"
  - "Amir Zabet-Khosousi"
  - "Piotr Czekala"
  - "Haiping Lin"
  - "Werner A. Hofer"
venue: "Nature Chemistry 3, 400–405 (2011)"
pdf_sha256: "1fce3b75b9960fa597fdb34ab0ed003f209363d59f52d3432053b8d8523e3fea"
pdf_path: "papers/Others/Si_halogen_hydrocarbons_NCHEM-3-400-2011.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2011harikumar-nat-directed-long-range -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This article reports **scanning tunneling microscopy (STM)** evidence on **Si(100)** for **in-plane, directed, long-range migration** of physisorbed **ethylenic** products produced by surface reactions—distinct from short-range random hopping diffusion. **Thermal** reactions of **1,2-dihaloethanes** (F, Cl, Br) and **electron-induced** reactions of chemisorbed **ethylene, propene, and trans-2-butene** are studied. Migration distances up to on the order of **200 Å** are discussed for some channels, with thermal channels showing ethylene separated from halogen pairs by tens of ångströms on average. **Ab initio** calculations support a picture in which **asymmetric forces** on the two carbons of the ethylenic unit produce **torque** and favor **rolling/cartwheeling**-like motion over the rough surface, including crossing steps and defects without losing directionality.

## Methods


**Experiments (STM).** **Scanning tunneling microscopy** on **Si(100)-2×1** reports **six** channels: **three thermal** reactions of **1,2-dihaloethanes** (**XCH\(_2\)CH\(_2\)X**, **X = F, Cl, Br**) at **room temperature (~25 °C)**, and **three electron-induced** reactions of chemisorbed **ethylene**, **propene**, and **trans-2-butene**. The abstract contrasts **in-plane directed migration** up to **~200 Å** before a final attachment reaction with conventional short-range **~5 Å** hopping diffusion on smooth metals.

**3 — Static QM / DFT (VASP benchmarks cited in the excerpt).** **Program:** **VASP** is named for the quoted **heats of reaction**. **Functional:** **N/A —** specific **XC functional** not stated on the indexed pages. **Dispersion:** **N/A —** **dispersion correction** not stated in the excerpt. **Basis / PAW / cutoff:** **N/A —** not transcribed from `normalized/extracts/2011harikumar-nat-directed-long-range_p1-2.txt`. **k-sampling:** **N/A —** **k-mesh** not stated in the excerpt. **Structures / pathways:** **1,2-dihaloethane** reactions forming **two chemisorbed halogens** plus **chemisorbed ethylene** on **Si(100)-2×1** as discussed in Results. **Properties computed:** quoted **reaction energies** (**23.6**, **22.6**, **22.5 eV** for **DFE**, **DCE**, **DBE**, respectively, as printed) as **electronic-structure energy** benchmarks.

**1 — MD application.** **N/A —** this paper’s primary evidence is **STM** plus **DFT** support, not classical **production MD** protocols.

**2 — Force-field training.** **N/A —** not applicable.

## Findings

**In-plane directed migration** over **tens to ~200 Å** contrasts with the **~5 Å** short-range random hopping typical of diffusion on metals in the cited literature. For **dihaloethane** reactions, “hot” **ethylene** products can appear **separated** from partner **halogen pairs**—with **mean ethylene–halogen separations ~25–30 Å** across the three halides (distributions biased by halogen-pair clustering for some species), and separations up to about **80 Å** noted for selected **DBE** assignments. **Directionality** along the **C–C axis**, traversal of **steps** and **defects** without losing direction, and **end-to-end inversion** for **propene** / **trans-2-butene** under electron-induced conditions support **rolling/cartwheeling** over simple hopping. **Ab initio** results indicate **asymmetric forces** on the two carbons that generate **torque**, consistent with the proposed migration mechanism.

**Limitations (STM interpretation).** The paper notes that **assigning partner halogen pairs** to specific ethylene products can **bias** distance statistics and that **clustering** effects matter for some halides—**caveats** to keep when reading the separation histograms.

## Limitations

- Assignment of partner halogen pairs to specific ethylene products can bias distance statistics; the paper discusses clustering effects for some halides.
- The study is specific to **Si(100)** chemistry and STM-accessible conditions; direct transfer to other semiconductors or metals is not claimed.

## Relevance to group

Surface reaction dynamics and **ab initio** validation; **not** a ReaxFF/van Duin-group paper but relevant as **surface chemistry** context for silicon and hydrocarbon reactivity.

## Citations and evidence anchors

- DOI: [10.1038/nchem.1029](https://doi.org/10.1038/nchem.1029)
- Text-aligned pointer: `normalized/extracts/2011harikumar-nat-directed-long-range_p1-2.txt`

## Related topics

- [[theme-catalysis-surfaces]]
- Silicon surfaces and alkene/surface reactions (corpus cross-links as curated)
