---
id: paper:2023oviroh-npj-clean-wa-towards-realisation
type: paper
title: "Towards the realisation of high permi-selective MoS2 membrane for water desalination"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:water-silica-geo
  - task:application
paper_keywords:
  - keyword:review-or-perspective
  - keyword:water-interfaces
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1038/s41545-023-00228-y"
year: 2023
authors:
  - "Peter Ozaveshe Oviroh"
  - "Tien-Chien Jen"
  - "Jianwei Ren"
  - "Adri van Duin"
venue: "npj Clean Water"
pdf_sha256: "25b99486261d462e7aff8de2407fae8f398b0a6b1cdc419655a1eebc12fdaa18"
pdf_path: "papers/Oviroh_et_al-2023-npj_Clean_Water.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023oviroh-npj-clean-wa-towards-realisation -->

## Summary

The introduction cites **climate change** and **freshwater** stress, notes that most **Earth** water is **saline**, and positions **reverse-osmosis** membranes as an energy-intensive but widespread **desalination** technology whose performance depends on **permeability**, **rejection**, **fouling**, and **material** durability. Oviroh et al. review **molybdenum disulfide (MoS₂)** as a candidate **2D membrane** material for **desalination**, motivated by **climate stress** on **freshwater** and the **water–energy nexus**. The article contrasts **polymeric reverse-osmosis** membranes with **atomically thin** MoS₂, arguing that **nanometer thickness** can increase **water permeability** by shortening **diffusion lengths** while—if **pores/defects** are controlled—maintaining **ion rejection**. The review organizes reported **experimental** strategies, discusses **manufacturing** and **defect** challenges for **near-atomic** membranes, and outlines **fabrication** and **process** needs for **industrial** translation. **Adri van Duin** is a co-author, linking the piece to the group’s **2D materials** and **interface** modeling threads.

## Methods

### Literature synthesis (D)

**Narrative review** of **MoS\(_2\)** **2D** **membranes** for **desalination**: **pore** engineering, **transport** metrics, **fabrication**, **scalability**—**methods** belong to **cited** studies.

### Atomistic simulation stance

**No** new **MD/DFT** campaign in the main text; any **atomistic** **membrane/MD** work is **second-hand** from **cited** papers.

**1 — MD application.** **N/A** in this *npj Clean Water* **review** for a **reproducible** LAMMPS- or GROMACS-class recipe—**N/A** for a **universal** **timestep**, **NPT** **barostat**, or **E-field** **table**; **N/A** for **metadynamics/umbrella** in this **authored** **main** text (if **cited** work uses them, go to **that** **DOI**).

**2 — Force training.** **N/A**—not a ReaxFF or other **reactive** **FF** **parametrization** paper; **N/A** for an **optimizer**-**weight** line.

**3 — Static DFT.** **N/A** as a **new** PBE+DFT **study**; **N/A** for a VASP *k*-mesh in this work—the **Oviroh** *et al.* article is **narrative**+**bibliography**, not a static-QM data release.

**Review organization (additional).** The article walks through **MoS\(_2\)** membrane concepts starting from **monolayer** **permeability** arguments, then summarizes **pore** engineering routes (including **defect** versus **sub-nm** **pores**), **interlayer** **spacing** control, and **support** **substrate** effects that appear in experimental literature. Because each subsection cites **primary** studies, quantitative **water** **permeance** and **ion rejection** values must be traced to those **sources** rather than summarized as universal benchmarks here.

## Findings

### Abstract roadmap

Compares **ion rejection**/**permeability** strategies, discusses **scalability** barriers, and outlines **controlled fabrication** needs for **industrial** translation.

### Practical hurdles

**Near-atomic** membrane fabrication, **defect/pore** control, and **process integration** are emphasized as **lab-to-market** gates.

### Scope

Provides a **roadmap** narrative rather than a single **benchmark** number—trace metrics to **primary** membrane studies.

## Limitations

The review’s **engineering** focus means **atomistic** **ReaxFF** or **DFT** studies appear only where cited authors pursued them; this page does **not** summarize **pore** **MD** benchmarks by itself. **Performance metrics** (permeability, rejection, stability) vary widely with **pore geometry**, **support** layers, and **measurement** conditions across cited works; readers must compare studies carefully. This review **does not** present new **atomistic** simulations in the main text.

**Confidence rationale:** `high`—clear scope and author claims from the open extract.

## Reader notes (navigation)

**van Duin** co-authorship makes this review a useful **bridge** between **membrane** **engineering** discourse and **2D** **simulation** themes elsewhere in the corpus, even though the article itself is not a **ReaxFF** methods paper.

- [[theme-2d-epitaxy-growth]]
- [[reaxff-family]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[reaxff-family]]
