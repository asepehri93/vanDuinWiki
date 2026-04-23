---
id: paper:2019akbarian-venue-paper
type: paper
title: Atomistic-scale insights into the crosslinking of polyethylene induced by peroxides
  (uncorrected proof PDF)
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:organics-polymers-pyrolysis
- domain:reactive-md
- method:reaxff
- task:experiment-integrated
- material:polymer-organic
paper_keywords:
- keyword:polymer
- keyword:reaxff-application
- keyword:validation-experiment
- keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: 10.1016/j.polymer.2019.121901
year: 2019
authors:
- Dooman Akbarian
- Hossein Hamedi
- Behzad Damirchi
- Dundar E. Yilmaz
- Katheryn Penrod
- W. H. Hunter Woodward
- Jonathan Moore
- Michael T. Lanagan
- Adri C. T. van Duin
venue: Polymer (uncorrected proof in corpus)
pdf_sha256: c128df98bbc5b2a05fe5a2c07be2a1a8ab22dcac896bf178fb419786bf14010e
pdf_path: papers/Akbarian_Polymer_2019_proof.pdf
extraction_quality: partial
group_affiliation: true
---
<!-- id:paper:2019akbarian-venue-paper -->

## Summary

**ReaxFF MD** plus **FTIR mapping** and **WAXS** probe **peroxide-induced cross-linking** of **polyethylene** relevant to **HV cable XLPE**. The study focuses on **dicumyl peroxide (DCP)** chemistry, **byproduct** formation, and how **temperature**, **density**, **DCP loading**, **electric field**, and **alternative peroxides** modulate **cross-link yield**. **Cable** **insulation** reliability depends on **uniform** **cure** and **low** **void** content; **atomistic** models here isolate how **peroxide** **fragmentation** and **radical** **recombination** channels compete before **continuum** **processing** maps are attempted.

## Methods

- **Reactive MD:** **ReaxFF** simulations of **PE** with **peroxide** curing agents under varied **thermal** and **density** conditions (abstract).
- **Experiments:** **FTIR** spatial mapping and **WAXS** to corroborate **cross-linking** extent and **phase** features (abstract).
- **Sweeps:** **Curing temperature** (noting **~500 K** as a practical optimum in abstract before **over-curing**), **system density**, **DCP:PE ratio**, applied **electric field**, and comparison of **DCP** vs **di-(1-decyl-1-phenylundecyl) peroxide** efficiency (abstract).
- **Spatial FTIR** interpretation ties **carbonyl** and **unsaturation** signatures to **under-cured** versus **over-cured** regions when available in the article figures.

**MD application.** **ReaxFF** **molecular dynamics** in **LAMMPS** on **3D** **PBC** **polyethylene**/**peroxide** **supercells** with **atom**/**stoichiometry** **details** on **`[[2019akbarian-polymer-183-atomistic-scale-insights]]`**. **NVT** **protocol:** **2.25 ns** **equilibration**, **0.25 fs** **timestep**, **Berendsen** **thermostat** (**100 fs** **damping**). **Barostat / pressure:** **N/A —** these **NVT** **state-point** **runs** are **constant-volume** **sampling** without a **NPT** **barostat** (no independent **hydrostatic pressure** **control** in the quoted **NVT** **equilibration** **blocks**). The **uncorrected proof** here is for **line-numbered** **QA**; copy **integrator** settings from the **VOR** **PDF** for **external** **citations**.
## Findings

- **Temperature:** Raising cure temperature toward **~500 K** increases **cross-linking**, but **>500 K** can **hurt** cross-link quality (abstract).
- **Density:** **Higher density** promotes **cross-linking** (abstract).
- **DCP stoichiometry:** **Large DCP excess** raises **byproducts** without necessarily increasing **XLPE** yield (abstract).
- **Field:** Simulations report **negligible** influence of an **external electric field** on cross-linking under their protocol (abstract).
- **Peroxide choice:** The **alternative peroxide** explored is **less efficient** than **DCP** for **XLPE** in their comparison (abstract).
- **Byproduct** channels are highlighted where **excess** **initiator** drives **scission** or **oxidation** side chemistry that **does not** contribute to **gel** fraction gains.

## Limitations

**Uncorrected proof** PDF—prefer **`[[2019akbarian-polymer-183-atomistic-scale-insights]]`** for the **version-of-record** path when available. Industrial **XLPE** recipes contain many additives not modeled atomistically here.

**Curation note:** the **Elsevier** proof may interleave **queries**; do not treat **placeholder** **pages** as **final** **pagination** for external citations—use the **VOR** sibling above when possible. **FTIR** **maps** in the article are the primary **experimental** anchor for **spatial** **heterogeneity** in **cure** quality. **WAXS** traces supplement **FTIR** by indicating **crystallinity** changes when **cross-links** **pin** **chains** differently across **temperature** ramps. **DCP** **stoichiometry** sweeps in the abstract bracket **practical** **cable** **recipe** windows without claiming **industrial** **batch** **reproducibility**.

## Relevance to group

Integrates **ReaxFF polymer chemistry** with **industrial** (Dow) **analytics** for **dielectric** materials aligned with **power cable** research.

## Citations and evidence anchors

- DOI: [10.1016/j.polymer.2019.121901](https://doi.org/10.1016/j.polymer.2019.121901)

## Reader notes (navigation)

- **Corpus catalog (non-primary PDFs):** [Non-primary article PDF slugs (GitHub)](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md)
- Canonical article page when curated: [[2019akbarian-polymer-183-atomistic-scale-insights]]

## Related topics

- [[reaxff-family]]
