---
id: paper:2015verners-corrosion-sc-comparative-molecular-2
type: paper
title: "Comparative molecular dynamics study of fcc-Al hydrogen embrittlement"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:aluminum
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:reactive-md
  - keyword:metallic-systems
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1016/j.corsci.2015.05.008"
year: 2015
authors:
  - "Osvalds Verners"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
venue: "Corrosion Science (Article in Press)"
pdf_sha256: "02bedc4934956e74853b3fb0619770250d8d3ebb229915560ff6eb4eca5a0548"
pdf_path: "papers/Verners_AlH_CorrosionScience_2015_online.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015verners-corrosion-sc-comparative-molecular-2 -->

## Evidence and attribution

!!! note "Authority of statements"

    This file is an **Elsevier “Article in Press”** PDF for the same study as [[2015verners-corrosion-sc-comparative-molecular]] (**DOI** `10.1016/j.corsci.2015.05.008`). Full **Methods** detail and primary citation anchors live on that page.

## Summary

**ReaxFF** molecular dynamics in **LAMMPS** probes **hydrogen embrittlement** in **fcc Al** with **oxidized** surfaces and **notched Al/Al₂O₃** interfaces, comparing **H** tied to **initial Al vacancies** versus **random bulk H**. This ingest is a **publisher workflow duplicate** of the curated **version-of-record** article; scientific content matches [[2015verners-corrosion-sc-comparative-molecular]]. The duplicate PDF exists so the corpus can preserve **“Article in Press”** provenance while the wiki still points readers to the **paginated** sibling for **stable** **citation** **anchors**.

## Methods

This **Elsevier “Article in Press”** PDF (`pdf_path`) is the same **Corrosion Science** study as DOI **10.1016/j.corsci.2015.05.008** documented on **`[[2015verners-corrosion-sc-comparative-molecular]]`** with the paginated file `papers/Verners_AlH_CorrosionScience_2015.pdf`. The protocol is **LAMMPS ReaxFF** on a **3D periodic** oxidized, notched **fcc Al** slab with **162 H** either on **162 Al vacancies** (paired) or at **random bulk** sites, **573 K**, **0.2 fs**, **NPT** tensile cycling along **[1̄10]** (**0.25% / 0.5 ps** strain pulses, **2.5 ps** relaxations, **5 × 10⁻⁶ fs⁻¹** nominal rate) with lateral stresses relaxed to **0 Pa** via **Nosé–Hoover** thermostat (**100 fs**) and barostat (**10,000 fs** damping). **Force-field training:** targeted **VASP PBE PAW** **Al/H** augmentation (**350 eV**, **9×9×9** **k**-mesh) merged into published **Al/O/H** ReaxFF subsets, as on the canonical page. **Static QM:** same **VASP PBE** bulk references tabulated in the VOR article. No electric field or enhanced sampling is used.

## Findings

Qualitative conclusions match **`[[2015verners-corrosion-sc-comparative-molecular]]`**: **H** placement shifts **decohesion**, **voiding**, and **dislocation-mediated plasticity**; **vacancy-paired H** lowers **effective H diffusivity** versus **random bulk H** in the supersaturated slab tests summarized in the abstract. ReaxFF metrics are validated against **DFT** and experiment on the canonical validation table. For figure citations, stress–strain detail, and discussion of **nanoscale** and **ReaxFF** limits, use the **version-of-record** PDF; this **Article in Press** file is retained for corpus provenance.

## Limitations

Prefer the **paginated Corrosion Science** PDF ([[2015verners-corrosion-sc-comparative-molecular]]) for **stable pagination** and figures; **nanoscale slabs** and **ReaxFF** parameter bounds apply as on the canonical page. **Hydrogen** **embrittlement** in **real** **Al** **alloys** also involves **precipitates**, **grain** **boundaries**, and **hydrogen** **trapping** sites beyond the **model** **notch** geometries emphasized in the simulation campaign. **Corrosion** **environments** add **chloride**, **pH**, and **electrochemical** **potential** effects that are not the same problem as the **mechanical** **loading** cases tabulated here. **Hydrogen** **entry** from **aqueous** **paths** may follow **different** **transport** **channels** than **bulk** **interstitial** **H** **scenarios** emphasized in some **slab** **models**.

## Relevance to group

**Penn State / van Duin** **ReaxFF** application to **Al** **hydrogen embrittlement**; this slug preserves **non-primary** ingest provenance.

## Citations and evidence anchors

- **DOI:** `10.1016/j.corsci.2015.05.008` — this artifact: `papers/Verners_AlH_CorrosionScience_2015_online.pdf`.

## Reader notes (navigation)

- **Canonical article page:** [[2015verners-corrosion-sc-comparative-molecular]].

## Related topics

- [[2015verners-corrosion-sc-comparative-molecular]]
- [[reaxff-family]]
