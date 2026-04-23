---
id: paper:2014sch-nfelder-chemical-phy-reactive-force-2
type: paper
title: "Reactive force field for electrophilic substitution at an aromatic system in twin polymerization"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:polymer
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.chemphys.2014.06.003"
year: 2014
authors:
  - "Thomas Schönfelder"
  - "Joachim Friedrich"
  - "Janett Prehl"
  - "Steffen Seeger"
  - "Stefan Spange"
  - "Karl Heinz Hoffmann"
venue: "Chemical Physics"
pdf_sha256: "6d6eecdee2bf1c112819321a13bff1a3e87561b84348448fe12b667ceb5b51bc"
pdf_path: "papers/ReaxFF_others/Schonfelder_ChemPhys2014_TwinPolymer.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014sch-nfelder-chemical-phy-reactive-force-2 -->

!!! abstract "Journal-formatted PDF for the Chemical Physics article developing a C/H/O/Si ReaxFF parametrization for an electrophilic aromatic substitution step central to twin polymerization, contrasting older parametrizations that fail on this reaction."

## Summary

This entry is the **typeset Chemical Physics** PDF for the article also summarized under [[2014sch-nfelder-chemical-phy-reactive-force]]. The scientific content is the **ReaxFF reparameterization** for an **electrophilic substitution** on an **aromatic** subunit within **twin polymerization** chemistry, with explicit comparison showing that several **prior ReaxFF parametrizations** (developed for hydrocarbon/CNT-like settings) **do not transfer** to this reaction class despite sharing elements.

## Methods

### Corpus PDF role (typeset journal layout)

- Local PDF: `papers/ReaxFF_others/Schonfelder_ChemPhys2014_TwinPolymer.pdf`; extract: `normalized/extracts/2014sch-nfelder-chemical-phy-reactive-force-2_p1-2.txt` (overlaps accepted-manuscript extract for the same DOI).

### Scientific protocol (same as sibling page)

- **DFT-informed ReaxFF** reparameterization for **C/H/O/Si** targeting **electrophilic aromatic substitution** that creates the **first C–C bond** in **twin polymerization**, with **benzene + benzyl cation** training/validation motifs before transfer to the full **twin monomer** (**Sections 2–3**, **`[[2014sch-nfelder-chemical-phy-reactive-force]]`**).

### Mechanistic target (twin polymerization)

- The authors follow the **acid-catalyzed** route described by **Spange *et al.*** where **O–CH\(_2\)** cleavage yields a **benzyl cation**, followed by **π-complex** and **σ-complex** formation on a second aromatic ring (**article** Figures 1–3; see **`[[2014sch-nfelder-chemical-phy-reactive-force]]`** for full narrative).

### QM benchmarks and fitting strategy

- **DFT** reference data for the reduced **benzene + benzyl cation** motif underpin the **ReaxFF** refit; the manuscript compares **legacy** **hydrocarbon/CNT-oriented** **ReaxFF** sets against the **new** parametrization on the same reaction targets (**article** Section 2).

### Citation guidance

- Prefer this **typeset** PDF for **final** **equation**, **figure**, and **page** numbers versus the accepted-manuscript ingest.

### 1 — MD application

Same **Chemical Physics** article as **`[[2014sch-nfelder-chemical-phy-reactive-force]]`**: **QM-informed ReaxFF reparameterization** for an **electrophilic substitution** motif. **System size / composition:** reduced **benzene + benzyl cation** **atom** motif (**Figure 2**) before transfer to the full **twin monomer**; large-scale **reactive MD supercells** — **N/A —** not excerpted on `normalized/extracts/2014sch-nfelder-chemical-phy-reactive-force-2_p1-2.txt`. **Boundary conditions:** **cluster**/**gas-phase** **training** is implied; explicit **PBC** wording — **N/A —** confirm in **`pdf_path`**. **Temperature:** **N/A —** thermostat **K** targets not on indexed pages. **Engine, timestep (fs), NVT/NPT, ns equilibration, thermostat:** **N/A —** duplicate-byte note only—use **`[[2014sch-nfelder-chemical-phy-reactive-force]]`** or this **typeset** **`pdf_path`** for any reported **molecular dynamics** production details.

### 2 — Force-field training

Same **ReaxFF** **reparameterization** story as **`[[2014sch-nfelder-chemical-phy-reactive-force]]`**: **C/H/O/Si** coverage, **DFT** on **benzene + benzyl cation**, **training** data for **electrophilic aromatic substitution**, **optimization** of **ReaxFF** parameters, and **benchmark** comparisons against legacy **hydrocarbon/CNT** sets.

## Findings

As in the accepted-manuscript entry, the article’s core result is that **transferable** “general organic” **ReaxFF** parametrizations can **fail** for this **aromatic substitution** despite shared elements, necessitating a **reoptimized** parameter set. The **typeset** PDF should be preferred for **pagination**, **figure**, and **equation** numbering when citing specific validation details. **Twin polymerization** couples **sol–gel** and **polymer** formation from a single **monomer**, so an accurate **electrophilic** **first C–C** bond is a **gating** step for **both** networks; mis-modeled **aromatic** **attack** therefore corrupts **macroscopic** **kinetics** even when **aliphatic** **ReaxFF** terms are well fit.

**Comparisons / limitations.** Head-to-head **QM**/**ReaxFF** comparisons on the same **reaction** targets motivate the refit; **future work** must still **validate** **condensed-phase** and substituted-arene **transferability** using the full **Chemical Physics** discussion.

## Limitations

None beyond the primary entry; this path is preferred for **publisher layout** and stable figure numbering.

When porting the **twin-polymerization** parameter set to **other** **aromatic** **electrophiles**, repeat **QM** **spot** **checks** on **barrier** **heights**—**transferability** across **substituted** **arenes** is **not** **automatic** even after this **reoptimization**.

**Condensed-phase** **solvation** and **counter-ion** **pairing** around **benzyl** **cation** **motifs** in **real** **twin** **monomers** may require **explicit** **solvent** **ReaxFF** **tests** beyond **gas-phase** **training** **geometries**.

**Residual** **silicon** **byproducts** from **sol–gel** **branches** can introduce **additional** **reaction** **classes** not covered by **benzene** **+** **benzyl** **cation** **training** alone.

## Relevance to group

Same as the accepted-manuscript entry: a **parameterization** lesson in **reaction-specific** ReaxFF scope.

## Reader notes (navigation)

- Accepted-manuscript ingest: [[2014sch-nfelder-chemical-phy-reactive-force]].

## Citations and evidence anchors

- DOI: [10.1016/j.chemphys.2014.06.003](https://doi.org/10.1016/j.chemphys.2014.06.003)
