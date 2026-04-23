---
id: paper:2022liu-nat-uniform-nucleation
type: paper
title: "Uniform nucleation and epitaxy of bilayer molybdenum disulfide on sapphire"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - task:experiment-integrated
  - material:tmd
  - scale:multiscale
candidate_tags: []
paper_keywords:
  - keyword:2d-materials
  - keyword:validation-experiment
source_refs: []
doi: "10.1038/s41586-022-04523-5"
year: 2022
authors:
  - "Lei Liu"
  - "Taotao Li"
  - "Liang Ma"
  - "Weisheng Li"
  - "Si Gao"
  - "Wenjie Sun"
  - "Ruikang Dong"
  - "Xilu Zou"
  - "Dongxu Fan"
  - "Liangwei Shao"
  - "Chenyi Gu"
  - "Ningxuan Dai"
  - "Zhihao Yu"
  - "Xiaoqing Chen"
  - "Xuecou Tu"
  - "Yuefeng Nie"
  - "Peng Wang"
  - "Jinlan Wang"
  - "Yi Shi"
  - "Xinran Wang"
venue: "Nature"
pdf_sha256: "a7250ce24510e94ff6318eab3d1e9789d66db05d011f1295b2aee012cf245d04"
pdf_path: "papers/Others/Nature_MoS2_sapphire_Liu_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2022liu-nat-uniform-nucleation -->

## Summary

This *Nature* article addresses a practical bottleneck for **two-dimensional transition-metal dichalcogenide (TMD)** transistors: although **monolayer** TMD growth has matured, **uniform epitaxial bilayers** with wafer-scale homogeneity have remained elusive, even though **bilayer** channels are argued to be an attractive compromise between **electrostatic control**, **density of states**, and **mobility** for deeply scaled devices. The authors report **chemical vapor deposition (CVD)** of **bilayer molybdenum disulfide (MoS₂)** on **c-plane sapphire** where engineering **atomic terrace heights** steers an **edge-nucleation** pathway and enables **>99% uniform bilayer nucleation** with **coalescence** into **centimeter-scale** continuous films. Fabricated **field-effect transistors (FETs)** on bilayer channels show **field-effect mobility** up to **122.6 cm² V⁻¹ s⁻¹** with improved **device-to-device variation** relative to monolayer-film controls under the reported processing. **Short-channel** FETs further report **on-state current** **1.27 mA μm⁻¹**, which the authors compare against an industry **2028** high-performance FET roadmap target cited in the abstract.

## Methods

The growth strategy couples **CVD** with **substrate engineering** on **c-sapphire** to manipulate **terrace structure** and favor bilayer nucleation and orientation over the fragmented bilayer flakes typical of prior attempts. The paper’s introduction contrasts **layer-by-layer** epitaxy routes that may be too slow for manufacturing with the targeted **CVD** throughput. Thermodynamic arguments in the article use **density functional theory (DFT)** estimates of **edge energies** and **surface energies** to rationalize why bilayer domain evolution is nontrivial on vdW-like substrates. Device fabrication spans multiple **channel lengths** to probe **mobility** statistics and **short-channel** **drive current**; detailed fabrication stacks, dielectric integration, and metrology appear in the full text and Extended Data.

## Findings

Experimentally, the work demonstrates **large-area** bilayer **MoS₂** films with high bilayer yield and **FET** metrics that improve on monolayer baselines in the reported cohort, supporting the claim that bilayer epitaxy can combine uniformity and competitive transport for beyond-silicon exploratory technology. The **short-channel** current benchmark is presented as exceeding a cited roadmap figure, framing bilayer TMDs as candidates for high-drive, scaled transistors if contact and integration challenges continue to improve. The study is **experimental** and **DFT-informed** rather than a reactive MD paper; it complements atomistic simulation literature on MoS₂ in this corpus by establishing a growth/device benchmark.

## Limitations

Wafer-edge defect maps, transfer-integration yield, and long-term reliability are outside the scope of the abstract-level summary and require the full article. This entry is not a **ReaxFF** study; mechanistic atomistic claims should not be imported from unrelated force fields.

## Relevance to group

Experimental **2D TMD** **epitaxy** benchmark; complements **computational** **MoS₂** **ReaxFF** papers (e.g., Ponomarev et al.) but is **not** an atomistic simulation study.

## Citations and evidence anchors

- DOI: [10.1038/s41586-022-04523-5](https://doi.org/10.1038/s41586-022-04523-5)

## Related topics

- [[graphene-nanocarbon]]
