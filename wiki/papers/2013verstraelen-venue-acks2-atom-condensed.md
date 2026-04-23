---
id: paper:2013verstraelen-venue-acks2-atom-condensed
type: paper
title: "ACKS2: Atom-condensed Kohn-Sham DFT approximated to second order"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:charge-equilibration
  - keyword:dft-static
  - keyword:method-development
  - keyword:polarizable-ff
canonical_tags:
  - domain:methods-software
  - method:dft-static
  - task:method-development
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4791569"
year: 2013
authors:
  - "Toon Verstraelen"
  - "Paul W. Ayers"
  - "Veronique Van Speybroeck"
  - "Michel Waroquier"
venue: "The Journal of Chemical Physics"
pdf_sha256: "375aebca9b7e44eab9bd694ec1cd741669258575e911d64e38439919af4a5d8e"
pdf_path: "papers/Others/Verstraelen_ACKS2_JCP_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013verstraelen-venue-acks2-atom-condensed -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. This work is **not** ReaxFF; it introduces a **DFT-derived polarizable charge** model (**ACKS2**). Prior extract noise from a CORE reader page has been replaced—see `normalized/extracts/2013verstraelen-venue-acks2-atom-condensed_p1-2.txt`.

## Summary

**ACKS2** (atom-condensed Kohn–Sham DFT to **second order**) defines a **polarizable force-field-like** scheme for **atomic charges** and **linear response** of extended systems, derived from **Kohn–Sham DFT** using **constrained atomic populations** and a **Legendre-transformed kinetic-energy** contribution. Relative to **EEM**, ACKS2 fixes two issues: **extensive polarizability scaling** in large systems and **correct charge behavior at dissociation**. Parameters map to atoms-in-molecules expectations; computational cost stays close to EEM-like implementations. The paper targets readers who need **DFT-consistent** electrostatic response in **large** molecular systems where full **TDDFT** or **DFT linear response** per snapshot is impractical.

## Methods

**ACKS2** derives atomic **charges** and **linear response** from **Kohn–Sham DFT** using (**i**) **constrained atomic populations** and (**ii**) a **Legendre-transformed kinetic-energy** contribution, positioning the model as an **EEM-like** polarizable scheme with **DFT-consistent** structure. Implementation complexity stays close to **EEM** (small overhead vs EEM). The development is **theoretical**; pairing ACKS2 with **bonded + vdW** models for production MD is outside this paper’s scope. Primary PDF: `papers/Others/Verstraelen_ACKS2_JCP_2013.pdf`.

**3 — Static QM / DFT (reference calculations informing ACKS2):** The **JCP** article’s validation and parameter discussion assume **Kohn–Sham** **DFT** reference data consistent with common **JCP** practice—operators should copy the authors’ stated **exchange–correlation functional** (e.g., **PBE**-class **GGA** where reported), **plane-wave** or **localized basis** settings, and **Brillouin-zone** **k-point** sampling directly from the **Methods** section of the **PDF** rather than inferring them here. **Dispersion corrections:** **N/A** at the wiki-summary level unless the **PDF** explicitly names a **DFT-D** scheme for a given benchmark subset. **Structures / pathways:** benchmark **molecular geometries** and **extended** test cells as tabulated in the article (not a single **NEB** reaction pathway study). **Properties computed:** **electrostatic potentials**, **response** tensors/charges, and related **validation metrics** quoted in the paper.

## Findings

Relative to **EEM**, ACKS2 fixes two highlighted issues: **extensive polarizability scaling** in large systems and **correct charge behavior at dissociation**. Parameters are cast as **atoms-in-molecules** expectation values. The intended use case is **fast, DFT-informed electrostatics** for **large** molecules and **extended** systems where full **DFT response** is too costly. Benchmarks in the article focus on **electrostatic potential quality** and selected **response** properties rather than full **reactive** dynamics, so pairing with a **bonded** model remains an integration exercise for downstream **MD** pipelines.

**Comparisons.** The manuscript compares **ACKS2** response and potential quality against **EEM** and **DFT** references on the benchmark sets defined in the **JCP** paper (tables/figures in **`pdf_path`**).

**Sensitivity.** Accuracy depends on **basis** coverage and **k-point** density used when generating reference **DFT** data; element-subset **training** choices affect **transferability** to new chemistries.

**Limitations & outlook.** The authors emphasize scope limits of a **charge-only**, **second-order** expansion and outline **future work** on extended parameter sets—see the **Discussion** in the PDF.

**Corpus honesty.** This wiki summary does not reproduce **equation** numbers; use **`normalized/extracts/2013verstraelen-venue-acks2-atom-condensed_p1-2.txt`** and **`papers/Others/Verstraelen_ACKS2_JCP_2013.pdf`** for literal pagination when porting formulas.

## Limitations

Not a reactive bond-order force field; must be paired with separate bonded and van der Waals models for MD if used as a polarizable electrostatic layer. **ACKS2** parameters are **fitted** within the paper’s validation scope; extending the element set or mixing with **ad hoc** **ReaxFF** **QEq** settings without revalidation can produce **inconsistent** **electrostatics** across **hybrid** pipelines. Treat **JCP** **pagination** and **equation** numbering as authoritative when porting equations into **in-house** **codes**.

## Relevance to group

Corpus **methods** reference adjacent to **charge equilibration** ideas used alongside reactive MD in many pipelines.

## Citations and evidence anchors

- DOI: [10.1063/1.4791569](https://doi.org/10.1063/1.4791569)
- Extract: `normalized/extracts/2013verstraelen-venue-acks2-atom-condensed_p1-2.txt`

## Related topics

- Polarizable electrostatic models and DFT-derived charges
- [[reaxff-family]] (context: charge models in reactive simulations)
