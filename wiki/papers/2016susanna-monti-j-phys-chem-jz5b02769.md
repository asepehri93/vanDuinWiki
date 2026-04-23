---
id: paper:2016susanna-monti-j-phys-chem-jz5b02769
type: paper
title: "Simulation of Gold Functionalization with Cysteine by Reactive Molecular Dynamics"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reactive-md
  - material:metal-surface
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpclett.5b02769"
year: 2016
authors:
  - "Susanna Monti"
  - "Vincenzo Carravetta"
  - "Hans Ågren"
venue: "J. Phys. Chem. Lett. (2016) 7, 272–276"
pdf_sha256: "56c17d9b374105dd6174e0c16ef85eb46978f226c489bfa5a9043c47fc03ca81"
pdf_path: "papers/ReaxFF_others/Monti_Cystein_Gold_JPC_Letter_2016.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:water-interfaces
  - keyword:neb
  - keyword:dft-static
---
<!-- id:paper:2016susanna-monti-j-phys-chem-jz5b02769 -->

## Summary

The paper studies **cysteine** adsorption on **Au** in **aqueous solution** using **quantum chemistry (QC)** plus **reactive classical MD (RC-MD)** with a **modified protein-oriented ReaxFF** in which **Au–biomolecule** interactions are **reparametrized from QC**. **Nudged elastic band (NEB)** estimates **reaction barriers**, checked against QC. The work emphasizes a **two-stage** binding (**slow physisorption**, then **fast chemisorption**) and documents **Au surface reconstructions** that further stabilize the adsorbate. **Thiol–gold** binding underpins **nanoparticle** functionalization and **biosensing** architectures; the authors position **atomistic** pathways as a bridge between **gas-phase** **cluster** studies and **solution-phase** **experiments** on **citrate-capped** **Au** colloids (introduction themes).

## Methods

**1 — MD application (ReaxFF RC-MD).** **Reactive classical MD (RC-MD)** uses the **ReaxFF** implementation in **Amsterdam Density Functional (ADF)** as stated in the letter. The model cell contains **one cysteine**, **303** explicit **water** molecules, and an **Au(111)** slab (**10** layers of **90** **Au atoms** each) in a simulation box of order **26 × 25 × 70 Å** (in **x**, **y**, **z**). Simulations are **NVT** at **T = 300 K** and **ambient pressure** (no separate **barostat** details beyond that statement in the excerpt). **Timestep** is **0.25 fs**; **temperature** is controlled with a **Berendsen thermostat** (relaxation constant **0.1 ps**). **Equilibration** runs **25 ps**; the **production** segment saves configurations every **0.025 ps** for a total elapsed time of about **100 ps**. **Nudged elastic band (NEB)** estimates **barriers** for key **Au–S** steps with **quantum-chemistry** checks. **PBC** apply in the simulation box. **Shear**, **shock**, applied **electric field** driving, and **umbrella**/**metadynamics**/**replica-exchange** sampling are **N/A —** not used in the protocol described in the indexed letter text.

**2 — Force-field training.** **DFT/QM** **reference energies** and **structures** for **Au–thiol** interactions train **patch** parameters starting from the conjunction of a **protein ReaxFF** and **van Duin**-line **Au** parameters, combined with additional **QC** data (see **Supporting Information** in the article). Optimization uses the procedure built into the **serial ReaxFF** code referenced there. The fitted field is validated against **QC** data not used in training and against **ab initio molecular dynamics** benchmarks reported in the SI.

**3 — Static QM / DFT.** **QC**/**DFT** levels for the training and **NEB** checks are documented in the letter and **`[[2016susanna-venue-paper-2]]`** (**N/A —** full tables not duplicated here).

## Findings

- RC-MD supports a concrete **adsorption–reaction route** consistent with a **two-step** mechanism (**physisorption** followed by **chemisorption**) in line with experimental reports cited by the authors.
- **Surface reconstructions** on **Au**, driven by strong adsorption, are identified and interpreted as **additional stabilizers** of the adsorbate state.
- Overall **QC/experiment** consistency is argued to validate using reactive MD to follow **local** adsorption dynamics on **selected** interfaces.

- **Implication:** **reactive** **MD** with **metal-specific** **ReaxFF** patches is presented as a practical compromise between **full** **QM/MM** and **non-reactive** **classical** **force fields** for **bio–inorganic** **interfaces** (discussion framing).

## Limitations

- Force-field fidelity is concentrated in the **Au–biomolecule** extensions; other environments (different pH, impurities, complex protein sequences) may need additional parametrization.
- Sampling length scales and system sizes remain **classical-MD** limited despite reactivity.

- **pH** and **counter-ion** effects in **real** **electrolytes** can shift **thiol** **deprotonation** and **Au** **charge** states beyond the **explicit** **water** models used here.

## Relevance to group

Demonstrates **ReaxFF extension** for **bio–inorganic interfaces** (Au–thiol chemistry) with **QC-trained** metal–organics terms—methodologically adjacent to peptide-on-Au workflows in the corpus.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpclett.5b02769](https://doi.org/10.1021/acs.jpclett.5b02769)
- Text-aligned pointers: `normalized/extracts/2016susanna-monti-j-phys-chem-jz5b02769_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[2016xin-li-j-chem-theor-ct6b00283]]
