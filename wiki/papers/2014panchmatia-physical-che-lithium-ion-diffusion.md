---
id: paper:2014panchmatia-physical-che-lithium-ion-diffusion
type: paper
title: "Lithium-ion diffusion mechanisms in the battery anode material Li₁₊ₓV₁₋ₓO₂"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:batteries-electrochemistry
  - material:oxide
  - method:classical-md
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:classical-ff
  - keyword:batteries-interfaces
  - keyword:oxide-surface
  - keyword:nose-hoover
  - keyword:npt-simulation
  - keyword:nvt-simulation
candidate_tags: []
source_refs: []
doi: "10.1039/C4CP01640H"
year: 2014
authors:
  - "Pooja M. Panchmatia"
  - "A. Robert Armstrong"
  - "Peter G. Bruce"
  - "M. Saiful Islam"
venue: "Phys. Chem. Chem. Phys. 16, 21114–21118 (2014)"
pdf_sha256: "f82292950a0461da930c19c10dafbf2721e24ea29476285b31df93729336440f"
pdf_path: "papers/Others/LiVO2_PCCP_diffusion_sept14.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014panchmatia-physical-che-lithium-ion-diffusion -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow the **PCCP** communication (`doi`). Methods are **atomistic simulation** (potentials described in the paper), **not** ReaxFF from this wiki’s perspective unless cited there.

## Summary

Layered **Li₁₊ₓV₁₋ₓO₂** is investigated as a **low-voltage oxide anode** candidate offering **high energy density** by exploiting **Li⁺** storage in **transition-metal layers**. The communication uses **atomistic simulation** to compare **stoichiometric LiVO₂** with **Li-rich non-stoichiometric** compositions. In the model, **stoichiometric LiVO₂** exhibits **no facile long-range Li⁺ migration** on **>1 ns** MD trajectories, aligning with **poor electrochemical intercalation** behavior. By contrast, **Li-rich** structures with **interstitial Li** occupying sites related to **transition-metal layers** enable **cooperative interstitial diffusion** with **lower barriers** and **higher Li diffusivity**, linking **excess Li** to improved **rate capability** in the simulation framework. The **PCCP** study thus ties **non-stoichiometry**—often accessible synthetically—to **microscopic** **transport** motifs that could rationalize **rate** improvements without invoking **surface** **reactions** alone. **When** connecting to **ReaxFF** **electrolyte** pages, remember this work uses **fixed-charge** **shell** models rather than **bonded** **reactive** **oxide** **electrodes**, so **interfacial** **charge transfer** must be **imported** from **other** sources.

## Methods

### Interatomic model (classical shell potential)

- **Buckingham**-type **shell model** potentials parameterized/refined using **GULP**, with parameters collected in **ESI Table S1** (article citation in extract).
- **Defect energetics:** **Mott–Littleton** calculations for **isolated** defect energies where required by the parameterization workflow (article).

### Molecular dynamics protocol

- **Code:** **DL_POLY 2.20**.
- **Integration:** **0.5 fs** timestep; **Nose–Hoover** thermostat; **NPT** equilibration followed by **NVT** production runs exceeding **1.1 ns** total sampling for the trajectories summarized in the extract.
- **Electrostatics / cutoffs:** follow **DL_POLY** settings described in the **PCCP** article (not fully reproduced in the short extract).

### Simulation cells and compositions

- **Stoichiometric LiVO₂:** **10×10×2** supercell totaling **2400 atoms**.
- **Li-rich model:** **Li₁.₀₇₊ᵧV₀.₉₃O₂** with **y = 0.09** (**2454 atoms**) including **interstitial Li** placed on selected **tetrahedral** sites related to **transition-metal layers** (extract).

### MD checklist details (extract-backed)

- **Boundaries / periodicity:** **Bulk** **PBC** **supercells** for layered **LiVO₂** / **Li-rich** compositions (extract describes **10×10×2** construction for **2400 atoms**).
- **Temperature:** **MD** sampling spans **200–600 K** in **100 K** intervals with **1.1 ns** **NVT** production segments after **NPT** thermal expansion equilibration (extract).
- **Pressure:** **NPT** used during the thermal-expansion equilibration stage (extract), then **NVT** for production statistics.

## Findings

### Outcomes and mechanisms

**Stoichiometric LiVO₂** shows **no facile long-range Li⁺ migration** within **>1 ns** trajectories, consistent with **poor intercalation** kinetics in the model. **Li-rich** compositions enable **cooperative interstitial diffusion** along pathways involving **transition-metal-layer-related** sites, yielding **lower barriers** and **higher diffusivity** than the stoichiometric case—linking **excess Li** to improved **rate capability** in this **shell-model** picture.

### Comparisons

The study contrasts **stoichiometric** vs **Li-rich** **Li₁.₀₇₊ᵧV₀.₉₃O₂** models and relates simulated **transport** behavior to prior **intercalation** phenomenology for this family (introduction/extract).

### Sensitivity

**Temperature** sweeps (**200–600 K**) probe how **thermally activated** **Li⁺** **diffusion** differs between compositions in the **classical** model.

### Limitations and corpus honesty

**Classical shell** models omit explicit **redox**/**charge transfer**; cite **`papers/Others/LiVO2_PCCP_diffusion_sept14.pdf`** and **ESI Table S1** for parameters rather than relying on this summary for numerical **barriers** beyond the qualitative claims excerpted here.

## Limitations

**Classical** potentials omit **explicit charge transfer** and **interface** **electrolyte** complexity; **thin-film** vs **bulk** **electrode** morphologies may differ from periodic **bulk** cells. **Li-rich** **defect** arrangements explored here are **idealized** **supercell** constructs; **real** **electrodes** may exhibit **grain boundaries** and **surface** **reconstruction** not represented in these **MD** boxes. **PCCP** **communication** format emphasizes **transport** **mechanism**; consult **ESI** for any **additional** **structures** referenced in the **article**. **This wiki** does not reproduce **ESI** **tables** verbatim.

## Relevance to group

**Battery oxide anode** **transport** benchmark alongside **ReaxFF** **Li-ion** interface studies in the wiki. The **shell-model** **MD** approach differs from **reactive** **electrolyte** simulations but informs **composition-driven** **diffusivity** expectations for **layered oxides** used in **intercalation** discussions.

## Citations and evidence anchors

- https://doi.org/10.1039/C4CP01640H — PCCP **16**, 21114–21118; `papers/Others/LiVO2_PCCP_diffusion_sept14.pdf`; extract `normalized/extracts/2014panchmatia-physical-che-lithium-ion-diffusion_p1-2.txt`.

## Related topics

- [[batteries-interfaces-reaxff]]
