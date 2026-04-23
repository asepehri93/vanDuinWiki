---
id: paper:2021pols-venue-paper
type: paper
title: "Supporting Information: Atomistic insights into the degradation of inorganic halide perovskite CsPbI3 (ReaxFF MD)"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - material:perovskite-oxide
  - task:application
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: ""
year: 2021
authors:
  - "Mike Pols"
  - "José Manuel Vicent-Luna"
  - "Ivo Filot"
  - "Adri C. T. van Duin"
  - "Shuxia Tao"
venue: "Supporting Information PDF (see primary article)"
pdf_sha256: "0b7ed0316ffe7002d3e7b0ed2fa5b0c84c1fa71c51f00adfaf985ff2876fd1a0"
pdf_path: "papers/Pols_JPC_Letters_CsPbI3_perovskiites_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2021pols-venue-paper -->

!!! note "Corpus note"
    This path registers the **Supporting Information** PDF for the *J. Phys. Chem. Lett.* study on **CsPbI₃** degradation with **ReaxFF MD**. The **main article** is **`[[2021mike-pols-j-phys-chem-atomistic-insights]]`**.

## Summary

**CsPbI₃** is an **inorganic halide perovskite** with attractive **optoelectronic** properties but **environmental** sensitivity; **atomistic** insight into **decomposition** pathways helps interpret **stability** experiments. The SI package **`papers/Pols_JPC_Letters_CsPbI3_perovskiites_SI.pdf`** accompanies the letter **“Atomistic Insights Into the Degradation of Inorganic Halide Perovskite CsPbI₃: A Reactive Force Field Molecular Dynamics Study.”** It expands on **DFT benchmarking**, **training-data** tables for the **ReaxFF** fit, **MD protocol** details (integration, ensembles, analysis of **diffusion** and **defect** populations), and **supplementary figures** on **phase behavior**, **lattice metrics**, and **degradation pathways** referenced from the main text. This wiki entry exists so manifests can point at the **SI blob** while narrative science remains centralized on the **primary JPCL** page.

## Methods

`pdf_path` registers the **Supporting Information** PDF for *J. Phys. Chem. Lett.* **12**, **5519**–**5525** (parent DOI **10.1021/acs.jpclett.1c01192**). The **narrated** article is **[[2021mike-pols-j-phys-chem-atomistic-insights]]**. The **SI** **contains** the **ReaxFF** **parameter** **file**, **extra** **DFT** **convergence** and **reaction** **set** **tabulations** used in the **MC** **fit** (**AMS** **2020**), and **ReaxFF**+**LAMMPS** **molecular** **dynamics** **protocols** in **3D** **PBC** **perovskite** **supercells** (atom **counts** in **the** **tables**) with **NVT**/**NPT** **molecular** **dynamics** **at** **stated** **temperatures** in **K** (e.g. **100**–**700** **K** **phase** **sweeps** and **450**–**700** **K** **defect** **diffusion** in the **parent** **text**) and **(where** **given)** **atm-scale** **pressure** **(bar)** **for** **NPT** **self**-**diffusion** **blocks**; **fs**-scale **timestep**, **Nosé**–**Hoover**/**Berendsen**-class **thermostat**/**barostat** **families**, **ps**–**ns** **equilibration**/**production** **lengths** — read **this** **SI** **+** the **parent** **letter**; **N/A** to **re-key** them **here** without **re-opening** the **Blob**. **Cite** the **letter**; **`doi`** in **YAML** is **empty** for this **SI**-**only** **slug** by **design**.

## Findings

**SI** **role** **only:** **tabulated** **PBE+**-**D3** **VASP** **training** **agreement**, **extra** **E\(_\mathrm{EOS}\)**, **RDF**/**MSD**/**D(T)** **plots** **for** **iodine** **defect** **dynamics** **(450**–**700** **K** **NPT** **in** the **parent** **note)**, and **decomposition** **snapshots** at **600** **K** **(letter)** **as** **expanded** **in** the **supplement** **/ Supporting** **Notes** **1**–**3** **(see** `pdf_path` **PDF)**. **Narrated** **science** **(phase** **kinetics**, **decomposition** **pathways)**: **read** `[[2021mike-pols-j-phys-chem-atomistic-insights]]` **not** **this** **file** in **isolation**.

**Corpus** **/ KB** **honesty** **(SI-only** **slug)**: no **new** **mechanistic** **number** not **also** in **VOR+SI** **+** `pdf_path` **source**.

## Limitations

If your pipeline needs **simulation-ready** inputs, extract **force field** parameters, **cutoff** settings, and **charge** equilibration rules from the **SI** tables rather than from this wiki note. **Partial** extraction in the corpus may omit long SI sections—open the **PDF** for completeness. **`doi`** is blank here because the SI file shares the **parent DOI**; cite the **letter**. Category **A** SI in [`NON_PRIMARY_ARTICLE_PAPER_SLUGS.md`](https://github.com/asepehri93/vanDuinWiki/blob/main/docs/corpus/NON_PRIMARY_ARTICLE_PAPER_SLUGS.md).

**Confidence rationale:** `med`—SI pointer page.

## Reader notes (navigation)

When updating **normalized** records for this slug, keep **`pdf_sha256`** aligned with the **SI** file on disk and ensure **`wiki_path`** points here while **`bibliography.doi`** still reflects the **parent** **JPCL** entry.

- Primary letter: [[2021mike-pols-j-phys-chem-atomistic-insights]]
- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
- [[docs/benchmarks/WARMUP_CANDIDATE_QUESTIONS.md|Phase 0 warmup questions]]

## Related topics

- [[2021mike-pols-j-phys-chem-atomistic-insights]]
- [[reaxff-family]]
