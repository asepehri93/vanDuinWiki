---
id: paper:2024winetrout-nat-implementing-reactivity
type: paper
title: "Implementing reactivity in molecular dynamics simulations with harmonic force fields"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:classical-ff-specialized
  - method:reactive-md-generic
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:method-development
  - keyword:classical-ff
  - keyword:reactive-md
  - keyword:polymer
candidate_tags: []
source_refs: []
doi: "10.1038/s41467-024-50793-0"
year: 2024
authors:
  - "Jordan J. Winetrout"
  - "Krishan Kanhaiya"
  - "Joshua Kemppainen"
  - "Pieter J. in 't Veld"
  - "Geeta Sachdeva"
  - "Ravindra Pandey"
  - "Behzad Damirci"
  - "Adri van Duin"
  - "Gregory M. Odegard"
  - "Hendrik Heinz"
venue: "Nat. Commun."
pdf_sha256: "010772d49769254d1fbe5664f7df9b9e7d9166839045b0a4b12b2bcced977ce2"
pdf_path: "papers/Winetrout_IFF_ReaxFF_NatureComm_2024.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2024winetrout-nat-implementing-reactivity -->

!!! abstract "Scope"
    **Reactive INTERFACE Force Field (IFF-R):** replace **harmonic** bond springs with **Morse** bonds inside **IFF**-class and compatible **biomolecular/organic** harmonic FFs (**CHARMM, PCFF, OPLS-AA, AMBER**), add **template-based bond formation**, and benchmark against **ReaxFF**-style cost—**~30×** reported speedup over prior reactive schemes.

## Summary

Large-scale **reactive molecular dynamics** must balance **accuracy**, **system size**, and **cost**. The paper introduces **IFF-R**, which keeps the **nonbonded** and most **bonded** machinery of **harmonic** force fields but swaps **harmonic bond potentials** for **reactive, energy-conserving Morse** bonds (**three interpretable parameters per bond type**, **zero energy at full dissociation**). **Bond-forming** events are handled with **template-based** approaches. The framing contrasts this with **bond-order** reactive models such as **ReaxFF**, which add many energy terms and higher computational overhead while using **single atom types per element**.

## Methods

The extract covers **motivation**, **IFF** design principles (accuracy targets on lattices, surfaces, hydration, **compatibility** with **CHARMM/AMBER/OPLS/PCFF**), and **comparison to ReaxFF** (many-body bond order, complexity, cost). **IFF-R** construction—**Morse** parameters per bond type, **merging** with existing **IFF + biomolecular** setups—and **implementation details** (software, integrator, parallelization) continue **beyond** the two-page extract. **Numerical benchmarks** (timing vs. ReaxFF, energy conservation tests) appear later in the article.

**IFF-R mechanics (as stated at high level).** **Harmonic** **bond** terms are replaced by **Morse** potentials with **three** **parameters** per **bond** type so bonds can **dissociate** smoothly while retaining compatibility with existing **atom typing** in **biomolecular** force fields. **Bond formation** uses **template**-driven **reconnection** moves rather than **bond-order**-dependent many-body energy expressions, which is how the authors report large **speedups** relative to **legacy** reactive schemes while staying in a **CHARMM/OPLS/AMBER**-like **typing** ecosystem.

**Relation to ReaxFF (comparison, not a fit).** The article contrasts **ReaxFF**’s **element-centric** **bond-order** formalism and larger **parameter** count with **IFF-R**’s strategy of **minimal** **reactive** extensions atop **IFF** **nonbonded** models; timing comparisons and **energy conservation** tests in the **full PDF** quantify **computational** trade-offs for **polymer** and **composite** examples.

**1 — MD application (IFF-R benchmark systems).** **Engine:** **molecular** **dynamics** in **LAMMPS**-integrable **setups** (as **documented** in the **full** **article**) using **IFF**-**R**; **N/A** for **integrator** **name** and **ps**/**ns** **trajectory** **length** in the **short** **extract** (see **`pdf_path`** for **Results**). **System** **sizes** and **atom** **counts** for **timing** **vs** **ReaxFF** and **polymer**/**composite** **demos** are in the **full** **article**. **NVT**/**NVE** **ensembles**, **fs** **timestep**, **K**-scale **temperature** **baths**, **GPa**/**bar**-scale **NPT** **pressures** (if any), **PBC** **wiring**, **Langevin**/**Nosé**-style **thermostat** tags, and **E-field** **or** **metadynamics** **add-ons:** **N/A** in the **two-page** **excerpt** used to seed this note.

**2 — Force-field training (IFF-R construction).** **Not** **ReaxFF** **parameterization**: **IFF-R** **replaces** **harmonic** **bonds** with **three-parameter** **Morse** **terms** on **IFF**/**CHARMM**/**OPLS**/**AMBER**/**PCFF**-compatible **typings** and adds **template**-based **bond** **formation**; **parent** **nonbonded** **params** **retained** where **bonds** **intact**. **3 — Static QM** — **N/A** as a **DFT**-centric **paper**; **quantum** **data** may **enter** **IFF** **benchmarks** **elsewhere**, not the **focus** of the **intro** **extract**.

**4 — Methodology / software paper** — see **`## Findings`** for **declared** **speedups** and **scope**.
## Findings

As described in the **abstract** and full **text**, the paper reports **molecular dynamics** (MD) **benchmarks** and **reactive** **trajectories** in **LAMMPS**-compatible and related **environments** for **polymers** and **composites**; the short extract on disk does not reproduce every **ps/ns** table.

**Scope and performance (abstract).** **IFF-R** is reported to support **bond** **dissociation** and **reformation** via **templates** across **molecules**, **polymers**, **carbon** **nanostructures**, **proteins**, **composites**, and **metals**, while **retaining** **parent** **harmonic**-**FF** **accuracy** where **bonds** **remain** **intact**, with **~30×** **wall**-**clock** **gains** **vs** **prior** **reactive** **schemes** in the **abstract**’s **claim** (see **full** **text** for **definitions**). **Design** **philosophy** (introduction): **atom**-**type**-centric **compatibility** **vs** **ReaxFF**’s **element**-centric **bond**-**order** **formalism**.

**Corpus honesty** — **quantitative** **timings** and **failure** **modes** need **`pdf_path`**; short **extract** only orients the **method**.
## Limitations

The local extract is **short**; **quantitative** performance data, **failure modes**, and **parameter fitting** workflows require the **full PDF**. **Template-based bond formation** may not cover all **reaction classes** accessible to **ReaxFF**.

## Relevance to group

**Adri van Duin** is a co-author alongside **Heinz**, **Odegard**, and others, situating the work at the interface of **INTERFACE/ReaxFF communities** and **reactive MD** methodology.

## Citations and evidence anchors

- DOI: [10.1038/s41467-024-50793-0](https://doi.org/10.1038/s41467-024-50793-0)

## Related topics

- [[reaxff-family]]
