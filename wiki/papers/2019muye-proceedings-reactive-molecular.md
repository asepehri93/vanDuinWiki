---
id: paper:2019muye-proceedings-reactive-molecular
type: paper
title: "A reactive molecular dynamics simulation study of methane oxidation assisted by platinum/graphene-based catalysts"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:catalysis-surfaces
  - domain:reactive-md
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:combustion
  - keyword:catalysis-surface
  - keyword:graphene-carbon
  - keyword:reaxff-application
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.proci.2018.05.109"
year: 2019
authors:
  - "Muye Feng"
  - "Xi Zhuo Jiang"
  - "Kai H. Luo"
venue: "Proc. Combust. Inst."
pdf_sha256: "88e5f49b73eca69fae481add25410eb4aea25e35ff830d45029a091ba52f1cd5"
pdf_path: "papers/ReaxFF_others/Feng_Luo_ProcCombInst_Methane_Pt_2019.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019muye-proceedings-reactive-molecular -->

## Summary

Platinum-decorated functionalized graphene sheets (Pt@FGS) are proposed as catalytic additives to enhance methane oxidation relevant to catalytic combustion. This Proceedings of the Combustion Institute contribution compares ReaxFF molecular dynamics of methane oxidation in the presence of several Pt/graphene-based motifs to isolate initiation steps, hydrogen-transfer sequences, and support oxidation. The study emphasizes elementary reaction events accessible to reactive MD at high temperature, including C–H activation, hydroxyl formation, and edge oxidation of functionalized graphene.

## Methods

**1 — MD application (ReaxFF methane oxidation with catalyst models).** **ReaxFF** (as implemented in **LAMMPS**, per **§2** of the **Proceedings** paper) uses **C/H/O** parameters for the **uncatalyzed** **CH₄/O₂** **base** case and for **FGS** (**functionalized** **graphene**), and **Pt/C/H/O** parameters for **tetrahedral** **Pt** and **Pt@FGS** cases. All systems share **3D** **PBC** at a **gas-phase** **mass** **density** **0.0325 g cm⁻³** (**~30** **atm**-equivalent initial **pressure** in the text). The **base** **stoichiometry** is **50 CH₄** and **100 O₂** (**ϕ = 1** **mixture**). **Catalyst** constructions: **pristine** **graphene** with **1269** **C** atoms, **FGS** with **16** **oxygen**-bearing **groups** (target **C/O = 13**; **divacancy** **+** **ether**/**hydroxyl** motifs per **SI**), **Pt** and **Pt@FGS** variants as in **Figs. S1**. For **CH₄/O₂ + Pt@FGS** the **box** is **cubic** with **60 Å** sides; other cases adjust **z**-**length** to keep **density** with the **same** **in-plane** **footprint** (per **§2**). **Protocol:** **NVT** for **all** **runs**; **conjugate-gradient** **minimization** first. **Nosé–Hoover** **thermostat** (damping **50 fs**). **Equilibration** at the **start** **temperature** for **100 ps** with **0.1 fs**; for **T > 1000 K** equilibrations, **C–O** and **H–O** **bond** terms in the **field** are **switched** **off** to avoid **spurious** **reactions**; **Pt–O**/**Pt–H** terms likewise **off** in **high-**T **Pt** equilibrations, with **catalysts** and **gas** **equilibrated** **separately** for **FGS**/**Pt@FGS** as described. **Production** uses **0.2 fs** for **4000 ps** **(ramped-**T**)** or **1000 ps** **(fixed-**T**)** segments after equilibration. **Barostat:** **N/A** — **NVT** at **fixed** **cell** **shape**/**volume** after **size** **choices** in **§2** (not **NPT** **fluctuating** **box** in the quoted protocol). **External uniform electric field:** **N/A**. **Replica / enhanced sampling:** **N/A** — reactive **NVT** kinetics at high **T** as a comparative study across catalysts.
## Findings

Pt@FGS provides the strongest catalytic boost among candidates tested, lowering the effective activation barrier by roughly 73% relative to uncatalyzed methane oxidation in their setup (per article abstract/conclusions). Oxidation begins with C–H cleavage and hydroxyl generation; hydrogen transfer between Pt sites and the support sustains a catalytic cycle. Functionalized graphene oxidizes preferentially at edges, increasing oxygen functionality over trajectory time.

Edge-selective oxidation matters for catalyst durability: if supports graphitize or over-oxidize, Pt–support synergy may degrade across repeated ignition cycles—an effect the trajectories begin to capture through oxygen functional group accumulation.

## Limitations

Idealized nanoparticle geometries and high-temperature MD omit detailed coverage effects and experimental transport; quantitative rates require experimental or QM validation.

## Corpus notes

Proceedings DOIs sometimes map to multiple download formats; if the corpus later ingests a journal version, keep `pdf_path`/`pdf_sha256` aligned via `scripts/sync_wiki_paper_frontmatter.py` without merging distinct `paper_id` slugs unless the manifest migration explicitly retires one.

Combustion Institute papers often include supplementary trajectory logs; if those arrive, store pointers under `normalized/papers` rather than embedding huge tables in markdown, keeping the wiki readable in MkDocs exports.

When citing the 73% barrier reduction figure, always include the simulation definition of “effective barrier” used in the proceedings, because it may differ from experimental apparent activation energies.

Tag this page with combustion-relevant theme hubs only when the surrounding context discusses methane oxidation catalysts rather than general hydrocarbon pyrolysis.

## Relevance to group

Demonstrates **ReaxFF** on **methane oxidation** with **metal–carbon** catalyst motifs tied to combustion applications.

## Citations and evidence anchors

- DOI: [10.1016/j.proci.2018.05.109](https://doi.org/10.1016/j.proci.2018.05.109)

## Related topics

- [[reaxff-family]]
