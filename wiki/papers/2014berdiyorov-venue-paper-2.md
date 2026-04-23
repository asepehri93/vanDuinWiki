---
id: paper:2014berdiyorov-venue-paper-2
type: paper
title: "Stabilized silicene within bilayer graphene (proof duplicate)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - domain:reactive-md
  - material:graphene-carbon-nano
  - method:reaxff
  - method:semiempirical-tightbinding
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-application
  - keyword:graphene-carbon
source_refs: []
doi: "10.1103/PhysRevB.89.024107"
year: 2014
authors:
  - "G. R. Berdiyorov"
  - "M. Neek-Amal"
  - "F. M. Peeters"
  - "Adri C. T. van Duin"
venue: "Phys. Rev. B"
pdf_sha256: "d646005b9857cfa5634e5b2978eca4778f2c3153f0f4286b4c40b3ae36712edc"
pdf_path: "papers/Berdiyorov_graph_silicene_PRB_proof_2014.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2014berdiyorov-venue-paper-2 -->

## Evidence and attribution

!!! note "Proof duplicate"

    **`[[2014berdiyorov-venue-paper]]`** carries the **version-of-record** PDF preferred for figures. This slug records the **proof** file `papers/Berdiyorov_graph_silicene_PRB_proof_2014.pdf`.

## Summary

ReaxFF molecular dynamics with DFTB cross-checks examines silicon intercalated between bilayer graphene. The authors argue that van der Waals confinement stabilizes planar silicon clusters that would be high-energy in vacuum, while larger silicon aggregates adopt buckled honeycomb silicene-like order weakly bound to graphene. Higher temperatures drive silicon toward sp³-bonded three-dimensional precipitates between the sheets. The narrative matches the primary Phys. Rev. B entry; this page documents alternate PDF bytes.

## Methods

ReaxFF simulations in LAMMPS construct Si/C/H supercells with silicon inserted between graphene layers. One protocol randomizes isolated silicon positions and ramps temperature at 20 K ps⁻¹ from 0 to 2000 K; another equilibrates then heats to 2000 K at 4 K ps⁻¹ under NPT with Nosé–Hoover thermostat and barostat, followed by 500 ps at target temperature to assess thermal stability of silicon motifs. DFTB molecular dynamics provides independent checks of structural outcomes, especially silicene-like versus three-dimensional silicon.

The bilayer graphene scaffold supplies van der Waals confinement without covalent Si–C bonds in the initial setup, isolating how interlayer spacing templates silicon clustering versus vacuum-like evaporation to bulk silicon droplets.

**1 — MD application (atomistic dynamics).** Same **LAMMPS/ReaxFF** and **DFTB/MD** narrative as [[2014berdiyorov-venue-paper]]: **Si/C/H** supercells with silicon between **bilayer graphene** layers; **ramp** protocols (**20 K/ps** to **2000 K**; **NPT** path at **4 K/ps** with **Nosé–Hoover** controls then **500 ps** holds) and **3D PBC** sandwich cells are given in the **Phys. Rev. B** article. **Timestep and full lattice metrics:** **N/A — not duplicated** on this proof-ingest stub—use the **version-of-record** PDF linked from the primary slug.

**2 — Force-field training:** **N/A —** same as primary entry (applies literature **ReaxFF**, not a new fit here).

## Findings

Confinement between graphene sheets stabilizes planar or lightly buckled silicon clusters not favored in isolation, with honeycomb silicene-like order persisting above room temperature in the reported trajectories. Elevated temperature converts silicon toward sp³-bonded precipitates, consistent with thermally activated escape from metastable two-dimensional arrangements. Quantitative barriers should be taken from the version-of-record PDF because proof typography can differ.

The published discussion also links confined silicon motifs to epitaxial graphene on SiC and broader hydrogen-storage speculation, positioning the simulations as exploratory hypotheses about metastable 2D silicon rather than quantitative process models.

## Limitations

ReaxFF Si–C parameter accuracy limits quantitative barriers; proof PDF may contain placeholder page headers—cite DOI [10.1103/PhysRevB.89.024107](https://doi.org/10.1103/PhysRevB.89.024107) using the clean file when possible.

## Corpus notes

If automated manifest tooling ever merges duplicate Phys. Rev. B PDFs, keep this slug’s `pdf_sha256` aligned with `scripts/sync_wiki_paper_frontmatter.py` outputs so drift between proof and VOR does not confuse retrieval indexes.

DFTB cross-checks in the article are there because ReaxFF Si–C energetics can be sensitive; when updating this page, preserve the explicit statement that DFTB is a secondary validator, not the primary production driver for large-scale MD.

## Relevance to group

Ingest bookkeeping for van Duin co-authored **silicon–graphene** reactive modeling.

## Citations and evidence anchors

- DOI: [10.1103/PhysRevB.89.024107](https://doi.org/10.1103/PhysRevB.89.024107)

## Related topics

- [[2014berdiyorov-venue-paper]]
- [[reaxff-family]]
