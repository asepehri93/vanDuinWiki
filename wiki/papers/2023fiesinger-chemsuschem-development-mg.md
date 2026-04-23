---
id: paper:2023fiesinger-chemsuschem-development-mg
type: paper
title: "Development of a Mg/O ReaxFF Potential to describe the Passivation Processes in Magnesium-Ion Batteries"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:lammps
candidate_tags: []
source_refs: []
doi: "10.1002/cssc.202201821"
year: 2023
authors:
  - "Florian Fiesinger"
  - "Timo Jacob"
  - "Adri C. T. van Duin"
venue: "ChemSusChem"
pdf_sha256: "e8620167589a5a609b2eec0981573979a02daa28f6708cc7d0ef7b69515a29aa"
pdf_path: "papers/Fiesinger_ChemSusChem_2022_MgO.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2023fiesinger-chemsuschem-development-mg -->

## Summary

A **Mg/O ReaxFF** parameter set is trained against **DFT** data to capture **bulk Mg and MgO**, **low-index Mg surfaces**, **adsorption**, and **diffusion**, then applied to **O₂ attack on Mg anode facets** and related oxidation pathways relevant to **magnesium-ion battery** anode **passivation** by oxygen impurities. The framing emphasizes that **trace O₂** exposure can dominate early-stage interface evolution even when electrolyte chemistry is nominally “dry,” so an accurate **Mg/O** reactive model is a prerequisite for realistic anode simulations. The introductory discussion in *ChemSusChem* stresses **Mg-ion battery** deployment barriers around **passivating** **interphases** at **Mg** anodes and positions **O₂** impurities as a chemically simple yet practically important oxidation channel to model before tackling full **electrolyte** complexity.

## Methods

### ReaxFF training against DFT (A)

- **Mg metal:** **hcp**, **fcc**, **bcc**, **A15**, **sc** **equations of state**, **cohesive energies**, **bulk moduli**, and **low-index surface energies**.
- **Mg–O:** **Bulk MgO**, **adsorption**, and **surface** scenarios; **diffusion barriers** and other targets summarized in **ChemSusChem** + **SI**.
- **QM level:** **DFT** settings described in the paper feed the weighted optimization.

### Validation simulations (B / GCMC + MD)

- **GCMC + MD:** **Oxidation** of a **Mg nanoparticle** + **high-T anneal** (~**2000 K**) to form **rocksalt MgO**.
- **Facet MD:** **O\(_2\)** on **Mg(0001)**, **Mg(10̄10)A**, **Mg(10̄11)**—track **dissociative adsorption**, **exothermic heating**, **oxide** **thickness** (up to **~25 Å** on the most reactive facet), and **grain-boundary** microstructure.

### Analysis emphasis

Compare facets by **oxide thickness**, **local temperature rise**, and **defect** content—not terrace **adsorption energy** alone.

### MD application (integrated)

**Engine / code:** **LAMMPS** and **ReaxFF**. **Systems:** **O\(_2\)** on **Mg** **nanoparticle** and **(0001)**, **(10̄10)A**, **(10̄11)** **slabs**; **GCMC + MD** plus **~2000 K** **high-T** anneal in *ChemSusChem* (see full paper for high-**T** segments). **PBC** for **slabs**; **3D** **nanoparticle** cell. **N/A — full atom counts, exact timestep, ps/ns** segment lengths, **thermostat** damping, **NVT** setpoints, **NPT** usage, **QEq** and **long-range** settings, **O\(_2\)** **dosing** *pressures* in **SI**—**not re-listed** on this page to avoid **inventing** numbers. **N/A — applied electric field; N/A — umbrella/REX** in the main **O\(_2\)** line described.

## Findings

### Exothermic oxidation

**O\(_2\)** **dissociates on contact**, releasing enough energy to heat surfaces to **thousands of kelvin** in trajectories, accelerating **MgO** formation.

### Facet ranking

**Mg(10̄10)A** is the **most reactive** facet examined, supporting the **thickest** transient **MgO** film.

### Training-set quality

The field matches key **DFT** metrics with documented limitations (e.g. **bulk modulus** trends) in the article.

### Multiscale implication

**Localized hot spots** and **grain boundaries** in nascent oxides arise from **exothermic** **O** incorporation—motivating **heat dissipation** models beyond isothermal **MD**.

The abstract-level narrative also highlights that **O₂** **dissociates on first contact** with modeled **Mg** facets, **heating** surfaces to **several thousand kelvin** and driving rapid **rocksalt** **MgO** formation—consistent with the **thick** transient films and **facet-dependent** reactivity summarized above.

## Limitations

ReaxFF remains **semi-empirical**; quantitative oxidation kinetics and oxide electronic structure require validation against experiment and higher-level theory for specific electrolyte environments.

## Relevance to group

Direct **ReaxFF parameterization** collaboration (**van Duin**) on **Mg/O** chemistry for **metal-anode passivation**, adjacent to broader **battery interface** simulation themes.

## Citations and evidence anchors

- DOI: [10.1002/cssc.202201821](https://doi.org/10.1002/cssc.202201821)

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
