---
id: paper:2017zhang-carbon-115-2-weakening-effect
type: paper
title: "Weakening effect of nickel catalyst particles on the mechanical strength of the carbon nanotube/carbon fiber junction"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - material:metal-surface
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.01.042"
year: 2017
authors:
  - "Chi Zhang"
  - "Adri C. T. van Duin"
  - "Jin Won Seo"
  - "David Seveno"
venue: "Carbon"
pdf_sha256: "5527fdaac2b077cbc0e460ee18d059fc61d354207ffff5216a35de15c507febd"
pdf_path: "papers/Zhang_Seveno_Carbon_2017.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:metallic-systems
---

<!-- id:paper:2017zhang-carbon-115-2-weakening-effect -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Carbon fiber reinforced polymer composites are widely used where high stiffness-to-weight ratios matter, and growing carbon nanotubes directly on fibers is one strategy to improve transverse toughness and stress transfer. Catalytic chemical vapor deposition with transition-metal nanoparticles is a common synthesis route, but the catalyst’s chemical state during growth—metallic versus oxide-influenced—and its mechanical embedding in graphitic substrates can complicate the final fiber–tube junction. **ReaxFF tensile simulations** evaluate **junction strength** between **SWCNT** and **graphene** layers modeling **CNT-on-carbon-fiber** attachments, comparing systems with **no nanoparticle**, **metallic Ni**, and **oxidized Ni** catalyst inclusions. The **pure Ni** particle case weakens failure stress substantially versus the **no-NP** baseline, whereas **oxidized Ni** leaves the junction comparatively strong; bond-level analysis ties differences to **Ni–C/O** bonding evolution during loading. The abstract emphasizes that tracking bond formation and rupture during load clarifies how the nanoparticle alters failure mechanisms beyond a purely elastic stress-concentration picture. **KU Leuven** experimental motivation meets **van Duin** reactive modeling.

## Methods

**Molecular dynamics (reactive).** **ReaxFF reactive molecular dynamics** loads **single-wall CNT**–**graphene** junction models in **tension**, comparing junctions with **no catalyst nanoparticle**, a **metallic Ni** cluster, and an **oxidized Ni** inclusion to mimic **CVD** residues on **carbon-fiber** surfaces at the **temperature** (**K**) and **strain-rate** conditions tabulated in *Carbon* **Methods**. **Periodic** **supercells**, **atom** counts, **timestep** (fs), **thermostat**/**barostat** choices, **NVT**/**NPT** staging, **equilibration**/**production** **duration** (ps/ns), and **strain-rate** details are given in *Carbon* **115** (**2017**) **589–599** (`pdf_path`); this wiki follows the **abstract** plus `normalized/extracts/2017zhang-carbon-115-2-weakening-effect_p1-2.txt`. **Electric fields** and **metadynamics**/**umbrella** **enhanced sampling** are **not** indicated for these **mechanical** pulls.

**Force-field training.** **N/A —** the study applies a published **C/O/Ni ReaxFF** description for **metal–carbon** contacts; no new **parameter optimization** is claimed on this page.

**Static QM / DFT.** **N/A —** **MD** drives bond rupture monitoring; **DFT** is not the trajectory engine here.

**Review scope.** **N/A —** primary *Carbon* article; **proof** sibling **`[[2017zhang-venue-paper]]`** tracks alternate **PDF** bytes.

## Findings

**Outcomes and mechanisms.** The **nanoparticle-free** junction attains the **highest failure stress** in the abstract’s comparison set. A **pure Ni** cluster **weakens** the junction by up to **~50%** relative to that baseline, whereas an **oxidized Ni** particle leaves the junction comparatively **strong** because **Ni–C/O** **bond** rearrangements during **tension** reroute **failure** away from the catastrophic pathways favored by the metallic case.

**Comparisons.** **Versus** the **no-NP** reference, both **Ni** chemistries shift **peak stress** and **bond** populations; the abstract frames the comparison as motivation for controlling **catalyst** **oxidation** state after **CNT** growth on fibers.

**Sensitivity / design levers.** **Strain**-controlled **tensile** loading exposes how **oxidation** state changes **interface** **bond** persistence, acting as a materials-processing lever distinct from elastic stress concentration alone.

**Limitations / outlook.** Idealized **graphene**/tube junctions omit **polycrystallinity** and real **CVD** defect distributions from **KU Leuven** experiments motivating the geometry.

**Corpus honesty.** Quantitative stress–strain tables and additional cases beyond the abstract should be read from the **PDF**; the maintainer excerpt is introduction-heavy.
## Limitations

- Idealized **graphene**/tube junction geometry; real **CVD** interfaces add **polycrystallinity** and **defect** distributions.

## Relevance to group

Demonstrates **ReaxFF** on **metal–carbon** **composite** interfaces coauthored by **van Duin**.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2017.01.042](https://doi.org/10.1016/j.carbon.2017.01.042)
- `normalized/extracts/2017zhang-carbon-115-2-weakening-effect_p1-2.txt`

## Reader notes (navigation)

- Nanocarbon mechanics: [[graphene-nanocarbon]]; group ReaxFF hub: [[reaxff-family]].

## Related topics

- [[reaxff-family]]
