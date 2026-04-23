---
id: paper:2022campbell-venue-manuscript
type: paper
title: "Effect of Nitrogen Doping and Oxidation of Graphene on the Deposition of Platinum from Trimethyl(methylcyclopentadienyl)platinum(IV)"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - material:graphene-carbon-nano
  - method:dft-static
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:graphene-carbon
  - keyword:dft-static
  - keyword:neb
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.2c04117"
year: 2022
authors:
  - "Ian E. Campbell"
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Suzanne E. Mohney"
venue: "J. Phys. Chem. C"
pdf_sha256: "254ae37994e123eaf5facb6de60264e5d1a52c47df9262c2606212f3ccd29c9e"
pdf_path: "papers/Campbell_Pt_graphene_JPC_2022_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2022campbell-venue-manuscript -->

## Summary

Density functional theory examines how nitrogen doping and vacancy oxidation of graphene influence adsorption and stepwise demethylation of the Pt ALD precursor MeCpPtMe\(_3\), a common vapor-phase platinum source. Pyridinic nitrogen substitutions lengthen substrate–oxygen bonds at oxidized monovacancies, strengthening precursor–surface coupling, while nudged elastic band calculations compare reaction and activation enthalpies for methyl loss pathways on doped and undoped oxidized surfaces. **Pt** **ALD** on **carbon** **supports** underpins **electrocatalysis** **electrodes**; **defect** **and** **N** **dopant** **patterns** control **nucleation** **density**, so **DFT** **surfaces** here map **precursor** **binding** to **likely** **island** **formation** **sites**.

## Methods

**Canonical curation (same work):** **`[[2022ian-e-campbell-j-phys-chem-effect-nitrogen]]`**. The corpus **`pdf_path`** is a **galley**-style *J. Phys. Chem. C* PDF—**pagination** and **table** **labels** should be checked against the **VOR** at the DOI.

**1 — MD application (atomistic dynamics).** **N/A** — no **production** **MD** **trajectories** are central to the published study; it is a **0 K** **DFT** + **NEB** **survey** of **MeCpPtMe\(_3\)** on **defect** **graphene**.

**2 — Force-field training.** **N/A**.

**3 — Static QM / DFT.** **Program: Quantum ESPRESSO**-style **planewave** **PBE**-class **DFT** (see **convergence**: **ecutwfc**, **charge** **density** **cutoff**, a plain-text **k-mesh** / **k-point** mesh per **slab** class, and **Fermi** **smearing** in the **article**), with **PBE**+**D3**-or-equivalent **dispersion** and **ultrasoft**/**PAW** **pseudopotentials** as **specified** in *J. Phys. Chem. C* (rely on the **VOR** **not** the galley for **final** **value**s). **Structures** include **pristine** **graphene**, **monovacancy (MV)**, **MV+2O**, **MV+3O** **oxides**, and **pyridinic** **N**-substituted **lattices** (e.g. **N@C1**, **N@C5**, **N@C13** in the **paper**’s **nomenclature**). **Property** work includes **MeCpPtMe\(_3\)** **adsorption** **energies** in **several** **adsorption** **poses**, and **NEB** **reaction** **pathways** for **methyl** **cleavage** and **trapping** to **bridge** / **in-plane** **O**; **Bader**/**difference**-**density** **style** **plots** in the **PDF** **illustrate** **charge** **reorganization**. **Dipole**-**corrected** **slab** **vacuums** are **as** **documented** in the **Supplementary/Methods** when present.

**4 — Experiments.** **N/A** — the paper is **computation**-**forward**; **Pt** **ALD** **serves** as **context** in the **introduction**/**discussion**.

## Findings

**Outcomes and mechanisms.** **O** **addition** at the **monovacancy** is **favorable** **thermochemically** in the **defect** **scenarios** the authors **treat**; **pyridinic** **N** at **the** **sites** **modeled** **lengthens** **C–O** **bonds** at **vacancy** **oxides** relative to the **N**-**free** **analogs**, and **tightens** **MeCpPtMe\(_3\)** **adsorption** **trends** the authors use to **discuss** **nucleation** **favorability**. **NEB**-based **reaction** and **activation** **enthalpies** for the **first** **demethylation** stay **endothermic** on the **oxidized** **graphenes** **sampled** in the **study**, yet **pyridinic** **N** can **lower** both **reaction** **endothermicity** and the **cited** **barrier** for the **first** **step** and **reorder** **exothermicity** of **subsequent** **CH\(_3\)** **sticking** vs **detachment** in **multi-**O **vacancy** **geometries**—in **some** **paths** a **net** **exothermic** **multistep** **sequence** from **precursor** to **O**-**saturated** **defects** is **reached** for **N**-**doped** **lattices**, which they **relate** to **enhanced** **Pt** **ALD** **nucleation** on **N**-**riched** **carbon**.

**Comparisons.** **Doped** **vs** **undoped** **defects**, O-poor vs O-rich **vacancy** **motifs**, and **multiple** **N**-**neighborhoods** (see the **VOR** **tables** for **concrete** **\(\Delta E\)** and **barrier** data); **N**-**doping** is **not** reduced to **Lewis**-**base**-only **effects**—it **restructures** **oxide** **local** **strain** and **electronic** **localization** at the **defects**.

**Sensitivity and levers.** **N** **location** in the **supercell** and **O** **coverage** at the **monovacancy** are the main **chemical** **knobs** **swept** in the **DFT** **sweep**.

**Corpus / KB honesty.** Reproduce **eV** **energies** and **barrier** **heights** from the **version-of-record**; the **corpus** **galley** **file** is for **manifest** **fingerprint** **only** when it **differs** from **VOR** **typography**—see **`## Limitations`**.
## Limitations

Static 0 K DFT omits entropic and coverage effects of real ALD cycles; model vacancy/oxide motifs simplify actual N-doped carbon supports. **Galley** PDF in corpus may differ slightly from **pagination** and **figure** **labels** in the **version of record** at **DOI** **10.1021/acs.jpcc.2c04117**. **Coverage**-dependent **precursor** **competition** and **chlorine** **surface** **species** from **Pt** **chemistry** are simplified in the **static** **slab** **survey**.

## Relevance to group

Penn State collaboration with van Duin on organometallic adsorption at functionalized graphene for catalysis and ALD initiation.

## Citations and evidence anchors

<!-- Prefer DOI link when `doi` is present in frontmatter. -->

## Related topics

- [[reaxff-family]]
- Optional: [[batteries-interfaces-reaxff]], [[graphene-nanocarbon]] where relevant after curation.
