---
id: paper:2013aiaa-venue-paper
type: paper
title: "Molecular dynamics studies of thermal accommodation on carbon structures"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:carbon-hydrocarbon, material:graphene-carbon-nano, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: ""
year: 2013
authors: ["Mehta, Neil", "Levin, Deborah A.", "van Duin, Adri C. T."]
venue: "AIAA conference abstract / manuscript"
pdf_sha256: "9376825fba2c4db26837f13007552b05f281f87e03df6b0cb7d61f07c64923f8"
pdf_path: "papers/AIAA_Abstract_NeillMehta.pdf"
extraction_quality: "partial"
group_affiliation: true
---

<!-- id:paper:2013aiaa-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose summarizes text present in **`normalized/extracts/2013aiaa-venue-paper_p1-2.txt`** and the PDF **`papers/AIAA_Abstract_NeillMehta.pdf`**. **No journal DOI** is registered in metadata; **confidence** remains **low** pending archival publication details.

## Summary

Mehta, Levin, and van Duin present an **aerospace-motivated** **ReaxFF molecular dynamics** study of **thermal accommodation** between **N\(_2\)** gas and a **graphene** surface, using **graphene** as a surrogate for a **bacillus anthracis spore** wall in a high-temperature gas environment. The introduction frames **thermal accommodation coefficients** as central to predicting how efficiently **hot gas** transfers energy to a **biological** particle during **thermal inactivation** scenarios, with immediate application to modeling **spore** interactions in **high-T** flows. The authors cite **ReaxFF** as enabling **gas–surface** simulations that go beyond hard-sphere **Baule** estimates by explicitly treating **atomic** collisions and energy redistribution. **Adri C. T. van Duin** appears as a coauthor, linking the manuscript to the group’s broader **gas–surface** **reactive MD** portfolio.

## Methods

### Literature scope (theory + MD setup narrative)

The manuscript introduces **thermal accommodation** for **bacillus anthracis** spores modeled as a **graphene** surface in **N\(_2\)** (**§I**; `normalized/extracts/2013aiaa-venue-paper_p1-2.txt`). It reviews **Baule** hard-sphere theory with \(\alpha = 1 - \langle E_r\rangle/\langle E_i\rangle\), angular relations \(\alpha = 4\mu\cos^2\psi/(1+\mu)^2\), and the isotropic average \(\alpha = 2\mu/(1+\mu)^2\) for mass ratio \(\mu = M_g/M_s\).

### MD application (as described on indexed pages)

**Engine / code:** **ReaxFF molecular dynamics** is named for **gas–surface** interaction modeling (**§II**; extract).

**System & composition:** **Graphene** surface with **nitrogen** as the gas species is described at the conceptual level on p1–2; **N/A —** supercell sizes, **N** atom counts, and **slab** thickness are **not** stated in the extract.

**Boundaries / periodicity:** **N/A —** **PBC** details are **not** stated in the extract.

**Ensemble:** The text defines **NVE** (fixed **N**, **V**, energy) and **NVT** (fixed **N**, **V**, **T**) as standard options (**§II**).

**Thermostat:** For **NVT**, the **Berendsen** update \(\Delta T = (\delta t/\tau)(T_0 - T(t))\) is given, with coupling time \(\tau\) controlling coupling strength (**§II**).

**Timestep / duration / production protocol:** **N/A —** \(\delta t\), trajectory **length (ps/ns)**, and collision **sampling** workflow are **not** on pages 1–2 of the extract—use **`pdf_path`**.

**Barostat / pressure:** **N/A —** **NPT** / stress control **not** discussed on indexed pages.

**Temperature:** **High-temperature gas** motivation appears in **§I**; **N/A —** thermostat setpoints for production runs **not** in the excerpt.

**Electric field:** **N/A —** not discussed.

**Replica / enhanced sampling:** **N/A —** not discussed.

### Force-field training

**N/A —** this document is **not** a ReaxFF parameterization paper; it **uses** **ReaxFF** as the interaction model for planned/ongoing **MD** gas–surface studies.

## Findings

**Outcomes:** The excerpt states the goal of estimating **thermal accommodation coefficients** from **ReaxFF MD** of **N\(_2\)** on **graphene**, moving beyond **Baule** hard-sphere limits (**§I–II**).

**Comparisons:** **Baule** analytic limits are contrasted with the need for **atomistic MD**; **N/A —** numerical agreement with **experiment** is **not** on the indexed pages.

**Sensitivity:** **Thermostat coupling** \(\tau\) controls how closely **NVT** resembles **NVE**-like behavior (indexed **§II**).

**Limitations:** **Conference/abstract** PDF; **no DOI** in corpus metadata; quantitative \(\alpha\) values require later sections of **`pdf_path`** or a peer-reviewed version if published separately.

**Corpus honesty:** `2013aiaa-venue-paper_p1-2.txt` is **two pages** of introduction + ensemble definitions only.

## Limitations

**Partial** extraction; **conference/abstract** PDF may lack full peer-review context. **DOI** absent in corpus metadata. Any future **peer-reviewed** expansion should be ingested as a **new** manifest row rather than overwriting this **AIAA** artifact without operator review.

## Reader notes (navigation)

Treat **`papers/AIAA_Abstract_NeillMehta.pdf`** as a **historical** ingest for **group authorship** tracing; quantitative accommodation results require the full manuscript if it exists outside this repository.

## Relevance to group

Demonstrates **ReaxFF** applied to **gas–surface energy transfer** adjacent to **aerospace** thermal environments.

## Citations and evidence anchors

- Sections I–II in `papers/AIAA_Abstract_NeillMehta.pdf` (see `normalized/extracts/2013aiaa-venue-paper_p1-2.txt`).

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
