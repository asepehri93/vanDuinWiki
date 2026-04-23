---
id: paper:2017atmani-chemical-sci-cellulose-kerogen
type: paper
title: "From cellulose to kerogen: molecular simulation of a geological process"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:water-silica-geo
  - method:reaxff
  - method:enhanced-sampling
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:parallel-tempering
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1039/C7SC03466K"
year: 2017
authors:
  - "Lea Atmani"
  - "Christophe Bichara"
  - "Roland J.-M. Pellenq"
  - "Henri Van Damme"
  - "Adri C. T. van Duin"
  - "Zamaan Raza"
  - "Lionel A. Truflandier"
  - "Amaël Obliger"
  - "Paul G. Kralert"
  - "Franz J. Ulm"
  - "Jean-Marc Leyssale"
venue: "Chem. Sci."
pdf_sha256: "b034946d80f9d8ded4511e1b824e7ea0f9fdff603a6abd9124f614ed8e2f2c2a"
pdf_path: "papers/Atmani_ChemicalScience_2017.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017atmani-chemical-sci-cellulose-kerogen -->

## Summary

Petroleum genesis from **organic matter** spans **Myr** timescales, so brute-force **MD** alone cannot reach **burial** chemistry. Atmani *et al.* (*Chem. Sci.*, DOI **`10.1039/C7SC03466K`**) combine **ReaxFF reactive MD** with **replica-exchange molecular dynamics (REMD)** to follow **cellulose → kerogen + fluids** under **maturation-like** heating. The abstract reports **crystal fragmentation**, **water** release, **unsaturated aliphatic** condensation, and **aromatization**, with **solid** compositions tracking **natural type III kerogen** and **confined artificial maturation** benchmarks. After **fluid expulsion**, the **microporous kerogen** model is compared to **mature type III kerogen** and **microporous carbon** from **low-temperature saccharose pyrolysis** on **structure, texture, density, porosity, and stiffness**. **Methane** dominates **hydrocarbon** products for this **type III** precursor class in their narrative.

## Methods

**MD application.** **LAMMPS**-style **ReaxFF** simulations allow **C/H/O** bond rearrangements without fixed connectivity; parameter provenance and structural benchmarks are documented in the article and **ESI** (`papers/Atmani_ChemicalScience_2017.pdf`). **REMD** (**replica-exchange** / **parallel-tempering**) spans temperature replicas to escape kinetic traps during **cellulose** breakdown and later **aromatization**; **replica spacing**, **exchange** statistics, and **thermostat** choices appear in the **PDF/ESI**, not the short abstract extract. Heating schedules mimic **burial/catagenesis**-like **maturation** rather than laboratory **flash pyrolysis**. Post-processing classifies **solid** and **fluid** products to compare **density**, **porosity**, and **elastic** response with **natural** and **sacrificial-carbon** references. **Atom** counts, **PBC** vectors, **NVT/NPT** choices, **barostat** targets, **timestep**, **production duration**, and **electric fields** are **not** restated in the indexed **p1–2** extract—read **`pdf_path`** for executable inputs.

**Force-field training:** **N/A —** the article **uses** a **ReaxFF** description for **C/H/O** chemistry as referenced in the main text and **ESI**; it does **not** center on a new parameterization fit in this publication.

## Findings

The authors claim a continuous **atomistic** story from **cellulose** to **kerogen** plus **volatiles**, with **semi-quantitative** agreement to **type III** **solid** composition benchmarks along the **maturation** path. **Confined artificial maturation** and **sacrificial carbon** references anchor comparisons of **microporous kerogen** **density**, **porosity**, and **stiffness** after **fluid loss**. **Mechanisms** emphasize **fragmentation**, **dehydration**, **aliphatic** growth, and **aromatization**, with **methane** as the leading **hydrocarbon**. **Temperature** ladders accessed through **REMD** are central to the sampling strategy. **Geological time** remains **compressed**; **ReaxFF** barriers are only **QM**-accurate within the training scope—take **numerical** claims from **figures/ESI**, not this summary.

## Limitations

**Geological time** is still **compressed** via **REMD** and elevated temperatures—**kinetic** correspondence to **basin burial history** requires careful interpretation. **ReaxFF** organic chemistry is **approximate** versus **QM**; quantitative matches should be verified in **figures/SI** rather than inferred from this summary alone.

## Relevance to group

**Adri C. T. van Duin** coauthored this **ReaxFF + REMD** demonstration that **reactive MD** can follow **cellulose → kerogen** chemistry with **geoscience-facing** validation targets—linking the group’s **organic** reactive workflows to **petroleum** and **geomaterials** audiences beyond classical **oxide** applications.

## Citations and evidence anchors

- DOI: `10.1039/C7SC03466K` — *Chem. Sci.* edge article; `papers/Atmani_ChemicalScience_2017.pdf`; extract `normalized/extracts/2017atmani-chemical-sci-cellulose-kerogen_p1-2.txt`.

## Related topics

- [[reaxff-family]]
