---
id: paper:2022ian-e-campbell-j-phys-chem-effect-nitrogen
type: paper
title: "Effect of Nitrogen Doping and Oxidation of Graphene on the Deposition of Platinum from Trimethyl(methylcyclopentadienyl)platinum(IV)"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - method:dft-static
  - task:application
  - material:graphene-carbon-nano
  - material:metal-surface
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:dft-static
  - keyword:neb
  - keyword:graphene-carbon
  - keyword:catalysis-surface
source_refs: []
doi: "10.1021/acs.jpcc.2c04117"
year: 2022
authors:
  - "Ian E. Campbell"
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Suzanne E. Mohney"
venue: "J. Phys. Chem. C"
pdf_sha256: "14ac77cad0c6227abfcc0900e6f12ee791a82204adbe81296b52b078b324cc24"
pdf_path: "papers/Campbell_Pt_graphene_JPC_2022.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022ian-e-campbell-j-phys-chem-effect-nitrogen -->

## Summary

**Density functional theory** evaluates how **N doping** and **oxidation** of **graphene** (via **vacancy oxidation**) affect vapor-phase **trimethyl(methylcyclopentadienyl)platinum(IV)** (**MeCpPtMe\(_3\)**) **adsorption** and **dissociation** relevant to **atomic layer deposition (ALD)** of **Pt** on **defective** **carbon** supports. **Oxygen incorporation** at **monovacancies** is favorable **with and without** **N** dopants, establishing **oxidized** **defect** sites as **thermodynamically** preferred anchors for **O**. **N doping** **elongates** **substrate–oxygen** bonds, which the authors connect to **stronger** **precursor–substrate** interaction on **oxidized** **defective** graphene. **Nudged elastic band (NEB)** calculations report **positive** reaction and **activation** **enthalpies** for elementary **MeCpPtMe\(_3\)** dissociation steps on the **oxidized** substrates studied, yet **N doping** lowers both **activation** and **reaction** **enthalpies** along the sequence and makes **chemisorbed** **MeCpPtMe\(_2\)** more favorable. For **pyridinic-N**-containing models, the **overall** transformation from **MeCpPtMe\(_3\)** plus **two oxidized monovacancies** to **MeCpPtMe\(_2\)** plus **methyl** groups bound at those vacancies is **exothermic** (abstract).

## Methods

### A — Density functional theory (periodic slabs)

- **Quantum ESPRESSO** (**PWscf**) **DFT** with **dispersion** and **k**-mesh per article; **graphene** supercells with **vacancies**, **oxygenated** defects (**epoxide**/**hydroxyl** patterns), and **pyridinic** / **graphitic** **N** substitutions.

### B — Nudged elastic band (NEB)

- **NEB** paths for **MeCpPtMe\(_3\)** **dissociation** and **methyl** transfer to **surface O** sites—**ALD**-relevant coordinates.

### C — Analysis

- **Reaction** and **activation** **enthalpies**; **C–O** bond lengths vs **N** **doping**; compare **N**-free vs **N**-doped **oxidized** **vacancy** models.

### D — Experiments

- None; static **0 K** **enthalpy** survey for **ALD** precursor–substrate chemistry.

**Static QM (DFT-only) spine:** **Program:** **Quantum** **ESPRESSO** **PWscf**. **Functional / dispersion:** **PBE**-family **DFT** with **dispersion** **corrections** and **Monkhorst–Pack** k-mesh / Γ-centered Brillouin sampling as in *J. Phys. Chem. C* **Methods** (k-point density tabulated in the **PDF**). **Basis:** **plane-wave** **PAW**/**pseudopotential** **treatment**. **Structures / pathways:** periodic **graphene** **slabs** with **vacancies**, **O-functionalized** **defects**, and **pyridinic**/**graphitic** **N**; **NEB** **reaction** **paths** for **MeCpPtMe\(_3\)** **elementary** **steps**. **Properties compared:** **0** **K** **reaction** and **activation** **enthalpies**, **barrier** **heights** along **NEB**, **bond** **lengths**—full **convergence** **settings** in the **PDF**.

## Findings

- **Oxidized vacancies** are stabilized by **O incorporation**; **N** dopants alter **substrate–O** bonding distances and strengthen **MeCpPtMe\(_3\)** coupling to **oxidized** defects relative to selected reference models.
- **NEB:** elementary steps can remain **barrier-limited** with **positive** **enthalpies**, but **N doping** reduces **activation** and **reaction** **enthalpies** for key **precursor** steps and favors **MeCpPtMe\(_2\)** formation on the **oxidized** **defective** surfaces examined.
- For **pyridinic-N**-containing models, the **net** reaction described in the abstract is **exothermic**, whereas **graphitic-N** and **N**-free cases show different **thermodynamic** favorability (see article for site-by-site comparison). **Comparisons / sensitivity:** **site**-by-**site** **N** **coordination** and **defect** **oxidation** **pattern** change **barrier** and **driving** **force** **trends**; **experimental** **ALD** not in this **DFT** **paper**. **Limitations / outlook:** **0** **K** **static** **picture**; **finite-temperature** and **solvent** **omitted**—see **authored** **caveats** in the **full** text. **Corpus / KB:** **enthalpy** **values** and **NEB** **images** must be **taken** from the **version-of-record** **PDF**/**SI**, not this **summary** alone.


## Limitations

**Periodic** **DFT** omits **explicit solvent** and **finite-temperature** **entropic** contributions important for **ALD** **partial pressures**; **experimental** **ALD** windows require validation beyond **0 K** **enthalpy** trends alone. **Dispersion** **correction** choices and **supercell** sizes follow the **J. Phys. Chem. C** computational section.

## Relevance to group

**van Duin** co-authorship connects to broader **catalytic carbon** / **ALD** interface work; methodologically this entry is **DFT + NEB**, not ReaxFF.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.2c04117](https://doi.org/10.1021/acs.jpcc.2c04117)

## Related topics

- [[graphene-nanocarbon]]

## Reader notes (navigation)

For **ALD** **process** **windows**, pair this **DFT**/**NEB** page with **experimental** **deposition** papers: the **J. Phys. Chem. C** study supplies **0 K** **enthalpy** trends on **defective** **graphene**, not **finite-pressure** **precursor** **fluxes** or **surface** **coverage** **kinetics** measured in **reactors**.
