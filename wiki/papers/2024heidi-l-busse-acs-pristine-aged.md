---
id: paper:2024heidi-l-busse-acs-pristine-aged
type: paper
title: "Pristine and Aged Microplastics Can Nucleate Ice through Immersion Freezing"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - task:experiment-integrated
  - material:polymer-organic
  - domain:water-silica-geo
  - scale:atomistic
paper_keywords:
  - keyword:polymer
  - keyword:water-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsestair.4c00146"
year: 2024
authors:
  - "Heidi L. Busse, Devaka Dharmapriya Ariyasena, Jessica Orris, and Miriam Arak Freedman"
venue: "ACS EST Air"
pdf_sha256: "697f3efbff79158e38cf35847dd2a55fce9083e4731c8b578d2982d9e164e1e3"
pdf_path: "papers/Others/busse-et-al-2024-pristine-and-aged-microplastics-can-nucleate-ice-through-immersion-freezing.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2024heidi-l-busse-acs-pristine-aged -->

## Summary

Laboratory-prepared microplastics (LDPE, PP, PVC, PET) are tested as immersion freezing nuclei before and after simulated aging (UV, ozone, sulfuric acid, ammonium sulfate); ATR-FTIR tracks surface chemistry changes alongside ice nucleation activity.

## Methods

**Materials:** Commercial polymers (PP isotactic, LDPE, PVC, PET with glass fiber) were **cryo-milled** and sieved into size classes (**25-53, 53-75, 75-106, >106 micrometers**); a combined **<106 micrometer** fraction was used for aging and most freezing assays. **PET** was **density-separated in chloroform** (sonication **20 min**, settling **>=48 h**, repeated) to remove glass fibers. **Aging:** UV (broad metal-halide lamp, quartz lid; exposure converted to Harrisburg PA equivalent days), **ozone** (Poseidon 200, chamber exposure; ppm-h converted to equivalent days using **0.030 ppm** surface ozone), **pH 2 H2SO4** and matched **(NH4)2SO4** (**72 h**, room temperature, rinse). **Ice nucleation:** immersion freezing chamber (Alstadt-type protocol cited), **~0.1 wt%** LDPE/PP and **~1 wt%** PVC/PET in **UHPLC water**, **2.0 microL** droplets on **siliconized** slides, cooling **-3 C/min**, **K-type thermocouple**, **LabView** imaging **0.5 or 0.1 C** steps, **ImageJ** contrast, **MATLAB** frozen fraction **F(T)** from at least **100** droplets total; active site density **K(T)** with background water subtraction; **n_m(T)** normalized per mass. **ATR-FTIR** (Nicolet 6700 Smart iTX) on dry powders; **UV-vis** on THF solutions checked for chromophores (**300-800 nm**).

## Findings

All four polymers act as **immersion ice nuclei**. **Aging generally reduces** ice nucleation activity for **LDPE, PP, and PET** (median freezing temperatures shift colder or **n_m** drops depending on treatment), while **PVC often shows increased activity after aging**, attributed to **cleaning chemical defects** from stock material. **ATR-FTIR:** growth of **1650-1800 cm^-1** absorbance correlates with **decreased** ice activity in several cases; **loss** of an existing peak in that region correlates with **increased** activity. **Particle size** (**<106 micrometer** classes) shows **little systematic trend** of **n_m** with size for PVC, LDPE, and PP in the range studied, supporting use of the combined size class for aging comparisons. **Ammonium sulfate** on LDPE produces a **large shift to warmer** median freezing (**~-19.5 C** vs **~-23.7 C** pristine for 0.1 wt% LDPE in one comparison). The authors argue that, at plausible atmospheric loadings, MP could be a **non-negligible** INP source.

## Limitations

Despite beam blanking during heating, **in situ** microscopy still couples **temperature** with **finite electron dose**; **aging** protocols simplify atmospheric **multiphase** chemistry (acid, ozone, UV) relative to full environmental matrices. **FTIR** peak assignments for surface oxidation are **interpretive**; **INP** activity is measured on **laboratory** suspensions and droplets, so **atmospheric** relevance requires scaling arguments beyond this study’s scope.

## Relevance to group

Experimental **ice nucleation** on **polymers** and **aging** chemistry—useful cross-reference for **water–interface** and **material aging** themes; **not** a **ReaxFF** simulation paper.

## Citations and evidence anchors

- DOI: [10.1021/acsestair.4c00146](https://doi.org/10.1021/acsestair.4c00146)

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
