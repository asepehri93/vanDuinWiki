---
id: paper:2020aniruddh-vashisth-acs-an9b02524
type: paper
title: "ReaxFF Simulations of Laser-Induced Graphene (LIG) Formation for Multifunctional Polymer Nanocomposites"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:application
  - material:graphene-carbon-nano
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1021/acsanm.9b02524"
year: 2020
authors:
  - "Aniruddh Vashisth"
  - "Małgorzata Kowalik"
  - "Joseph C. Gerringer"
  - "Chowdhury Ashraf"
  - "Adri C. T. van Duin"
  - "Micah J. Green"
venue: "ACS Appl. Nano Mater."
pdf_sha256: "4fd0af6f442743021fe871899cacfb90bfaed0d7549f36cf02f54dc63f86e170"
pdf_path: "papers/Vashisth_AppliedNano_2020_LIG_formation.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020aniruddh-vashisth-acs-an9b02524 -->

Reactive molecular dynamics with an extended C/H/O/N ReaxFF parameterization is used to study laser-induced graphene (LIG) formation from five commercial polymers (PBM, PEEK, PEI, PC, Kapton), complementing experimental LIG fabrication and Raman evidence discussed in the article.

## Summary

The work reports ReaxFF simulations of high-temperature conversion of polymer films into porous, graphitic carbon resembling LIG. Simulations track gas evolution (notably CO and H\(_2\)), ring statistics (5-, 6-, and 7-member carbon rings), surface area, and interlayer spacing, and compare trends to experimental LIG characterization. The authors relate polymer oxygen content to CO release, explore inert versus oxygen-containing conditions, and identify a practical simulation temperature window (about 2500–3000 K) that produces graphitic structure without complete disintegration.

## Methods

- **Force field and code:** ReaxFF parameters extended for C/H/O/N chemistry and improved graphitic ring stability (as cited in the article from prior work by Kowalik et al.). Simulations are described as reactive MD for bond breaking and formation during pyrolysis-like heating.
- **Systems:** Five polymers with aromatic backbones: polybenzimidazole (PBM), poly(ether ether ketone) (PEEK), poly(ether imide) (PEI), polycarbonate (PC), and polyimide (Kapton). Initial cells are reported as roughly \(\sim\)1400 atoms total at \(\sim\)0.8 g cm\(^{-3}\).
- **Protocol:** High-temperature runs (e.g., 2500–3000 K and comparisons including below 2000 K and above 3500 K) with trajectories analyzed over **1.25 ns** at **3000 K** for ring counts and surface area. Gases are not removed from the box during the 1.25 ns production segment. After isolating LIG-like carbon, structures are cooled to **300 K** and further **NPT** then **NVT** equilibration is performed before carbon–carbon radial distribution functions.
- **Experiments (context for validation):** CO\(_2\) laser processing of thin films (e.g., 3.75 W, 0.1 m/s on Kapton) with SEM and Raman of LIG; TEM interlayer spacing compared to simulated layer spacing (reported \(\sim\)3.4–4.0 Å in simulations, \(\sim\)3.37 Å experimentally).

- **MD protocol (RMD).** **LAMMPS** **ReaxFF** on **PBC** cells with **~1400** **atoms** at **~0.8 g cm\(^{-3}\)**; high-**T** anneals **2500**–**3000 K** with a **1.25 ns** segment at **3000 K** for **ring**/**surface-area** **analysis**; **Nose–Hoover**-type **thermostat** (or as in the article) for those **NVT** legs; **N/A —** **fs** **timestep** and full **NVT**/**NPT** breakdown for all segments: see *ACS Appl. Nano Mater.* **N/A —** **barostat**; **N/A —** **electric** field in the RMD. **N/A —** **umbrella** / **replica** **exchange** for pyrolysis. **NPT** then **NVT** on **cooled** **LIG** **morphologies** is reported for **RDFs**.

**FF training (block 2).** **C/H/O/N** ReaxFF **parameters** are **cited** from **prior** work (Kowalik et al. as referenced); **N/A** — this paper’s **new** code **changes** are not a refit in the sense of a fresh **Reaxff** **optimization** article.

**Static QM (block 3).** **N/A** — the core is **ReaxFF** **RMD** plus **experiment**; DFT is not the primary **method** block for LIG.

## Findings

- CO is released especially during early conversion of polymer to amorphous carbon; H\(_2\) evolution continues as amorphous carbon orders into graphitic regions. Kapton releases the most CO among the polymers studied, consistent with higher oxygen content in the monomer.
- LIG-like models contain substantial **5- and 7-member** carbon rings, producing undulated, non-ideal graphene sheets rather than purely hexagonal graphene; normalized 6-ring counts show an initial drop during amorphization then recovery as graphitic structure forms.
- Simulated interlayer spacing (\(\sim\)3.4–4.0 Å) agrees with TEM-derived spacing for few-layer LIG. PBM-derived models achieve the highest surface area among the five precursors under the reported simulation conditions.
- **O\(_2\) presence** reduces LIG yield relative to inert conditions in the simulations, paralleling the experimental sensitivity to atmosphere.
- Temperatures **below \(\sim\)2000 K** yield largely amorphous carbon; **above \(\sim\)3500 K** the backbone disintegrates with little residual LIG-like structure; **2500–3000 K** is identified as a window where graphitic character develops.

## Limitations

ReaxFF remains an approximate reactive model; absolute kinetics and quantitative agreement with laser heating rates and spatial gradients are not claimed. The simulated cells are nanoscale and omit explicit laser coupling, fluid flow, and continuum heat transport.

## Relevance to group

Direct **van Duin-group** ReaxFF application to laser-driven carbonization and graphitization from engineering polymers, aligned with reactive carbon/polymer chemistry in the broader corpus.

## Citations and evidence anchors

- DOI: [10.1021/acsanm.9b02524](https://doi.org/10.1021/acsanm.9b02524)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
