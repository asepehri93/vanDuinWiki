---
id: paper:2014rahnamoun-venue-research
type: paper
title: "Reactive molecular dynamics simulation on the disintegration of Kapton, POSS polyimide, amorphous silica, and Teflon during atomic oxygen impact using the ReaxFF reactive force-field method"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - domain:oxides-ceramics
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:oxide-surface
  - keyword:combustion
  - keyword:nvt-simulation
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1021/jp4121029"
year: 2014
authors:
  - "A. Rahnamoun"
  - "Adri C. T. van Duin"
venue: "The Journal of Physical Chemistry A"
pdf_sha256: "859d17042be66d2e1d8483b36a940a18ee50c8922589a1e0b56148fd477ae4ee"
pdf_path: "papers/Rahnamoun_Kapton_JPCA_2014_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014rahnamoun-venue-research -->

!!! abstract "Large-scale ReaxFF MD compares Kapton, POSS polyimide, amorphous silica, and Teflon under low Earth orbit–like atomic oxygen impacts; relative damage resistance, silicon-doping ideas for Kapton, and faster heat transfer reducing disintegration are discussed."

## Summary

This study models **atomic oxygen (AO) bombardment** of spacecraft-relevant materials—**Kapton polyimide**, a **POSS-containing polyimide**, **amorphous silica**, and **Teflon**—using **ReaxFF reactive molecular dynamics** to capture **bond-breaking chemistry** at impact-relevant conditions. The abstract reports comparative **disintegration/oxidation** behavior, with **Kapton less resistant than Teflon** in the simulations, **silica most stable** prior to strongly exothermic silicon oxidation, and qualitative agreement with experiment highlighted by the authors.

The paper also explores **Si doping in Kapton** as a stabilizing modification in the model setup and discusses how **increased heat transfer** during AO impact can reduce **material disintegration**, particularly emphasized for **silica** collisions.

Broader framing positions **ReaxFF** screening of **polymer**, **ceramic**, and **fluoropolymer** responses to **eV**-scale **AO** impacts as a complement to flight data when ranking **spacecraft** materials for **erosion** resistance under **oxidizing** beams.


Readers should verify numerical values, units, and section references against the peer-reviewed PDF and any Supporting Information, especially when extracts or galley PDFs truncate tables.

## Methods

Canonical protocol text matches **`[[2014rahnamoun-venue-jp4121029]]`** (same DOI); this page exists for **proof-PDF** provenance.

### Materials and reactive model

- **ReaxFF reactive MD** on atomistic targets of **Kapton**, **POSS–polyimide**, **amorphous silica**, and **Teflon** under **atomic oxygen** bombardment (**Summary**).

### Environmental / impact parameters

- Introduction cites representative **LEO** collision energies **~4.5 eV** for **AO** and **~8 eV** for **N₂** as **context** (not necessarily every in-sim impact energy).

### Heat-transfer studies

- Additional **canonical MD** runs probe **in-solid heat transfer** during impacts (see **jp4121029** article).

### Authoritative detail

- Use **`[[2014rahnamoun-venue-jp4121029]]`** + **JPCA** PDF for **supercells**, **schedules**, and **analysis** metrics; this proof slug is for **hash** tracking.

### 1 — MD application (same article as VOR sibling)

Treat **`[[2014rahnamoun-venue-jp4121029]]`** as the **pagination-canonical** Methods source. This **proof** PDF (`papers/Rahnamoun_Kapton_JPCA_2014_proof.pdf`) registers the **same DOI** with different bytes; `normalized/extracts/2014rahnamoun-venue-research_p1-2.txt` is **abstract/introduction–limited**. The **abstract** states simulations use the **ReaxFF reactive force-field program** to run **molecular dynamics (MD)** at sizes sufficient to capture **reactive** chemistry, and that **impact energies**, **material composition**, and **temperature** of the material are studied—without restating numerical protocol tables on this excerpt. **Engine beyond “ReaxFF program” naming, timestep, thermostat damping, PBC vectors, and total ps/ns production lengths:** **N/A —** copy from **`[[2014rahnamoun-venue-jp4121029]]`** §2–3 in `papers/Rahnamoun_Kapton_JPCA_2014.pdf`. **Stages:** the canonical indexed Methods excerpt records **geometry optimization** followed by **NVT equilibration** as early steps in each four-step workflow (**Figure 6** there). **Barostat / pressure control:** **NVT** staging is explicit on the canonical excerpt; **NPT** **pressure** servo — **N/A —** not indicated for those slab equilibration segments. **Ambient beam partial pressures / stress tensor targets:** **N/A —** not stated on the proof abstract pages. **Electric field / enhanced sampling:** **N/A —** not described for these AO impacts.

### 2 — Force-field training

**N/A —** application paper using **ReaxFF**; no new parameterization summary on the proof ingest page.

## Findings

**Outcomes, comparisons, and levers** match the **abstract** on **`[[2014rahnamoun-venue-jp4121029]]`**: **Kapton** < **Teflon** AO resistance in simulation (**experimental** agreement claimed); **silica** most stable until vigorous **Si oxidation**; **bulk Si** improves Kapton resilience; **heat-transfer** effects reduce **disintegration** (highlighted for **silica**).

**Corpus honesty.** This slug tracks **`papers/Rahnamoun_Kapton_JPCA_2014_proof.pdf`** bytes; cite **`[[2014rahnamoun-venue-jp4121029]]`** for **figure/section** locators and final layout.

## Limitations

- LEO environments include **electron/UV** effects and **contamination** not fully represented in a single AO-impact model class.
- The corpus PDF is labeled as a **proof**; cite the **journal version** for final figure numbering.

## Relevance to group

Strong **Penn State van Duin-group** application paper for **space-environment polymer/oxide degradation** with **ReaxFF**.

## Reader notes (navigation)

- Related slug [[2014rahnamoun-venue-jp4121029]] may duplicate the same DOI with a different PDF path—dedupe carefully in navigation indexes.

## Citations and evidence anchors

- DOI: [10.1021/jp4121029](https://doi.org/10.1021/jp4121029)
