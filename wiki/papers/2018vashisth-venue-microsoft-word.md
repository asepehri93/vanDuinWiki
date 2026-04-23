---
id: paper:2018vashisth-venue-microsoft-word
type: paper
title: 'Supporting Information: Accelerated ReaxFF simulations for epoxy cross-linking
  (parameter tables)'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:organics-polymers-pyrolysis
- domain:reaxff-lineage
- material:polymer-organic
- method:reaxff
- scale:atomistic
- task:method-development
paper_keywords:
- keyword:supporting-information
- keyword:reaxff-parameterization
- keyword:polymer
- keyword:lammps
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpca.8b03826
year: 2018
authors:
- Aniruddh Vashisth
- Chowdhury Ashraf
- Weiwei Zhang
- Charles E. Bakis
- Adri C. T. van Duin
venue: J. Phys. Chem. A — Supporting Information
pdf_sha256: 3f210692bd0a5d06b618cc8f35f5ecf51d8961a0e93f8165038bbfb56c8dd00d
pdf_path: papers/Vashisth_JPC_bondboost_2018_SI.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018vashisth-venue-microsoft-word -->

## Evidence and attribution

!!! note "Authority of statements"

    This PDF is the **Supporting Information** for [[2018vashisth-j-phys-chem-accelerated-reaxff]].

!!! abstract "Corpus role"

**Supporting Information** for **`[[2018vashisth-j-phys-chem-accelerated-reaxff]]`**: **full ReaxFF** parameter listings and ancillary numerical material; the **article** states methods, barriers, and properties.

## Summary

This Supporting Information PDF publishes the complete ReaxFF parameter listings used in the *Journal of Physical Chemistry A* article on accelerated epoxy–amine curing for a bisphenol-F diglycidyl ether (bis-F) and DETDA formulation, refined from the CHNO-2017_weak baseline to reproduce quantum-mechanical reaction barriers while also matching experimental density, glass transition temperature, and elastic modulus trends. The corpus treats the document as the bitwise companion to the main article: anyone reproducing the published LAMMPS decks should copy parameter blocks directly from these tables to avoid transcription drift between comma-delimited fields and LAMMPS input syntax. The tables include general and bonded terms exactly as read into LAMMPS for the published workflows, together with ancillary numerical material such as force-parameter scan data and documentation for tracking and post-processing steps associated with quantum-mechanical transition-state cleanup. Interpretive discussion of cure kinetics, mechanical property validation, and bond-boost acceleration strategies remains on **`[[2018vashisth-j-phys-chem-accelerated-reaxff]]`**; this file is the numerical appendix for reproducibility.

## Methods

This file is **Supporting Information** for **`[[2018vashisth-j-phys-chem-accelerated-reaxff]]`**: its role is **tabular reproduction** of the **ReaxFF** parameter set and ancillary numerical inputs used in **LAMMPS**. **Interpretation** of cure kinetics, **QM** benchmarks, **accelerated MD** logic, and **mechanical** validation narratives stay on the **main article** page.

### Force-field provenance (SI scope)

- **Parent parameterization / elements:** Tables extend the **CHNO-2017_weak**-class **ReaxFF** description for **bis-F / DETDA** epoxy chemistry (**C/H/N/O** reactive interactions); copy **bond**, **angle**, **off-diagonal**, and **charge** blocks directly from this PDF when building inputs.
- **QM reference data:** The **J. Phys. Chem. A** article documents **QM transition states** and barrier targets used to reweight **epoxide–amine** interactions; the SI lists the resulting **ReaxFF** numbers rather than re-deriving **DFT** settings here.
- **Training / fitting targets:** **Bond dissociation**, **angle distortion**, and **reaction-energy** points for **C–O / C–N / N–H** motifs appear in the SI tables as fitted objectives mirroring the article’s **QM** comparison set.
- **Optimization workflow:** Parameter **adjustments** follow the **least-squares / ReaxFF** optimization conventions described in the primary text; the SI is not a standalone optimizer log—use the article + these tables together.
- **Experimental validation hooks:** **Density**, **\(T_g\)**, and **tensile modulus** comparisons to **dogbone** experiments are summarized in the **issue PDF**; the SI supplies the **force-field** side of that pipeline.

### MD protocol pointers (defer to main text)

Production **LAMMPS** settings referenced across the article/SI pair include **0.25 fs** integration for **\(T_g\)** sweeps, alternating **NVT** / **NPT** densification, and **high strain-rate** tensile deformation for **modulus** (`[[2018vashisth-j-phys-chem-accelerated-reaxff]]`). **Barostat / thermostat** damping values and full **production** segment lengths in **ps** are enumerated in the **Methods** of the main paper rather than duplicated in every SI table caption.

### MD application (SI document scope)

This **Supporting Information** file does **not** define standalone **MD** cells; the bullets below document **what is / is not** in this PDF for operators reproducing **LAMMPS** inputs.

- **Engine / code:** **LAMMPS**-formatted **ReaxFF** parameter tables (bond/angle/off-diagonal/charge blocks) meant to pair with the issue **Methods** in **`[[2018vashisth-j-phys-chem-accelerated-reaxff]]`**.
- **System size & composition:** **N/A —** **atom** budgets and **molecule** counts are staged in the **main article**; this **SI** is **tabular** **force-field** data only.
- **Boundaries / periodicity:** **N/A —** **PBC** choices and supercell vectors are **not** re-derived here—copy the **periodic** **LAMMPS** cell setup from the primary **Methods** when building decks from these tables.
- **Ensemble / timestep / duration:** **N/A —** **NVT**/**NPT** staging, **timestep** choices, and **ps/ns** segment lengths are specified in the **JPC A** article text, not in every **SI** caption.
- **Thermostat / barostat:** **N/A —** algorithm labels and damping constants are given in the **main** **Methods**; the **SI** focuses on **ReaxFF** numbers consumed by those controls.
- **Temperature / pressure targets:** **N/A —** set-point **temperature**/**pressure** schedules for production **MD** are **not** tabulated as standalone **thermal** protocols in this **SI** file—use the issue **PDF** for **300–600 K** annealing ladders, **\(T_g\)** sweeps, and **NPT** densification windows referenced there.
- **Electric field / replica / metadynamics:** **N/A — not part** of this **SI** (electrostatics follow standard **ReaxFF/QEq** conventions in the supplied **LAMMPS** decks; acceleration uses **restraints** per the article).
## Findings

The SI underpins the main manuscript’s claims of QM agreement for key elementary reactions, an illustrative trajectory reaching roughly 82% cross-linking, and consistent density, \(T_g\), and modulus behavior relative to laboratory measurements—those headline results should be cited from the issue PDF, not abstracted independently from the SI tables.

## Limitations

Parameters are specific to the bis-F/DETDA chemistry and the accelerated-curing workflow; extending them to other epoxies or curing agents requires independent validation. Any discrepancy between proof and issue layouts should be resolved against the publisher version when assigning page-level locators.

## Relevance to group

The SI is the bitwise reference for van Duin-group epoxy ReaxFF parameter tables tied to accelerated reactive curing benchmarks, supporting MAS pipelines that ingest publication-specific force fields.

## Reader notes (navigation)

- Main article: [[2018vashisth-j-phys-chem-accelerated-reaxff]]
- Related corpus proof: [[2018vashisth-venue-paper]]

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.8b03826](https://doi.org/10.1021/acs.jpca.8b03826)

## MAS / retrieval notes

Parameter ingestion should use machine-readable tables from this SI; cite **`[[2018vashisth-j-phys-chem-accelerated-reaxff]]`** for tensile and \(T_g\) validation narratives. Bond-boost and restraint keywords in the main text map to supplemental paragraphs here—do not infer barrier heights without QM references listed in the primary article.

## Related topics

- [[reaxff-family]]
