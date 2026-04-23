---
id: paper:2020gkoura-biomicroflui-peculiar-size
type: paper
title: "The peculiar size and temperature dependence of water diffusion in carbon nanotubes studied with 2D NMR diffusion–relaxation D–T2eff spectroscopy"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:2d-layered
  - method:classical-md
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:water-interfaces
  - keyword:validation-experiment
  - keyword:classical-ff
source_refs: []
doi: "10.1063/5.0005398"
year: 2020
authors:
  - "L. Gkoura"
  - "G. Diamantopoulos"
  - "M. Fardis"
  - "D. Homouz"
  - "S. Alhassan"
  - "M. Beazi-Katsioti"
  - "M. Karagianni"
  - "A. Anastasiou"
  - "G. Romanos"
  - "J. Hassan"
  - "G. Papavassiliou"
venue: "Biomicrofluidics 14, 034114 (2020)"
pdf_sha256: "cda552486d0cec19324b090324e553e50fbb80be10dd06ba708e66c92f8e9753"
pdf_path: "papers/Others/CNT_water_diffusion_Biomicrofluidics_2020.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020gkoura-biomicroflui-peculiar-size -->

## Summary

The study combines **two-dimensional nuclear magnetic resonance diffusion–relaxation (D–T2eff) spectroscopy** in the stray field of a superconducting magnet with **molecular dynamics (MD) simulations** to resolve how **water dynamics inside carbon nanotubes (CNTs)** depend on **tube diameter** (about 1.1–6.0 nm) and **temperature** (265–305 K). The work reports multiple resolved “tubular” water components with distinct self-diffusion coefficients and highlights a diameter window (about 3.0–4.5 nm) where confined water shows **non-Arrhenius**, **ultrafast** diffusion and high **fragility**. **Nanofluidic** **transport** in **CNT** **membranes** motivates separating **bulk-like** vs **surface** **layers** of **confined** **water** because **slip** lengths and **effective** **permeability** depend on which **population** dominates **signal** in **NMR**.

## Methods

- **Experiments:** 2D NMR D–T2eff measurements on confined water in CNTs across the stated diameter and temperature ranges; methods and pulse/field details are given in the article and Supporting Information.
- **Simulations:** MD simulations of confined water in CNTs used alongside experiment to interpret size- and temperature-dependent dynamics (implementation details, water model, thermostat, and simulation length are specified in the PDF).
- **Stray-field** **NMR** leverages **spatially** **encoded** **diffusion** **filters** to separate **components** with distinct **D** and **T2**—critical where **pore** **polydispersity** would **overlap** **1D** **spectra**.

**Molecular dynamics (complement to experiment).** The authors use **molecular dynamics** in a standard **MD** package to simulate **water** confined in **cylindrical** **carbon** **nanotube** models with **O(10^2–10^3) atoms** per cell (as stated). **PBC** or finite-length CNTs follow the published setup. Runs use an **NVT**-type **thermostat** to hold **265–305 K** **temperature**; **N/A — barostat** and **N/A** for **NPT** **GPa** **pressure** in typical confined-water equilibration under fixed **volume**; **N/A — electric field**. **Timestep** in **femtoseconds** and **duration** in **ns**/long **ps** of **equilibration** and **production** are in the article/SI. **N/A — metadynamics** / **replica exchange** per abstract scope.

## Findings

- Confined water can separate into **two or more** dynamical components along the CNT axis, with **different self-diffusion coefficients** depending on diameter.
- In a **favorable diameter range (about 3.0–4.5 nm)**, dynamics of water near the CNT center show **distinctly non-Arrhenius** behavior, with **very fast diffusion** and **extraordinary fragility**, matching the experimental emphasis in the abstract.
- **Joint** **fit** of **simulation** **radial** **density** **profiles** and **experimental** **D–T2** **clusters** supports assigning **fast** **components** to **weakly** **perturbed** **core** **water** populations in **mid-sized** **tubes**.

## Limitations

NMR and MD each carry assumptions (surface chemistry of CNTs, water model, accessible time scales); quantitative comparison across all diameters should follow the uncertainties and controls described in the publication. **Metallic** vs **semiconducting** **CNT** **chirality** and **residual** **catalyst** **particles** can modify **confined** **water** **dynamics** beyond **smooth** **cylinder** models. **Pore** **length** and **entrance** **effects** in **membrane** **samples** may couple to **NMR** **exchange** **times** not captured in **infinite** **cylinder** **idealizations**.

## Relevance to group

Provides a tightly coupled **experiment + MD** example of **nanoconfined water** transport—useful context for interface and confinement problems adjacent to reactive MD work, though the core methodology here is not ReaxFF-centric.

## Citations and evidence anchors

- DOI: [10.1063/5.0005398](https://doi.org/10.1063/5.0005398)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

## Reader notes (navigation)

This is primarily a **classical** **water** **+** **NMR** paper—use it for **nanoconfined** **transport** context adjacent to **ReaxFF** **electrolyte** work.
