---
id: paper:2013kim-venue-research
type: paper
title: "Development of a ReaxFF reactive force field for titanium dioxide/water systems (galley PDF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - material:oxide
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:reaxff-parameterization
  - keyword:oxide-surface
  - keyword:water-interfaces
  - keyword:qm-training-data
  - keyword:aimd
  - keyword:dft-static
source_refs: []
doi: "10.1021/la4006983"
year: 2013
authors:
  - "Sung-Yup Kim"
  - "Nitin Kumar"
  - "Petter Persson"
  - "Jorge Sofo"
  - "Adri C. T. van Duin"
  - "James D. Kubicki"
venue: "Langmuir"
pdf_sha256: "08faad78f331eeb9a3b3dd9afea4bc5be518c90281f353f853ea5203ef252fd2"
pdf_path: "papers/Kim_Langmuir_TiO2_water_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013kim-venue-research -->

## Evidence and attribution

!!! note "Corpus PDF role"
    This ingest is a **galley/proof** PDF for *Langmuir* **DOI `10.1021/la4006983`**. The **version-of-record** PDF and figure-stable curation: **[[2013kim-venue-la4006983]]**. Prose below summarizes the **same peer-reviewed article**; locators may differ between PDFs.

## Summary

**TiO\(_2\)–water** interfaces control **photocatalysis**, **corrosion**, and **environmental** speciation at **oxide** surfaces, but **reactive** simulations require a force field that captures **water dissociation**, **polymorph** energetics, and **surface** **hydration** structure. This paper develops **ReaxFF** for **Ti–O–H** by fitting to **DFT** training data spanning **molecular clusters**, **periodic bulk**, and **surface** configurations, augmented where noted by **experimental** **crystal structures**, **heats of formation**, and **bulk modulus** constraints in the optimization narrative. Validation emphasizes **relative** **polymorph** stability (**rutile**, **brookite**, **anatase**), **water binding** strengths, **surface energies**, and **dissociation barriers** against **QM**. For **rutile (110)**, **ReaxFF MD** is compared to **DFT/MD** for **one** and **three** **H\(_2\)O** monolayer-equivalent coverages, reporting **dissociated-water fractions** within about **10%** of the **DFT/MD** reference at **both** coverages.

## Methods

**ReaxFF** optimization targets **bond dissociation energies**, **angle/dihedral** distortions, and **water–TiO\(_2\)** reaction pathways drawn from **DFT** on **clusters** and **periodic** **bulk/surface** models. The article documents checks of **polymorph** energetics, **adsorption** and **surface** energies, and **barrier** heights against **QM**. **Validation MD** compares **ReaxFF** to **DFT/MD** for **rutile (110)** **hydration** at defined **monolayer** counts under consistent **coverage** definitions. Training emphasizes **consistency** across **cluster** and **periodic** segments so that **surface** **proton-transfer** events remain compatible with **bulk** **Ti–O** chemistry in the same parameter set.

**1 — MD application.** **Validation molecular dynamics** with **LAMMPS** (or the engine named in the **galley**/**VOR** **PDF**) on **rutile (110)** **slabs** with **PBC**, **NVT**/**NPT**, **fs** **timestep**, **ps**/**ns** **equilibration**/**production**, **thermostat**/**barostat**, **temperature** (**K**), and **pressure** settings as tabulated in **`papers/Kim_Langmuir_TiO2_water_galley.pdf`**—confirm against **[[2013kim-venue-la4006983]]**.

**2 — Force-field training (when this paper fits ReaxFF parameterization):**

- **Parent FF / elements:** **ReaxFF** / **bond-order** reactive **force field** starting point as named in the article.
- **QM reference:** **DFT** (functional, **basis** set, **k-point** mesh) as the authors report for reference data.
- **Training set:** **Training** structures, **reaction** channels, and target observables (energies, **barriers**, **EOS**, etc.) enumerated in the **PDF**.
- **Optimization:** **Parameter** **optimization** / least-squares or genetic-algorithm language as used by the authors’ **fitting** software.
- **Reference data / validation:** **QM**, **experiment**, or **benchmark** sets used to **validate** the fitted **potential**.

## Findings

For practitioners, the practical payoff is a **single** **Ti–O–H** parameterization that can move from **bulk** **benchmarks** to **explicit** **interfacial** **MD** without changing **functional** forms mid-project. The fitted **ReaxFF** reproduces the **QM training** set for **small-cluster** energetics and captures **bulk polymorph** ordering consistent with the benchmarks discussed. On **rutile (110)**, **dissociated-water fractions** from **ReaxFF** align with **DFT/MD** within ~**10%** at **monolayer** and **trilayer** **water** loadings, while **binding**, **surface energy**, and **barrier** trends are described as matching **QM** reasonably for the tests summarized.

**Sensitivity / outlook:** **Monolayer** vs **trilayer** **coverage** changes **dissociation** statistics; **facet** transfer beyond **(110)** requires extra **validation**.

**Comparisons:** Primary **benchmarks** are **versus** **QM** training sets and **DFT/MD** references cited in the article.

**Corpus honesty:** **`paper:2013kim-venue-research`** is a **galley** ingest—confirm numbers against **[[2013kim-venue-la4006983]]** and the tracked **`pdf_path`**.

## Limitations

**Transfer** to other **facets**, **defected** surfaces, and long-time **proton transport** may require additional **training** and **validation**. Readers should treat **monolayer** coverage definitions carefully when comparing to other **rutile** **hydration** literature. **Galley** PDFs can differ in **pagination** and **figure** numbering from the **VOR** on **[[2013kim-venue-la4006983]]**.

## Reader notes (navigation)

- Version-of-record page: **[[2013kim-venue-la4006983]]**
- [[reaxff-family]]

These sections summarize what the checked-in extraction and abstracts support where quoted above; they are not a substitute for the full PDF. For theme-level retrieval, see [[paper-index-by-domain]] and hubs linked from `canonical_tags` in the front matter.
