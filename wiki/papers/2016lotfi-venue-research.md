---
id: paper:2016lotfi-venue-research
type: paper
title: "A reactive force field study on the interaction of lubricant with diamond-like carbon structures"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:carbon-hydrocarbon
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1021/acs.jpcc.6b09729"
year: 2016
authors:
  - "Roghayyeh Lotfi"
  - "ASM Jonayat"
  - "Adri C. T. van Duin"
  - "Mousumi M. Biswas"
  - "Robert Hempstead"
venue: "Journal of Physical Chemistry C"
pdf_sha256: "1a1a16d035af8089e8a96de37c949865d2ef177f5d6ba56fd547acac7122cf34"
pdf_path: "papers/Lotfi_2016_DLC_paper_proof.pdf"
extraction_quality: "good"
group_affiliation: true
paper_keywords:
  - keyword:reaxff-application
  - keyword:polymer
  - keyword:tribology
  - keyword:thermal-decomposition
  - keyword:nvt-simulation
  - keyword:npt-simulation
  - keyword:berendsen-thermostat
  - keyword:galley-or-proof-pdf
---

<!-- id:paper:2016lotfi-venue-research -->

## Summary

**ReaxFF MD** constructs **amorphous DLC** and **hydrogen/nitrogen-functionalized DLC** films by **high-temperature melt/quench** recipes, targets experimental **sp²:sp³**, **H**, and **N** compositions, then simulates **perfluoropolyether (D4OH)** droplet **spreading** and **chemical degradation** on **DLC** vs **DLC:H:N** surfaces relevant to **hard-disk lubrication**. The study connects **atomistic** **wettability** and **scission** chemistry to **industry-relevant** **PFPE** fluids used near **slider** interfaces where **tribochemical** stability is a **yield** limiter.

## Methods

Film construction uses a **C–H–N ReaxFF** extension on published carbon parameters for DLC generation [61] with **EEM** charges [60] (Section 2.1). Starting from a **4×4×1** diamond supercell (**128 C**) in **7.27×7.27×20 Å³** with Ar-filled headspace, an **NVT** melt at **7500 K** (**115k** iterations, **Δt = 0.1 fs**, **Berendsen** thermostat, **250 fs** damping) is followed by cooling **7500 → 3000 K** at **0.004 K per iteration**, **NPT** relaxation to relieve stress, and in-plane expansion to reduce symmetry artifacts; **DLC:H** comes from ethylene pyrolysis in Ar and **DLC:H:N** from heating with **N₂** (Section 2.2 onward). Composition targets near **~30% sp³:sp²**, **~20% H**, and **~15% N** yield **sp³:sp² = 27.3%** (DLC) versus **31.7%** (DLC:H:N), with **17.9% H** and **13.7% N** for DLC:H:N in the abstract.

**LAMMPS** **ReaxFF** then places a nine-strand **D4OH** (perfluoropolyether) droplet on **DLC** (**12,800** atoms) and **DLC:H:N** (**9,850** atoms) slabs. The droplet is equilibrated in an **80 × 80 × 140 Å³** box at **1200 K** for **1,000,000** steps (**100 ps** at **0.1 fs**), deposited on each surface, and equilibrated under **NVT** at **300**, **1000**, and **1500 K** for **500,000** steps (**50 ps**) before spreading and degradation analysis (Section 2). Three-dimensional periodic boundaries apply. **Berendsen** damping (**250 fs**) is documented for the melt/quench DLC build; thermostat details for every D4OH segment should be confirmed in Section 2 if not quoted here. **NPT** appears during DLC stress relaxation; the droplet-on-surface equilibration lines above are **NVT**. External electric fields and umbrella or replica metadynamics are not used. Section 3.1 documents further **C–H–N** ReaxFF training against ab initio QM for C/N bonds and angles—supporting parametrization for DLC:H:N chemistry beyond the abstract’s application focus.

## Findings

Less functionalized **DLC** shows faster D4OH spreading than **DLC:H:N** in the simulations summarized in the abstract. Both surfaces alter PFPE degradation chemistry relative to gas-phase expectations, showing interfacial participation in scission pathways. The work contrasts DLC versus DLC:H:N wettability and decomposition using the composition metrics above. Ar versus **N₂** processing and ethylene pyrolysis stoichiometry are the main film-construction levers used to approach industrial H/N/C and sp²/sp³ targets. Extended HDD context and outlook appear in the full article.

**Corpus note.** Local `pdf_path` is an **ACS proof** PDF—confirm pagination against the *J. Phys. Chem. C* issue pages.

## Limitations

Corpus PDF is an **ACS proof**; cite the **J. Phys. Chem. C** issue for final pagination.
- **Timescales** for **degradation** may still be short relative to **HDD** service lifetimes—qualitative chemistry insight.
- **Industrial** **lubricant** blends include **additives** beyond the **PFPE** strand model shown here; transferability to **full** **formulations** requires additional **validation** not claimed by the abstract alone.
- **Shear** rates and **contact** pressures in **MD** may still exceed **drive** **testing** conditions; map **atomistic** events to **wear** metrics using the **scaling** discussion in the **full** **article** where provided.

## Relevance to group

**van Duin co-authorship**; **ReaxFF** application to **DLC + fluoropolyether** tribochemistry tied to **data-storage** industry context (Western Digital co-authorship).

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcc.6b09729](https://doi.org/10.1021/acs.jpcc.6b09729) — *J. Phys. Chem. C* **120**, 27443–27451 (2016).

## Related topics

- [[reaxff-family]]
