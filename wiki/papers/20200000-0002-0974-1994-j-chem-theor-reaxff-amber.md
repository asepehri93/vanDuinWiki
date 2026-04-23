---
id: paper:20200000-0002-0974-1994-j-chem-theor-reaxff-amber
type: paper
title: "ReaxFF/AMBER: A Framework for Hybrid Reactive/Nonreactive Force Field Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:methods-software
  - domain:reactive-md
  - method:reaxff
  - task:method-development
  - scale:atomistic
paper_keywords:
  - keyword:method-development
  - keyword:reactive-md
  - keyword:enhanced-sampling
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jctc.0c00874"
year: 2020
authors:
  - "Rahnamoun, Ali"
  - "Kaymak, Mehmet Cagri"
  - "Manathunga, Madushanka"
  - "Goetz, Andreas W."
  - "van Duin, Adri C. T."
  - "Merz, Kenneth M. Jr."
  - "Aktulga, Hasan Metin"
venue: "J. Chem. Theory Comput."
pdf_sha256: "8b5ff14f0e30a0bb4501b20577c995da2bd0e3f7f70c48c48a9f90b1a58a84c7"
pdf_path: "papers/Rahnamoun_JCTC_2020_AMBER_ReaxFF.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:20200000-0002-0974-1994-j-chem-theor-reaxff-amber -->

!!! abstract "Scope"

Software/methods paper integrating ReaxFF reactive dynamics into the AMBER molecular dynamics package, with validation on a solvated benzene test case and a Claisen rearrangement potential-of-mean-force example.

## Summary

Bridging fully quantum mechanical treatments and fixed-bond force fields, reactive force fields enable bond-breaking chemistry at scales inaccessible to routine QM/MM with ab initio electronic structure. The manuscript introduces a hybrid ReaxFF/AMBER implementation that exposes ReaxFF chemistry within AMBER’s infrastructure so that local reactivity can be embedded in large biomolecular or solvated organic systems. Benchmarking against related approaches and demonstration of AMBER’s umbrella sampling machinery for an organic reaction in water are central outcomes. The **JCTC** paper targets **workflows** where **biomolecular** **force** **fields** handle **solvent** and **protein** **scaffold** degrees of freedom while **ReaxFF** covers a **localized** **reactive** **region**.

## Methods

**Software integration.** **ReaxFF** is coupled to the **AMBER** MD package so **bond making/breaking** is treated with ReaxFF in a **user-selected reactive zone** while the remainder can use standard **AMBER** **fixed-bond** models—aimed at **large** solvated or biomolecular cells at cost below **QM/MM**.

**Validation (benzene in water).** A **benzene** molecule in **explicit water** tests the **mixed reactive/nonreactive** partitioning against **related approaches** compared in the article.

**Enhanced sampling.** **Umbrella sampling** maps the **Claisen rearrangement** in **aqueous** solution using AMBER’s **PMF** machinery with ReaxFF in the reactive region—the abstract highlights this as a **first** ReaxFF use of AMBER **PMF** for such a reaction profile.

**Implementation detail.** Build/configuration notes, inputs, and benchmarks appear in the **JCTC** article and **Supporting Information** (`pdf_path` in front matter).

**MD application (AMBER production details).** AMBER/ReaxFF runs use **3D** **PBC** **supercells** with **explicit** **solvent**; **solvated** **test** **systems** contain on the order of **10^3** **atoms** for the **benzene** benchmark and a larger **aqueous** cell for the **allyl vinyl ether** **Claisen** system (exact water counts in the *JCTC* article/SI). **N/A —** timestep (fs) not transcribed to this page. **N/A —** equilibration plus production **duration** in **ps**/**ns** for each example: see primary text. **Thermostat** and **barostat** (if **NPT** used in any leg): per article/SI; **NVT**-style sampling is typical for the **Claisen** **umbrella** path reported in the abstract. **Target temperature** near **300 K** is used for the **aqueous** demonstration unless the manuscript specifies a different set point. **N/A —** hydrostatic **pressure** control and **barostat** name where trajectories are strictly **NVT** at 1 atm implicit pressure. **N/A —** applied **electric** **field** during the benchmarks summarized here. **Umbrella** / **PMF** windows: **N/A** for number of **replica** **exchange** **replica**; **Umbrella** **sampling** (enhanced) is the reported rare-event method.

**Force-field training (block 2).** **N/A** — the paper documents **software integration** and validation of existing ReaxFF and AMBER FFs, not a new ReaxFF training protocol.

**Static QM (block 3).** **N/A** for standalone DFT as the main result; the Claisen PMF is ReaxFF-driven in AMBER, not a full *ab initio* MD study.

## Findings

**Outcomes and mechanisms (software).** The **hybrid** engine exposes **ReaxFF** in a user-carved **reactive** **zone** while **AMBER** treats the rest of the **solvent** and **scaffold** with **fixed** **bond** **FF** terms, enabling **interfacial** chemistry in **solvated** **organic** and **biomolecular** **cells** without a full **QM** layer on every **atom**.

**Comparisons.** The **solvated benzene** test tracks **energies** and **geometries** **plausibly** next to **literature** **hybrid** **reactive** / **MM** **protocols** cited in the article. The **Claisen** **umbrella** run yields a **free** **energy** **profile** **consistent** with using **ReaxFF** in place of **higher** **level** **QM** for the **reactive** **subspace**, subject to the **ReaxFF** **training** **scope**.

**Sampling / sensitivity.** The **Claisen** work demonstrates **restraint**-based **umbrella** **sampling** in **AMBER** with **ReaxFF**-level **reactive** **MD**; **sensitivity** of the **barrier** **height** and **well** **depth** to **force** field **partitions** and **water** **model** (e.g. **rigid** vs **flexible** **water**) requires **reoptimization** for each **new** **reaction** class, as the authors **note**.

**Limitations and outlook (authored).** Residual error comes from the **reactive**/**nonreactive** **boundary** placement, **finite** **sampling** in each **umbrella** **window**, and **ReaxFF** **transferability**; **future** **work** in the **JCTC** space typically targets broader **chemistry** in **larger** **assemblies** once this **AMBER** **plumbing** is in place. **Corpus note:** for **definitive** **PMF** **numbers** and **figure** **PMF** **comparisons**, use the **peer-reviewed** **PDF** and **SI**, not this **summary** alone.

## Limitations

Hybrid accuracy depends on force-field boundaries, water models, and sampling convergence; users must validate partitions and barostat/thermostat choices for each new chemistry.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

Method-development contribution extending ReaxFF usability through a major biomolecular MD ecosystem, co-authored by van Duin.

## Citations and evidence anchors

- https://doi.org/10.1021/acs.jctc.0c00874

## Related topics

- [[reaxff-family]]
