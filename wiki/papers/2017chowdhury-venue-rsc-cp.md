---
id: paper:2017chowdhury-venue-rsc-cp
type: paper
title: "ReaxFF based molecular dynamics simulations of ignition front propagation in hydrocarbon/oxygen mixtures under high temperature and pressure conditions"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:fuel-combustion
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:combustion
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/c6cp08164a"
year: 2017
authors:
  - "Chowdhury Ashraf"
  - "Abhishek Jain"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Phys. Chem. Chem. Phys."
pdf_sha256: "cf500afa602429bd4ebd9f5d8d2ac340880bf5055c14f14b385d56cd2d503190"
pdf_path: "papers/Chowdhury_PCCP_2016_flame_propagation_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017chowdhury-venue-rsc-cp -->

## Summary

**ReaxFF molecular dynamics** is used to study **ignition front propagation** in **hydrocarbon/oxygen** mixtures under **high temperature and pressure**, with emphasis on **atomistic-level ignition front speeds**. The corpus PDF is a **publisher proof/galley**; quantitative **front speeds**, **mixture specifications**, and full **computational protocols** must be taken from the **version-of-record** at **DOI 10.1039/c6cp08164a**, not from proof boilerplate pages.

## Methods

**MD application (ReaxFF combustion).** The **published** *Phys. Chem. Chem. Phys.* article uses **ReaxFF** with the group’s **combustion** parameterization (see **version-of-record** references) to simulate **hydrocarbon + O₂** mixtures under **high temperature** and **high pressure**, extracting **atomistic ignition front speeds** / **front propagation** metrics as claimed in the **abstract**.

**Force-field training** and **standalone static QM campaigns** are **N/A** for the paper’s main thrust (**application** of an existing **ReaxFF** description).

**Corpus constraint:** the repo **`pdf_path`** is a **publisher proof / galley** (`Chowdhury_PCCP_2016_flame_propagation_galley.pdf`) whose indexed pages are mostly **proof boilerplate**, not the final **Methods** text. **Reproducibility fields**—**MD code**, **PBC** cell vectors and **atom** totals, **ensemble**, **timestep**, **thermostat/barostat**, **initiation** protocol, **production duration**, **front-tracking** analysis, **electric fields**, and **enhanced sampling**—must be taken from the **version-of-record PDF** at **DOI 10.1039/c6cp08164a** (and **SI** if published). This wiki page **does not** invent those numbers from the proof file.

**MD blueprint honesty (galley).** **Reactive molecular dynamics** with **ReaxFF** is the stated tool class. **LAMMPS** is the typical **MD engine** for this publication line—confirm in the **VOR**. **PBC** **gas-phase** supercells are expected for ignition-front studies; **NVT**/**NPT** labels, **timestep**, **thermostat**/**barostat**, **pressure**, **equilibration**/**production** times (**ps**/**ns**), and **electric-field**/**enhanced-sampling** flags are **N/A** from the ingested **proof** pages—use the **VOR**.

## Findings

**Outcomes / mechanism framing:** the PCCP article reports **ignition front propagation** in **hydrocarbon/oxygen** mixtures using **ReaxFF**, positioning the work as among the first **atomistic** estimates of **ignition front speed** under **extreme** **temperature** and **pressure**. **Comparisons:** the narrative contrasts **atomistic** front speeds with **continuum** combustion models—quantitative agreement/disagreement belongs to the **published** tables/figures, not this **galley** file. **Sensitivity:** **temperature**, **pressure**, and **composition** are the natural design levers, but **numerical values** require the **VOR** **PDF**. **Limitations / outlook:** the in-repo **proof** lacks reliable **methods** pagination and may omit **SI** links; authors also discuss scope limits of **ReaxFF** kinetics in the full discussion. ## Limitations

**Non-version-of-record PDF** in-repo (`galley`/`proof`). **Incomplete methods** in the local file; **re-curate** after **VOR** ingest. **ReaxFF** kinetics remain **qualitative** without experiment-backed rate validation for each mixture.

## Relevance to group

**Group-authored** **large-scale reactive MD** on **combustion fronts**; pairs with **CHO** parameter-line work ([[2017chowdhury-venue-jp6b12429]]).

## Citations and evidence anchors

- DOI: [10.1039/c6cp08164a](https://doi.org/10.1039/c6cp08164a)

## Related topics

- [[reaxff-family]]
