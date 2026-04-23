---
id: paper:2019lu-journal-of-c-structure-activity
type: paper
title: "The structure–activity relationship of Fe nanoparticles in CO adsorption and dissociation by reactive molecular dynamics simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reactive-md
  - method:reaxff
  - task:application
  - material:metal-surface
  - scale:atomistic
paper_keywords:
  - keyword:catalysis-surface
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:metallic-systems
candidate_tags: []
source_refs: []
doi: "10.1016/j.jcat.2019.04.010"
year: 2019
authors:
  - "Kuan Lu"
  - "Chun-Fang Huo"
  - "Yurong He"
  - "Wen-Ping Guo"
  - "Qing Peng"
  - "Yong Yang"
  - "Yong-Wang Li"
  - "Xiao-Dong Wen"
venue: "Journal of Catalysis"
pdf_sha256: "43a889283f7890c9dc53bb23c59d41f54d36cc3b53d8cf1af8ec512c14832faa"
pdf_path: "papers/ReaxFF_others/Kuan_Lu_JCat_2019_CO_Fe.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2019lu-journal-of-c-structure-activity -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the *Journal of Catalysis* article identified by `doi`, `title`, and `pdf_path`.

## Summary

Structure–activity relationships are central to catalyst design but difficult to establish experimentally because nanoparticles change shape, size, and defect content on fast timescales. Carbon monoxide activation on iron is important for Fischer–Tropsch synthesis and for high-temperature carburization of iron. This study uses ReaxFF reactive molecular dynamics to relate CO adsorption and dissociation on iron nanoparticles to four structural characteristics: morphology, size, defects (including line dislocations and vacancies), and heteroatom dopants when included. The simulations show strong structure sensitivity: line dislocations and vacancies can markedly accelerate CO dissociation, suggesting defect engineering as a lever on activity. Mechanistic analysis further argues that CO\(_2\) formation may involve Eley–Rideal-like steps at early times and Langmuir–Hinshelwood-like coupling at later stages, with implications for how iron carburizes under CO-rich conditions.

The **nanoparticle** focus matters because **defects** can concentrate **strain** and **local** **coordination** environments that differ from **extended** **facets**, changing both **thermodynamic** **binding** and **barriers** for **C–O** activation without requiring a different **bulk** **phase**.

## Methods

**1 — MD application (ReaxFF, Fe nanoparticles + CO).** The study uses **molecular dynamics** with a **ReaxFF** **Fe–C–O–H** parameter set suited to **reactive** **MD** of **iron** **nanoparticles**; the *Journal of Catalysis* article gives the **lineage** and **validation** **scope**. **System / composition:** **several** **nanoparticle** **constructs** **that** **vary** **morphology**, **size**, and **defect** **content** **(line** **dislocations**, **vacancies**, **etc.**)**; **exact** **atom** **counts** **and** **CO** **coverage** **per** **model** **are** **in** the **full** **PDF** **(not** **in** the **local** **p1–2** **extract**). **Engine / code:** **N/A** in the **indexed** **excerpt** used here—use the **publication** **for** the **MD** **package** **name** if **needed**. **Boundaries:** **3D** **PBC** **(typical** **for** **isolated** **nanoparticle** **cells** **in** **this** **literature** **class**)**; **confirm** **free-space** **padding** **and** **PBC** **in** the **article** **figures**/**Methods**. **Ensemble,** **timestep,** **duration,** **thermostat,** **and** **target** **temperatures** **for** **adsorption**/**reaction** **sampling**:** **N/A** **to** **quote** **from** the **short** **extract**—**read** **the** **simulation** **details** **in** the **version-of-record** **PDF** **(values** **belong** **in** **the** **primary** **paper,** **not** **guessed** **here**)**. **Barostat / mean** **hydrostatic** **pressure** **in** **production** **CO** **runs**:** **N/A** **if** **the** **protocol** **is** **constant-****volume** **NVT** **(as** **is** **common** **for** **adsorption** **studies**)**—** **verify** **NPT** **use** **in** **the** **PDF** **if** **any** **stage** **applies** **stress** **control**. **External** **electric** **field**:** **N/A** **unless** **stated** **(not** **in** **the** **abstract-****level** **summary**). **Replica** / **metadynamics**:** **N/A**—**unbiased** **NVT**/**NVE**-**class** **sampling** **as** **in** the **source**. **Analysis:** **trajectory**-**based** **CO** **adsorption**, **C–O** **scission**, and **CO\(_2\)**-**related** **channels** with **Eley–Rideal** **vs** **Langmuir–Hinshelwood**-**like** **labels** **(time-****segmented** **statistics** **in** the **article**).

**2 — Force-field training:** **N/A**—the work **applies** an **existing** **ReaxFF** **parameterization** **and** does **not** **re-optimize** the **full** **library** **in** the **sense** of **a** **new** **FF** **paper** **(parameter** **choice** **is** **authored,** **not** **a** **from-****scratch** **fit** **here**).

**3 — Static** **QM**/**DFT** **as** **primary** **result**:** **N/A**—**DFT** **appears** **for** **context**/**benchmarks** **in** the **field,** **not** **as** the **dominant** **evidence** **in** this **RMD** **work**.
## Findings

CO adsorption and dissociation vary strongly with nanoparticle structure in the surveyed models. Defects—especially line dislocations and vacancies—substantially enhance CO dissociation relative to more idealized particle shapes, highlighting defects as tunable “activity” knobs in the classical reactive picture. The authors connect early-time CO\(_2\) formation channels to Eley–Rideal-like sequences and later stages to Langmuir–Hinshelwood-like coupling, and they frame the results as mechanistic guidance for iron carburization and related processes, with the usual caveat that nanoscale models and short trajectories may not capture full reactor-scale behavior.

The time-labeled **Eley–Rideal** vs **Langmuir–Hinshelwood** language for **CO\(_2\)** channels should be read as **inferences** from **ReaxFF** **trajectory** statistics in the paper, not as stand-alone experimental proof of those labels.

## Limitations

Nanoparticle ensembles, simulation duration, and force-field scope bound transferability to industrial catalysts; experimental validation remains essential for quantitative rates and selectivities.

## Relevance to group

Illustrates ReaxFF-driven structure–activity mapping for reactive iron–CO chemistry at the nanoscale, adjacent to broader reactive MD work in the corpus.

## Citations and evidence anchors

- **DOI:** [https://doi.org/10.1016/j.jcat.2019.04.010](https://doi.org/10.1016/j.jcat.2019.04.010) (`papers/ReaxFF_others/Kuan_Lu_JCat_2019_CO_Fe.pdf`).
- Extract pointer: `normalized/extracts/2019lu-journal-of-c-structure-activity_p1-2.txt`.

## Related topics

- [[reaxff-family]]
