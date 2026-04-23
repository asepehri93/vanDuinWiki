---
id: paper:2015weismiller-modelling-an-reaxff-molecular
type: paper
title: "ReaxFF molecular dynamics simulations of intermediate species in dicyanamide anion and nitric acid hypergolic combustion"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:fuel-combustion
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1088/0965-0393/23/7/074007"
year: 2015
authors:
  - "Michael R. Weismiller"
  - "Chad E. Junkermeier"
  - "Michael F. Russo Jr"
  - "Michael R. Salazar"
  - "Dmitry Bedrov"
  - "Adri C. T. van Duin"
venue: "Modelling Simul. Mater. Eng. Sci."
pdf_sha256: "89b92dfd300d2dd0ee3824ef710f01eefbad00a8630b7629024c531a9976096c"
pdf_path: "papers/Weismiller_DCA_MSME_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015weismiller-modelling-an-reaxff-molecular -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF molecular dynamics** targets two **predicted intermediates** in **dicyanamide (DCA⁻)**-based **ionic liquid** combustion with **nitric acid (HNO₃)**: **protonated DCA (DCAH)** and **nitro-dicyanamide-carbonyl (NDC)**. The abstract reports **single-component** runs showing **NDC** can undergo **exothermic decomposition**/**ignition**, and **mixture** simulations with **HNO₃** at **low (0.25 g ml⁻¹)** and **high (1.00 g ml⁻¹)** densities to compare **dense vapor** vs **liquid-like** conditions; **higher density** shortens the time to **thermal runaway**. The authors state that, contrary to a proposed **DCA** combustion mechanism, **neither DCAH nor NDC** converts to **1,5-dinitrobiuret (DNB)** before **thermal runaway**, and they discuss **pathway** details in the article body. **Ionic-liquid** hypergols are motivated as **less toxic** replacements for **hydrazine**-class fuels (abstract, introduction).

## Methods

Reactive trajectories use a **standalone ReaxFF** implementation **patched** to represent **carbon–nitrogen triple bonds** in **protonated dicyanamide (DCAH)** (`papers/Weismiller_DCA_MSME_2015.pdf`, Computational section). Simulations cover **single-component NDC** decomposition and **binary DCAH/HNO₃** and **NDC/HNO₃** mixtures; the abstract compares **HNO₃** at **0.25 g mL⁻¹** (“dense vapor”) and **1.00 g mL⁻¹** (“liquid-like”). **3D periodic** cells are **rescaled** during an early **NVT** segment (“first **20 000** time steps…”) to reach high-density mixture targets. Protocol: **NVT** heating **250 → 500 K** at **5 K ps⁻¹** with **Berendsen** thermostat (**500 fs** damping), then **1.5 ns NVE** at **500 K**; **0.1 fs** timestep throughout. No barostat, explicit pressure target, electric field, or enhanced sampling is described—density is set by **manual cell rescaling** in **NVT**. Bond-order **species tagging** is done in the ReaxFF code.

**Force-field training:** The work builds on published **C/H/O/N** combustion / ionic-liquid **ReaxFF** lines plus the **code modification** for **DCAH nitriles**; it is **not** a full new QM-trained global refit (no standalone optimization dataset in the AGENTS sense).

**Static QM / DFT:** **N/A —** reactive MD is the reported primary modality.

## Findings

**NDC** alone undergoes **exothermic decomposition** toward **ignition** in the single-component runs summarized in the abstract. **DCAH** and **NDC** both react **hypergolically** with **HNO₃**; **higher HNO₃ density** shortens the time to **thermal runaway** (**1.00 vs 0.25 g mL⁻¹**). Against a literature mechanism invoking **1,5-dinitrobiuret (DNB)**, the authors report **neither DCAH nor NDC** forms **DNB** **before thermal runaway** in their trajectories. **Mixture density** is the main lever on ignition delay at abstract level; detailed pathways and populations are figure- and time-series–driven in the PDF—use the journal file for quantitative delays and species counts.

## Limitations

- **Ignition** is sensitive to **initial mixing morphology** and **quantum effects** not included in classical ReaxFF.
- **Quantitative barrier heights** should be spot-checked with **QM** along select reaction coordinates.

- **Propellant safety:** **simulation** **temperatures** and **densities** are **idealized**; do **not** use this page as **operational** safety guidance without **experimental** **hazard** data for **DCA**/**WFNA** blends.

**Figures:** use the **article** **time-series** plots as the **authoritative** **population** **records** for **intermediate** **species**—this wiki avoids duplicating **numeric** **timelines** without **PDF** **pagination**.

## Relevance to group

Shows the group’s **ReaxFF portfolio in reactive propellant chemistry**, adjacent to **combustion and safety** modeling use cases.

## Citations and evidence anchors

- Title/author block and abstract in `papers/Weismiller_DCA_MSME_2015.pdf`; **DOI:** `10.1088/0965-0393/23/7/074007`.

## Related topics

- [[reaxff-family]]
