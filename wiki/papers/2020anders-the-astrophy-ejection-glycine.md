---
id: paper:2020anders-the-astrophy-ejection-glycine
type: paper
title: "Ejection of Glycine Molecules Adsorbed on a Water Ice Surface by Swift-heavy Ion Irradiation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:water-interfaces
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.3847/1538-4357/ab6efe"
year: 2020
authors:
  - "Anders, Christian"
  - "Bringa, Eduardo M."
  - "Urbassek, Herbert M."
venue: "Astrophys. J."
pdf_sha256: "4e57860ea0910fcb50608e05e7b7106a308473c1379edfc3b354c41bc74e0954"
pdf_path: "papers/ReaxFF_others/Anders_Bringa_Water_Ice_2020_ApJ_891_21.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2020anders-the-astrophy-ejection-glycine -->

!!! abstract "Scope"

Classical molecular dynamics of a 2 MeV sulfur ion impacting glycine adsorbed on water ice, modeling magnetospheric irradiation of Europa-like surfaces and quantifying intact versus fragmented ejecta velocities.

## Summary

Solar-system ice bodies host organic molecules that may be sputtered into exospheres by energetic ions. Focusing on glycine on crystalline water ice as a prototype amino-acid–ice system, the authors simulate a single swift-heavy-ion impact representative of magnetospheric sulfur ions impinging on Europa. The goal is to quantify radial zones of molecular survival versus fragmentation and to estimate ejecta speeds relative to Europa’s escape velocity for astrobiological transport models. The **Astrophys. J.** framing connects **classical** **collision cascades** to **observable** **exosphere** **composition** constraints without resolving **electronic** **excitation** explicitly.

## Methods

**MD engine / interactions.** Molecular dynamics with **ReaxFF** (Monti et al. 2013 parametrization optimized for **glycine**-containing systems) so bond making/breaking can occur during the cascade. The **two-body** ReaxFF terms are **splined** to the **ZBL** potential at high pair energies to capture **projectile–target** nuclear collisions; **electronic stopping** for the **2 MeV S** ion is represented with a **thermal-track** energy-deposition model consistent with their prior ion-track work (see **ApJ** Methods and citations). **3D** **PBC** in the **lateral** **x**/**y** **ice** **film** (or as stated) with **border** **thermostat** **zones**; see paper for full **boundary** **conditions** on **z**.

**Target construction.** An **amorphous** **water-ice** slab is built with **PACKMOL** (**~204 × 104 Å** surface footprint, **~212 Å** depth); **1000** **glycine** molecules are placed on the top surface (**~2 Å** average spacing). After relaxation and surface creation, the film is equilibrated **18 ps** at **101 K** (Europa-like surface **T**). **Berendsen** thermostats (**10 Å** border zones on sides/bottom) hold **101 K** while the top remains free.

**Impact protocol.** A **2 MeV** **sulfur** ion impacts at **45°** to the surface normal (magnetospheric **S** on **Europa**-like **ice**). **Electronic stopping power** is taken as **~89 eV Å⁻¹** in the reported parameterization.

**Analysis.** Radial **maps** distinguish **intact** **glycine** **desorption** vs **fragmentation**; catalogs include **CN⁻**, **CO**, **OCN⁻**, **CO₂**, and **water**-radiolysis products (**H⁺**, **H₃O⁺**, **HO⁻**, **H₂**, **O₂**, **H₂O₂**, per abstract). **Velocity** distributions are extracted for **organics** and **light** **fragments** for comparison to **Europa** **escape** (**~2 km s⁻¹**).

**MD protocol (additional coverage).** **N/A** — no **NPT** **barostat** (non-equilibrium **impact** cascade; **N/A** for **replica** **umbrella**). **N/A** — static **E**-field. **N/A —** **cumulative** **equilibration**+**cascade** **ps** in one line: see *ApJ*; **~18** **ps** pre-impact **NVT** **thermalization** of the **ice** film is reported. **Adaptive** **timestep** during the **ZBL**+**ReaxFF** **collision** stage: **N/A** for a single number here. **N/A —** **shear**; **2 MeV** **S** is **~45°** to **normal** (magnetospheric) **shock**-analog in abstract framing.

**FF training (block 2).** **N/A** — uses a published **Reaxff** (Monti et al. 2013) with **ZBL** **splice**.

**Static QM (block 3).** **N/A** — DFT is not the engine of the **MD** **cascade** study.

## Findings

**1 — Outcomes and mechanisms**

- **Spatial pattern.** The authors map **intact** glycine **ejection** out to about **25 Å** from the ion path, while a **~10 Å** **core** experiences strong **shattering**; **most** ejecta in that core are **fragments** rather than whole molecules.
- **Glycine and water chemistry.** The impact drives extensive **bond breaking** in the **thermal spike**; **~189** glycine units are **destroyed** in their accounting, with many **Gly±H** (protonation/deprotonation) products, while **water** is **partially** **replenished** by **recombination** after **radiolysis** (H⁺, OH⁻, H₃O⁺, then **H₂** and **O₂** within about **1 ps**), consistent with **laboratory** water-ice **radiolysis** references they cite.
- **C–N–O fragments.** **CN⁻**, **CO**, **OCN⁻**, and **CO₂** appear among **C/N/O** products, with several species flagged as matching **Portugal** *et al.* **experimental** assignments where noted in their **Table 2** / **“Exp”** column.
- **No di-glycine.** In this **~32.1 ps** track, they **do not** observe **peptide-bond** formation, and they argue the **thermodynamic** **window** for **dimerization** (vs prior **shock** studies at **higher** sustained **pressure**/**temperature**) is too **brief** for **C–N** coupling in the track.

**2 — Comparisons**

- **Direct nuclear damage vs thermal spike.** Only about **0.4 keV** of the **2 MeV S** energy goes to **nuclear** stopping; the authors estimate **O(10)** **direct-collision** dissociations, versus **hundreds** from the **electronic**-stopping **thermal track**—so **cascade chemistry** is **spike-dominated**, not **projectile-knock-on**-dominated.
- **Experiments.** **Fragment** identities and **intact** **ejection** of a **minority** of **Gly±H** are discussed alongside **Hedin**, **Ens**, and related **swift-ion** **desorption** work; **H₂**/**O₂** from **ice** match **Bar-Nun**/**Baragiola**-class **laboratory** **radiolysis** expectations.

**3 — Sensitivity and design levers**

- **Ejecta velocity vs mass.** **Light** **fragments** and **volatiles** readily exceed **Europa**’s **~2 km s⁻¹** **escape** speed, whereas **most** ejected **intact** **glycine** remains **slower**—a **strong** **mass**/**energy** **partitioning** for **exosphere** modeling.
- **Electronic stopping model.** The **thermal-track** **radius** (**R = 5 Å**) and **stopping** **power** choice set the **deposited** **energy** density; the authors note **not** all **electronic** loss becomes **lattice** **heat**, which would **lower** **yields** but leave **qualitative** behavior from their **prior** **ice** studies.

**4 — Limitations and outlook (as authored)**

- **Single track, one impact geometry:** they position the run as a **detailed** **template** for **height**/**flux** **models** of **ejecta** in **Europa**-like **exospheres**, not a **full** **fluence** **average**; **O₂ ejection** is **suppressed** at **low** **fluence** in their run compared to **steady** **sputtering** pictures with **trapped** **O₂** accumulation.
- **Classical chemistry:** **electronic** **excitation** is **mimicked** by **heating** in the track—appropriate for their **rarefied** **chemistry** goals but not a full **first-principles** **nonadiabatic** model.

**5 — Corpus / KB honesty**

- Numbers and **species** lists follow **`pdf_path`**; this page does not duplicate **Table 2** in full.

## Limitations

Classical potentials cannot capture all electronic excitation channels; single-impact statistics require ensemble averaging for exospheric flux models.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

Astro-chemistry / **impact** **cascade** **reference** in the broader corpus; **ReaxFF**+**ZBL** **classical** **RMD** (not a DFT or continuum study).

## Citations and evidence anchors

- https://doi.org/10.3847/1538-4357/ab6efe

## Related topics

- [[reaxff-family]]
