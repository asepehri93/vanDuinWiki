---
id: paper:2018zhang-venue-research
type: paper
title: Improvement of the ReaxFF Description for Functionalized Hydrocarbon/Water
  Weak Interactions in the Condensed Phase (proof PDF)
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:reaxff-lineage
- method:reaxff
- task:validation
- scale:atomistic
paper_keywords:
- keyword:galley-or-proof-pdf
- keyword:reaxff-parameterization
- keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: 10.1021/acs.jpcb.8b01127
year: 2018
authors:
- Weiwei Zhang
- Adri C. T. van Duin
venue: J. Phys. Chem. B (proof PDF in corpus)
pdf_sha256: 36d641d45ec55c6b37db262b565f13ec8cc85bbeb18dc7f6ecd33106bf23581c
pdf_path: papers/Zhang_JPCB_Weak_Interactions_2018_proof.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018zhang-venue-research -->

??? info "PDF variant"
    ACS **line-numbered proof**. Canonical note: [[2018zhang-j-phys-chem-improvement-reaxff]] with non-proof PDF when available.

## Summary

The proof PDF `papers/Zhang_JPCB_Weak_Interactions_2018_proof.pdf` corresponds to *J. Phys. Chem. B* DOI `10.1021/acs.jpcb.8b01127`, “Improvement of the ReaxFF Description for Functionalized Hydrocarbon/Water Weak Interactions in the Condensed Phase.” The abstract in the extract states that the **protein-2013** aqueous ReaxFF branch simulates biomolecules and membrane fuel cells but **inaccurately** describes weak interactions of functionalized hydrocarbons with water in condensed phases, **especially densities**. It introduces **CHON-2017_weak** built on protein-2013 to improve C/H/O/N weak interactions, validated with MD showing **experimental density trends** for pure and mixed systems, **hexane–water** phase separation, and **ethanol** or **tetramethylammonium (TMA)** dissolution. For alkaline membrane fuel cells, it reports structural properties and **TMA degradation** chemistry in alkaline water, plus small-molecule reaction benchmarks, and states an **additional degradation pathway** for TMA appears **more energetically favorable** than the main mechanism from prior QM studies.

## Methods

This slug indexes an ACS **line-numbered proof** of the same DOI as [[2018zhang-j-phys-chem-improvement-reaxff]]; use that **version-of-record** page for definitive tables.

**Force-field training (proof text).** The **Introduction** on the proof PDF explains **QM**/**DFT** cost limits versus **ReaxFF**, contrasts generic **MM** force fields (AMBER, CHARMM, OPLS, etc.), and traces **protein-2013** lineage: first-row **carbon** from **C/H/O-2008 combustion** training, **oxygen**/**hydrogen** from the first-generation **water** line, **nitrogen** from glycine-in-water extensions. It records **protein-2013** weaknesses—**liquid water** **density** underestimated, **hydrocarbon** **density** overestimated—that motivate **CHON-2017_weak** while preserving prior AEM-related successes. **Training** targets, **optimization** steps, and **reference data** tables match the issue article.

**MD application (proof text mirrors the issue article).** **Engine / code:** **LAMMPS** + standalone **ReaxFF** development path as in §2.2 of the **JPCB** article. **System / composition:** validation **supercells** include **~500**-**molecule** **liquid water** boxes, **~200**-molecule **n-alkane** **periodic** cells, **hexane–water** mixtures, **TMA**/**OH⁻**/water compositions, and **crystal** **amino acid** cells as enumerated in §2.2—see the **supercell** **atom** counts in the issue **PDF** for each figure. **Ensemble / protocol:** **NPT** equilibration of **liquid** **densities** from **low-density** starts, then **500 ps** **NPT** at **room temperature** (density averaged **last 400 ps**); **500 ps NVT** segments for **RDF**/**MSD** and **TMA/OH⁻/water** mixtures; **amino acid crystals** use **100 K NPT** to limit thermal noise. **Timestep 0.25 fs**; **Berendsen** **thermostat** with **100 fs** damping for **NVT** and **2500 fs** **pressure** damping for **NPT**. **PBC** in all directions. For line-level tables and any proof-vs-issue deltas, prefer **`[[2018zhang-j-phys-chem-improvement-reaxff]]`**.
## Findings

Qualitative conclusions follow the abstract above; numerical density deviations and reaction energetics should be read from the version-of-record PDF linked on the canonical page. The proof extract also notes prior AEM studies of **functionalized poly(phenylene oxide)** membranes where ReaxFF predicted hydroxide and water diffusion constants successfully and captured degradation trends for large hydrophilic cations—context for why TMA chemistry is used as a validation case for CHON-2017_weak. Proof line numbers and placeholder page fields (“XXXX”) in the extract header should not be used as citation locators; migrate to the issue PDF when available.

## Limitations

Proof PDFs can differ in pagination from the final issue. Operators should migrate citations to the non-proof file when ingested.

## Relevance to group

Van Duin-group aqueous-branch ReaxFF refinement for biomolecular and fuel-cell-adjacent electrolyte modeling.

CHON-2017_weak is explicitly positioned as fixing condensed-phase densities and mixing behavior where protein-2013 struggled; applications that rely on accurate hydration free energies should cite validation cases in the JPCB article (pure liquids, mixtures, and TMA chemistry) rather than assuming transfer to arbitrary organics without testing.

Alkaline fuel-cell degradation pathways for TMA involve multiple protonation states; reproducers should verify that their simulation pH and hydroxide count match the cases enumerated in the published article’s Methods.

## Reader notes (navigation)

- [[2018zhang-j-phys-chem-improvement-reaxff]]
- [[reaxff-family]]

## Citations and evidence anchors

DOI: `10.1021/acs.jpcb.8b01127`.
