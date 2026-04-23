---
id: paper:2021rajadpour-advanced-mat-tunable-group
type: paper
title: "Tunable 2D Group-III Metal Alloys"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:alloys-metallurgy
  - method:dft-static
  - material:metal-surface
  - task:application
paper_keywords:
  - keyword:2d-materials
  - keyword:metallic-systems
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1002/adma.202104265"
year: 2021
authors:
  - "Siavash Rajabpour"
  - "Alexander Vera"
  - "Wen He"
  - "Benjamin N. Katz"
  - "Roland J. Koch"
  - "Margaux Lassaunière"
  - "Xuegang Chen"
  - "Cequn Li"
  - "Katharina Nisi"
  - "Hesham El-Sherif"
  - "Maxwell T. Wetherington"
  - "Chengye Dong"
  - "Aaron Bostwick"
  - "Chris Jozwiak"
  - "Adri C. T. van Duin"
  - "Nabil Bassim"
  - "Jun Zhu"
  - "Gwo-Ching Wang"
  - "Ursula Wurstbauer"
  - "Eli Rotenberg"
  - "Vincent Crespi"
  - "Su Ying Quek"
  - "Joshua A. Robinson"
venue: "Adv. Mater. 2021, 2104265"
pdf_sha256: "0a57c52aba95e2f667f864c6a0b170e744cc394772e54b3485c61683c021e309"
pdf_path: "papers/Rajadpour_Tunable2DGroupIIIalloys_AdvancedMaterials_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021rajadpour-advanced-mat-tunable-group -->

!!! abstract "Scope"
    **Confinement heteroepitaxy (CHet)** synthesis of air-stable **In\(_x\)Ga\(_{1-x}\)** intercalated under epitaxial graphene on SiC, with **XPS/AES/STEM/ARHEED/EELS** and **DFT**, tuning optical, electronic, and superconducting response with composition.

## Summary

The article reports synthesis and characterization of two-dimensional Group-III metal alloys In\(_x\)Ga\(_{1-x}\) confined at the epitaxial graphene/SiC interface using confinement heteroepitaxy. Precursor composition tunes the alloy fraction across nearly the full indium mole-fraction range with near-linear mapping observed by X-ray photoelectron spectroscopy. Auger mapping shows lateral uniformity without obvious segregation for representative compositions. Cross-sectional STEM, azimuthal RHEED, and EELS support epitaxial, confined metal layers between graphene and SiC. First-principles DFT predicts randomly mixed bilayer-like alloy configurations consistent with STEM, and experiments track how optical response, band structure, superconductivity, and charge transfer into graphene vary systematically with indium content.

The work situates confined III–V-like alloys as a platform where wafer-scale 2D metals can be stabilized under graphene, avoiding ambient degradation that limits free-standing ultrathin metals.

## Methods

**Synthesis and characterization (CHet).** **In\(_x\)Ga\(_{1-x}\)** is intercalated under **epitaxial graphene** on **SiC** by confinement heteroepitaxy; **In**/**Ga** precursor **fluxes** tune composition over nearly the full range. **XPS** links precursor **stoichiometry** to film **composition**; **AES** mapping checks **lateral** uniformity. **STEM**, **ARHEED**, and **EELS** establish epitaxial metal confined between **graphene** and **SiC**. **Optical** response, **band** signatures, **superconductivity**, and **charge** **transfer** into **graphene** are measured versus **indium** fraction (details in *Adv. Mater.* and **SI**).

**Static QM / DFT (no production MD).** First-principles **density functional theory** is used to model **In\(_x\)Ga\(_{1-x}\)** as **randomly mixed**, **bilayer**-like **alloys** and to connect **structure** to **electronic** trends seen in **STEM** and spectroscopy. The **exchange–correlation** **functional**, **plane-wave** / **PAW** (or equivalent) **basis** / **pseudopotential** choices, **k-point** / **k-mesh** **sampling** for **periodic** **geometry** **relaxation**, and whether **DFT-D3**-style **dispersion** (or a **vdW**-aware **meta-GGA**) is included are given in the computational **Methods** of the **PDF** (this short extract does not copy every tag). **Structures** are **relaxed** to obtain **total energy** and **electronic** **property** sets (**band gap**-related **band** structure, **DOS**, **work-function**-related **charge** trends) **compared** to **experiment**. **N/A —** **NEB** or **transition-state** **pathways** are not the focus unless the full paper adds them; **N/A —** ReaxFF or classical **molecular dynamics** in this work.

**MD / force fields.** **N/A —** not a classical or ReaxFF **molecular dynamics** study; coupling is **experiment** + **DFT**.
## Findings

- Large-area In\(_x\)Ga\(_{1-x}\) alloys form under graphene/SiC confinement with composition controlled by precursor stoichiometry and near-linear precursor-to-film composition relation in the examined range.
- Structural probes indicate epitaxial, intercalated metals without strong lateral phase separation for the highlighted samples.
- Optical, electronic, superconducting, and graphene charge-transfer signatures shift in a correlated way with indium fraction, enabling compositional tuning of 2D metal–graphene hybrid response.

The authors argue that this tunability opens a design space for hybrid photonic and electronic devices where graphene’s Dirac physics is modulated by an intercalated alloy whose work function and superconducting \(T_c\) can be steered continuously.

**Comparisons and trends.** **DFT**-predicted disordered **bilayer**-like **alloys** are **compared** to **STEM**; **optical** and **superconducting** response **correlate** with **indium** **concentration** in ways the authors map across **compositions**. **Limitations (corpus):** full DFT settings and any quantitative **band**-matching should be taken from the **version-of-record** **PDF**/**SI**, not this summary alone.

## Limitations

The study focuses on the specific CHet platform and characterization window; broader substrate or coverage regimes may behave differently.

## Relevance to group

Collaborative experimental/theory work with van Duin-group participation on confined 2D alloy electronics.

## Citations and evidence anchors

- DOI: [10.1002/adma.202104265](https://doi.org/10.1002/adma.202104265)

## Related topics

- Interlink 2D alloy / graphene theme hubs in `wiki/concepts/` when available.
