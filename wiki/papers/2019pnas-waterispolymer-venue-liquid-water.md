---
id: paper:2019pnas-waterispolymer-venue-liquid-water
type: paper
title: "Liquid water is a dynamic polydisperse branched polymer"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:water-silica-geo
  - method:classical-md
  - task:parameterization
  - scale:atomistic
paper_keywords:
  - keyword:qm-training-data
  - keyword:water-interfaces
  - keyword:classical-ff
candidate_tags: []
source_refs: []
doi: "10.1073/pnas.1817383116"
year: 2019
authors:
  - "Saber Naserifar"
  - "William A. Goddard III"
venue: "Proc. Natl. Acad. Sci. U.S.A."
pdf_sha256: "298481e616bc4dff409bc1659fd7bf2c635e075e34a6416a6a7bacec17da9ed5"
pdf_path: "papers/Others/PNAS-WaterIsPolymer.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019pnas-waterispolymer-venue-liquid-water -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes the **PNAS** article identified by `doi`. **RexPoN** is a **Goddard-group** water force field distinct from **ReaxFF**; use this page as a **comparative reference** for **QM-fitted** **classical** water models.

## Summary

The **RexPoN** force field for water is parametrized from **quantum mechanics** **without empirical fitting** to experimental liquid properties. **Molecular dynamics** with **RexPoN** is reported to reproduce **bulk** **thermodynamics** and **structure**, then supports a **structural** interpretation of **hydrogen-bond** connectivity in the liquid as a **dynamic**, **polydisperse**, **branched** network. The authors motivate the work as a route to reconcile **anomalies** in liquid and **supercooled** water with **microscopic** **connectivity** statistics beyond simple **tetrahedral** pictures (abstract; introduction).

## Methods

**1 — MD application.** **Molecular dynamics** simulates a **water** system with on the order of **hundreds to thousands of atoms** in **3D** **PBC** (see **PNAS** for the exact **supercell** and **H₂O** count). **NVT**/**NVE**-style **control** through **melting** from **ice** to **liquid**; **thermostat** and any **NPT** **barostat** **/ hydrostatic** **pressure** are as in **Methods**. **Time step** in **fs**, **equilibration** and **production** **ps**/**ns** spans, and **temperature** **K** **ramps** follow the paper (not retyped here at **~298** **K** checkpoints). **External electric field:** **N/A** in the main SHB **analysis** description. **Umbrella / metadynamics:** **N/A** unless stated. **NEMD** (thermal gradient MD): **N/A** for the **RexPoN** **bulk** **liquid** **connectivity** **study** summarized here.

**2 — Force-field training (RexPoN, classical water).** **RexPoN** is a **Goddard-group** **classical** **force field** for water built from **QM** (no **empirical** **fit** to **bulk** **liquid** **PVT** in the same way as many **TIP** models). Contributors include **vdW** terms tied to **H\(_2\)**/**O\(_2\)** **equations of state**, **electrostatics**, and **many-body** couplings (see **PNAS** and prior **RexPoN** references). This is **not** a **ReaxFF** reparameterization.

**3 — Static QM.** **QM** data underpin **RexPoN** **parameters**; there is no separate **DFT** **Results** “application” block as the main **finding** of the paper is **classical** **MD** on **RexPoN** water.

**4 — Review / non-sim.** **N/A.**
## Findings

- **Thermodynamic** checkpoints at **298 K** (density, \(\Delta H_\mathrm{vap}\), entropy, dielectric constant) and **melting point** lie close to **experiment** in the reported comparisons.
- Upon **melting**, **SHBs** per molecule drop from **ice**-like values near **four** to about **two** in the liquid regime described; lifetimes are on the order of **tens** to **~90 fs** at **298 K** in their analysis.
- **SHBs** link into **dynamic** **branched chains** averaging **~150** water molecules at **298 K** with **branch points** carrying **three** **SHBs** and **terminators** **one** **SHB**—a picture offered to rationalize **long-range** **angular correlations** and **anomalies** in **supercooled** water.
- The **“polymer”** metaphor is explicitly **structural** (connectivity statistics), not a claim that water is a **covalent polymer** in the usual chemical sense (discussion framing in the article).

**Corpus honesty.** For **definitive** **locators** and any **update** to **RexPoN** text, use the **version-of-record** **PNAS** PDF; this page is a **curated** summary, not a substitute for **figure** captions and **SI**.
## Limitations

Interpretive claims about macroscopic “polymer” behavior are model-dependent; subsequent literature debates alternative explanations—read alongside critical discussions.

**RexPoN** parameters prioritize **bulk** **water**; **transfer** to **interfaces** and **solutes** requires **separate** **validation** against **QM** or **experiment** for each **new** **chemistry**.

## Relevance to group

Complementary reference water model (RexPoN) outside the ReaxFF lineage; useful contrast for aqueous interface projects parametrized with ReaxFF.

## Citations and evidence anchors

- DOI: [10.1073/pnas.1817383116](https://doi.org/10.1073/pnas.1817383116)

