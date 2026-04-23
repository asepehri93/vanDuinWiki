---
id: paper:2012anders-nimb-2013-venue-impacts-cosmic
type: paper
title: "Impacts into cosmic ice surfaces: A molecular-dynamics study using the Reax force field"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - domain:reactive-md
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:reactive-md
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.nimb.2012.10.015"
year: 2013
authors:
  - "Christian Anders"
  - "Herbert M. Urbassek"
venue: "Nuclear Instruments and Methods in Physics Research B 303, 200–204 (2013)"
pdf_sha256: "e382edc632e9b08694a0d840df6c3a6a5ea28bcdaec48f8d46f70ec45ba01763"
pdf_path: "papers/ReaxFF_others/Anders-NIMB-2013.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2012anders-nimb-2013-venue-impacts-cosmic -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Energetic impacts** on **icy Solar System surfaces** (moons, comets, grains) can **dissociate** and **recombine** molecular species; capturing chemistry requires **reactive** potentials. This study uses **ReaxFF** in **LAMMPS** to simulate **cosmic ice** mixtures (**H\(_2\)O, CO\(_2\), CH\(_4\), NH\(_3\)**; **N\(_2\)** noted in astro context) under **cluster–cluster** collisions and **Ne\(^+\)**-like **ion impact** into a **flat** ice target. The authors monitor **reaction products**, **radicals**, and **fragments** to connect **collisional chemistry** to **sputtering** and **prebiotic** contexts where **CHONS** chemistry matters.

## Methods

### 1 — MD application (atomistic dynamics)

Simulations use **LAMMPS** with **ReaxFF** (**van Duin et al.**, “most recent” parameter set as cited) including **charge equilibration** (`normalized/extracts/2012anders-nimb-2013-venue-impacts-cosmic_p1-2.txt`).

- **Engine / code:** **LAMMPS** + **ReaxFF** (Sec. 2.1, extract).
- **System size & composition (flat target):** **PACKMOL**-built **amorphous** ice mixture: **6400 H₂O** plus **300** each of **CO₂**, **CH₄**, **NH₃**, **N₂** in **~80×50×50 Å³**, **23,400 atoms** total, **average density 1.218 g/cm³** (**water** partial density **0.956 g/cm³**) (Sec. 2.2, extract).
- **Boundaries / periodicity (ion impact):** **Viscous (velocity-proportional) damping** applied in the outer **5 Å** on **lateral** and **bottom** faces (not the top free surface); damping constant **46 eV·fs/Å²** (Sec. 2.3, extract).
- **Cluster–cluster collisions:** **Spherical** clusters (**r = 12.2 Å**, **1067 atoms**: **294 H₂O**, **15 CO₂**, **10 CH₄**, **17 NH₃**, **11 N₂**) cut from the target; **no** analogous damping boundary conditions applied in this mode (Sec. 2.3 continuation, extract).
- **Ensemble / timestep / thermostat / barostat:** **N/A —** **NVT**/**NPT**/**NVE** labels, timestep sizes, and thermostat/barostat algorithms are not stated on the indexed excerpt pages beyond the **0 K** relaxation note below.
- **Duration / stages:** Target **surface relaxed at 0 K for 6 ps** to mimic a frozen outer-solar-system ice (Sec. 2.2, extract); **N/A —** full impact/production schedule not on pp. 1–2.
- **Temperature:** **0 K** relaxation of the prepared surface is explicitly stated (Sec. 2.2, extract); **N/A —** subsequent impact thermostat/target temperature details are not on pp. 1–2.
- **Pressure / stress:** **N/A —** not stated on the indexed excerpt pages.
- **Electric field:** **N/A —** not stated on the indexed excerpt pages.
- **Replica / enhanced sampling:** **N/A —** not stated on the indexed excerpt pages.

### 2 — Force-field training

**N/A —** application paper using published **ReaxFF** parameters; **ZBL** hybridization for close encounters is a **modeling protocol** detail (Sec. 2.1, extract).

**Close-encounter repulsion:** **ZBL** is hybridized with **ReaxFF** so **nuclear-like** collisions are treated repulsively while **ReaxFF** dominates the **covalent** range (Fig. 1 example for **N–O**, extract). **Pseudo-Ne** projectiles use **Ne** mass, **O**-like **ReaxFF** attractive parameters, but **Ne** parameters for short-range **ZBL** repulsion (Sec. 2.2 rationale, extract).

### 3 — Static QM / DFT-only

**N/A —** not a DFT-first study in the indexed excerpt.

## Findings

**Outcomes and mechanisms:** The abstract frames **molecular dynamics** of **cosmic ice mixtures** (**H₂O, CO₂, CH₄, NH₃**) using **ReaxFF** to allow **bond rearrangements**, monitoring **radicals**, **fragments**, and **intermediates** for **cluster–cluster** collisions and **Ne⁺**-like **ion impact** into a **flat** target (extract).

**Comparisons:** The introduction contrasts prior **Lennard–Jones** sputtering studies from the same group with the need for **reactive potentials** to capture **molecular** chemistry under irradiation (Introduction, extract).

**Sensitivity and design levers:** Compositionally, the setup explicitly includes **CHONS**-class chemistry availability in **ReaxFF** as motivation; target preparation emphasizes a **multi-component** amorphous ice density recipe (Introduction + Sec. 2.2, extract).

**Limitations / outlook:** The excerpt notes **ReaxFF** potentials are **still being optimized** for universality (Sec. 2.1), and that **pseudo-Ne** is an approximation argued minor at high impact energies (Sec. 2.2, extract).

**Corpus / KB honesty:** Quantitative sputtering yields and full collision-energy sweeps are **not** on `normalized/extracts/2012anders-nimb-2013-venue-impacts-cosmic_p1-2.txt` pp. 1–2; verify **`pdf_path`** for results sections.

## Limitations

- **ReaxFF** parameter sets remain **under active refinement** (as noted); **pseudo-Ne** is an approximation.
- System sizes (~**10⁴** atoms) and timescales remain below full **macroscopic** sputtering experiments.

## Relevance to group

Applied **ReaxFF** to **astrophysical ice chemistry**—shows breadth of reactive FF use beyond terrestrial combustion or electrochemistry.

## Citations and evidence anchors

- DOI: [10.1016/j.nimb.2012.10.015](https://doi.org/10.1016/j.nimb.2012.10.015)
- Text-aligned pointer: `normalized/extracts/2012anders-nimb-2013-venue-impacts-cosmic_p1-2.txt`

## Related topics

- [[reaxff-family]]
- [[theme-water-silica-geo]]
- Impact chemistry and sputtering of molecular ices
