---
id: paper:2018vashisth-venue-paper
type: paper
title: "Effect of chemical structure on thermo-mechanical properties of epoxy polymers (uncorrected proof)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:methods-software
  - domain:organics-polymers-pyrolysis
paper_keywords:
  - keyword:galley-or-proof-pdf
  - keyword:polymer
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.polymer.2018.11.005"
year: 2018
authors:
  - "Aniruddh Vashisth"
  - "Chowdhury Ashraf"
  - "Charles E. Bakis"
  - "Adri C. T. van Duin"
venue: "Polymer (uncorrected proof)"
pdf_sha256: "ac60ebe91546bf2d050d4376fde977c326a62ecbfa4da7abfa6b2dbeb8a4c2ac"
pdf_path: "papers/Vashisth_Polymer_2018_proof.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2018vashisth-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    This corpus PDF is labeled **UNCORRECTED PROOF** for *Polymer*. The **final Elsevier article** (DOI [10.1016/j.polymer.2018.11.005](https://doi.org/10.1016/j.polymer.2018.11.005)) is authoritative for pagination and copy editing; prose here follows the proof abstract and introduction visible in the local extract.

## Summary

The article compares aromatic, cycloaliphatic, and aliphatic amine curing agents reacted with bisphenol-A epoxide using an accelerated ReaxFF cross-linking strategy suited to kinetically slow epoxy curing. The central claim is that chemical structure at the network level governs bulk thermo-mechanical response: cyclic curing agents yield local heterogeneities in the simulated polymer that can be partially relaxed by annealing, while strain-rate dependence in molecular dynamics appears strongest for aliphatic curing chemistry and weaker for aromatic curing agents. The authors report good correlation between accelerated cross-linking plus virtual testing and experimental structure–property trends across the curing chemistries.

## Methods

The workflow builds on **Accelerated ReaxFF** as referenced in the introduction: reactants receive energy comparable to reaction barriers so that successful bond formation can occur when molecules approach along physically plausible paths, without requiring the manual bond activation schemes used in some earlier epoxy simulations. Experiments use EPON 828 (diglycidyl ether of bisphenol A) with three curing agents: DETDA (aromatic diamine), IPDA (cycloaliphatic diamine), and JEFFAMINE T-403 (trifunctional polyetheramine with oxypropylene repeat units). The paper’s Methods section details stoichiometries, cure schedules, and the property suite evaluated both in simulation and experiment, including density, glass transition temperature, coefficient of thermal expansion, and elastic modulus. For simulation specifics beyond the extract, the formatted article and Supporting Information should be consulted.

## Findings

The abstract states that cyclic curing agents produce spatial heterogeneity resolvable after annealing, that aliphatic systems show the most pronounced strain-rate sensitivity in MD relative to aromatic systems, and that overall the accelerated cross-linking route tracks experimental thermo-mechanical trends when curing chemistry is varied. The introduction positions these outcomes as evidence that reactive MD with targeted acceleration can translate variable chemical structure into measurable bulk responses for thermosets, reducing purely empirical screening.

Experimentally, the article cures EPON 828 with DETDA, IPDA, and JEFFAMINE T-403 under supplier-defined formulations, then measures density, glass transition temperature, coefficient of thermal expansion, and elastic modulus for comparison to the virtually cross-linked networks. That pairing is what motivates the claim that accelerated ReaxFF cross-linking plus virtual testing captures how curing-agent class shifts bulk thermo-mechanical observables, not only local connectivity statistics.

## Limitations

Proof PDFs may omit final figure quality, line numbers, and editorial corrections present in the version of record. The local extract is page-limited; numerical benchmarks and full simulation protocols should be verified against the published PDF.

## Related topics

- [[2018vashisth-j-phys-chem-accelerated-reaxff]]
- [[reaxff-family]]
