---
id: paper:2014leven-venue-paper
type: paper
title: "Inter-layer potential for hexagonal boron nitride"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:hexagonal-boron-nitride
  - method:classical-md
  - task:parameterization
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:dft-static
  - keyword:2d-materials
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1063/1.4867272"
year: 2014
authors:
  - "Leven, Itai"
  - "Azuri, Ido"
  - "Kronik, Leeor"
  - "Hod, Oded"
venue: "The Journal of Chemical Physics"
pdf_sha256: "a24db9e3c86d8c18433647992f9e0ba626b84253eb21be691f4205214b256073"
pdf_path: "papers/ReaxFF_others/Leven_inter-layer-BN-reaxff_JCP_2014.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2014leven-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi`, `title`, and `pdf_path` in the front matter. For definitive numerical values and figures, use the peer-reviewed article.

## Summary

Stacked **hexagonal boron nitride (h-BN)** is a prototypical **van der Waals** layered solid: accurate interlayer energetics control exfoliation, friction, and self-assembly, yet generic Lennard-Jones stacks miss registry-dependent anisotropy and quantitatively wrong binding/sliding can derail mesoscale models. Leven, Azuri, Kronik, and Hod introduce a dedicated **interlayer potential (ILP)** for h-BN that couples **dispersion**, **anisotropic short-range repulsion**, and **layer-resolved electrostatics** fitted to high-quality **DFT** references. The resulting model is intended for **large-scale molecular dynamics** of **bilayers**, **few-layer stacks**, and **double-walled boron nitride nanotubes (DWBNNTs)** where interlayer motion—not intralayer bond rearrangement—is the primary degree of freedom.

## Methods

The **ILP** superposes three physical contributions: **(i)** **dispersion attraction** formulated in the spirit of **Tkatchenko–Scheffler (TS-vdW)** corrections so long-range attraction tracks polarizability and layer separation; **(ii)** **anisotropic Pauli repulsion** expressed in a **Kolmogorov–Crespi**-type **registry-dependent** form that captures how interlayer overlap depends on in-plane alignment; and **(iii)** **classical monopolar electrostatics** between partially charged atoms to represent **in-plane ionicity** within each BN sheet. Parameters are adjusted against **benchmark DFT** datasets for **interlayer binding curves**, **in-plane shear/sliding** paths on **h-BN bilayers**, and **interlayer telescoping and rotation** in **DWBNNT** pairs spanning multiple **relative orientations** (see *J. Chem. Phys.* **140**, 104106 and the local extract). Intralayer bonding remains outside this interlayer functional: simulations pair the ILP with an intralayer model appropriate for covalent BN sheets.

### 1 — MD application (intended use of the ILP)

- **Engine / code:** **Molecular dynamics** with an **interlayer potential** is the *intended* downstream use case for **large-scale h-BN** assemblies (**abstract**); **N/A — specific MD package and timestep not stated on extract p1–2** (JCP article).
- **System targets / composition:** **bilayer** sliding landscapes, **few-layer stacks**, and **double-walled BN nanotube** interlayer modes as described in the **abstract**/**introduction** (extract); treat these as explicit **atomistic** targets paired with separate **intralayer** models.
- **Boundaries / periodicity:** **Periodic** **in-plane** boundary conditions are standard for **bilayer** sliding energy maps in this article class; **N/A — explicit PBC strings not on extract p1–2**.
- **Ensemble:** **NVT** is a common choice for **classical MD** validation of **interlayer** models, but **N/A — not stated on extract p1–2** (JCP Methods).
- **Timestep / thermostat:** **N/A — not stated on extract p1–2** (JCP Methods for any validation **MD**).
- **Duration / stages:** **Equilibration**/**production** lengths for any reported **MD** validation are **N/A — not on extract p1–2**.
- **Barostat / hydrostatic pressure:** **N/A — pressure control not stated on extract p1–2** (interlayer distance scans are typically energy landscapes).
- **Temperature:** **N/A — explicit MD temperature set points not stated on extract p1–2**.
- **Electric field:** **N/A — not indicated** in the indexed extract opener.
- **Replica / enhanced sampling:** **N/A — not indicated** in the indexed extract opener.

### 2 — Force-field training (classical interlayer potential, not ReaxFF)

- **Functional form (“parent” models):** **h-BN ILP** combines **(i)** a **Tkatchenko–Scheffler (TS-vdW)**-style **dispersion** attraction, **(ii)** a **Kolmogorov–Crespi**-type **registry-dependent** **repulsion**, and **(iii)** **classical monopolar electrostatics** for **in-plane ionicity** (extract; *J. Chem. Phys.* **140**, 104106).
- **QM reference / training set:** parameters adjusted to **advanced DFT** benchmarks covering **interlayer binding**, **sliding**, and **DWBNNT telescoping/rotation** across registries (extract); **N/A — full functional/basis/k-mesh tables not on extract p1–2**.
- **Optimization / software:** parameter adjustment workflow as described in the article; **N/A — optimizer implementation details not on extract p1–2**.
- **External reference data:** **DFT** benchmark energies/landscapes used for fitting and validation (article).

## Findings

Across the benchmarks used in the paper, a **single interlayer parametrization** reproduces **binding energies**, **sliding barriers**, and **telescoping/rotation** energetics for **DWBNNT** pairs with different **crystallographic registry**, supporting transferability within the h-BN stacking manifold targeted by the fit. Practically, this enables **classical MD** of **layered BN** assemblies—twists, stacks, and nanotube bundles—at sizes and timescales impractical for **DFT** or **full reactive** treatments, provided chemistry is limited to **non-reactive** interlayer motion. The approach is complementary to **intralayer** **ReaxFF** or **Tersoff**-style models: researchers should not expect **ILP** alone to describe **sp³ defect** chemistry or **nitrogen** **vacancy** formation without augmenting the Hamiltonian.

## Limitations

Intralayer bonding uses a separate model; interlayer potential is not a ReaxFF reactive treatment. Users should verify **interlayer** parameter units and **cutoffs** against the **JCP** article when mixing **ILP** with intralayer engines in **LAMMPS** input decks.

## Citations and evidence anchors

- DOI `10.1063/1.4867272` (extract citation line).
- Title and abstract opening (extract page 1).

## Related topics

- [[graphene-nanocarbon]]
