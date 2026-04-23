---
id: paper:2014rossi-2014-doi-10-reduced-yield
type: paper
title: "Reduced yield stress for zirconium exposed to iodine: reactive force field simulation"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reactive-md
  - method:reaxff
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:lammps
  - keyword:qm-training-data
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1186/s40323-014-0019-z"
year: 2014
authors:
  - "Matthew L. Rossi"
  - "Christopher D. Taylor"
  - "Adri C. T. van Duin"
venue: "Advanced Modeling and Simulation in Engineering Sciences"
pdf_sha256: "114c8863ad2becf7f29cdfb2da1142de49a7d73ecf32ecb1cd35f0a3ecc5fb68"
pdf_path: "papers/Rossi_AdvModSimEng_2014_ZrI.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2014rossi-2014-doi-10-reduced-yield -->

!!! abstract "A Zr–I ReaxFF parameterization is used in MD to connect iodine surface coverage to reduced yield stress for a high-energy grain boundary, supporting an adsorption-enhanced decohesion picture relevant to iodine stress-corrosion cracking in zirconium cladding."

## Summary

**Iodine-induced stress-corrosion cracking (ISCC)** is a known concern for **zirconium alloy nuclear fuel cladding** when **iodine** (a fission product) reaches the **inner clad surface** and interacts with the metal under stress. This letter develops a **ReaxFF parameterization** compatible with **Zr–I** chemistry and applies it to simulate how **iodine exposure** affects **mechanical strength** at a **high-energy grain boundary**, using **yield stress** as a practical stress metric in the model setup described.

The authors report that **resistance to stress** decreases with increasing **iodine surface coverage**, supporting an **adsorption-enhanced decohesion** interpretation consistent with the framing of ISCC in the abstract.

## Methods

**Local sources:** the PDF at `papers/Rossi_AdvModSimEng_2014_ZrI.pdf` is present in this workspace; `normalized/extracts/2014rossi-2014-doi-10-reduced-yield_p1-2.txt` covers only the opening pages—the full **Methods** narrative below follows the **published letter** (LAMMPS ReaxFF-MD protocol, bicrystal geometry, iodine loading, and strain–stress workflow).

### 1 — MD application (ReaxFF in LAMMPS)

**Reactive MD** is run in **LAMMPS** using the **ReaxFF** implementation described by Chenoweth, van Duin, and Goddard (cited in the paper), with the **Zr–I** parameterization summarized under **Force-field training** below. To focus on **intergranular** ISCC, the authors study a **tilt grain boundary** intersecting the **Zr(0001)** surface: **unrelaxed grain-boundary energies** vs. tilt angle \(\theta\) about **[0001]** are scanned in **ReaxFF**, and a **15°** tilt is chosen as a **high-energy** boundary expected to be most vulnerable to iodine interaction. Each production setup uses **31,500 Zr atoms** in two **20-layer** single-crystal slabs separated by the grain boundary, with **iodine** introduced into the **vacuum** between periodic **Zr(0001)** slabs. After **energy minimization**, the cell is **equilibrated at 500 °C and 0 MPa in-plane** to the bicrystal supercell; **MD** uses a **10 fs** timestep. **Temperature:** **773 K** (**500 °C**) for equilibration and the **1 ns** tensile deformation stage. **Thermostat:** **N/A —** explicit algorithm (Berendsen, Nosé–Hoover, etc.) not restated in this wiki summary—see **`pdf_path`** Methods. **Atomic iodine** is placed in the vapor region (radiolytic-release idealization); the **effective iodine partial pressure** is inferred from the equilibrium cell volume and iodine count (**0–12 MPa** bracketing **pellet-gap** fission-gas conditions). **Uniaxial strain** is applied **perpendicular to the grain boundary** at **\(10^8\,\mathrm{s}^{-1}\)** (**10%** strain over **1 ns**), at **constant 500 °C**, with **stress** computed and normalized to the slab cross section every **50** steps to build **stress–strain** curves vs. iodine exposure. **Yield** is identified near **\(\sim\)4%** strain (Figure 4 in the article); **Additional file 1** tabulates raw stress–strain data. **Replica / enhanced sampling / electric field:** **N/A —** not used. **Barostat:** in-plane **0 MPa** equilibration is followed by **NVT**-style **constant-volume** **deformation** reporting (see article for how lateral **stress** is handled during uniaxial strain); **NPT** during the mechanical test — **N/A —** confirm wording in **`pdf_path`**.

### 2 — Force-field training

The **Zr–I** extension builds on prior **molecular and solid-state DFT** models of **Zr–I** aggregation and related states (article refs. [22–24]); **parent** parameters are the broader **ReaxFF** framework with **element** coverage extended for **Zr–I** chemistry. **QM reference data** feed the **training**/**bond-order** refinements (see letter). **Training set / optimization:** the communication points to those **QM** references rather than reprinting every **training** geometry here—**full training tables:** **`pdf_path`** + SI. **External validation:** **stress–strain** responses are compared against the **iodine-free** baseline and **iodine-loaded** cases in the model; **experimental** PCI details are discussed qualitatively in framing.

## Findings

The letter reports that the **maximum yield stress** of the **15° high-energy grain boundary** **falls as iodine exposure increases**. **Relative yield stress** drops sharply at low iodine pressure (up to **\(\sim\)20%** of the iodine-free yield by **\(\sim\)0.5 MPa**), then more gradually, reaching up to **\(\sim\)80%** reduction at **\(\sim\)11 MPa** when pressure is used as the control variable. At low pressure, iodine is largely **chemisorbed** (with **I\(_2\)** dissociation treated as barrierless on Zr in the discussion), so the authors replot **yield stress vs. chemisorbed iodine coverage** (iodine atoms per surface Zr) and find an approximately **linear** weakening—supporting **adsorption-enhanced decohesion** tied to **zirconium iodide** surface film formation rather than bulk grain-boundary iodine loading. **Trajectory inspection** near yield shows **crack initiation** where the **grain boundary meets the free surface**, with ingress of iodine at the yield point; at higher pressure a **surface phase transformation** (intermingled Zr and I) adds driving force for opening. The authors summarize that **chemisorption-mediated** iodide films **reduce** the stress needed to initiate failure at the **GB–surface** junction, consistent with an **ISCC** framing.

## Limitations

- A single **boundary geometry** and simplified environmental chemistry do not exhaust real **PCI** conditions (other halides/irradiation effects).
- Classical reactive FF cannot capture full **electronic-structure** details of bond rupture under all conditions.

## Relevance to group

Demonstrates **ReaxFF** applied to **nuclear materials** degradation pathways with **van Duin coauthorship**.

## Citations and evidence anchors

- DOI: [10.1186/s40323-014-0019-z](https://doi.org/10.1186/s40323-014-0019-z)
