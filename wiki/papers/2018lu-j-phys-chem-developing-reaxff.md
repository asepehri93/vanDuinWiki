---
id: paper:2018lu-j-phys-chem-developing-reaxff
type: paper
title: "Developing ReaxFF to Visit CO Adsorption and Dissociation on Iron Surfaces"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - material:metal-surface
  - method:dft-static
  - method:reaxff
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:dft-static
  - keyword:lammps
  - keyword:catalysis-surface
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.8b10427"
year: 2018
authors:
  - "Kuan Lu"
  - "Yurong He"
  - "Chun-Fang Huo"
  - "Wen-Ping Guo"
  - "Qing Peng"
  - "Yong Yang"
  - "Yong-Wang Li"
  - "Xiao-Dong Wen"
venue: "J. Phys. Chem. C 2018, 122, 27582–27589"
pdf_sha256: "3767c70d08e443eb67be843fbfa2d88d0744687df968c2fe911f111cbcbe229d"
pdf_path: "papers/ReaxFF_others/Lu_JPC_CO_Fe_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2018lu-j-phys-chem-developing-reaxff -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

## Summary

Iron Fischer–Tropsch and related catalysis hinges on CO adsorption, CO bond scission, hydrogenation, and C–C coupling on metallic iron surfaces, but transferable reactive models must reproduce both energetics and the many-body environment around steps and terraces. The manuscript parameterizes a **Fe/C/O ReaxFF** potential (**RPOFeCO-2018**) using **VASP** **spin-polarized DFT** training data (including **NEB** paths for **CO dissociation** on **Fe** surfaces), with **genetic-algorithm** fitting described in the article, then validates the model on **CO adsorption/dissociation** and **C–C coupling** while including **lateral** adsorbate–adsorbate interactions that are easy to omit in cluster-only quantum studies. **Reactive MD** with **LAMMPS** explores how **CO activation** differs across **Fe** facets; the abstract states that **Fe(110)** is **inert for CO activation at the initial stage** yet **maintains comparatively high CO dissociation activity in the long run** relative to other surfaces examined, **including Fe(310)**. Section 2 of the peer-reviewed PDF documents plane-wave cutoffs, PAW setups, and smearing choices used to build the training sets feeding the ReaxFF fit. The authors note explicitly that extending the model to carbide phases and full Fischer–Tropsch product spectra will require additional training beyond the Fe/C/O scope emphasized here.

## Methods

### A — QM reference data (DFT, VASP)

- **Functional / potentials:** **GGA-PBE** with **PAW** **pseudopotentials**; **plane-wave** **cutoff 400 eV**; **Methfessel–Paxton** smearing (**σ = 0.1 eV**).
- **Spin treatment:** **spin-polarized** **Fe** **surfaces** and **adsorbates** as appropriate to training sets.
- **Reaction pathways:** **climbing-image NEB** (or equivalent) for **CO** **dissociation** barriers on **Fe** facets used in **ReaxFF** training.

### B — ReaxFF optimization

- **Parameter set:** **RPOFeCO-2018** for **Fe/C/O** chemistry fit to the **DFT** databases (genetic-algorithm / optimization workflow in §2 of the article).
- **Charges:** standard **ReaxFF** **EEM**-type **charge** treatment (§2.2).

### C — Reactive molecular dynamics (LAMMPS)

- **RMD:** **LAMMPS** **large-scale** **ReaxFF** simulations comparing **CO** **adsorption**/**dissociation** on multiple **Fe** **facets** (**Fe(110)**, **Fe(310)**, others in **Results**); **timestep**, **ensemble**, **temperature**, and **run lengths** in the peer-reviewed **Methods**.

### D — Experiments

- **Not an experimental catalysis paper**; **surface science** claims are **computational** with **literature** context.

### MD application (RMD validation on Fe surfaces)

**Large-scale reactive MD** is performed with **LAMMPS** using **RPOFeCO-2018** to compare **CO adsorption/dissociation** on multiple **Fe** facets (including **Fe(110)** and **Fe(310)** in the abstract). **System & boundaries:** periodic **slab/supercell** models of the cited surfaces (**atom** counts and vacuum padding in **Methods**). **Ensemble / thermostat / barostat / timestep:** **N/A — not duplicated** in this excerpt-based note—copy from §2–3 of the **J. Phys. Chem. C** PDF. **Duration / stages:** **equilibration** followed by **production** **RMD** segments with lengths in **ps**/**ns** tabulated in **Methods** (not transcribed here). **Temperature:** setpoints for production **RMD** appear in the article’s simulation tables (**N/A — explicit K list** not transcribed here). **Pressure:** **N/A — surface RMD** typically constant-volume unless the article specifies **NPT** for a given stage (confirm in PDF). **Electric field:** **N/A — not used**. **Enhanced sampling:** **N/A — not indicated** for the **RMD** validation stages summarized in the abstract (authors use **NEB** at the **DFT** stage, not as a bias in the quoted **RMD** summary).

### Force-field training (ReaxFF optimization)

**Parent / scope:** new **Fe/C/O** parameter set **RPOFeCO-2018** built on prior **Fe–C** ReaxFF work expanded with **Fe–C–O** interactions (Introduction/§2). **QM reference:** **spin-polarized DFT** in **VASP** with **GGA-PBE**, **PAW** potentials, **400 eV** plane-wave cutoff, and **Methfessel–Paxton** smearing (**σ = 0.1 eV**); **climbing-image NEB** locates **CO dissociation** transition states on **Fe** surfaces used in the training corpus. **Training set:** expanded **trainsets** of **first-principles** **energies**, **geometries**, and **barrier** structures feeding the **Fe/C/O** fit (§2.1–2.2 narrative). **Optimization:** **genetic algorithm** in the authors’ in-house fitting code (§2.2). **Validation / reference data:** **RPOFeCO-2018** is tested against **DFT** for **CO adsorption/dissociation** and **C–C coupling**, including **lateral** adsorbate–adsorbate interactions called out in the abstract.
## Findings

**Outcomes.** **RPOFeCO-2018** reproduces the **DFT**-targeted **CO adsorption/dissociation** and **C–C coupling** checks quoted in the abstract, explicitly including **lateral** interactions between co-adsorbed molecules.

**Facet trends.** **Fe(110)** is **inert for CO activation at the initial stage** yet retains **comparatively high CO dissociation activity in the long run** relative to other surfaces examined (**Fe(310)** named in the abstract).

**Comparisons / validation.** Claims are **computational**: **ReaxFF** vs **VASP** training/validation data as described in the article rather than new experiment on this communication.

**Sensitivity / outlook.** **Surface structure** (terrace vs step-like facets in the study’s models) is the primary **sensitivity** axis in the abstract’s **structure–activity** framing.

**Limitations.** Extending to **carbide** phases and full **Fischer–Tropsch** product space requires **additional training** beyond the emphasized **Fe/C/O** scope (see **## Limitations**).

**Corpus honesty.** Surface-specific numerical barriers and coverages should be read from the **PDF** (`papers/ReaxFF_others/Lu_JPC_CO_Fe_2018.pdf`) and SI, not inferred from the short extract alone.
## Limitations

- **Transferability** to **carbide** phases and **complex** **Fischer–Tropsch** environments requires additional **training** beyond the **Fe/C/O** scope emphasized here.

## Relevance to group

Illustrates **ReaxFF** **reparameterization** for **Fe/C/O** with **DFT**-heavy **training** and **surface-catalysis** **RMD** follow-through.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1021/acs.jpcc.8b10427](https://doi.org/10.1021/acs.jpcc.8b10427)

## Reader notes (navigation)

- Surface catalysis + ReaxFF training: [[reaxff-family]], [[theme-oxides-silica-ceramics]] (adjacent oxides context).

## Related topics

- [[reaxff-family]]
