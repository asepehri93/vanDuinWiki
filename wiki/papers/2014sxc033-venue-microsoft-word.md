---
id: paper:2014sxc033-venue-microsoft-word
type: paper
title: "Atomistic simulation and virtual diffraction characterization of stable and metastable alumina surfaces"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - material:oxide
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:oxide-surface
  - keyword:lammps
  - keyword:validation-experiment
candidate_tags: []
source_refs: []
doi: "10.1016/j.actamat.2014.06.061"
year: 2014
authors:
  - "Shawn P. Coleman"
  - "Douglas E. Spearot"
venue: "Acta Mater."
pdf_sha256: "dacb76dc440a8ac0acaa94a1fcec80ac86d78f9111b8795f149a6d35558da57b"
pdf_path: "papers/ReaxFF_others/Coleman_Spearot_PhysReviewB_Al2O3_Surfaces.pdf"
extraction_quality: "good"
group_affiliation: false
---

<!-- id:paper:2014sxc033-venue-microsoft-word -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Molecular statics** and **ReaxFF MD** study **bulk** and **surface** models of several **Al\(_2\)O\(_3\)** **polymorphs**, with **virtual XRD/SAED** used to compare structures to experiment. **Bulk** runs recover **α-Al\(_2\)O\(_3\)** as the lowest **crystalline** phase but also find a **lower-energy amorphous** basin in the model—an artifact that biases some **high-T** **surface** runs toward **premature reconstruction**. **0 K** **surface** energies/structures align reasonably with **prior DFT**; **MD** at **300–700 K** shows **reconstructions** earlier than expected, interpreted as coupling between **free-surface** degrees of freedom and the **spurious amorphous** stability. **Virtual diffraction** shows **partial order** (not fully **amorphous**) when the bulk lattice constrains the **surface** region. **Surface energies** are tabulated for **mesoscale** **PVD** modeling contexts.

## Methods

**Local sources:** the PDF at `papers/ReaxFF_others/Coleman_Spearot_PhysReviewB_Al2O3_Surfaces.pdf` is present in this workspace (despite the historical filename, the article matches DOI **10.1016/j.actamat.2014.06.061**, *Acta Mater.* **78**, 354–368 (2014)). Opening text is captured in `normalized/extracts/2014sxc033-venue-microsoft-word_p1-2.txt`.

The authors study **alumina** using **molecular statics** and **molecular dynamics** with **ReaxFF** as implemented in **LAMMPS** (as stated in the article body), and they characterize structures with **virtual X-ray diffraction (XRD)** and **selected-area electron diffraction (SAED)**-style post-processing. **Bulk** simulations first probe **transferability** across **Al\(_2\)O\(_3\)** polymorphs; **surface** studies compare **0 K** relaxed surfaces to **prior first-principles** literature, then examine **finite-temperature** dynamics on selected surfaces.

**MD application.** **LAMMPS** **molecular dynamics** with **ReaxFF** implements **bulk** polymorph sampling and **finite-temperature** **surface** dynamics, while **molecular statics** at **0 K** supplies relaxed **surface** structures and **surface energies** (opening text in `normalized/extracts/2014sxc033-venue-microsoft-word_p1-2.txt`). Atom counts, slab thicknesses, vacuum, **periodic** (**PBC**) treatment, timestep, **equilibration**/**production** **durations** (**ps**/**ns**), **NVT**/**NPT** staging, thermostat/**barostat** damping, and **temperature**/**pressure** schedules are **N/A** on the short extract and appear only in **`papers/ReaxFF_others/Coleman_Spearot_PhysReviewB_Al2O3_Surfaces.pdf`**.

**Force-field training.** **N/A**: the article applies a published **ReaxFF** for **Al/O** as referenced there, not a new **QM** fit documented in the excerpt.

**Static QM / post-processing.** **0 K** **molecular statics** compares **surface** energies/structures to **prior DFT**; **virtual XRD** and **SAED**-style analysis compares modeled diffraction signatures to experiment as described in the article.

## Findings

**Bulk ReaxFF** correctly identifies **α-Al\(_2\)O\(_3\)** as the lowest-energy **crystalline** phase in their tests, but it also predicts an even **lower-energy amorphous** basin, which the authors flag as an **artifact** with consequences for **surface** simulations. At **0 K**, **virtual XRD** for crystalline polymorphs is described as **consistent with experimental** references, and **surface** energies/structures from **molecular statics** align **reasonably** with **prior DFT**. **Finite-temperature MD** reports **premature surface reconstructions** at temperatures **below experimental expectations**, interpreted as bias from the **spurious amorphous stability** combined with extra degrees of freedom at **free surfaces**. **Virtual SAED** shows **partial order** (not fully amorphous) when an internal **bulk lattice** constrains the surface region. The authors tabulate **surface energies** for use in **mesoscale** **PVD** modeling contexts.

## Limitations

- **Filename** in the corpus suggests **Phys. Rev. B**; the article matches **Acta Materialia** (**DOI** above)—treat **bibliography** from the **DOI**, not the folder name.
- **Amorphous** phase as **lowest** energy is a known **FF** pathology to monitor in **oxide** simulations.

## Relevance to group

**Alumina** **ReaxFF** **validation** and **characterization** workflow parallels other **oxide** **interface** studies in the corpus.

## Citations and evidence anchors

- **DOI:** https://doi.org/10.1016/j.actamat.2014.06.061 — *Acta Mater.* **78**, 354–368 (2014).

## Related topics

- [[reaxff-family]]
