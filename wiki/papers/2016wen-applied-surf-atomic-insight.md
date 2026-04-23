---
id: paper:2016wen-applied-surf-atomic-insight
type: paper
title: "Atomic insight into tribochemical wear mechanism of silicon at the Si/SiO2 interface in aqueous environment: Molecular dynamics simulations using ReaxFF reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.apsusc.2016.08.082"
year: 2016
authors:
  - "Jialin Wen"
  - "Tianbao Ma"
  - "Weiwei Zhang"
  - "George Psofogiannakis"
  - "Adri C. T. van Duin"
  - "Lei Chen"
  - "Linmao Qian"
  - "Yuanzhong Hu"
  - "Xinchun Lu"
venue: "Appl. Surf. Sci."
pdf_sha256: "db69d721bec0ceabd37290cd22b75ef5e89bd1f6b4d788ccdac0132f96357fec"
pdf_path: "papers/Jialin_Wen_AppSurfSci_2016.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:tribology
  - keyword:water-interfaces
  - keyword:oxide-surface
---

<!-- id:paper:2016wen-applied-surf-atomic-insight -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This Applied Surface Science article investigates tribochemical wear of single-crystal silicon against amorphous silica in an aqueous environment using ReaxFF molecular dynamics implemented in LAMMPS, with George Psofogiannakis and Adri C. T. van Duin contributing reactive force-field expertise from Penn State alongside Tsinghua- and Southwest Jiaotong-affiliated coauthors. The motivation is practical: silicon-based microelectromechanical systems operate in humid environments, and silicon chemical mechanical polishing relies on nanoscale removal mediated by slurry particles and water chemistry. Atomic force microscopy experiments cited in the paper suggest that interfacial Si–O–Si bridge bonds play an important role in silicon removal during aqueous wear, but the atomistic sequence of bond-breaking events remains incompletely resolved. The simulations aim to identify explicit silicon removal pathways and to separate chemical oxidation effects from mechanical load effects at a sliding Si/SiO\(_2\) contact.

## Methods

**1 — MD application (ReaxFF / LAMMPS).** **Engine:** **LAMMPS** with a **ReaxFF** parametrization formed by merging the **Si/Ge/H** and **H\(_2\)O** parameter sets cited in §2 (Supporting Information documents the validation path). **Geometry:** **five-layer** **slab-on-slab** model (**4.26 nm × 4.26 nm × 8.0 nm** cell) with **PBC in x and y**; bottom **rigid Si** fixture, **mobile Si(100)** layer, **300 H\(_2\)O** molecules, **mobile amorphous silica** film, and **top rigid silica** slab that can move laterally and vertically to impose load. **Surface prep:** separate **ReaxFF** equilibrations of **Si(100)+water** and **SiO\(_2\)+water** to build **H/OH/H\(_2\)O**-passivated surfaces (**Figures S3b / S5b**), then combined into the **sandwich** wear cell (**Figure 1**). **Wear protocol (five steps):** (i) approach silica until the target **normal force** is reached, (ii) hold **normal load** on the top rigid slab along **z**, (iii) **250 ps** equilibration of the compressed stack, (iv) **1 ns** lateral slide along **+x** at **10 m/s** (**0.1 Å/ps**), (v) **35 ps** normal retraction at **10 m/s**. **Normal loads:** uniform stresses equivalent to **2.0, 4.0, and 6.0 GPa** applied to the top rigid body (§2). **Ensemble:** **NVT** with **Nosé–Hoover** thermostat, **300 K**, **0.25 fs** timestep, **100 fs** damping, **Verlet** integration (§2 cites prior Yeon practice). **Barostat:** **N/A —** load is imposed mechanically via the **rigid** top slab rather than a **hydrostatic barostat**. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training.** **N/A —** the manuscript **combines** published **ReaxFF** libraries; it does not report a new **parameter fit** in the main text.

**3 — Static QM.** **N/A —** not used for the production wear trajectories (DFT literature cited only for mechanistic context in **Discussion**).

**4 — Analysis.** **OVITO** visualization of **Si removal counts**, **Si–O–Si bridge** populations, **H\(_2\)O** consumption, and **friction traces** (**Figures 3d, 8**).

## Findings

**Removal mechanisms.** The **abstract** and **§3** describe **two** **Si** removal channels: (i) rupture of **stretched Si–O–Si** bridges on the **Si** side, assisted by **H** attaching to **bridging O**; (ii) fracture of **Si–Si** bonds within **Si–Si–O–Si** chains that are mechanically loaded through **interfacial Si–O–Si** bridges to **silica**.

**Pressure response.** Under the **0.3 bond-order** molecular recognition criterion quoted in **§3**, **no Si** removal occurs at **2.0 GPa**, whereas **7** and **14 Si** atoms are removed at **4.0** and **6.0 GPa**, respectively, tracking the growth of **interfacial bridge-bond** populations (**Figure 7** narrative).

**Role of water.** **Water** both **oxidizes** the **Si** near-surface (contributing **Si–O–Si** in the **O-depth** profiles of **Figure 3c**) and, mechanically, can **separate** surfaces—yielding the **dual chemical/mechanical** interpretation summarized in **§4** (see also **Figure 8** friction / water-count correlations).

**Comparisons / context.** The **Introduction** ties the model to **AFM**-scale **Hertzian** contacts and **CMP** slurry **silica** particles; **Discussion** notes remaining **velocity** gaps between **MD** and **AFM** experiments.

**Corpus honesty.** Detailed **snapshots** and **bond-order** time series are in **Figures 2–8** of the **PDF** (`pdf_path`).

## Limitations

- **Time** and **length scales** remain below **engineering** CMP loads; qualitative **mechanism** focus.

## Relevance to group

Collaborative **Tsinghua**/**PSU** effort with **van Duin** on **ReaxFF** **tribochemistry** at **oxide** interfaces.

## Citations and evidence anchors

- **DOI:** [10.1016/j.apsusc.2016.08.082](https://doi.org/10.1016/j.apsusc.2016.08.082) (`papers/Jialin_Wen_AppSurfSci_2016.pdf`).
- Text-aligned pointers: `normalized/extracts/2016wen-applied-surf-atomic-insight_p1-2.txt`

## Reader notes (navigation)

- Tribochemistry cluster: [[2016yeon-venue-la5b04062]], [[theme-oxides-silica-ceramics]]; method hub: [[reaxff-family]].

## Related topics

- [[reaxff-family]]
