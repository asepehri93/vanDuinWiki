---
id: paper:2017matthew-w-thompson-we-report-a-atomistic-carbide-derived
type: paper
title: "An atomistic carbide-derived carbon model generated using ReaxFF-based quenched molecular dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - method:reaxff
  - task:method-development
  - material:graphene-carbon-nano
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: null
year: 2017
authors:
  - "Matthew W. Thompson"
  - "Boris Dyatkin"
  - "Hsiu-Wen Wang"
  - "C. Heath Turner"
  - "Xiahan Sang"
  - "Raymond R. Unocic"
  - "Christopher R. Iacovella"
  - "Yury Gogotsi"
  - "Adri C. T. van Duin"
  - "Peter T. Cummings"
venue: "Carbon (MDPI)"
pdf_sha256: "3bbd9403704262f731450826a68a6d6fea098a44d5276db30166b38d0bd3be17"
pdf_path: "papers/Thompson_C_2017-proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017matthew-w-thompson-we-report-a-atomistic-carbide-derived -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The work introduces **quenched MD** with **ReaxFF** to build **three-dimensional carbide-derived carbon (CDC)** models capturing **heterogeneous porosity** and **short-range graphitic order** beyond idealized **slit pore** geometries. **Radial distribution functions**, **pore size distributions**, and **adsorption** metrics are compared to **experiment**; **post-quench compression** adjusts **pore statistics** toward targets, and **ring statistics** emphasize abundant **non-hexagonal** rings in **CDC** vs conventional **activated carbon** scenarios. **Vanderbilt**/**Drexel**/**ORNL**/**van Duin** collaboration targets **supercapacitor** and **adsorption** modeling needs.

## Methods

**1 — MD application (quenched ReaxFF MD + optional NPT compression in LAMMPS).** **Reactive MD (ReaxFF)** is run in **LAMMPS** to generate **3D carbide-derived carbon (CDC)** models using a **quenched MD (QMD)** schedule from **3500 K → 3000 K** on **fluid-like randomized initial carbon** cells (**20000 atoms** per sample in the reported **QMD-x** series, **~6.5–7.5 nm** cubic **periodic** boxes). **Quench duration** is varied (**5–500 ps**), giving nominal **quench rates ~100–1 K ps⁻¹** as described in the Computational Details section. **NVT** integration uses a **Nosé–Hoover thermostat** (**~100.5 fs** damping per the article text) with **Δt = 0.5 fs**. For selected models, a **post-quench NPT compression** step is applied (**3000 K**, **~20 000 atm** in the excerpted protocol) using the **Shinoda–Rahman**-style **NPT** integrator in **LAMMPS** with **Δt = 0.5 fs** and **stated damping** values for **temperature/pressure** control, intended to **shift pore-size distributions** toward experimental targets without destroying short-range **graphitic** motifs. **GCMC nitrogen adsorption** (also **LAMMPS**) is used to compare **simulated vs experimental** isotherms after structural generation. **N/A — electric field**: not part of the described QMD workflow.

**2 — Force-field training / fitting.** **N/A — new QM refit in this paper**: the authors apply a **published ReaxFF carbon** parameterization (cited combination of references in the article) suitable for **amorphous/porous carbon** QMD workflows.

**3 — Static QM / DFT.** **QSDFT** and related **experimental PDF/STEM** comparisons appear in the analysis pipeline, but **DFT** is **not** the on-the-fly **structure generator** for the QMD samples.

**4 — Review / non-simulation framing.** **N/A**: primary modeling paper. **Proof PDF** (`papers/Thompson_C_2017-proof.pdf`) may show placeholder metadata; confirm **final DOI/issue** via publisher records (**sibling:** **`[[2017matthew-w-thompson-we-report-a-atomistic-carbide-derived-2]]`** when populated).

## Findings

**Outcomes and mechanisms.** **QMD** models reproduce **g(r)**, **pore-size distributions**, and **adsorption** metrics that **track experimental CDC data** better than simplistic **slit-pore** baselines. **Ring statistics** show abundant **non-hexagonal** rings, distinguishing **CDC** models from many **activated-carbon**-like constructs at comparable mean pore sizes.

**Comparisons.** **Simulated N\(_2\) isotherms** and **QSDFT-reduced pore metrics** are compared to **experimental** CDC benchmarks; **STEM** images provide qualitative structural anchors in the article figures.

**Sensitivity and design levers.** **Quench rate** strongly controls **amorphous vs ordered** character (**faster quenches → more stringy/amorphous**; **slower quenches → more six-membered rings and larger pores** as summarized in the Results). **Post-quench compression** shifts **pore-size distributions** toward **sub-nanometer** targets while preserving much of the **local bonding** learned at slower quenches.

**Limitations and outlook (as authored).** The manuscript stresses that **simulation quench rates** lack a **direct one-to-one** mapping to **chlorine-etching** laboratory timescales; compression is likewise a **targeting device**, not a literal **synthesis** replica.

**Corpus / PDF honesty.** This page summarizes the **proof PDF** in-repo; operators should align **DOI**/**pagination** with the **published MDPI *C*** article when wiring automation.

## Limitations

- **DOI** not captured in local manifest metadata—resolve from the **journal issue** when wiring bibliographic automation.

## Relevance to group

**van Duin** contributes **ReaxFF** expertise to **nanoporous carbon** structure generation for **energy** materials.

## Citations and evidence anchors

- Source PDF: `papers/Thompson_C_2017-proof.pdf` (proof; confirm **final** **DOI** via publisher metadata).

## Related topics

- [[reaxff-family]]
