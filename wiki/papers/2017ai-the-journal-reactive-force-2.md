---
id: paper:2017ai-the-journal-reactive-force-2
type: paper
title: "A reactive force field molecular dynamics simulation of nickel oxidation in supercritical water"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:alloys-metallurgy
  - domain:reactive-md
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:metallic-systems
  - keyword:water-interfaces
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.supflu.2017.10.025"
year: 2017
authors:
  - "Liqiang Ai"
  - "Yusi Zhou"
  - "Haishen Huang"
  - "Yongjun Lv"
  - "Min Chen"
venue: "J. Supercrit. Fluids"
pdf_sha256: "6df5ba12a98ec8418a9f8320a5981471e486154fb75128752f072f52b7dd208f"
pdf_path: "papers/ReaxFF_others/Ai_NiO_supercritical_JSupFluids_2018.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2017ai-the-journal-reactive-force-2 -->

## Summary

Ai et al. investigate **nickel oxidation in supercritical water (SCW)** using **ReaxFF molecular dynamics**, motivated by **corrosion** of **Ni-based alloys** in **fossil and nuclear** plants operating toward higher steam temperatures. The abstract reports simulations spanning **300–800 °C** and **water densities 26–164 kg m⁻³**, tracking **water adsorption**, **dissociation**, **deprotonation**, and **Ni hydroxylation/oxidation**. The article positions **SCW** as a stronger **oxidizing** environment than ambient liquid water for the conditions sampled, and analyzes **charge evolution** during **deprotonation** to argue that **homolytic** water cleavage becomes more plausible at **high temperature** and **relatively low density** than **heterolytic** pathways familiar near ambient conditions.

## Methods

Alternate **`pdf_path`** (`papers/ReaxFF_others/Ai_NiO_supercritical_JSupFluids_2018.pdf`) for **DOI `10.1016/j.supflu.2017.10.025`**; scientific protocol matches **`[[2017ai-the-journal-reactive-force]]`** (**§2**). **LAMMPS** runs employ **Assowe Ni–O–H ReaxFF** on a **28.896 × 28.896 × 51.896 Å³** **Ni + SCW** cell (**968–1078 atoms** by facet, **Table 1**), **PBC** in **x/y**, **reflecting-wall** **z** closure, **NVT** **Berendsen thermostat**, **Δt = 0.25 fs**, and **4,000,000-step (~1 ns)** production segments at **supercritical water** conditions spanning roughly **300–800 °C** and **26.1–164 kg m⁻³** as in the abstract. **Bulk SCW** **NPT** segments (**~0.25 ns** each) support **EOS** comparisons (**Fig. 4**). **CASTEP PBE** (**571 eV**, ultrasoft **PP**) supplies **QM** spot checks. The **interface** leg is **NVT** (**no barostat** there); **electric fields** and **replica / enhanced sampling** are **not** used.

## Findings

Trajectory analysis tracks **adsorption → dissociation → hydroxylation → oxide** with **interfacial charge** evolution; **SCW** is portrayed as a **stronger oxidizer** than **ambient liquid water** for the sampled **temperature**–**density** grids, with bond metrics (**Ni–O**, **O–H** cutoffs in **§3**) used to follow **reaction** progression. **Compared** to near-ambient interfaces, the authors argue **rate** increases with **temperature** and fluid **density** in the studied regime. **CASTEP PBE** spot checks in **§2** support qualitative energetics but are **not** an exhaustive **benchmark** of all **oxide** stoichiometries. **Limitations** include staying within the **Assowe** training manifold and short **production** windows (**~1 ns** per state in **§2**). This duplicate **`pdf_path`** should defer **pagination**-locked claims to **`[[2017ai-the-journal-reactive-force]]`** when needed.

## Limitations

**ReaxFF** accuracy depends on **training** scope; **SCW** chemistry pushes **bond rearrangements** that should be spot-checked against **QM** where feasible. This slug is **corpus bookkeeping** for an alternate **`pdf_path`**; use **`[[2017ai-the-journal-reactive-force]]`** when **pagination** must match a specific PDF hash, and prefer **one** primary narrative for citations unless provenance requires both digests.

**Confidence rationale:** `med`—duplicate ingest; core claims from abstract/extract.

## Reader notes (navigation)

- Sibling PDF: [[2017ai-the-journal-reactive-force]]
- [[reaxff-family]]
- [[theme-reactive-md-corpus]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2017ai-the-journal-reactive-force]]
- [[reaxff-family]]
