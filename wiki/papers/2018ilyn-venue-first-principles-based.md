---
id: paper:2018ilyn-venue-first-principles-based
type: paper
title: "First-principles–based reaction kinetics from reactive molecular dynamics simulations: Application to hydrogen peroxide decomposition"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:fuel-combustion
  - method:reaxff
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:combustion
  - keyword:method-development
candidate_tags: []
source_refs: []
doi: "10.1073/pnas.1701383115"
year: 2018
authors:
  - "Daniil V. Ilyin"
  - "William A. Goddard III"
  - "Julius J. Oppenheim"
  - "Tao Cheng"
venue: "Proc. Natl. Acad. Sci. U.S.A."
pdf_sha256: "2c4b9c7d8816f1e6f4e98615c0ac05fcdac15590f47d51c9403f0c1af4a41362"
pdf_path: "papers/ReaxFF_others/Ilyn_Goddard_PNAS_H2O2_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018ilyn-venue-first-principles-based -->

## Summary

This PNAS perspective lays out a computational strategy—termed **RMD2Kin** (reactive molecular dynamics to kinetics), with the QM-trained ReaxFF instantiation called **ReaxMD2Kin**—for turning large-scale reactive molecular dynamics into analytic reaction networks and rate expressions that can feed continuum and computational fluid dynamics models. The motivating problem is that technologies from combustion and propulsion to chemical vapor deposition and reactive etching are governed by condensed-phase chemistry whose detailed mechanisms are difficult to observe experimentally, so practitioners often rely on highly simplified kinetic schemes with adjustable parameters that do not map cleanly onto molecular intermediates. The authors argue that fully quantum mechanical sampling over the nanometer spatial scales and nanosecond time scales needed for useful kinetic closure is prohibitively expensive, whereas ReaxFF, trained to reproduce quantum mechanics for two-body reactive interactions, can support reactive MD at costs closer to classical force fields while retaining much of the chemical fidelity needed for mechanism discovery. The article uses hydrogen peroxide decomposition as a proof of concept: radical-initiated pathways are analyzed to extract mechanisms, rates, and transition-state thermochemistry, and the extracted analytic model is shown to reproduce concentration evolution in a self-consistent way.

## Methods

The methodological backbone is **ReaxFF reactive molecular dynamics** on systems large enough to capture condensed-phase environment effects, paired with automated post-processing that extracts reaction events, constructs a kinetic scheme without requiring chemists to prespecify every elementary step, and fits analytic rate expressions suitable for upscaling. The perspective emphasizes that ReaxFF uses **atom-centered distributed charges** rather than point charges, which matters for electrostatics in reactive environments. The hydrogen peroxide demonstration analyzes radical-initiated decomposition, extracting transition-state enthalpies and entropies for the participating reactions and then integrating those rates into a kinetic reconstruction of species versus time. The article frames the output as suitable for hierarchical coupling: atomistic QM/ReaxFF fidelity at the smallest scales, analytic chemistry embedded into continuum or CFD treatments from roughly tens of nanometers to micrometers and beyond, with repeated coarse-graining as needed for engineering length scales. Supporting information referenced from the PNAS entry documents additional algorithmic detail for the automated mechanism and rate extraction workflow.

**Reactive MD application (demonstration trajectories).** The perspective uses **reactive molecular dynamics** (RMD) at scales larger than affordable **QM** dynamics; **engine**, **supercell** sizes, **PBC** conventions, **timestep**, **thermostat**, **equilibration**/**production** lengths in **ps**/**ns**, and any **NPT** stages are specified in the article and **SI** rather than duplicated here. **N/A — this wiki page does not transcribe every numerical MD control** from the **PDF**—use `pdf_path` for production tables. **N/A — macroscopic electric-field or bias coupling** as a standalone MD driver is not the focus of the summarized **H\(_2\)O\(_2\)** workflow unless the **PDF** adds such protocols. **N/A — umbrella sampling / metadynamics / replica exchange** for the demonstration unless explicitly stated there.

**ReaxFF parameterization context (training lineage).** **Parent potential:** **ReaxFF** with **atom-centered distributed charges** (not fixed point charges), trained to reproduce **QM** for two-body reactive interactions as described in the **ReaxFF** literature cited in the perspective. **QM reference data:** **DFT**-level energies, charges, and reaction energetics underpin the published **ReaxFF** training philosophy (functional, basis, and **k**-mesh choices appear in the underlying **ReaxFF** references and companion fits—not re-derived here). **Training / optimization:** **genetic-algorithm**/**ParReaxFF**-style optimization against **QM** **training sets** is the standard workflow referenced for **ReaxFF** construction; the **H\(_2\)O\(_2\)** example uses an existing parameterization to generate **RMD** trajectories, not a new element-by-element fit reported in this perspective. **Validation:** the **ReaxMD2Kin** demonstration **compares** extracted **kinetics** back against the originating **RMD** species trajectories as an internal consistency check.

## Findings

**Outcomes and mechanisms.** For **H\(_2\)O\(_2\)** decomposition, the **ReaxMD2Kin** pipeline recovers radical-initiated **reaction** sequences—including **transition-state** enthalpies and entropies—and re-integrates analytic **rates** so that species **concentration** vs **time** matches the parent **RMD** statistics, supporting a closed loop from **reactive MD** to **kinetic** models.

**Comparisons.** The article contrasts fully **QM** sampling (accurate but too costly for condensed-phase **kinetics** closure) with **ReaxFF RMD** as a practical bridge, and positions the extracted schemes for coupling to **continuum**/**CFD** **literature** workflows.

**Sensitivity and levers.** Operating **temperature**, **pressure**, and condensed-phase environment enter implicitly through the **RMD** ensemble used for extraction; the perspective stresses that **mechanism** discovery is tied to the **statistical** sampling achieved in those trajectories.

**Limitations, outlook, and PDF grounding.** Transferability of any **ReaxFF** parameterization remains training-set dependent; **upscaling** choices (heterogeneity, turbulence–chemistry coupling) sit above the atomistic layer. Detailed **mechanism** graphs, **rate** tables, and **MD** settings live in the **PNAS** article and **SI** (`pdf_path`); this summary does not add claims beyond those sources.
## Limitations

Transferability of any ReaxFF parameterization to new compositions, phases, and extreme conditions requires explicit validation; the perspective is a strategy paper and the numerical accuracy of each application remains training-set dependent. Upscaling also introduces modeling choices about spatial heterogeneity and turbulence–chemistry coupling that are outside the atomistic ReaxFF layer.

## Relevance to group

Foundational **reactive MD → kinetics** workflow paper for **combustion** and **oxidation** modeling communities; ties to **[[2018hanson-venue-supporting-online]]** SI package.

## Citations and evidence anchors

- DOI: `10.1073/pnas.1701383115`.

## Related topics

- [[2018hanson-venue-supporting-online]]
- [[reaxff-family]]
