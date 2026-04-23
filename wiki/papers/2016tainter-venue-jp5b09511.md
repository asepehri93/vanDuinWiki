---
id: paper:2016tainter-venue-jp5b09511
type: paper
title: "Reactive Force Field Modeling of Zinc Oxide Nanoparticle Formation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - material:widegap-semiconductor
  - method:reaxff
  - method:dft-static
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b09511"
year: 2016
authors:
  - "Craig J. Tainter"
  - "George C. Schatz"
venue: "J. Phys. Chem. C (2016) 120, 2950–2961"
pdf_sha256: "6055ebacf8671a0085a50957b988e3cacbefdd2aff379832c1a0a0b6b368c323"
pdf_path: "papers/ReaxFF_others/Tainter_Schatz_ZnO_NP_JPCC_2016.pdf"
extraction_quality: "good"
group_affiliation: false
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reactive-md
  - keyword:graphene-carbon
  - keyword:dft-static
  - keyword:lammps
---
<!-- id:paper:2016tainter-venue-jp5b09511 -->

## Summary

The authors develop an extended **ReaxFF** description to capture **Zn–C** interactions needed when **diethyl zinc (EZE)** reacts on **epoxidized graphene**, motivated by **ALD-style** experiments where **ZnO nanoparticles** nucleate after oxygen functionalization and organometallic exposure. Large-scale **reactive MD** follows **oxygen abstraction from epoxides**, **Zn–O condensation**, and **nanoparticle** emergence. Complementary **time-dependent DFT** analyzes **optical absorption** shifts for small **ZnO**-like clusters vs **wurtzite** reference.

The study bridges organometallic precursor chemistry on carbon templates with oxide nanoparticle nucleation—phenomena central to hybrid nanomaterial synthesis routes.

## Methods

**1 — MD application (ReaxFF).** Simulations use **LAMMPS** with **ReaxFF** (periodic boundary conditions). **Ensemble:** **NVT** in all production segments described for nanoparticle formation. **Thermostat:** **Berendsen** with a **100 fs** coupling time. **Timestep:** **0.25 fs**. **System:** a **180-carbon graphene** sheet functionalized with **two epoxide** groups (coverage consistent with the cited ALD-style experiments), with **diethyl zinc (EZE)** initially placed above the sheet. **Protocol:** **12.5 ps** heating/equilibration from **100 K** to the target temperature while keeping the gas-phase molecule’s net linear and angular momentum at zero; the Zn atom is then given a Boltzmann-distributed velocity aimed at the epoxidized face, followed by **500 ps** dynamics (additional “ALD cycle” restarts use the output geometry as noted in the article). **Barostat / pressure control:** **N/A —** runs are **NVT** without stated stress control. **Electric field:** **N/A —** not used. **Replica / enhanced sampling:** **N/A —** not used.

**2 — Force-field training (ReaxFF).** **Parent model:** ReaxFF hydrocarbon formalism of **van Duin *et al.*** extended along the **Zn–O** literature cited in the paper; **Zn–C** terms are added because earlier **ZnO / MOF** parametrizations omitted interactions needed for **EZE** on carbon. **QM reference:** **DFT** with **B3LYP** and **6-311+G\*** in **NWChem 6.1.1** on training species (**EZE**, **EOZE**, **EOZOE**, methyl-substituted analogues) including **bond-stretch** and **valence-angle** surfaces; parameters are refined by iterative single-parameter minimization of a weighted **(ReaxFF − DFT)\(^2\)** error (eq 5 in the article). **Training targets:** bond dissociation profiles, angle potentials, and checks against **ZnO** polymorph energies as summarized in the main text and **Supporting Information**.

**3 — Static QM / TD-DFT on clusters.** **TD-DFT** calculations on **nonstoichiometric Zn–O clusters** (including capped motifs taken from MD) use **ADF 2013.01** with the **B3LYP** functional, **TZP** basis on all atoms, and the **frozen-core** approximation, following the **Optical Spectra** subsection of the article. Solvent effects are included with **COSMO-RS** (water), consistent with typical optical measurements. The solver targets **50** excitations with a squared excitation-energy tolerance of **8 × 10⁻⁶ hartree**; stick spectra are broadened with a **0.5 eV** Gaussian, omitting excitations within **0.5 eV** of the highest-energy excitation from the line shape, as stated in the same section. **k-point sampling:** **N/A —** finite cluster models rather than periodic **k**-mesh sampling.

**4 — Reviews / non-simulation blocks.** **N/A —** primary research article with new simulations and parametrization.
## Findings

**Outcomes and mechanisms.** Reactive trajectories follow **oxygen abstraction from graphene epoxides** that enables **Zn–O** condensation and growth of **ZnO-like fragments** toward **nanoparticles**, consistent with the experimental motivation (Johns *et al.*). **Structural motif:** nanoparticle models are **nonstoichiometric** Zn–O arrangements with **average Zn coordination ≈ 3.6** (abstract).

**Comparisons.** **TD-DFT** absorption for selected clusters is **red-shifted by a few tenths of an eV** relative to **wurtzite**, described in the abstract as excitations with **O 2p** character near the cluster surface to **Zn 4s**-like interior states.

**Sensitivity and levers.** The Introduction notes experimental control of **nanoparticle size** via **temperature** and **concentration** during growth; the MD setup varies **epoxide** coverage consistent with estimated experimental oxygenation.

**Limitations (as discussed).** The article compares a **ReaxFF** reaction-path test for epoxide abstraction to **DFT** and discusses discrepancies (e.g., barrier ordering) while noting that **room-temperature** chemistry still requires fast (picosecond-scale) events in MD—read **Figure 4** and discussion for the quantitative comparison.

**Corpus honesty.** Protocol tables, extended figures, and TD-DFT settings beyond this summary remain in the **PDF/SI** (`pdf_path` above).

## Limitations

- **ReaxFF** accuracy depends on the breadth of **Zn–C/Zn–O/C–O** training space; exotic organometallic pathways may require additional validation.
- Optical properties are computed for **selected** cluster models; nanoparticle polydispersity in experiment is not fully captured.

## Relevance to group

Methodological neighbor to **ReaxFF oxide + carbon** reactive simulations; cites the **van Duin** ReaxFF lineage as the starting point for hydrocarbon-style reactive modeling before Zn-specific extensions.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.5b09511](https://doi.org/10.1021/acs.jpcc.5b09511)
- Text-aligned pointers: `normalized/extracts/2016tainter-venue-jp5b09511_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
