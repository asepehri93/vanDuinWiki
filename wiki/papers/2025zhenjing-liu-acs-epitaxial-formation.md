---
id: paper:2025zhenjing-liu-acs-epitaxial-formation
type: paper
title: "Epitaxial Formation of Ultrathin HfO2 on Multilayer Graphene by Sequential Oxidation"
updated: "2026-04-22"
confidence: med
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
pdf_sha256: "86280011cc0697c4d97fd6149d2937cb1f6ff2b805eb6fc39bc4451562acb455"
pdf_path: "papers/Liu_Mao_ACSNano_Hf_graphene_2025.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2025zhenjing-liu-acs-epitaxial-formation -->

## Summary

**STEM** tracks **epitaxial ultrathin hafnia** grown by **sequential oxidation** of **epitaxial Hf** on **multilayer graphene**, resolving **a-HfOₓ → h-HfOₓ → m-HfO₂** with substrate-aligned orientations. The work reports **heteroepitaxial** **Hf → suboxide → monoclinic HfO₂** on **graphene**, with **STEM** (epitaxy, **h-HfOₓ** structure) and **SNOM** on conductivity across phases. **ReaxFF reactive MD** in **AMS** (with **hybrid fbMC/MD** in places) supports the **oxidation** **sequence** and **graphene-templated** **crystallization** versus **O₂** loading and **temperature** **ramps**, complementing **experiment**.

## Methods

- **Experiment:** **Epitaxial Hf** on **multilayer graphene**; **controlled oxidation** to **a-HfOₓ**, **h-HfOₓ**, and **m-HfO₂**; **STEM** / diffraction for epitaxial relationships; **SNOM** contrast between phases; additional **SI** materials (see journal **Supporting Information**).
- **ReaxFF MD (AMS):** **Conjugate-gradient** minimization; **NVT equilibration** at **300 K** for **100 ps** (**Berendsen**, **100 fs** damping); **separate Berendsen thermostats** on **Hf**, **4-layer graphene**, and **O₂** during **300 → 900 K** heating at **10 K/ps** with **Hf/O ReaxFF interactions disabled** until oxidation; then **annealing** at **900 K NVT** for **2 ns** with interactions enabled (**0.1 fs** time step; **10,000 fs** damping on Hf and O₂, **100 fs** on graphene). **18** model variants with/without graphene and **O₂** density documented (**Table S1**).
- **Hybrid fbMC/MD (AMS):** **Uniform-acceptance fbMC/MD** with alternating **10,000** MD and **10,000** fbMC iterations (**36,000,000** each), **0.1 fs** **timestep**, **~3.6 ns** **effective** MD at **900 K**; **parameters** **drₘₐₓ = 0.1**, **imcfrq = 10,000**, **imcstp = 10,000**, **imcroo = 4** per manuscript.

**1 — MD application (atomistic dynamics).** ReaxFF **molecular dynamics** in **AMS** (Amsterdam Modeling Suite) on **Hf**/**O₂**/**graphene** **compositions** (**18** **variants** in **Table S1**); **3D** **PBC**; **NVT** **stages** at **300 K** and **900 K** with **0.1 fs** **time step**; **Berendsen** **thermostats** on **Hf**, **4-layer** **graphene**, and **O₂** with stated **damping**; **Ramped** **temperature** to **900 K** with **Hf**/**O** **interactions** **disabled** then **enabled** for **2 ns** **anneal**; **fbMC/MD** **rare**-event **sampling** as above. **N/A** — no **NPT** **barostat** in the quoted **NVT** **blocks**; **N/A** — no **static electric field**; **N/A** — not **classical** **replica** **exchange**; **N/A** — not **metadynamics** in the NVT sense (use **fbMC/MD** label for enhanced sampling here).

**2 — Force-field training** — **N/A** to first principles (applies a published **Hf**/**C**/**H**/**O** **ReaxFF** **stack**; **covalent** C–Hf **training** limits per manuscript).

**3 — Static QM** — **N/A** (STEM/SNOM **experiment** + **ReaxFF** **MD** story).

**4 — Review** — **N/A.**
## Findings

- **Sequential oxidation** of **epitaxial** **Hf** on **multilayer** **graphene** gives **a-HfOₓ → h-HfOₓ → m-HfO₂** with **epitaxial** alignment, with **STEM**-resolved **displacive** relations among **hcp-Hf**, **h-HfOₓ**, and **m-HfO₂** relative to **graphene** (see main text and **SI**).
- ReaxFF **molecular dynamics** reproduces **coexistence** of **crystalline** (**hcp-Hf**, **h-HfOₓ**, **m-HfO₂**) and **amorphous** (**a-Hf**, **a-HfOₓ**) **domains** and supports the **proposed** **oxidation** **sequence**; **O₂** **density** and **temperature** **ramp** are **swept** in **Table S1** **variants**, giving **sensitivity** to **processing** **levers**. The **Hf**/**C**/**H**/**O** set omits **covalent** **graphene–Hf** **training**, so **MD** should not be read as **proving** **chemical** **adhesion**; **STEM** and **diffraction** remain the **primary** **experiment** **versus** **simulation** **comparison** for **epitaxy** and **phase** **labels**. **Limitations** and **outlook** for **interface** **chemistry** are in `## Limitations` and the **manuscript**.


## Limitations

**Hf/C/H/O ReaxFF** coverage does not include **explicit covalent graphene–Hf** bond training; **direct film–substrate bonding** and **graphene reconstruction** are outside the model. **ACS Nano** details and **SI** tables should be checked for **final** published **pagination**.

## Relevance to group

**Adri C. T. van Duin** (Penn State) contributes **ReaxFF modeling** partnered with **MIT** **in situ TEM** / growth expertise (**Ross**, **Jaramillo**).

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acsnano.5c04437](https://doi.org/10.1021/acsnano.5c04437)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
