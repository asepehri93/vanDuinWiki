---
id: paper:2019ashraf-venue-paper
type: paper
title: "Supporting information: atomistic investigation of C/H/O/N polymer carbonization (ReaxFF vs QM bond energies)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - method:dft-static
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
source_refs: []
doi: ""
year: 2019
authors:
  - "Malgorzata Kowalik"
  - "Chowdhury Ashraf"
  - "Behzad Damirchi"
  - "Dooman Akbarian"
  - "Siavash Rajabpour"
  - "Adri C. T. van Duin"
venue: "Supporting information (J. Phys. Chem. B polymer carbonization study)"
pdf_sha256: "a520360fdf9523116fcf2063eceb68519b692862dfe1d5071eb33ddd820ed775"
pdf_path: "papers/Kowalik_JPCB_2019_CHON_polymer_SI.pdf"
extraction_quality: "partial"
group_affiliation: false
---
<!-- id:paper:2019ashraf-venue-paper -->

## Summary

This ingest registers a **supporting-information PDF** (`papers/Kowalik_JPCB_2019_CHON_polymer_SI.pdf`) associated with **ReaxFF** development for **C/H/O/N polymer carbonization** chemistry in the van Duin-group **J. Phys. Chem. B** line. The SI’s role is **QM validation**: figures compare **DFT** bond dissociation energies (reported with **B3LYP/6-311G\*\*** in the SI materials) against **ReaxFF** dissociation curves for **CHNO-2010** and **CHNO-2019** parameter generations across selected bond families (for example **C–N** and **N–O**-related motifs as labeled in the panels). This file is **not** a standalone article; the full scientific narrative—training scope, application simulations, and conclusions—belongs to the parent **JPCB** publication that the SI accompanies.

## Methods

This file registers **supporting information** for the **J. Phys. Chem. B** study *Atomistic Scale Investigation of the Carbonization Process for C/H/O/N-based Polymers with the ReaxFF Reactive Force Field* (see the parent article record in the group bibliography; this corpus row intentionally ships **SI-only** bytes under `pdf_path`).

**Static QM / DFT benchmarking (SI figures).** The SI panels compare **DFT** and **ReaxFF** curves using the printed caption form *DFT(6-311G**/B3LYP)* alongside **ReaxFF (CHNO-2010 vs CHNO-2019)** for **bond dissociation energies** and **valence-angle distortion energies** across **C/N/O/H**-rich motifs (multiple **Figures S1–S10** families in the SI PDF). **k-sampling / supercells:** **N/A —** the SI captions indicate **molecular/cluster** QM benchmarks rather than a periodic **k-point** workflow. **Dispersion:** **N/A — not stated** on this SI-first ingest beyond the **B3LYP** + **6-311G\*\*** label in the figure captions.

**Force-field training / parameter release.** **Section S11** begins the **machine-readable ReaxFF parameter table** for **CHNO-2019** (header: **“Force Field developed in this study (ReaxFF CHON-2019)”**), documenting the **combustion C/H/O + N** lineage referenced in the SI front matter.

**MD application (production trajectories).** **N/A —** this **SI** does not publish a standalone **LAMMPS** (or other package) **reactive molecular dynamics** production protocol for operators to copy here: it is **QM–ReaxFF validation** material tied to the parent **JPCB** article. For slot bookkeeping only: **Engine** **N/A**; **system** sizes are the small **atom** clusters/molecules of each SI panel; **PBC** **N/A** for the gas-phase dissociation scans unless a figure explicitly shows a periodic cell; **ensemble** **N/A** (**NVT**/**NVE**/**NPT** trajectories not defined in this PDF); **timestep** **N/A**; **equilibration**/**production** spans in **ps**/**ns** **N/A**; **thermostat** **N/A**; **barostat** and **hydrostatic pressure** **N/A**; **electric field** and **enhanced sampling** **N/A**. **Temperature:** **N/A** for bulk **MD** thermostats—bond scans are **QM**/ReaxFF **energy** profiles, not **constant-temperature** **thermal** sampling runs.
## Findings

**Outcomes.** The SI’s **primary** quantitative message is **side-by-side improvement** of **CHNO-2019** vs **CHNO-2010** relative to the **B3LYP/6-311G**\*\* reference curves for the **bond** and **angle** benchmark panels included in the PDF.

**Comparisons.** Figures are organized as **families** (**C–N**, **N–N**, **N–O**, etc.) so readers can judge **systematic** vs **local** errors across **nitrogen-rich** chemistry needed for **pyrolysis/carbonization** training.

**Corpus honesty.** This wiki entry should not be treated as a substitute for the **parent article** text, **complete training-set enumeration**, or **reactive MD application** results—those live in the **main paper** + its primary PDF path, not this SI ingest slug alone.

## Limitations

Front matter in this slug lacks a filled **`doi`** field because the record is **SI-only** in the corpus automation; identify the parent article DOI from the journal bundle or group bibliography before citing this material as primary literature. Confidence is **med** (not **high**) because the wiki cannot replace the parent article text.

## Reproducibility notes

QM–ReaxFF benchmarking for polymer carbonization should always pair **bond dissociation** scans with **transition-state** checks where pathways are branched; dissociation curves alone can miss **concerted** elimination channels important at pyrolysis temperatures. Archive **B3LYP** basis-set choices and **spin** states used in the SI plots so later parameter revisions can be diffed cleanly against CHNO-2019.

When linking this SI to downstream **reactive MD** studies, record which **CHNO** generation (2010 vs 2019) was used for production runs, because mixed lineages can silently change barrier ordering in complex polymer fragments even when small-molecule benchmarks look improved. Keep a **table** mapping each plotted bond class in the SI to the corresponding ReaxFF **bond order** or **parameter group** in the distributed force field file to make regression tests possible after retraining.

## Relevance to group

ReaxFF CHNO training/validation collateral for polymer carbonization studies led by the group.

## Citations and evidence anchors

`papers/Kowalik_JPCB_2019_CHON_polymer_SI.pdf`

## Related topics

- [[reaxff-family]]
