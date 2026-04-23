---
id: paper:2019hahn-j-phys-chem-surface-reactivity
type: paper
title: "Surface Reactivity and Leaching of a Sodium Silicate Glass under an Aqueous Environment: A ReaxFF Molecular Dynamics Study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - material:silicate-glass
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.9b02940"
year: 2019
authors:
  - "Seung Ho Hahn"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C"
pdf_sha256: "6e0752a4a6d93bb5499e066bed9be06841fc5cc41c2be8684bf988588927e8dd"
pdf_path: "papers/Hahn_JPC_leaching_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019hahn-j-phys-chem-surface-reactivity -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Large-scale ReaxFF MD** is used to follow **structural and chemical evolution** at a **sodium silicate glass / water** interface, beyond the simpler **pure silica–water** case. **Water** attack **displaces Na⁺** from **nonbridging oxygen (NBO)** sites, promotes **water dissociation** to **H⁺/OH⁻**, and builds **silanol (SiOH)** through **NBO protonation**; **protons** propagate **into the glass** by **hopping** between **adjacent NBO** sites, so **silanol** populations **grow** over the **nanosecond** trajectories rather than plateauing. **Na⁺ leaching** is tracked from **surface-bound Na–OH-like** motifs through a **finite residence time** before **release** into **bulk water**. **Seung Ho Hahn** and **Adri C. T. van Duin** provide an atomistic picture of **glass corrosion** relevant to **environmental** and **biomedical** **glass** uses. The **JPCC** article emphasizes **alkali** **content** as a **driver** of **enhanced** **hydrolysis** relative to **vitreous** **silica** **alone**.

## Methods

### Force-field lineage (A)

**ReaxFF** for **Na–Si–O–H** glass/water chemistry uses the group’s **reactive** parametrization appropriate to **sodium silicate** surfaces in contact with water (trained against **QM** data in prior **van Duin**-line work cited in **JPCC**—see article for references to the underlying **parameter** set and **Supporting Information**).

### Molecular dynamics protocol (B)

**Large-scale reactive MD** of **hydrated sodium silicate** **slabs** with **liquid water** films: **slab construction**, **water thickness**, **equilibration**, **production length**, **timestep**, **thermostat/ensemble**, and **ReaxFF** **charge equilibration** schedules are specified in `papers/Hahn_JPC_leaching_2019.pdf` (and **SI**). Analysis tracks **time-resolved** **Na**, **H**, and **Si–O** speciation across the **interface** and shallow **glass** interior, including **movies**/trajectory figures for **ion** motion near the surface.

### Static QM (C)

**Not the primary result**—the paper positions **QM** as costly for the **length scales** targeted and uses **ReaxFF MD** for **reactive** sampling.

**Reactive MD on glass–water slabs.** **LAMMPS** **ReaxFF** trajectories in `pdf_path` use **periodic** in-plane **boundary** conditions on **sodium silicate** **slabs** contacted by **liquid water** films (full **atom** counts, film thickness, **timestep**, **NVT**/**NPT** choice, **Berendsen**/**Nose–Hoover** parameters, and **production** lengths in **ns** are listed in **Computational Methods** and **SI**). **Temperature:** **300 K** (or other **K** setpoints) for the interfacial runs match the tables in the **JPCC** article unless the **SI** specifies a variant. **Barostat / pressure:** **N/A** if the summarized leaching study stays **constant-volume** **NVT**; confirm any **NPT** segments in the **PDF**. **External electric field:** **N/A**. **Enhanced sampling:** **N/A**.

## Findings

### Mechanisms

**Ion exchange** and **acid–base** chemistry at **nonbridging oxygen (NBO)** sites drive **continuous** surface modification: **water** displaces **Na⁺** from **NBO**, **water dissociation** supplies **H⁺/OH⁻**, **NBO protonation** builds **silanol (SiOH)**, and **protons** propagate inward by **discrete hopping** between adjacent **NBO** sites—so **SiOH** populations **grow** over **nanosecond** trajectories rather than plateauing. **Na⁺** shows **finite surface residence** as **Na–OH-like** motifs before **release** to bulk water.

### Limitations vs experiment

**Nanosecond** windows may not reach **steady-state** **altered-layer** thicknesses from **long-term** corrosion experiments.

### Outlook

The abstract frames **ReaxFF MD** as supplying **physical insight** at **time/length scales** difficult for **experiment** or **first-principles** MD alone for these **multicomponent** **glass–water** interfaces.

## Limitations

- **Nanosecond** **MD** may not reach **steady-state** **thickness** of **altered layers** seen in **long-term** **experiment**.
- **ReaxFF** for **Na–Si–O–H** must stay within the **fitted** **composition** and **condition** range validated in related **group** work.

Wiki prose here is a **navigation aid**. **Definitive** **numbers**, **protocol** **details**, and **figure**-level **claims** should be taken from the **peer-reviewed** **article** at `pdf_path` (and any **Supporting Information** cited there), not from this page alone.

## Relevance to group

Extends the **Na/Si/O/H ReaxFF** line (see also **`paper:2018ho-venue-paper`** SI / main **JPCC** **NaSiOₓ** parameterization) toward **explicit** **glass–water** **reactivity**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcc.9b02940` (`papers/Hahn_JPC_leaching_2019.pdf`).

## Related topics

- [[reaxff-family]]
