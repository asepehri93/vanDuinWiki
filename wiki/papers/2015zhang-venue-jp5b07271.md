---
id: paper:2015zhang-venue-jp5b07271
type: paper
title: "ReaxFF Reactive Molecular Dynamics Simulation of Functionalized Poly(phenylene oxide) Anion Exchange Membrane"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:batteries-interfaces
  - keyword:water-interfaces
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b07271"
year: 2015
authors:
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "153cf51adb27c08de61564093605efbf3bf54c91e76378298ff759e0cee9c136"
pdf_path: "papers/Zhang_Anion_Exchange_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015zhang-venue-jp5b07271 -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the article identified by `pdf_path` and **`doi`**.

## Summary

Alkaline anion exchange membranes (AEMs) for fuel cells require both **hydroxide conductivity** and **chemical stability** under high-pH operation. This **J. Phys. Chem. C** study uses **ReaxFF molecular dynamics** to compare **quaternized poly(phenylene oxide)** membranes bearing **trimethylammonium (TMA)**, **dimethylbenzylammonium (DMBA)**, and **dimethyloctylammonium (DMOA)** headgroups at controlled hydration (**λ = 8.3** and **20.8** water molecules per cation). Simulations resolve membrane **swelling**, **nanophase** structure, **hydroxide** mobility, and **degradation** tendencies associated with **OH\(^-\)** attack on cation centers versus **hydrophobic shielding** by long alkyl substituents.

The comparison is structured around **headgroup** **sterics** and **hydrophobicity**: **TMA** is compact, **DMBA** adds an **aromatic** substituent, and **DMOA** introduces a **long** **alkyl** tail intended to **shield** the **quaternary** nitrogen from nucleophilic attack while still permitting hydration channels at high **λ**.

## Methods

All **ReaxFF reactive molecular dynamics** in the main text uses **ADF 2012** (`papers/Zhang_Anion_Exchange_JPCC_2015.pdf`, Computational Details)—**molecular dynamics** trajectories in the authors’ **MD package**, not **LAMMPS** unless parameters are ported. **Amorphous quaternized PPO** membranes carry **TMA**, **DMBA**, or **DMOA** headgroups at **λ = 8.3** and **20.8** **H₂O** per cation plus **OH⁻** in **3D periodic supercells** (full **atom** counts, box sizes, and equilibration in §2 / tables). **Velocity Verlet**, **0.25 fs** timestep, **Berendsen** thermostat (**100 fs** coupling) on the **whole** system for **NVT**-style room-temperature production (exact **T** in the article’s table). No barostat, controlled pressure, electric field, or enhanced sampling in the cited protocol. Analysis includes **RDFs**, coordination, **swelling**, **OH⁻** **MSD**/diffusivity, and **degradation** statistics (§3).

**Force-field training:** **N/A —** a published-style **ReaxFF** set for **PPO / quaternary ammonium / hydroxide** is **used**; full numerical tables are in **`[[2015zhang-venue-microsoft-word]]`** (SI PDF), not a new refit narrative in the article body.

**Static QM / DFT:** **N/A —** not the dominant modality relative to ReaxFF MD (any QM benchmarks only in the PDF if present).

## Findings

**Higher λ** swells membranes, improves **water** connectivity, and raises **OH⁻** diffusivity; **TMA** shows the **largest OH⁻ diffusion constant** of the three headgroups at **high λ** in the authors’ comparison (§3). **DMOA’s** long **alkyl** tails **shield** the quaternary **N** from **OH⁻**, lowering **degradation** versus more exposed headgroups—**hydrophobic protection**. **TMA**, **DMBA**, and **DMOA** are compared head-to-head at matched **λ** for **transport** and **stability**. **λ** trades **conductivity** (more water aids **OH⁻** transport) against **OH⁻** exposure. Discussion flags missing **CO₂ / carbonation** chemistry for air-exposed AEMs. For machine porting, take **ReaxFF** numbers from **`[[2015zhang-venue-microsoft-word]]`** plus **JPCC** Methods—**ADF** inputs are primary, not assumed **LAMMPS** decks.

## Limitations

ReaxFF organic/ion chemistry may omit **carbonation**, **CO\(_2\)**, and **bicarbonate** chemistry relevant to air-exposed AEM operation.

## Relevance to group

Penn State **ReaxFF** application to **AEM** **ion transport** and **alkaline stability**.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.jpcc.5b07271](https://doi.org/10.1021/acs.jpcc.5b07271) (`papers/Zhang_Anion_Exchange_JPCC_2015.pdf`); SI: `papers/Zhang_Anion_Exchange_SI_JPCC_2015.pdf`.
- **SI parameters:** numerical **ReaxFF** tables in **`[[2015zhang-venue-microsoft-word]]`**.

## Related topics

- [[2015zhang-venue-microsoft-word]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
