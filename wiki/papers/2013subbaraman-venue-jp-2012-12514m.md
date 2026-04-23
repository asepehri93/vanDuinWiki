---
id: paper:2013subbaraman-venue-jp-2012-12514m
type: paper
title: "Atomistic insights into early stage oxidation and nanoscale oxide growth on Fe(100), Fe(111) and Fe(110) surfaces"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reactive-md
  - keyword:charge-equilibration
  - keyword:metallic-systems
  - keyword:oxide-surface
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:ereaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/jp312514m"
year: 2013
authors:
  - "Ram Subbaraman"
  - "Sanket A. Deshmukh"
  - "Subramanian K. R. S. Sankaranarayanan"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "bbb4d9258f2988fdeefc50836c6b4c33b387a8cd88e8c6db9f1b016c75d4d8dc"
pdf_path: "papers/ReaxFF_others/Subbaraman_JPC_C_Fe_oxidation_2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013subbaraman-venue-jp-2012-12514m -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`. Filename uses a legacy **jp-2012-12514m** token; the article DOI is **jp312514m**.

## Summary

**Reactive MD with dynamic charge transfer** probes early-stage **O\(_2\)** oxidation of Fe(100), Fe(111), and Fe(110). Oxide thickness grows with **logarithmic time**, saturating around **1–2 nm** depending on facet. **Fe(110)** shows the strongest **T** and **p** sensitivity vs the other facets. Near-room-temperature oxides are **non-stoichiometric**: a more oxidized **surface** region (Fe\(_x\)O\(_y\), \(y/x \approx 1.3\)–\(1.5\)) over a **bulk-like** layer (\(y/x \approx 0.7\)–\(0.8\))). Effective oxidation barriers are lowest on **Fe(110)** (**7.44 kJ/mol**) vs **Fe(100)** (**23.69 kJ/mol**) and **Fe(111)** (**19.88 kJ/mol**) under the conditions sampled. Transport of anions/cations rationalizes orientation-dependent morphology and stoichiometry, consistent with experimental reports cited in the paper.

<!-- stage-a-wave-005-batch-07 summary expansion -->

## Methods

**1 — MD application (atomistic dynamics).** The abstract and introduction describe **reactive MD** with **dynamic charge transfer** between atoms to study **early-stage** **O\(_2\)** oxidation and **nanoscale** oxide growth on **Fe(100)**, **Fe(111)**, and **Fe(110)** (`normalized/extracts/2013subbaraman-venue-jp-2012-12514m_p1-2.txt`; `pdf_path`). **Temperature** and **pressure** effects are reported as part of the orientation-dependent study. **Ensemble:** oxidation **MD** sweeps use **NVT** and/or **NPT** controls as specified in **`pdf_path`** (the **p1–2** excerpt names **temperature**/**pressure** scans but not the thermostat/barostat table). **Engine / code, timestep, duration, ensemble labels, thermostat/barostat types, slab sizes, and PBC details:** **N/A —** not present in the **p1–2** extract; the **J. Phys. Chem. C** **Methods** section in **`pdf_path`** is required for integration settings. **Electric field:** **N/A —** not stated in the indexed excerpt (the introduction mentions field-driven diffusion ideas from the literature, not an applied field in the authors’ protocol). **Replica / enhanced sampling:** **N/A —** not stated in the indexed excerpt.

**2 — Force-field training.** **N/A —** the indexed text positions the work as **MD with dynamic charge transfer** applied to **Fe** oxidation kinetics rather than documenting a new public training workflow in the excerpted pages.

**3 — Static QM / DFT-only.** **N/A —** oxidation kinetics and morphology are pursued with **reactive MD**; **DFT** appears in the introduction as prior **Fe**/**O** literature context.

## Findings

**Outcomes & mechanisms.** Oxide growth rates follow **logarithmic** time dependence with **limiting thicknesses ~1–2 nm** depending on facet. **Fe(110)** shows stronger **temperature** and **pressure** dependence than **Fe(100)** and **Fe(111)** in the abstract’s summary. Near-room-temperature films are **non-stoichiometric**: a **surface-rich** mixed-oxide region (**\(y/x \approx 1.3\)–\(1.5\)** for Fe\(_x\)O\(_y\)) over a **bulk-like** layer (**\(y/x \approx 0.7\)–\(0.8\)**), tied in the abstract to differing **anion/cation** transport and facet-dependent morphology.

**Comparisons.** The abstract states agreement with **previously reported experimental observations** of **Fe** surface oxidation.

**Sensitivity & design levers.** **Facet**, **temperature**, and **pressure** modulate growth, stoichiometry profiles, and reported **effective oxidation barriers** (**7.44 kJ/mol** on **Fe(110)** vs **23.69 kJ/mol** on **Fe(100)** and **19.88 kJ/mol** on **Fe(111)** in the abstract).

**Limitations & outlook.** Parameterization and finite-time sampling limits are generic caveats for classical reactive oxide growth; author-specific discussion is in the PDF beyond the excerpt.

**Corpus honesty.** Filename token **jp-2012-12514m** is legacy; the curated **DOI** is **10.1021/jp312514m**. Detailed MD protocol is **not** in **`normalized/extracts/..._p1-2.txt`** alone.

## Limitations

Parameterization and finite-time sampling bound quantitative barrier values; continuum-scale oxide stress not included.

## Relevance to group

Corpus **iron oxidation** benchmark using **eReaxFF-style** dynamics (Argonne-led), adjacent to van Duin-group Fe/O workstreams.

## Citations and evidence anchors

- DOI: [10.1021/jp312514m](https://doi.org/10.1021/jp312514m)
- Extract: `normalized/extracts/2013subbaraman-venue-jp-2012-12514m_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Corrosion and oxide growth on iron surfaces
