---
id: paper:2011cranford-venue-paper
type: paper
title: "Mechanical properties of graphyne"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2011.05.024"
year: 2011
authors:
  - "Steven W. Cranford"
  - "Markus J. Buehler"
venue: "Carbon 49 (2011), 4111–4121"
pdf_sha256: "1d43fb22608e6606c34db2a7ac10c6b4e42460087b9bcfd7c41a8a94a037bc23"
pdf_path: "papers/ReaxFF_others/Cranford_Buehler__Graphyne_Carbon_2011.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2011cranford-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Mechanical ranges (**48.2–107.5 GPa**, strains **8.2–13.2%**) are taken from the **abstract** as printed.

## Summary

The paper uses **ReaxFF molecular dynamics** to characterize **single-layer graphyne** mechanics: in-plane **elastic and failure** behavior, **bending**, and **intersheet adhesion**. Graphyne is described as a **2D sp–sp\(^2\)** carbon network related to graphene; the abstract reports **strong directional dependence** of fracture stress/strain due to alignment with **acetylenic** linkages, with fracture stresses **48.2–107.5 GPa** and ultimate strains **8.2–13.2%** across loading directions. Despite **half the density** of graphene, **intersheet adhesion** and **bending stiffness** are said to be **comparable** to graphene; the sparser lattice yields **nonlinear** stress–strain behavior and directional **stiffening** effects.

## Methods


**ReaxFF molecular dynamics** is used to characterize **single-layer graphyne** under **adhesion**, **in-plane tension**, and **bending** deformation, including **failure** (abstract + start of Sec. 2 in the local extract). The methodology section describes a **~100 Å \(\times\) 100 Å** **H-terminated** sheet (finite specimen motivated by precursor-scale synthesis), **ReaxFF** for **C–C** interactions, and—importantly—a **finite-size / non-periodic** in-plane boundary choice for the tensile tests as motivated in the text. **N/A —** full **LAMMPS input details**, **timestep**, **thermostat time constants**, **production lengths**, and **complete adhesion/bending protocols** are **not contained** in `normalized/extracts/2011cranford-venue-paper_p1-2.txt` (the extract ends early in Sec. 2); the **Carbon** PDF at `pdf_path` is required for executable settings.

**Prior curation note (PDF-derived details not in `_p1-2` extract).** Earlier wiki text recorded **LAMMPS**, **NVT** at **10 K** for small-strain tests, **Berendsen** thermostat with **0.2 fs** timestep derived from stated damping/step counts, **0.5 ns** equilibration at **300 K**, **~1900 C atoms**, **non-periodic** tensile constraints, and **virial stress** post-processing with an **effective thickness ~3.20 Å**—treat these as **PDF-grounded** operator notes, **not** reproduced by the short extract file.

**2 — Force-field training.** **N/A —** parameter derivation is not the focus of the indexed excerpt (application paper using ReaxFF).

**3 — Static QM / DFT.** **N/A —** not positioned as the primary engine in the excerpted methodology opening.

**Checklist closure (indexed pages).** **Pressure / stress:** mechanical tests report **virial stress**/**stress–strain** constructs in the PDF; **N/A — hydrostatic pressure** (**NPT**) control is not discussed on the indexed excerpt pages.

## Findings

**Mechanical anisotropy (abstract).** **Fracture stress** and **strain** depend **strongly** on direction relative to **acetylenic** linkages, with reported ranges **48.2–107.5 GPa** and **8.2–13.2%** ultimate strain across loading orientations.

**Nonlinearity and directional stiffening.** The abstract highlights **nonlinear stress–strain** and **internal stiffening** tied to **acetylenic** alignment under load (contrasted with more **isotropic** graphene-like small-strain behavior in the narrative).

**Intersheet adhesion / bending vs density.** Despite **half** the **areal density** of graphene, **intersheet adhesion** and **out-of-plane bending stiffness** are reported **comparable** to graphene in the abstract framing.

**Comparisons / limitations.** The introduction notes **large homogeneous graphyne sheets** were **not experimentally available** at publication, motivating modeling of **DBA-like** finite segments; treat quantitative **223.5 mJ/m\(^2\)** adhesion and detailed **tangent-modulus** claims as **PDF-sourced** (not re-proven by the `_p1-2` excerpt).

**Corpus honesty.** `extraction_quality` is **partial**; stress–strain curves and failure morphologies are in **`pdf_path`**, not the short extract.

## Limitations

Large homogeneous graphyne sheets with long-range order were not available experimentally at publication; models idealize periodic defect-free sheets. `extraction_quality` is **partial**; stress–strain curves and failure morphologies are in the PDF.

## Relevance to group

Direct **ReaxFF** application to **exotic carbon allotropes**—useful link for **nanocarbon** retrieval alongside graphene-related pages.

## Citations and evidence anchors

- DOI: `10.1016/j.carbon.2011.05.024`.
- PDF: `papers/ReaxFF_others/Cranford_Buehler__Graphyne_Carbon_2011.pdf`.
- Extract: `normalized/extracts/2011cranford-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
