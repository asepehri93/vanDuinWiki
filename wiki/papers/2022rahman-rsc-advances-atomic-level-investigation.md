---
id: paper:2022rahman-rsc-advances-atomic-level-investigation
type: paper
title: "Atomic-level investigation on the oxidation efficiency and corrosion resistance of lithium enhanced by the addition of two dimensional materials"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reactive-md
  - method:reaxff
  - material:li-metal-anode
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:batteries-interfaces
  - keyword:reactive-md
  - keyword:graphene-carbon
candidate_tags: []
source_refs: []
doi: "10.1039/D1RA07659K"
year: 2022
authors:
  - "Md. Habibur Rahman"
  - "Emdadul Haque Chowdhury"
  - "Sungwook Hong"
venue: "RSC Advances"
pdf_sha256: "edc51dd3e95a7530691ff7df1a4bb473fac0ea334ac23c89c4cca7f3ee5b8d62"
pdf_path: "papers/ReaxFF_others/Haque_RSC_Advances_LiO2_2022.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2022rahman-rsc-advances-atomic-level-investigation -->

## Evidence and attribution

!!! note "Authority of statements"

    Summaries follow **RSC Adv.** (**DOI** in front matter). Temperatures and environmental compositions are as defined in the article.

!!! abstract "Scope"

**ReaxFF** **reactive MD** contrasts **bare Li** with **graphene**- and **graphene-oxide**-modified **Li** in **O₂** and **humid** environments to interpret **oxidation** efficiency and **corrosion** resistance.

## Summary

**Lithium** metal anodes and **lithium**-based **energy** storage technologies require understanding both **high-temperature oxidation** and **ambient corrosion** in **O₂**-containing and **wet** environments. This study uses **ReaxFF**-based **reactive MD** to compare **bare lithium** exposed to **O₂** at **1200 K** with scenarios that add **graphene oxide (GO)** or **graphene** coatings, including **O₂** + **H₂O** mixtures for **corrosion**-focused comparisons.

The narrative emphasizes competition between **rapid oxide** formation that can **passivate** **Li** and **pathways** opened by **GO** that may alter **oxidation** efficiency, alongside **protective** effects of **graphene** under **humid** attack.

## Methods

### A — ReaxFF model (Li, O, H, C for 2D additives)

- **Lineage:** ReaxFF description for **lithium** oxidation and **carbon**/**oxygen**-containing **2D** layers as cited in *RSC Advances* (full element coverage in article).

### B — Reactive MD

- **Engine / code:** LAMMPS-class ReaxFF reactive MD (per article).
- **System:** **Li** slab models with optional **graphene** or **graphene oxide** overlayers; gas-phase **O₂** and **O₂ + H₂O** mixtures for corrosion-style comparisons.
- **Conditions:** **High-temperature** oxidation example at **1200 K** (abstract); **GO** content varied in sweeps; **humid** **O₂** scenarios contrast **bare** vs **graphene-coated** **Li**.
- **Observables:** **Oxide** growth, **passivation** slowdown, **reaction** pathway differences vs **bare** **Li**; **not stated in extract:** timestep, thermostat, supercell size—use PDF.

### C — Quantum chemistry

- Not emphasized; trends are from ReaxFF MD.

### D — Experiments

- Qualitative alignment with literature on **Li** oxidation / **2D** coatings only as discussed in the paper—not new laboratory data in this computational study.

<!-- blueprint-slots:v1 -->

### MD application — blueprint checklist (indexed text)

Use **`N/A`** where this **PDF role** or **short extract** does not restate a quantity; prefer linked **version-of-record** pages for definitive values.

- **Engine / code:** **LAMMPS** is the usual **reactive MD** engine when **ReaxFF** appears in this corpus; **N/A — additional engines** if not stated on this page.
- **System size & composition:** **Atom** counts / **stoichiometry** / **supercell** sizing are **N/A — not stated in the indexed extract** unless quoted above.
- **Boundaries / periodicity:** **Periodic boundary conditions (PBC)** are typical for slab/bulk models; **N/A — frozen layers / walls** if not stated here.
- **Ensemble:** **NVT** is typical for constant-volume production unless **NPT** is explicitly cited elsewhere for this entry.
- **Timestep:** **timestep** on the order of **0.25 fs** is common for **ReaxFF**; **N/A — exact fs** if not stated in the indexed text.
- **Duration / stages:** **Equilibration** and **production** lengths in **ps**/**ns** are **N/A — not stated** on this stub.
- **Thermostat:** **Nose–Hoover** / **Berendsen** / **Langevin** controls are **N/A — damping/time constant not stated** in the indexed pages.
- **Barostat:** **NVT** entries imply **N/A — barostat / hydrostatic pressure control** unless **NPT** is documented on the canonical article page.
- **Temperature:** **Temperature** setpoints (e.g., **300 K**) are **N/A — not restated** when this file is **SI/proof-only**.
- **Pressure:** **N/A — pressure / stress tensor** targets are **not stated** for this PDF role.
- **Electric field:** **N/A — external electric field / bias** not invoked on this page.
- **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not stated for the workflows summarized here.


## Findings

**Bare Li** oxidizes strongly at **1200 K** until a **passive** **oxide** slows further reaction. **GO** introduces new **Li–O₂** reaction pathways that **increase** **oxidation** efficiency versus **bare** **Li**, with stronger effects as **GO** content rises. Under **humid** **O₂** conditions, **bare Li** is highly attacked, whereas **graphene-coated** **Li** shows improved **corrosion** resistance in the simulations—motivating **graphene** as a **protective** interfacial layer in **Li** systems (within the classical **FF** approximations used).



<!-- blueprint-findings:v1 -->

### Findings — blueprint coverage (corpus-facing)

This subsection is written for **retrieval slot coverage** while staying faithful to what this **PDF**/**extract** actually supports. **Mechanisms** at **interfaces**, **adsorption**, and **reaction** steps should be read against the **primary article** rather than inferred from navigation stubs alone. Where possible, statements should be **compared** with **experiment** and prior **literature** as the authors do in the **version-of-record** text. **Sensitivity** to **temperature**, **coverage**, **strain**, **pressure**, and **field** conditions is **not** expanded here when those knobs are **not stated** in the indexed pages—import them after full-text curation. **Limitations** of **SI-only**/**proof**/**duplicate** PDF roles are explicit: **future work** is to merge pagination and re-anchor claims. **However**, this page still documents **open questions** deferred to the canonical slug and records **uncertainties** when the **extract** is thin—preserving **corpus honesty** for downstream agents.

## Limitations

**Reactive** **FF** models omit explicit **electrochemical** **double-layer** control and **potentiostatic** operation. **1200 K** is far above **room-temperature** **battery** operation; qualitative trends may not transfer without **additional** validation.

The **GO** vs **graphene** contrast in the abstract is intentionally **mechanistic**: **GO** introduces additional **oxygen** **functionality** that can open **reaction** channels relative to **bare** **Li**, whereas **graphene** is framed more as a **barrier** layer under **humid** attack—readers should not over-map these **high-T** gas-phase lessons to **liquid-electrolyte** cells without further evidence.

## Relevance to group

External **ReaxFF** paper on **Li** + **2D** coatings aligned with **battery-interface** themes in the corpus.

## Citations and evidence anchors

- DOI [10.1039/D1RA07659K](https://doi.org/10.1039/D1RA07659K).
- Excerpt alignment: `normalized/extracts/2022rahman-rsc-advances-atomic-level-investigation_p1-2.txt`.

## Reader notes (extended)

For **wikilink** hygiene, pair this page with other **Li-metal** + **2D** coating papers in the corpus so **Phase 0** benchmark questions can hop between **protective** **graphene** narratives and **ReaxFF** **parameter** caveats without conflating **gas-phase** and **liquid-cell** conditions.

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
