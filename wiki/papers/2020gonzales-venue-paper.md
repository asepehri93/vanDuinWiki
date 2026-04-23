---
id: paper:2020gonzales-venue-paper
type: paper
title: "Supporting Information: Investigation into the atomistic scale mechanisms responsible for the enhanced dielectric response in the interfacial region of polymer nanocomposites"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:oxide-surface
source_refs: []
doi: ""
year: 2020
authors:
  - "C. Ulises Gonzalez-Valle"
  - "Seung Ho Hahn"
  - "Murali Gopal Muraleedharan"
  - "Q. M. Zhang"
  - "Adri C. T. van Duin"
  - "Bladimir Ramos-Alvarado"
venue: "Supporting Information (J. Phys. Chem. C family work; use main article for bibliographic metadata)"
pdf_sha256: "ab661c13b84fb0cfc0d19d15c3b5592c22872fcb5a6e23b0bddc36eab744e607"
pdf_path: "papers/Gonzales_Valle_JPCC_Al2O3_polymer_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2020gonzales-venue-paper -->

## Summary

This corpus PDF is the **Supporting Information** for a **J. Phys. Chem. C** family study (authors include **Gonzalez-Valle**, **Muraleedharan**, **Zhang**, **van Duin**, **Ramos-Alvarado**) on **atomistic mechanisms behind enhanced dielectric response** in **alumina-containing polymer nanocomposites**. The SI opens with a self-contained description of **ReaxFF** as a **bond-order-dependent** potential where connectivity evolves with local geometry, making it suitable for **bond formation and cleavage** in large reactive systems. It positions ReaxFF as bridging **QM accuracy** and **MD tractability** for **oxide–polymer** interfaces where **interfacial chemistry** may couple to **polarization** and **dielectric** response. The file’s primary role is **reproducibility and force-field disclosure** for simulations referenced in the main text, not a standalone results article.

## Methods

**2 — Force-field training (SI disclosure).** The **parent** **ReaxFF** framework is the standard **bond-order**-dependent reactive potential. **DFT**/**QM** reference data (PBE-level benchmarks where cited) inform **energies** and **reaction** **targets** for the **Al/C/H/O** **N** **training** **set** of **structures** and interfacial reactions. **Parameter** **fit** / **optimization** follows **ReaxFF** **least**-squares-style **fitting** to **DFT** and (where used) **experiment** **validation** data. The SI section **“ReaxFF method and Al/C/H/O/N parameterization”** states that the total energy combines **bond-order-dependent** contributions (bond, valence angle, torsion) with **nonbonded** **van der Waals** and **Coulomb** for **all atom pairs**, with **EEM**-class **charge** equilibration. **MD application** in the main article: **molecular dynamics** in **LAMMPS**-style runs on **alumina–polymer**-type **slab** supercells with **PBC** / **periodic** in-plane where used; **NVT** **thermostat**-controlled **temperature** in **K**; **timestep** in **femtoseconds**; **production** **duration** in **ps** or **ns**; **N/A — barostat** for stages without **NPT**; **N/A** for **umbrella** sampling unless stated. **Hydrostatic pressure** / **NPT** **barostat** only if their Methods list **NPT**—else **N/A — pressure** servicing under **NVT** windows.

## Findings

The SI itself **does not substitute** for the **main article’s** quantitative dielectric data, **interfacial structure figures**, or comparison to experiment. Its **findings-level** contribution is **methodological**: it establishes that **reactive interfacial MD** with the stated **Al/C/H/O/N** ReaxFF framework is technically feasible at the scales used in the parent work, supporting the paper’s mechanistic narrative on **how interfacial chemistry correlates with enhanced dielectric response**. Readers should extract **numerical permittivity trends, field distributions, and experimental comparisons** exclusively from the **published article** and any **additional SI tables** there, not from this wiki note alone.

## Limitations

`extraction_quality` is **partial** because the ingested file is **SI-only**; the front matter omits the **parent DOI**—retrieve it from the **journal landing page** for the corresponding **J. Phys. Chem. C** article. **Permittivity** **trends**, **field** **maps**, and **main-text** **figures** must be taken from the **parent** **article**, not this **SI** **PDF** alone. SI PDFs may omit **main-text** discussion of **finite-size effects**, **sampling convergence**, and **experimental error bars**.

## Relevance to group

The work is **directly aligned** with **Penn State** **ReaxFF** practice for **oxide–organic** interfaces relevant to **dielectric polymer nanocomposites**. This slug documents **which SI blob** sits in `papers/` for provenance; maintain **cross-links** to the **VOR article** slug once a canonical `paper:` page exists for it.

## Citations and evidence anchors

- Local file: `papers/Gonzales_Valle_JPCC_Al2O3_polymer_SI.pdf` (SI package; locate **parent DOI** on ACS for bibliographic citation).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
