---
id: paper:2010quenneville-venue-paper
type: paper
title: "Reactive molecular dynamics studies of DMMP adsorption and reactivity on amorphous silica surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:oxides-ceramics, domain:catalysis-surfaces, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1021/jp104547u"
year: 2010
authors: ["Quenneville, Jason", "Taylor, Ramona S.", "van Duin, Adri C. T."]
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "92ec8b991cdbee2820af8f1e8aaf948a2e9f614fc9936571a2f8ea6b41cf4c78"
pdf_path: "papers/Quenneville_2010_JPC.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2010quenneville-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study uses **ReaxFF molecular dynamics** to study **dimethyl methylphosphonate (DMMP)** interacting with **amorphous silica** as a function of surface hydroxylation (reported modeled densities 2.0–4.5 OH/nm²). The introduction frames DMMP as a **nerve-agent simulant** relevant to environmental fate on silica-rich materials. Key qualitative results in the excerpt include: at higher OH coverage, binding involves **vdW + hydrogen bonding**; at lower coverages, **covalent** interaction between the phosphonyl oxygen and **3-coordinate Si defects**; at very low coverage, **fragmentation** is observed. A stated binding energy example is **−4.7 kcal/mol** at **4.5 OH/nm²**, and added water can **displace/hydrolyze** adsorbed DMMP. MP2/DFT cluster calculations are reported as supporting selected ReaxFF predictions.

## Methods

**Reactive MD setup (abstract + introduction in extract).** The authors study **dimethyl methylphosphonate (DMMP)** on **amorphous silica** as a function of **surface hydroxylation**, using **molecular dynamics** with the **fully reactive ReaxFF** potential (van Duin–Goddard lineage as cited in the paper). **Modeled OH densities** are **2.0, 3.0, 4.0, and 4.5 OH/nm\(^2\)**. The **a-SiO\(_2\)** surface model is stated to be **structurally quantified** and to **compare well** with **experiment** (per the authors’ claim on the indexed pages).

**1 — MD application.** **Engine / code:** **N/A —** MD engine name not stated in `normalized/extracts/2010quenneville-venue-paper_p1-2.txt` (verify `papers/Quenneville_2010_JPC.pdf`). **System / PBC / ensemble / timestep / thermostat / barostat / production schedule:** **N/A —** not recoverable from the short extract beyond the qualitative **ReaxFF MD** statement. **Temperature context:** the introduction cites **prior TPD work** on DMMP/a-SiO\(_2\) performed at **170 K** (experimental reference temperature, not asserted here as the authors’ MD thermostat setpoint unless stated later in the PDF). **Pressure:** **N/A —** not stated for the authors’ MD in the excerpt. **Electric field:** **N/A —** not indicated. **Replica / enhanced sampling:** **N/A —** not indicated.

**2 — Force-field training.** **N/A —** this article **uses** published ReaxFF silica/organophosphate chemistry rather than deriving a new global parameterization on the indexed pages.

**3 — Static QM / cluster validation.** To **validate** reactions suggested by MD, the authors performed **MP2** and **DFT** quantum-chemistry calculations on **small silica clusters**; the indexed text states these **QM results support** the **MD/ReaxFF** conclusions.

**Checklist closure (indexed pages).** **Ensemble:** **N/A — NVT**/**NPT**/**NVE** not stated in the short extract. **Duration / stages:** **N/A — equilibration**/**production** schedule not stated on pp. 1–2—verify **`pdf_path`**.

## Findings

**Coverage-dependent binding and reactivity.** At **higher OH** densities, DMMP binds via **van der Waals** plus **hydrogen bonding**. At **lower OH** coverages, the excerpt reports **strong covalent** interaction between the **phosphonyl (P=O) oxygen** and **3-coordinate Si defects**. At **2.0 OH/nm\(^2\)**, **DMMP fragmentation** is reported.

**Quantitative example.** The **binding energy** on amorphous silica at **4.5 OH/nm\(^2\)** is given as **−4.7 kcal/mol** (as printed in the abstract/extract).

**Water displacement / hydrolysis.** Adding a **water layer** can **displace** and/or **hydrolyze** adsorbed DMMP in the reported simulations.

**Literature context (experimental simulant studies).** The introduction summarizes **DMMP** as a **simulant** for **sarin/VX** and recounts **TPD** behavior on **a-SiO\(_2\)** (e.g. desorption between **200–275 K**, **16.9 kcal/mol** desorption activation energy in the cited Henderson study) as background—**not** new experimental results claimed by this MD paper on those specific numbers.

**Corpus honesty.** `extraction_quality` is **partial**; barriers, full product lists, and sensitivity sweeps require the **J. Phys. Chem. C** PDF at `pdf_path`.

## Limitations

- Extraction is **partial**; barrier heights, full product distributions, and sensitivity analysis may require the full article.
- Classical reactive FF uncertainty for organophosphate/surface chemistry should be tracked against QM benchmarks.

## Relevance to group

Demonstrates **ReaxFF + QM validation** for **oxide surface chemistry** with organics, a template for adsorption/reactivity studies on amorphous silica and related environmental interfaces.

## Citations and evidence anchors

- Abstract and introduction: DMMP/silica coverage effects, binding energy example, water displacement (J. Phys. Chem. C 2010; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]
