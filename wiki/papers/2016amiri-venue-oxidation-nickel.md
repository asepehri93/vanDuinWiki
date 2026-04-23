---
id: paper:2016amiri-venue-oxidation-nickel
type: paper
title: "Oxidation of nickel surfaces through the energetic impacts of oxygen molecules: Reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reactive-md
  - method:reaxff
  - domain:oxides-ceramics
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:metallic-systems
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1063/1.4945421"
year: 2016
authors:
  - "Negar Amiri"
  - "Hassan Behnejad"
venue: "J. Chem. Phys."
pdf_sha256: "5d47b4e229adf596dbec91b8599b3a027ea3094bd25849dbd0b422ca780bd93c"
pdf_path: "papers/ReaxFF_others/Amiri_NiO_impact_JCP_2016.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2016amiri-venue-oxidation-nickel -->

## Summary

Reactive molecular dynamics with ReaxFF studies hyperthermal oxidation of Ni(100) and Ni(111) by 5 eV O₂ impacts at surface temperatures of 300, 600, and 900 K. The work connects impact-driven nucleation, growth kinetics (island versus Langmuir-like descriptions), oxygen uptake versus temperature, and the amorphous structure of the growing NiO film, with analysis of radial distribution functions, oxygen density profiles, and charge distributions. The **J. Chem. Phys.** article targets **aerospace**-relevant **hyperthermal** **atomic/molecular** **oxygen** scenarios where **impact** **energy** **deposits** **locally** and drives **non-equilibrium** **oxide** **nucleation**.

## Methods

### MD application (atomistic dynamics)

- **Engine / code:** **LAMMPS** (parallel ReaxFF integration path cited in the Computational Details section) with **variable-charge ReaxFF** for **Ni–O** chemistry.
- **Force-field lineage:** Ni–O parameters are taken from the **Zou et al.** ReaxFF training line referenced in the article (with additional Ni/O oxide formation benchmarks discussed there against QM heats of formation).
- **Surfaces / supercells:** **Ni(100)** in a **(9×9)** surface unit cell (**162** surface Ni atoms) and **Ni(111)** in a **(7×7)** cell (**196** surface Ni atoms), each with **eight** Ni layers in **Z** (Table I in the article).
- **Boundaries / periodicity:** **Periodic in XY** during equilibration and the **hyperthermal impact** stage; **Z** is treated as the non-periodic direction for gas-phase **O₂** approach (normal incidence), consistent with the slab-with-vacuum geometry described in Computational Details.
- **Equilibration:** Substrates coupled to a **Berendsen** thermostat for **20 ps** at **300**, **600**, or **900 K** (damping **0.1 ps**), then **10 ps NVE** relaxation before impacts.
- **Impact protocol:** **O₂** molecules introduced **every 2.5 ps** at **15 Å** above the surface, **5 eV** translational energy, **normal incidence**, random **XY** placement; **Berendsen** thermostat used to remove excess energy **before each new impact** as described in the article.
- **Ensemble during oxidation:** The protocol uses **Berendsen** thermalization during **substrate equilibration**, a short **NVE** segment (**10 ps**) after equilibration, then **hyperthermal O₂** impacts with **Berendsen** cooling **before each new impact** to remove excess energy (Computational Details in *J. Chem. Phys.* **144**, **144705**).
- **Timestep:** **0.25 fs** (**velocity Verlet** integration stated in Computational Details).
- **Duration / sampling:** Results quoted in the abstract follow **200 successive O₂ impacts** per supercell for growth-rate and film-structure analysis.
- **Thermostat:** **Berendsen** during **substrate equilibration** (**20 ps**, damping **0.1 ps**) and **between successive O₂ impacts**; **N/A — Nosé–Hoover** is **not** the thermostat used in the documented hyperthermal oxidation loop.
- **Barostat:** **N/A — not used** in the documented hyperthermal oxidation workflow.
- **Temperature:** Substrate setpoints **300 / 600 / 900 K** for the compared series.
- **Pressure:** **N/A — not a controlled thermodynamic variable** in the impact protocol described.
- **Electric field:** **N/A — not used.**
- **Replica / enhanced sampling:** **N/A — not used.**
- **Diagnostics:** **Oxygen uptake vs impact count**, **RDFs**, **oxygen density profiles**, and **charge profiles** across **Ni | NiO** for film morphology.

### Force-field training

**N/A — application paper** using a literature **ReaxFF Ni/O** parameterization with QM benchmarks cited for validation; it does not report a new ReaxFF optimization campaign as the contribution.

### Static QM / DFT

**N/A — not a DFT production study**; QM values appear as **reference heats of formation** for force-field context in the ReaxFF section, not as AIMD results driving the oxidation trajectories.

## Findings

- **Nucleation sites:** Under **5 eV O₂** impacts, **primary oxide nuclei** can appear at **arbitrary impact sites**, contrasting with island-perimeter-limited pictures from some thermal oxidation scenarios discussed in the introduction.
- **Growth law comparison:** The authors report that an **island-growth** picture **does not** accurately describe their simulated uptake kinetics; under these hyperthermal conditions growth is described as closer to a **Langmuir-type** law.
- **Temperature sensitivity:** Raising the surface temperature from **300 K** to **900 K** increases **oxygen consumption** by about **18.75%** on **Ni(100)** and about **23%** on **Ni(111)** by the end of the **200-impact** series (abstract values).
- **Film structure:** After **200 impacts**, the **NiO** film is **amorphous** according to **RDF** and **density-profile** diagnostics in the article.
- **Plasticity / twins:** Additional mechanical-response discussion (including **twinning**) appears later in the full text beyond the abstract-level oxidation summary—consult **`pdf_path`** for stress–strain context if linking this paper to nanomechanics notes.

## Limitations

Another corpus slug (`2016amiri-venue-oxidation-nickel-2`) points to a second PDF with the same DOI—verify checksum when deduplicating.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

Reactive MD/ReaxFF lineage for metal oxidation under energetic oxygen exposure (aerospace-relevant hyperthermal conditions).

## Citations and evidence anchors

- DOI: [10.1063/1.4945421](https://doi.org/10.1063/1.4945421)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
