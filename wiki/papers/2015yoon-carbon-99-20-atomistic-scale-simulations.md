---
id: paper:2015yoon-carbon-99-20-atomistic-scale-simulations
type: paper
title: "Atomistic-scale simulations of the chemomechanical behavior of graphene under nanoprojectile impact"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:mechanics-tribology
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2015.11.052"
year: 2015
authors:
  - "Kichul Yoon"
  - "Alireza Ostadhossein"
  - "Adri C. T. van Duin"
venue: "Carbon, 99 (2016) 58–64"
pdf_sha256: "1bdb01e1fb2e05795b21499c8d4ef9451b37c4528178d902d0340806cfbf1f88"
pdf_path: "papers/Yoon_Carbon_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015yoon-carbon-99-20-atomistic-scale-simulations -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study uses ReaxFF to simulate supersonic impact of nanoscale silica and nickel projectiles on single-layer graphene, enabling bond-breaking chemistry at the projectile–graphene interface beyond fixed-bond carbon potentials. Reported penetration energies \(E_p^*\) are related to pre-crack deformation, defect content (mono-vacancies, grain boundaries), and projectile chemistry, including crack-edge structures such as pentagon–heptagon pairs during penetration. Simulated \(E_p^*\) values are compared with multilayer graphene experiments (Lee et al., Science 2014), supporting large energy absorption under extreme strain-rate loading.

## Methods

**LAMMPS ReaxFF** (`papers/Yoon_Carbon_2015.pdf`, §2) merges **C-2013** carbon parameters with published **Si/O/C/H** and **Ni/O/C/H** subsets for projectile chemistry. **Hydrogen-terminated** single-layer **graphene** sheets (**~380 Å × 360 Å**) are **pristine** or contain **mono-vacancies** or **polycrystalline** patches (**~25 Å** grain size). **Spherical amorphous silica** (**~48 Å** diameter) and **fcc Ni** (**~38 Å**) projectiles impact along the surface normal. **In-plane PBC**, **H-passivated** edges with **edge C atoms fixed** mimic supported samples. After **0.1 K** minimization and **300 K** equilibration (including defective models where noted), production is **NVE** microcanonical penetration with **0.05 fs** timestep and initial projectile speed **5 km s⁻¹** (authors state this exceeds typical **~1 km s⁻¹** experiments to remain tractable at the modeled scale). **Pressure** in the shock direction is not a fixed **GPa** setpoint but emerges from the **NVE** piston; lateral **stress** relaxes according to the periodic **slab** constraints in §2. No thermostat or barostat during **NVE** impact; no electric field or enhanced sampling. **Specific penetration energy** \(E_p^\*\) comes from projectile **kinetic-energy loss** per mass; **armchair vs zigzag** edges and **5|7** rings are tracked (abstract, §3).

**Force-field training:** **N/A —** literature merges are used.

**Static QM / DFT:** **N/A —** not the primary modality.

## Findings

**ReaxFF** captures **reactive** **oxidation** and fracture **mechanisms** for **Ni** or **silica** impact on **graphene**, beyond fixed-bond carbon models (`papers/Yoon_Carbon_2015.pdf`). Simulated **\(E_p^\*\)** is the same **order of magnitude** as **Lee et al., Science 2014** **experimental** multilayer-graphene microparticle impacts—a **benchmark comparison** noted in the abstract. **Pentagon–heptagon** defects appear at crack edges; **pre-crack deformability** and **defect** content (**mono-vacancy**, **grain boundary**) **sensitivity** shifts **\(E_p^\*\)** and morphology, as does **projectile** chemistry (**Ni** vs **silica**). **Limitations** in **§2** include **single-layer** models versus **multilayer** tests and **higher simulated impact speed** than typical experiment. **Corpus honesty**: tabulated **\(E_p^\*\)** values and time-resolved **react**ion counts belong in the journal **PDF** figures; this page stays at abstract precision.

## Limitations

- ReaxFF C-2013 tensile response differs from REBO families at moderate strain; the reported impact studies operate in large-strain fracture regimes where this parametrization was judged applicable in the original work.
- Direct comparison to experiment is indirect (multilayer experimental graphene vs simulated single-layer).

## Relevance to group

Demonstrates ReaxFF for **2D carbon under extreme mechanical loading** with van Duin group leadership—useful reference for reactive simulations of graphene in contact with metals/oxides.

## Citations and evidence anchors

- DOI: [10.1016/j.carbon.2015.11.052](https://doi.org/10.1016/j.carbon.2015.11.052)
- Abstract and Methods: `normalized/extracts/2015yoon-carbon-99-20-atomistic-scale-simulations_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
