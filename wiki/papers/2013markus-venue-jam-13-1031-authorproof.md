---
id: paper:2013markus-venue-jam-13-1031-authorproof
type: paper
title: "Fracture of graphdiyne: Structurally directed delocalized crack propagation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:lammps
source_refs: []
doi: "10.1115/1.4024176"
year: 2013
authors:
  - "Dieter B. Brommer"
  - "Markus J. Buehler"
venue: "Journal of Applied Mechanics"
pdf_sha256: "405cb148a0d7e5d441cc85ff4da428ca1610c2607e26897e194779c181619be1"
pdf_path: "papers/ReaxFF_others/JAM-13-1031_2013_proof.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013markus-venue-jam-13-1031-authorproof -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the article identified by **DOI `10.1115/1.4024176`**. The corpus PDF is an **ASME proof**; confirm pagination against the **published issue** if needed.

## Summary

**LAMMPS** **molecular dynamics** with **ReaxFF** compares **mode-I**-like **fracture** of **graphdiyne** versus **graphene** under comparable loading. **Graphdiyne**—a **2D** carbon allotrope featuring **sp**-hybridized **acetylenic** linkages interwoven with **sp²** **aromatic** subunits—presents **heterogeneous bond types** and **network topology** distinct from **graphene**. The study reports that **graphdiyne** fails through a comparatively **delocalized** crack path in which the crack **deflects diagonally** relative to its initial orientation, whereas **graphene** exhibits a more **localized** failure mode under the parallel simulation setup.

The authors connect mechanical response to the **mixed bonding** character (**sp** vs **sp²** load paths) and draw qualitative analogies to **toughening** motifs discussed in **biological** materials (for example **hidden length** and **sacrificial bonding**), framing **graphdiyne** as a mechanically interesting **nanostructured** carbon for **composite** and **membrane** contexts where **defect tolerance** matters.

## Methods

**1 — MD application:** Simulations use the **LAMMPS** molecular dynamics package with a **first-principles-parameterized ReaxFF** reactive potential (as cited in the paper) to evolve **mode-I**-like **crack** geometries initialized from **continuum-inspired** notch/crack configurations (see figures in **`papers/ReaxFF_others/JAM-13-1031_2013_proof.pdf`** and **`normalized/extracts/2013markus-venue-jam-13-1031-authorproof_p1-2.txt`**). **Graphene** under **parallel** loading provides a **baseline** for **path morphology** and **failure localization**.

**Remaining MD slots (not on proof p1–2 excerpt):** **N/A —** **supercell atom counts**, **full periodic (PBC)** description, **ensemble** (**NVE**/**NVT**/**NPT** not stated here), **timestep**, **run durations**, **thermostat/barostat**, **temperature/pressure targets**, and any **enhanced sampling** are **not** quoted here; confirm in the **published ASME** article (**DOI `10.1115/1.4024176`**) rather than this **proof** PDF alone.

**2 — Force-field training:** **N/A —** the study **employs** a literature **ReaxFF** parameterization; it is not a **new** parameterization paper.

**3 — Static QM / DFT-only:** **N/A —** fracture progression is treated with **reactive MD**, not standalone static **QM** as the primary tool.

## Findings

**Outcomes and mechanisms:** **Graphdiyne** shows **delocalized** failure with **diagonal crack deflection**; **graphene** shows more **localized** cracking under the **parallel** setup described in the introduction. The discussion ties differences to **heterogeneous** **sp/sp²** bonding and network **covalency**, using qualitative **toughening** language (e.g., analogies to **hidden length** and **sacrificial bonding** in biological materials) rather than a single scalar **toughness** metric on the opening proof pages.

**Comparisons:** Direct **graphdiyne** vs **graphene** comparison is **in silico** under the authors’ **notched** **MD** protocol; experimental **graphdiyne** datasets remain sparser than for **graphene**.

**Sensitivity / design levers:** **Strain rate**, **system size**, and **temperature** (if held fixed in the study) are the usual levers for **brittle** vs **ductile-like** **MD** response; see full text for what was **varied**.

**Limitations and outlook:** **Proof PDF** pagination may differ from the **final** **ASME** layout; **finite-size** and **MD strain-rate** effects limit direct mapping to **experimental** **polycrystalline** or **multilayer** specimens.

**Corpus honesty:** Evidence anchors: **`papers/ReaxFF_others/JAM-13-1031_2013_proof.pdf`**, **`normalized/extracts/2013markus-venue-jam-13-1031-authorproof_p1-2.txt`**. Prefer the **published** issue for authoritative **figure** numbering.

## Limitations

**Proof PDF** may differ slightly from final layout. **Finite-size** samples, **strain-rate** effects, and **temperature** (if not varied) limit direct transfer to **experimental** **polycrystalline** or **multilayer** specimens.

Conceptually, the paper is a **mechanics** complement to **graphene** fracture studies: **graphdiyne**’s mixed **sp/sp²** network provides additional **degrees of freedom** for **crack** **branching** and **deflection** compared with homogeneous **sp²** sheets, which is why the authors emphasize **delocalized** damage rather than a single **cleavage** plane.

## Relevance to group

**2D carbon** **mechanics** study using **ReaxFF**—complements **nanocarbon** **electrode** and **mechanical** **failure** literature in the corpus.

Because **graphdiyne** remains less common than **graphene** in experimental datasets, treat simulation predictions here as **hypothesis generators** for **defect engineering** and **mechanical** **design** rather than as calibrated **failure** criteria for specific **samples**.

## Citations and evidence anchors

- DOI [10.1115/1.4024176](https://doi.org/10.1115/1.4024176).
- Excerpt alignment: `normalized/extracts/2013markus-venue-jam-13-1031-authorproof_p1-2.txt`.

## MAS / retrieval

Stable `id` **`paper:2013markus-venue-jam-13-1031-authorproof`** participates in `scripts/build_chunks.py` chunking; link the **published** **ASME** article for authoritative **pagination** when teaching **graphdiyne** **fracture** mechanics.

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
