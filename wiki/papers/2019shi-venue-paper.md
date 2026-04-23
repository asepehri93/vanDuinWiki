---
id: paper:2019shi-venue-paper
type: paper
title: "Modeling carbon fiber oxidation under high temperature by ReaxFF-based molecular dynamics simulation"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:reactive-md
source_refs: []
doi: "10.2514/6.2020-0484"
year: 2020
authors:
  - "Linyuan Shi"
  - "Marina Sessim"
  - "Michael R. Tonks"
  - "Simon R. Phillpot"
venue: "AIAA SciTech Forum 2020 (proceedings paper; local PDF matches conference manuscript)"
pdf_sha256: "338ffa836991f71f7fcc0c1ed653e1d1daf91e82b743fbcff91ae57f572e3ef7"
pdf_path: "papers/ReaxFF_others/2020.01 Modeling Carbon fiber oxidation under high temperature by ReaxFF based molecular dynamics simulation.pdf"
extraction_quality: "partial"
group_affiliation: false
---
<!-- id:paper:2019shi-venue-paper -->

## Summary

Phenolic impregnated carbon ablator (PICA) combines a phenolic resin matrix with carbon fibers and is widely used in thermal protection systems for atmospheric entry. Understanding high-temperature oxidation of the carbon fiber reinforcement is important because char oxidation and fiber microstructure evolution influence recession and heat load into the material. This AIAA SciTech contribution builds an atomistic carbon fiber model by extending a kinetic Monte Carlo plus molecular dynamics generation scheme (after Desai et al.) with a cylindrical confining potential that keeps the fiber thin enough to emphasize edge-site chemistry. Reactive MD with ReaxFF then probes high-temperature oxidation of the fiber model. The authors report carbon monoxide as the dominant oxidation product in their simulations, consistent with other carbon oxidation studies referenced in the introduction.

## Methods

**1 — MD application (ReaxFF oxidation of the fiber model).** The authors build a high-fidelity carbon fiber by extending the Desai *et al.* combined kinetic-Monte-Carlo and MD generation scheme: repeating ladder units grow into sheets (Figure 1 in the AIAA proceedings), and a Lennard-Jones “energy wall” (Eq. (1) in the text) acts on the radial distance \(r\) from the fiber axis so the structure stays in a thin cylindrical region at the center of the periodic cell. That geometry deliberately stresses **edge** sites with under-coordinated **carbon atoms** (highlights sheet terminations) relative to in-plane sites in ideal graphite, matching the experimental emphasis on fiber *surfaces* rather than inert basal planes. Reactive MD with a ReaxFF potential is then applied to high-temperature oxidation of that fiber model. The local PDF matches the AIAA SciTech 2020 proceedings (DOI 10.2514/6.2020-0484). The short corpus extract (p1–2) only covers the fiber model and the start of Section II; it does *not* reproduce the full oxidation protocol table. **N/A** — for this wiki page, explicit LAMMPS (or other engine) name, time step, thermostat type and damping, full temperature history, simulation cell oxygen content or effective \(p_{\mathrm{O_2}}\), NVT vs NVE staging, and production run length in ps/ns: not captured in the indexed text—use Section II of the full proceedings PDF. **Barostat / hydrostatic pressure control:** **N/A** for the fiber-generation and likely constant-volume oxidation stages *as typically reported* for this problem class; confirm in Section II. **Shear, shock, and external electric field:** **N/A**. **Replica / metadynamics / umbrella sampling:** **N/A** — not described on the indexed pages.

**2 — Force-field training.** **N/A** — the paper applies an existing ReaxFF carbon/oxygen (and related) parameterization; it does not report a new fit or reoptimization study.

**3 — Static QM.** **N/A** — the contribution is not a primary DFT study; the introduction cites prior DFT, DFTB, and ReaxFF work for chemical context.

## Findings

Simulations emphasize CO as the major product during high-temperature oxidation of the constructed fiber model, aligning with the authors’ comparison to other computational carbon oxidation studies. The introduction frames future work on quantifying reaction rates and additional products; readers should consult the full proceedings PDF for numerical rates and conditions.

The motivation section ties the fiber oxidation problem to PICA-style thermal protection systems, noting that improved atomic-scale oxidation models could tighten predicted recession versus flight data where post-flight analyses sometimes undershoot predicted char loss. Even though this proceedings article does not close that gap, it positions the ReaxFF fiber model as a stepping stone toward rate-informed oxidation schemes.

## Limitations

Conference proceedings formatting; conditions should be verified against the PDF and any subsequent journal version if one exists. Reactive MD at high temperature may omit radiative cooling and gas-phase transport effects present in flight.

## Relevance to group

ReaxFF application to **ablative carbon** oxidation relevant to thermal protection and pyrolysis chemistry.

## Citations and evidence anchors

- DOI: [10.2514/6.2020-0484](https://doi.org/10.2514/6.2020-0484)
- Local PDF: `papers/ReaxFF_others/2020.01 Modeling Carbon fiber oxidation under high temperature by ReaxFF based molecular dynamics simulation.pdf`

## Related topics

- [[reaxff-family]]
