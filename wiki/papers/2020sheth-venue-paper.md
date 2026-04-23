---
id: paper:2020sheth-venue-paper
type: paper
title: "Influence of acid leaching surface treatment on indentation cracking of soda lime silicate glass (galley proof PDF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:berendsen-thermostat
  - keyword:galley-or-proof-pdf
  - keyword:npt-simulation
  - keyword:nvt-simulation
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.jnoncrysol.2020.120144"
year: 2020
authors:
  - "Nisha Sheth"
  - "Seung Ho Hahn"
  - "Dien Ngo"
  - "Alexandra Howzen"
  - "Raul Bermejo"
  - "Adri C. T. van Duin"
  - "John C. Mauro"
  - "Carlo G. Pantano"
  - "Seong H. Kim"
venue: "Journal of Non-Crystalline Solids (Elsevier proof PDF)"
pdf_sha256: "085115c18bca04d86d84681713a9eaaf1942c30949dec48a1196e66dbc9916ec"
pdf_path: "papers/Sheth_JNonCrystSol_2020_Acid_Leaching_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2020sheth-venue-paper -->

This ingest registers a **galley / uncorrected proof** PDF for the same peer-reviewed article as **`[[2020sheth-journal-of-n-influence-acid]]`**. The narrative below matches that work so operators can use either local file without losing scientific content.

## Summary

Prior studies showed that water or acid soaking can increase the strength of soda lime silicate (SLS) glasses. This paper demonstrates that acid leaching increases the apparent crack resistance of the leached surface during Vickers indentation. Controlled-environment indentation reveals a humidity dependence of radial cracking, implicating transport of water through the leached surface layer in crack paths toward the free surface. Reactive molecular dynamics with a Na/Si/O/H ReaxFF parametrization indicates that the leached layer can undergo pressure-induced mechanochemical reactions during indentation that increase bridging-oxygen connectivity in the near-surface silica network and hinder molecular water transport toward subsurface crack tips. The authors synthesize experiment and simulation into a hypothesis that load-driven restructuring lowers water transport kinetics to critical flaws, producing enhanced apparent crack resistance.

## Methods

Experiments use remelted SLS bottle glass with bulk composition stated in the article, polished and fire-polished coupons, and acid leaching in hot hydrochloric acid at controlled pH. Vickers indentation is performed under dry versus humid nitrogen, with the abstract tying radial crack behavior to environmental humidity. Reactive MD employs the Na/Si/O/H ReaxFF implementation in ADF with a 0.25 fs timestep, Verlet integration, and Berendsen thermostat (100 fs damping) and barostat (5 ps damping) where NPT is used. The leached region is mimicked by partial Na⁺→H⁺ exchange in a ~4.30 × 4.37 × 12.05 nm periodic cell of a simplified glass, with NVT equilibration at 300 K followed by NPT hydrostatic pressure scans (0.1–10 GPa in 100 ps segments) and final relaxation at 1 atm. Full experimental and simulation boundary conditions appear in the version-of-record PDF and any supporting information.

## Findings

Acid leaching increases apparent surface crack resistance under indentation relative to the polished baseline in the reported experiments. Radial cracking depends on humidity, supporting a mechanistic role for water transport through the thin leached layer even when the layer is much shallower than the indent depth. Simulations suggest pressure-induced reactions in the leached layer that increase Si–O–Si connectivity and impede water transport toward the crack tip, aligning with the proposed transport-limited explanation for humidity-dependent cracking.

## Limitations

Galley PDFs may differ in pagination and minor wording from the **Journal of Non-Crystalline Solids** version-of-record. The reactive model simplifies real SLS chemistry and mechanical loading fields around a Vickers tip.

## Relevance to group

Duplicate corpus path for a van Duin co-authored **glass surface** / **ReaxFF** study; prefer **`[[2020sheth-journal-of-n-influence-acid]]`** when citing the cleaner PDF hash.

## Citations and evidence anchors

- DOI: [10.1016/j.jnoncrysol.2020.120144](https://doi.org/10.1016/j.jnoncrysol.2020.120144)

## Related topics

- [[2020sheth-journal-of-n-influence-acid]]
- [[reaxff-family]]
