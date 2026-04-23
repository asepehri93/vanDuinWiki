---
id: paper:2006chenoweth-venue-ffield-parameters
type: paper
title: "ReaxFF force field parameter file (C/H/O combustion): supporting information"
updated: "2026-04-20"
confidence: med
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:combustion
  - keyword:supporting-information
  - keyword:reactive-md
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2006
authors:
  - "Kimberly Chenoweth"
  - "Adri C. T. van Duin"
  - "William A. Goddard III"
venue: "Supporting information (manuscript supplement)"
pdf_sha256: "119917fb0c34efc0eb277d04c54603be9ea6bd5a40d203f3f92a4695f7bea138"
pdf_path: "papers/CHO_supplements/ReaxFF_CHO_forcefield_parameters.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2006chenoweth-venue-ffield-parameters -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below summarize the **supporting-information document** identified by `pdf_path`. They are **not** new primary claims by this wiki.

    Numeric parameter tables in the PDF are **authoritative**; this page does not reproduce full parameter lists.

## Summary

This PDF is the **ReaxFF parameter file** supporting the manuscript “A ReaxFF Reactive Force Field for Molecular Dynamics Simulations of Hydrocarbon Oxidation” (Chenoweth, van Duin, Goddard). It records the **C/H/O combustion** reactive MD force field dated November 2006: general ReaxFF parameters, atom blocks (C, H, O), and bond (and higher-order) parameter sections in standard ReaxFF listing format.

## Methods


**Artifact type (checklist D):** numeric **supporting information**—not a standalone simulation study.

### What this file contains

- **Machine-readable ReaxFF parameter listing** for the parent manuscript *A ReaxFF Reactive Force Field for Molecular Dynamics Simulations of Hydrocarbon Oxidation* (**Chenoweth**, **van Duin**, **Goddard**): **C/H/O combustion** parameterization dated **November 2006**.
- **Format:** standard **ReaxFF** text listing with a **general-parameter** block (**39** entries in the corpus extract), **per-element** rows for **C**, **H**, and **O**, and **bond**/**valence** parameter records for the element pairs printed in the file.
- **Intended software coupling:** meant for import alongside the companion **functional-form** supplement (`papers/CHO_supplements/ReaxFF_CHO_potential_functions.pdf` and related CHO SI).

### What this file does *not* replace

- **Training data**, **QM** levels, **validation** benchmarks, and **application** results are **not** re-derived here—they live in the **peer-reviewed article** and its SI narrative.

### MD application (not reported in this artifact)

This PDF is a **parameter listing**, not a trajectory log. **N/A — molecular dynamics engine**; **N/A — atom count / stoichiometry** for a reported run; **N/A — PBC**; **N/A — NVE/NVT/NPT** protocol; **N/A — timestep**; **N/A — trajectory duration**; **N/A — thermostat**; **N/A — barostat**; **N/A — MD temperature**; **N/A — MD pressure control**; **N/A — electric field**; **N/A — umbrella / metadynamics / replica exchange**.

### Force-field training (what this file documents)

**Parent FF / elements:** **ReaxFF** **C/H/O combustion** listing dated **November 2006** for the parent manuscript *A ReaxFF Reactive Force Field for Molecular Dynamics Simulations of Hydrocarbon Oxidation* (**Chenoweth**, **van Duin**, **Goddard**). **QM / DFT reference, training reactions, optimizer, and weights:** **N/A here**—those narratives live in the **peer-reviewed article** and companion SI PDFs, not in the bare parameter file. **Reference data used:** the listing is the **fitted output** consumed by **molecular dynamics** engines after **optimization** elsewhere. Grounding: `papers/CHO_supplements/ReaxFF_CHO_forcefield_parameters.pdf`, `normalized/extracts/2006chenoweth-venue-ffield-parameters_p1-2.txt`.

## Findings

The file archives the **November 2006** C/H/O combustion **ReaxFF** in standard listing form: **39** general parameters, **C / H / O** atom blocks, and bond (and higher-order) records as printed. It contains **no independent scientific conclusions** beyond documenting the numeric parameter set used with the parent hydrocarbon-oxidation manuscript; **accuracy**, **QM training data**, and **validation** sit in the **main article** and related supplements. **Corpus honesty:** do not treat this SI as a substitute for the **PDF** tables when auditing numbers.
- **Comparisons:** side-by-side use is implied only in the sense that engines load this file **versus** narrative training tables in the parent publication—no new **experiment**/**QM** agreement is asserted here.
- **Sensitivity / design levers:** changing any printed parameter shifts **reaction** energetics in downstream **molecular dynamics**—operators must diff against the **version-of-record** listing.
- **Limitations / outlook:** **future work** on extending the **training set** belongs to the peer-reviewed article, not this numeric dump.
- **Mechanistic outcomes:** **N/A —** this artifact does not report **reaction pathways**; it supplies coefficients consumed by the parent **combustion** **ReaxFF** study.

## Limitations

- This artifact is **supplementary data**; scientific claims and fitting targets belong to the **peer-reviewed parent paper**, not to the parameter listing alone.
- The wiki does not duplicate extended numerical tables; consult the PDF for complete values. Repository automation maps this stable `paper_id` to `normalized/papers/2006chenoweth-venue-ffield-parameters.json` and the repo-relative `pdf_path`. Where `extraction_quality` is partial, the tracked PDF and DOI remain the quantitative authority over short local extracts.

## Relevance to group

**Adri C. T. van Duin** is a named co-author on the parent work; this file is part of the canonical **CHO combustion** ReaxFF lineage used across oxidation and combustion applications.

## Citations and evidence anchors

- PDF: `papers/CHO_supplements/ReaxFF_CHO_forcefield_parameters.pdf`.
- Extract snippet: `normalized/extracts/2006chenoweth-venue-ffield-parameters_p1-2.txt`.

## Related topics

- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
