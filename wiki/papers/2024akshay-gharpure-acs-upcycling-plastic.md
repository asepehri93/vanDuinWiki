---
id: paper:2024akshay-gharpure-acs-upcycling-plastic
type: paper
title: "Upcycling plastic waste into graphite using graphenic additives for energy storage: yield, graphitic quality, and interaction mechanisms via experimentation and molecular dynamics"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:organics-polymers-pyrolysis
  - method:reaxff
  - task:experiment-integrated
  - domain:batteries-electrochemistry
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:polymer
  - keyword:graphene-carbon
  - keyword:batteries-interfaces
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1021/acssuschemeng.3c07783"
year: 2024
authors:
  - "Akshay Gharpure"
  - "Malgorzata Kowalik"
  - "Randy L. Vander Wal"
  - "Adri C. T. van Duin"
venue: "ACS Sustainable Chem. Eng."
pdf_sha256: "8563d7255c1dcabe63fee8c51db24da1f7f0d7e45551ea594c0896c00ecaf689"
pdf_path: "papers/Gharpure_Kowalik_ACS_SusChemEng_Upcycling_Plastic_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024akshay-gharpure-acs-upcycling-plastic -->

## Summary

Upcycling plastic waste into battery-grade carbon addresses both environmental plastic accumulation and demand for synthetic graphite anodes, but process yields and microstructure depend on poorly understood interactions between molten polymers and catalytic carbon additives during pyrolysis. The introduction frames a broader materials context: graphite remains the dominant lithium-ion anode material, and projected battery manufacturing capacity has been argued to stress flake-graphite supply chains, while high-purity synthetic graphite can carry a substantial per-ton cost premium. Against that backdrop, diverting mixed plastic streams toward uniform graphitic carbon phases could, in principle, reduce landfill burden and diversify carbon feedstocks for electrochemical applications. This *ACS Sustainable Chemistry & Engineering* article reports sealed-tube carbonization of mixed post-consumer plastics—including reprocessed polypropylene, high-density polyethylene in multiple recycled forms, polystyrene foam, and polyethylene terephthalate bottles—followed by high-temperature graphitization at 2500 °C. Graphene oxide and related graphenic additives are shown experimentally to accelerate carbonization and boost elemental carbon yields, with thermogravimetric and differential scanning calorimetry tracing how polymer–GO mixtures devolatilize differently from neat polymers. Five additive grades are used to probe how graphenic chemistry couples to polymer decomposition during pyrolysis. ReaxFF reactive molecular dynamics supplies atomistic narratives for chemical coupling between polymer chains and oxidized graphene during heat-up, complementing microscopy and spectroscopy of the recovered solids. Adri C. T. van Duin is a coauthor, tying the work to the group’s reactive modeling of polymer and carbon chemistry.

## Methods

### Pyrolysis, graphitization, and characterization (experiment)

**Sealed-tube** carbonization of **mixed post-consumer plastics**; **2500 °C** graphitization; **XRD** crystallinity, **TEM** microstructure, **Raman** **sp²** vs **anthracene-coke**-like references; **TGA/DSC** on **polymer–GO** vs controls (**five** **GO** grades).

### ReaxFF reactive MD (B)

**LAMMPS** **ReaxFF** on **polymer–GO** contacts during heat-up—**bond-breaking** and **O-mediated** coupling; **supercell** sizes, **ramps**, **ensembles** in article/**SI**.

**MD application (ReaxFF heat-up).** **LAMMPS** runs use **ReaxFF** for **reactive** trajectories of **polymer** chains against **graphene**/**GO**-like **substrates**; **atom** counts, **PBC** **slab**/**supercell** design, and **NVT**/**NPT** choice (usually **NVT** during rapid **heating** for pyrolysis-coupling narratives) are in the **primary** paper. **N/A**—this wiki does not copy **time step** (fs), **equilibration**/**production** (ps/**ns**), **Nosé–Hoover**/**Berendsen** **thermostat** and damping, or **NPT** **Parrinello–Rahman**/**Berendsen** **barostat** if used—import from the **version-of-record**. **Temperature** programs follow the **TGA**-linked **ramp** logic in the **Methods**. **N/A**—**external electric field**; **N/A**—**metadynamics**; **N/A**—**hydrostatic** **pressure** in typical **NVT** heat-up unless **NPT** is specified.

## Findings

The abstract reports that graphene oxide can increase elemental carbon yield from recycled plastics by up to roughly 250% relative to additive-free processing under their conditions. Graphitized products exhibit crystallite sizes and Raman signatures competitive with reference coke-derived graphites, with thin lamellar morphologies argued to be favorable for lithium-ion anodes. Reactive trajectories support chemical interaction mechanisms—rather than purely physical templating—that rationalize how graphenic additives assist carbonization and subsequent graphitization.

**Comparisons, sensitivity, corpus note.** The study **compares** **TGA**/**DSC**, **Raman**/**XRD**/**TEM** metrics, and **simulation**-derived **interaction** pictures; **sensitivity** to **additive** grade, **heating** **rate**, and **polymer** **mix** composition is in the main text. **No** **galley** caveat applies to this **ACS**—use **`pdf_path`** and **DOI** for final numbers.

## Limitations

Absolute yields, reactor volumes, and MD ensemble sizes must be taken from the primary tables; reactive force fields may omit heteroatom chemistry present in real waste plastics beyond the modeled subsets.

## Relevance to group

The paper couples ReaxFF with sustainable carbon synthesis and battery materials, a high-priority theme for retrieval around pyrolysis, graphene oxides, and anode engineering.

## MAS / retrieval notes

Chunking should preserve quantitative yield claims with units as printed in the abstract (~250% increase stated there) and tie simulations to `papers/Gharpure_Kowalik_ACS_SusChemEng_Upcycling_Plastic_2024.pdf`. Flag `keyword:polymer` and `keyword:batteries-interfaces` together when routing sustainability+battery questions.

## Citations and evidence anchors

- DOI: `10.1021/acssuschemeng.3c07783`

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
