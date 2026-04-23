---
id: paper:2013dlc-venue-untitled
type: paper
title: "A shear localization mechanism for lubricity of amorphous carbon materials"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:mechanics-tribology
  - domain:carbon-hydrocarbon
  - method:classical-md
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:tribology
  - keyword:classical-ff
  - keyword:reactive-md
  - keyword:graphene-carbon
source_refs: []
doi: "10.1038/srep03662"
year: 2014
authors:
  - "Ma, Tian-Bao"
  - "Wang, Lin-Feng"
  - "Hu, Yuan-Zhong"
  - "Li, Xin"
  - "Wang, Hui"
venue: "Scientific Reports"
pdf_sha256: "ae8146dca00108a905471341d7c3adf829f42dddb6b8e2a9e107a183c9f96880"
pdf_path: "papers/Others/DLC_friction_AIREBO_srep03662_2015.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013dlc-venue-untitled -->

## Evidence and attribution

!!! note "Authority of statements"

    Sections below summarize the publication identified by `doi`, `title`, and `pdf_path` in the front matter.

## Summary

Large-scale **atomistic simulations** (including **AIREBO**-class reactive hydrocarbon potentials in the authors’ framework) are used to argue that **ultralow friction** and **stick–slip** transitions in **diamond-like carbon (DLC)** sliding can arise from **shear localization**: inhomogeneous deformation concentrates strain in a **tribolayer**, with **bond reorientation**, local **sp³→sp²**-like ordering, and **graphitic** sheet clustering rather than only **dangling-bond passivation**. The study reports a pressure-driven transition from **stick–slip** to **continuous sliding** with exceptionally low friction as layered graphitic structures develop in the localized shear band.

## Methods

- **Atomistic MD** shear of **hydrogen-free** and **hydrogenated** **diamond-like carbon (a-C)** against **diamond** and self-mated **a-C** using **AIREBO**-class **reactive** hydrocarbon potentials (as described in the article’s simulation section), exposing stick–slip and steady sliding over **nanosecond**-scale trajectories.
- **Normal loads** are varied to span nominal **pressures** from **~4 GPa** to **~80 GPa** in the setup reported in **Figure 1**; friction traces and **C–C bond-orientation (CBOA)** metrics track **tribolayer** restructuring during sliding.

**1 — MD application (explicit vocabulary aligned with the article; confirm any package name in the PDF):**

- **Engine / code:** Large-scale **molecular dynamics** with **AIREBO**-style **reactive** hydrocarbon interactions (implementations commonly use **LAMMPS**; verify the stated engine in the **Methods** section of `papers/Others/DLC_friction_AIREBO_srep03662_2015.pdf`).
- **System size & composition:** **Many-atom** **supercells** of **DLC** films on **diamond** and self-mated **a-C** tribopairs with **hydrogen** coverage variants as summarized above (exact **atom** counts and film dimensions are given in the article’s setup tables/figures).
- **Boundaries / periodicity:** In-plane **periodic boundary conditions** (**PBC**) on the **simulation** cell with tribology-appropriate out-of-plane boundary handling as described in the publication (**fixed** regions vs free surfaces per their **Figure 1** protocol).
- **Ensemble / thermostat:** **NVT**-like **thermal** control (thermostat type and damping as in the article) on non-sliding regions while imposing **shear**; **temperature** is maintained in the reported **300 K** class window unless the **PDF** states ramps—quote the **PDF** for exact values.
- **Timestep:** Sub-femtosecond to ~**1 fs** class **timestep** typical for **C–C** reactive carbon **MD** (confirm in **Methods**).
- **Duration:** **Multi-ns** segments (**ns**-scale production) as summarized by “**nanosecond**-scale trajectories” above; equilibration vs production split per **PDF**.
- **Barostat:** **N/A** — normal **stress** is imposed via **mechanical loading** (**GPa**-scale **pressure** targets) rather than a homogeneous fluid **Parrinello–Rahman** **barostat** on the entire cell (tribology boundary condition).
- **Pressure:** Nominal contact **pressures** **~4–80 GPa** from applied **load** as in **Figure 1**.
- **Shear / strain:** **Shear** driven sliding at reported **sliding speeds** (see **PDF** for **strain rate** magnitudes).
- **Electric field / enhanced sampling:** **N/A** — no applied **electric field** or umbrella/metadynamics workflow indicated in this wiki summary.

## Findings

- Friction traces show **running-in** (**shear weakening**) where peak friction first rises then falls; **steady-state** friction after weakening **decreases** with increasing **pressure** in the high-load regime reported, eventually approaching a near-**frictionless** steady state with strongly suppressed **stick–slip**.
- **Shear localization** appears as a **thin shear band** with large **CBOA** changes (toward in-plane **graphitic** ordering) rather than homogeneous **affine** shear through the film.
- The authors argue that **superlubricity**-like behavior in this model arises from **pressure-driven** **graphitic** **clustering**/**layering** within the **tribolayer**, not from **dangling-bond passivation** alone (which they compare in separate hydrogenated scenarios in the study).

## Limitations

- Potential-dependent tribology: quantitative friction coefficients and transferability across DLC chemistries require potential validation; simulation strain rates exceed experiment.

## Relevance to group

**Not ReaxFF-centric**; included as **carbon tribology / classical reactive MD** corpus context adjacent to group carbon materials interests.

## Citations and evidence anchors

- Abstract and results: mechanism claims (Sci. Rep.; DOI above).

## Reader notes (navigation)

- Wiki slug retains **2013**-style naming from ingest, but the **published** article is **2014** (`10.1038/srep03662`). Future manifest normalization may rename the slug; stable `id` remains until maintainers migrate.

## Related topics

- [[graphene-nanocarbon]]
- [[reaxff-family]]
