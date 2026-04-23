---
id: paper:2013yamada-venue-first-principle
type: paper
title: "First principle and ReaxFF molecular dynamics investigations of formaldehyde dissociation on Fe(100) surface"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:neb
  - keyword:catalysis-surface
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reactive-md
  - method:dft-static
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1002/jcc.23320"
year: 2013
authors:
  - "Takahiro Yamada"
  - "Donald K. Phelps"
  - "Adri C. T. van Duin"
venue: "Journal of Computational Chemistry"
pdf_sha256: "0609ee4ed239033b598a43795f28d1064809b6aa864b68c622a5bd3cd2569517"
pdf_path: "papers/Yamada_Formaldehyde_JCC_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013yamada-venue-first-principle -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path`.

## Summary

**DFT** and **ReaxFF MD** study **formaldehyde**, **formyl (HCO)**, and **CO** on **Fe(100)**, building **energy diagrams** for dehydrogenation/decarbonylation sequences and computing **vibrational frequencies** and **DOS** features. Strongest adsorption for H\(_2\)CO and HCO occurs at **hollow (fourfold)** sites with orientation-dependent adsorption energies in the ranges reported in the paper (hundreds of kcal/mol in the authors’ units—see tables). Barrier heights for key steps (**H\(_2\)CO → HCO + H**, **HCO → H + CO**, **CO → C + O**) are given as **11.0**, **4.1**, and **26.3 kcal/mol**, respectively, in the abstract’s pathway analysis. **ReaxFF** trajectories are compared to **HREELS**-inferred kinetics and **TST** rates: agreement is **mixed** by temperature and step, with TST aligning better with HREELS in several cases discussed in the article.

## Methods

**3 — Static QM / DFT-only.** Spin-polarized **PAW-PBE** in **VASP** on a **2×2 Fe(100)** slab (**five layers**, **bottom three fixed**), **400 eV** cutoff, **Monkhorst–Pack** **k**-sampling (mesh details in the article). **Gas-phase** and **slab** references follow the adsorption-energy conventions stated in the paper. **CI-NEB** with **seven images** maps **HCHO → HCO + H**, **HCO → H + CO**, and **CO → C + O**. **Dispersion:** **N/A —** not called out on this wiki layer; confirm any **DFT-D** usage in **`pdf_path`**.

**2 — Force-field training.** **ReaxFF** parameters are **trained** to **DFT** adsorption/dissociation **energies** and **geometries** for **H, C, O, CO, HCO, HCHO** on **Fe(100)**, augmented with prior **Fe/O/H** bulk training data as described in the article. **QM reference** matches the **DFT** block above (**PBE**/**PAW**/**VASP**). **Optimization:** **N/A —** specific optimizer / weighting scheme not summarized here—see **J. Comput. Chem.** **Methods** for the fitting workflow language.

**1 — MD application (atomistic dynamics).** **ReaxFF MD** explores **finite-temperature** **surface reactions**; **TST** rates are compared to **HREELS**-inferred kinetics (`papers/Yamada_Formaldehyde_JCC_2013.pdf`). **Engine / code, timestep, duration, thermostat, PBC:** **N/A —** not expanded on this wiki layer beyond the article text—read **`pdf_path`** for **LAMMPS** (or equivalent) settings. **Ensemble:** surface **MD** is typically run under **NVT** on a fixed **slab** supercell for **Fe(100)** chemistry of this type—confirm thermostat/ensemble labels in **`pdf_path`**. **Barostat / hydrostatic pressure control:** **N/A —** not summarized here for the **MD** legs. **Electric field / enhanced sampling:** **N/A —** not used in the synopsis.

## Findings

**Outcomes & mechanisms.** **DFT** gives **barriers** of **11.0**, **4.1**, and **26.3 kcal/mol** for **HCHO → HCO + H**, **HCO → H + CO**, and **CO → C + O** along the analyzed **NEB** paths. **ReaxFF MD** is **less reactive than HREELS** at **310 and 523 K** overall; at **523 K** **ReaxFF** can be **more reactive than TST** for **formaldehyde dissociation** but **less reactive than TST** for **HCO dissociation**, while **TST** tracks **HREELS** more closely in several comparisons—showing **mixed** transferability for **Fe(100)** oxygenate chemistry.

**Comparisons.** Side-by-side **ReaxFF MD**, **TST**, and **HREELS**-based kinetics at **310 K** and **523 K**; **DFT** barriers anchor the **oxygenate** decomposition sequence.

**Sensitivity & design levers.** **Temperature** (**310 K** vs **523 K**) changes which step is **over/under**-reactive relative to **TST**/**HREELS**.

**Limitations & outlook.** Single **Fe(100)** facet and **functional** sensitivity; **ReaxFF** **transferability** limits for **surface redox** chemistry motivate further training when **experimental** kinetics exist (**## Limitations**).

**Corpus honesty.** Adsorption-energy magnitudes in **`## Summary`** should be checked against tables in **`pdf_path`**—the wiki cautions against quoting **hundreds of kcal/mol** ranges without table confirmation.

## Limitations

Single facet Fe(100); DFT functional sensitivity; ReaxFF transferability limits for surface redox chemistry.

## Relevance to group

Direct **van Duin** co-authorship on **iron catalysis** with **QM + ReaxFF** coupling for oxygenate chemistry.

## Citations and evidence anchors

- DOI: [10.1002/jcc.23320](https://doi.org/10.1002/jcc.23320)
- Extract: `normalized/extracts/2013yamada-venue-first-principle_p1-2.txt`

## Related topics

- [[reaxff-family]]
- Iron surfaces and oxygenate decomposition in FT synthesis
