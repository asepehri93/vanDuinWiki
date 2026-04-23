---
id: paper:2016gonzalez-venue-metal-nanotube-composites
type: paper
title: "Metal-nanotube composites as radiation resistant materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reactive-md
  - material:metal-surface
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4959246"
year: 2016
authors:
  - "Rafael I. González"
  - "Felipe Valencia"
  - "José Mella"
  - "Adri C. T. van Duin"
  - "Kang Pyo So"
  - "Ju Li"
  - "Miguel Kiwi"
  - "Eduardo M. Bringa"
venue: "Applied Physics Letters"
pdf_sha256: "de1309f1c7d5b598ef58badb96378c41640d6a05832cca342ccf3dd90cc09731"
pdf_path: "papers/Gonzalez_CNT-Ni-chimney_2016.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:graphene-carbon
  - keyword:lammps
  - keyword:nose-hoover
---
<!-- id:paper:2016gonzalez-venue-metal-nanotube-composites -->

## Summary

**Reactive molecular dynamics** with **ReaxFF** studies **helium** transport in **nickel** containing **carbon nanotubes (CNTs)**, motivated by **radiation-induced helium swelling and embrittlement** in **structural** materials where **He** **bubbles** degrade **ductility**. The simulations compare **defect-free** versus **vacancy-containing** CNT models to separate **interface** **trapping** from **fast** **outgassing** along **CNT** **interiors** when **wall** **defects** exist. **Helium** is represented with **Morse**-type **van der Waals** interactions to **Ni** and **C** atop the reactive **Ni/C/H** **ReaxFF** core, enabling **physisorption**-limited **ingress** without **spurious** **chemistry** at the **He** **pair** level. **Adri C. T. van Duin** is a coauthor.

## Methods

- **Code:** **LAMMPS** large-scale reactive MD.
- **Potential:** **ReaxFF** parametrization combining **Ni/C/H** with **noble-gas** interactions; **He** interacts with **Ni** and **C** via **van der Waals (Morse)** terms with **combination-rule** parameters (as described in the article).
- **Integration / ensemble:** Time step **0.5 fs**; **NPH** dynamics with **Nose-Hoover** **thermostat** coupling and **barostat**-style **anisotropic stress** control implemented via the **LAMMPS stress tensor** (damping **500 fs**) plus periodic **temperature rescaling every 10 steps** (values stated in the paper).
- **System:** **Atomistic** **supercell** with **Ni** matrix, embedded **CNTs**, and explicit **He** loading; **vacancies** introduced in **CNT** walls to mimic **radiation** **defects**; **helium** **diffusion** tracked at **metal–CNT interfaces** and along **CNT** **cores**. **Periodic boundary conditions (PBC)** apply in three dimensions as in standard **LAMMPS** bulk models.
- **Duration:** per-protocol **production** times in **ps**/**ns** are tabulated in *Appl. Phys. Lett.* (**N/A — not copied into this note**).

## Findings

- For **pristine (defect-free) CNTs**, **helium** diffuses along **metal–CNT interfaces** and accumulates there; **no helium penetration** through **perfect** CNT walls is observed, consistent with **impermeable graphene**-like **barriers** in the model.
- With **vacancies** in CNT walls, **helium** can **enter CNT interiors**, where nanotubes act as **one-dimensional “nano-chimneys”** enabling **outgassing** and reducing **bubble** **nucleation** in the **metal** relative to scenarios without such **escape** paths.
- The authors argue **metal–CNT composites** can improve **radiation tolerance** when **helium swelling / embrittlement** is limiting, by providing **fast escape pathways** for **helium** relative to **bulk** **Ni** without **CNTs**.

Relative to **bulk Ni** without **CNTs**, embedding changes **He** partitioning and escape kinetics under the same loading assumptions. **Vacancy** density in **CNT** walls is the main structural lever between **interface-only** transport and **nano-chimney** outgassing. **Figure-level He fields and stress targets** are in **`papers/Gonzalez_CNT-Ni-chimney_2016.pdf`**; idealized **interfaces** and absent **collisional defect production** are caveats in **Limitations** and the **APL** text.

## Limitations

Classical reactive MD cannot capture full **defect production** under **irradiation**; **vacancies** are **introduced phenomenologically**. **Atomistic** **length/time** scales require **upscaling** to **engineering** microstructures and **dose** rates; **He** **production** rates are not modeled explicitly.

## Relevance to group

Direct **van Duin co-authorship**; demonstrates **ReaxFF** for **He transport** in **Ni–carbon** nanocomposite geometries relevant to nuclear materials concepts.

## Citations and evidence anchors

- DOI: [10.1063/1.4959246](https://doi.org/10.1063/1.4959246) — *Appl. Phys. Lett.* **109**, 033108 (2016).

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

Pair this **Appl. Phys. Lett.** entry with broader **nuclear materials** **MD** corpora by noting that **He** **transport** here is **classical** **physisorption**-limited and does not include **radiation** **damage** **cascade** physics or **H**/**He** **co-diffusion** at **grain** **boundaries**. **CNT** **diameters** and **Ni** **matrix** **dimensions** should be read from the **APL** figures when scaling **flux** estimates.
