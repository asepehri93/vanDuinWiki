---
id: concept:theme-ferroelectrics-polar-oxides
type: concept
title: "Theme: ferroelectrics and polar perovskite oxides (corpus)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:ferroelectrics-polar
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2024baksa-adv-elect-ma-strain-fluctuations"
    note: "BaZrO₃ elastic properties; NN potential"
  - paper_id: "paper:2023roshan-venue-paper"
    note: "Perovskite / high-T oxide mechanics"
  - paper_id: "paper:2025krstic-venue-paper"
    note: "High-temperature oxide behavior"
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Li-ion electrolytes (oxide chemistry overlap)"
supported_by:
  - "paper:2024baksa-adv-elect-ma-strain-fluctuations"
  - "paper:2023roshan-venue-paper"
---

<!-- id:concept:theme-ferroelectrics-polar-oxides -->

!!! abstract "TL;DR"

    This cluster covers **polar perovskites** and **functional oxides** where **elastic**, **thermal**, or **defect** behavior is studied with **atomistic** models. It overlaps [[theme-oxides-silica-ceramics]] for **oxide chemistry** but emphasizes **ABO₃** systems and **electromechanical** response.

## Scope (in / out)

**In corpus:** **BaZrO₃**, **perovskite** high-temperature mechanics, and related **oxide** notes tagged `domain:ferroelectrics-polar`.

**Out of scope here:** **silica** and **non-perovskite** ceramics unless the paper page explicitly bridges (see cross-links).

## Literature review (this knowledge base)

Corpus-limited synthesis; follow `[[slug]]` pages for **equations**, **simulation setup**, and **primary citations**.

### Elastic properties and strain fluctuations

[[2024baksa-adv-elect-ma-strain-fluctuations]] is a central KB page for **elastic constants** via **strain-fluctuation** methods using a **neural network potential** for **BaZrO₃**. It is the strongest link between this theme and [[theme-ml-atomistic-potentials]].

### High-temperature mechanics and perovskite oxides

[[2023roshan-venue-paper]] and [[2025krstic-venue-paper]] provide **high-temperature** / **perovskite** oxide content in the KB; read each note for **whether ferroelectric order** is central or **mechanical/thermal** response is the focus.

### Electrolytes and polar oxide chemistry (adjacent)

Solid-state **Li-ion electrolyte** interface chemistry in [[2018shin-physical-che-development-reaxff]] connects **polar oxide** environments to [[batteries-interfaces-reaxff]] rather than bulk ferroelectric switching.

## Debates, tensions, and cross-references

- **Classical vs MLIPs** for **anharmonic** thermal properties: [[reaxff-vs-mlip-accuracy]], [[2024baksa-adv-elect-ma-strain-fluctuations]].  
- **Domain switching** vs **defect chemistry**: the KB may not cover every **ferroelectric switching** mechanism—check paper pages rather than assuming completeness.  
- **Related themes:** [[theme-oxides-silica-ceramics]], [[theme-ml-atomistic-potentials]], [[theme-water-silica-geo]] (surface hydration of oxides).

## Representative entry points

- **BaZrO₃ + elasticity / NN potential:** [[2024baksa-adv-elect-ma-strain-fluctuations]].  
- **Perovskite / high-T:** [[2023roshan-venue-paper]], [[2025krstic-venue-paper]].  
- **Domain index:** [[paper-index-by-domain]] (`domain:ferroelectrics-polar`).

## Methods and limitations

**Harmonic** approximations and **small-cell** elastic sampling can mis-estimate **soft modes** near **phase boundaries**. **Polarization** in MD requires **careful** definitions when comparing to continuum **ferroelectric** theory.

??? info "MAS / retrieval"

    **id:** `concept:theme-ferroelectrics-polar-oxides`. When new perovskite papers are ingested, tag `domain:ferroelectrics-polar` and add a bullet here if the theme narrative should cite them.
