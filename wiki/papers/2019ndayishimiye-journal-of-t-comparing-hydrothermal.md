---
id: paper:2019ndayishimiye-journal-of-t-comparing-hydrothermal
type: paper
title: "Comparing hydrothermal sintering and cold sintering process: Mechanisms, microstructure, kinetics and chemistry"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reactive-md
  - method:reaxff
  - task:application
  - task:experiment-integrated
  - scale:atomistic
paper_keywords:
  - keyword:oxide-surface
  - keyword:reaxff-application
  - keyword:reactive-md
candidate_tags: []
source_refs: []
doi: "10.1016/j.jeurceramsoc.2019.11.049"
year: 2019
authors:
  - "Arnaud Ndayishimiye"
  - "Mert Y. Sengul"
  - "Sun Hwi Bang"
  - "Kosuke Tsuji"
  - "Kenji Takashima"
  - "Thomas Hérisson de Beauvoir"
  - "Dominique Denux"
  - "Jean-Marc Thibaude"
  - "Adri C. T. van Duin"
  - "Catherine Elissalde"
  - "Graziella Goglio"
  - "Clive A. Randall"
venue: "J. Eur. Ceram. Soc."
pdf_sha256: "156c6580e75224c57a4db3c01b8055b97e570dabc1bd6d457f78b6d051e457db"
pdf_path: "papers/Ndayishimiye_JECS_2019_sintering_in_press.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019ndayishimiye-journal-of-t-comparing-hydrothermal -->

## Summary

**Low-temperature sintering** of ceramics promises energy savings and compatibility with temperature-sensitive components, but different process families—here **hydrothermal sintering (HS)** in a **closed** system versus **cold sintering (CSP)** in an **open** system—can yield similar densities while differing in chemistry and microstructure. This **Journal of the European Ceramic Society** article studies **zinc oxide (ZnO)** pellets densified at **155 ± 5 °C** under **~320 MPa** pressure with holds of **0–80 minutes**, comparing HS and CSP routes. Experiments characterize **relative density**, **grain structure**, **residual molecular species**, and **phase** content. **ReaxFF molecular dynamics** simulations complement the experiments by probing plausible **zinc acetate “bridge”** formation mechanisms and contrasting **chemical activity** between HS and CSP environments. **Adri C. T. van Duin** coauthors from Penn State, tying the work to the group’s reactive MD practice.

## Methods

**Experiments (ZnO, HS vs CSP).** Pellets are processed at **155 ± 5 °C** under **~320 MPa** with holds **0–80 min** for each route, comparing **hydrothermal sintering (closed)** vs **cold sintering (open)**. Characterization: **relative density**, **microstructure** / **grain** metrics, **residual molecular** species, and **phase** content (instruments and full matrices in the article). The **open vs closed** environment shifts **chemical potential** of **water** and volatiles, so microstructural and chemical differences can appear at similar density.

**1 — MD application (ReaxFF).** **Reactive MD** probes **zinc acetate** “**bridge**”-type motifs and **closed vs open** **chemical activity** consistent with **ex situ** data. **Engine, cell size, PBC, ensemble, timestep, thermostat, barostat, run length, QEq, cutoffs:** follow the *J. Eur. Ceram. Soc.* **computational** section and SI; **N/A** to restate from this short wiki if not in the local extract—**LAMMPS**-class usage is typical for this group’s **ReaxFF** but confirm in the VOR. **External electric field, shear, shock, umbrella/metadynamics:** **N/A** unless the article states them.

**2 — Force-field training.** **N/A** as a new **ReaxFF** **fit** paper—the study **applies** an established **ReaxFF** parameterization to **ZnO**/**acetate**/**water** chemistry.

**3 — Static QM.** **N/A** as a central *ab initio* production story.

**4 — Review.** **N/A.**

**MD line items (confirm in VOR).** **ReaxFF** **molecular** **dynamics** uses **3D** **PBC** **slabs** with **atom** counts in the *J. Eur. Ceram. Soc.* **computational** section; **NVT** or **NPT** **ensemble**, **timestep** **fs**, **thermostat**, and **equilibration**/**production** **ps**/**ns** as **stated** there. **Hydrostatic** **pressure** in **MD** and **barostat** choice: **N/A** on this page without the **VOR** **SI** open—**confirm** in **PDF**.
## Findings

**Outcomes.** For the conditions tested, **relative density** and **ZnO** **phase** are broadly **similar** between **HS** and **CSP**, but **stabilized phases** (in the sense used in the abstract), **grain size**, and **residual molecular** amounts **differ**. **Ex situ** data support **zinc acetate** **bridging** in **hydrothermally** sintered material.

**Atomistic support.** **ReaxFF** trajectories are used to compare plausible **reaction** pathways and **chemical** **driving forces** for **HS** vs **CSP** (including **bridge**-related motifs). **Comparisons** to **experiment** are as reported in the paper, not re-quantified here.

**Design levers.** Differences in **open vs closed** **environment** couple to **chemistry** even when **macroscopic** **density** looks alike—**pressure**, **time**, and **route** (HS vs CSP) appear in the **experimental** matrix.

**Limitations / outlook (as authored and corpus).** **Mesoscale** texturing is still **experiment-led**; the **`pdf_path`** is an **in-press** manuscript file—use the **version-of-record** *J. Eur. Ceram. Soc.* PDF for final **figure** numbers and corrections.
## Limitations

The corpus **`pdf_path`** is an **in-press** manuscript PDF; prefer the **version-of-record** *J. Eur. Ceram. Soc.* layout for authoritative figure numbering and any editorial corrections. Atomistic models capture selected reaction motifs in idealized cells; **mesoscale** microstructure evolution remains experiment-led, and ReaxFF parameters must be interpreted within their training scope.

## Relevance to group

Couples **experimental** low-temperature ceramic processing with **ReaxFF** insight for aqueous ZnO **sintering aids**, with **van Duin** coauthorship.

## Citations and evidence anchors

- DOI: [10.1016/j.jeurceramsoc.2019.11.049](https://doi.org/10.1016/j.jeurceramsoc.2019.11.049)

## Related topics

- [[reaxff-family]]
