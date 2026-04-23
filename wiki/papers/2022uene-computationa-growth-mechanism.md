---
id: paper:2022uene-computationa-growth-mechanism
type: paper
title: "Growth mechanism study of boron nitride atomic layer deposition by experiment and density functional theory"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:dft-static
  - material:hexagonal-boron-nitride
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:oxide-surface
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2022.111919"
year: 2022
authors:
  - "Naoya Uene"
  - "Takuya Mabuchi"
  - "Masaru Zaitsu"
  - "Yong Jin"
  - "Shigeo Yasuhara"
  - "Takashi Tokumasu"
venue: "Computational Materials Science"
pdf_sha256: "3976c4aad26f7d7460be4263ff8af83bd11583e224d3e1862a4917ffaa798e30"
pdf_path: "papers/Others/Uene_BCl3_silica_DFT_CompMatSci_2023.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2022uene-computationa-growth-mechanism -->

!!! abstract "Scope"

ALD of BN from BCl\(_3\) or TDMAB with NH\(_3\) on Si(100): experiments map growth per cycle vs temperature; DFT identifies rate-limiting surface reactions setting the lower ALD window.

## Summary

Atomic layer deposition of boron nitride must stay within a finite temperature window. Experiments compare BCl\(_3\)+NH\(_3\) vs tris-dimethylaminoborane (TDMAB)+NH\(_3\) on Si(100), measuring how growth per cycle (GPC) responds between roughly **700–900 °C**. Static DFT then evaluates four representative elementary steps on OH-, Cl-, H-, and BN-terminated surfaces to locate the highest activation barrier controlling the lower temperature bound. The **study** is **explicitly** **ALD-focused**: **precursor** **choice** changes **surface** **termination** **sequences** between **cycles**, so **GPC** **curves** are interpreted together with **stepwise** **ligand** **exchange** **pictures** rather than as a single **effective** **activation** **energy** for **all** **boron** **sources**.

## Methods

### Experiments (ALD window and GPC)

- **Substrate:** **Si(100)**.
- **Precursor pairs:** **BCl\(_3\) + NH\(_3\)** versus **TDMAB + NH\(_3\)** (tris(dimethylamino)borane).
- **Observables:** **Growth per cycle (GPC)** vs **temperature** in an approximately **700–900 °C** window (as described in the article), comparing temperature sensitivity between chemistries.

### Static quantum chemistry (C)

- **Goal:** Identify representative **elementary steps** on **F-terminated** / **OH-terminated** / **H-terminated** / **BN-terminated** **Si(100)** motifs relevant to **BN** ALD.
- **Reactions labeled (a)–(d) in the paper:** (a) **BCl\(_3\)** on **OH-terminated** Si(100); (b) **NH\(_3\)** on **Cl-terminated** Si(100); (c) **BCl\(_3\)** on **H-terminated BN** on Si(100); (d) **NH\(_3\)** on **Cl-terminated BN** surfaces.
- **Electronic structure readout (full DFT):** The **PBE**-family **DFT** setup, **convergence** tolerances, **k-point** / **k-mesh** sampling, **slab** **geometries** for the **(a)–(d)** **reaction** **pathways** on **OH-**, **Cl-**, **H-**, and **BN-terminated** **Si(100)** motifs, and resulting **barrier** **energies** (**e.g. 30.0 kcal mol\(^{-1}\)** for step **(c)**) are reported in the primary *Comput. Mater. Sci.* text; **DFT-D** or other **vdW**/**dispersion** **corrections** and **PAW**/**plane-wave** / **basis** **cutoffs** are as stated there or **N/A** if the manuscript does not add a separate dispersion **correction** line in the indexed summary. **N/A** to **NEB** if the paper uses a different static **path** search; align with the published **method** name.

## Findings

### Experimental GPC trends

**TDMAB + NH\(_3\)** shows a **steep** increase in **GPC** with **temperature** in the studied window, whereas **BCl\(_3\) + NH\(_3\)** exhibits a **weaker** **temperature dependence** (qualitative comparison in the article).

### DFT barrier assignment

Static **DFT** assigns an **activation barrier** of **30.0 kcal mol\(^{-1}\)** to reaction **(c)** (**BCl\(_3\)** on **H-terminated BN**), interpreted as **rate-limiting** for the **lower** bound of the **ALD** **temperature window**. The corresponding **activation temperature** is about **789 °C**, falling **inside** the **experimental** **ALD** window reported by the authors.

### Mechanistic takeaway

**GPC** vs **T** behavior should be interpreted with the **specific** **boron** **precursor** and its **surface** **termination** sequence—not a single universal **BN** growth law across **BCl\(_3\)** vs **TDMAB** routes.

## Limitations

DFT models idealized surfaces; reactor-scale nonuniformities are not captured. The **Comp. Mater. Sci.** workflow separates **experimental** **GPC** **vs** **T** trends for **BCl\(_3\)+NH\(_3\)** and **TDMAB+NH\(_3\)** from **static** **barrier** assignments on **OH-**, **Cl-**, **H-**, and **BN-terminated** **Si(100)** motifs; retrieval should preserve that pairing so **ALD** **window** arguments are not quoted without the **DFT** **reaction** labels **(a)–(d)** used in the manuscript. **Surface** **hydroxyl**/**chloride** **coverages** inferred from **ideal** **slabs** may differ from **industrial** **reactor** **surfaces** where **contaminants** and **roughness** shift **effective** **barriers**, **stick** **probabilities**, and **local** **coverage**.

## Relevance to group

Peripheral DFT/ALD study in corpus (not ReaxFF).

## Reader notes (navigation)

- Not a [[reaxff-family]] paper—DFT + ALD experiment.
- Nitride **epitaxy** context: [[theme-2d-epitaxy-growth]], [[theme-oxides-silica-ceramics]]

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2022.111919](https://doi.org/10.1016/j.commatsci.2022.111919)

## Related topics

- [[theme-oxides-silica-ceramics]]
