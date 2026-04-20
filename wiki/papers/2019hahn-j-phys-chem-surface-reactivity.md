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
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2019hahn-j-phys-chem-surface-reactivity -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Large-scale ReaxFF MD** is used to follow **structural and chemical evolution** at a **sodium silicate glass / water** interface, beyond the simpler **pure silica–water** case. **Water** attack **displaces Na⁺** from **nonbridging oxygen (NBO)** sites, promotes **water dissociation** to **H⁺/OH⁻**, and builds **silanol (SiOH)** through **NBO protonation**; **protons** propagate **into the glass** by **hopping** between **adjacent NBO** sites, so **silanol** populations **grow** over the **nanosecond** trajectories rather than plateauing. **Na⁺ leaching** is tracked from **surface-bound Na–OH-like** motifs through a **finite residence time** before **release** into **bulk water**. **Seung Ho Hahn** and **Adri C. T. van Duin** provide an atomistic picture of **glass corrosion** relevant to **environmental** and **biomedical** **glass** uses.

## Methods

- **ReaxFF reactive MD** of **hydrated sodium silicate** surface slabs with **large** system sizes (per **JPCC**).
- **Time series** analysis of **Na**, **H**, and **Si–O** speciation across the **interface** and shallow **bulk**.

## Findings

- **Ion exchange** and **acid–base** chemistry at **NBO** sites drive **continuous** **surface** **modification** on simulated **timescales**.
- **Na** **mobility** and **proton** **subnetworks** rationalize **leaching** and **silanol** **front** **propagation** trends reported in the article.

## Limitations

- **Nanosecond** **MD** may not reach **steady-state** **thickness** of **altered layers** seen in **long-term** **experiment**.
- **ReaxFF** for **Na–Si–O–H** must stay within the **fitted** **composition** and **condition** range validated in related **group** work.

## Relevance to group

Extends the **Na/Si/O/H ReaxFF** line (see also **`paper:2018ho-venue-paper`** SI / main **JPCC** **NaSiOₓ** parameterization) toward **explicit** **glass–water** **reactivity**.

## Citations and evidence anchors

- **DOI:** `https://doi.org/10.1021/acs.jpcc.9b02940` (`papers/Hahn_JPC_leaching_2019.pdf`).

## Related topics

- [[reaxff-family]]
