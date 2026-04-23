---
id: paper:2016nomura-srep-2016-do-nanocarbon-synthesis
type: paper
title: "Nanocarbon synthesis by high-temperature oxidation of nanoparticles"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:oxides-ceramics
  - method:reaxff
  - method:aimd
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:graphene-carbon
  - keyword:aimd
candidate_tags: []
source_refs: []
doi: "10.1038/srep24109"
year: 2016
authors:
  - "Ken-ichi Nomura"
venue: "Sci. Rep. 6, 24109 (2016)"
pdf_sha256: "17651b3deee7b5f00a6ecb02b4db1dc7a54fc9513cb9f287403ed69ad13c9138"
pdf_path: "papers/ReaxFF_others/Nomura_SiC_oxidation_SciRep2016.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2016nomura-srep-2016-do-nanocarbon-synthesis -->

## Summary

Reactive molecular dynamics (RMD) of silicon carbide nanoparticle oxidation at high temperature, cross-checked with ab initio quantum molecular dynamics (QMD), shows how oxygen attack on nSiC can produce a molten silica shell that transports oxidant while sequestering carbonaceous products, leading to condensation of large graphene-like flakes and ultimately porous sp\(^2\)-rich nanocarbon under the simulated conditions.

The study is motivated by high-temperature oxidation routes to nanostructured carbon where experimental control is difficult; large-cell RMD is used to capture spatially resolved oxidation fronts, cavity nucleation, and carbon condensation that would be inaccessible in mean-field continuum oxidation models.

## Methods

**Reactive MD (RMD).** The authors embed a spherical **nSiC** particle (diameter \(D\)) cut from **3C–SiC** in a bath of **O\(_2\)** and integrate trajectories with an **environment-dependent reactive bond-order force field** that allows bond making/breaking and uses a **charge-equilibration** treatment for charge transfer (Supplementary Section 1 as cited in the main text). For **\(D = 10\)** nm they compare oxidation at **2400 K** and **2800 K**; for **size scaling** they additionally run **\(D = 46\)** nm and **\(D = 100\)** nm at **2800 K** on a **786,432-core IBM Blue Gene/Q** system at Argonne. Analysis tracks **bond-type populations**, evolving **morphology** (unreacted core, **silica** shell, **cavities**), and relates **oxide-shell thickness** vs time to a crossover from **reaction-limited** early growth toward **diffusion-limited** late growth (see main-text discussion of Fig. 1d). The overall high-temperature oxidation stoichiometry discussed includes **SiC(s) + 3/2 O\(_2\)(g) → SiO\(_2\)(s) + CO(g)** as a reference frame for release of small oxidized carbon species.

**Ab initio QMD.** **Quantum molecular dynamics (QMD)** simulations in **Supporting Section 2** are used to **validate** aspects of the chemistry reported for the RMD model (parameter and functional details appear in the SI).

**Interpretation.** The manuscript contrasts nanoparticle oxidation with bulk Deal–Grove expectations, emphasizing curvature, heterogeneous shells, and confinement absent in planar models.

RMD is carried out in three-dimensional **periodic** cells embedding a spherical **nSiC** particle in an **O\(_2\)** bath (Supplementary Section 1). The main article emphasizes multimillion-atom scaling (including **786,432**-core **Blue Gene/Q** runs for **\(D = 46\)** and **\(100\)** nm at **2800 K**) and reports bond-count and morphology kinetics on **picosecond–nanosecond** horizons (for example, full consumption of the **\(D = 10\)** nm core near **~1.7 ns** at **2800 K** in the showcased trajectory). **Ensemble, timestep, thermostat, barostat, and target pressure** are not restated as explicit **NVT**/**NPT**/**NVE** labels or numeric **pressure** set points in the *Scientific Reports* main-text PDF reviewed for this page; **Supplementary Section 1** is where the authors place engine, integration, and thermostat/barostat details, so this wiki does not transcribe those numbers here. **N/A — applied electric field; umbrella / metadynamics / replica exchange** — not reported for the RMD campaign summarized above.

**Force-field training.** **N/A —** the communication applies an existing environment-dependent reactive bond-order framework (Supplementary Section 1); it does not publish a new parameterization line in the main text.

**Static QM / QMD.** Supporting Section 2 reports *ab initio* quantum molecular dynamics as a chemistry cross-check; functional and basis details are in the SI.
## Findings

Initial oxidation builds a **silica-rich shell** around an **unreacted SiC core**, with small oxidized carbon species (e.g., **CO**) released consistent with the high-oxygen-pressure reaction framing above. For **\(D = 10\)** nm at **2800 K**, snapshots show **graphene-like** carbon **condensing in cavities** within the shell; the **SiC core** is reported to be **fully consumed** around **~1.7 ns** in the illustrated trajectory. **Percolation** of condensed carbon yields **porous** nanocarbon with **pentagonal and heptagonal** defects embedded in predominantly **sp\(^2\)** networks. **Bond-count** trajectories indicate relatively faster **Si–C** and **O–O** scission and preferential **Si–O** formation versus **C–O** at the sampled conditions, which the authors use to rationalize **carbon enrichment** and **self-organization** into extended carbon domains inside the shell. They position the mechanism as a **high-temperature** route to **high-surface-area, low-density** nanocarbon for energy, biomedical, and mechanical-metamaterial applications (as stated in the abstract-level motivation).

The paper highlights how confinement inside a viscous silica network can transiently reduce carbon escape to the gas phase, promoting coalescence into extended sp\(^2\) domains even when the ambient atmosphere would fully oxidize isolated molecules.

## Limitations

Extreme temperatures and large RMD cells are demanding; readers should verify quantitative rates and finite-size effects in the original figures and SI.

## Relevance to group

Combines large-scale ReaxFF-style RMD with QMD checks for high-temperature oxidation-driven nanocarbon formation from SiC.

## Citations and evidence anchors

- DOI: [10.1038/srep24109](https://doi.org/10.1038/srep24109)

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
