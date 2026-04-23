---
id: paper:2014paupitz-physical-che-fullerenes-generated
type: paper
title: "Fullerenes generated from porous structures"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - material:hexagonal-boron-nitride
  - method:reaxff
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:graphene-carbon
  - keyword:2d-materials
  - keyword:thermal-decomposition
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1039/C4CP03529A"
year: 2014
authors:
  - "Ricardo Paupitz"
  - "Chad E. Junkermeier"
  - "Adri C. T. van Duin"
  - "Paulo S. Branicio"
venue: "Phys. Chem. Chem. Phys. 16, 25515–25522 (2014)"
pdf_sha256: "67912cb9b7b9fe6c3de40766b84e347c4b1b01bbe9261188c5ed6380bd7a3d31"
pdf_path: "papers/Paupitz_PCCP_2014_Fullerenes.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014paupitz-physical-che-fullerenes-generated -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **PCCP** **16**, **25515–25522** (**DOI** in front matter). This slug uses the **typeset-style** PDF; **`paper:2014paupitz-venue-rsc-cp`** is a **proof** duplicate.

## Summary

The article introduces **giant fullerene-like** architectures constructed from **porous graphene** and **biphenylene-carbon** motifs, including **hexagonal BN** analogues. The work combines **DFTB**/**tight-binding**-class calculations for **baseline energetics** and **electronic** structure with **ReaxFF-class reactive molecular dynamics** to probe **high-temperature** **stability** and **rearrangement** pathways. Motivations include **gas storage**/**encapsulation** enabled by **intrinsic porosity** and the fundamental question of which **exotic** **carbon** topologies remain **thermochemically** viable at extreme temperature.

The abstract frames comparisons of **atomization energies** against **C₆₀** and **B₁₂N₁₂** references and claims a **thermochemical stability window** extending toward **~2500 K** for selected **porous fullerene** candidates (exact candidates and numerical tables are in the main text).

## Methods

### Electronic-structure baselines (DFTB / tight-binding class)

- **DFTB** and related **DFT-based tight-binding** approaches provide **static** **energetics** and **electronic-structure** comparisons for **giant fullerene-like** cages assembled from **porous graphene** and **biphenylene-carbon** networks, including **hexagonal BN** analogues (abstract).

### Reactive molecular dynamics (ReaxFF)

- **ReaxFF MD** explores **high-temperature** rearrangements and **stability** limits for the same **exotic nanocarbon** / **BN** architectures. **Annealing schedules**, **thermostats**, **timesteps**, and **temperature ceilings** are specified in the **PCCP** article body—**not** in the short checked-in extract, so operators must take protocol details from the PDF.

### Analysis metrics

- The abstract highlights comparisons of **atomization energies** against **C₆₀** and **B₁₂N₁₂** references and discusses a **thermochemical stability window** extending toward **~2500 K** for selected candidates (verify candidate identities and numerical tables in the article).

### 1 — MD application (atomistic dynamics)

**ReaxFF MD** explores **high-temperature** rearrangements for **giant fullerene-like** **porous graphene** / **biphenylene-carbon** architectures and **BN** analogues (**Summary**). **`normalized/extracts/2014paupitz-physical-che-fullerenes-generated_p1-2.txt`** is abstract-scoped; detailed **MD** settings (**timestep**, **NVT**/**NPT**, run lengths, thermostats) are **N/A — not in the short extract**—read **`papers/Paupitz_PCCP_2014_Fullerenes.pdf`**.

- **Engine / code:** **Reactive molecular dynamics** (**ReaxFF**) per abstract; **N/A — MD software** not in `p1–2` excerpt.
- **System size & composition:** **N/A — atom totals** not in `p1–2` excerpt (structures described qualitatively in abstract).
- **Boundaries / periodicity:** **N/A — PBC** details not in the short excerpt; typical **isolated** cage/supercell setups should be confirmed in **`papers/Paupitz_PCCP_2014_Fullerenes.pdf`**.
- **Ensemble / timestep / duration / thermostat / barostat / pressure / electric field / enhanced sampling:** **N/A — not stated** in the indexed excerpt beyond qualitative **high-temperature** annealing language.

### 2 — Force-field training

**N/A —** this page reports **application** of **ReaxFF**/**DFTB** workflows rather than documenting a new **parameterization** on wiki.

### 3 — Static QM / DFT-only

**DFTB**/**DFT-based tight-binding** baselines for **energetics**/**electronic** structure comparisons (**Summary**); detailed **functional**/basis settings are in **PCCP** **16**, **25515–25522**.

## Findings

### Outcomes and mechanisms

**Static rankings:** **Atomization energy** ordering relative to **C₆₀** / **B₁₂N₁₂** references differentiates **porous fullerene** candidates and their **BN** analogues (abstract themes). **Reactive trajectories:** **ReaxFF** annealing supports qualitative conclusions about which **architectures** survive **high-temperature** dynamics versus rearranging (**Summary**).

### Comparisons and sensitivity

Abstract language compares **atomization energies** to **C₆₀** and **B₁₂N₁₂** references and highlights a **~2500 K** **thermochemical stability window** for selected candidates—verify identities/tables in the **PDF**.

### Limitations and corpus honesty

**~2500 K** reflects **simulated** **thermochemistry**/**MD** exploration in the article’s framing, not a laboratory synthesis guarantee. **Exotic** topologies may remain **kinetically** inaccessible despite favorable static rankings.

## Limitations

**Exotic** structures may be **synthetically** inaccessible; **DFTB**/**ReaxFF** accuracy for **BN** nanostructures should be validated case by case. **High-temperature** simulations may explore chemistry outside the **training** scope of the reactive model.

## Relevance to group

**van Duin**-coauthored **porous carbon**/**fullerene** stability study linking **nanocarbon** creativity to **reactive** simulation tools.

## Citations and evidence anchors

- DOI [10.1039/C4CP03529A](https://doi.org/10.1039/C4CP03529A).
- Excerpt alignment: `normalized/extracts/2014paupitz-physical-che-fullerenes-generated_p1-2.txt`.

## Reader notes (navigation)

- Proof duplicate: [[2014paupitz-venue-rsc-cp]]

## Reader notes (extended)

The **DFTB** + **ReaxFF** pairing in this study mirrors common practice: **DFTB** for **baseline** **electronic**/ **static** checks where affordable, **ReaxFF** for **hot** **annealing** trajectories where **DFT** is too expensive—always note which method supports which claim when quoting **stability** numbers.

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
