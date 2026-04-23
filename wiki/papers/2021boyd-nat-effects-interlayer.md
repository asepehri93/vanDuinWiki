---
id: paper:2021boyd-nat-effects-interlayer
type: paper
title: "Effects of interlayer confinement and hydration on capacitive charge storage in birnessite"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - method:reaxff
  - method:dft-static
  - material:oxide
  - task:experiment-integrated
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:water-interfaces
  - keyword:monte-carlo-sampling
source_refs: []
doi: "10.1038/s41563-021-01066-4"
year: 2021
authors:
  - "Shelby Boyd, Karthik Ganeshan, Wan-Yu Tsai, Tao Wu, Saeed Saeed, De-en Jiang, Nina Balke, Adri C. T. van Duin, Veronica Augustyn"
venue: "Nature Materials"
pdf_sha256: "b1f48bd54cd5ddc14596b9ee362842aee1584bb2dba254d69085ef01f84461c7"
pdf_path: "papers/Boyd_birnessite_NatureMaterials_2021.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021boyd-nat-effects-interlayer -->

## Summary

The paper resolves how layered birnessite stores charge in neutral aqueous electrolytes by combining ex situ XRD, EQCM, in situ Raman, operando AFM dilatometry, DFT, and ReaxFF grand canonical Monte Carlo and molecular dynamics to connect interlayer expansion, mass transport, and atomistic intercalation pathways involving confined water and cations. The central narrative is that **apparently capacitive** voltammetry can coexist with **massive** **ion** and **water** reorganization in **confined** galleries—blurring the line between **EDLC**-like and **intercalation**-like storage in **layered oxides**.

## Methods

### Experiments (electrochemical, diffraction, gravimetry, imaging)

- **Electrodes and electrolyte:** **Electrodeposited** **birnessite** on conductive substrates, cycled in **aqueous** electrolytes (e.g. **0.5 M K₂SO₄** at **near-neutral pH** as in the main text) with **cyclic voltammetry** (CV) over controlled **sweep** **rates** at **298 K** (room-temperature class; see `pdf_path` for exact **thermal** protocol) (see `pdf_path` for exact **T** and **pH**); a **non-aqueous** electrolyte with **bulky tetrabutylammonium** is used as a **control** to disentangle **intercalation**-like **mass** changes from **EDL**-like response.
- **XRD / Raman / AFM:** **Ex situ XRD** tracks the **(001)** **interlayer** **d-spacing** vs **potential**; **Raman** follows **Mn–O** **phonon** bands; **operando AFM dilatometry** measures **out-of-plane** **height** changes in **electrolyte**.
- **EQCM:** **Gravimetric** **electrochemistry** maps **mass** **flux** to **charge**; **DFT**-informed **interpretation** in the **SI** (per the **Nature Materials** article) supports assigning **H₂O** and **K⁺** **stoichiometry** in the same **intercalation** picture the authors promote.

### MD application (ReaxFF + grand canonical sampling)

- **Engine / code:** ReaxFF-based **molecular dynamics** and **GCMC**-style intercalation sampling (as described in the **main** text and **supplementary** materials/videos) for **K⁺** and **H₂O** in the **MnOₓ** interlayer. **N/A**—whether the production code is **LAMMPS**-only vs a linked **PuReMD**/**ReaxFF** path: follow `pdf_path` and the **supplementary** protocol for exact executables and input decks.
- **System size & composition:** **Birnessite**-like **interlayer** models; **K⁺** and **H₂O** **insertion** from **dehydrated** and **partly hydrated** starting interlayers. Atom counts, **NₓNᵧ** in-plane repeats, and **H₂O****:****K** ratios **N/A**—copy from `pdf_path`/SI when reproducing trajectories.
- **Boundaries / periodicity:** **2D** **PBC** in the **a–b** **plane** of the **layered** model with vacuum or explicit **electrolyte** treatment as given in the **SI** (**N/A**—cell vectors not duplicated here).
- **Ensemble / control:** The MD segments follow **NVT**/**NVT**+**MC** **stages** reported in the article (the exact **NVT** vs **NVE** for short relaxations **N/A**—in **SI**). There is no macroscopic **continuum** **NPT** **barostat** on the *electrochemical* cell: **E**-field/ionic **double layer** in experiment is not represented as a classical **E-field** in every listed MD segment (**N/A**—treat the MD as a **chemical** **potential**/**grand-canonical** sampling complement to the **XRD** data).
- **Timestep / duration / thermostat:** `pdf_path` + **SI** give **femtosecond** **timestep**, **equilibration** and **production**-stage **MD** **lengths**, and **NVT**-compatible **thermostat** use where applicable. **N/A**—numeric values not duplicated in this **wiki** (copy from the **version-of-record** and **supplementary** videos). **N/A** for **replica** **exchange** and **metadynamics**-style **enhanced sampling** in the primary workflow.

### Static DFT in this work

- **DFT (when split out from ReaxFF):** **K⁺**/**H₂O**-dependent **interlayer** relaxations/energetics in **condensed** models as referenced (functional/basis: **N/A**—pulled in full in `pdf_path`/SI, not in this one-line note).

## Findings

**Pseudocapacitive** **CVs** and **anomalously** **high** **gravimetric** **capacitance** relative to **EDL** benchmarks: **K⁺**-based **XRD** **(001)** **peaks** **shift** reversibly with **potential**, and **EQCM** shows **H₂O**/cation **co-transport** (not a single **K⁺**-only **Faradaic** line). The combined **XRD**/**Raman**/**AFM**/**EQCM** package supports **co-intercalation** in **confined** **H₂O**-rich **interlayers** that still **appear** like **EDLC**-like kinetics. **ReaxFF**+**GCMC**/MD **movies** in the **supplementary** materials illustrate how **H₂O**+**K⁺** can enter the **interlayer** together rather than a pure **K⁺**-for-**H** exchange, tying **ion**+**water** reorganization to the **XRD** **(001)** **sweep** and the **AFM** **dilation** signal. For **citation**-ready **concentration** and **H₂O**/cation **number** assignments, use the `pdf_path` and **SI** tables/figures; this wiki is a **retrieval** summary, not a substitute for the full **data** product.

## Limitations

Thin-film morphology (island structures) and electrolyte scope (focus on neutral pH sulfate) limit direct transfer to all device configurations; force-field models simplify electronic transitions of Mn oxidation states. **Operando** **AFM** and **EQCM** coupling can also introduce **instrument**-specific **artifacts** that must be separated from **intrinsic** **intercalation** **mass** changes when interpreting **gravimetric** **capacitance**. **ReaxFF** **GCMC/MD** provides **atomistic** **hypotheses** for **ion** and **water** **uptake** that should be cross-checked against **crystallography** and **spectroscopy** constraints from the **same** **electrode** **films**. **Nature Materials** **supplementary** videos illustrate **intercalation** **pathways** that are easier to **qualify** than to **reduce** to a single **order** **parameter**.

## Relevance to group

Adri van Duin is a co-author; ReaxFF GCMC/MD supports intercalation mechanisms for birnessite supercapacitors.

## Citations and evidence anchors

- DOI: [10.1038/s41563-021-01066-4](https://doi.org/10.1038/s41563-021-01066-4) — main text and supplementary videos for **GCMC/MD** setup.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
