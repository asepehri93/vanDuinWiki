---
id: paper:2025zhang-venue-paper
type: paper
title: "ReaxFF studies of surface fluorination of alumina and etching of alumina/aluminum metal heterostructures under gas-phase hydrogen fluoride exposure"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:oxide
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
  - keyword:oxide-surface
  - keyword:dft-static
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1063/5.0260909"
year: 2025
authors:
  - "Yuwei Zhang"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
venue: "J. Chem. Phys."
pdf_sha256: "94771f5b80cdc58715cd48760aba97fa42c674942034e83758dfbd2aac737c63"
pdf_path: "papers/Zhang_Yuwei_AlFHO_JCP_2025_galley.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2025zhang-venue-paper -->

Reactive molecular dynamics with a merged **Al/O/H/F ReaxFF** parameterization is used to study **HF-driven fluorination and etching** of α-Al₂O₃(0001) and **alumina / Al / alumina** heterostructures. The work emphasizes how **surface termination** (Al-rich versus O-rich), **HF chemical potential** (replenishment and gas-phase loading), and **temperature** (1250 K for bare alumina; 750 K for heterostructures to remain below bulk Al melting) control conversion, **HF dissociation kinetics** (Arrhenius analysis), and volatile products (including **AlHₓ** in metal-containing stacks).

## Summary

The study investigates self-limiting **surface conversion** of alumina and oxide–metal–oxide stacks under **gas-phase HF** using ReaxFF. Simulations compare **100% Al–, 50% Al–, and 100% O-terminated** α-Al₂O₃(0001) models and several **sandwiched Al** heterostructures (thick crystalline oxide, thin amorphous oxide, thin crystalline oxide). **DFT** (VASP for periodic HF adsorption on alumina; **Jaguar M06-2X** for small gas-phase HF/H₂O and Al-oxide fragments) supports training and spot checks of HF dissociation pathways relative to ReaxFF.

## Methods

- **Force field:** ReaxFF formulation with **EEM charges**, **bond-order** bonded terms, **Coulomb + van der Waals** nonbonded terms, and **Taper** truncation; the manuscript merges prior **Al/O/H** and **Al/F/H** training and extends the set for **HF on α-Al₂O₃(0001)** (adsorption structures, barriers) as described in Sec. II.C and Fig. 1.
- **DFT reference:** **VASP**, **GGA-PBE**, **PAW**, **500 eV** cutoff, **(2×5×1)** *k*-mesh for a **12-layer (2×1) α-Al₂O₃(0001)** slab; **Jaguar M06-2X / 6-311++G(d,p)** for constrained HF/H₂O and cluster fragments.
- **MD engine and protocol:** Simulations in **LAMMPS**; slabs and heterostructures are relaxed (**NPT**, **Berendsen** thermostat and barostat, **300 K**, pressure damping **5000 fs**, temperature damping **100 fs**), then heated (**NVT**, **Berendsen**, **0.02 K/fs**) to **1250 K** (alumina-only) or **750 K** (heterostructures). Production runs use **NVT** at the target **T**; **time step 0.25 fs**; **HF replenishment** every **0.5 ns** (non-rarefied, ≥120 HF) or **0.25 ns** (rarefied, 10 HF); **H₂O** product molecules removed every **5000** steps; equilibration judged when HF is no longer consumed.
- **Kinetics:** **HF → H⁺ + F⁻** rate constants from **Arrhenius** fits of **ln k vs 1/T** after initial HF loading; additional analysis references **Figs. S1–S3** and **Table I** for slab thinning and **AlFₓ** coordination.

**1 — MD application (atomistic dynamics).** **Engine:** **LAMMPS** **reactive MD** with the merged **Al/O/H/F** **ReaxFF**; **slab** **α-Al₂O₃(0001)** and **oxide/Al/oxide** **heterostructures**; **3D** **PBC**; **NPT** **relaxation** then **NVT** **production** (see above); **time step 0.25 fs**; **multistage** **heating** and **HF** **replenishment**/**H₂O** **removal**; **T** = **1250 K** (bare **alumina**) or **750 K** (stacks, below **Al** **melting**). **N/A** — no **replica**/**metadynamics**; **N/A** — no **static electric field**; **N/A** — no **NPT** **barostat** during the quoted **NVT** **etch** legs.

**2 — Force-field training** — The manuscript **merges** **prior** **Al/O/H** and **Al/F/H** **training**; **N/A** as a net-new “from scratch” **ReaxFF** **paper** in the narrow sense, but new **DFT**-guided **data** for **HF** on **α-Al₂O₃(0001)** are added for **reactive** **MD** (Sec. II.C, Fig. 1).

**3 — Static QM / DFT (spot **QM** and barrier checks).** **VASP** **GGA-PBE** **PAW** **(2×5×1) k-mesh** **12-layer (2×1) slab** **500 eV**; **Jaguar** **M06-2X/6-311++G(d,p)** **cluster** work on **gas**-phase **fragment** and **barrier** checks.
## Findings

- On **α-Al₂O₃(0001) at 1250 K** with replenished HF, **100% Al-terminated** surfaces show the **largest reacted-Al fraction** and **most complete fluorination** versus **50% Al** and especially **100% O-terminated** surfaces (the O-rich case forms dense **hydroxyl** coverage and **little Al–F** despite facile HF dissociation). **Al–F** coordination and **alumina thinning** track the degree of fluorination; **–OH:–F** ratios distinguish residual hydroxyls versus fluoride.
- **HF concentration** on **100% Al-terminated** surfaces is non-monotonic: **higher HF loading** can raise the **barrier** but also the **pre-exponential factor**, with an **optimal** loading (e.g., **280 HF** in the reported series) giving the **deepest** conversion before **very high** loading (**360 HF**) **suppresses** dissociation via **hydrogen-bonding** and **H transport** through **AlFₓ**.
- For **oxide/metal/oxide stacks at 750 K**, **Al diffusion** from the metal layer couples to **AlHₓ** and **AlFₓ** **products**; **thinner oxides** etch more strongly, and **amorphous** **vs** **crystalline** **thin** **oxide** kinetics differ in **barrier** **vs** **pre-factor** **(collision frequency)**. **Rarefied** **vs** **non-rarefied** **HF** exposes **kinetic** **vs** **transport** limits on **ns** **trajectory** **scales** (see **Figs. S1–S3**/**Table I**).

- **Limitation (authored view):** **Idealized** **defect**-free **terminations** isolate **stoichiometry**; **outlook** toward **rough** **real** **films** is in `## Limitations` and the main text.

## Limitations

The repository PDF is an **author proof / galley** (AIP query boilerplate appears in extracts); **page and issue numbers** in the file may be placeholders until the **version of record** is confirmed. Reactive dynamics are **classical (ReaxFF)** and omit explicit **excited-state** chemistry. Idealized **defect-free** terminations isolate stoichiometry effects but omit **real polycrystalline / rough** microstructures.

## Relevance to group

**Adri C. T. van Duin** (Penn State) co-authors; the paper extends **group ReaxFF** development toward **halogen plasma / ALE-relevant** alumina and **metal–oxide** interfaces.

## Citations and evidence anchors

- DOI: [https://doi.org/10.1063/5.0260909](https://doi.org/10.1063/5.0260909)

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
