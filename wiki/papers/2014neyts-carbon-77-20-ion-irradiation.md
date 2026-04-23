---
id: paper:2014neyts-carbon-77-20-ion-irradiation
type: paper
title: "Ion irradiation for improved graphene network formation in carbon nanotube growth"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:catalysis-surface
  - keyword:berendsen-thermostat
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2014.05.083"
year: 2014
authors:
  - "E. C. Neyts"
  - "A. Bogaerts"
venue: "Carbon 77, 790–795 (2014)"
pdf_sha256: "629b6c6ea7238060774c1eb9d6b96b0020f76b48ad2e4e8b4de5d4978438ff4d"
pdf_path: "papers/ReaxFF_others/Neyts_CNT_growth_Carbon_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014neyts-carbon-77-20-ion-irradiation -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow the **Carbon** article abstract (`doi`). Quantitative energy windows and mechanisms should be verified in the **full text**.

## Summary

Uses **reactive molecular dynamics** to argue that **Ar⁺ irradiation** in an extended **10–35 eV** window can **heal** carbon-network defects **after nucleation** via a **non-metal-mediated** mechanism when the growing **carbon** network is **not** in contact with the **Ni** **catalyst**—complementing prior work showing **10–25 eV** **Ar⁺** can **enhance cap nucleation** when **metal** contact is present. The **Carbon** article frames **low-energy ion** bombardment as a tunable knob in **PECVD**-like **carbon nanotube (CNT)** growth: **ions** can either **assist** early **nucleation** near **metal** or **anneal** **defective** **graphene** **networks** away from **metal**, depending on **energy** and **geometry**. This **dual** role motivates careful **energy** windows rather than treating **ions** only as **damaging** projectiles.

## Methods

### Interatomic models

- **Reactive MD** uses **ReaxFF** parameters for **Ni–C** from **Mueller *et al.***.
- **Ar–Ni** and **Ar–C** interactions use a **Molière** potential with **Firsov** constants consistent with the authors’ prior ion-beam studies (**abstract**; **Carbon** article).

### Initial configuration and thermalization

- Starting geometry: **defective single-walled CNT cap** on a **surface-bound Ni\(_{40}\)** cluster, thermalized at **1000 K** using a **Berendsen** thermostat with **250 fs** damping (**extract**).

### Ion bombardment protocol

- **Ar⁺** impacts are modeled as **fast neutrals** with **Auger** neutralization rationale stated in the article.
- Beam energies span **10–50 eV** with **200** consecutive impacts per trajectory, **rethermalizing to 1000 K** after each impact (**extract**).
- **Velocity Verlet** integration; statistics from **10** independent replicas per energy (**extract**).

### Evidence anchor

- Full parameter tables: **Carbon** **77**, 790–795; `normalized/extracts/2014neyts-carbon-77-20-ion-irradiation_p1-2.txt`.

### 1 — MD application (atomistic dynamics)

- **Engine / code:** **Reactive molecular dynamics** with **ReaxFF** (extract/abstract); **N/A — MD integrator package** not named in `2014neyts-carbon-77-20-ion-irradiation_p1-2.txt`.
- **System size & composition:** **Defective single-walled CNT cap** on a **surface-bound Ni₄₀** cluster (extract); **Ar⁺** modeled as **fast neutrals** with **Auger** neutralization rationale per article framing (abstract).
- **Boundaries / periodicity:** **N/A — full cell boundary description** beyond the excerpt’s geometry hint—confirm in **Carbon** **77** PDF.
- **Ensemble:** **NVT**-like constant-temperature segments are implied by **Berendsen** thermalization/rethermalization language, but **N/A — explicit NVT/NPT declaration** not in `p1–2` text—confirm in **Carbon** **77**.
- **Timestep:** **Velocity Verlet** integration noted (extract); **N/A — numerical timestep** not in `p1–2` text.
- **Duration / stages:** **200** consecutive **Ar⁺** impacts per trajectory with **rethermalization to 1000 K** after each impact (extract); statistics from **10** replicas per beam energy.
- **Thermostat:** **Berendsen** thermostat with **250 fs** damping during thermalization at **1000 K** (extract).
- **Barostat:** **N/A — not stated** in the indexed excerpt.
- **Temperature:** **1000 K** thermalization; beam energies **10–50 eV** explored (extract).
- **Pressure:** **N/A — not stated** as a controlled bulk **pressure** in the excerpt.
- **Electric field:** **N/A — not stated.**
- **Replica / enhanced sampling:** **N/A — not stated** (independent **replica** trajectories used for statistics, not enhanced sampling in the metadynamics sense).

### 2 — Force-field training

**N/A —** this article applies **ReaxFF**; it does not report a new **parameterization** workflow in the abstract/excerpt layer.

## Findings

### Outcomes and mechanisms

The work argues **10–35 eV Ar⁺** can **heal** **carbon-network** defects **after nucleation** by a **non-metal-mediated** mechanism when the growing network is **not** on the **Ni** **catalyst**, complementing prior **10–25 eV** **metal-contact** **nucleation** assists (abstract/extract narrative).

### Comparisons

Positions **low-energy ion** effects relative to earlier **Neyts**/**Bogaerts** **CNT nucleation** studies cited in **Carbon** **77**.

### Sensitivity

Beam **energy** window (**10–50 eV** in simulations) and **metal** contact versus detached **network** geometry are the central **sensitivity** axes in the summarized story.

### Limitations and corpus honesty

**Hyperthermal** **ion** impacts are **force-field**- and **model**-dependent; translate to **PECVD** only with reactor-specific **ion** energy distributions. Prefer the **version-of-record** **PDF** for figures/tables beyond the excerpt.

## Limitations

**Finite** simulation **size** and **impact** count; **ReaxFF** transferability for **hyperthermal** **ion** impacts; **experimental** translation depends on **plasma** **ion energy distributions** and **surface** **bias** not fully captured in the idealized **beam** model.

## Relevance to group

**Reactive carbon** + **plasma/ion** processing literature adjacent to **ReaxFF** C/H/O work in the corpus.

## Citations and evidence anchors

- https://doi.org/10.1016/j.carbon.2014.05.083 — **Carbon** **77**, 790–795.

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]

## Reader notes (navigation)

The **Carbon** article should be read together with earlier **Neyts**/**Bogaerts** **CNT nucleation** work cited therein to distinguish **metal-contact** **nucleation** assists from **post-nucleation** **healing** **windows** reported here. **Impact** statistics (**200** impacts per energy, **10** replicas) matter when interpreting **defect** **annealing** versus **accumulated** **damage** trade-offs.
