---
id: paper:2022lingmei-ni-j-am-chem-so-identification-catalytically
type: paper
title: "Identification of the Catalytically Dominant Iron Environment in Iron- and Nitrogen-Doped Carbon Catalysts for the Oxygen Reduction Reaction"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - method:dft-static
  - task:application
  - material:graphene-carbon-nano
  - scale:atomistic
paper_keywords:
  - keyword:dft-static
  - keyword:catalysis-surface
  - keyword:graphene-carbon
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/jacs.2c04865"
year: 2022
authors:
  - "Lingmei Ni"
  - "Charlotte Gallenkamp"
  - "Stephan Wagner"
  - "Eckhard Bill"
  - "Vera Krewald"
  - "Ulrike I. Kramm"
venue: "J. Am. Chem. Soc."
pdf_sha256: "0e7e647dbf601156b8bd92f49ba737efbfd404b68f4218f7cd853b706a9d257b"
pdf_path: "papers/Others/Ni_Krewald_etal_Iron_carbon_catalyst_JACS_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022lingmei-ni-j-am-chem-so-identification-catalytically -->

## Summary

**Fe–N–C (FeNC)** catalysts for the **oxygen reduction reaction (ORR)** are heterogeneous at the atomic scale: multiple **Fe** coordination environments can coexist after pyrolysis, frustrating assignment of the **dominant active site**. This **Journal of the American Chemical Society** article combines **operando ⁵⁷Fe Mössbauer spectroscopy** with **quantum-chemical** cluster and periodic models to correlate **spectroscopic doublets** with candidate **Fe–N\(_x\)** motifs on **graphene-like** supports. A newly resolved **operando signature (D4)** appears concurrently with loss of other doublets (**D2**, **D3a**, **D3b**), implying **interconversion** of Fe sites during catalysis. The authors argue that **pyrrolic N-coordinated FeN\(_4\)C\(_{12}\)** motifs provide a **spectroscopically and thermodynamically consistent** account of the **full ORR cycle**, preferred over **pyridinic** alternatives in their modeling framework, and they propose a **new intermediate** along the ORR pathway on FeNC.

## Methods

Experiments apply **⁵⁷Fe Mössbauer** under **operando** electrochemical conditions to track Fe environments as the cell is driven through ORR-relevant potentials. Theory employs **DFT-level** cluster and periodic models (details in the article) to compute **hyperfine parameters** and reaction energetics for competing **Fe–N\(_x\)** sites, comparing to measured isomer shifts and quadrupole splittings. The joint workflow aims to match not only static spectra but also **potential-dependent** changes tied to catalytic turnover. For MAS retrieval, note that this is a **spectroscopy-first** identification strategy: the computational models are tightly coupled to **Mössbauer** observables, which reduces ambiguity compared to purely catalytic turnover metrics that integrate over many site types.

**Static QM (DFT + embedded-cluster / periodic models as in *JACS*):** **Functional** and **dispersion** **(e.g.** **PBE** + **D3** or **hybrid** **tests**—read **PDF**); **plane-wave** or **localized** **basis** **sets** for **periodic** vs **cluster** **tasks**; **Brillouin**-zone **k**-**mesh** / **k**-**point** **sampling** (e.g. **Γ**-centered **grids**) for **graphene**-like **supports**; **geometry** **optimizations** and **ORR** **path** **energetics**; **properties:** **hyperfine** **parameters** (to match **Mössbauer**), **reaction** **energies**, **barrier**-like **metrics** as **tabulated**. **N/A** **—** full **DFT** **settings** **not** **reproduced** **line**-**by**-**line** here.

## Findings

**D4** emerges while other Fe signatures decay, supporting a direct link between **site interconversion** and **ORR** conditions. The modeling section claims **pyrrolic FeN\(_4\)C\(_{12}\)** frameworks best reconcile spectra, thermochemistry, and cycle constraints compared to **pyridinic** FeN\(_4\) alternatives in their dataset. The paper further claims identification of a previously unresolved **ORR intermediate** associated with FeNC systems. These conclusions depend on model approximations for disordered, pyrolyzed materials. **Comparisons: versus** **experimental** **Mössbauer** **doublets**; **theory** **identifies** **D4** **interconversion**. **Sensitivity:** **applied** **potential** in **operando** **cell**; **disorder** of **pyrolyzed** **FeNC** limits **site** **models**. **Limitations** (authored) on **real** **catalyst** **heterogeneity**—**see** **JACS** **Discussion**. **Corpus / PDF:** read **isomer** **shifts**/**QS** and **energetics** from the **version-of-record**; **this** page is a **scoping** **summary** only. For retrieval, pair this paper with user questions that mention **Mössbauer doublets** and **Fe–N–C site assignment**, because the experimental discriminator is spectroscopic rather than turnover-only.


## Limitations

Pyrolyzed **FeNC** heterogeneity means single-site models are approximate; operando cell gradients and transport may not be fully captured.

## Reader notes (MAS / retrieval)

Prioritize when queries mention **Mössbauer**/**Fe–N–C**/**ORR** site assignment jointly.

This page is **DFT + spectroscopy**, not **ReaxFF** reactive MD.

See also operando electrochemistry discussions in the full text.

## Relevance to group

**Fe–N–C graphene** electrocatalyst characterization—computationally adjacent to carbon **electrode** topics though **not** a **ReaxFF** study.

## Citations and evidence anchors

- DOI: [10.1021/jacs.2c04865](https://doi.org/10.1021/jacs.2c04865)

## Related topics

- [[graphene-nanocarbon]]
