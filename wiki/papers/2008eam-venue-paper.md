---
id: paper:2008eam-venue-paper
type: paper
title: "An embedded-atom method interatomic potential for Pd–H alloys"
updated: "2026-04-20"
confidence: high
paper_keywords:
  - keyword:eam-potential
  - keyword:classical-ff
  - keyword:metallic-systems
  - keyword:validation-experiment
canonical_tags:
  - domain:alloys-metallurgy
  - domain:classical-ff-specialized
  - material:alloy-bulk
  - method:classical-md
  - task:parameterization
  - task:validation
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1557/JMR.2008.0090"
year: 2008
authors:
  - "X. W. Zhou"
  - "J. A. Zimmerman"
  - "B. M. Wong"
  - "J. J. Hoyt"
venue: "Journal of Materials Research 23 (3), 704–718 (2008)"
pdf_sha256: "15627774bdc020ff328f6086f9b00e85e8572a1cadf9323b79ff34f1e0d8e576"
pdf_path: "papers/Others/EAM_PdH_JMR.2008.0090.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2008eam-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the **Journal of Materials Research** article identified by `doi`. Numeric examples (e.g., H:Pd concentrations) appear in the extract as printed.

## Summary

The authors extend an existing **palladium EAM** description to a **Pd–H** EAM potential by **normalizing** elemental **embedding energy** and **electron density** functions, targeting a model that works across the full hydrogen composition range **\(0 \le x \le 1\)** for PdH\(_x\)-like phases. The abstract states the potential predicts **lattice constants**, **cohesive energies**, and **elastic constants** for Pd, H, and PdH\(_x\) across compositions, correct **octahedral** hydrogen interstitial sites, reproduces the **α/β phase miscibility gap** (plateau behavior), and preliminary MD captures **phase stability**, **hydrogen diffusion mechanism**, and **mechanical response**.

## Methods


The interatomic model is an embedded-atom method (EAM) potential in the Daw–Baskes spirit: total energy combines environment-dependent embedding energies \(F_i(\bar{\rho}_i)\) evaluated at atomic electron densities \(\bar{\rho}_i\) superposed from neighboring atoms, plus pairwise terms \(\phi_{ij}(r_{ij})\) and atomic electron-density functions \(\rho_j^a(r)\) as in Equations (1)–(2) of the paper. The authors extend an existing palladium EAM description by normalizing elemental embedding-energy and electron-density functions to build a Pd–H alloy potential intended to span the full hydrogen composition range \(0 \le x \le 1\) for PdH\(_x\)-like phases, including correct octahedral hydrogen sites and the \(\alpha/\beta\) miscibility gap that many earlier Pd–H models missed or misrepresented (including incorrect tetrahedral occupancy in some parametrizations). The manuscript documents how model functions and parameters are obtained and reports lattice constants, cohesive energies, elastic constants, phase behavior, hydrogen diffusion, and mechanical response from the fitted potential (including preliminary MD in the abstract).

### MD application (abstract-level)

The abstract reports **preliminary molecular dynamics** for **phase stability**, **hydrogen diffusion**, and **mechanical response** using the fitted **Pd–H** **EAM**. **N/A — MD code name** in the short extract; **N/A — supercell sizes and stoichiometry** line-by-line; **N/A — PBC** details; **N/A — NVE/NVT/NPT** labels; **N/A — timestep**; **N/A — trajectory lengths** (no **ps**/**ns** schedule in the excerpt); **N/A — equilibration** segments as reported in the abstract; **N/A — thermostat**; **Barostat:** **N/A — NPT** protocol not stated in the excerpt; **Temperature:** **room temperature** appears in the wiki summary for the **α/β** discussion; **Pressure / stress:** **ambient pressure** framing in the introduction; **mechanical** **stress–strain** behavior referenced at abstract level—see **`pdf_path`** for protocols. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

### Force-field training

**Parent FF / elements:** **EAM** for **Pd–H** built by **normalizing** an existing **Pd** **EAM** embedding/density description to span **PdH\(_x\)** (**0 ≤ x ≤ 1**). **QM reference:** **N/A — DFT/QM training** not summarized from the short extract (the fit emphasizes **experimental** **lattice**, **cohesive**, and **elastic** data plus **phase** behavior); verify **`pdf_path`** for any **QM** benchmarks. **Training set / reference data:** **experimental** **lattice constants**, **cohesive energies**, **elastic constants**, **α/β** **plateau** / **miscibility gap**, and **octahedral** **H** site preferences as described in the article. **Optimization:** parameters obtained via the manuscript’s fitting strategy (see PDF for objective/weights). **Reference data used:** **experiment**-anchored **validation** of **EOS**-like quantities and **phase** behavior; **MD** as an additional **validation** modality in the abstract.

## Findings

Near **room temperature** and **ambient pressure**, dilute **\(\alpha\)**-phase Pd–H and concentrated **\(\beta\)**-phase hydride compositions (the introduction cites representative **H/Pd** contents of order **0.03** and **0.60**, respectively) bracket the **plateau** behavior the potential targets. The fitted **Pd–H EAM** reproduces reported **lattice constants**, **cohesive energies**, and **elastic constants** for **Pd**, **H**, and **PdH\(_x\)** across compositions, enforces **octahedral** **H** sites, reproduces the **\(\alpha/\beta\)** **miscibility gap**, and **preliminary MD** reports consistent **phase stability**, **H** **diffusion** behavior, and **mechanical** response. **Corpus honesty:** `extraction_quality` is **partial**; use **`pdf_path`** for complete tables.

## Limitations

`extraction_quality` is **partial** in the normalized record; rely on the PDF for complete potential forms and validation tables. The model is fixed-bonding EAM physics, not a bond-order reactive framework such as ReaxFF.

## Relevance to group

Useful comparator for **metal–hydrogen** parameterization culture and for **large-scale MD** of hydrides adjacent to reactive workflows.

## Citations and evidence anchors

- DOI: `10.1557/JMR.2008.0090`.
- PDF: `papers/Others/EAM_PdH_JMR.2008.0090.pdf`.
- Extract: `normalized/extracts/2008eam-venue-paper_p1-2.txt`.

## Related topics

- [[material:alloy-bulk]]
