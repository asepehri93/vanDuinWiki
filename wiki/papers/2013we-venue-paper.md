---
id: paper:2013we-venue-paper
type: paper
title: "Atomistic simulation of frictional sliding between cellulose Iβ nanocrystals"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:tribology
  - keyword:polymer
  - keyword:lammps
  - keyword:classical-ff
  - keyword:npt-simulation
canonical_tags:
  - domain:mechanics-tribology
  - material:polymer-organic
  - method:classical-md
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1007/s11249-013-0223-x"
year: 2013
authors:
  - "Xiawa Wu"
  - "Robert J. Moon"
  - "Ashlie Martini"
venue: "Tribology Letters"
pdf_sha256: "fc46c266fe9ecd128507b52549614c15374c93e18635c7ffbc1a7877df6f00a4"
pdf_path: "papers/ReaxFF_others/We_Moon_Martini_Cellulose_Tribol_Letter_2013.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2013we-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. The **Methods** section of the article states **LAMMPS** simulations using **ReaxFF** (`normalized/extracts/2013we-venue-paper_p1-2.txt`); frontmatter **`method: classical-md`** reflects corpus tagging rather than overriding the authors’ stated potential.

## Summary

**Atomistic MD** pulls **cellulose Iβ nanocrystals** past each other, varying **sliding velocity**, **normal load**, and **relative in-plane angle**. Trends in friction are analyzed alongside **hydrogen-bond counts** within and between cellulose chains. The authors report that although friction tracks HB metrics in many cases, **hydrogen bonding may not be the dominant** discriminator of friction on these nanocrystal surfaces—other mechanics (contact area, registry, elasticity) matter.

## Methods

**1 — MD application (atomistic dynamics).** **Fully atomistic** simulations in **LAMMPS** slide a **mobile cellulose Iβ** block on a **two-layer** substrate: the **bottom** substrate layer is **immobile**, the **upper** substrate layer is **free**, and the **mobile** block is driven as a **rigid body** with prescribed **lateral velocity** \(V_\mathrm{mc}\) and **normal load** \(N\) (`papers/ReaxFF_others/We_Moon_Martini_Cellulose_Tribol_Letter_2013.pdf`; `normalized/extracts/2013we-venue-paper_p1-2.txt`). **PBC** applies in the **in-plane** directions (**x**, **z** in the paper’s figure convention), with a **fixed** boundary along the **surface normal** (**y**). After screening facets, reported results focus on the **(200)** surface. The **Iβ** lattice follows cited **X-ray** parameters; the **atomistic supercell** is **equilibrated in NPT** before sliding sweeps (Section **2 Materials and Methods** in the extract). **Force field:** the authors state **ReaxFF** as implemented in **LAMMPS**, noting prior successful use for **CNC** mechanical properties. **Timestep, production run length, thermostat/barostat settings for sliding legs, and temperature setpoints:** **N/A —** not on the **p1–2** excerpt (the extract cuts mid-**NPT** sentence); read the full **Tribology Letters** PDF. **Shear / strain:** rigid-body **sliding** with controlled **velocity** and **normal load** as above. **Electric field / enhanced sampling:** **N/A —** not stated in the indexed excerpt.

**2 — Force-field training.** **N/A —** tribology application using a literature **ReaxFF** parametrization per the article’s own statement—not a new training study summarized here.

**3 — Static QM / DFT-only.** **N/A —** classical **MD** sliding study.

## Findings

**Outcomes & mechanisms.** Friction trends are analyzed vs **sliding velocity**, **normal load**, and **in-plane misorientation** \(\theta\) between contacting **Iβ** surfaces. **Hydrogen-bond** statistics within and between chains correlate with friction in many cases, but the abstract argues **H-bonding may not be the most significant factor**—contact **mechanics** (registry, contact area, elasticity) also matters.

**Comparisons.** The introduction contrasts **AFM** colloidal-probe experiments on cellulose-related surfaces (load trends, chemistry, roughness) with this first **CNC–CNC** crystalline sliding **MD** study.

**Sensitivity & design levers.** **Velocity**, **load**, and **misorientation** are the explicit knobs in the abstract framing.

**Limitations & outlook.** Classical **FF** omits **glycosidic** chemistry; `extraction_quality: partial` reflects publisher wrapper noise in the corpus extract header.

**Corpus honesty.** Despite the **`ReaxFF_others/`** folder name, the **authors** explicitly report **LAMMPS** + **ReaxFF** in **`normalized/extracts/2013we-venue-paper_p1-2.txt`**; confirm any updated parameterization notes in the **PDF** if results are compared to other **cellulose** force fields.

## Limitations

Classical FF limits chemistry (no glycosidic reactivity); `extraction_quality` **partial** due to publisher wrapper in the corpus extract.

## Relevance to group

Biopolymer **tribology** reference in corpus; complements reactive oxide/polymer studies elsewhere.

## Citations and evidence anchors

- DOI: [10.1007/s11249-013-0223-x](https://doi.org/10.1007/s11249-013-0223-x)
- Extract: `normalized/extracts/2013we-venue-paper_p1-2.txt`

## Related topics

- Nanocellulose interfaces and hydrogen-bond-dominated materials
- [[reaxff-family]] (orthogonal method)
