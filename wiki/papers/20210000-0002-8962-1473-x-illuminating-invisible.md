---
id: paper:20210000-0002-8962-1473-x-illuminating-invisible
type: paper
title: "Illuminating Invisible Grain Boundaries in Coalesced Single-Orientation WS2 Monolayer Films"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:methods-software
  - material:tmd
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:2d-materials
  - keyword:validation-experiment
  - keyword:lammps
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/acs.nanolett.1c01517"
year: 2021
authors:
  - "Danielle Reifsnyder Hickey"
  - "Nadire Nayir"
  - "Mikhail Chubarov"
  - "Tanushree H. Choudhury"
  - "Saiphaneendra Bachu"
  - "Leixin Miao"
  - "Yuanxi Wang"
  - "Chenhao Qian"
  - "Vincent H. Crespi"
  - "Joan M. Redwing"
  - "Adri C. T. van Duin"
  - "Nasim Alem"
venue: "Nano Lett."
pdf_sha256: "316abc7ddf0cf3ea4cfcb3e5048210f168bfe5862f13d12dd36a4c22cd3a020e"
pdf_path: "papers/Hickey_NanoLetters_WS2_GBs_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20210000-0002-8962-1473-x-illuminating-invisible -->

**MOCVD** **2H-WS₂** on **c-plane sapphire** shows **near-single-orientation** **SAED/BF-TEM**, yet **dark-field TEM** reveals **faceted defect arrays**; **ADF-STEM** identifies **translational grain boundaries**. **ReaxFF MD** at **300 K** relaxes **type A/B** mismatch models consistent with **experiment**; facet statistics link **nm-scale** motifs to **μm-scale** morphology.

## Summary

**Electron microscopy** (**BF/DF-TEM**, **SAED**, **ADF-STEM**) characterizes **wafer-scale** **monolayer WS₂** transferred to **TEM grids**. Apparent **single-crystal** diffraction hides **translational GBs** visible in **DF-TEM**. Atomic models distinguish **type A** (single **vacancy-line**-like mismatch with compressed planes yet **hexagonal** **3|W** metal rows) versus **type B** (**sub-unit-cell** offset yielding **rectangular** **4|W** motifs). **ReaxFF MD** equilibrates these **GB** structures at **300 K**, reproducing **out-of-plane tilt** upon **freestanding** relaxation. **>1300 facet** traces support a picture of **microstructure** built from **nanoscale** units spanning **Å-to-μm** scales. The study addresses **optoelectronic** **yield**: **large-area** **monolayers** can still harbor **hidden** **GBs** that **scatter** **carriers** and **lower** **mobility**, so **diffraction**-only **characterization** is insufficient for **quality** metrics.

## Methods

**1 — Experiments and microscopy.** MOCVD **2H-WS₂** on 2 in. c-plane **Al₂O₃**; transfer to **TEM** grids (Quantifoil). **BF**/**DF**-TEM, **SAED** (including **±15°** tilt series), and **ADF-STEM** on translational **grain** **boundaries**; **>1300** **facet** traces connect **local** **STEM** motifs to **mesoscale** **texture** on wafers.

**2 — MD application.** ReaxFF **LAMMPS** **MD** (potential from [[20210000-0002-3621-2481-x-reaxff-force]], same DOI family) **NVT** equilibration at 300 K of **type** **A** and **B** **GB** **supercells** (including **freestanding** relaxations with in-plane **PBC** as in the paper). Sub-1 **fs** **timestep**; **Nose–Hoover** (or **Langevin**) **thermostat**; **ps**-scale equilibration runs. **NPT** / **barostat**—**N/A** for the static **tilt**-recovery tests if the article holds cell vectors fixed. **External** **electric** **field**; **rare**-**event** **(umbrella)**—**N/A** in the described protocol.

**3 — Force-field training on this page.** **N/A**—the **JPCC** study defines the **WS₂**+**sapphire** **ReaxFF**; this *Nano Lett.* work **applies** it to **GB** **models**.

**4 — Galley.** The registered **pdf_path** is a **galley**; use the **VOR** for final values.

## Findings

**Outcomes and mechanisms (experiment + MD).** Wafer-scale **MOCVD** **WS₂** can show **SAED** consistent with a **single** **orientation** while **DF-TEM** still reveals **translational** **grain** **boundaries** hidden to diffraction-averaging views. **ADF-STEM** distinguishes **type** **A** and **B** **mismatches** (e.g. **(3|W) hex**-row vs **(4|W) rect**-row motifs in the paper’s language). **ReaxFF** **NVT** equilibration at 300 K relaxes these **GB** **supercells**, including **out-of-plane** **tilt** upon **freestanding**-like release, in **qualitative** structural agreement with **STEM** (not **electronic** structure). **Comparisons** pair **imaging** with **ReaxFF**-relaxed **models**; **>1300** **facet** traces link **local** **STEM** **motifs** to **mesoscale** **texture** on wafers.

**Sensitivity and limitations.** The study emphasizes that **apparent** **single-crystal** **diffraction** is an insufficient **quality** **metric** for **optoelectronic** **yield** if **GBs** that **scatter** **carriers** are present. **ReaxFF** addresses **mechanics** and **morphology**, not **band** **structure**. **Corpus** note: the local **pdf_path** is a **galley**; verify **values** and **locators** on the **version of record** PDF. **Strain** from **transfer** and **substrate**-induced **defects** may add **mechanisms** beyond the two **translational** **classes** highlighted; **kinetic** pathways during **CVD** may not match **static** after-the-fact **relaxations**.

## Limitations

**Galley** PDF. **ReaxFF** does not predict **electronic** **GB** states. **Transfer** **wrinkles** and **substrate** **strain** during **CVD** may introduce **defect** **types** beyond the **two** **translational** classes emphasized in the main text. **Growth** **kinetics** on **sapphire** may favor **metastable** **GB** **arrays** that differ from **equilibrium** **structures** after **long** **anneals**.

## Relevance to group

Joint **STEM + ReaxFF** paper linking **synthesis** conditions to **defect** **arrays** in **TMD** **films**.

## Citations and evidence anchors

- DOI: [10.1021/acs.nanolett.1c01517](https://doi.org/10.1021/acs.nanolett.1c01517)

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Pair with **`paper:20210000-0002-3621-2481-x-reaxff-force`** for the **WS₂ ReaxFF** definition.
- `paper_keywords` includes **`keyword:galley-or-proof-pdf`**.
- After **VOR** **PDF** ingest, refresh **locators** and **figure** references that may shift vs the **galley** text.
