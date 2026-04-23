---
id: paper:2018shin-venue-rsc-cp
type: paper
title: Development of a ReaxFF reactive force field for lithium ion conducting solid
  electrolyte Li1+xAlxTi2−x(PO4)3 (LATP)
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:batteries-electrochemistry
- domain:reaxff-lineage
- material:ceramic-electrolyte
- method:reaxff
- task:parameterization
- task:application
- scale:atomistic
candidate_tags: []
source_refs: []
doi: 10.1039/C8CP03586E
year: 2018
authors:
- Yun Kyung Shin
- Mert Y. Sengul
- A. S. M. Jonayat
- Wonho Lee
- Enrique D. Gomez
- Clive A. Randall
- Adri C. T. van Duin
venue: Phys. Chem. Chem. Phys.
pdf_sha256: 2488af5d342f16b0454b5963f66e3b234357643ae98b9a61d280d53371f5c552
pdf_path: papers/Shin_LATP_PCCP_2018_proof.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018shin-venue-rsc-cp -->

## Summary

**NASICON-type LATP** (**Li\(_{1+x}\)Al\(_x\)Ti\(_{2-x}\)(PO\(_4\))\(_3\)**) is a **Li\(^+\)**-conducting **oxide electrolyte** of interest for **all-solid-state batteries** because it combines reasonable **room-temperature conductivity** with processability in **composite** electrodes. Modeling **Li\(^+\)** transport and **local framework** response in defective, polycrystalline environments benefits from potentials that allow **bond rearrangement** at **interfaces** and **grain boundaries**, motivating **ReaxFF** beyond fixed-bond harmonic models. This **PCCP** article develops a **ReaxFF** description for **Li–P–O–Ti–Al** chemistry, validates it against **QM** and **crystallographic** references in the training sets described, and applies **MD** to analyze **composition-dependent** **Li** migration and **local structure** across **Al** substitution (**x**) space. **Adri C. T. van Duin** is a corresponding author together with the **Shin**-led parameterization effort. The corpus PDF is an **RSC proof** manuscript (**C8CP03586E**).

## Methods

This corpus entry records the **RSC proof** PDF (`papers/Shin_LATP_PCCP_2018_proof.pdf`) for the same **PCCP** study summarized on **`[[2018shin-physical-che-development-reaxff]]`**. **Methods** prose below mirrors that **version-of-record** page at a high level so checklist coverage remains self-consistent; operators should still copy **tables**, **timesteps**, and **ensemble** keywords from the final **issue PDF** when reproducing work.

**Force-field training (ReaxFF for Li–Al–Ti–P–O).** **Parent potential / elements:** **ReaxFF** for **Li–P–O–Ti–Al** chemistry built by extending **oxide**/**phosphate** **parameter** families to **NASICON-type** **LATP**. **QM reference:** **DFT** **training** data include **equations of state**, **formation enthalpies** for reference crystals (**Li\(_x\)TiO\(_2\)**, **Al\(_2\)TiO\(_5\)**, **LiAlO\(_2\)**, **AlPO\(_4\)**, **Li\(_3\)PO\(_4\)**, **LiTi\(_2\)(PO\(_4\))\(_3\)**), and **Li** **diffusion** **barriers** in **TiO\(_2\)** and **LTP** along **vacancy** and **interstitial** pathways. **Training set / targets:** bulk crystals, **migration** paths, and selected **interface**-relevant motifs as listed in the article. **Optimization:** **ReaxFF** **parameter** **optimization** against the **DFT** database using the standard **least-squares**/**ParReaxFF**-style workflow described in *PCCP*. **Reference validation:** compares **lattice** trends and **conductivity** orders of magnitude to **experiment** for selected compositions.

**MD application + hybrid MC/MD.** **Engine:** **molecular dynamics** with the fitted **ReaxFF** plus **hybrid Monte Carlo / MD** moves for **disordered** **Li**/**Al** arrangements (**reactive MD**). **System:** **periodic** **supercells** of **LATP** across **\(x\)** (**atom** counts in article). **PBC:** **three-dimensional periodic** cells. **Ensemble:** **NVT**-like **canonical** **MD** for **conductivity** evaluation, consistent with the published workflow on **`[[2018shin-physical-che-development-reaxff]]`**. **Temperature:** **300–1100 K** **conductivity** sweeps as reported. **Duration:** **production** segments are **nanosecond**-scale in the parent article’s protocol summary (**~1 ns** order-of-magnitude segments should be confirmed in the **issue PDF**). **Timestep / thermostat / barostat:** **N/A — proof PDF pagination** may differ from the final **Methods**; copy from **`[[2018shin-physical-che-development-reaxff]]`** and the **issue PDF**. **Pressure:** **N/A — not emphasized** in this summary. **Electric field:** **N/A — not used**. **Enhanced sampling:** **hybrid MC/MD**; **N/A — umbrella / metadynamics** not indicated in the indexed excerpt.
## Findings

The manuscript reports that **ReaxFF** reproduces key **structural** benchmarks and captures **transport trends** for **LATP** compositions explored in the study, including mechanistic insight into how **Li** motion couples to **local phosphate** framework distortions. **Comparisons:** **ionic conductivity** at **300 K** is compared between **LTP**, **LATP** at **\(x=0.2\)**, and a **hybrid MC/MD**-sampled **\(x=0.5\)** arrangement, with explicit **comparison** to an in-house **experimental** value and **literature** ranges for mid-**\(x\)** compositions (see **`[[2018shin-physical-che-development-reaxff]]`** for the tabulated numbers used in this wiki). **Sensitivity:** **conductivity** depends strongly on **composition**/**disorder** realization, motivating careful sampling. **Limitations / outlook:** bulk fits do not automatically validate **electrode–electrolyte** **interfaces** under **operating** electrochemical conditions. **Corpus honesty:** this slug is a **proof** PDF; confirm final wording and **tables** against the **version-of-record** **PCCP** issue PDF.

## Limitations

Proof PDF may differ cosmetically from the **version of record**; quantitative barriers and conductivities should be taken from the final **PCCP** article.

## Relevance to group

Flagship **solid-electrolyte ReaxFF** reference from the **group’s battery materials** line.

## Citations and evidence anchors

- **DOI:** [10.1039/C8CP03586E](https://doi.org/10.1039/C8CP03586E) (manuscript id **C8CP03586E** on the proof header).

## Related topics

- [[reaxff-family]]
