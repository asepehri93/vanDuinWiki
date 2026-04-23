---
id: paper:2016ostadhossein-venue-jp-2015-119086
type: paper
title: "Atomic insight into the lithium storage and diffusion mechanism of SiO2/Al2O3 electrodes of lithium ion batteries: ReaxFF reactive force field modeling"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - method:monte-carlo
  - material:oxide
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:batteries-interfaces
  - keyword:monte-carlo-sampling
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.5b11908"
year: 2016
authors:
  - "Alireza Ostadhossein"
  - "Sung-Yup Kim"
  - "Ekin D. Cubuk"
  - "Yue Qi"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. A 2016 (ASAP from 2015 manuscript id 5b11908)"
pdf_sha256: "13b876667232c8ee31fc39f32d7194043517355749115e809e5033e47af10f1f"
pdf_path: "papers/Ostadhossein_JPCA_2016_LiSiO_online.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2016ostadhossein-venue-jp-2015-119086 -->

## Summary

Silicon-rich battery anodes are frequently paired with thin oxide coatings—silica-rich native oxides, deliberate SiO\(_x\) layers, or atomic-layer-deposited alumina—to buffer volume changes during lithiation and to steer solid–electrolyte interphase formation away from continuous fracture paths. Ostadhossein et al. develop a ReaxFF reactive model for the Li–Si–O–Al quaternary space so that lithium insertion, network rearrangement, and diffusion can be simulated in silica and alumina motifs relevant to coated silicon electrodes. The workflow couples grand-canonical Monte Carlo (GCMC) moves that adjust lithium content with molecular dynamics relaxation segments, enabling thermodynamic sampling of lithiated oxide stoichiometries and kinetic extraction of diffusivities that fixed-composition trajectories cannot represent.

## Methods

**Force-field training.** The authors develop a ReaxFF description for Li–Si–O–Al interactions so that lithiation, reaction, and transport can be treated in silica- and alumina-rich environments relevant to coated silicon anodes. DFT reference data on clusters, surfaces, and condensed phases (energetics and structural motifs summarized in the abstract and tabulated in the article/SI) drive the reparameterization; optimization details, weighting, and training-set scope appear in *J. Phys. Chem. A* (DOI `10.1021/acs.jpca.5b11908`) and its Supporting Information.

**MD application and sampling.** Hybrid **grand canonical Monte Carlo** (**GCMC**) moves alternate with **molecular dynamics** relaxation to vary lithium content in crystalline silica polymorphs and amorphous silica networks. Later segments use **NVT** sampling (for example, **250 ps** RDF accumulations on a **3000-atom** α-quartz-derived glass at **300 K**) and **NPT** relaxation (**P = 0**, **T = 300 K**) to densify amorphous silica before mechanical tests; voltage-profile GCMC/**MD** cycling for lithiation follows the Metropolis scheme referenced for **ReaxFF** implementations. Amorphous silica preparation heats a **10×10×10** α-quartz **supercell** from **300 K** toward **3500 K** for **1 ns**, then quenches at **1.024 K/ps** before the shorter **NVT** diagnostics. Nonequilibrium **MD** (**NEMD**) tensile tests probe strain-rate dependence at **300 K** under the **0 atm**-class conditions stated in the tensile section. Trajectories for diffusivity and lithiation use **periodic** cells with **in-plane PBC** as defined in the article. The study does not apply an external electric field or use umbrella sampling, metadynamics, or replica exchange as the main workflow beyond GCMC + MD. **N/A — explicit integration timestep in fs** — not recovered as plain ASCII in the *J. Phys. Chem. A* PDF text extracted here; copy the numerical **timestep** and thermostat coupling lines from the issue **PDF**/Supporting Information when reproducing inputs. DFT supports parametrization, not large-cell production dynamics.
## Findings

The published field reproduces DFT-level trends for lithium site preferences and migration barriers in silica, including anisotropic lithium transport in crystalline channels versus effectively averaged hopping in discontinuous amorphous networks. The authors relate these kinetic patterns to how oxide coatings can throttle or redirect lithium flux toward silicon active material, informing mechanistic interpretations of rate capability in composite electrodes. Interface models further illustrate stress accommodation pathways during repeated lithiation, although absolute rate constants must still be validated against electrochemical experiments that include electrolyte decomposition, solvation, and electric fields omitted in the dry oxide-focused study.

GCMC/MD sampling also highlights how coating thickness and disorder control whether lithium accumulates at the coating surface or percolates through before reaching silicon, a distinction that maps onto rate-limiting hypotheses for coated anode architectures.

## Limitations

Idealized thin films omit explicit liquid electrolyte decomposition, electric double-layer fields, and porous electrode transport; ReaxFF also lacks explicit electronic polarization beyond the fitted bond-order form.

## Relevance to group

Direct van Duin-group contribution on ReaxFF for LIB oxide coatings and Li transport in amorphous silica networks.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpca.5b11908](https://doi.org/10.1021/acs.jpca.5b11908)

## Related topics

- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
