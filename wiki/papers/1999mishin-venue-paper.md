---
id: paper:1999mishin-venue-paper
type: paper
title: "Interatomic potentials for monoatomic metals from experimental data and ab initio calculations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:classical-ff-specialized
  - method:dft-static
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1103/PhysRevB.59.3393"
year: 1999
authors:
  - "Y. Mishin"
  - "D. Farkas"
  - "M. J. Mehl"
  - "D. A. Papaconstantopoulos"
venue: "Phys. Rev. B"
pdf_sha256: "ee1ef5a1c7cbcdc80220ab76ada3643d69d89327dc4ce8b90b9b6f93e5be1b71"
pdf_path: "papers/Others/Mishin_EAM_Al_PhysRevB.59.3393.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:1999mishin-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The paper develops **embedded-atom method (EAM)** potentials for **Al** and **Ni** by fitting to a joint database of **experimental** observables and **ab initio** energies of many **alternative crystal structures**, with a **distance rescaling** step to improve consistency between experiment and theory. An **alternating fit–test** loop compares **ab initio structural energies** to **EAM predictions** so the parameterization stays accurate within the limits of the **EAM** functional form. The resulting potentials reproduce **elastic constants**, **phonons**, **vacancy** formation and migration, **stacking faults**, **surfaces**, and **relative stabilities** across a range of coordinations—aimed at **defect**, **grain-boundary**, and **dislocation** simulations. The motivation is that **simple** **pair** fits often fail when **coordination** changes away from **fcc** **bulk**, which is precisely the regime encountered near **defect cores**.

## Methods

This paper reports **interatomic potential development and validation** only (no molecular dynamics production runs).

### Force-field lineage and functional form (checklist A)

- **Form:** **Embedded-atom method (EAM)** / **glue model**: total energy as a **pair sum** plus **embedding** \(F(\bar\rho)\) with **atomic density** \(\rho\) summed over neighbors (Eqs. (1)–(2) in the article). **Al** and **Ni** are parameterized in parallel for consistent comparative use (intended also as building blocks toward **Ni–Al** compounds, as stated in the introduction).
- **Parametrization:** **cubic splines** for \(V(r)\) and \(\rho(r)\) with a shared **cutoff** \(r_c\) and smooth cutoff function; **embedding** \(F(\bar\rho)\) chosen so an **effective-pair** gauge can be enforced to simplify elastic constants (Sec. III.B–III.C).

### Training / reference data

- **Experimental database (Sec. III.A.1):** equilibrium **lattice parameter**, **cohesive energy**, **elastic constants** \(c_{11},c_{12},c_{44}\), **vacancy formation** energy (aligned with the data used by **Voter–Chen** reference potentials), plus **vacancy migration** energy, **intrinsic stacking fault** energy, **phonon dispersions**, and constraints on **surface energies** and an empirical **equation of state** (**Rose et al.**) anchored at \(a_0\), \(E_0\), and **bulk modulus**.
- **Ab initio structural energies (Sec. III.A.2):** **first-principles LAPW**, **all-electron**, **general crystal potential**; **exchange–correlation:** **Perdew–Wang** parametrization of **LDA** within **Kohn–Sham DFT**; **Brillouin-zone** integration via **Monkhorst–Pack** meshes (modified for low-symmetry cells); **Fermi** smearing at **2 mRy**; authors state a **large basis** and **k**-point mesh such that energies converge to **better than ~0.5 mRy/atom**.
- **Spin treatment:** **Al** calculations **spin-restricted**; **Ni** treated with **spin-polarized LDA** by iterating from an initial moment (Sec. III.A.2).
- **Crystal prototypes and distances:** energies for **fcc**, **hcp**, **bcc**, **simple hexagonal**, **simple cubic**, **L12**, and **diamond** structures; **hcp** taken at ideal **c/a**; **Al** additionally includes **A15 (\(\beta\)-W)**; **Ni** **A15** omitted for **computational limitations**. Each structure evaluated at **three** nearest-neighbor distances: **0.95R₀**, **R₀**, and **1.1R₀** (Sec. III).
- **Experiment vs theory alignment:** **rescaling** of distances in the **ab initio** vs **EAM** comparison (Eq. (4)) to reduce inconsistency between **experimental** and **ab initio** reference volumes; effect on **elastic constants** discussed explicitly for **Al** **LAPW** elastic constants vs experiment (Sec. III).

### QM reference (checklist C, as used to build the FF database)

- **Clusters / finite systems:** not the focus; the **QM** block is **periodic LAPW** structural energies as above.

### Optimization / fitting (checklist A)

- **Optimizer:** **Nelder–Mead simplex** with many random starts (Sec. III.C).
- **Objective:** minimize **weighted sum of relative squared deviations** from target properties; weights encode reliability and intended **defect** applications (Sec. III.C).
- **Fit vs test split:** **hcp/bcc/diamond** **ab initio** energies included in the fit (via Eq. (4)); other **structural energies** and tests (including rms metrics reported in Sec. IV/V) used for **testing** stages; **alternating** fit/test strategy emphasized in the abstract.

## Findings

- **Bulk and harmonic properties:** for both **Al** and **Ni**, the fitted potentials reproduce the targeted **equilibrium** properties, **elastic constants**, and **phonon branches** substantially better than the **Voter–Chen** reference in several columns of the paper’s **Tables I–II** (quantitative comparisons tabulated there).
- **Nonfcc stability and coordination:** potentials reproduce **relative energies** of **hcp/bcc/diamond**-like prototypes and predict sensible **trends** for **vacancy**, **interstitial**, **stacking fault**, **unstable stacking fault**, **grain-boundary**, and **surface** energies relative to the reference potentials; authors highlight improved **\(\gamma_\mathrm{us}\)** values as relevant to **dislocation nucleation** (discussion around **Fig. 3** and **Tables I–II**).
- **Testing-stage structural-energy rms:** authors quote **~0.06 eV** (**Al**) and **~0.15 eV** (**Ni**) rms deviations for **ab initio** vs **EAM** structural-energy tests (Sec. IV/V), interpreted as a practical accuracy ceiling for **EAM** transferability across the sampled **coordination** range.
- **Transferability caveat:** agreement for **structural energies** is best near **equilibrium** nearest-neighbor conditions and degrades for more extreme coordinations (e.g., discussion of **diamond** and **surface** energies); **surfaces** are systematically **underestimated**, consistent with known **EAM** limitations (**Fig. 4** / surface discussion).
- **Future / limitations (authors):** emphasize **EAM** form limits and the need for **high-quality, broad** **QM** structural databases; **no MD** validation trajectories are reported in the article itself.

## Limitations

- Accuracy is bounded by the **EAM** ansatz; **chemically complex** environments (alloys, charge transfer) require other models.
- Heavy reliance on the quality and breadth of the **DFT** reference set used in the fit.

## Relevance to group

Foundational **interatomic potential** methodology in the same empirical-MD ecosystem as later **reactive** and **ReaxFF** work; useful historical context for **metal** **parameterization** culture and **QM-informed** fitting.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1103/PhysRevB.59.3393 — *Phys. Rev. B* **59**, 3393 (1999).

## Related topics

- [[reaxff-family]]
