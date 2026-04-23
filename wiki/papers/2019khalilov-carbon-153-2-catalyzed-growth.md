---
id: paper:2019khalilov-carbon-153-2-catalyzed-growth
type: paper
title: "Catalyzed growth of encapsulated carbyne"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:catalysis-surfaces
  - method:reaxff
  - method:dft-static
  - task:application
  - material:graphene-carbon-nano
paper_keywords:
  - keyword:reaxff-application
  - keyword:dft-static
  - keyword:graphene-carbon
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2019.06.110"
year: 2019
authors:
  - "Umedjon Khalilov"
  - "Charlotte Vets"
  - "Erik C. Neyts"
venue: "Carbon"
pdf_sha256: "91ef1bafe8279dc14e8ba94395c2319555492f236f505ee33e2a93aafd668f93"
pdf_path: "papers/ReaxFF_others/Khalilov_Neyts_Carbon_2019_carbyne_growth.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019khalilov-carbon-153-2-catalyzed-growth -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *Carbon* article identified by `doi`, `title`, and `pdf_path`.

## Summary

Linear carbon chains (**carbyne**) inside carbon nanotubes are of fundamental interest, but growth mechanisms from small **hydrocarbon** feeds on **catalyst** clusters require atomistic detail. This work combines **ReaxFF molecular dynamics** (Zou *et al.* parameters) with **DFT** (**VASP**, **GGA-RPBE**, **PAW**) to study **Ni-catalyzed** insertion of **C\(_2\)**, **C\(_2\)H**, and **C\(_2\)H\(_2\)** into a **(5,5)@(10,10)** double-walled nanotube at **500 K** versus **1700 K** effective carbon fluxes. **Sticking** and **adsorption energies** **anticorrelate** with **H/C** ratio in the feed; **step-like** Ni facets favor **C–H** cleavage compared with flatter **(111)**-like surfaces. **DFT** finds **stronger binding** magnitudes than **ReaxFF** but **consistent trends**.

The **double-walled** **CNT** framework confines **Ni** and **hydrocarbon** **feeds** to a **one-dimensional** reaction environment, amplifying **facet**-dependent **selectivity** that would be harder to resolve on open **surfaces** with many competing sites.

## Methods

### 1 — MD application (RMD, ReaxFF)

**Engine / code:** **ReaxFF** (parameters of **Zou** *et al.*, as in the *Carbon* **Methods**), **periodic** **PBC** along the **nanotube** **axis** only. **System / composition:** **(5,5)@(10,10)** **double-walled** **nanotube** (inner/outer diameters **~0.70** / **~1.39 nm**); **Ni** **cluster** in the **inner** channel; feed **C\(_2\)**, **C\(_2\)H**, **C\(_2\)H\(_2\)**. **Ensemble and thermostats:** **NpT** equilibration with a **Berendsen** **thermostat** and **barostat**, then **NVT** production with a **Bussi** **thermostat**; **500 K** vs **1700 K** **target** **temperatures** for **RMD** as reported. **Feed protocol:** **insertion** every **25 ps** at **1700 K** and every **250 ps** at **500 K** to match **low** vs **high** **carbon** **flux**. **Timestep (fs):** **N/A** — not stated in the *Carbon* **Methodology** text in the **PDF** (confirm in **SI** if **reproducing**). **Barostat in production:** **N/A** when **NVT**—**NPT** only in the **preequilibration** **stage** as written. **Mean** **hydrostatic** **pressure** **control** in **NVT:** **N/A** (constant **volume** **NVT**). **Electric field:** **N/A**. **Replica / enhanced sampling:** **N/A**—sequential **RMD** only. **Long-range** **electrostatics** / **ReaxFF** **QEq** **update** **schedule:** per **Zou** **et al.** / **ReaxFF** **defaults** in the **cited** **implementation** (not re-tabulated here).

### 2 — Force-field training

**N/A** — this work **uses** a **published** **ReaxFF** for **C/H** and **Ni**-containing **carbon** **environments** (**Zou** *et al.*); the **new** **science** is the **MD**+**DFT** **application**, not a **reoptimization** of the **field** in this **article**.

### 3 — Static QM (VASP, supporting DFT and NEB)

**Functional / theory level:** **GGA** **RPBE** in **VASP** with **PAW**; **400 eV** **cutoff**; **in-plane** **~20×20 Å**-scale **supercells** with **Γ-centered (1×1×1) k** **mesh** as **described**; **spin** **polarization**; **no** **symmetry** **constraints**; **Gaussian** **smearing** as in the **paper**. **Dispersion:** **PBE+TS** **tests** **(Tkatchenko–Scheffler)** are **reported** as **negligible** for the **quantities** **considered**; **main** **DFT** **data** in the **manuscript** are **without** **vdW** **corrections** for those **comparisons**. **Structures / pathways:** **slab**/**cluster** **geometries** for **adsorption** and **NEB** **reaction** **paths** (initial **dimer** **nucleation** with **barriers** **~0.1–0.3 eV** in the **Results**). **Properties computed:** **adsorption** **energies** and **barrier** **heights** used to **compare** **trends** with **ReaxFF**.
## Findings

**Dimerization** competes with **dehydrogenation** during early growth; **Ni-terminated** chains allow **hydrogen** tuning of electronic response; **hydrocarbon identity** controls whether **C–C** or **C–H** scission dominates on **curved** Ni facets. **ReaxFF** and **DFT** adsorption energies can differ by roughly **2×** in places while preserving qualitative ordering.

**Cross-validation message.** The authors use **DFT** not only for **barriers** but also as a **check** on **ReaxFF** **trends**, which is important when **absolute** **adsorption** strengths feed into **rate** estimates.

**Confinement effects.** The **inner** **(5,5)** tube sets a **strong** **curvature** and **electronic** **perturbation** on **Ni** clusters compared with **flat** **surface** **models**, so **facet** arguments should be read as **curvature-dependent** **selectivity** rather than universal **Ni** **catalysis** rules.

**Chain-growth outlook.** The paper focuses on **early** **insertion** steps; **long** **chain** **stability** under **beam** or **oxidizing** environments is outside the **present** **ReaxFF** scope.

**Repository use.** Treat **`papers/ReaxFF_others/Khalilov_Neyts_Carbon_2019_carbyne_growth.pdf`** as the **evidence** anchor for **barrier** ranges and **cluster** **geometries** when aligning **follow-on** **kinetic** **Monte** **Carlo** models.

## Limitations

Long **carbyne** **stability** is not the primary focus; results emphasize **growth mechanism** trends. Parameter transfer to other metals or tube chiralities needs separate validation.

## Relevance to group

**Reactive carbon nanotube** chemistry adjacent to broader **ReaxFF** carbon materials work.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1016/j.carbon.2019.06.110](https://doi.org/10.1016/j.carbon.2019.06.110) (`papers/ReaxFF_others/Khalilov_Neyts_Carbon_2019_carbyne_growth.pdf`).

## Related topics

- [[reaxff-family]]
