---
id: paper:2025zhenjing-liu-acs-epitaxial-formation-2
type: paper
title: "Epitaxial Formation of Ultrathin HfO2 on Multilayer Graphene by Sequential Oxidation"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:oxides-ceramics
  - method:reaxff
  - task:experiment-integrated
  - material:graphene-carbon-nano
  - material:oxide
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:oxide-surface
  - keyword:nvt-simulation
  - keyword:reactive-md
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1021/acsnano.5c04437"
year: 2025
authors:
  - "Zhenjing Liu"
  - "Qian Mao"
  - "Varun Kamboj"
  - "Rishabh Kothari"
  - "Paul Miller"
  - "Kate Reidy"
  - "Adri C. T. van Duin"
  - "R. Jaramillo"
  - "Frances M. Ross"
venue: "ACS Nano"
pdf_sha256: "f0b7b6f00e09b16d6776ec69a4cf55f4b3f4644fcef0ddd2f35dcedbc2a5419d"
pdf_path: "papers/Liu_Mao_ACSNano_Hf_graphene_2025_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025zhenjing-liu-acs-epitaxial-formation-2 -->

!!! note "Corpus registration"

    This note documents the **same ACS Nano article** as [[2025zhenjing-liu-acs-epitaxial-formation]] but registers the corpus **`papers/Liu_Mao_ACSNano_Hf_graphene_2025_online.pdf`** variant (distinct SHA-256 from the sibling path). Bibliographic identity is the **DOI** below.

## Summary

The work combines **in situ scanning transmission electron microscopy (STEM)** with **sequential oxidation** of **epitaxial hafnium** grown on **multilayer graphene**, targeting an **ultrathin epitaxial hafnia** stack that progresses through **amorphous** and **hexagonal suboxide** motifs before forming **monoclinic HfO₂**. Complementary **scanning near-field optical microscopy (SNOM)** contrasts electronic response across phases. On the modeling side, **ReaxFF reactive molecular dynamics** within **AMS** explores oxidation sequencing, oxygen ingress, and coexistence of crystalline and amorphous regions, including **hybrid force-biased Monte Carlo / MD (fbMC/MD)** segments intended to accelerate rare oxygen penetration and **subsurface** oxidation relative to straightforward NVT annealing alone. This wiki slug mirrors the scientific narrative on [[2025zhenjing-liu-acs-epitaxial-formation]] while preserving provenance for the **online PDF** filename in the manifest.

## Methods

**Experiments** deposit and oxidize **epitaxial Hf** on **multilayer graphene** under controlled oxygen exposure, using **STEM** diffraction and imaging to resolve **hcp-Hf**, **a-HfOₓ**, **h-HfOₓ**, and **m-HfO₂** relationships and epitaxial alignment with the graphene template; **SNOM** supplements phase mapping. **Simulations** use a **Hf/C/H/O ReaxFF** parameterization with protocols spelled out in the article and **Table S1** of the Supporting Information: conjugate-gradient minimization; **NVT** equilibration at **300 K**; staged heating with **separate Berendsen thermostats** on **Hf**, a **four-layer graphene** block, and **O₂** during a ramp to high temperature; subsequent **900 K** **NVT** annealing with a **0.1 fs** timestep and differentiated thermostat damping on Hf, oxygen, and graphene. Optional **fbMC/MD** alternation (**10,000** MD steps and **10,000** fbMC iterations per cycle, repeated to large cumulative counts) targets enhanced sampling of oxygen transport at **900 K**. **Eighteen** model variants in the manuscript explore with/without graphene and varying **O₂** density.

**1 — MD application (atomistic dynamics).** ReaxFF **molecular dynamics** in **AMS** on **3D** **periodic** **(PBC)** **Hf**/**O₂**/**graphene** **supercells** (**18** **variants** in **Table S1**; full **stoichiometry** on **[[2025zhenjing-liu-acs-epitaxial-formation]]**). **NVT** at **300** **K** and **900** **K**; **0.1** **fs** **time** **step**; **2** **ns** **anneal** at **900** **K**; **Berendsen** **thermostat**; **fbMC/MD** **rare-event** **sampling**. **N/A** — **NPT** **barostat**; **N/A** — **static** **E**-**field** in **MD**; **N/A** — **replica** or **metadynamics**; **O₂** **fugacity** or **bar**-scale **control** (e.g. **1** **bar** in **SI**-style **setups**) is in the **VOR**, not re-derived from this **hash-only** **online** **PDF**.

**2 — Force-field training** — **N/A** (same **Hf**/**C**/**H**/**O** **ReaxFF** as sibling).

**3 — Static QM** — **N/A.**
**4 — Review** — **N/A.**
## Findings

The authors report a **sequential oxidation** pathway from **amorphous** and **hexagonal** suboxides to **epitaxial monoclinic HfO₂**, with **STEM**-resolved **displacive** relationships among **hcp-Hf**, **h-HfOₓ**, and **m-HfO₂** aligned relative to **graphene**. **Reactive MD** reproduces **coexistence** of crystalline and amorphous domains and supports the proposed oxidation ordering under the stated force-field assumptions. The manuscript explicitly notes that the **Hf/C/H/O** training does **not** include **strong covalent graphene–metal** bonds, so direct **chemical adhesion** between Hf and graphene falls outside the model’s intended scope even when simulations include both subsystems.

- **Comparisons:** **STEM**/**simulation** **agreement** on **phase** **order**; **O₂**/**T** **levers** in **Table S1**.

## Limitations

Maintain clarity between this **online-PDF** ingest and the sibling **`Liu_Mao_ACSNano_Hf_graphene_2025.pdf`** record when citing **pagination**. **Hf/C/H/O ReaxFF** limitations and **SI** tables should be checked for any **erratum**-level updates after publication.

## Relevance to group

**van Duin** group **ReaxFF** collaboration with **MIT** **epitaxial growth / TEM** ([[2025zhenjing-liu-acs-epitaxial-formation]]).

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acsnano.5c04437](https://doi.org/10.1021/acsnano.5c04437)

## Related topics

- [[2025zhenjing-liu-acs-epitaxial-formation]]
- [[reaxff-family]]
