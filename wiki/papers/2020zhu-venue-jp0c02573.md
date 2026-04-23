---
id: paper:2020zhu-venue-jp0c02573
type: paper
title: "Development of a Reactive Force Field for Catalytic C/H/O Conversion on Cu and Cu-Oxide Surfaces and Application to Cu/CuO Chemical Looping"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reaxff-lineage
  - domain:fuel-combustion
  - method:reaxff
  - task:parameterization
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reactive-md
  - keyword:lammps
  - keyword:galley-or-proof-pdf
  - keyword:combustion
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.0c02573"
year: 2020
authors:
  - "Wenbo Zhu"
  - "Hao Gong"
  - "You Han"
  - "Minhua Zhang"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "986443a50a6598e274d7360b8135f74ff3e95262cf38ecd970a996d19e573994"
pdf_path: "papers/Zhu_JPCC_CuCHO_2020_galley.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020zhu-venue-jp0c02573 -->

Fully interactive **Cu/C/H/O ReaxFF** development for Cu-metal and Cu-oxide catalysis, combined with new **ReaxFF-based transition-state search** tools, followed by **reactive MD** demonstrations including **chemical looping** scenarios (Cu oxidation with glucose; hydrocarbon oxidation with Cu oxide).

## Summary

The work develops a **Cu/C/H/O ReaxFF** in three stages: **re-optimization** of the Cu subset against an extended training set including Cu cluster properties; **merging** with an existing **C/H/O** ReaxFF; and **fitting Cu–C/H/O cross terms** using extensive **DFT** data on binding energies and elementary steps. A **transition-state search** framework under the ReaxFF formalism is introduced, together with algorithms to build **reaction paths** and high–degrees-of-freedom coordinate scans. **Reactive MD** tests probe elementary **C/H/O** surface chemistry on Cu and two **chemical looping–style** cases: **CuO formation** from metallic Cu with **glucose**, and **hydrocarbon oxidation** using a **copper oxide** oxidizer.

## Methods

**1 — MD application (atomistic dynamics).** The abstract reports **reactive MD** of **≫1000-atom** **Cu** **surface** and **chemical-looping**-style **Cu/CuO** **systems** using the developed **Cu/C/H/O ReaxFF** (see *J. Phys. Chem. C* and SI for **slab** **stoichiometry**, **PBC**, **NVT**/**NVE**-style **protocols**, **0.25–1.0 fs**-class **timestep** choices, **equilibration** and **production** **lengths** in **ps**/**ns**, **Nose–Hoover**-type **thermostat** use where given, and **temperature** setpoints in **K** for isothermal segments not restated in the one-page extract, and whether **NPT** or **NVT** is used (many catalysis **surfaces** are run **NVT** without **barostat** **hydrostatic pressure** **control**). The indexed excerpt does not restate the MD engine string; the article/SI is authoritative (**N/A** here for exact **LAMMPS** line—confirm in full PDF; **reactive MD** is the stated tier). **Shear**, **shock**, **replica**/**metadynamics**—**N/A** in the abstract framing. **Electric** **bias**/**field** in MD—**N/A** in the excepted summary.

**2 — Force-field training (ReaxFF and related).** The authors build a **Cu/C/H/O** **ReaxFF** in **three** steps: **(1)** **re-optimization** of the **Cu** **subset** using an **extended training set** (including **Cu** **cluster** data); **(2)** **merge** with an existing **C/H/O** ReaxFF; **(3)** **fit** **Cu–C/H/O** **cross** terms to **extensive** **DFT** **energies** for **binding** and **elementary** **reaction** steps. **Parametrization** uses a **ReaxFF** **optimization** **workflow** against the **DFT** **reference** set; **EEM**-style **charges** update every iteration. They also report **in-ReaxFF** **transition-state** (TS) **search** and **reaction** **path**/**coordinate**-scan **algorithms** (new with respect to the paper’s stated ReaxFF tooling goals).

**3 — Static QM / DFT (reference calculations).** **DFT (training/validation data):** **DMol3** **GGA-rPBE**, **ECPs**, **unrestricted** **spin**, **0.006 Ha** **smearing** for **periodic** **cells**, **4 × 4 × 1** *k*-mesh, **4.5 Å** **orbital** **cutoff**, and stated **SCF/optimization** tolerances. **Nonperiodic** **clusters** use **integer** occupations. **Binding energies** use the standard **surface**–**adsorbate** **decomposition** in the **paper**. **N/A** — stand-alone hybrid DFT beyond this training set for MD production.

**4 — Galley** corpus note. Ingested PDF is a **galley**; align **pagination** to the **VOR** when citing **section** **numbers**.

## Findings

**Primary results.** The fitted **ReaxFF** **matches** key **DFT** trends for **Cu**/**C/H/O** **interactions** and **elementary** **steps** on **Cu** **surfaces** **(authors’ assessment in the article)**. **Test MD** on **Cu** **surfaces** shows **H** **transfer** and **H₂**/**CHO**-type **dissociation** **reactions** consistent with a complex **C/H/O** **surface** **network** on **Cu**. **Chemical** **looping**-oriented **cases** include **CuO** formation from **glucose** + **metallic** **Cu** and **hydrocarbon** **oxidation** with **copper** **oxide** as **oxidant**; **reaction** **pathways** and **redox** **differ** **between** **fuels** in the **reported** **scenarios** **(abstract and discussion)**. **Comparisons** are **DFT vs ReaxFF** and **case vs case** within the MD suite. **Sensitivity** to **fuel** choice and **surface** **redox** state is a stated theme. **Limitations** include transferability to **uncovered** **catalyst** **morphologies** and **pressures** not in the **training** **set**; **however** much of that remains in the main text. **Version-of-record** check recommended because the local file is a **galley** proof.

## Limitations

The corpus PDF is a **galley**; final pagination and minor editorial values may differ from the version of record. TS search and MD numerical details beyond §2.1 require the **full article/SI**.

## Relevance to group

Extends **Reaxff** parameterization for **heterogeneous catalysis** and **combustion/chemical looping** on **Cu** surfaces with open **methodological** contributions (TS search on ReaxFF).

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.0c02573](https://doi.org/10.1021/acs.jpcc.0c02573)

## Related topics

- [[reaxff-family]]
- [[catalysis-surfaces]]

## Reader notes (navigation)

- `paper_keywords` includes **`keyword:galley-or-proof-pdf`** for this ingest.
