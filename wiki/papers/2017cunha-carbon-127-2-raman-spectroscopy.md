---
id: paper:2017cunha-carbon-127-2-raman-spectroscopy
type: paper
title: "Raman spectroscopy revealing noble gas adsorption on single-walled carbon nanotube bundles"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:reaxff-lineage
  - material:graphene-carbon-nano
  - method:reaxff
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2017.11.017"
year: 2017
authors:
  - "Renato Cunha"
  - "Ricardo Paupitz"
  - "Kichul Yoon"
  - "Adri C. T. van Duin"
  - "Ana Laura Elías"
  - "Victor Carozo"
  - "Archi Dasgupta"
  - "Kazunori Fujisawa"
  - "Néstor Perea Lopez"
  - "Paulo T. Araujo"
  - "Mauricio Terrones"
venue: "Carbon"
pdf_sha256: "8c4b1d74453819bfc1cfcf1b039d42483d6eefe04e333da83d66c3598bc0bf8b"
pdf_path: "papers/Cunha_Carbon_2018.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2017cunha-carbon-127-2-raman-spectroscopy -->

## Summary

Noble-gas adsorption on single-walled carbon nanotube bundles is a controlled way to probe weak van der Waals coupling and mechanical perturbations of the tube lattice without introducing strong chemical doping. This *Carbon* article combines Raman spectroscopy at 20 K with ReaxFF-based modeling to interpret how argon and xenon populate external and groove sites on bundles, and how that adsorption couples to measurable changes in the radial breathing mode (RBM), G band, and two-phonon 2D feature. The experimental story emphasizes blueshifts across these bands when solidified gas loads the bundle, interpreted as a hydrostatic-like compressive environment created by condensed noble gas in interstitial and surface pockets. Complementary atomistic modeling is used to support a picture of physisorption that leaves electronic doping minor, consistent with modest changes in linewidth and intensity relative to frequency shifts. The author list places Adri C. T. van Duin and Kichul Yoon in the computational support role within a multi-institution collaboration led by experimental carbon nanoscience groups.

## Methods

**Experiment.** **Single-walled carbon nanotube (SWCNT) bundles** supported on **TEM grids** are dosed with **Ar** or **Xe** at **20 K**, where condensed adsorbate occupies **groove** channels between tubes and **outer** bundle surfaces. **Raman spectroscopy** follows the **radial breathing mode (RBM)**, **G band**, and **G′/2D** (two-phonon) features versus **gas exposure**.

**MD application (ReaxFF, supporting modeling).** **Reactive MD** with **ReaxFF** builds **PBC** **bundle** models with **noble-gas** loading patterns meant to represent **groove vs exterior** site populations and the **mechanical coupling** of adsorbate shells to tube walls, linking structure to **phonon** frequency shifts observed in **Raman**. **Force-field** provenance is cited in *Carbon* **Computational methods**.

**Force-field training** and **standalone bulk DFT** campaigns are **N/A** for the main evidence chain.

**Full MD run cards** (**code**, **ensemble**, **timestep**, **thermostat**, **barostat**, **duration**, **supercell** construction) appear in the *Carbon* **Methods**; they are **not transcribed** from the short indexed extract (the **20 K** experimental temperature is explicit in the abstract).

**MD blueprint honesty.** **Reactive molecular dynamics** with **ReaxFF** on **PBC** **bundle** models supplements experiment. **LAMMPS** is typical for **ReaxFF** production—confirm in *Carbon*. **NVT**/**NPT**/**NVE**, **timestep**, **thermostat**, **barostat**/**pressure**, and **equilibration**/**production** lengths (**ps**/**ns**) are **N/A** on this page—use the **Methods**/**SI**.

## Findings

**Spectroscopy:** **gas solidification** in **grooves**/surfaces yields **blueshifts** of **RBM**, **G**, and **2D/G′** bands; **Ar** vs **Xe** give **almost identical** shifts, arguing for **very similar** bundle–gas interaction strengths in this **physisorption** regime. **Mechanistic readout:** authors interpret the condensed adsorbate as imposing an effective **hydrostatic pressure** on the bundle, mechanically coupling to phonons. **Modeling alignment:** **ReaxFF** simulations support **weak chemisorption** / **minor doping** pictures—shifts dominate over large **charge-transfer** changes in linewidth/intensity. **Quantitative shift magnitudes** (e.g. **~4 cm⁻¹** **RBM** change cited in discussion) should be verified in the **final PDF** tables/figures. **Comparisons:** **Ar** vs **Xe** shifts are compared experimentally; modeling is compared qualitatively to those **Raman** trends. **Sensitivity / limitations:** bundle **heterogeneity** and **site** averaging affect how uniquely one can infer groove vs exterior occupancy from **Raman** alone—authors discuss evidence limits in the article.

## Limitations

Bundled samples average over diameter polydispersity and heterogeneous site occupancy, so extracting a single-site picture from Raman alone is inherently approximate; ReaxFF also carries parametrization uncertainty for rare-gas–carbon interactions that should be weighed when transferring conclusions to other pressures or bundle morphologies.

## Relevance to group

The paper exemplifies a ReaxFF-assisted interpretation pipeline for nanocarbon surface science with direct van Duin-group participation, useful for retrieval queries that connect spectroscopy, physisorption, and reactive carbon force fields.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1016/j.carbon.2017.11.017` (`papers/Cunha_Carbon_2018.pdf`).

## Related topics

- [[reaxff-family]]
