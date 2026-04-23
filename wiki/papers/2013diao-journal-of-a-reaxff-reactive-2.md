---
id: paper:2013diao-journal-of-a-reaxff-reactive-2
type: paper
title: "ReaxFF reactive force field for molecular dynamics simulations of epoxy resin thermal decomposition with model compound (corrected proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:thermal-decomposition
source_refs: []
doi: "10.1016/j.jaap.2013.05.005"
year: 2013
authors:
  - "Diao, Zhijun"
  - "Zhao, Yuemin"
  - "Chen, Bo"
  - "Duan, Chenlong"
  - "Song, Sun"
venue: "Journal of Analytical and Applied Pyrolysis"
pdf_sha256: "1c2600f5d3658756bfebc3444a22f262329cc440261b402f49df89e164edcd42"
pdf_path: "papers/ReaxFF_others/Diao_epoxy_resin_J_An_App_Pyr_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013diao-journal-of-a-reaxff-reactive-2 -->

!!! note "Corpus note"

    This ingest is an **Elsevier corrected proof / in-press** PDF for **DOI `10.1016/j.jaap.2013.05.005`**. Prefer the **paginated issue** PDF when available. Substantive curated prose is duplicated under [[2013diao-journal-of-a-reaxff-reactive]]; this slug exists for **manifest** alignment with the proof path.

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter, except where they explicitly point to the sibling VOR page [[2013diao-journal-of-a-reaxff-reactive]].

## Summary

Diao *et al.* apply **ReaxFF reactive molecular dynamics** to **thermal decomposition** of an **epoxy resin model compound**, scanning **temperature** and **heating rate** to follow small-molecule products and classify elementary pathways during **pyrolysis**. The study is situated in **analytical pyrolysis** and **polymer degradation** contexts where **experimental** thermograms and **mass spectrometry** motivate atomistic interpretations, but where **full thermoset network** simulations remain expensive. The authors report that decomposition initiates preferentially through **ether C–O** cleavage, with major products including **H\(_2\)O**, **CO**, and **H\(_2\)**, and they organize mechanisms into **radical** channels and **1,1 / 1,2 / 1,3 elimination** families as described in the article. The work highlights both **kinetic accessibility** at **nanosecond** MD timescales and **force-field** limitations that may shift apparent onset temperatures relative to experiment.

## Methods

This slug tracks an **Elsevier corrected proof** PDF (`pdf_path`); protocol details should be confirmed against the paginated **JAAP** issue and the parallel entry **`[[2013diao-journal-of-a-reaxff-reactive]]`**.

**1 — MD application (atomistic dynamics).** **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** (explicit **MD** package name in **`pdf_path`** **Methods**). **System & composition:** **15** epoxy **model** molecules, **33 Å** cubic **PBC** cell, **~0.47 g/cm³** initial density (**~10³ atoms** class). **Boundaries / periodicity:** **three-dimensional PBC**. **Ensemble / staging:** **energy minimization**, then **NPT** at **300 K** for **50 ps** with **Berendsen** thermostat and **barostat**, compressing toward **~1.0 g/cm³**; **NVT** **pyrolysis** with **velocity Verlet** (**0.1 fs**), **Berendsen** thermostat (**100 fs** damping), **temperature-programmed** heating **300 → 2300 K** at **100–500 K/ps**, plus **constant-T** runs up to **4300 K** as in the article. **Duration:** per-stage **ps**/**ns** lengths in **`pdf_path`**. **Temperature:** **300–4300 K** span in the summarized protocol. **Pressure:** **NPT** equilibration uses **barostat** coupling; **NVT** pyrolysis legs **N/A —** no separate **GPa** hydrostatic **pressure** target stated for those segments. **Electric field:** **N/A —**. **Replica / enhanced sampling:** **N/A —**. **Species analysis:** **bond-order cutoff 0.3**.

**2 — Force-field training.** **H/C/N/O** **ReaxFF** parameter set as cited; **N/A —** not a new general **parameterization** paper.

**3 — Static QM / DFT.** **N/A —** not a standalone **DFT** results paper.

## Findings

**1 — Outcomes & mechanisms.** **Ether (C–O)** cleavage initiates **decomposition**; **heating rate** and **temperature** control onset timing (**Abstract**/**Results**). Products include **H₂O**, **CO**, and **H₂** with **radical** vs **1,1/1,2/1,3 elimination** families as classified in the article.

**2 — Comparisons.** **Qualitative agreement** with prior **experimental** epoxy **pyrolysis** observations is claimed at abstract level.

**3 — Sensitivity & design levers.** **Heating ramp**, **final T**, and **constant-T** set points are the main simulation **knobs** in the summarized protocol.

**4 — Limitations & outlook.** **Nanosecond** sampling and **model-compound** cells motivate cautious transfer to cured **thermoset** networks.

**5 — Corpus honesty.** **Proof** PDF may differ in figure numbering from the **final issue**; prefer **`[[2013diao-journal-of-a-reaxff-reactive]]`** for stable corpus narrative when bytes differ only by proof status.

## Limitations

**Proof** PDFs can differ in **figure** numbering from the **final issue**. **Model compound** cells omit **cross-linked** topology present in cured **epoxies**.

## Relevance to group

Workflow duplicate for **JAAP** **ReaxFF** **polymer pyrolysis** registration; canonical narrative may be consolidated with [[2013diao-journal-of-a-reaxff-reactive]] over time.

## Citations and evidence anchors

- DOI: [10.1016/j.jaap.2013.05.005](https://doi.org/10.1016/j.jaap.2013.05.005)

## Reader notes (navigation)

- [[2013diao-journal-of-a-reaxff-reactive]]

## Related topics

- [[2013diao-journal-of-a-reaxff-reactive]]
- [[reaxff-family]]
