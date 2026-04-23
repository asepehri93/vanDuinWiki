---
id: paper:2014m-ffield-valega-thijsse-2014-pdf
type: paper
title: "ReaxFF parameter tables: alumina / epoxy (N–Al) (Valega & Thijsse; supporting parameter file)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - material:oxide
  - material:polymer-organic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:neb
  - keyword:oxide-surface
  - keyword:polymer
  - keyword:supporting-information
candidate_tags: []
source_refs: []
doi: "10.1021/jp5105328"
year: 2015
authors:
  - "F. O. Valega Mackenzie"
  - "B. J. Thijsse"
venue: "J. Phys. Chem. C (parameterization reported; SI-style file in corpus)"
pdf_sha256: "54db07ac27fb6f011585e4e6810527764cdd37ad0253ec08f7eca4434654116e"
pdf_path: "papers/ReaxFF_others/Valega_Thijsse_JPC_C_2015_epoxide_amine_alumina_SI_force_field.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014m-ffield-valega-thijsse-2014-pdf -->

## Evidence and attribution

!!! note "Authority of statements"

    This corpus entry is primarily a **ReaxFF parameter listing** (numerical coefficients). The scientific description of the fit appears in the **peer-reviewed J. Phys. Chem. C** article **10.1021/jp5105328** (Valega Mackenzie & Thijsse). Use that paper for **validation claims**; this page documents **what the file is**.

## Summary

**Reactive force field** parameter set for **aluminum–nitrogen** interactions aimed at **epoxy–amine** chemistry on **alumina** surfaces, combined with prior **Al–O / organics** ReaxFF building blocks. The associated journal work develops the parametrization against **DFT** clusters and **NEB** reaction paths for **amine-containing epoxy precursors** on **alumina** and discusses **adhesion vs. hydroxyl coverage**. This wiki slug primarily documents the **coefficient listing** PDF path so pipelines can attach **consistent** **N–Al** parameters when building **metal–oxide–polymer** interfaces in **LAMMPS**.

## Methods

### What this corpus file is

`papers/ReaxFF_others/Valega_Thijsse_JPC_C_2015_epoxide_amine_alumina_SI_force_field.pdf` is primarily a **tabular ReaxFF coefficient listing** (header: “Reactive MD-force field: Alumina/Epoxy(N-Al)…”). A mechanical extract exists at `normalized/extracts/2014m-ffield-valega-thijsse-2014-pdf_p1-2.txt` (numerical parameters only).

### 1 — MD application (atomistic dynamics)

Production **molecular dynamics** protocols are **not** specified in the coefficient table. For this slug: **N/A — not in the parameter file**; use **J. Phys. Chem. C** **10.1021/jp5105328** for application setups (typical downstream engine: **LAMMPS** with **ReaxFF**, per that article’s context).

- **System size & composition:** **N/A — not specified** in this artifact (atom counts and **supercell** choices belong to application studies).
- **Boundaries / periodicity:** **N/A — periodic boundary conditions (PBC)** choices are not encoded in the parameter table; define **PBC** when building the **slab** or **bulk** cell in **LAMMPS**.
- **Ensemble:** **N/A — NVT**/**NPT** settings are not in the coefficient dump; copy from the **primary article** when reproducing published **MD**.
- **Timestep / duration / thermostat / barostat / temperature / pressure / electric field / enhanced sampling:** **N/A — not specified** in this artifact.

### 2 — Force-field training (authored fit; cite the journal article)

The **primary publication** documents **ReaxFF** development for **alumina–amine** (**epoxy**) **adhesion**, including **DFT** cluster data and **NEB** pathways versus **hydroxyl coverage** (full **QM** settings, **training** scope, and **optimization** workflow: **10.1021/jp5105328**).

- **Parent FF / elements:** **ReaxFF** extension for **N–Al** with **C/H/O/N/Al** blocks in the listing; merge with compatible **Al/O/C/H** libraries as described in the **article**/**SI**.
- **QM reference / training set / optimization / external reference data:** **N/A — not duplicated numerically** on this wiki page—read the **peer-reviewed** **PDF**/**SI**.

### 3 — Static QM / DFT-only

**N/A —** this ingest is not a standalone **DFT** methods note; static **QM** content is in **10.1021/jp5105328**.

### Operator note (safe reuse)

Combine this **N–Al** block only with **consistent** element coverage and **non-overlapping** interaction definitions; verify **LAMMPS** **pair_style** settings to avoid **double counting** adjacent libraries.

## Findings

### Outcomes and mechanisms

The **tabular file** does not report new **reaction** or **interface** **mechanisms** by itself; it supplies **parameters** for **ReaxFF** simulations of **epoxy–amine** chemistry on **alumina** when merged with consistent **Al/O/C/H/N** blocks.

### Comparisons and sensitivity

**Adhesion** trends versus **hydroxyl coverage** and **NEB**-based energetics are **authored findings** in **10.1021/jp5105328**—cite that **article** for **benchmark** and **experimental** comparisons, not this coefficient PDF.

### Corpus / KB honesty

This slug is **SI-style** corpus provenance; **`normalized/extracts/2014m-ffield-valega-thijsse-2014-pdf_p1-2.txt`** supports checksum-style review of coefficients, not replacement for the journal **Methods**/**Results** text.

## Limitations

Ingest is a **coefficient dump**; **year** in slug (`2014`) predates the **2015 JPCC** article—front matter uses **publication year 2015** for the linked DOI. When combining this **N–Al** block with other **ReaxFF** **libraries**, verify **element** **coverage** and **exclusion** **rules** in **LAMMPS** **pair** **styles** to avoid **double-counting** **interactions** already embedded in **adjacent** **parameter** **files**. **Epoxy** **cure** **kinetics** depend on **temperature** **schedules** not represented in **static** **QM** **reaction** **paths**; use **large-scale** **MD** only with **experimentally** **informed** **thermal** **histories**. **Alumina** **hydroxyl** **density** should match **substrate** **preparation** when comparing **adhesion** **simulations** to **experiments**.

## Relevance to group

**Polymer–oxide adhesion** and **ReaxFF parameterization** adjacent to the group’s **oxide / interface** portfolio; useful as a **reference parameter lineage** for epoxy–alumina simulations.

## Citations and evidence anchors

- https://doi.org/10.1021/jp5105328 — “Study of Metal/Epoxy Interfaces … Using a Newly Developed Reactive Force Field for Alumina–Amine Adhesion.”
- **SI-style coefficient file:** maintainer context for **supporting-information**-like PDF roles: [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
