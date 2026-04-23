---
id: paper:2017dom-nguez-guti-rrez-nuclear-fusi-unraveling-plasma-material
type: paper
title: "Unraveling the plasma-material interface with real time diagnosis of dynamic boron conditioning in extreme tokamak plasmas"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reactive-md
  - method:reaxff
  - method:hybrid-qmmm
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1088/1741-4326/aa7b17"
year: 2017
authors:
  - "F. Javier Domínguez-Gutiérrez"
  - "Felipe Bedoya"
  - "Predrag S. Krstić"
  - "Jean P. Allain"
  - "Stephan Irle"
  - "Charles H. Skinner"
  - "Robert Kaita"
  - "Bruce Koel"
venue: "Nucl. Fusion"
pdf_sha256: "b986c2ce957a58192c4bc7d62c954fb5eb86daa4ea8c83adac2af9a2658ff11b"
pdf_path: "papers/ReaxFF_others/Dominguez_Gutierrez_NuclFusion_2017.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017dom-nguez-guti-rrez-nuclear-fusi-unraveling-plasma-material -->

## Summary

**First in-chamber XPS** (via **MAPP**) on samples between **deuterium plasma** exposures probes **boronized** **ATJ graphite** after **boronization**. **Reactive molecular dynamics** explains how **B**, **C**, **O**, and **D** interplay controls retention; **QCMD** checks trends. Simulations **decode oxygen and boron roles** and predict **D uptake** on **boronized carbon** **similar in magnitude** to prior predictions for **lithiated, oxidized carbon**. The paper positions **boronization** as a common **wall conditioning** strategy in **tokamaks** and stresses that **fuel retention** on **PFM** materials couples **plasma exposure** to evolving **surface chemistry**—motivating **in situ** spectroscopy rather than **post-mortem** coupons alone (introduction themes; extract).

## Methods

**Experiment (tokamak PMI).** The **Material Analysis Particle Probe (MAPP)** on **NSTX-U** performs **XPS** on samples retracted to an **in-vessel** analysis chamber **between** **deuterium** plasma exposures—**Mg Kα** excitation (**hν = 1253.4 eV**) with a **hemispherical analyzer** configuration described in *Nucl. Fusion* **§2.1**. **MAPP** positions **ATJ graphite** coupons flush with **lower divertor** tiles during the **2015–2016** campaign window reported here, focusing on a **boronized** surface state **~12 days** after **boron** deposition; an **Au** reference sets the **binding-energy** scale (**4f\(_{5/2}\)** at **88 eV** as stated).

**MD application (ReaxFF + QCMD).** **Reactive MD** with **ReaxFF** treats **B/C/O/D** chemistry on **boronized graphite** models meant to mirror **XPS**-resolved **surface** speciation under **D** exposure. **Quantum–classical MD (QCMD)** is used as a **cross-check** on selected retention trends (coupling philosophy and software names appear in the **Methods** section). **Supercell** construction, **PBC**, **temperature**, **timestep**, **thermostat**, **ensemble**, and **trajectory length** are specified in *Nucl. Fusion* **§2** onward; this wiki page does **not** transcribe those tables from the short front-matter extract.

**Force-field training** is **N/A** (**published** reactive parameters as cited). **Bulk standalone DFT** is **N/A** as the headline method (**QCMD** supplies **QM**-level forces in a **hybrid** sense where used).

**MD blueprint honesty.** **Reactive molecular dynamics** with **ReaxFF** and **QCMD** checks use **PBC** **graphite**/boronized **surface** cells as described in *Nucl. Fusion*. **LAMMPS**/**other** engine strings, explicit **NVT**/**NPT**/**NVE** labels, **timestep**, **thermostat**, **barostat**/**pressure**, and **equilibration**/**production** durations (**ps**/**ns**) are **N/A** on this page—copy from the **PDF** **Methods**.

## Findings

- **Time-resolved** (between-exposure) **XPS** resolves **B–C–O–D** chemistry not accessible with **ex situ** post-campaign analysis alone.
- **Reactive MD** reproduces the **subtle B/O/C/D interplay** governing **D retention** on **boronized** surfaces.
- **Predicted D uptake** for **boronized carbon** is **close to** prior **lithiated + oxidized carbon** predictions—highlighting **oxygen-mediated** retention pathways.
- **Integrated picture:** **boron** and **oxygen** **co-species** on **graphite** are argued to set **effective** **trapping** sites that compete with **bare** **C–D** chemisorption scenarios emphasized in older models (discussion as summarized in abstract/extract).
- **Community context:** linking **boronized** **PFMs** to **fuel retention** benchmarks matters for **ITER**-era **material** choices and **divertor** **conditioning** strategies discussed in the fusion literature (introduction framing).

## Limitations

**Single campaign window** and **specific sample history**; **MD** models **specific** surface models and may not span **all** divertor conditions.

## Relevance to group

Shows **ReaxFF-style reactive MD** integrated with **tokamak PMI diagnostics**—adjacent to **plasma–surface** and **carbon hydrogen retention** modeling in the broader ReaxFF literature.

## Citations and evidence anchors

- DOI: [10.1088/1741-4326/aa7b17](https://doi.org/10.1088/1741-4326/aa7b17)

## Related topics

- [[reaxff-family]]
