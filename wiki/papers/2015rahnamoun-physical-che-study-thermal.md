---
id: paper:2015rahnamoun-physical-che-study-thermal
type: paper
title: "Study of thermal conductivity of ice clusters after impact deposition on silica surfaces using the ReaxFF reactive force field"
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
  - keyword:oxide-surface
  - keyword:silica-silicate
candidate_tags: []
source_refs: []
doi: "10.1039/C5CP05741H"
year: 2015
authors:
  - "A. Rahnamoun"
  - "A. C. T. van Duin"
venue: "Physical Chemistry Chemical Physics"
pdf_sha256: "2f49538e651503e497528cd24dfc8f2f2413fb573547eca2365368a88f34a46e"
pdf_path: "papers/Rahnamoun_PCCP_Ice_clusters_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015rahnamoun-physical-che-study-thermal -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries track **Phys. Chem. Chem. Phys.** DOI `10.1039/C5CP05741H` and the local PDF/`normalized/extracts/2015rahnamoun-physical-che-study-thermal_p1-2.txt` abstract and introduction.

## Summary

Ice accretion on **aircraft** and **spacecraft** surfaces motivates quantifying **heat transfer** in impacted **ice** layers: thermal transport depends on **ice microstructure** and how clusters **attach** to **substrates**. The paper investigates **thermal conductivity (TC)** of **amorphous** and **crystalline** ice **after high-velocity deposition** on **silica** using **ReaxFF molecular dynamics**. It states that a **dual-thermostat** (non-equilibrium) method computes **TC**, with **validation** by comparing **crystal** and **amorphous ice** TC against **experimental** references before studying deposited clusters. The **abstract** reports that **TC drops** for both ice phases after deposition on silica, **more strongly** on **suboxide** silica surfaces; **crystal ice** retains **higher TC** than **amorphous** after accumulation, yet **1 km s⁻¹** impacts **disrupt crystallinity** so TC approaches **amorphous-like** values; **ionic species** embedded in ice **further reduce** TC in the modeled scenarios.

## Methods

**Reactive molecular dynamics** with **ReaxFF** uses the **silica–water/ice** interaction parametrization referenced in the article (bond-order + charge equilibration suitable for **proton transfer** at the interface). **System / composition:** **amorphous** ice clusters of **~500 H₂O molecules** and **crystalline** clusters of **512 H₂O** are prepared, **equilibrated** at **150 K**, placed **~20 Å** from **amorphous silica** **slabs** with contrasting **oxidation** (**fully oxidized** vs **suboxide**), then **impacted** at **0**, **0.5**, or **1 km s⁻¹**. **Boundaries:** **periodic boundary conditions** in **supercells** constructed for **thermal conductivity** extraction after attachment. **Ensemble / thermostat:** **equilibrium MD (EMD)** segments and **non-equilibrium MD (NEMD)** with **dual thermostats** (direct / heating–cooling-rate style method described in the article) are used to obtain **TC** values. **Timestep, production durations, bath temperatures, and supercell dimensions** appear in **Computational Methods** and are **not** in the short local extract.

**Barostat / hydrostatic pressure:** **N/A —** the summarized workflow emphasizes **NEMD** heat flux rather than **NPT** control.

**Electric field / metadynamics:** **N/A**.

**MD engine:** **N/A —** the indexed extract refers to the **ReaxFF reactive molecular dynamics program** generically; the **Methods** section of the **PDF** names the implementation.

## Findings

**After deposition on silica**, calculated **thermal conductivity** **drops** for both **crystal** and **amorphous** ice relative to free-standing references; the drop is **more pronounced** on **suboxide** silica. **Crystal ice** remains **more conductive** than **amorphous** after accumulation unless **1 km s⁻¹** impacts **disorder** the crystal toward **amorphous-like** **TC**. **Ionic dopants** inside ice **further reduce** **TC** in the abstract’s tests. **Comparisons:** the abstract states **validation** of the **NEMD** protocol against **experimental** **TC** for **crystal** and **amorphous** ice before deposition studies. **Sensitivity:** **TC** depends on **impact speed**, **substrate oxidation**, and **doping**. **Limitations:** **ReaxFF** phonon physics and **NEMD** finite-size effects are expected caveats (see article discussion).

## Limitations

**ReaxFF** captures **reactive** chemistry but **phonon** physics may differ from **spectral** or **GK**-based estimates; **NEMD** introduces **thermostat** and **size** effects. **Impact** simulations explore a **limited** speed set; **experimental** ice microstructures may span **beyond** the modeled clusters.

## Relevance to group

**van Duin**-co-authored **ReaxFF** application connecting **ice–silica** attachment and **suboxide** chemistry to **thermal conductivity** metrics relevant to **aerospace icing** and **surface energy** modeling—useful alongside other **water/silica** transport notes in the corpus.

## Citations and evidence anchors

DOI `10.1039/C5CP05741H` — PCCP **paper**; `papers/Rahnamoun_PCCP_Ice_clusters_2015.pdf`; extract `normalized/extracts/2015rahnamoun-physical-che-study-thermal_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[theme-water-silica-geo]]
