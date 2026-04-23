---
id: paper:2016andrew-c-antony-langmuir-201-la6b01974
type: paper
title: "Effect of surface chemistry on water interaction with Cu(111)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - domain:classical-ff-specialized
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:oxide-surface
  - keyword:classical-ff
  - keyword:dft-static
candidate_tags: []
source_refs: []
doi: "10.1021/acs.langmuir.6b01974"
year: 2016
authors:
  - "Andrew C. Antony"
  - "Tao Liang"
  - "Sneha A. Akhade"
  - "Michael J. Janik"
  - "Simon R. Phillpot"
  - "Susan B. Sinnott"
venue: "Langmuir"
pdf_sha256: "a5d7dec99f20aa098795dd6f88235a4937845052824c73ff616306e3cf531b75"
pdf_path: "papers/Others/2016_Antony_Langmuir.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016andrew-c-antony-langmuir-201-la6b01974 -->

## Summary

Classical molecular dynamics with the third-generation charge-optimized many-body **COMB3** potential studies water structure and dynamics on Cu(111), comparing COMB3 adsorption energetics and geometries to **DFT**. Nanoscale water droplets are simulated on bare, oxidized reconstructed, and hydroxylated Cu(111) at **20 K, 130 K, and 300 K** to capture temperature-dependent wetting and spreading, including spreading exponents and final base radii. The motivation is nanoscale wetting on metal electrodes and corrosion interfaces where native oxides and hydroxyls alter hydrophilicity relative to atomically clean Cu.

## Methods

### MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** with **COMB3** for coupled **Cu / O / H** chemistry and **flexible** water (implementation notes in §2.2 of the article).
- **System size / composition (droplet spreading benchmark):** **576** H₂O molecules prepared as an **ice I_h**-derived droplet with **initial diameter ~2.82 nm** (orthorhombic melt-preparation cell yields a slightly non-spherical initial cluster); **Cu(111)** substrate **142 Å × 143 Å** with **10,752 Cu** atoms in **three** metal layers (**Z** = surface normal).
- **Droplet preparation:** **NPT** melt of ice-I_h at **300 K** for **200 ps** to obtain an amorphous liquid droplet configuration before placing on Cu (§3.1).
- **Boundaries / periodicity:** **3D periodic** slab with **≥10 Å vacuum** in earlier adsorption benchmarks; droplet-on-slab images in the article are standard periodic-slab setups with vacuum separation along **Z** (see figures and §2.4 slab description: **31×31 Å** nine-layer slab with **10 Å** vacuum for adsorption minimizations—distinct cell from the large droplet slab).
- **Ensemble:** **NVT** (constant-volume, constant-temperature) for the spreading runs described in §3.1 (“constant-volume, constant-temperature ensemble at 300 K” for the room-temperature case; analogous setups at **130 K** and **20 K**).
- **Thermostat:** **Langevin** thermostat on the **mobile water + top two Cu layers** with damping **100.0 ps**; **bottom Cu layer fixed**. The manuscript documents an **effective-temperature calibration** trick: **input 370 K** for water to obtain **~300 K** output, while **Cu** uses **input 300 K** to stabilize charges/vibrations (§3.1).
- **Timestep:** **N/A —** an integration **Δt** is **not stated** in the *Langmuir* **2016**, **32**, **8061–8070** article body text extracted from **`pdf_path`** (full-PDF text search did not locate an explicit **fs** timestep); confirm in **Supporting Information** or the publisher PDF if strict reproduction requires this parameter.
- **Duration:** Droplet spreading statistics are accumulated after defining interfacial / precursor-film / surface / bulk regions as in §3.1 (use the article’s stated equilibration/spreading windows for exponent fits).
- **Barostat:** **N/A — spreading production is NVT** (barostat appears only in the **200 ps** droplet-preparation melt noted above).
- **Pressure:** **N/A — not a controlled variable** in the quoted **NVT** spreading segment.
- **Electric field:** **N/A — not used.**
- **Replica / enhanced sampling:** **N/A — brute-force classical MD** on the reported droplet trajectories.

### Force-field training (COMB3 parameter context)

The article documents **COMB3 O/H** fitting with **POSMat** against molecular and **ice I_h** benchmarks and **couples** that water description to existing **Cu–hydrocarbon** and **Cu₂O** COMB3 parameter files (§2.2–2.3). This page does **not** duplicate the parameter tables—use the paper/SI for numeric parameter sets.

### Static QM / DFT (benchmarking against COMB3)

- **Program / functional:** **VASP 5.3.5**, **PBE-GGA**, **PAW** cores; **DFT-D3** dispersion with **Becke–Johnson** damping (§2.1).
- **Cutoffs / smearing:** **450 eV** plane-wave cutoff; **Methfessel–Paxton** smearing (**σ = 0.2 eV** for Cu systems, **0.003 eV** for isolated water in the quoted setup text).
- **k-sampling:** **5×5×1** Monkhorst–Pack mesh for **Cu(111)** slabs in §2.1.
- **Structures / targets:** **Quasi-Newton** relaxations to **0.02 eV Å⁻¹** force tolerance; adsorption energies for **monomer/dimer/hexamer** water configurations on **Cu(111)** compared to COMB3 (§2.4, Table 3).

## Findings

- **DFT vs COMB3 adsorption:** COMB3 reproduces the **trend** of stronger adsorption with increasing cluster coverage for the **dimer/hexamer** cases tabulated, while **monomer site ordering** (atop vs hollow) can disagree with DFT because of **transferable Cu–O/Cu–H** parameters not refit on these specific adsorption points (authored caveat in §2.4).
- **Spreading exponents (300 K):** Bare **Cu(111)** shows **R₀ ≈ t^0.16** with **final base radius ~3.5 nm** in the abstract-level summary (simulation setup uses the **~2.82 nm** initial droplet diameter in §3.1).
- **Low temperature:** At **20 K** and **130 K**, droplets remain **compact** with **minimal spreading**, consistent with **STM**-reported clustering / limited mobility discussed in the article.
- **Surface chemistry:** **Oxidized reconstructed** and **OH-covered** Cu(111) reduce both the spreading exponent (**≈t^0.14**) and the final base radius (**≈3.0 nm** oxidized, **≈2.5 nm** hydroxylated, as reported in the abstract), linking **oxide/hydroxide** termination to **less efficient nanoscale wetting** on Cu.

## Limitations

COMB3 is distinct from ReaxFF; do not conflate with reactive bond-order ReaxFF parameterizations in downstream retrieval.

## Relevance to group

PSU co-authors (Janik); complements metal–aqueous interface and corrosion-adjacent simulation themes.

## Citations and evidence anchors

- DOI: [10.1021/acs.langmuir.6b01974](https://doi.org/10.1021/acs.langmuir.6b01974)

## Related topics

- [[theme-water-silica-geo]]
