---
id: paper:2016osti-venue-microsoft-word
type: paper
title: "Supporting information: Effect of metal ion intercalation on the structure of MXene and water dynamics on its internal surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:water-interfaces
  - keyword:2d-materials
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.6b01490"
year: 2016
authors:
  - "Naresh C. Osti"
  - "Eugene Mamontov"
venue: "ACS Appl. Mater. Interfaces 2016 (Supporting Information)"
pdf_sha256: "86ead778c0ad9dcda0629155a697e24c13765de79ebad8eae116a3fc366902a2"
pdf_path: "papers/Osti_ACS_AMI_Water_Mxene_SI_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016osti-venue-microsoft-word -->

## Summary

This Supporting Information PDF accompanies the ACS Applied Materials & Interfaces letter DOI `10.1021/acsami.6b01490` on potassium-intercalated Ti₃C₂Tₓ MXene and dynamics of water confined between its internal surfaces, studied with a combination of experimental scattering and molecular simulations described in the main text. The SI expands on sample preparation, measurement protocols, and simulation setup details referenced by figure and table callouts in the primary article. It is the appropriate place to recover extended procedural text—such as MXene synthesis from Ti₃AlC₂ via HF etching, aqueous KOH intercalation with washing and centrifugation, vacuum annealing, pellet preparation for oriented quasi-elastic neutron scattering samples, and data-reduction notes—that would be unwieldy in the short letter format.

## Methods

**Supporting Information scope.** Section I of the SI expands experimental preparation relative to the main letter: Ti\(_3\)AlC\(_2\) precursors etched with **HF (48%)** at room temperature for **24 h**, washed to neutral pH, converted to Ti\(_3\)C\(_2\)T\(_x\), soaked in **2 M KOH** (1 g solid per 10 mL) with repeated stirring/centrifugation cycles, filtered, air-dried (**18 h**), then vacuum-annealed (**110 °C**, **4 h**) before additional XRD. Pressed oriented discs (**~300 MPa**) seal in aluminum holders for QENS as described in the SI excerpt.

**Scattering and analysis.** The SI documents SANS instrument settings, QENS sample geometry, and data-reduction notes referenced by Figure S2 and related panels in the letter.

**MD companion simulations.** Thermostat choices, water content, interlayer spacing construction, and ReaxFF run parameters for confined-water dynamics appear in the SI sections cross-referenced by [[2016osti-venue-am6b01490]]; this page does not duplicate those tables. The SI supports the letter’s conclusions rather than introducing a separate hypothesis. It does not document a new force-field training study or standalone static QM campaign.

## Findings

The SI spells out how HF etching, 2 M KOH intercalation with repeated stirring and centrifugation, washing, air drying, and 110 °C vacuum annealing prepare Ti\(_3\)C\(_2\)T\(_x\) powders whose diffraction and scattering results appear in the letter. Supplementary figures (SEM, SANS, and panels cited from the letter) support statements about interlayer water populations and K\(^+\)-induced gallery swelling. Pristine versus K\(^+\)-intercalated preparation and scattering pipelines are laid out side by side so SI metrics can be checked against main-text panels; sample-history sections highlight levers such as KOH concentration, soak and stir times, and anneal duration that move interlayer spacing and confined-water content before QENS. Supporting information can lag minor corrections to the main article, so device-level stability claims should still anchor on the primary letter first.

This file is **SI-only** for DOI `10.1021/acsami.6b01490`; it does not replace the version-of-record article [[2016osti-venue-am6b01490]] for pagination or figure numbering.
## Limitations

Supporting information can lag minor corrections to the main article. Scientific interpretation should always cite the primary letter first.

## Relevance to group

Van Duin-coauthored MXene hydration work; SI supports reproducibility for intercalation and confined-water modeling.

The SI is particularly important for reconciling simulation cell choices with experimental interlayer spacing inferred from scattering, because confined-water dynamics are sensitive to basal spacing, edge terminations, and potassium stoichiometry. When extending the study to new intercalants or hydration levels, revisit both the experimental preparation chain documented here and the MD equilibration assumptions referenced from the main letter.

Replication checklists should explicitly verify that simulation water content and confinement length scales map to the interlayer spacings reported in the SI tables, not only to nominal bulk hydration targets.

## Reader notes (navigation)

- [[2016osti-venue-am6b01490]]
- [[batteries-interfaces-reaxff]]
