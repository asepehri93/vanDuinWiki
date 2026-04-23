---
id: paper:2020momeni-npj-computat-multiscale-computational
type: paper
title: "Multiscale computational understanding and growth of 2D materials: a review"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:ml-atomistic
  - method:dft-static
  - method:classical-md
  - method:reaxff
  - method:continuum-or-mesoscale
  - task:review
  - scale:multiscale
paper_keywords:
  - keyword:review-or-perspective
  - keyword:aimd
  - keyword:machine-learning-potential
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1038/s41524-020-0280-2"
year: 2020
authors:
  - "Kasra Momeni"
  - "Yanzhou Ji"
  - "Yuanxi Wang"
  - "Shiddartha Paul"
  - "Sara Neshani"
  - "Dundar E. Yilmaz"
  - "Yun Kyung Shin"
  - "Difan Zhang"
  - "Jin-Wu Jiang"
  - "Harold S. Park"
  - "Susan Sinnott"
  - "Adri van Duin"
  - "Vincent Crespi"
  - "Long-Qing Chen"
venue: "npj Computational Materials"
pdf_sha256: "6a979482ad22e4e851a2bf4036c3fcae66eaa951f15cf5f56cde37dff536dd15"
pdf_path: "papers/Momeni_2D_review_NPJ_CompMat_2020.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020momeni-npj-computat-multiscale-computational -->

Review of **atomistic** (DFT, empirical and reactive MD including ReaxFF lines), **mesoscale** (e.g., phase-field), and **continuum** transport models for **2D material growth**, plus **machine-learning** angles for structure–property mapping and discovery.

## Summary

Since **graphene’s** isolation, **2D semiconductors** and **heterostructures** have motivated a broad **computational** ecosystem. The **abstract** frames the review around **three methodological tiers**: (**i**) **nanoscale atomistic** simulations—**DFT** and **MD** with **empirical** and **reactive** potentials (explicitly naming **reactive interatomic potentials**); (**ii**) **mesoscale** methods such as **phase-field** models; and (**iii**) **macroscale continuum** approaches coupling **thermal** and **chemical transport**. It further discusses **machine learning** to connect **structures** and **properties** and to **guide discovery** of new **2D materials**, closing with an **outlook** on **computational** support for **2D synthesis and growth**. The **introduction** stresses that **growth perfection** and **properties** are **exquisitely sensitive** to **processing**, enumerating desired traits (**mobility**, **bandgap tunability**, **flexibility**, **optical coupling**) and noting **top-down** vs **bottom-up** synthesis routes (**exfoliation** vs **CVD/ALD**) with contrasting **quality vs scalability** trade-offs.

## Methods

**4 — Review / perspective (primary article type).** The article is a **narrative review** in *npj Computational Materials* (DOI 10.1038/s41524-020-0280-2) that **surveys** **2D material** **growth and synthesis** across **length and time** scales. It **organizes** the field into: **(i)** **atomistic** tools—**DFT** and **molecular dynamics** with **empirical** and **reactive** interatomic potentials (including ReaxFF-line models in cited work); **(ii)** **mesoscale** **phase-field** and related **morphology** **models**; and **(iii)** **continuum** **thermal** and **chemical** **transport** coupled to **reactor**-relevant **heat/mass** **fluxes**. It also treats **machine learning** combined with **computation and experiment** for **structure–property** links and **new-material** **discovery**, and includes an **outlook** on **computation**-guided **2D** **synthesis and growth** after the **graphene-era** **expansion** of **layered** **systems** (per abstract and **Introduction** in the **VOR** at `pdf_path`). **Reproducibility** for any **numerical** value means opening the **cited primary** work—this review’s **scope** is **curatorial and comparative**, not a **single** **laboratory** protocol.

**1 — MD application (as one protocol in *this* document).** **N/A** — the article is **bibliography**-**driven**; it does not report one **NVE**/**NVT**/**NPT** **molecular** **dynamics** **run** with a single **code**, **time step (fs)**, **production (ns)**, and **thermostat**/**barostat** table for a single **2D** growth benchmark.

**2 — Force-field training.** **N/A** — no **de novo** **ReaxFF** (or other) **force-field** **fit** is a **result** of **this** **manuscript**; such **lines** are **cited** from the **literature**.

**3 — Static QM / DFT (a unified DFT study in *this* document).** **N/A** — the **DFT** content is **synthetic** (e.g. **GGA–PBE**-class **examples** and **limitations** in the **ATOMISTIC** **section**); **cutoffs, k-meshes, and structures** belong to **cited** **primaries** and **Table 1**-style **summaries** in the **review** itself, not a **one-off** DFT project performed **for** this **manuscript** alone.

## Findings

**Outcomes, comparisons, and sensitivity.** The review frames **wafer-relevant** outcomes—**uniformity**, **defect** burden, **grain** texture—as emerging from **coupled** **heat** and **mass** transport, **nucleation**, and **surface** reaction kinetics, so that **useful** **multiscale** **models** must link **DFT/atomistic** **barriers** to **FEM-** or **continuum-**class **transport** in realistic geometries. **Machine learning** is presented as a practical layer for **exploring** high-dimensional **synthesis** **parameter** spaces when paired with **expensive** DFT or **reactive** **MD**. **Challenges** called out in the text include **substrate** **defects** and **wrinkling**, **van der Waals** interactions across **scales**, **kinetics** **specific** to **monolayer** **growth**, and **reproducing** **flexural** (quadratic) **phonon** behavior with **classical** or **reactive** potentials. **Comparisons** to **experiment** and **agreement** between methods are **citation-specific**; no single **number** in this **wiki** should replace a **cited** **primary** study.

**Limitations and outlook (as authored).** A **review** **selects** **exemplars**; **ranks** of **codes** or **potentials** are **not** a **universal** table here. **Corpus honesty:** use the **VOR** file at `pdf_path` for **figure** and **table** **numbering**; the **sibling** **proof** **PDF** is listed under [[2020momeni-npj-computat-multiscale-computational-2]] if a **local** **duplicate** **bytes** need **governance** only.


## Limitations

As a **review**, it **selects** exemplars rather than **ranking** all codes/potentials; readers must consult **primary** studies for **quantitative** performance. **Adri van Duin** co-authorship signals **ReaxFF** ecosystem ties but does not make every section **ReaxFF-specific**.

## Relevance to group

**Adri van Duin** co-authorship ties the **ReaxFF / reactive MD** ecosystem to **2D growth** modeling communities spanning **Penn State** and partner institutions—useful for cross-linking **method** pages with **2D materials** theme hubs.

## Reader notes (navigation)

- [[2020momeni-npj-computat-multiscale-computational-2]] (uncorrected proof duplicate PDF)
- [[reaxff-family]]

## Related topics

- [[reaxff-family]]
