---
id: paper:2014sch-nfelder-chemical-phy-reactive-force
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
pdf_sha256: "8b385677de650b8d56f552b1af1a140d8ac1f990678ec7f8a45d03fd111252b7"
pdf_path: "papers/ReaxFF_others/Prehl_coworkers_JCP_accepted_2014.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014sch-nfelder-chemical-phy-reactive-force -->

!!! abstract "Twin polymerization motivates a new C/H/O/Si ReaxFF parametrization for an early electrophilic aromatic substitution step; existing hydrocarbon/CNT-oriented ReaxFF fits fail for this reaction despite shared elements, so a targeted reparameterization is developed and compared."

## Summary

**Twin polymerization** forms **organic and inorganic polymer domains** from a **single twin monomer** in one process; understanding the **initial electrophilic substitution** on an **aromatic** fragment is a key mechanistic step. This manuscript develops a **first-principles-guided ReaxFF** description for **C/H/O/Si** chemistry adequate to capture that **electrophilic aromatic substitution** event.

The authors report that **established ReaxFF parametrizations** aimed at **hydrocarbon** or **CNT-like** chemistry **do not reproduce** this specific reaction, even though elements overlap, motivating a **new parametrization** and explicit comparison to prior parameter sets.

## Methods

**Local sources:** the PDF at `papers/ReaxFF_others/Prehl_coworkers_JCP_accepted_2014.pdf` is present in this workspace; the accepted-manuscript opening is captured in `normalized/extracts/2014sch-nfelder-chemical-phy-reactive-force_p1-2.txt`. A typeset journal PDF is also ingested as [[2014sch-nfelder-chemical-phy-reactive-force-2]].

The authors implement **reactive MD with ReaxFF** for **C/H/O/Si**, targeting the **first C–C bond** between twin monomers by way of an **electrophilic aromatic substitution** step in **twin polymerization**. The mechanism follows Spange et al.: **acid-catalyzed O–CH\(_2\)** cleavage yields a **benzyl cation**, which forms a \(\pi\)-complex and then a \(\sigma\)-complex with a second monomer’s aromatic ring (Figures 1–3 in the article). For tractable **DFT** benchmarking and fitting, they introduce a reduced **benzene + benzyl cation** test system (Fig. 2) before transferring the validated **ReaxFF** parameter set to the **full twin monomer**. They compare **established ReaxFF parametrizations** aimed at **(hydro)carbon** and **CNT-like** chemistry against a **new parametrization** fit to reproduce the **aromatic substitution** energetics and pathways (Section 2 in the journal paper describes the **ReaxFF** energy expressions and fitting strategy; **DFT** reference data and parameter subsets are given there and in the Results).

### 1 — MD application (production trajectories)

This **Chemical Physics** contribution is centered on **QM-informed ReaxFF reparameterization** and comparative energetics/pathways for the **electrophilic substitution** motif. **System size / composition:** **DFT** and **ReaxFF** comparisons use a reduced **benzene + benzyl cation** **atom** motif (**Figure 2**) before transfer to the full **twin monomer**; any large-scale **reactive MD** **supercell** used for dynamics is **N/A —** not summarized on `normalized/extracts/2014sch-nfelder-chemical-phy-reactive-force_p1-2.txt`. **Boundary conditions:** **cluster**/**gas-phase** **training** setups are implied for the **QM** benchmarks, but explicit **PBC** text is **N/A —** confirm in **`pdf_path`**. **Temperature:** **N/A —** thermostat **K** targets for any illustrative **molecular dynamics** are not on the indexed excerpt. **Engine, timestep (fs), NVT/NPT ensemble, ns-scale equilibration:** **N/A —** read **`pdf_path`** if the article reports production **MD** beyond the parameterization narrative.

### 2 — Force-field training

**Parent FF / elements:** **ReaxFF** for **C/H/O/Si**, starting from literature **hydrocarbon**/**CNT-oriented** parameter sets that the authors show **fail** on the targeted **aromatic substitution** despite overlapping elements. **QM reference:** **DFT** on the reduced **benzene + benzyl cation** motif supplies **training** energies and pathway constraints (functional/basis/k-point specifics in **Section 2** of **`pdf_path`**). **Training set:** **reaction** coordinates and **σ/π-complex** intermediates along the Spange *et al.* mechanism (Figures 1–3). **Optimization:** **parameter fit** / **least-squares**-style **ReaxFF optimization** is described in the article’s **Methods** (see **`pdf_path`** for algorithmic detail). **External benchmarks:** side-by-side comparisons to prior **ReaxFF** sets on the same **reaction** targets.

## Findings

The abstract states that **existing parametrizations** that succeed for **hydrocarbon/CNT-like** chemistry **fail to reproduce** the specific **electrophilic substitution** targeted here **even though the elements overlap** and some mechanistic ingredients are shared. The manuscript therefore introduces a **new parametrization** that **does** reproduce the reaction “properly” (in the authors’ assessment) and uses side-by-side comparisons to **identify what differs** between parametrizations. The broader motivation is **twin polymerization**, where the **first C–C bond formation** between monomer units is treated as an essential step toward the **organic network**.

**Corpus honesty.** Accepted-manuscript ingest (`papers/ReaxFF_others/Prehl_coworkers_JCP_accepted_2014.pdf`); prefer **`[[2014sch-nfelder-chemical-phy-reactive-force-2]]`** for typeset pagination when citing figures.

## Limitations

- Accepted-manuscript PDF may differ slightly from final **Chemical Physics** formatting.
- Scope is tied to **twin polymerization** chemistry; broader organosilicon reactivity requires additional validation.

## Relevance to group

Clear **parameterization** case study illustrating **domain-of-validity** issues when reusing ReaxFF sets across reaction classes.

## Reader notes (navigation)

- Typeset article PDF: [[2014sch-nfelder-chemical-phy-reactive-force-2]].

## Citations and evidence anchors

- DOI: [10.1016/j.chemphys.2014.06.003](https://doi.org/10.1016/j.chemphys.2014.06.003)
