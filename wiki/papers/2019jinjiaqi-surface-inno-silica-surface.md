---
id: paper:2019jinjiaqi-surface-inno-silica-surface
type: paper
title: "Silica surface states and their wetting characteristics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - method:dft-static
  - task:application
  - material:silicate-glass
candidate_tags: []
paper_keywords:
  - keyword:water-interfaces
  - keyword:oxide-surface
  - keyword:silica-silicate
  - keyword:classical-ff
  - keyword:dft-static
source_refs: []
doi: "10.1680/jsuin.19.00053"
year: 2019
authors:
  - "Jiaqi Jin"
  - "Xuming Wang"
  - "Collin D. Wick"
  - "Liem X. Dang"
  - "Jan D. Miller"
venue: "Surface Innovations"
pdf_sha256: "86e4ec1db69d175077e34370fb0f9e5bd0cc656879f4a052ffe1b893029281ab"
pdf_path: "papers/Others/Jiaqi_Jin_Surface_Innovations_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019jinjiaqi-surface-inno-silica-surface -->

## Summary

The study couples VASP PBE-PAW calculations with Grimme D3 van der Waals corrections (500 eV cutoff, 4×4×1 k-mesh for slab models) to Amber classical MD using ClayFF for silica and SPC/E water. Surfaces include talc (001), tridymite (001), quartz (001), and a siloxanated quartz model built by fitting a talc-like siloxane overlayer onto quartz (001) followed by DFT relaxation. Together the methods quantify wetting, hydroxylation propensity, interfacial layering, and cluster hydration energies that bracket non-polar siloxane versus polar silanol chemistries. The mineral set spans phyllosilicate and framework silica polymorphs so hydrophobic basal planes can be contrasted with more hydrophilic cuts without changing the water model.

## Methods

### 1 — Classical MD (sessile drops, interfacial water)

**Engine / code:** **Amber** (including **Sander**), **ClayFF** for **silica** and **SPC/E** for **water**. **Systems / geometry:** **(001)** **talc**, **tridymite**, **quartz**, and a **DFT**-informed **siloxanated quartz** model; for **contact-angle** “sessile drop” runs, **~140×140 Å²** surfaces, **>15 Å** **slab** thickness, **3D** **PBC**, **~1300** water molecules, **~6 nm** **droplet** **diameter**. **Ensemble / thermostats:** **NVT** at **298 K**; **1 ns** equilibration then **200 ps** for **drop** **contours**; the paper also reports a separate **1 ns + 1 ns** **NVT** protocol for **interfacial** **number-density** and **retention** analyses. **Time step and thermostat:** **N/A** — not reported in the article text (standard **Amber** defaults implied). **Real-space / LJ cutoff:** **10 Å**. **Barostat / servocontrol of pressure:** **N/A** — **NVT** cells. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A** — direct **MD** only. **Output:** **contact** **angles** from **2D** **density** **contours** averaged over **200 ps**; **Wenzel**-style discussion where noted.

### 2 — DFT (VASP)

**Functional:** **PBE**; **PAW**; **500 eV** **plane-wave** cutoff; **Grimme D3** for **vdW**; **4×4×1** **k**-mesh (for **(001)** **slab** models tabulated in the **Methods**). **Structures and observables** include relaxed **(001)** terminations, **H₂O** **chemical-potential** / **hydroxylation**-style **probes** (e.g. **four** **H₂O/nm²** in **~30 Å** **vacuum** in the DFT part of the **Methods**), plus **E_ads** trends used to set **Amber**+**ClayFF** **chemistry** of **siloxanated** **quartz**.

### 3 — ReaxFF / RMD and FF training

**N/A** — the paper does **not** use **reactive** **RMD** or a **ReaxFF** reparameterization; it couples **PBE+vdW** **VASP** with **ClayFF**+**SPC/E** **Amber** **NVT** **dynamics** at **room** **temperature**.

## Findings

**Outcomes and mechanisms.** **Non-polar** **siloxane**-terminated **models** are **more** **hydrophobic** (contact **angles** **~80°**, **~3 Å** **depletion** at the **interface**, **weaker** **layering**). **Silanol**-**rich** **faces** are **more** **hydrophilic** with **brighter** **1–2** **Å** **layering** and **cluster** **hydration** **energies** **~−1.2 to −1.6 eV**, in line with **immersion** **calorimetry** the **paper** **cites**.

**Comparisons to experiment / literature** where stated: the **energetics** **trends** are **framed** against **immersion** data (see **citations** in the **source**), not a **full** **world** **wetting** **database**.

**Sensitivity to processing history (surface preparation).** **Calcination** vs **re-hydroxylation** **switches** **terminations** (siloxane vs **silanol**), so **wetting** **responses** and **flotation**-relevant **behavior** **shift** for the **same** **nominal** **mineral** **cleavage** **face**.

**Corpus / KB honesty** The **Amber**+**rigid** **water** **treatment** does **not** follow **proton**-**transfer** **RMD**; **Siloxanated** **quartz** is an **intermediate** **morphology** when **industrial** **grains** **are** not **one** **ideal** **termination** **everywhere**.
## Limitations

ClayFF with rigid SPC/E water does not capture dissociative hydrolysis pathways that the authors address only in selected DFT calculations. See **Findings** above for **corpus**-level caveats vs **authored** **claims**.

## Relevance to group

The paper is a silica–water interface benchmark for geochemical and mineral-processing classical MD, complementary to reactive ReaxFF studies elsewhere in the corpus.

## Citations and evidence anchors

- `papers/Others/Jiaqi_Jin_Surface_Innovations_2019.pdf`

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- DFT + ClayFF pipeline: see [[reaxff-family]] for contrast with reactive water–oxide field development.
