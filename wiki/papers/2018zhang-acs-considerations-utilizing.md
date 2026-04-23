---
id: paper:2018zhang-acs-considerations-utilizing
type: paper
title: "Considerations for Utilizing Sodium Chloride in Epitaxial Molybdenum Disulfide"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:tmd
  - task:application
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:2d-materials
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: ""
year: 2018
authors:
  - "Kehao Zhang; Brian M. Bersch; Fu Zhang; Natalie C. Briggs; Shruti Subramanian; Ke Xu; Mikhail Chubarov; Ke Wang; Jordan O. Lerach; Joan M. Redwing; Susan K. Fullerton-Shirey; Mauricio Terrones; Joshua A. Robinson"
venue: "ACS Appl. Mater. Interfaces 2018.10:40831-40837"
pdf_sha256: "1c22dd1a155cb7d258c0986b17e97787409764eab0a1aa2a60809c416dfcd00f"
pdf_path: "papers/Others/MoS2_NaCl_ACS_AMI_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018zhang-acs-considerations-utilizing -->

## Summary

This **experimental materials** study compares **alkali-free epitaxial monolayer MoS₂ on sapphire** with **NaCl-assisted metal–organic chemical vapor deposition (MOCVD)** growth. While **NaCl** can **greatly enlarge domains**, the authors show it can also introduce **spatial heterogeneity** in **optical and electronic** response, **nanoscale MoS₂ particulates**, **loss of epitaxy**, and **>1% tensile strain** that **suppresses photoluminescence** and **degrades transistors** relative to alkali-free growth under matched conditions.

Alkali promoters are widely used in TMD growth recipes; this paper documents that domain-size gains can coexist with defect populations that hurt optoelectronic uniformity.

## Methods

- **Growth:** **MOCVD** of **monolayer MoS₂** on **sapphire**, comparing **alkali-free** runs to **NaCl-assisted** growth (abstract).
- **Benchmarking:** Side-by-side comparison under the **same growth conditions** where the abstract emphasizes fair contrast between routes.
- **Characterization (as claimed in abstract):** Metrics tied to **domain size**, **strain**, **photoluminescence (PL)**, **field-effect transistor** performance, and **microscopy**-level evidence for **nanoscale MoS₂ particle** density (**4 ± 0.7 μm⁻²** scale in abstract) and **interface/epitaxy** behavior.

The matched-conditions design isolates the role of NaCl rather than confounding changes in temperature or precursor flow.

## Findings

- **NaCl** increases **monolayer MoS₂ domain size** dramatically (abstract: **~20×** vs alkali-free under their conditions).
- **Trade-offs:** NaCl coexists with **strong optical/electronic heterogeneity** across large films, **variable growth rates**, **epitaxy loss**, and elevated **nanoscale MoS₂ particle** counts on the surface (abstract).
- **Strain and optoelectronics:** NaCl-assisted films carry **>1% tensile strain** in domains; **PL drops ~20×** versus alkali-free counterparts, and **transistor metrics worsen** accordingly (abstract).

The takeaway for process engineers is to treat NaCl as a two-edged modifier: it can coarsen morphology while introducing residual particulates and strain that undermine device metrics.

ACS Applied Materials & Interfaces includes growth recipes, statistical distributions of domain sizes, and supplementary microscopy establishing particulate counts cited in the abstract.

Confirm the DOI from the publisher landing page if your toolchain requires a resolver link in addition to volume and page span metadata.

## Limitations

The note is **not a ReaxFF/atomistic simulation paper**—claims are from **growth and device/optical characterization**. Full protocol details (precursor flows, temperatures, times) should be read in the article and **SI**; **DOI** was not in normalized metadata—confirm from the publisher landing page if needed.

## Relevance to group

**2DCC / Penn State** growth science for **TMD electronics**—complements atomistic **TMD** work elsewhere in the corpus even though this paper is **experimental**.

## Citations and evidence anchors

- Journal locator in frontmatter (`ACS Appl. Mater. Interfaces 2018, 10, 40831–40837`); confirm **DOI** on the publisher page if needed for linking.

## Related topics

- [[graphene-nanocarbon]]
