---
id: concept:theme-ferroelectrics-polar-oxides
type: concept
title: "Theme: ferroelectrics and polar oxide dielectrics"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - method:reaxff
  - task:application
candidate_tags: []
source_refs:
  - paper_id: "paper:2019akbarian-physical-che-understanding-influence"
    note: "BaTiO3 defects and switching; ReaxFF"
  - paper_id: "paper:2022yawei-gao-j-phys-chem-al-reaxff"
    note: "Al-containing ferroelectric-adjacent ReaxFF"
  - paper_id: "paper:2024baksa-adv-elect-ma-strain-fluctuations"
    note: "Strain fluctuations in ferroelectric contexts"
supported_by:
  - "paper:2019akbarian-physical-che-understanding-influence"
---

<!-- id:concept:theme-ferroelectrics-polar-oxides -->

!!! abstract "TL;DR"

    **Perovskite** and related **polar oxide** problems appear in the corpus through **ReaxFF** studies of **defects**, **domain-scale** behavior, and **strain** coupling. The flagship entry for **BaTiO₃**-style questions in frozen eval **FE1** is [[2019akbarian-physical-che-understanding-influence]].

## Scope

**In:** **ABO₃**-like and **titanate** systems where **polarization** or **defect chemistry** is simulated reactively.

**Out:** generic **TiO₂** surface chemistry without ferroelectric context → see [[theme-oxides-silica-ceramics]].

## Representative papers

- **BaTiO₃ / defects / switching:** [[2019akbarian-physical-che-understanding-influence]] — **FE1** gold.  
- **Al / ferroelectric-adjacent parameterization:** [[2022yawei-gao-j-phys-chem-al-reaxff]].  
- **Strain / electromechanical coupling:** [[2024baksa-adv-elect-ma-strain-fluctuations]].

## Methods and limitations

**ReaxFF** captures **local** bond rearrangements; **long-range depolarization** and **finite electric fields** may require **continuum** or **DFT** augmentation not present in every note.

## Related

- [[theme-oxides-silica-ceramics]]  
- [[reaxff-family]]  

??? info "Maintainers"

    Tag: `domain:ferroelectrics-polar`. Cross-link new perovskite slugs as they appear.
