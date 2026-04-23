---
id: paper:2021gupta-journal-of-c-coke-resistant
type: paper
title: "Coke resistant catalyst for hydrogen production in a versatile, multi-fuel, reformer"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:fuel-combustion
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:catalysis-surface
  - keyword:thermal-decomposition
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: "10.1016/j.jcat.2021.08.031"
year: 2021
authors:
  - "Prashant Gupta"
  - "Swarit Dwivedi"
  - "Adri C. T. van Duin"
  - "S. Srinivas"
  - "Akshat Tanksale"
venue: "Journal of Catalysis, 402 (2021) 177–193"
pdf_sha256: "3c3779fd48f8593c66bdefbb4b25d1ee0175e17c112fdc4c40ebf6a4ce2d9ac2"
pdf_path: "papers/Gupta_Coke_Resistant_Catalysts_J_Catalysis_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021gupta-journal-of-c-coke-resistant -->

## Summary

The authors report a potassium-promoted Ni–Pt catalyst on a pillared clay–alumina support for **oxidative steam reforming** of several liquid fuels (methanol, gasoline, diesel). Near **5 wt% K** the system stays on stream for about **42 h** under start-up/shut-down cycling with similar conversion and H\(_2\) productivity across fuels. Characterization ties coke resistance to stronger metal–support interaction, higher **basicity** (including **CO\(_2\)-TPD**), and **K–Al–Si–O** phases in the support. **ReaxFF MD** in the **ADF** suite (Cu/zeolite ReaxFF) **anneals** a **K\(_2\)O–Al\(_2\)O\(_3\)–SiO\(_2\)** mixture, with **g(r)** compared to DFT reference **KAlSiO\(_4\)** and **KAlSi\(_3\)O\(_8\)** structures to support assignment of K–Al–Si–O environments.

## Methods

### 1 — MD application (atomistic dynamics)

- **Engine / code:** ReaxFF reactive MD in the **ADF Modelling Suite** (noting the manuscript’s Section 2.6 text); coordinates visualized in **VMD** as stated.
- **System & composition:** A mixed K\(_2\)O/Al\(_2\)O\(_3\)/SiO\(_2\) system with **elemental ratios** tied to the experimental support (Table S1 / discussion); reference **DFT** structures of Al\(_2\)O\(_3\), SiO\(_2\), K\(_2\)O, KAlSiO\(_4\), KAlSi\(_3\)O\(_8\) from the **Materials Project** for property comparison. **Catalyst activity** and **TGA/XPS/BET/TPR/SEM**-class data are from **experiment** in Sections 2–3, not from MD.
- **Boundaries / periodicity:** **NPT** 3D cell (simulation of bulk mixed-oxide annealing as described).
- **Ensemble:** **NPT** for the annealing trajectory.
- **Timestep:** **0.25 fs** for **T < 2200 K**; **0.1 fs** for **T > 2200 K** (as stated in Section 2.6).
- **Duration / stages:** **300 K** for **100 ps**; then **4 K/ps** ramp to **2800 K**; **2800 K** held **200 ps**; then **4 K/ps** cool to **300 K**; **100 ps** at 300 K. Separate **100 ps NPT** reference runs for comparison structures at **300 K**.
- **Thermostat:** **Berendsen** with **100 fs** damping.
- **Barostat:** **Berendsen** barostat with **1500 fs** damping in the **NPT** protocol.
- **Temperature:** 300 K holds; ramp to 2800 K; cooling; **4 K/ps** rate during ramps.
- **Pressure:** NPT (hydrostatic) as implemented with the Berendsen barostat; exact target pressure follows the **Journal of Catalysis** text (isotropic NPT in ADF per standard practice unless SI states otherwise).
- **Electric field:** N/A.
- **Enhanced sampling:** N/A (accelerated anneal via high-T MD rather than umbrella/hyperdynamics); **N/A** for metadynamics.

**Experiment (reforming):** Pillared support synthesis, Ni/Pt impregnation, reforming of commercial fuels, characterization as in the main text and ESI; **N/A** in the MD slot sense for atomistic table—handled as laboratory protocol in the article’s experimental sections.

### 2 — Force-field training

**N/A** — the article **uses** the **ReaxFF Cu/zeolite** field from the literature [**33**] in **ADF** for this mixed-oxide anneal; the authors do **not** re-fit parameters in this work. DFT (Materials Project) structures are used to **check density** to within **±5%** before/around the anneal narrative.

### 3 — Static QM

**DFT** reference **geometries** from the **Materials Project** for K–Al–Si–O crystal benchmarks; the MD section compares the annealed structure’s **RDFs** to those of **KAlSiO\(_4\)** and **KAlSi\(_3\)O\(_8\)** from literature/MP sources. This supports short-range order assignment; **N/A** as a peer study of reforming on Ni surfaces.

### 4 — Review

N/A — primary **experiment + targeted ReaxFF** support study.

## Findings

- **Reforming:** Optimum near **5 wt% K** balances **activity** and **stability**; lower/higher K loadings shift **Ni** **sintering**, **side reactions** (methanation, RWGS, coking), and **H\(_2\)** yield in the direction summarized in the article’s Figs. 1–2.
- **Support chemistry:** K raises **BET** and **pore** volume to intermediate K; **CO\(_2\)-TPD** basicity ties to **reverse Boudouard**-style **CO\(_2\)** chemistry that reduces carbon buildup.
- **ReaxFF:** Simulated **g(r)** of the annealed K–Al–Si–O mixture aligns **K–Si** correlations more closely with **KAlSiO\(_4\)** than with **KAlSi\(_3\)O\(_8\)**; **Al–Si** motifs match **aluminosilicate**-like order, **supporting XRD/XPS** evidence for **KAlSiO\(_4\)**-type phases. **N/A** — the **anneal** is **kinetic** and need not reach full **crystallization**; authors state limits explicitly.

**Limitations / outlook (authored):** ReaxFF explores **kinetic accessibility** of local structures, not full thermodynamic equilibrium of industrial supports. **TGA**-level coke **assignments** remain as in the main text. **Comparisons:** K promotion routes (**during support synthesis** vs co-impregnation) and fuel-to-fuel **conversion** plateaus. **Corpus / KB honesty:** protocol numbers are from *Journal of Catalysis* **402 (2021) 177–193**; confirm any SI-only tables locally.

## Limitations

ReaxFF annealing is a finite-time, high-temperature model of mixed-oxide order; it complements but does not replace long-range **crystallinity** from XRD. External validation of the MD force field to **K–Al–Si** chemistry is as stated in the paper.

## Relevance to group

ReaxFF MD alongside **van Duin**-coauthored **reforming** and **K–aluminosilicate** characterization.

## Citations and evidence anchors

- Reforming and characterization: *J. Catal.* **402 (2021)** main text and ESI.  
- ReaxFF: Section **2.6** and **Fig. 10** (discussing RDFs vs KAlSiO\(_4\)/KAlSi\(_3\)O\(_8\)).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
