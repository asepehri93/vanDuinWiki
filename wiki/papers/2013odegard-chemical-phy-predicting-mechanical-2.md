---
id: paper:2013odegard-chemical-phy-predicting-mechanical-2
type: paper
title: "Predicting mechanical response of crosslinked epoxy using ReaxFF (duplicate PDF)"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:mechanics-tribology
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:application
  - task:validation
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:lammps
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:validation-experiment
  - keyword:reactive-md
source_refs: []
doi: "10.1016/j.cplett.2013.11.036"
year: 2014
authors:
  - "Gregory M. Odegard"
  - "Benjamin D. Jensen"
  - "S. Gowtham"
  - "Jianyang Wu"
  - "Jianying He"
  - "Zhiliang Zhang"
venue: "Chemical Physics Letters"
pdf_sha256: "bbf0817e0dd40cd2fda1ddb84c74f68da98c9a86a469667b27cf61aeab172c6c"
pdf_path: "papers/ReaxFF_others/ZZ-J092-2014-Chem_Phys_Lett_Predicting mechanical response of crosslinked epoxy using ReaxFF.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013odegard-chemical-phy-predicting-mechanical-2 -->

## Evidence and attribution

!!! note "Evidence"

    This ingest is a **second PDF bytes** for the same **Chemical Physics Letters** letter (**DOI `10.1016/j.cplett.2013.11.036`**). Curated summary: **`[[2013odegard-chemical-phy-predicting-mechanical]]`**.

## Summary

This wiki entry documents a **second corpus PDF** (different path and SHA-256) for the same **Chemical Physics Letters** article (**DOI `10.1016/j.cplett.2013.11.036`**, **2014**, **591**, **175–178**). The letter uses **ReaxFF molecular dynamics** to predict **elastic stiffness** and **yield** for **crosslinked epoxy** built from **EPON 862** cured with **DETDA**, comparing to **experimental** mechanical data on the same chemistry. The scientific question is whether a **transferable** **hydrocarbon-oriented** **ReaxFF** parameterization—already used for **polymer** **mechanics** elsewhere—can describe **covalent network** epoxy **response** without refitting every **new** **thermoset** formulation. The authors report that, despite a large **strain-rate** gap between **MD** and **experiment**, **elastic** and **yield** responses **align closely**, supporting reuse of the cited **ReaxFF** set for **bulk epoxy** in the scope tested. Full section-level detail and evidence anchors: **`[[2013odegard-chemical-phy-predicting-mechanical]]`**.

## Methods

Scientific protocol matches the primary page: **EPON 862** and **DETDA** at **2:1** stoichiometry; **five** independent crosslinked samples (**4284** **atoms** each) constructed in **LAMMPS** starting from **OPLS-AA**-relaxed melts under **3D periodic** (**PBC**) **bulk** cells, **uniaxial compression**, and **`fix bond/create`**-driven **epoxide–amine** crosslinking to target experimental **cure** stoichiometry, followed by **ReaxFF** (**Liu et al.** parameterization as cited on the canonical page) **equilibration** and **NPT** relaxation at **300 K** with a **Berendsen barostat**, then **deformation** protocols to extract **Young’s modulus**, **yield stress**, and **stress–strain** trends compared to **mechanical test** data. This slug’s **`pdf_path`** is the alternate bytes under `papers/ReaxFF_others/`; for **timestep**, **damping**, **strain rate**, and **figure** references, use **`[[2013odegard-chemical-phy-predicting-mechanical]]`**.

**Electric field / enhanced sampling:** **N/A —** same **DOI** study as the canonical page; not a focus of the **Chem. Phys. Lett.** letter.

## Findings

**ReaxFF** **MD** predicts **elastic stiffness** and **yield** in **close agreement** with **measured** properties for this **EPON/DETDA** formulation in the letter’s comparison; the authors frame **elastic** and **yield** **metrics** as **trackable** across **simulation** and **experiment** even though **MD** accesses much higher **strain rates** than typical **test** coupons. **Failure** morphology and **ultimate strain** limits may still differ from **experiment** where **defects**, **rate-dependent plasticity**, and **submicron heterogeneity** matter—topics the primary page discusses with fuller **figure** grounding. For quantitative **moduli** and **yield** values, use **`[[2013odegard-chemical-phy-predicting-mechanical]]`**.

**Corpus honesty:** **Duplicate PDF bytes** for the same **DOI**; see **`docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`** entry **2013odegard-chemical-phy-predicting-mechanical-2**.

## Limitations

This slug tracks **alternate PDF bytes** only: **figure resolution**, **font embedding**, and **pagination** can differ from the file used on the **canonical** wiki page. Operators should not treat **`pdf_sha256`** here as interchangeable with the **primary** ingest when auditing **manifest** rows. Any **SI** tables or **error bars** on **experimental** moduli belong to the **same** **DOI** but may be easier to cite from whichever PDF your workflow opened first.

## Relevance to group

Demonstrates **ReaxFF** applied to **thermoset** **mechanics** with **experimental** validation—useful cross-link for **polymer** **mechanics** and **reactive** **FF** **transferability** discussions adjacent to combustion and oxide work elsewhere in the corpus.

## Reader notes (navigation)

- **Corpus catalog (duplicate PDF bytes):** [Non-primary article PDF slugs](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md) (entry **2013odegard-chemical-phy-predicting-mechanical-2**)
- Canonical narrative and hashes: [[2013odegard-chemical-phy-predicting-mechanical]]
- [[reaxff-family]]
