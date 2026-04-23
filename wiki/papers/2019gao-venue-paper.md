---
id: paper:2019gao-venue-paper
type: paper
title: "A ReaxFF molecular dynamics study of molecular-level interactions during binder jetting 3D-printing"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:application
  - material:oxide
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:galley-or-proof-pdf
source_refs: []
doi: "10.1039/C9CP03585K"
year: 2019
authors:
  - "Yawei Gao"
  - "Yun Kyung Shin"
  - "Daniel Martinez"
  - "Guha Manogharan"
  - "Adri C. T. van Duin"
venue: "Physical Chemistry Chemical Physics (Accepted Manuscript)"
pdf_sha256: "e8b917fd0291b5cd0e3d5e6a8f0f6d24cf84980e0b5d38dafd20551c22e74f91"
pdf_path: "papers/Gao_PCCP_binder_jetting_3D_printing_accepted.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019gao-venue-paper -->

??? info "PDF role"
    RSC **Accepted Manuscript** PDF (`10.1039/C9CP03585K`). Full simulation parameters, restraint-based breaking-strength workflow, and temperature staging are curated on [[2019gao-physical-che-reaxff-molecular]] with the version-of-record article PDF.

## Summary

The study uses ReaxFF molecular dynamics to represent binder jetting additive manufacturing at atomistic resolution with chromium-oxide nanoparticles and water-based binders containing diethylene glycol (DEG). The abstract states that both DEG and water contribute to particle bonding during print and cure by forming a hydrogen-bond network, that heating to burn-out oxidizes DEG and disrupts that network, and that subsequent sintering partially joins particles through Cr–O bonds with further bonding at a final high-temperature sintering stage. The authors vary binder composition in two series to change the relative numbers of water and DEG molecules, reporting that combining both can increase the number of “useful” hydrogen bonds and raise breaking strength during print and cure. During burn-out and sintering, water’s effect on strength is described as less obvious, while an optimal quantity of binder species exists for strength after sintering. Comparing 2-ethoxyethanol, DEG, and a trihydroxy-rich binder shows that more hydroxyl groups correlate with higher breaking strength in the print and cure stages according to the ReaxFF workflow.

## Methods

The accepted-manuscript extract matches the scientific title and abstract of the PCCP article; detailed protocols—including Cr/C/H/O ReaxFF from Shin et al., NVT staging at 300 K, 393 K, 900 K, and 1900 K, Berendsen thermostat damping, restraint potentials for mechanical separation tests, nanoparticle sizes, and compositional Sets A and B—are documented on [[2019gao-physical-che-reaxff-molecular]] because that page ties to the full article PDF in the corpus. This slug exists for the duplicate ingest of the author-accepted PDF, which may carry RSC boilerplate pages before the article body.

**MD engine (VOR-aligned).** The **PCCP** study runs **ReaxFF molecular dynamics** in **LAMMPS** on **periodic** **supercells** with **Cr-oxide** nanoparticles, **NVT** staging (**300 K**, **393 K**, **900 K**, **1900 K**), **Berendsen** thermostat (**100 fs** damping), and restraint-based separation tests—full tables on [[2019gao-physical-che-reaxff-molecular]] (`pdf_path` there). **Timestep / duration:** **equilibration** and **production** **ps**/**ns** spans and **fs** **timestep** appear in that **VOR** **PDF**; this accepted-manuscript slug does not duplicate every entry. **Barostat / pressure:** **N/A** — **constant-volume** **NVT** in the summarized BJP model. **External electric field:** **N/A**. **Enhanced sampling:** **N/A**.

## Findings

### Mechanisms (from accepted-manuscript abstract)

**Reaction / interface picture:** **DEG** and **water** jointly build **hydrogen-bond** networks that bridge **Cr-oxide** particles during **print/cure**; **burn-out** **oxidizes** **DEG** and disrupts that network; **sintering** forms **Cr–O** bridges. These **mechanistic** points follow the **RSC accepted manuscript** abstract at `pdf_path`.

### Comparisons, sensitivity, and limitations

**Comparisons:** quantitative **restraint-force** curves and **experimental** BJP references are only summarized on [[2019gao-physical-che-reaxff-molecular]] with the **VOR** **PDF**. **Sensitivity:** abstract-level trends tie **hydroxyl** content of alternate binders (**2-ethoxyethanol**, **DEG**, triol) to **print/cure** strength and note an optimal binder loading for **post-sinter** strength. **Limitations:** **accepted manuscript** text may differ slightly from the final **PCCP** wording; **nanoscale** models omit industrial fluidics and dwell times. **Corpus honesty:** this slug is a **non-primary** manuscript PDF; detailed **Methods** numbers are not transcribed here—use the **VOR** sibling for reproduction.

## Limitations

Accepted manuscripts can differ slightly from the final typeset article in wording and layout. Nanoscale models omit full powder-bed fluidics and industrial dwell times.

## Relevance to group

Penn State mechanical engineering collaboration with van Duin on ReaxFF for additive manufacturing binders and oxide powders.

## Reader notes (navigation)

- Full methods and numerical findings: [[2019gao-physical-che-reaxff-molecular]]
- [[reaxff-family]]
