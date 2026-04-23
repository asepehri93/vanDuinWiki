---
id: paper:2015tavazza-venue-research
type: paper
title: "Molecular dynamics investigation of the effects of tip–substrate interactions during nanoindentation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:reactive-md
  - domain:methods-software
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b01275"
year: 2015
authors:
  - "F. Tavazza"
  - "T. P. Senftle"
  - "C. Zou"
  - "C. A. Becker"
  - "A. C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "516536c5dfd1d863e8a45c341281ccda2a1895fef66f675c22c787a0a8762911"
pdf_path: "papers/Tavazza_JPC_2015_indentor.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2015tavazza-venue-research -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the publication identified by `doi` and `pdf_path`.

## Summary

Nanoindentation **MD** often uses **idealized repulsive tips** and neglects **contamination** and **oxide** films. Tavazza *et al.* compare **Ni(111)** indentation with a **deformable diamond** tip under several interaction treatments—**purely repulsive Ni–C**, **attractive Ni–C** augmented by a **DFT-fitted Lennard-Jones** term, and **ReaxFF** that allows **reactive Ni/C/H/O** chemistry—against **AFM tip-blunting** observations and selected **DFT** references. The abstract emphasizes **substantial Ni transfer** to the tip under **clean** or **oxidized Ni** (oxygen included to mimic a **passivating NiO-like** layer), with transferred **Ni** remaining on the tip after retraction, whereas **hydrogen termination** of the **diamond tip** **reduces or eliminates** transfer—an effect described as **larger** than a simple **contaminating oxide** story.

## Methods

**MD application (nanoindentation).** **Engine:** **LAMMPS** for large-scale **molecular dynamics** as referenced in the article/SI. **Substrate:** **(111)-oriented Ni** slab (**~80 × 79 × 50 Å³** in the excerpted Simulation conditions section) with **3D PBC** in **x** and **y** as stated there—**>10⁴ atoms** total in that excerpted geometry class. **Indenter:** **deformable diamond** tip, both **spherical** and **pyramidal** (four **(111)** faces), **atomically stepped** as in the referenced DFT setup. **Protocol (semistatic segment described in excerpt):** indent by lowering a **9 Å-thick grip** layer in **0.1 Å** steps; after each step, run **50 000 MD steps** at **Δt = 1 fs** while fixing the **grip** and the **bottom 6 Å** of Ni in bulk-like positions—each relaxation segment is therefore **~0.05 ns** of **production** **MD** at **1 fs**. **Temperature:** **NVT** **thermostat** (**Nosé–Hoover**) maintains the Kelvin target stated in **`pdf_path`** for these room-temperature-class indentation studies. **Ensemble / thermostat:** **NVT** with a **Nosé–Hoover** thermostat (Sec. 2 excerpt). **Potentials:** (1) **EAM Ni** + **Tersoff C** with **repulsive-only** Ni–C; (2) same plus **LJ** attraction fit to **DFT**; (3) **ReaxFF** for **Ni/C/H/O** enabling **H-terminated tip** and **oxygen-covered Ni** scenarios. **Barostat:** **N/A** — indentation under **NVT** relaxation segments in the excerpted protocol. **Pressure:** **N/A** for bulk **hydrostatic** control; contact **stress** is analyzed via the **virial** formulation in the article. **Electric field / replica enhanced sampling:** **N/A**.

**Force-field fitting (Ni–C LJ).** **QM reference:** **DFT** investigations of early indentation contact used as **source data** for the **attractive LJ** correction (Sec. 2 narrative).

**Static QM / DFT:** **DFT** benchmarks used for **Ni–C** contact fitting/validation—not standalone production MD.

## Findings

**Transfer and retraction:** Under **clean** or **oxidized Ni**, **Ni atoms transfer** to the tip and can **remain adsorbed after retraction** (abstract). **Hydrogen** on the **diamond tip** **strongly suppresses** that transfer—larger effect than the modeled **oxide contaminant** scenario in the abstract’s contrast.

**Comparisons:** Trends are discussed relative to prior **DFT** contact studies and **AFM** observations of **tip blunting** (abstract + introduction).

**Sensitivity:** **Tip chemistry** (**H** vs **clean** vs **oxide**) is the dominant lever on **Ni pickup** in the reported **MD**; **indentation rate** and **tip geometry** modulate deformation details (article discussion).

**Limitations / outlook:** Model **Ni(111)** surfaces omit full **alloy**/**oxide** microstructures of real probes; mapping semistatic **MD** to **AFM** scan rates requires care.

**Modeling lesson:** **Purely repulsive** tips can miss **chemomechanical** adhesion and **wear** channels that appear once **reactive** or **attractive** **Ni–C** interactions are allowed (abstract + introduction).

## Limitations

Focus on **model Ni/diamond** contacts; other metal/ceramic pairs need separate validation. **Indentation speed** and **tip geometry** influence outcomes; mapping to AFM time scales is non-trivial. Supplementary load cases and full thermostat tables are on **`pdf_path`**.

## Relevance to group

**NIST + Penn State** collaboration connecting **ReaxFF-class** modeling to **nanomechanics** interpretation problems with van Duin coauthorship.

## Citations and evidence anchors

- DOI `10.1021/acs.jpcc.5b01275`; `papers/Tavazza_JPC_2015_indentor.pdf`.
- `normalized/extracts/2015tavazza-venue-research_p1-2.txt` (Sec. 2 excerpt).

## Related topics

- [[reaxff-family]]
