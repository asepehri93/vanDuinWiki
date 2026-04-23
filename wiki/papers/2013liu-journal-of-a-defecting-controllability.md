---
id: paper:2013liu-journal-of-a-defecting-controllability
type: paper
title: "Defecting controllability of bombarding graphene with different energetic atoms via reactive force field model"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - material:graphene-carbon-nano
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:dft-static
source_refs: []
doi: "10.1063/1.4817790"
year: 2013
authors:
  - "Xiao Yi Liu"
  - "Feng Chao Wang"
  - "Harold S. Park"
  - "Heng An Wu"
venue: "Journal of Applied Physics"
pdf_sha256: "51948ecf3e167df9021aff390605b0bc9c057a194dd8c9bca2146688c4515a8f"
pdf_path: "papers/ReaxFF_others/Liu_JAP_Fe_O_Au_graphene_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2013liu-journal-of-a-defecting-controllability -->

## Evidence and attribution

!!! note "Evidence"

    Prose below summarizes the **peer-reviewed article** (**DOI `10.1063/1.4817790`**). The normalized **`pdf_path`** filename contains “2018” while front matter **`year`** follows the **journal** assignment (**2013**); resolve any mismatch against the **PDF** in your checkout.

## Summary

**ReaxFF MD** simulates **bombardment** of **suspended monolayer graphene** by **different energetic atoms**, emphasizing how **impact site**, **projectile chemistry**, and **incident energy** control **defect probability**, **quality** (vacancy vs substitution), and **controllability**. Comparisons to **DFT** motivate rules tying **electron density** and **bond order** to **defect outcomes**. An **energy spectrum** narrative argues that **single vacancies** vs **direct substitution** can be selected by tuning **energy** and projectile choice. **Ion** **irradiation** is a **scalable** route to **defect** **engineering** in **2D** materials for **transport** and **magnetism** studies, but **empirical** **knobs** need **atomistic** guidance to avoid **uncontrolled** **amorphization** (introduction themes).

## Methods

**Classical MD** with **ReaxFF** treats **C–C** and **C–projectile** interactions using literature **Fe/C**, **Au/C**, and **O/C** parameter sets (cited in the paper), enabling bond breaking/formation during **bombardment** of **suspended monolayer graphene**. Simulations sweep **impact site**, **projectile species**, and **incident energy**; selected outcomes are compared to **DFT** to interpret **defect** types and **bond-order** trends.

**Statistics:** multiple **impact replicas** at each condition are used in the article to estimate **defect probabilities** and **distributions** (figures in the full paper).

**MD protocol details not in p1–2 extract:** **Engine (LAMMPS or other):** **N/A —** not named on **`normalized/extracts/2013liu-journal-of-a-defecting-controllability_p1-2.txt`**. **Ensemble:** **N/A —** whether bombardment **production** uses **NVE**, **NVT**, or **NPT** is **not** in the indexed excerpt. **Supercell atom counts / PBC / timestep / duration / thermostat / barostat / temperature / pressure / electric field / enhanced sampling:** **N/A —** not restated here; read **`papers/ReaxFF_others/Liu_JAP_Fe_O_Au_graphene_2018.pdf`** (**DOI `10.1063/1.4817790`**) for authoritative numerics.

**2 — Force-field training:** **N/A —** the study **uses** literature **Fe/C**, **Au/C**, and **O/C** ReaxFF descriptions for projectiles; it does not report a **new** fit.

**3 — Static QM / DFT:** **DFT** comparisons are used to interpret **defect** types and **electron-density** / **bond-order** trends as stated in the abstract/introduction; **functional/basis/k-mesh** choices belong in the article’s **Methods** section, not inferred here.

## Findings

**Defect probability**, **quality** (e.g., **pristine vacancies** vs **direct substitution**), and overall **controllability** depend jointly on **impact location**, **projectile chemistry**, and **energy**. Compared with **DFT**, **vacancy** formation is associated with regions of **high electron density** in the pristine sheet, while **bond order** of **projectile–C** bonds correlates with whether **vacancies** or **substitutions** dominate. The authors summarize an **energy–projectile** “spectrum” arguing that **single vacancies** and **direct substitution** can be selected in distinct **energy windows** for suitable projectiles.

**Design implication:** the paper frames **projectile** choice as a **chemical knob** partly **orthogonal** to **incident energy**, supporting **orthogonal** tuning of **defect class** when **beam** parameters are set jointly (discussion framing in the article).

**Comparisons:** **DFT** is used alongside **ReaxFF** to relate **vacancy** formation to regions of **high electron density** and to tie **bond order** of **projectile–C** bonds to **vacancy** vs **direct-substitution** outcomes (indexed introduction).

**Sensitivity / design levers:** **Impact site**, **projectile species**, and **incident energy** jointly control **probability**, **quality**, and **controllability** of defects; the abstract summarizes an **energy–projectile** “spectrum” for selecting **single vacancies** vs **direct substitution**.

**Limitations and outlook:** Hypervelocity chemistry and **electronic excitations** are classic caveats for **classical** bombardment models; **suspended monolayer** setups omit **substrate** dissipation present in **supported** samples (see **## Limitations** below).

**Corpus honesty:** **`pdf_path`** uses a filename containing **“2018”** while **`year: 2013`** follows the **journal** metadata; resolve any mismatch against the **PDF** bytes in your checkout. Do not cite **simulation numerics** from this wiki without confirming the **full** **JAP** **Methods** section.

## Limitations

Classical treatment of hypervelocity impacts may miss electronic excitations; statistics depend on number of repeated impacts.

**Suspended** **monolayer** **models** omit **substrate** **dissipation** channels present in **supported** **samples**, which can change **defect** **yields** at comparable **projectile** **energy**.

**Engineering** **readout:** the paper’s **controllability** discussion is aimed at **irradiation** **patterning** of **2D** films—use **statistics** across **impact** sites when designing **beam** **doses** (discussion emphasis).

**Replication:** when **re-running** **similar** **bombardment** studies, archive **random** **seeds** and **impact** **parameter** **tables** alongside **trajectories** for **reproducibility** (good practice for **MD** **irradiation** work).

## Reader notes (navigation)

- [[reaxff-family]]
- [[graphene-nanocarbon]]
