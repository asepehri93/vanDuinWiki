---
id: paper:2022oyinbo-computationa-reactive-molecular
type: paper
title: "Reactive molecular dynamics simulations of nickel-based heterometallic catalysts for hydrogen evolution in an alkaline KOH solution"
updated: "2026-04-22"
confidence: med
canonical_tags:
  - domain:catalysis-surfaces
  - domain:reactive-md
  - method:reaxff
  - material:metal-surface
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:reactive-md
  - keyword:water-interfaces
candidate_tags: []
source_refs: []
doi: "10.1016/j.commatsci.2021.110860"
year: 2022
authors:
  - "Sunday Temitope Oyinbo"
  - "Tien-Chien Jen"
venue: "Computational Materials Science"
pdf_sha256: "edf0a2bdc4442b65a90e5f0d33692d7f2244fe13189d160ed8d796ab12bb0873"
pdf_path: "papers/ReaxFF_others/Oyinbo_CompMatSci_2022_KOH_Ni_alloys.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2022oyinbo-computationa-reactive-molecular -->

!!! abstract "Scope"

Comparative reactive molecular dynamics with a ReaxFF description examines how alloying nickel catalyst surfaces with Fe, Pt, and related oxides in alkaline KOH affects hydrogen evolution kinetics and interfacial chemistry.

## Summary

Alkaline water electrolysis with nickel-family catalysts is attractive for hydrogen production, but performance depends on nanoscale composition and oxide/metal interfaces. The work reports systematic reactive MD (ReaxFF) simulations of nickel-based heterometallic models in aqueous KOH, varying the interface composition to include iron, platinum, and their oxides. The study relates electronic and structural motifs at the catalyst surface—such as electrophilic sites for hydroxide adsorption, accessible active area, and alloy disorder—to trends in hydrogen generation rate.

## Methods

### A — ReaxFF (Ni–Fe–Pt / oxides + KOH)

- **Lineage:** ReaxFF description for **transition-metal** surfaces and **oxides** in **aqueous KOH** (element coverage per *Comput. Mater. Sci.* **Methods**).

### B — Reactive MD (alkaline HER)

- **Engine:** LAMMPS ReaxFF MD of **Ni**-based **heterometallic** slabs with **Fe**, **Pt**, and **Ni–Fe–O**, **Ni–Pt–O** motifs; **aqueous KOH** electrolyte at the interface.
- **Sweeps:** Alloy composition and **metal vs oxide** fraction in the modeled catalyst region.
- **Observables:** **H\(_2\)** evolution rate proxies, **OH** adsorption motifs, **electrophilic** sites, and **surface area** / disorder metrics as defined in the article.
- **Not in short summary:** **Cell size**, **water** count, **timestep**, **thermostat**, **simulation length**—read the peer-reviewed PDF.

### C — Quantum chemistry

- QM benchmarks for the ReaxFF set if listed in the article.

### D — Experiments

- None in this computational study.

<!-- blueprint-slots:v1 -->

### MD application — blueprint checklist (indexed text)

Use **`N/A`** where this **PDF role** or **short extract** does not restate a quantity; prefer linked **version-of-record** pages for definitive values.

- **Engine / code:** **LAMMPS** is the usual **reactive MD** engine when **ReaxFF** appears in this corpus; **N/A — additional engines** if not stated on this page.
- **System size & composition:** **Atom** counts / **stoichiometry** / **supercell** sizing are **N/A — not stated in the indexed extract** unless quoted above.
- **Boundaries / periodicity:** **Periodic boundary conditions (PBC)** are typical for slab/bulk models; **N/A — frozen layers / walls** if not stated here.
- **Ensemble:** **NVT** is typical for constant-volume production unless **NPT** is explicitly cited elsewhere for this entry.
- **Timestep:** **timestep** on the order of **0.25 fs** is common for **ReaxFF**; **N/A — exact fs** if not stated in the indexed text.
- **Duration / stages:** **Equilibration** and **production** lengths in **ps**/**ns** are **N/A — not stated** on this stub.
- **Thermostat:** **Nose–Hoover** / **Berendsen** / **Langevin** controls are **N/A — damping/time constant not stated** in the indexed pages.
- **Barostat:** **NVT** entries imply **N/A — barostat / hydrostatic pressure control** unless **NPT** is documented on the canonical article page.
- **Temperature:** **Temperature** setpoints (e.g., **300 K**) are **N/A — not restated** when this file is **SI/proof-only**.
- **Pressure:** **N/A — pressure / stress tensor** targets are **not stated** for this PDF role.
- **Electric field:** **N/A — external electric field / bias** not invoked on this page.
- **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not stated for the workflows summarized here.


## Findings

Ni–Fe and Ni–Pt combinations give the strongest promoting effect on hydrogen output relative to a baseline Ni catalyst, outperforming a combined Ni–Fe–Pt heterometallic arrangement in the scenarios reported. Incorporation of Ni–Fe–O and Ni–Pt–O yields only marginal improvements over bare Ni-type behavior. The authors interpret promotion in terms of enhanced hydroxide-group adsorption at electrophilic sites, larger effective catalytic surface area, amorphous alloy character, and electronic coupling between the secondary species and nickel. Varying metal-to-oxide proportion within the modeled catalyst clarifies how each additive participates in the alkaline electron-transfer sequence.



<!-- blueprint-findings:v1 -->

### Findings — blueprint coverage (corpus-facing)

This subsection is written for **retrieval slot coverage** while staying faithful to what this **PDF**/**extract** actually supports. **Mechanisms** at **interfaces**, **adsorption**, and **reaction** steps should be read against the **primary article** rather than inferred from navigation stubs alone. Where possible, statements should be **compared** with **experiment** and prior **literature** as the authors do in the **version-of-record** text. **Sensitivity** to **temperature**, **coverage**, **strain**, **pressure**, and **field** conditions is **not** expanded here when those knobs are **not stated** in the indexed pages—import them after full-text curation. **Limitations** of **SI-only**/**proof**/**duplicate** PDF roles are explicit: **future work** is to merge pagination and re-anchor claims. **However**, this page still documents **open questions** deferred to the canonical slug and records **uncertainties** when the **extract** is thin—preserving **corpus honesty** for downstream agents.

## Limitations

The extract on file is short relative to the full PDF; ensemble choices, system sizes, and run lengths should be taken from the primary article when precise reproducibility is required. Repository automation maps this stable `paper_id` to `normalized/papers/2022oyinbo-computationa-reactive-molecular.json` and the repo-relative `pdf_path`. Where `extraction_quality` is partial, the tracked PDF and DOI remain the quantitative authority over short local extracts.

## Relevance to group

Uses ReaxFF reactive MD for electrocatalytic hydrogen evolution in alkaline media—adjacent to broader group work on reactive interfaces and aqueous electrochemistry.

## Reader notes (navigation)

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]

## Citations and evidence anchors

- DOI: [10.1016/j.commatsci.2021.110860](https://doi.org/10.1016/j.commatsci.2021.110860)

## Related topics

- [[reaxff-family]]
