---
id: paper:2015hong-venue-research-2
type: paper
title: "Molecular dynamics simulations of the oxidation of aluminum nanoparticles using the ReaxFF reactive force field (ACS proof PDF)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:oxides-ceramics
  - domain:fuel-combustion
  - method:reaxff
  - task:application
  - material:metal-surface
  - scale:atomistic
source_refs: []
doi: "10.1021/acs.jpcc.5b04650"
year: 2015
authors:
  - "Sungwook Hong"
  - "Adri C.T. van Duin"
venue: "Journal of Physical Chemistry C (ACS proof PDF in corpus)"
pdf_sha256: "4bb92ac3034563c946d182205499a61321d54c81d14932a180c6fdc552f1c9e1"
pdf_path: "papers/Hong_AlOx_JPCA_2015_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015hong-venue-research-2 -->

## Summary

This slug registers an **ACS proof** PDF (`papers/Hong_AlOx_JPCA_2015_proof.pdf`) for the same **Hong–van Duin** *J. Phys. Chem. C* article documented on [[2015hong-venue-research]] (DOI `10.1021/acs.jpcc.5b04650`). The scientific narrative matches the published study: **ReaxFF MD** of **aluminium nanoparticle** oxidation at **300, 500, and 900 K** with initial **O\(_2\)** densities **0.13** and **0.26 g cm\(^{-3}\)**, analyzing **hot spots**, **void** formation, **accelerated oxygen transport** in the developing **oxide**, and trends in **oxide thickness/density** with **temperature** and **oxygen availability**. For **pagination**, **SI** pointers, and corpus `pdf_sha256` hygiene, prefer the **ASAP / issue-of-record** PDF tracked on [[2015hong-venue-research]] unless you intentionally need this proof artifact.

## Methods

This slug is an **ACS proof** PDF for the same Hong–van Duin *J. Phys. Chem. C* manuscript as [[2015hong-venue-research]] (DOI `10.1021/acs.jpcc.5b04650`). The proof does **not** define a separate computational study: **ReaxFF** reactive **MD** in **LAMMPS**, **3D PBC** gas–metal cells, **864-atom** amorphous **Al** nanoparticles versus **504-atom** **Al(431)** slab validation setups, **NVT** production at **300–900 K** with a **Nosé–Hoover** thermostat (**100 fs** damping), **Δt = 0.2 fs**, **1 ns** (5×10⁶ steps) trajectories, and initial **O\(_2\)** densities **0.13** and **0.26 g cm\(^{-3}\)** (plus the **NVE** low-density control described on the sibling page) are all reported there. **Force-field training / standalone static QM for this work:** **N/A —** established **Al/O ReaxFF** with validation against **slab** oxidation trends as on [[2015hong-venue-research]]. **Barostat / NPT:** **N/A —** primary nanoparticle runs are **constant-volume NVT**; **pressure** control is not used for those production segments.

## Findings

The proof-stage PDF carries the same scientific conclusions as the issued article: **exothermic** early **O\(_2\)** consumption, **localized heating**, **void**-rich metal/oxide regions, **barrier** trends from the authors’ **bond-restraint** diffusion scans (**void** configurations lowering the modeled barrier by up to **~92%** in their setup), and **temperature** / **oxygen availability** effects on **oxide** thickness and density, with **qualitative** comparison to selected **experimental** references. **Pagination and figure callouts** should be taken from the **version-of-record** PDF on [[2015hong-venue-research]] (or the publisher download for the DOI), not from this proof layout.

## Limitations

- **Proof** PDFs can include **layout** differences versus the **final** **JPCC** issue; cite the **publisher** **PDF** for authoritative **pagination**, **scheme** numbering, and any **Supporting Information** pointers that moved between proof and issue.
- Separate **manifest** rows preserve **SHA-256** integrity between **proof** and **ASAP** uploads so automated provenance checks remain unambiguous even when both files coexist in `papers/`.

## Relevance to group

Duplicate PDF lineage for the same research product; keep both when collaborators archive different submission stages.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1021/acs.jpcc.5b04650](https://doi.org/10.1021/acs.jpcc.5b04650)

## Related topics

- [[reaxff-family]]
