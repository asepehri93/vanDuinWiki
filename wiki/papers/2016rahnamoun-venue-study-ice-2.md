---
id: paper:2016rahnamoun-venue-study-ice-2
type: paper
title: "Study of ice cluster impacts on amorphous silica using the ReaxFF reactive force field molecular dynamics simulation method"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:reaxff
  - material:oxide
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:water-interfaces
  - keyword:lammps
  - keyword:oxide-surface
candidate_tags: []
source_refs: []
doi: "10.1063/1.4942997"
year: 2016
authors:
  - "A. Rahnamoun"
  - "Adri C. T. van Duin"
venue: "J. Appl. Phys. 119, 095901 (2016)"
pdf_sha256: "e2dbcd4af61d5c2c3e08a42e36df6c388d55b3f4e76439443bd5c729d57b0356"
pdf_path: "papers/Rahnamoun_JPA_Ice_clusters_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016rahnamoun-venue-study-ice-2 -->

## Summary

ReaxFF reactive MD simulates hypervelocity impacts of amorphous and crystalline ice clusters (150 and 128 water molecules, respectively) onto fully oxidized and suboxide amorphous silica surfaces at 1, 4, and 7 km s\(^{-1}\). The study connects sticking versus bounce, dissociation, secondary impacts on ice-covered silica, and temperature diagnostics to judge when electronic excitation might invalidate classical chemistry. **J. Appl. Phys.** **119**, **095901** frames the problem as **icy-body** **impingement** on **silica** **spacecraft** materials—distinct from **ambient** **water** adsorption studies—where **hypervelocity** **clusters** impart **shock** heating and **scattering** not captured by **static** **surface** **adsorption** models.

## Methods

This **DOI** duplicates the article curated on [[2016rahnamoun-venue-study-ice]]; the protocol is the same **ReaxFF** study in *J. Appl. Phys.* **119**, **095901**. **Amorphous** (**150** H\(_2\)O) and **crystalline** (**128** H\(_2\)O) ice clusters strike **fully oxidized** and **suboxide** amorphous silica built from compressed **SiO\(_2\)** / **SiO\(_{1.5}\)** precursors in **periodic** cells (**~2600–2610**-atom slabs). Clusters start **~20 Å** from the surface; the combined system is **NVT**-equilibrated at **150 K**, then given normal velocities of **1**, **4**, or **7 km s\(^{-1}\)**. The text specifies **NVT** for this equilibration but does not name a **thermostat** coupling scheme in the PDF body checked here (**N/A — thermostat model** beyond the **NVT** label). Collisions are integrated in **NVE** for **30 ps** with a **0.1 fs** timestep (with a **0.05 fs** cross-check for the fastest amorphous-on-suboxide case). Each condition is run **three** times. Second impacts quantify mass gain/loss on **ice-pre-covered** silica. **N/A — barostat or target hydrostatic pressure** — **NVE** impacts omit **pressure** control. **N/A — applied electric field; umbrella / metadynamics / replica exchange** — not reported.

**Force-field training.** **N/A —** applies an existing ReaxFF description.

**Static QM / AIMD.** **N/A —** not the primary modality; the text discusses classical chemistry limits versus possible **electron excitation** near **~10 km s\(^{-1}\)**.
## Findings

At 1 km s\(^{-1}\), clusters deposit on the surface; at 4 and 7 km s\(^{-1}\), partial rebound appears. Limited water dissociation occurs at the higher speeds. Second impacts on iced surfaces show velocity-dependent accumulation or stripping—for example, full accumulation at 1 km s\(^{-1}\) for both impact rounds, partial stripping after a second 7 km s\(^{-1}\) hit, and mixed behavior at 4 km s\(^{-1}\) comparing crystalline versus amorphous ice. Temperature analysis argues electronic excitation is unlikely below ~10 km s\(^{-1}\) in this model, but near ~10 km s\(^{-1}\) peak temperatures can reach very high local values where ReaxFF’s ground-state chemistry assumption may break down. **Amorphous** vs **crystalline** **ice** clusters differ in **rigidity** and **energy** **partitioning**, which feeds through to **secondary-impact** **mass** balance on **pre-iced** **silica**.

## Limitations

Classical reactive MD omits explicit electronic dynamics; the paper flags ~10 km s\(^{-1}\) as a prudence threshold for excitation effects.

**Dust** **charging**, **plasma** **sheath** **acceleration**, and **multi-body** **impacts** in **orbital** **debris** **environments** exceed the **single-cluster** **normal** **incidence** **protocol** summarized on this page.

**Crystalline** **ice** **polymorphs** and **porous** **silica** **substrates** may alter **energy** **partitioning** compared to **dense** **amorphous** **silica** **films** used as **baselines** in the article.

## Relevance to group

van Duin-group application of ReaxFF to ice–silica hypervelocity collisions with explicit velocity staging.

## Citations and evidence anchors

- DOI: [10.1063/1.4942997](https://doi.org/10.1063/1.4942997)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
