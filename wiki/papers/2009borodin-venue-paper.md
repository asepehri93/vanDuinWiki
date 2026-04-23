---
id: paper:2009borodin-venue-paper
type: paper
title: "Polarizable force field development and molecular dynamics simulations of ionic liquids"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:polarizable-ff
  - keyword:classical-ff
  - keyword:batteries-interfaces
  - keyword:validation-experiment
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:classical-ff-specialized
  - method:classical-md
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp905220k"
year: 2009
authors:
  - "Oleg Borodin"
venue: "Journal of Physical Chemistry B 113 (33), 11463–11478 (2009)"
pdf_sha256: "833af7b0a3083e888c7494f5c1deb15ca298485ab714f4223fcae56fda9b772f"
pdf_path: "papers/Others/Borodin_IL_polarizable.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2009borodin-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose follows the **abstract** and introduction in the extract. Counts such as “30 ionic liquids” and temperatures **298, 333, 393 K** are taken from the abstract text.

## Summary

The paper develops a **many-body polarizable force field** for a broad family of **ionic liquid** cations and anions (listed in the abstract), then performs **classical MD** on **30 ionic liquids** at **298, 333, and 393 K**. Reported validations include **density**, **heat of vaporization**, **ion self-diffusion**, **conductivity**, and **viscosity** vs. experiment, plus tests of **crystal cell parameters** for four **ionic crystals** with **TFSI\(^-\)** anions. For **[emim][BF\(_4\)]**, turning **polarization off** changes structure and **slows** ion dynamics, linking polarization to transport.

## Methods


The authors develop a **many-body polarizable force field** covering a broad library of room-temperature ionic liquid **cations and anions** (listed explicitly in the abstract: imidazolium, pyrrolidinium, pyridinium, piperidinium, morpholinium, tetraalkylammonium/phosphonium, oligoether-functionalized cations, and anions including BF\(_4^-\), fluoroborates, triflate, PF\(_6^-\), dicyanamide, tricyanomethanide, tetracyanoborate, TFSI\(^-\), FSI\(^-\), nitrate). **Classical molecular dynamics** simulations are reported for **30 ionic liquids** at **298 K, 333 K, and 393 K**, with properties compared to **experiment** (mass **density**, **heat of vaporization**, **ion self-diffusion**, **conductivity**, **viscosity**). **Crystal cell parameters** for **four ionic crystals** containing **TFSI\(^-\)** are used as an additional test. For **[emim][BF\(_4\)]**, turning **polarization off** versus on probes how **many-body polarizability** couples to **structure** and **ion dynamics**.

**1 — MD application.** **Engine / code:** **N/A —** simulation program name not stated on the indexed pages (`normalized/extracts/2009borodin-venue-paper_p1-2.txt`); verify `papers/Others/Borodin_IL_polarizable.pdf`. **System size & composition / PBC / timestep / thermostat / barostat / trajectory length:** **N/A —** not recoverable from the short local extract; the JPCB PDF is the authority for cell construction and integrator settings. **Temperature:** **298**, **333**, and **393 K** as in the abstract. **Pressure / stress control:** **N/A —** not stated in the excerpt. **Electric field:** **N/A —** not indicated for these IL benchmarks. **Replica / enhanced sampling:** **N/A —** not indicated.

**Checklist closure (indexed pages).** **Ensemble:** **N/A — NVT**/**NPT**/**NVE** not stated in the abstract/excerpt (IL property MD is often **NPT**, but confirm in the PDF). **Duration / stages:** **N/A — equilibration**/**production** trajectory lengths are not quoted on pp. 1–2.

**2 — Force-field training.** The abstract frames a **new polarizable potential** validated broadly against **experiment**; **N/A —** detailed QM reference level (functional/basis), optimizer, and full training-structure inventory are not reproduced in the pages captured by the local extract—see **`pdf_path`**.

## Findings

**Against experiment (abstract-level claims).** The polarizable model is reported to reproduce **available experimental** **densities**, **heats of vaporization**, **ion self-diffusion coefficients**, **conductivities**, and **viscosities** for the **30 ILs** at **298**, **333**, and **393 K**, and to capture **unit-cell** parameters for **four** **TFSI\(^-\)**-containing **ionic crystals**.

**Polarization sensitivity.** For **[emim][BF\(_4\)]**, **disabling polarization** is tied to **structural changes** and **slower ion dynamics**, supporting the abstract’s statement that **many-body polarization** couples to **structure** and **transport**.

**Broader parametrization claims (introduction excerpt).** The introduction notes the developed FF also targets additional **molecular/liquid** chemistries (e.g. **alkanes**, **fluoroalkanes**, **oligoethers**, **carbonates**, **hydrazines**, **acetonitrile**, **amines**, **ketones** as printed); treat those as **in-PDF** scope statements rather than re-derived here.

**Corpus honesty.** `extraction_quality` is **partial**; tables, error bars, and full methods live in **J. Phys. Chem. B** at `pdf_path`.

## Limitations

Classical polarizable force fields are not ReaxFF; reactive chemistry is not sampled unless encoded in predefined functional forms. `extraction_quality` is **partial**; use the **J. Phys. Chem. B** PDF for tables and figures.

## Relevance to group

Electrolyte and **polarization** phenomenology relevant to **battery interface** modeling culture adjacent to **eReaxFF** charge models, though the functional form differs.

## Citations and evidence anchors

- DOI: `10.1021/jp905220k`.
- PDF: `papers/Others/Borodin_IL_polarizable.pdf`.
- Extract: `normalized/extracts/2009borodin-venue-paper_p1-2.txt`.

## Reader notes (navigation)

These sections summarize what the checked-in extraction and abstracts support; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter above. Operators updating chunks should reconcile numbers with `normalized/extracts/` and the version-of-record PDF when available.

## Related topics

- [[batteries-interfaces-reaxff]]
- [[themes-index]]
