---
id: paper:2017ai-the-journal-reactive-force
type: paper
title: "A reactive force field molecular dynamics simulation of nickel oxidation in supercritical water"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reactive-md
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:water-interfaces
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.supflu.2017.10.025"
year: 2017
authors:
  - "Liqiang Ai"
  - "Yusi Zhou"
  - "Haishen Huang"
  - "Yongjun Lv"
  - "Min Chen"
venue: "J. Supercrit. Fluids"
pdf_sha256: "ca44a74ae4eb4b9d567f75e4d972d753c37ab67e52e4a3934dc164d84b3c251a"
pdf_path: "papers/ReaxFF_others/2018_LiqiangAi_A reactive force field molecular dynamic simulation of nickel oxidation in supercritical water.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017ai-the-journal-reactive-force -->

## Summary

Reactive molecular dynamics with a **reactive force field (ReaxFF-class)** is used to study **nickel surface oxidation in supercritical water (SCW)** over a range of **temperatures (300–800 °C)** and **densities (26–164 kg m⁻³)** stated in the abstract. The motivation is to probe how extreme water fluid states—between dense liquid and low-density steam—change nickel passivation chemistry relative to near-ambient interfaces. The work follows water adsorption, dissociation, and deprotonation, together with nickel hydroxylation/oxidation, to interpret how SCW conditions alter reaction mechanism compared with ambient liquid water.

## Methods

**MD (LAMMPS, ReaxFF).** **§2** documents **Ni–O–H ReaxFF** (**Assowe et al.**) simulations in **LAMMPS** (`papers/ReaxFF_others/2018_LiqiangAi_A reactive force field molecular dynamic simulation of nickel oxidation in supercritical water.pdf`). A **fcc Ni** slab plus **supercritical water (SCW)** occupies **28.896 × 28.896 × 51.896 Å³** with **968–1078 atoms** depending on **(110)/(100)/(111)** termination (**Table 1**). **PBC** span **x** and **y**; the **z** axis uses a **fixed** boundary with a **reflecting wall** so only one **Ni–water** interface reacts. Production runs use **NVT** integration, **Berendsen thermostat**, and **Δt = 0.25 fs** across **4,000,000** steps (**~1 ns** at that **timestep**); **thermostat damping** constants are **not** quoted in the **§2** excerpt checked here. The **Ni–water** slab leg is **constant-volume** (**no barostat** on that segment). Auxiliary **bulk SCW** **NPT** trajectories (**~0.25 ns** per state point) map **temperature–density** grids against the **FEQ Helmholtz EOS** (**Fig. 4**). State points follow the abstract grids (**300–800 °C** at selected **ρ**, and **600 °C** across **26.1–164 kg m⁻³**). **Electric fields** and **replica / enhanced sampling** are **not** applied.

**Force-field training:** **N/A — applies** the published **Assowe** parameter set.

**Static QM (validation).** **CASTEP** spin-polarized **PBE** with **ultrasoft pseudopotentials** and a **571 eV** cutoff benchmarks **gas-phase water**, **water/Ni**, and **OH/Ni(110)** energetics versus **ReaxFF** (**§2**, **Figs. 1–2**).

## Findings

Time-resolved bond metrics (**r_cut,NiO = 2.1 Å**, **r_cut,OH = 1.2 Å**, §3) show **hydration**, **water dissociation**, **hydroxylation**, and **oxide** thickening with **Ni/O** rearrangement. **SCW** is argued to be a **stronger oxidizer** than **ambient water** for the sampled states, with rates rising with **temperature** and **fluid density**. **Deprotonation** statistics motivate **homolytic**-leaning **water cleavage** at **high T** and **lower ρ**, framed as more **radical-like** than ambient **ionic** chemistry. **Ni(110)/(100)/(111)** comparisons use **Table 1** trajectories. **Limitations:** accuracy stays within the **Assowe** training manifold; **DFT** checks are **spot validations**, not exhaustive **oxide** coverage.
## Limitations

This repo’s PDF filename suggests a 2018 volume imprint; the abstract header lists *J. Supercrit. Fluids* **133**, **421–428** with **©2017** — reconcile against your PDF’s final bibliographic block. Supercritical water chemistry is sensitive to cluster statistics and surface facet choice; the abstract’s mechanistic classification should be read alongside the article’s full surface model and sampling duration rather than as a universal Ni oxidation rule across all crystallographic terminations.

## Relevance to group

Application of ReaxFF-style reactive MD to **corrosion/oxidation** of **Ni** in extreme **water** environments (energy-systems context).

## Citations and evidence anchors

- DOI: `10.1016/j.supflu.2017.10.025`.

## Reader notes (navigation)

- Ni–water oxidation at ambient field: [[2012assowe-venue-reactive-molecular]]; extreme P–T water chemistry cluster in [[theme-reactive-md-corpus]].

## Related topics

- [[reaxff-family]]
- [[2012assowe-venue-reactive-molecular]]
- [[theme-reactive-md-corpus]]
