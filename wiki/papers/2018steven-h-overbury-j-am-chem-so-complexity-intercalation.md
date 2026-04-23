---
id: paper:2018steven-h-overbury-j-am-chem-so-complexity-intercalation
type: paper
title: 'Complexity of Intercalation in MXenes: Destabilization of Urea by Two-Dimensional
  Titanium Carbide'
updated: "2026-04-20"
confidence: high
canonical_tags:
- domain:2d-layered
- domain:batteries-electrochemistry
- domain:reactive-md
- method:reaxff
- scale:atomistic
- task:experiment-integrated
paper_keywords:
- keyword:2d-materials
- keyword:batteries-interfaces
- keyword:validation-experiment
- keyword:supporting-information
candidate_tags: []
source_refs: []
doi: 10.1021/jacs.8b05913
year: 2018
authors:
- Steven H. Overbury
- Alexander I. Kolesnikov
- Gilbert M. Brown
- Zhiyong Zhang
- Gokul S. Nair
- Robert L. Sacci
- Roghayyeh Lotfi
- Adri C. T. van Duin
- Michael Naguib
venue: J. Am. Chem. Soc.
pdf_sha256: c856548fa9bae52d7b229a05be9ec36cb9700d3cb022c4117ed67b6730cca00c
pdf_path: papers/Overbury_JACS_Complexity of Intercalation in MXenes_ Destabilization
  of Urea by Two-Dimensional titanium Carbide_accepted.pdf
extraction_quality: good
group_affiliation: true
---
<!-- id:paper:2018steven-h-overbury-j-am-chem-so-complexity-intercalation -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the JACS article identified by `doi`, `title`, and `pdf_path`. The corpus PDF is a **Just Accepted** manuscript; formatting may differ from the final issue.

## Summary

**Ti\(_3\)C\(_2\)T\(_z\)** MXene treated with **aqueous urea** is compared to reference solids using **inelastic neutron scattering (INS)** and **infrared** spectroscopy, alongside **Ti(urea)\(_6\)** complexes and **NH\(_4\)**-intercalated MXene prepared separately. The data support **urea decomposition** under intercalation-relevant conditions, with **ammonium** signatures in INS and **CO\(_2\)** evolution detected by IR, rather than persistence of intact urea between layers as often assumed from **c-axis** expansion alone. **Reactive MD (ReaxFF)** simulations (detailed in **Supporting Information**) provide atomistic reaction pathways and energetics consistent with the experimental observations. The central cautionary message is that **gallery expansion** after **urea** treatment is **not** sufficient evidence for **intact urea** intercalation—**vibrational** fingerprints and **gas-phase** products matter.

## Methods

- **Materials:** **HF-etched** Ti\(_3\)C\(_2\) MXene from **Ti\(_3\)AlC\(_2\)**, **urea-treated** MXene (e.g. **50 wt%** urea, **15 h**, **60 °C**), vacuum-dried variants; **NH\(_4\)HF\(_2\)**-etched **ammonium-intercalated** reference; **Ti(urea)\(_6\)I\(_3\)** complex synthesized for vibrational references.
- **Spectroscopy:** **INS** (ORNL; instrument details in SI) on dried samples; **IR** for gas-phase **CO\(_2\)** signatures during controlled treatments as described in the paper/SI.
- **Modeling:** **ReaxFF-based** reactive MD to explore **urea–MXene** reaction pathways and products; parameters and protocols in **Supporting Information** (per manuscript).

**Reactive MD (SI-first in this corpus).** The main text points to **Supporting Information** for **ReaxFF** parameters and simulation setup for **reactive molecular dynamics** of **urea** with **Ti\(_3\)C\(_2\)**-family **MXene** models. **Engine:** **ReaxFF MD** as implemented in the SI workflow (**N/A — whether LAMMPS vs another engine** is not stated in the p1–2 **Just Accepted** extract used here). **System / composition:** **MXene** **slab**/**supercell** models with intercalated **urea**-derived species as described in **SI** (**N/A — exact atom counts** should be copied from **SI** tables). **PBC:** **three-dimensional periodic** supercells assumed for the interlayer gallery models unless the **SI** specifies otherwise. **Ensemble / timestep / duration / thermostat / barostat:** **N/A — not recoverable** from the indexed p1–2 extract for this **Just Accepted** PDF; use the **Supporting Information** and final **JACS** issue **Methods** for **NVT**/**NPT** labels, **timestep**, **temperature** ramps, and **production** **lengths**. **External electric field in MD:** **N/A — not used** as a bias in the excerpted description. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not indicated in the indexed excerpt.
## Findings

- **INS** of urea-exposed MXene matches **ammonium**-containing references more closely than intact **urea** or the Ti–urea complex, supporting **decomposition** of urea and intercalation of **NH\(_4^+\)**-derived species rather than pristine urea as the primary intercalant.
- **IR** detects **CO\(_2\)**, consistent with **oxidative decomposition** of urea during treatment.
- **Reactive simulations** corroborate feasible **bond-breaking pathways** and energetics for urea destabilization at the MXene interface, motivating caution when inferring intercalant identity from **interlayer spacing** alone.
- Together, experiment and modeling argue that **urea-based** MXene processing recipes should be interpreted as **reactive infiltration** chemistry, not merely **physical intercalation** of a neutral molecule.

## Limitations

Just-Accepted PDF may differ slightly from the final edited article; INS/IR are bulk probes and may miss minority species. **Urea** chemistry is sensitive to **temperature**, **time**, and **residual** **HF**-etch **byproducts**; the experiments therefore should be read together with the **sample preparation** paragraphs when inferring **intercalant** speciation.

## Reader notes (navigation)

- **Just Accepted** manuscript PDF in corpus; confirm final pagination against the journal issue when available. **ReaxFF** details: Supporting Information (as cited in the article).

## Related topics

- [[reaxff-family]]
- [[theme-oxides-silica-ceramics]]
