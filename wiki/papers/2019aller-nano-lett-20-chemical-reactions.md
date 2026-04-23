---
id: paper:2019aller-nano-lett-20-chemical-reactions
type: paper
title: "Chemical Reactions Impede Thermal Transport Across Metal/β-Ga2O3 Interfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:oxides-ceramics
  - material:widegap-semiconductor
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:validation-experiment
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.9b03017"
year: 2019
authors:
  - "Henry T. Aller"
  - "Xiaoxiao Yu"
  - "Adam Wise"
  - "Robert S. Howell"
  - "Andrew J. Gellman"
  - "Alan J. H. McGaughey"
  - "Jonathan A. Malen"
venue: "Nano Lett."
pdf_sha256: "9e7ab86a0f5e2c87191b46595690edf454ac13eff0d49afd6188d52796c8f62a"
pdf_path: "papers/Others/2020_McGaughey_Cr2O3.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2019aller-nano-lett-20-chemical-reactions -->

## Summary

Thermal management of **wide-bandgap** **β-Ga\(_2\)O\(_3\)** electronics depends on **thermal boundary conductance (TBC)** across **metal/oxide** stacks, but interfaces are seldom atomically inert: **interfacial reactions** can form **new oxide phases** that alter **phonon transport** pathways. This **Nano Lett.** study uses **time-domain thermoreflectance** to measure **TBC** in **Au / adhesion metal / β-Ga\(_2\)O\(_3\)** stacks as a function of **adhesion metal thickness** for **Cr**, **Ti**, and **Ni** underlayers, interpreting trends with **TEM** evidence of reaction products such as **Cr\(_2\)O\(_3\)** formed by **oxygen transfer** from the **gallium oxide**. The core empirical result is **non-monotonic** **TBC** versus metal thickness: reaction-grown oxides can first **enhance** transport relative to a bare baseline, then **plateau** or **limit** transport as films **thicken** and **passivate** the interface.

## Methods

This is an **experimental thermal-transport** study of **metal / β-Ga\(_2\)O\(_3\)** stacks, not an atomistic simulation paper.

**Sample fabrication and metrology.** The authors investigate **Au / adhesion metal / β-Ga\(_2\)O\(_3\)** layered samples as a function of **Cr**, **Ti**, or **Ni** **contact thickness**, using **(010)** **β-Ga\(_2\)O\(_3\)** substrates and a **wedge-shaped** metal deposition geometry so that **thickness varies continuously** across a wafer (enabling **high-throughput** mapping rather than discrete coupons). **Energy-dispersive X-ray spectroscopy (EDX)** maps elemental thickness trends (reported thicknesses are derived assuming **bulk metal density** and do not distinguish **metal vs oxidized** metal in the signal). A **65–70 nm Au** cap is deposited **without breaking vacuum** after the adhesion layer.

**Thermal boundary conductance (TBC).** **Frequency-domain thermoreflectance (FDTR)** is used as a **noncontact** optical approach to extract **TBC** of the **Au/contact/β-Ga\(_2\)O\(_3\)** junction (including contributions from **internal interfaces** and the **metal layer** as defined in the article). The **Nano Lett.** abstract reports an **Au/β-Ga\(_2\)O\(_3\)** baseline **TBC** near **45 ± 7 MW m\(^{-2}\) K\(^{-1}\)**.

**Microscopy / chemistry evidence.** **Transmission electron microscopy (TEM)** supports **reaction-formed oxides** for at least the **Cr** case, including **Cr\(_2\)O\(_3\)** formation via **oxygen removal** from **β-Ga\(_2\)O\(_3\)** as discussed in the article.

**Atomistic MD / ReaxFF / DFT.** **N/A —** the publication’s core evidence is **thermoreflectance + microscopy** under controlled metallization; there is no central **reactive MD** or **DFT** production protocol to summarize here.

## Findings

For **Cr**, **TBC** reaches a **peak ~530 ± 40 MW m\(^{-2}\) K\(^{-1}\)** near **~2.5 nm** Cr thickness. For **Ti**, the peak is **~260 ± 25 MW m\(^{-2}\) K\(^{-1}\)** near **~5 nm** Ti. For **Ni**, **TBC** **saturates** near **~410 ± 35 MW m\(^{-2}\) K\(^{-1}\)** for thicknesses **>3 nm** without a pronounced peak in the same sense. Relative to the bare **Au/oxide** baseline, optimized stacks improve **TBC** by roughly **6–12×** in the comparisons quoted. The authors interpret **maxima** as arising when **thermodynamically favored** reaction products form beneficial transport pathways, while continued reaction and **passivation** eventually limit further gains—linking **chemistry** explicitly to **thermal resistance** engineering. For **wide-bandgap** device packaging, the takeaway is that **metal/oxide** **TBC** is not governed by **bulk** **κ** alone: a few **nanometers** of **interfacial oxide** can dominate **phonon** transmission, and that oxide may be **reaction-grown** rather than deposited intentionally. The **Cr**, **Ti**, and **Ni** comparisons therefore illustrate how **thermodynamic driving forces** for oxygen transfer from **β-Ga\(_2\)O\(_3\)** set distinct **TBC** curves. Heat-spreader design workflows should therefore treat **adhesion metal thickness** as a **process variable** with non-monotonic thermal consequences, not merely as an electrical contact convenience. Packaging engineers should read the **TBC** maxima as **chemistry-enabled** transport windows that can disappear if reaction layers become too thick or too disordered. Confirm thickness-dependent **TBC** values and microscopy in the **Nano Lett.** PDF.

## Limitations

This is an **experimental** transport study, not a **ReaxFF** simulation. Ensure the local **`pdf_path`** matches the **Nano Lett.** PDF for the DOI when auditing the corpus.

## Relevance to group

**Thermal management** context for **wide-gap oxide** electronics adjacent to **2D/wide-bandgap** materials work in the broader corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.nanolett.9b03017](https://doi.org/10.1021/acs.nanolett.9b03017)

## Related topics

- [[graphene-nanocarbon]]
