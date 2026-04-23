---
id: paper:2015zhang-venue-microsoft-word
type: paper
title: "Supporting information — ReaxFF parameters for functionalized PPO anion exchange membranes"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:reaxff-lineage
  - method:reaxff
  - material:polymer-organic
  - task:validation
  - scale:atomistic
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:batteries-interfaces
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.5b07271"
year: 2015
authors:
  - "Weiwei Zhang"
  - "Adri C. T. van Duin"
venue: "J. Phys. Chem. C (Supporting Information)"
pdf_sha256: "ffae2e7f9dfaff14a5a1fbffd42c135bdef027dda33f4a215635f632c436a9bf"
pdf_path: "papers/Zhang_Anion_Exchange_SI_JPCC_2015.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2015zhang-venue-microsoft-word -->

## Summary

This Supporting Information PDF `papers/Zhang_Anion_Exchange_SI_JPCC_2015.pdf` accompanies the Journal of Physical Chemistry C article DOI `10.1021/acs.jpcc.5b07271` on hydrated functionalized poly(phenylene oxide) anion-exchange membranes simulated with ReaxFF. The title page in the extract lists authors Weiwei Zhang and Adri C. T. van Duin (Pennsylvania State University) and a **CONTENTS** section pointing to “ReaxFF reactive force field parameters for hydrated membrane” and “Complete citation for reference 33.” The SI provides extended parameter tables so readers can reproduce the reactive MD energy expression used in the main text. The extract (`normalized/extracts/2015zhang-venue-microsoft-word_p1-2.txt`) shows numerical tables beginning on page 2 of the text layer with a header “1. Reactive MD-force field” and a line reporting **39** general parameters, followed by labeled scalar entries for overcoordination parameters, valency angle conjugation, triple-bond stabilization, C2-correction, undercoordination parameters, taper radii, valency undercoordination, lone-pair-related terms, vdWaals shielding, Coulomb cutoffs, and an atom block beginning with `Nr of atoms; cov.r; valency; a.m; Rvdw; Evdw; gammaEEM…` as formatted in the common tabulated **ReaxFF** parameter layout (compatible with **LAMMPS** `reax/c` when ported). Scientific interpretation of transport, hydration, and mechanical behavior remains in the primary article rather than in the SI alone.

## Methods

`papers/Zhang_Anion_Exchange_SI_JPCC_2015.pdf` is **Supporting Information** for DOI **10.1021/acs.jpcc.5b07271**. Section **“1. Reactive MD-force field”** lists **general** and **per-atom** **ReaxFF** coefficients (overcoordination, valence, vdW shielding, Coulomb cutoffs, atom blocks with covalent radii, valency, vdW terms, **gammaEEM**, etc.) for the **ADF 2012** simulations described on **`[[2015zhang-venue-jp5b07271]]`**. **MD application** timing (**production duration** in **ps**/**ns**), **temperature** setpoints, **periodic boundary** conditions (**PBC**), and **pressure** control are **N/A — SI-only**: those protocol fields are specified only in the **main JPCC** article (**NVT**, **0.25 fs**, **Berendsen** thermostat, room-**temperature** operation, constant-volume **pressure** handling as there described). Use this file as the **authoritative numeric appendix** when porting parameters to another **ReaxFF** implementation; reconcile comment lines (“Overcoordination parameter,” “vdWaals shielding,” “Cutoff for bond order (*100),” etc.) with your parser.

**Static QM / DFT:** **N/A —** not the SI’s primary purpose beyond any minor reference tables.

## Findings

**Mechanistic** results—**swelling**, **OH⁻ diffusion**, **degradation** chemistry, and **TMA / DMBA / DMOA** headgroup **comparisons** at varied hydration **λ**—live only in **`[[2015zhang-venue-jp5b07271]]`** and its **PDF** figures, not in this coefficient file. **Sensitivity** to **λ** (transport versus exposure) and any **experimental** benchmarking are likewise **main-text** content. **Limitations**: parameter tables omit trajectory **duration**, thermostat **uncertainty**, and post-processing scripts, so quantitative kinetics must be reconstructed from the primary paper. **Corpus honesty**: treat this SI as a **duplicate** disclosure of numbers supporting the **version-of-record** article, not as standalone scientific narrative.

## Limitations

Parameter files alone omit system setup and analysis context. SI PDFs can lag minor corrections applied to the main article in some publishers’ workflows.

## Relevance to group

Penn State AEM and ReaxFF work: reproducibility artifact for functionalized PPO membranes relevant to electrochemical device modeling.

For machine-learning ingestion pipelines, tag this page as **supplementary** so embeddings prioritize the main JPCC narrative while still surfacing parameter tables when users ask for “force field file” or “ReaxFF bond parameters” in the AEM context.

## Reader notes (navigation)

- [[2015zhang-venue-jp5b07271]]
- [[batteries-interfaces-reaxff]]
- [[reaxff-family]]
