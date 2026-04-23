---
id: paper:2019nayir-venue-paper
type: paper
title: "Supporting information: Development of the ReaxFF Reactive Force Field for Inherent Point Defects in the Si/Silica System"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:reaxff-lineage
  - domain:water-silica-geo
  - method:reaxff
  - task:parameterization
  - material:silicate-glass
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpca.9b01481"
year: 2019
authors:
  - "Nadire Nayir"
  - "Adri C. T. van Duin"
  - "Sakir Erkoc"
venue: "Supporting information (J. Phys. Chem. A)"
pdf_sha256: "b5c90c6d5eb7897ae8df5cddb65d5b6677e00ea1d3a8ac5fe8352816d12b3de8"
pdf_path: "papers/Nayir_JPC_C_SiOx_2019_SI.pdf"
extraction_quality: "partial"
group_affiliation: true
---
<!-- id:paper:2019nayir-venue-paper -->

## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**Corpus note:** this slug indexes the **J. Phys. Chem. A supporting-information PDF** (`papers/Nayir_JPC_C_SiOx_2019_SI.pdf`) for the Si/silica defect ReaxFF article **`[[2019nayir-j-phys-chem-development-reaxff-2]]`**. The SI adds **extra figures** comparing **QM** and **ReaxFF** equations of state for **Si** and **silica** polymorphs, **tabulated reaction energies** for **Si–O–H** training sets, and **implementation notes** for **ReaxFF**, **LAMMPS**, or **ADF**. The **main article** redevelops **Si/O/H** parameters so that **oxygen interstitials**, **migration in bulk Si**, and **a-SiO₂/Si** interface oxidation treat **point-defect** physics omitted by earlier fits; the revised field (**“ReaxFFpresent”**) targets **bond-centered** **O** hopping with a barrier near **~65 kcal/mol**, correcting **SiOH(2010)** behavior that had allowed **spurious deep O diffusion** near room temperature. The extract pages reproduced here show **Figure S1** (**EOS** for **α**, **β**, **cubic Si**) and **Figure S2** (**cristobalite** and **coesite** silica polymorphs) with paired **QM/ReaxFF** curves, plus **Table S1** listing **Si–O–H** reaction energies in kcal mol\(^{-1}\) for dimer/trimer anion condensation steps used in the fit.

## Methods

**Document role.** This PDF is the **Supporting Information** for the Si/silica defect ReaxFF work; full **simulation** protocols and the main **ReaxFF** optimization narrative are in **`[[2019nayir-j-phys-chem-development-reaxff-2]]`**.

**1 — MD application (production / validation runs).** **N/A in this SI slice** for a full **engine** / **ensemble** / **timestep** / **thermostat** table: the indexed SI material stresses **supplemental** **QM vs ReaxFF** **EOS** plots (**Figure S1** for **α-**, **β-**, and **cubic** Si; **Figure S2** for **cristobalite** and **coesite**) and **Table S1** **reaction** energies, not a reproduced LAMMPS run log. **Barostat, electric field, shear/shock, enhanced sampling:** **N/A** in the SI content summarized here; **O** **migration** and **interface** **MD** are in the main article.

**2 — Force-field training (ReaxFF, Si/O/H).** The **ReaxFFpresent** refit corrects **SiOH(2010)** **O** **superdiffusion**; the main text cites **bond-centered** **O** hopping with a barrier on the order of **~65 kcal/mol** (see main paper). **Table S1** lists **ReaxFFpresent** vs **DFT** (kcal mol\(^{-1}\)) for **Si–O–H** condensation training reactions (dimer/trimer anion and related steps). The SI states compatibility of the parameter set with **ReaxFF** in **LAMMPS** and **ADF**. **QM** **functional** / **basis** and the **CMA-ES** **fit** details are in the main article.

**3 — Static QM (SI validation).** **Figure S1–S2** pair **DFT** and **ReaxFF** **EOS** for **Si** and **silica** polymorphs; **DFT** settings follow the main paper.

**4 — Review / non-simulation.** **N/A.**

**MD protocol line items (SI honesty).** Full **production** **MD** with reported **atom** counts, **3D** **PBC**, **NVT** or **NPT** **ensemble**, **timestep** in **fs**, **equilibration** and **production** **ns** spans, **thermostat**, and any **barostat** / **hydrostatic** **pressure** control are **N/A** in this **SI** PDF slice—see the **main** article (`[[2019nayir-j-phys-chem-development-reaxff-2]]`) for those **LAMMPS**/ADF **reactive** **MD** details.
## Findings

Extended **QM vs ReaxFF** numerical agreement plots and **tabular** training targets support reproducibility; substantive mechanistic conclusions (**O** migration pathways, **interface** transport) belong with the **main text** at the same **DOI**. Representative **Table S1** entries in the extract span **−14** to **−28 kcal mol\(^{-1}\)** depending on reaction, illustrating how the refit balances clustered **Si(OH)\(_x\)** reactions against **DFT** references; readers should treat these numbers as **SI training diagnostics**, not standalone mechanistic claims without the main article’s discussion of **defect** migration barriers and **interface** oxidation tests.

## Limitations

**SI-only** packaging does not replace the **main article** narrative; cite **`[[2019nayir-j-phys-chem-development-reaxff-2]]`** for interpretation.

## Relevance to group

Provenance bundle for the Si/O/H ReaxFF reparameterization used in follow-on silica and interface studies.

## Citations and evidence anchors

Pair with `papers/Nayir_JPC_C_SiOx_2019.pdf` (main article). SI hosted with https://doi.org/10.1021/acs.jpca.9b01481

## Related topics

- [[2019nayir-j-phys-chem-development-reaxff-2]]
- [[reaxff-family]]
