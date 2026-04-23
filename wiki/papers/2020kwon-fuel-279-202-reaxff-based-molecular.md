---
id: paper:2020kwon-fuel-279-202-reaxff-based-molecular
type: paper
title: "ReaxFF-based molecular dynamics study of bio-derived polycyclic alkanes as potential alternative jet fuels"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:fuel-combustion
  - domain:organics-polymers-pyrolysis
  - domain:reaxff-lineage
  - domain:carbon-hydrocarbon
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:thermal-decomposition
  - keyword:combustion
  - keyword:lammps
source_refs: []
doi: "10.1016/j.fuel.2020.118548"
year: 2020
authors:
  - "Hyunguk Kwon"
  - "Aditya Lele"
  - "Junqing Zhu"
  - "Charles S. McEnally"
  - "Lisa D. Pfefferle"
  - "Yuan Xuan"
  - "Adri C. T. van Duin"
venue: "Fuel 279, 118548 (2020)"
pdf_sha256: "028d7e4f6bb3200074142443f94c05762b2f43073a74d6c486ac16909b1f68b9"
pdf_path: "papers/Kwon_Fuel_2020_polycyclic_alkanes_jet_fuel.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2020kwon-fuel-279-202-reaxff-based-molecular -->

## Summary

**ReaxFF MD** is used to study **early-stage pyrolysis** of bio-derived **head-to-head polycyclic alkanes** **HtH-1 (C₁₈H₃₂)** and **HtH-2 (C₁₈H₃₄)** as **high energy-density aviation fuel** candidates. The motivation is to connect molecular architecture—two cyclohexyl units joined head-to-head—to decomposition kinetics and early gas-phase products relevant to combustor feed chemistry. The work extracts **global Arrhenius** parameters, maps **temperature-dependent** **bond-scission** mechanisms, compares **product slates** (including **sooting** propensity proxies), and examines **binary mixtures** where the two components react largely **unimolecularly** with **weak cross-talk**, supporting interpretation of how stereochemistry and hydrogen count steer branching versus concerted fragmentation.

## Methods

**1 — MD application (ReaxFF pyrolysis in LAMMPS).** **ReaxFF** **reactive** **molecular** **dynamics** is run in the **LAMMPS** **ecosystem** for **head-to-head** **polycyclic** **alkanes** **HtH-1** and **HtH-2** (and **binary** **mixtures**) in **periodic** **vapor**-**like** **cells** that **typically** **hold** **O(10¹–10²)** **fuel** **molecules** per **setup** (e.g. **~40** **molecules** in the **protocol** **described** in the **uncorrected**-**proof** **sibling** **and** **confirmed** in the **version**-**of**-**record** **tables**); see **Fuel** **2020** for **ρ,** **T,** **and** **composition** **(not** **re**-**tabulated** **here**). The **manuscript** uses an **in-house** **reaction**-**analysis** **pipeline** on **bond**-**order**-**updated** **connectivity** to **identify** **pathways** **and** **species** **yields** **vs** **T**. **Kinetics:** **global** **Arrhenius** **parameters** are **fit** to **summary** **reaction** **rates** as **defined** in the **article**. **N/A** in this **short** **note:** **full** **table** of **time** **step** **(fs)**, **equilibration** **(ps)**, **production** **(ns)**, **thermostat** **(e.g.** **Berendsen**), **and** **barostat**—use **`pdf_path`** for **exact** **MD** **settings**. **Target** **temperature** **(K)** **for** **pyrolysis** **runs** **(e.g.** **1500–3000** **K** **window** **in** **the** **galley**-**level** **notes** **elsewhere** **in** **the** **corpus** **for** **this** **DOI**)**:** **take** **from** **the** **Fuel** **article** **/ SI** **(not** **re**-**typed** **here**). **Barostat** **(NPT)** **or** **fixed** **ρ** **(NVT** **at** **target** **ρ**): per **the** **published** **protocol** (often **NVT**-**style** **constant**-**volume** **heating** in **this** **corpus** line). **E-field** / **umbrella** / **replica** **sampling:** **N/A**—**not** **the** **focus** here.

**2 — Force-field training.** **N/A**—**applies** an **established** **ReaxFF** for **C/H** **hydrocarbon** **chemistry** (as **cited** in the **article**), **not** a **new** **fit** **in** this **publication**.

**3 — Static QM / DFT-only.** **N/A**—**result** **trajectories** are **ReaxFF** **MD**; **any** **QM** **in** the **paper** is **for** **reference** **or** **validation**, **not** the **headline** **sampling** **method**.

## Findings

- **HtH-1** pyrolyzes **faster** than **HtH-2** under matched **T, ρ** conditions, and both can exceed some conventional benchmarks such as **JP-10** in the compared decomposition metrics (per abstract).
- **Low T:** **Central C–C** bond between **cyclohexyl** units dominates initial scission for **both** fuels.
- **High T:** **C–CH₃** bond breaking becomes dominant due to **entropy**-favored fragmentation channels.
- **Major products:** **HtH-1** favors **C₅H₈** and **C₄H₈**; **HtH-2** favors **C₄H₈** and **C₂H₄**; product slates imply **higher sooting tendency** for **HtH-1**, consistent with **experiments** quoted by the authors.
- **Mixtures:** **Unimolecular** decomposition with **little intermolecular coupling** between **HtH-1** and **HtH-2** under their pyrolysis conditions, which the authors interpret as weak binary reactivity under the simulated heating protocols.

## Limitations

ReaxFF kinetics are **empirical**; extrapolation to **flame** conditions and **soot** chemistry requires separate validation against **experiment** and higher-level theory. Operator note: when citing **Arrhenius** parameters or **product yields**, align numbers with the **Fuel** **version-of-record** PDF and **SI** tables rather than secondary summaries; **mixture** simulations here probe **weak coupling** between **HtH** isomers but do not replace **engine** **spray** or **oxidizer** **coupled** kinetics.

## Relevance to group

Direct **PSU van Duin-group** contribution to **sustainable aviation fuel** chemistry using **ReaxFF pyrolysis** workflows.

## Citations and evidence anchors

- DOI: [10.1016/j.fuel.2020.118548](https://doi.org/10.1016/j.fuel.2020.118548)

## Reader notes (navigation)

- [[theme-pyrolysis-combustion-organics]] lists related fuel and pyrolysis papers in the corpus.

## Related topics

- [[2020huang-combustion-a-enhancing-combustion]]
- [[reaxff-family]]
- [[theme-pyrolysis-combustion-organics]]
