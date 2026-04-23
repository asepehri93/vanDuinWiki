---
id: paper:2016tao-liang-annu-rev-mat-reactive-potentials
type: paper
title: "Reactive Potentials for Advanced Atomistic Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:classical-ff-specialized
  - method:reaxff
  - method:classical-md
  - task:review
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1146/annurev-matsci-071312-121610"
year: 2016
authors:
  - "Tao Liang"
  - "Yun Kyung Shin"
  - "Yu-Ting Cheng"
  - "Dundar E. Yilmaz"
  - "Karthik Guda Vishnu"
  - "Osvalds Verners"
  - "Chenyu Zou"
  - "Simon R. Phillpot"
  - "Susan B. Sinnott"
  - "Adri C. T. van Duin"
venue: "Annu. Rev. Mater. Res. (2013) 43, 109–129"
pdf_sha256: "b40cc0b037263a003c6e0704b7c40fcd344f509cc09dd4f502aeeeb9f2aee9d2"
pdf_path: "papers/Liang_AnnuRev_Reax_COMB_2013.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:review-or-perspective
  - keyword:reaxff-parameterization
  - keyword:classical-ff
  - keyword:polarizable-ff
---

<!-- id:paper:2016tao-liang-annu-rev-mat-reactive-potentials -->

## Evidence and attribution

!!! note "Authority of statements"

    The canonical scholarly reference is **Annu. Rev. Mater. Res.** **2013**, **43**, **109–129** (**DOI** in front matter). The PDF filename includes **2016** metadata from download; cite the **Annual Reviews** volume/issue for bibliography.

## Summary

This **Annual Review** compares **variable-charge reactive empirical potentials**, focusing on **ReaxFF** and **COMB (charge-optimized many-body)** families, and surveys applications in **heterogeneous** environments where **bond-order** reactivity and **electrostatic flexibility** matter: catalysis on **metals** and **oxides**, oxidation, **electrochemical** interfaces, and complex **multicomponent** solids. The review’s pedagogical goal is to clarify how these potentials encode **charge equilibration** alongside **reactive** bond energetics, and how practitioners typically **fit** them to **QM** databases.

The article contrasts **ReaxFF**-style formulations with **COMB** approaches at the level of **energy partitioning**, **charge** models, and typical **training** practices, then uses literature examples to illustrate where **variable-charge** reactive models outperform fixed-bond force fields for **chemically evolving** systems.

## Methods

This peer-reviewed **Annual Review** article is not a single new simulation study; it synthesizes how **variable-charge** reactive empirical potentials—principally **ReaxFF** and **COMB**—partition **bond-order-mediated** reactivity versus **many-body** corrections, how **electrostatics** are treated (**self-consistent charge equilibration** versus **charge-optimized many-body** ideas), and how practitioners historically **optimize** parameters against **QM** databases cited throughout the chapter. Vignettes steer readers toward **metal**/**oxide** interfaces, **oxidation**, and **electrochemical**/**multicomponent** solids where bond-making and charge reorganization matter together. Because each primary reference brings its own **LAMMPS**/**VASP**/**CP2K** recipe, the review **does not** consolidate a single benchmark **MD** protocol—those details remain in the cited application papers.

**MD / reactive simulations (review-level).** Because the article is not one production study, **LAMMPS**/**CP2K**/**VASP**-class **engine** choices, **supercell**/**slab** sizes, **PBC** details, **NVT**/**NPT** labels, **timestep** (**fs**), **equilibration**/**production** **duration** (**ps**/**ns**), **temperature** (**K**) ramps, **barostat**/**pressure** targets (**bar**/**GPa**), and **thermostat** damping are **all N/A at review level**—read each cited primary paper. **Electric field:** **N/A —** not a unified theme. **Umbrella** / **metadynamics** / **replica exchange:** **N/A —** not surveyed as a methods spine.

**Force-field training (review-level).** **Parent** potentials: **ReaxFF** (van Duin lineage) vs **COMB** (Sinnott/Phillpot lineage). **QM reference data:** discussed generically with citations to **DFT** training corpora used historically in the literature. **Training sets** and **optimization** workflows (**least squares**, genetic/CMA-style searches where cited) vary by application; the review maps philosophies rather than publishing a new fit. **Experimental benchmarks:** cited where prior literature couples **ReaxFF**/**COMB** to measurements.
## Findings

The review argues that **variable-charge reactive potentials** are a workable compromise when simulations must reach **large system sizes** and **nanosecond** scales yet still allow **topology changes**. It contrasts **ReaxFF** and **COMB** not as interchangeable black boxes but as families with different **electrostatic** and **fitting** philosophies; **transferability** remains **training-limited** in both cases. **Comparisons:** the **abstract** frames a side-by-side of **ReaxFF** vs **COMB** for **multicomponent** problems. **Sensitivity / levers:** performance depends on how **QM** **training** breadth, **charge** models, and **bond-order** treatments match the application—details vary by cited study rather than a single knob table here. **Limitations / outlook:** reviews age; readers must pull **validation** evidence from **primary** sources rather than treating this article as a parameter file. **Corpus honesty:** this wiki entry aligns to *Annu. Rev. Mater. Res.* **2013**, **43**, **109–129** (DOI in front matter); the corpus **PDF** imprint shows a Penn State download stamp from **2016**—bibliography should follow the **journal** volume/issue, not the filename year.
## Limitations

Being anchored in **2013** literature, later **parameterization** advances, **software** implementations, and **best practices** must be updated from **primary** sources. Reviews do not replace **validation** for a specific **parameter file**.

For **operators** maintaining this wiki: use this review as a **map**, then jump to **application-specific** **ReaxFF** papers (oxide–water, organics, metals) for **quantitative** performance. The **COMB** comparison is especially useful when a simulation needs **charge** behavior beyond a minimal **QEq** treatment— but **compatibility** between **COMB** and **ReaxFF** databases is **not** automatic.

## Relevance to group

**van Duin-group** coauthored comparison of **ReaxFF** with **COMB**—often used as a **graduate-level** entry to **reactive potentials** in **materials** simulations.

When **MkDocs** readers land here from a **wikilink**, steer them next to **application** notes on **oxidation**, **electrolytes**, or **oxide** **interfaces**, because the review’s value is **orientation**, not **simulation-ready** parameters.

## Citations and evidence anchors

- DOI [10.1146/annurev-matsci-071312-121610](https://doi.org/10.1146/annurev-matsci-071312-121610).
- Excerpt alignment: `normalized/extracts/2016tao-liang-annu-rev-mat-reactive-potentials_p1-2.txt`.

## MAS / retrieval

Use this review as a **hub** pointer, not as a source of **parameter** numbers; chunk text still indexes useful **terminology** (**COMB**, **variable charge**, **ReaxFF**) for **hybrid** search.

## Related topics

- [[reaxff-family]]
