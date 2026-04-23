---
id: paper:2015han-venue-supporting-information
type: paper
title: "Electronic Supporting Information: Development of the ReaxFFCBN Reactive Force Field for Liquid CBN Hydrogen Storage Materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
source_refs: []
doi: ""
year: 2015
authors:
  - "Sung Jin Pai"
  - "Byung Chul Yeo"
  - "Sang Soo Han"
venue: "Electronic supplementary material (PCCP family)"
pdf_sha256: "56c2bb7f276093677ba9492e872d884fb6e02b87753e5a5b193bbc9030a0f3e9"
pdf_path: "papers/ReaxFF_others/Pai_BNCH_PCCP_2016_SupportingInformation.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2015han-venue-supporting-information -->

??? info "DOI"
    Front matter leaves `doi` empty because this ingest targets the **SI PDF**; resolve the parent PCCP article DOI from the publisher bundle when registering the main text.

## Summary

This Electronic Supporting Information package documents the ReaxFFCBN reactive force-field development for boron–carbon–nitrogen–hydrogen chemistries relevant to liquid CBN hydrogen-storage materials (authors Pai, Yeo, Han). The SI contains quantum-mechanics reference data and ReaxFF fits for bond dissociation and angle deformation coordinates on benchmark molecules such as 3-methyl-1,2-BN-cyclopentane motifs referenced in figure captions, together with plots comparing QM energies to the fitted reactive potential. The tables enumerate general ReaxFF terms (bond, overcoordination, valence, torsion, van der Waals shielding, Coulomb) as needed to reproduce the parameter file distributed with the parent article.

## Methods

**Force-field training (ReaxFFCBN).** This Electronic Supporting Information accompanies development of a **ReaxFFCBN** parameterization for **B–C–N–H** chemistry aimed at **liquid CBN hydrogen-storage** motifs (authors Pai, Yeo, Han). The SI documents **QM reference** **bond-dissociation** and **valence-angle deformation** scans on **small gas-phase benchmark molecules** (order **10–40 atoms** in the CBN-B motifs of Figure S1), with panels comparing **QM** and **developed ReaxFFCBN** energies along those coordinates. General ReaxFF energy classes used in the fit (**bond**, **overcoordination**, **valence**, **torsion**, **van der Waals shielding**, **Coulomb**) are summarized as in the distributed parameter file referenced by the parent article.

**QM reference level (as cited in the SI workflow).** The SI text points readers to the parent **Physical Chemistry Chemical Physics** article for the full QM level-of-theory statement and fitting protocol; this SI page does not restate basis sets, functionals, or program build strings beyond what appears in the SI figures’ captions.

**MD application (production validation).** **N/A —** this corpus `pdf_path` is **SI-only**. The indexed SI pages give **bond-dissociation / angle-deformation** scans and parameter tables for **ReaxFFCBN**; they do not independently specify **engine**, **PBC**, **ensemble**, **timestep**, **thermostat/barostat**, **production duration**, or **bulk validation** trajectories. Those belong to the **version-of-record** PCCP article for the ReaxFFCBN work (see parent article **Methods**).

**Static QM / other blocks.** **N/A —** beyond the QM-vs-ReaxFF training plots, this SI is not a standalone DFT benchmark or non-ReaxFF simulation report.

**Cross-reference (parent article Methods).** The **version-of-record** PCCP article for **ReaxFFCBN** reports **molecular dynamics** validation with **periodic** (**PBC**) cells, **NVT** or **NPT** staging as appropriate, a stated **thermostat**/**barostat**, **temperature** targets in **K**, integration **timestep** in **fs**, **ns**-scale (or **ps**-scale) **production** segments, and **pressure** control when used. Those items are **not tabulated on the SI pages** indexed for this slug—read the **main text Methods** rather than inferring them here.

## Findings

Figure S1 documents **QM versus ReaxFFCBN** energies along **NH\(_2\)** and **BH\(_2\)** **bond-dissociation** coordinates and matching **angle-deformation** scans for the small **CBN-B** training motifs; numerical residuals and parameter tables belong to the **SI/PDF** and are not transcribed here. The SI positions these panels as **training-quality** evidence for the **B–C–N–H** extension; **macroscopic experimental benchmarks**, **bulk liquid** validation trajectories, and tribology-scale conclusions live in the **parent PCCP** article, not this **SI-only** ingest. **Comparisons beyond QM-vs-ReaxFF on gas-phase coordinates:** **N/A —** not the excerpted SI scope. **Sensitivity tables** beyond the plotted scans: **N/A —** not provided on the indexed pages.

## Limitations

Supporting information alone does not substitute for the peer-reviewed article text, discussion, and bibliography. Operators should ingest or link the primary article PDF when assigning a DOI to this record.

## Relevance to group

Parameterization artifact for B–N–C–H ReaxFF chemistry adjacent to hydrogen-storage and combustion-related entries in the corpus.

Linking this SI to the eventual parent PCCP article DOI in `normalized/papers/*.json` will improve automated citation graphs; until then, keep a manual note in manifests that the SI belongs to the ReaxFFCBN development paper by Pai, Yeo, and Han.

Training plots in the SI should be read with the same unit conventions (kcal/mol vs eV) printed on each axis, because mixed units sometimes appear across QM packages referenced in the fitting workflow.

## Reader notes (navigation)

- [[reaxff-family]]
