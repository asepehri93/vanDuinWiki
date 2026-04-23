---
id: paper:2013lith-rev-csr-venue-rsc-cs
type: paper
title: "Lithium and sodium battery cathode materials: Computational insights into voltage, diffusion and nanostructural properties"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:batteries-electrochemistry, method:dft-static, method:classical-md, task:review, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1039/c3cs60199d"
year: 2014
authors: ["Islam, M. Saiful", "Fisher, Craig A. J."]
venue: "Chemical Society Reviews"
pdf_sha256: "0b01c7d87c5014faebf1aef8d8b13b7b90e37bf37bdef2233a3954418f42028d"
pdf_path: "papers/Others/Lith-Rev-CSR_jan14.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013lith-rev-csr-venue-rsc-cs -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Islam** and **Fisher** provide a **Chemical Society Reviews** survey of **computational work on lithium- and sodium-ion battery cathodes**, spanning **layered oxides**, **spinel** frameworks, and **polyanionic** frameworks such as olivine **LiFePO₄** alongside classic **layered LiCoO₂**-type and **spinel LiMn₂O₄**-type examples cited in the introduction. The review’s organizing axes include **intercalation voltage** trends, **alkali-ion diffusion** dimensionality and site networks, **defect** and **dopant** chemistry, and **surface** or **nanostructured** morphologies where **capacities** and **rate capability** deviate from bulk thermodynamic limits. A parallel thread motivates **Na-ion** cathodes for **grid-scale storage**, where **cost**, **abundance**, and **manufacturing** constraints can outweigh **gravimetric** energy density alone. The article is **context literature** for the corpus’s battery modeling notes rather than a van Duin-group primary study.

## Methods

As a **review**, **Methods** are **literature-scope** rather than a single simulation protocol. The introduction states that contemporary work uses two broad classes: **interatomic potential** methods (static lattice and **MD**) and **electronic-structure** methods, primarily **DFT** (extract Sec. 2 opening). A schematic (**Fig. 1** in the article) relates these computational approaches to complementary experiments and to properties such as **voltage**, **diffusion**, **defects**, and **surfaces**.

**DFT-oriented workflows** discussed include using **alkali chemical potential** differences to estimate **intercalation voltages**, **nudged elastic band**-type pathways or **AIMD** for **ion diffusion** barriers and dimensionality, and **Hubbard** or related corrections when **transition-metal d** states require beyond-standard **GGA** treatment (themes summarized in Sec. 2 and later application sections).

**Classical / potential-based** approaches are positioned for larger cells and longer times when **polarization** and **mechanical** distortions matter for **nanostructures**, with the caveat that parameter quality controls predictive power (Sec. 2.1 narrative in the extract).

## Findings

The opening overview highlights **layered**, **spinel**, and **polyanionic** examples (**LiCoO₂**, **LiMn₂O₄**, **LiFePO₄**) as recurring structural families whose **voltage**, **diffusion topology**, **defect chemistry**, and **surface/nano** effects have been studied computationally with strong **synergy** to experiment (abstract and Sec. 1).

**Outcomes and comparisons:** Across the surveyed literature, recurring **design tensions** appear in the excerpt: **polyanionic** frameworks often trade **gravimetric density** for **stability**; **layered** oxides can show **facile 2D** **Li⁺** transport but raise **interfacial oxygen** participation concerns; **spinel** frameworks can enable **3D** diffusion networks relevant to **rate capability**. The review stresses that **interfaces**, **electronic localization**, and **polaronic** carriers frequently demand **beyond-GGA** or specialized **electronic-structure** treatments—developed with material-specific citations in sections beyond the short extract.

**Sensitivity / levers (survey-level):** **Voltage**, **diffusion topology**, **defect/dopant** chemistry, and **nano/morphology** recur as levers coupling **thermodynamics** to **rate** and **capacity** in the cited computational literature.

**Limitations and outlook:** As a **review**, limitations are **field-level** (parameter accuracy, functional choice, accessible time/size scales) rather than tied to one simulation cell; see article sections for author-stated caveats.

**Corpus honesty:** This page is grounded in **`papers/Others/Lith-Rev-CSR_jan14.pdf`** and **`normalized/extracts/2013lith-rev-csr-venue-rsc-cs_p1-2.txt`** (short opening); it is **not** a substitute for the full **Chem. Soc. Rev.** article (**DOI `10.1039/c3cs60199d`**, **2014**, **43**, **185–204**).

## Limitations

- Not ReaxFF-specific; methods are broad. This PDF is included as **battery modeling context** in the corpus rather than a van Duin-group primary research memo.

## Relevance to group

Useful **battery cathode** background for connecting **atomistic electrolyte/interface** work (including reactive FF studies elsewhere) to mainstream DFT/potential literature.

## Citations and evidence anchors

- Title page and Sec. 1 (Chem. Soc. Rev., 2014, 43, 185–204; received 14 Jun 2013; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
