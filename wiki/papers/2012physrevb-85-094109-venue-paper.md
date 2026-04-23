---
id: paper:2012physrevb-85-094109-venue-paper
type: paper
title: "Electron dynamics of shocked polyethylene crystal"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:organics-polymers-pyrolysis
  - domain:methods-software
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:polymer
  - keyword:hugoniot
  - keyword:shock-compression
  - keyword:lammps
  - keyword:method-development
source_refs: []
doi: "10.1103/PhysRevB.85.094109"
year: 2012
authors:
  - "Theofanis, Patrick L."
  - "Jaramillo-Botero, Andres"
  - "Goddard, William A., III"
  - "Mattsson, Thomas R."
  - "Thompson, Aidan P."
venue: "Physical Review B"
pdf_sha256: "7cb33c6ea0532ab445be14401f6f2770532ff8883b17e8bd3e22bd2661450912"
pdf_path: "papers/Others/PhysRevB.85.094109_EFF_PE.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2012physrevb-85-094109-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose below summarizes the publication identified by `doi` and `pdf_path`. This work uses the **electron force field (eFF)**, not **ReaxFF**.

## Summary

**eFF** **wave-packet** **molecular dynamics** follows the **single-shock Hugoniot** of a **crystalline polyethylene** model. The abstract states **eFF** agrees with prior **DFT** and **experiment** where data exist (up to **~80 GPa** in the abstract’s comparison language), reports **Hugoniot** predictions to **~350 GPa**, and analyzes **ionization**, **molecular decomposition**, and **conductivity** under **isotropic compression**, including a **structural** transition to an **atomic fluid** above a **density** threshold stated in the abstract (**~2.4 g/cm³**) with increased **ionization** and **conductivity**.

## Methods


**Model:** **Electron force field (eFF)** treats each **electron** as a **floating spherical Gaussian** **wave packet** and **nuclei** as **classical** **point charges**; **Pauli** repulsion between **same-spin** **electrons** and **Coulomb** terms are included as in the cited **eFF** Hamiltonian. **Semiclassical** **wave-packet molecular dynamics** propagates both **nuclear** and **electronic** degrees of freedom. Simulations use a **parallel** **eFF** implementation in **LAMMPS**.

**Polyethylene setup:** A **crystalline** **polyethylene** model is built from an **orthorhombic** **PE** **supercell** (**2 × 6 × 3**), with chains **truncated** and **hydrogen-terminated** so as not to impose spurious **axial** stress; the final cell contains **12** **C₁₂H₂₆** molecules (**1632** particles: **144** C, **312** H, **1176** **explicit** **electrons**). **Single-shock** **Hugoniot** sampling follows the protocol in the article.

**Integration note:** Using the **physical** **electron** **mass** in **eFF** forces **sub-fs** **timesteps** (article discusses **attosecond** **order**).

**Shock / Hugoniot:** Single-shock **Hugoniot** sampling follows the protocol in **Section II** of the article (see **Computational details**).

## Findings

Along the **single-shock** **Hugoniot**, **eFF** **pressures** and **temperatures** for **polyethylene** agree with available **DFT** and **experimental** **EOS** data where those data exist (up to **~80 GPa** in the abstract’s comparison language), and the authors **extrapolate** predictions to **~350 GPa**. **Isotropic compression** analysis tracks **ionization** fraction, **molecular** **decomposition**, and **electrical conductivity**. Above **~2.4 g/cm³** **density**, the **PE** structure transitions to an **atomic** **fluid**-like state with a **sharp** rise in **ionization** and **conductivity**—behavior tied to **nonadiabatic** **electronic** effects that **Born–Oppenheimer** **reactive** force fields omit from the **EOS** path.

As a **methods** reference for the corpus, **eFF** fills a niche **orthogonal** to **ReaxFF**: it carries **explicit electrons**, enabling **EOS**-relevant **ionization** under **extreme** compression where classical bond-order models are not parametrized.

**Corpus / KB honesty:** Grounded in **`pdf_path`** and a **partial** extract (`normalized/extracts/2012physrevb-85-094109-venue-paper_p1-2.txt`); verify **Hugoniot** tables and discussion sections in the **PDF** before reusing numerical **EOS** entries.

## Limitations

**eFF** approximations vs **QM**; **partial** extract; **extreme** **shock** conditions extrapolated beyond **experimental** reach.

## Relevance to group

**Reactive MD**-adjacent **extreme conditions** reference for **hydrocarbon** polymers; **not** a **ReaxFF** study.

## Citations and evidence anchors

- DOI **10.1103/PhysRevB.85.094109** — *Phys. Rev. B* **85**, 094109 (2012).
- Extract: `normalized/extracts/2012physrevb-85-094109-venue-paper_p1-2.txt`.

## Related topics

- [[reaxff-family]]
