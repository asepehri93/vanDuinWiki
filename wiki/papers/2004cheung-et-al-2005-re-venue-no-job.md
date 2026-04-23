---
id: paper:2004cheung-et-al-2005-re-venue-no-job
type: paper
title: "ReaxFFMgH: reactive force field for magnesium hydride systems"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:reaxff-lineage
  - domain:batteries-electrochemistry
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: ""
year: 2004
authors:
  - "Sam Cheung"
  - "Wei-Qiao Deng"
  - "Adri C. T. van Duin"
  - "William A. Goddard III"
venue: "Caltech MSC (manuscript; see PDF for venue details)"
pdf_sha256: "3a215a3e28efbb9c5f592e70953e52fa04af6c16fda3e68971bf1baf37ac2c69"
pdf_path: "papers/cheung-et-al-2005-reaxffmgh-reactive-force-field-for-magnesium-hydride-systems.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2004cheung-et-al-2005-re-venue-no-job -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The work introduces **ReaxFF\(_{\mathrm{MgH}}\)**, a **ReaxFF** parameterization for **Mg**, **H**, and **MgH\(_x\)** chemistry trained on **QM** data for **clusters** and **equations of state** of **bulk** **Mg** and **MgH\(_2\)** phases. The model reproduces **lattice parameters**, **densities**, **EOS**, **bond/angle** energetics, and **reaction** energies for small **hydride** species. **MD** demonstrations follow **H\(_2\)** **absorption/desorption** in **nanoscale** **MgH\(_2\)**, emphasizing **size-dependent** **thermochemistry**: **heat of formation** becomes less negative for smaller **nanoparticles** (roughly **−16 to −19 kcal/Mg** between **0.6–2 nm**), trending toward the **bulk** value near **−20 kcal/Mg** beyond **~2 nm**—linking **nanostructure** to **desorption** behavior relevant to **hydrogen storage** kinetics. The introduction motivates **nanoscaling** as a lever to weaken **Mg–H** binding relative to bulk **MgH\(_2\)**, while noting that **ball-milled** powders often remain in a size regime that still looks **bulk-like** in thermochemistry.

## Methods

### ReaxFF training (checklist A)

- **Lineage / form:** **ReaxFF\(_{\mathrm{MgH}}\)** follows the same development strategy as prior **ReaxFF** families (**hydrocarbons**, **Si/SiO\(_2\)**, **Al/Al\(_2\)O\(_3\)**). Total energy includes **bond/order**, **over/undercoordination**, **valence**, an additional **\(E_{\mathrm{MgH}}\)** term to distinguish distinct **Mg–H** energetics in different bonding environments, plus **van der Waals** and **Coulomb** with **EEM**-style **charge equilibration** (Sec. 2, *J. Phys. Chem. A* **109**, 851–859; **DOI** **10.1021/jp0460184**).
- **Training structures / observables:** fit to **QM** **equations of state** for **Mg** (**hcp**, **fcc**, **bcc**, **simple cubic**, **diamond**) and multiple **MgH\(_2\)** phases (**α**, **β**, **γ**, **CaF\(_2\)**-type, **diamond**-type, plus ground-state **rutile**-type **R-MgH\(_2\)** as labeled in the paper); additional **cluster** data for **bond dissociation**, **angle bending**, and **reaction energies**; **EEM** parameters for **Mg** adjusted to match **DFT Mulliken** charges on small **Mg–H** clusters (**H** parameters inherited from **ReaxFF\(_\mathrm{CH}\)**) (Sec. 2–2.2).

### QM reference (checklist C)

- **Clusters / molecules:** **Jaguar 4.01**, **B3LYP**, **6-311G\*\*++** for **cluster** energetics; **Mulliken** charges for **EEM** training sometimes computed with a **smaller** basis **without diffuse** functions (Sec. 2.2).
- **Condensed phases:** **CASTEP** **plane-wave** **DFT**, **GGA-PBE**, **ultrasoft** pseudopotentials; **k**-mesh via **Monkhorst–Pack** with spacing **0.1 Å\(^{-1}\)**; **kinetic-energy cutoff** **380 eV** (Sec. 2.2).

### Optimization / fitting

- **Procedure:** **successive one-parameter** optimization against the **QM** database; parameters tabulated in **Tables 5–10** with supplementary material referenced (Sec. 2.2).

### Molecular dynamics (checklist B)

- **System build:** **Mg** and **MgH\(_2\)** **nanoparticles** **~0.6–2.2 nm** cut as **spherical** clusters from **hcp** **Mg** and **R-MgH\(_2\)** supercells using **Cerius2** “**Crystal Builder**” with a **bond-order cutoff** (Sec. 2.2).
- **Integration:** **NVT** with **Berendsen** thermostat for **equilibration** and **annealing**; **timestep** **0.25 fs**; **charges** updated **every MD step** (Sec. 2.2).
- **Electrostatics / ReaxFF:** standard **ReaxFF** treatment of **nonbonded** **vdW** + **Coulomb** with **dynamic** charges (Sec. 2).

**MD protocol details (nanoparticle demonstration):** The application section reports **molecular dynamics** of **H\(_2\)** absorption/desorption in **MgH\(_2\)** nanoparticles using **ReaxFF\(_{\mathrm{MgH}}\)**. **N/A — specific MD package** named in the short extract—confirm in `papers/cheung-et-al-2005-reaxffmgh-reactive-force-field-for-magnesium-hydride-systems.pdf`. **System:** spherical **Mg** and **MgH\(_2\)** **nanoparticles** **~0.6–2.2 nm** cut from **hcp** **Mg** and **R-MgH\(_2\)** supercells (**Cerius2** “**Crystal Builder**”, bond-order cutoff) as stated above. **Boundaries / periodicity:** **N/A — full PBC vs vacuum boundary** wording not recovered line-by-line from the excerpt; the nanoparticle demo is described as clusters carved from bulk cells—see Sec. 2.2 in the PDF. **Ensemble:** **NVT** with **Berendsen** thermostat for equilibration/annealing. **Timestep:** **0.25 fs**. **Duration / stages:** **ps**/**ns** timing for full equilibration/production is not restated beyond “equilibration and annealing” in the excerpt—see PDF for schedule. **Thermostat:** **Berendsen**; **N/A — coupling constant** in the indexed text. **Barostat:** **N/A — NPT** not stated for this **NVT** nanoparticle block. **Temperature:** **552 K** appears in the introduction as a cited bulk **dehydrogenation** condition (**1 atm**), not necessarily every production MD temperature—verify trajectory conditions in the PDF. **Pressure / stress:** **N/A — hydrostatic pressure control** for the excerpted **NVT** demo. **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**.

## Findings

- **FF quality (static tests):** **ReaxFF\(_{\mathrm{MgH}}\)** reproduces the **QM**-derived **cell parameters**, **densities**, and **EOS** trends for the **Mg** and **MgH\(_2\)** phases included in training, and matches **cluster** **bond/angle** scans and **reaction** energetics within the figures/tables reported in Sec. 3 (*J. Phys. Chem. A* **109**, 851–859).
- **Nanoparticle thermochemistry:** **heat of formation** becomes less exothermic as particle size decreases—**roughly −16 to −19 kcal/(mol Mg)** for **~0.6–2.0 nm** particles, approaching the **bulk** **~−20 kcal/(mol Mg)** by **~2 nm** and above—so **ball-milled** **20–100 nm** particles remain **near-bulk** in this model (Sec. 3 / abstract).
- **Implication stated by the authors:** **size-dependent** **thermochemistry** motivates exploring **smaller** **nanoscale** hydrides for **H\(_2\)** release conditions relative to **bulk** **MgH\(_2\)** (high **dehydrogenation** temperature at **1 atm** cited in the introduction).
- **Limitations (authors / model):** **kinetics** of **H\(_2\)** evolution includes barriers, **catalysis**, and **restructuring** beyond a single **nanothermochemistry** demonstration; **FF** transferability follows the usual **ReaxFF** bounds of the training set.

## Limitations

- **Kinetics** of **H\(_2\)** release involves **kinetics barriers**, **surface** **reconstruction**, and **catalysis** not fully captured in a single **nanoparticle** **thermochemistry** demo.
- **QM** training coverage bounds **transferability** to **alloys**, **defects**, and **extreme** conditions.

## Relevance to group

Core **ReaxFF** **lineage** paper with **Adri C. T. van Duin** on **metal hydrides** and **hydrogen-storage** motivated **MD**—directly adjacent to **materials** **energy** applications.

## Citations and evidence anchors

- Primary citation via PDF metadata; add **journal DOI** in front matter when confirmed from the **published** version if this file is a **preprint** capture.

## Related topics

- [[reaxff-family]]
