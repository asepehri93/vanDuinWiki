---
id: paper:2017mao-carbon-121-2-formation-incipient
type: paper
title: "Formation of incipient soot particles from polycyclic aromatic hydrocarbons: A ReaxFF molecular dynamics study"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.06.009"
year: 2017
authors:
  - "Qian Mao"
  - "Adri C. T. van Duin"
  - "K.H. Luo"
venue: "Carbon"
pdf_sha256: "1bf68ef7c2957ddd76e3481b5fe47b538a692d6f0eb1e425397e67cd97a574d7"
pdf_path: "papers/Mao_Qian_Carbon_soot_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017mao-carbon-121-2-formation-incipient -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

Soot inception in combustion remains challenging to model because it couples physical clustering of polycyclic aromatic hydrocarbons (PAHs) with progressively activated chemistry that builds covalent bridges and graphitic motifs. This open-access *Carbon* article reports ReaxFF molecular dynamics trajectories that follow incipient particle formation from PAH monomers ranging from naphthalene up to circumcoronene across 400–2500 K. The narrative partitions behavior by temperature: at low temperature, stacked clusters emerge primarily through noncovalent interactions; at intermediate temperatures, only certain larger PAHs remain chemically productive in the simulated time windows; at the highest temperature studied (2500 K), chemistry accelerates toward graphitizing aggregates with rising C/H ratio and structural motifs described as fullerene-like or bridge-linked stacks for the heaviest aromatics. The collaboration includes Tsinghua, University College London, and Adri C. T. van Duin, situating the work at the intersection of combustion chemistry and reactive molecular dynamics parameterization.

## Methods

**A — Force-field training / fitting:** **Combustion-oriented** **ReaxFF** for **hydrocarbon**/**PAH** chemistry—used as published in the article (**no** new fit summarized on this wiki page).

**B — Molecular dynamics / sampling:** **LAMMPS** **ReaxFF MD** on **PAH** monomers (**naphthalene → circumcoronene**) in **100 Å** cubic cells (**3D periodic boundary conditions**): each minimized monomer is replicated **50×**, randomly placed, **CG**-relaxed, then **vibrationally equilibrated** at the target **T** for **10⁶ iterations** at **Δt = 0.25 fs** with **zero** initial **translation/rotation**, followed by assignment of **Maxwellian** translational/rotational speeds (SI details). **System size & composition:** **50** copies of a given **PAH monomer** per cell (e.g. **~900 atoms** for **50 naphthalene** molecules as an order-of-magnitude lower bound; heavier PAHs scale toward **~10⁴ atoms** per cell—see article tables/SI for exact counts). **Production nucleation runs** use **NVT** at **400, 800, 1200, 1600, 2000, and 2500 K**, **8×10⁶ steps** (**Δt = 0.25 fs** ⇒ **2 ns** per run), **Nosé–Hoover** thermostat (**100 fs** damping), **three** independent initial seeds. **VMD** visualization. **N/A — barostat / hydrostatic pressure control**: **constant-volume NVT** pyrolysis cells—**no** stated **NPT** stage.

**C — DFT / static QM:** **Not** the production engine for these trajectories.

**D — Review / non-simulation framing:** **Primary** **Carbon** **application**—**not** a review.

## Findings

**Outcomes and mechanisms.** **Mechanistic regimes** separate with **PAH mass** and **temperature**: at **400 K**, **stacked clusters** form by **physical** association for all studied PAHs; as **T** rises, **physical nucleation** becomes less probable per PAH class; around **1600 K**, only **circumcoronene** remains reliably productive within the simulated windows; at **2500 K**, all PAHs become **chemically active**, driving **graphitizing** particles with rising **C/H** and motifs described as **fullerene-like** and **carbon-bridged stacks** for the heaviest PAHs.

**Comparisons.** The article positions these **ReaxFF** trajectories relative to prior **DFT**, **on-the-fly QM MD**, classical MD, and MC soot-nucleation literature summarized in the Introduction.

**Sensitivity and design levers.** **Temperature grid**, **PAH size**, **clustering criterion** (intermolecular distance cutoff for “particles”), and **replicate statistics** are the explicit knobs in the Methods/Results narrative.

**Limitations and outlook (as authored).** The authors acknowledge differences vs experiments where **collisional equilibration** of **translation/rotation** is imperfect in finite MD—mitigated by their **Maxwellian** assignment procedure.

**Corpus / PDF honesty.** Protocol numbers above come from the **open-access *Carbon*** PDF (`papers/Mao_Qian_Carbon_soot_2017.pdf`).


## Limitations

Simulation timescales and finite system sizes omit hydrodynamic transport, concentration fluctuations, and three-dimensional flame turbulence; extrapolation to full-engine soot models therefore requires hierarchical coupling beyond standalone MD.

## Relevance to group

The publication is a van Duin-coauthored application of ReaxFF to soot chemistry, valuable for retrieval queries on combustion, PAHs, and high-temperature carbon polymerization.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.carbon.2017.06.009` (`papers/Mao_Qian_Carbon_soot_2017.pdf`).

## Related topics

- [[reaxff-family]]
