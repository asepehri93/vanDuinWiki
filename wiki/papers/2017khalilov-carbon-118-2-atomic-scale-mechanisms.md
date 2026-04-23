---
id: paper:2017khalilov-carbon-118-2-atomic-scale-mechanisms
type: paper
title: "Atomic-scale mechanisms of plasma-assisted elimination of nascent base-grown carbon nanotubes"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - method:reaxff
  - method:monte-carlo
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:graphene-carbon
  - keyword:monte-carlo-sampling
  - keyword:nvt-simulation
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.03.068"
year: 2017
authors:
  - "Umedjon Khalilov"
  - "Annemie Bogaerts"
  - "Erik C. Neyts"
venue: "Carbon"
pdf_sha256: "b49eb0e7ac92bd31046b7a1b6dd7e9a926b74131e35cb5d584411289e4074eb1"
pdf_path: "papers/ReaxFF_others/Khalilov_Carbon_2017_CNT_growth.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017khalilov-carbon-118-2-atomic-scale-mechanisms -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** stage labels, structural assignments, and comparisons to DFT, use the **Carbon** article and Supplementary material—not this page alone.

## Summary

Hydrogen-rich plasmas can **etch** nascent carbon nanotubes (CNTs) while growth is still ongoing, yet nanoscale **sequencing** of cap versus sidewall chemistry is poorly resolved experimentally. This paper combines **ReaxFF-based reactive MD** with **temperature-accelerated force-bias Monte Carlo (tfMC)** to follow **atomic hydrogen** attack on **base-grown** (5,5) and (10,0) motifs supported on **Ni** nanoclusters with a **virtual Al** substrate, intended to mimic catalyzed base growth. The simulations resolve a **multi-stage** hydrogenation and elimination pathway through intermediate **carbon nanosheet**, **nanowall**, and **polyyne-like** motifs, and contrast **etch onset** for **caps** versus **tube** segments with literature DFT and TEM where cited.

## Methods

**1 — MD application (reactive MD + tfMC).** The authors combine **reactive molecular dynamics** with **temperature-accelerated force-bias Monte Carlo (tfMC)** to follow **atomic hydrogen** attack on **base-grown** carbon nanotube motifs. **Temperature** is held at **1600 K** using the **canonical Bussi thermostat**. **Interatomic interactions** use **ReaxFF** with the **Ni/C/H parameter set of Mueller et al.** (as cited in the article). **System size & composition:** finite **Ni nanoclusters** (**55 Ni atoms** or **147 Ni atoms**) plus **CNT cap/tube carbon** (e.g. **40 carbon atoms** in the **(5,5) cap** example in Results) and variable **H** loadings maintained in the gas-phase reservoir. **Boundary conditions:** **finite cluster** models on a **virtual Al substrate** (non-extended bulk lattice); **N/A — explicit 3D periodic supercell vectors** for the full catalyst+gas assembly are not spelled out on the indexed pages—confirm in SI. **Initial geometries** include **(5,5)** and **(10,0)** caps and tubes on **Ni\(_{55}\)** or **Ni\(_{147}\)** clusters **physisorbed on a virtual Al substrate**, with **tangential** versus **perpendicular** tube/cluster arrangements intended to mimic catalyzed base growth. **Gas phase** uses **atomic H only** (not a full plasma mixture); **H concentration** in the MD stage is **kept constant**. After each **H adsorption** event, structures are **relaxed with tfMC** while **no new H impinges**; **gas-phase etching products** are **removed every 10⁶ MD steps** to limit pyrolysis side chemistry. **Duration / stages:** alternating **MD impingement** and **tfMC relaxation** segments with periodic **product purges**; **N/A — a single quoted production length in ns** is not tabulated in the excerpted computational section—use the article/SI for aggregated times. **N/A — timestep (fs)** and **engine label** beyond “reactive MD”: the indexed *Carbon* computational section does not state an integration timestep or name a specific MD package; confirm in the full PDF/SI if needed. **N/A — barostat / hydrostatic pressure**: the described protocol is **canonical (constant-temperature) MD** with **no** stated **NPT** or stress control. **N/A — electric field in the simulation cell**: the model isolates **atomic H** chemistry rather than imposing an external field in the MD setup (plasma fields are discussed only at the literature level in the Introduction).

**2 — Force-field training.** **N/A — new fit in this paper**: the study **employs published ReaxFF Ni/C/H parameters (Mueller et al.)** validated in prior work cited by the authors; there is **no** reported **QM refit** or **CMA-ES**/**ParReX** optimization campaign in this article.

**3 — Static QM / DFT.** **N/A — on-the-fly DFT**: comparisons to **literature DFT and TEM** are cited for context, but the **production trajectories** are **ReaxFF + tfMC** only.

**4 — Review / non-simulation framing.** **N/A**: primary **application** article, not a methods review.

## Findings

**Outcomes and mechanisms.** For **cap elimination**, hydrogenation proceeds in **staged** fashion: a **(5,5) cap** on a carbon-containing Ni cluster first **hydrogenates** (stage I), then evolves toward a **carbon nanosheet** (stage II). **Stage II** marks the **onset of net carbon loss** by etching in the idealized cap trajectory, whereas **defective caps** can begin losing carbon earlier so that stages I and II **merge**. The nanosheet may convert to **nanowalls** or vertical graphene patches before simplifying to **rings and short polyyne chains**, then **full removal** from the cluster (stages III–IV in the authors’ division). For **tubes**, the authors report that **etch onset differs from caps**: hydrogenation/dehydrogenation compete first, with **H coverage** on long tubes reaching roughly **30%** before etching starts in their analysis; the **first C–C bond cleavage** often appears on the **sidewall** rather than the cap region, with details depending on **chirality** and **strain** as developed in the Results section and figures.

**Comparisons.** The article frames **cap versus tube** etching sequences against **available theoretical and experimental evidence** on **hydrogen-driven** restructuring of carbon nanostructures (see Introduction and Discussion in the *Carbon* article).

**Sensitivity and design levers.** **Temperature** (**1600 K** in the simulations), **cap versus tube morphology**, **defectiveness** of the cap, **chirality**, and **strain** in the tube scenarios all shift where **hydrogenation**, **carbon loss**, and **intermediate motifs** (nanosheet, nanowall, polyyne-like fragments) appear in the reported trajectories.

**Limitations and outlook (as authored).** The model isolates **atomic H** rather than a **real plasma** composition; **rates** are **illustrative** of **mechanistic** pathways, not quantitative plasma replicas. The **virtual substrate** and **nanocluster** construction simplify **supports**, **mass transport**, and **catalyst restructuring** relative to experiment.

**Corpus / PDF honesty.** This page is grounded in the **peer-reviewed *Carbon*** text and the short local extract; **quantitative** kinetics and any **SI-only** protocol refinements should be checked in the **full PDF**/**SI** if operators extend beyond the indexed pages.

## Limitations

- Only **atomic hydrogen** is injected, not a full **plasma** mixture (ions, electrons, radical diversity), so rates and selectivities are **mechanistic** rather than quantitative plasma replicas.
- **1600 K** is far above many CVD operating windows; it accelerates chemistry and may access rearrangements less relevant at growth temperatures.
- **Cluster + virtual substrate** models simplify real supports, gas transport, and catalyst restructuring during long experiments.

## Relevance to group

Antwerp **PLASMANT** work on **ReaxFF + tfMC** for **plasma–carbon** etching; complements the knowledge base’s reactive carbon and CNT literature without van Duin group authorship.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2017.03.068](https://doi.org/10.1016/j.carbon.2017.03.068)
- Text pointers: `normalized/extracts/2017khalilov-carbon-118-2-atomic-scale-mechanisms_p1-2.txt`; article figures for stage-resolved cap and tube scenarios.

## Reader notes (navigation)

- **Material hub:** [[graphene-nanocarbon]]
- **Force-field overview:** [[reaxff-family]]

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
