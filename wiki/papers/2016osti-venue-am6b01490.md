---
id: paper:2016osti-venue-am6b01490
type: paper
title: "Effect of metal ion intercalation on the structure of MXene and water dynamics on its internal surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:2d-layered
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:2d-materials
  - keyword:reaxff-application
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acsami.6b01490"
year: 2016
authors:
  - "Naresh C. Osti"
  - "Michael Naguib"
  - "Alireza Ostadhossein"
  - "Yu Xie"
  - "Paul R. C. Kent"
  - "Boris Dyatkin"
  - "Gernot Rother"
  - "William T. Heller"
  - "Adri C. T. van Duin"
  - "Yury Gogotsi"
  - "Eugene Mamontov"
venue: "ACS Appl. Mater. Interfaces 2016, 8, 8859-8863"
pdf_sha256: "97d2ce88ea1d2f364b9ec905ad69cdd7bcbca1f669c064f5908f92a51afa0d36"
pdf_path: "papers/Osti_ACS_AMI_Water_Mxene_2016.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016osti-venue-am6b01490 -->

## Summary

Experimental X-ray and neutron scattering on Ti\(_3\)C\(_2\)T\(_x\) MXene, combined with ReaxFF-based molecular dynamics, show that potassium-ion intercalation swells the layered stack, sharpens diffraction signatures toward more homogeneous layering, and strongly suppresses confined water mobility compared to pristine, more heterogeneous MXene—implying improved structural and hydration stability under varying humidity. The combined approach is explicitly aimed at linking interlayer ion identity to both mesoscale stacking coherence and the molecular-scale mobility of water that plasticizes or locks gallery environments. The **ACS Applied Materials & Interfaces** letter format foregrounds **collaborative** **ORNL** scattering plus **Drexel** synthesis/characterization and **Penn State** **ReaxFF** modeling as a **triangulation** between **diffraction**, **QENS**, and **atomistic** **diffusion** estimates.

## Methods

**Experiments.** The authors contrast air-dried pristine Ti\(_3\)C\(_2\)T\(_x\) with K\(^+\)-intercalated Ti\(_3\)C\(_2\)T\(_x\) prepared by aqueous alkali treatment (Supporting Information). Laboratory X-ray diffraction measures \(c\)-axis repeat distances in the initial air-dried state and after vacuum annealing at **110 °C** (four-hour anneal and measurement details in the SI). After annealing they report \(c\)-lattice spacings of **19.64 Å** (pristine) and **24.35 Å** (K\(^+\)-intercalated) for the 0001-like stacking peak analyzed in the letter. Small-angle neutron scattering probes nanoscale morphology (Figure S2 in the SI). Quasi-elastic neutron scattering targets confined-water rotational and translational dynamics in oriented pressed samples (sample preparation in the SI).

**MD application (ReaxFF).** Supporting Information for this letter states that **molecular dynamics** uses **ReaxFF** as implemented in **LAMMPS**, velocity-Verlet integration, and a **time step** of **0.25 fs**. GCMC/MD intercalation inserts water (and, separately, K\(^+\) with hydroxide) into OH-covered Ti\(_3\)C\(_2\) **supercells**; after every 20 successful GCMC moves the authors run **10 ps** segments under **NPT** at **300 K** and **0.1 MPa** to relax the water–MXene interface, then sample **MSD** over **1.5 ns** under **NVT** at **300 K** to extract water self-diffusivities. The main letter’s **ReaxFF** runs compare pristine versus K\(^+\)-intercalated galleries and report roughly **two orders of magnitude** lower simulated self-diffusion after intercalation, qualitatively matching quasi-elastic neutron data. **Periodic** three-dimensional cells match the experimental \(c\)-axis spacing trends discussed in the letter. Thermostat coupling details for the **NVT** production segments appear in the **Supporting Information** PDF ([[2016osti-venue-microsoft-word]]) alongside the LAMMPS-style input notes. **N/A — applied electric field; umbrella / metadynamics / replica exchange** for these gallery production runs.

**Force-field training.** **N/A —** the letter applies an existing ReaxFF parametrization for Ti–C–O–H chemistry as referenced in the article.

**Static QM.** **N/A —** DFT is not the primary modeling modality reported here.
## Findings

K\(^+\) intercalation increases layer spacing and yields sharper 0001 diffraction peaks than pristine MXene after comparable drying/annealing sequences, interpreted as larger, more uniform stacked domains with fewer interstack voids. SANS supports nanostructural differences consistent with more homogeneous swelling. QENS shows that confined water dynamics slow markedly after intercalation; MD with ReaxFF reports water self-diffusion coefficients reduced by about two orders of magnitude relative to the pristine case, aligning with the experimental trend. Together, the results argue that tuning interlayer cations and water content can stabilize MXene against humidity-driven structural heterogeneity while also reconciling neutron-derived mobility with atomistic diffusion estimates.

## Limitations

The letter format compresses sample history; exact water populations and surface terminations T\(_x\) require SI cross-check for quantitative modeling. Neutron and X-ray experiments average over macroscopic ensembles, whereas MD snapshots resolve only nanometer-scale stacks, so agreement on diffusion orders-of-magnitude should be interpreted as consistency of trend—not pixel-level spatial maps of water populations.

## Relevance to group

Includes van Duin-group ReaxFF modeling of MXene–water systems tied to neutron scattering validation.

## Citations and evidence anchors

- DOI: [10.1021/acsami.6b01490](https://doi.org/10.1021/acsami.6b01490)

## Reader notes (navigation)

- 2D MXene + confined water: [[theme-2d-epitaxy-growth]]; neutron-scattering + ReaxFF pairing similar to other interface validation papers under [[batteries-interfaces-reaxff]].

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
