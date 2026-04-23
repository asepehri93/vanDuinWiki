---
id: paper:2016susanna-venue-paper-2
type: paper
title: "Supporting Information: Simulation of Gold Functionalization with Cysteine (J. Phys. Chem. Lett.)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2016
authors:
  - "Susanna Monti"
  - "Vincenzo Carravetta"
  - "Hans Ågren"
venue: "Supporting Information (J. Phys. Chem. Lett. companion)"
pdf_sha256: "10a95e96d602f2e1ce2f5dcda288b1f439bf77ea8b27b422f41f19735db25e8e"
pdf_path: "papers/ReaxFF_others/Monti_Cystein_Gold_JPC_Letter_SI_2016.pdf"
extraction_quality: "partial"
group_affiliation: false
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
---
<!-- id:paper:2016susanna-venue-paper-2 -->

## Summary

This corpus entry stores the Supporting Information PDF for the Journal of Physical Chemistry Letter on gold functionalization with cysteine, paired with the main letter `paper:2016susanna-monti-j-phys-chem-jz5b02769`. The SI documents how density functional theory optimizations build training data for Au–cysteine interactions used in a modified ReaxFF parametrization, compares ab initio molecular dynamics–sampled configurations against ReaxFF single-point energies, and provides auxiliary trajectory analyses referenced by figure labels such as Figures 1S–5S in the SI text. It is a companion artifact for parameter validation rather than a standalone experimental report. Treat it as the engineering appendix for reproducing the reactive model: training geometries, error plots, and optional parameter file dumps.

## Methods

**1 — MD application (AIMD / RC-MD as cited).** The SI documents **training-set** construction, lists of **DFT-optimized** geometries, and diagnostic **trajectory** analyses (**distance traces**, **minimum-distance distributions** for **cysteine** and **water** relative to **Au**, **energy versus time** curves) referenced by **Figure 1S–5S** labels in the SI text. Production **RC-MD** in the parent letter uses **ReaxFF** within **ADF**, **NVT** at **300 K** and **ambient pressure** as stated there, **timestep** **0.25 fs**, **Berendsen thermostat** (**0.1 ps** coupling), **25 ps** **equilibration**, and **~100 ps** **production** with saves every **0.025 ps** on a **cysteine** + **303** **H\(_2\)O** + **Au(111)** slab model (**PBC**); see **`[[2016susanna-monti-j-phys-chem-jz5b02769]]`**. **Electric field** driving and **umbrella**/**metadynamics**/**replica-exchange** sampling are **N/A —** unless the SI explicitly adds them.

**2 — Force-field training.** **DFT/QM** **reference** energies and structures train **patched** **ReaxFF** parameters for **Au–S/O/H** chemistry; some SI revisions include an **`ffield`** listing for the modified **ReaxFF**—match the **PDF** revision to your bibliography.

**3 — Static QM / DFT.** **DFT** settings for optimizations and **NEB**/**AIMD** benchmarks are tabulated in the SI (**N/A —** not duplicated on this page).

## Findings

The SI substantiates that the ReaxFF extension reproduces key quantum energy ordering and structural motifs for cysteine on gold in explicit water within the stated validation windows. It does not replace the main letter for interpreting the full binding pathway, kinetics, or spectroscopic predictions. Practically, readers use the SI to audit whether the classical model is faithful on the sampled trajectories before trusting longer reactive runs. Any discrepancy between SI tables and main-text claims should be resolved against the published letter and, if needed, publisher corrections. This wiki entry is an archival pointer to the SI PDF bytes in **`pdf_path`**.

## Limitations

`extraction_quality: partial` in normalized metadata; rely on the full SI PDF for complete figures and any parameter tables. No DOI is assigned to the SI file alone.

## Relevance to group

Documents quantum-chemistry training and validation for ReaxFF extensions on Au–thiol chemistry in aqueous environments.

## Citations and evidence anchors

- Primary PDF: `papers/ReaxFF_others/Monti_Cystein_Gold_JPC_Letter_SI_2016.pdf`
- Main article: `[[2016susanna-monti-j-phys-chem-jz5b02769]]`

## Related topics

- [[2016susanna-monti-j-phys-chem-jz5b02769]]
- [[reaxff-family]]
