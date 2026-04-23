---
id: paper:2019nayir-j-phys-chem-development-reaxff
type: paper
title: "Development of a ReaxFF Reactive Force Field for Interstitial Oxygen in Germanium and Its Application to GeO2/Ge Interfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:widegap-semiconductor
  - method:reaxff
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.8b08862"
year: 2019
authors:
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Sakir Erkoc"
venue: "J. Phys. Chem. C 123:1208-1218 (2019)"
pdf_sha256: "076ea7746bef0efc7405eb183604704f0ff8d218ffae4379c05a718282012f37"
pdf_path: "papers/Nayir_JPC_C_GeOx_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019nayir-j-phys-chem-development-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

A Ge/O/H ReaxFF is extended from prior work with additional QM training on O interstitial energies and migration in diamond Ge and on bulk GeO/GeO2 condensed-phase data. The refined FF reproduces equations of state and heats of formation and ranks O-interstitial sites (bond-centered, split, tetrahedral, hexagonal) consistently with DFT. Oxygen diffusion between bond-centered sites and through the split-like transition state matches the intended DFT picture; ReaxFF predicts an effective barrier near 50 kcal/mol over 800–2000 K. GeO2/Ge interface oxidation simulations show oxide thickening and Ge consumption with temperature and time, unlike Tersoff-based runs that miss this behavior.

## Methods

**2 — Force-field training.** A Ge/O/H ReaxFF (“**ReaxFF\(_\text{present}\)**” in the article) is refit against the Zheng *et al.* GeO/GeO₂ condensed-phase training set plus interstitial O in diamond Ge, including formation energies and the DFT BC→BC migration pathway through the split-type saddle (PBE-class DFT as cited in *J. Phys. Chem. C*). After reoptimization, the model reproduces condensed GeO/GeO₂ energetics and the O-interstitial stability sequence BC → split → tetrahedral → hexagonal with near-DFT energy splittings (Table 1 in the paper).

**1 — MD application. Engine / code:** ReaxFF-based trajectories are run with **ADF/ReaxFF**; the parallel Tersoff study uses **LAMMPS** (the article states both explicitly). **3D** **PBC** are used, with an unwrapped-coordinate post-processing path for diffusion. **System / composition:** **O**-**interstitial** **diffusion** in **diamond-**structure **Ge** **uses** **periodic** **supercells** with **hundreds** **to** **thousands** of **host** **Ge** **atoms** (exact **supercell** **multiplicity** and **O** **placement** in *J. Phys. Chem. C* **Methods** / **Figs.**). **O diffusion in bulk Ge (800–2000 K, both force fields compared):** two-stage **NVT** with **Berendsen** thermostat; **stage 1** — coupling **100 fs**, **0.01 K/step** heating to the target *T*, **1 ns** equilibration; **stage 2** — **3.5 ns** at fixed *T* with weaker coupling **1000 fs** and unwrapped-trajectory sampling (every 100 MD frames) for the diffusion analysis. **a-GeO₂** glass preparation (as used in the Ge/GeO₂ stack work) includes **NPT** at **300 K** for **0.5 ns** in the Methods. **Time integration step in fs (integrator, not thermostat damping):** not captured in the text pass used for this curation; **N/A** — use the *J. Phys. Chem. C* PDF for the exact femtosecond **timestep** (the text quotes **100 fs** / **1000 fs** **damping** constants for the **thermostat**). **Barostat in the NVT diffusion stages:** **N/A** (constant-volume **NVT**). For the quoted **NPT** glass-formation block, isotropic servocontrol is **NPT** at the conditions given in the paper. **Mean external electric field on the cell:** **N/A**. **Umbrella / metadynamics:** **N/A** — conventional sampling.

**3 — Static DFT in Methods:** DFT supports the **ReaxFF** training; **N/A** as a standalone “DFT-only paper” — the **MD** + **Tersoff** **comparisons** are central.

## Findings

**1 — Outcomes and mechanisms.** ReaxFF\(_\text{present}\) recovers the O-interstitial ordering and a DFT-consistent hopping topology (BC–BC via a split-like saddle). **MD** between **800 K and 2000 K** yields a reported **effective** O-diffusion **barrier** of **~50.02** **kcal** **mol⁻¹** in the **abstract/Results** text. **2 — Comparisons.** For T ≳ **1400 K** along the O-hopping path, ReaxFF follows the intended route, while Tersoff-based trajectories visit H-site-flavored jumps that disagree with the cited DFT picture. For Ge/GeO₂ interface heating, ReaxFF (but not the Tersoff comparison the authors highlight) shows time- and temperature-dependent GeO₂ thickening and Ge consumption, qualitatively consistent with the cited experiments, whereas the Tersoff parallel shows nearly static film thicknesses in the same side-by-side comparison. **3 — Sensitivity and levers.** Temperature and oxidation time are the main knobs; **4 — Outlook / authored limits** — see **## Limitations** and the *J. Phys. Chem. C* discussion for transferability caveats (empirical potentials, prepared interface geometry).

## Limitations

Still an empirical reactive model—quantitative barriers and rates need continued benchmarking across defect configurations. Interface studies are specific to the prepared initial geometries and thermal protocol.

## Relevance to group

Core group contribution on semiconductor oxidation and defect diffusion with ReaxFF, relevant to Ge CMOS dielectric stacks.

## Citations and evidence anchors

- Local PDF: `papers/Nayir_JPC_C_GeOx_2019.pdf`
- DOI: https://doi.org/10.1021/acs.jpcc.8b08862

## Related topics

- [[reaxff-family]]
