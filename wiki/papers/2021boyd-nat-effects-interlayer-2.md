---
id: paper:2021boyd-nat-effects-interlayer-2
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
  - keyword:galley-or-proof-pdf
  - keyword:monte-carlo-sampling
source_refs: []
doi: "10.1038/s41563-021-01066-4"
year: 2021
authors:
  - "Shelby Boyd, Karthik Ganeshan, Wan-Yu Tsai, Tao Wu, Saeed Saeed, De-en Jiang, Nina Balke, Adri C. T. van Duin, Veronica Augustyn"
venue: "Nature Materials (proof PDF in corpus)"
pdf_sha256: "63261e0229120bf409747cdaf7d982e374767575c148e6781e6be68c3ec0848f"
pdf_path: "papers/Boyd_birnessite_NatureMaterials_2021_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2021boyd-nat-effects-interlayer-2 -->

## Summary

This entry points to a **publisher galley / proof** PDF (`Boyd_birnessite_NatureMaterials_2021_galley.pdf`) for the **Nature Materials** article **DOI [10.1038/s41563-021-01066-4](https://doi.org/10.1038/s41563-021-01066-4)** on **birnessite** **capacitive charge storage** under **interlayer confinement** and **hydration**. The scientific account matches **`[[2021boyd-nat-effects-interlayer]]`**, which uses the non-galley PDF `Boyd_birnessite_NatureMaterials_2021.pdf`. The study combines **ex situ XRD**, **EQCM**, **in situ Raman**, **operando AFM dilatometry**, **DFT**, and **ReaxFF** **grand canonical Monte Carlo** and **molecular dynamics** to connect **interlayer spacing**, **mass transport**, and atomistic **K⁺** / **H₂O** pathways in **nanoconfined**, **hydrated** interlayers. **Cyclic voltammetry** in **neutral aqueous** electrolytes (e.g. **0.5 M K₂SO₄**) is compared to **non-aqueous** conditions with bulky cations to test **intercalation** versus **surface-only** charge storage. The combined data support **intercalation** in **hydrated** interlayers that can appear **capacitive** because **structural water** mediates **cation–MnO₂** interactions with limited **hysteresis**. Readers comparing this **galley** PDF to the **final** article should verify **figure** numbering, **supplementary** video references, and any **Mn oxidation** state assignments against the publisher **proof** corrections recorded in **`[[2021boyd-nat-effects-interlayer]]`**.

## Methods

This `pdf_path` is a **publisher** **proof**/**galley**; **for Methods detail and figure numbering aligned to the final issue**, read **`[[2021boyd-nat-effects-interlayer]]`** and the same **DOI** on the **publisher** site. Summaries here mirror that article at a high level.

### Experiments

**Electrodeposited** **birnessite** films; **CV** at controlled **sweep** **rates** in **aqueous** electrolytes (e.g. **0.5 M K₂SO₄**); **298 K** class **temperature**; **XRD** ( **(001)** **spacing** vs **potential** ); **EQCM**; **Raman** (**Mn–O**); **operando** **AFM** **dilatometry** for out-of-plane **height**.

### MD application (ReaxFF + intercalation sampling)

- **Engine / code:** ReaxFF-based **molecular dynamics** and **interlayer** **GCMC**/MD for **K⁺**+**H₂O**; exact executable naming **N/A**—treat the **VOR** **SI** + **`[[2021boyd-nat-effects-interlayer]]`** as the canonical **protocol** source, not this **galley** `pdf_path`.
- **System size & composition:** **Birnessite**-like **layered** **MnOₓ** **supercells** with explicit **K⁺** and **H₂O** in the **interlayer** gallery; **atom** counts and in-plane repeats are **N/A** on this **proof**-path page—use the **VOR** **SI** for the exact **stoichiometry** and **unit** **cell** vectors.
- **Boundaries / periodicity:** **PBC** in the **in-plane** **directions** of the **layered** **simulation** **cell** (see **VOR** **SI** for full **boundary** conditions and any **vacuum**/**electrolyte** padding).
- **Ensemble / thermostat / timestep / run length / interatomic cutoffs / QEq:** **NVT**-class **sampling** in **portions** of the workflow, but **N/A** here: copy **0.25 fs**-class **timestep** (if used), **equilibration**/**production** **ps**–**ns** **lengths**, **Langevin** (or other) **thermostat** labels, and any **NPT** vs **NVT** choices from the **VOR** `pdf_path`/**SI** rather than the **proof** file.

### Static DFT in this work

- **N/A** for full detail on this page—**interlayer** **K⁺**+**H₂O** **DFT** in the same study is summarized on **`[[2021boyd-nat-effects-interlayer]]`**.

## Findings

The **main** text supports **(near-)ideal** **pseudocapacitive** **CV** shapes together with **large** **gravimetric** **capacitance** and **(001)** **XRD** **moves** and **EQCM** **signatures** of **H₂O**+**K** **co-transport** in a **confined** **interlayer**—a **pseudocapacitor**-like look from **cyclic** kinetics. **ReaxFF**+**sampling** supports **H₂O**+**K⁺** **uptake** (supplementary **videos** on the VOR) compared with a simple **K⁺**-only **exchange** story. For **citable** **numbers** and **figure** labels, **avoid** the **proof** `pdf_path` for primary evidence—use the **version-of-record** and **`[[2021boyd-nat-effects-interlayer]]`**.

## Limitations

**Proof**/**galley** files can differ from the **final** **Nature Materials** layout. **Thin-film** morphology and **electrolyte** scope constrain generalization; **ReaxFF** simplifies **Mn** redox electronic structure. **EQCM** interpretation assumes known **solvent** incorporation stoichiometries; combined **XRD**/**Raman**/**AFM** constraints in the article are what tie mass signals to **intercalation** rather than adsorption-only pictures. This caveat applies equally to **galley** and **final** PDFs.

## Relevance to group

**Adri van Duin** co-authorship; **ReaxFF** **GCMC**/**MD** supports **intercalation** mechanisms for **birnessite** **supercapacitors**.

## Citations and evidence anchors

- DOI: [10.1038/s41563-021-01066-4](https://doi.org/10.1038/s41563-021-01066-4)

## Reader notes (navigation)

- Version-of-record PDF: [[2021boyd-nat-effects-interlayer]]

## Related topics

- [[2021boyd-nat-effects-interlayer]]
- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
