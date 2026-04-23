---
id: paper:2014zou-acta-materia-molecular-dynamics
type: paper
title: "Molecular dynamics simulations of the effects of vacancies on nickel self-diffusion, oxygen diffusion and oxidation initiation in nickel, using the ReaxFF reactive force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:alloys-metallurgy
  - domain:oxides-ceramics
  - material:metal-surface
  - method:reaxff
  - task:parameterization
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2014.09.047"
year: 2014
authors:
  - "Chenyu Zou"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Huazhi Fang"
  - "Zi-Kui Liu"
venue: "Acta Materialia 83 (2015) 102–112"
pdf_sha256: "1f4c14bcf7a3c837c08435870afd2f2de142c1d147cc2a7700641a3a73466596"
pdf_path: "papers/Zou_ActaMater_2014.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014zou-acta-materia-molecular-dynamics -->

## Summary

A Ni–O ReaxFF description is developed from QM training data spanning Ni and NiO equations of state, Ni vacancy formation and self-diffusion, and O insertion and diffusion barriers in Ni. MD validation shows agreement with published Ni self-diffusivity and O interstitial diffusivity/activation energy. The work then examines how vacancies alter O transport and internal oxidation: a **vacancy-pair** oxygen migration mechanism is proposed, and simulations suggest voids at grain boundaries can promote local O segregation via strong O–vacancy binding, nucleating NiO in voids—linking atomistic transport to early oxidation microstructures. The study is framed as a **mechanistic** bridge between **bulk diffusion** coefficients and **microstructural** sites where oxide **nucleates** internally.

## Methods

**Force-field training (Ni–O ReaxFF).** Parameters are fit to QM-derived data that include equations of state for several Ni crystal phases and for NiO, Ni vacancy formation energy, the vacancy-mediated Ni self-diffusion barrier in fcc Ni, and—because interstitial oxygen is central to oxidation kinetics—oxygen insertion energies and oxygen diffusion barriers used as additional training targets (abstract; full tables in `papers/Zou_ActaMater_2014.pdf`).

**MD application (validation and oxidation scenarios in LAMMPS).** After parameterization, MD uses the **LAMMPS** ReaxFF package with a uniform **0.25 fs** timestep on **three-dimensional periodic boundary conditions (PBC)** supercells (bulk Ni, interstitial O models, and larger grain-boundary constructs as defined in the article). When temperature and pressure controls are active, the authors use a **Berendsen** thermostat (**100 fs** damping) together with a **Berendsen** barostat (**3000 fs** damping). Diffusion coefficients are extracted after switching to the **NVE** ensemble and accumulating mean-square displacements over **≥1 ns** trajectories as described in the article. Additional **NPT** segments (e.g., zero-pressure relaxation of GB models) and high-temperature **NVT** stages (e.g., **1500 K** for **200 ps** in the void/oxidation discussion) appear in the Results/Methods narrative for specific structural setups; supercell sizes, GB construction details, and stage-by-stage run lengths are tabulated in the PDF rather than duplicated here. **Pressure control:** **NPT** segments use the cited **Berendsen** barostat to relax cell volume toward **zero external pressure** where applicable, whereas **NVE** diffusion analysis is strictly constant-volume with **stress tensor**-derived diagnostics only as reported in the article.

**Static QM / DFT-only:** **N/A —** the peer-reviewed contribution centers on ReaxFF training and ReaxFF MD; refer to cited QM references within the article for original DFT settings.

**Electric field / shock / enhanced sampling:** **N/A —** not part of the reported Ni–O diffusion and internal-oxidation initiation studies.

## Findings

The ReaxFF parametrization reproduces Ni self-diffusion and interstitial O diffusion benchmarks, including diffusivities and activation energies that the authors report in quantitative agreement with published values. Beyond dilute interstitial hopping, they propose an **oxygen–vacancy pair** migration mechanism for O transport when vacancies are present. In grain-boundary models containing void space, simulations suggest strong **O–vacancy binding** can drive local oxygen segregation and **NiO** nucleation **inside voids**, offering an atomistic picture for internal oxidation ahead of uniform bulk scale growth. Validation is staged explicitly against literature Ni and O diffusion data; GB/void results are interpreted relative to experimental hints that GB oxygen short circuits may promote oxide inside GB voids. Vacancy concentration and GB topology shift oxygen partitioning between bulk-like interstitial paths versus vacancy-assisted channels and void-trapped oxide precursors (quantitative trends in the article’s figures). ReaxFF inherits QM-training approximations; GB models are finite and high-temperature, so extrapolation to long-time engineering oxidation requires the same caveats stated in the discussion.

## Limitations

- Complex real alloys (alloying elements, long-range stress) are not fully captured in a binary Ni–O model.
- **Short** MD windows can miss rare **long-range** diffusion events; reported diffusivities should be interpreted as consistent with the sampling protocol in the article rather than as exhaustive high-temperature kinetics.

## Relevance to group

Foundational **metal oxidation + ReaxFF** paper from the group with clear validation metrics—often cited for Ni/NiO reactive simulations.

## Citations and evidence anchors

- DOI: [10.1016/j.actamat.2014.09.047](https://doi.org/10.1016/j.actamat.2014.09.047)
- Abstract: `normalized/extracts/2014zou-acta-materia-molecular-dynamics_p1-2.txt`

## Reader notes (navigation)

- **Cluster:** [[theme-oxides-silica-ceramics]] (metal oxidation); compare catalytic Ni surfaces under [[theme-catalysis-surfaces]].  
- **Frozen eval:** MET1 gold hit in [`V1_FROZEN`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/benchmarks/V1_FROZEN.md).
- Proof-PDF sibling for the same DOI/work (Elsevier author proof): [[2014zou-venue-paper]]. Maintainer catalog: [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (section **D**, `2014zou-venue-paper` ↔ this slug).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
