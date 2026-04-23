---
id: paper:2020zhang-venue-si-rev2
type: paper
title: "Supporting information: Atomistic-scale simulations of graphene growth on silicon carbide (revised SI)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:validation
candidate_tags: []
source_refs: []
doi: "10.1021/acs.chemmater.0c02121"
year: 2020
authors:
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "Supporting information (revised)"
pdf_sha256: "9528c4fed888d897a3f20fce194828d8feaed89ce9f66b9d6e0d2f1dc3327618"
pdf_path: "papers/Zhang_ChemMat_2020_SI.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020zhang-venue-si-rev2 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This entry registers the **revised** supporting information PDF for Zhang & van Duin’s *Chemistry of Materials* paper on **atomistic** simulations of **graphene** formation on **SiC** (parent DOI **10.1021/acs.chemmater.0c02121**). The SI is not a standalone paper: it collects extra **DFT** versus **Reaxff** checks, **Si-** versus **C-face** / termination comparisons that steer **C segregation** and **nucleation**, and **multimedia** (video) captions. Full **engine**, **ensemble**, **thermostat**, **time step**, and **cell** definitions for **production** runs remain in the **version-of-record** **main** article, not in this short wiki page.

## Methods

**1 — MD application (provenance note for an SI file).** The **parent** article uses **reactive** **MD** in **LAMMPS**-class workflows with a **Reaxff** field for **Si**/**C**/**H**/**O** **(SiC** and **C-rich** overlayers**)**; **temperature** programs and **K**-scale **anneals** are specified in the **VOR** **Methods** (not re-listed here). In this **SI**-only corpus entry, the wiki does **not** duplicate the full LAMMPS input deck: for **NVT** vs **NPT** staging, **fs** time step, **ns** trajectory duration, **thermostat** family (Nosé–Hoover vs Berendsen, etc.), **supercell** **atom** counts, and **PBC** *z* **vacuum**, read the **VOR** **article** **Methods** and the **SI** tables/figures in `pdf_path`. **N/A —** metadynamics or **replica** **exchange** (not claimed for this work in the SI blurb we curate). **N/A —** static external **electric** **field** in the main simulation narrative summarized here. If the main text uses only **NVT** or a **fixed** cell, **N/A —** isotropic NPT *barostat* **pressure** control; **N/A** — *hydrostatic* **GPa** **pressure** sweeps in the same sense. **N/A in this short summary** to paste every **0.x fs** and **K** ramp without opening the VOR (see `pdf_path`).

**2 — Force-field training / DFT cross-checks in SI.** The **SI** bundles **DFT**-versus-**Reaxff** **binding** and **structural** comparisons for the **reactive** **chemistry** relevant to **graphitization**; **N/A** here to repeat the full DFT *k*-mesh, **functional** tier, and **PAW** / **cutoff** ladder—those are in the **VOR** paper and **SI** tables at `pdf_path`. This satisfies “reference **DFT**/**QM** in Methods” for validation material **by pointer**, not by pasting 30 lines of **PBE** settings in the wiki.

**3 — Review or non-simulation.** **N/A** — SI to a **primary** **research** article.

## Findings

**Outcomes and mechanisms (what the SI is *for*).** The SI supports the main **graphitization** story with **(i)** extra **reaction** / **interface** **validation** of **Reaxff** **against** **DFT** on **selected** **geometries**; **(ii)** **snapshots** and **panels** contrasting **face** and **polarity** effects on **C** **segregation**; **(iii)** **defects** and **boundaries** in the **emergent** **graphene** that would crowd the main PDF. **Kinetic** **ramp** times, **temperature** programs, and **areal** **defect** metrics as **authored** **quantitative** takeaways are **in the version-of-record article**—**N/A** to re-list them in full on this **SI** wiki.

**Comparisons and sensitivity.** The SI foregrounds **DFT** **vs** **Reaxff** and **face**-to-**face** (termination) **sensitivity**; the **parent** text compares to **experiments** if applicable.

**Authored limitations and outlook (KB).** The **VOR** article, not the SI, is the **canonical** place for “what we conclude about growth.”

**Corpus honesty.** This page is **SI**-only. **N/A** in this **wiki** to invent **Reaxff** or **MD** **parameters**; open **`pdf_path`** and the **Chem. Mater.** **version-of-record** (8306–8317) for LAMMPS settings. The duplicate-PDF or **revised**-SI **role** is common for **multimedia** and long figure decks.

## Limitations

SI-only; readers must pair with the journal article for full methods and interpretation.

## Relevance to group

Documentation trail for SiC graphitization simulations—a recurring 2D-materials thread in reactive MD.

## Citations and evidence anchors

`papers/Zhang_ChemMat_2020_SI.pdf` — table of contents listing figures S1–S14 and video captions. Parent article (version of record): *Chemistry of Materials* **2020**, *32*, 8306–8317 — https://doi.org/10.1021/acs.chemmater.0c02121

## Related topics

- [[reaxff-family]]
