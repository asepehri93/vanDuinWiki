---
id: paper:2018bejagam-venue-paper
type: paper
title: "Supplementary information: Nanoparticle activated and directed assembly of graphene into a nanoscroll"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:2d-layered
  - material:graphene-carbon-nano
  - method:reaxff
  - task:application
paper_keywords:
  - keyword:supporting-information
  - keyword:reaxff-parameterization
  - keyword:reaxff-application
candidate_tags: []
source_refs: []
doi: "10.1016/j.carbon.2018.03.077"
year: 2018
authors:
  - "Karteek K. Bejagam"
  - "Samrendra Singh"
  - "Sanket A. Deshmukh"
venue: "Supporting Information, Carbon, 134 (2018) (linked to main article)"
pdf_sha256: "240337af7234a5af8a2b7232744cc3b1a31f25813ce99489be3cf799274882af"
pdf_path: "papers/ReaxFF_others/Bejagam_Carbon_nanoscroll_2018_SI.pdf"
extraction_quality: "partial"
group_affiliation: false
---

<!-- id:paper:2018bejagam-venue-paper -->

## Summary

This Supporting Information PDF `papers/ReaxFF_others/Bejagam_Carbon_nanoscroll_2018_SI.pdf` accompanies the *Carbon* article DOI `10.1016/j.carbon.2018.03.077` on nanoparticle-directed rolling of graphene into nanoscrolls (Bejagam, Singh, Deshmukh). Section **S1** in the extract explains why **ReaxFF** is used: it captures association and dissociation, **charge transfer** between cations and anions, and nonbonded interactions, with parameters typically fit to large **QM** databases for ground and reactive pathways. **Equation S1** lists \(E_{\text{total}} = E_{\text{bond}} + E_{\text{over}} + E_{\text{under}} + E_{\text{val}} + E_{\text{pen}} + E_{\text{tors}} + E_{\text{conj}} + E_{\text{vdWaals}} + E_{\text{Coul}}\), and notes that nonbonded interactions are computed for all atom pairs with shielding to avoid excessive short-range repulsion. The SI traces provenance for **graphene–diamond** (hydrocarbon/nitramine-extended training cited), **graphene–nickel** (**Muller et al.** following **Nielson et al.** CNT-on-Ni development), **graphene–platinum** (**Sanz-Navarro et al.**), and **graphene–gold** (**Jarvi et al.**), stating each block was trained against QM interaction energies for **sp² carbon** on the respective metals.

## Methods

The SI is methodological documentation: it does not replace the main article’s simulation protocol. The extract elaborates **nickel–carbide** training cases (Ni₃C, Ni₂C, NiC phases) used in Muller et al.’s improvement to Ni-catalyzed hydrocarbon chemistry and notes validation of a graphene sheet on Ni against QM. Production reactive **NVT** **LAMMPS** runs—**300 K**, **0.5 fs** timestep, **~5 ns** duration, **300 Å** cubic cell with a fixed graphene strip edge—are summarized on [[2018bejagam-carbon-134-2-nanoparticle-activated]] together with nanoparticle compositions (**diamond**, **nickel**, **platinum**, **gold**) that nucleate scrolling.

- **Boundaries / periodicity:** **Three-dimensional periodic boundary conditions** on the **300 Å** cubic cell; frozen graphene edge atoms as in the main article figures.
- **Thermostat:** **NVT** thermal control at **300 K** (implementation per *Carbon* **Methods** / SI inputs).
- **Barostat / pressure:** **N/A —** constant-volume **NVT** **RMD**; **N/A —** no target **hydrostatic pressure** in the summarized scroll protocol.

**ReaxFF training documentation (SI, not a standalone refit in this work):** **Parent parameter sets** combine literature **ReaxFF** blocks for **hydrocarbon / nitramine** (**graphene–diamond**), **Muller et al.** Ni chemistry (**graphene–Ni**), **Sanz-Navarro et al.** Pt clusters (**graphene–Pt**), and **Jarvi et al.** Au–organics (**graphene–Au**), each trained against **DFT**/**QM** interaction energies for **sp² carbon** on the corresponding metal (**Section S1**). **Training sets** emphasize **QM** databases of bond dissociation, **equation of state** data, and surface-cluster **energies** as cited per block. **Optimization:** **N/A —** this SI documents **merged** literature parameters rather than a new global **parameter optimization** run for the nanoscroll study. **Validation:** authors point to **QM** benchmarks (e.g., graphene on **Ni**) used when those blocks were originally published.

## Findings

Scroll formation timelines, radii, and comparative nanoparticle efficiencies appear in the **primary article**; this **SI** substantiates **ReaxFF** **force-field** choices and **energy** decomposition underpinning those simulations. The narrative emphasizes that **Ni** parameters encode **surface/subsurface/bulk** hydrocarbon binding and **carbide** **formation energies**, **Pt** parameters target **cluster** **energies**, and **Au** blocks stem from **thiolate-focused** **QM** training—each motivating why merged sets should describe **sp² carbon on metals** in the nanoscroll geometry. **Compared** to using a single metal–carbon table blindly, the SI stresses **compatibility** checks when mixing blocks. **Sensitivity** to **NP** composition and **graphene** edge constraints is implicit: users must import **exact** parameter tables from this **PDF** rather than secondary summaries. **Limitations:** merged subsets were **not** simultaneously **reoptimized** in one global fit for this specific geometry—an authored caveat relevant when porting parameters. **Corpus honesty:** this slug is **SI-only**; quantitative **kinetics** claims belong with the **version-of-record** article linked by DOI and [[2018bejagam-carbon-134-2-nanoparticle-activated]].

## Limitations

Parameter provenance text references external studies; users must verify compatibility when mixing parameter blocks across publications.

## Relevance to group

ReaxFF documentation for graphene–nanoparticle self-assembly relevant to nanocarbon mechanics and tribology themes.

Users combining multiple metal–carbon parameter sources should verify compatibility of charge equilibration settings across blocks, because the SI itself warns that ReaxFF merges QM-trained subsets that were not simultaneously reoptimized in a single global fit for this specific nanoscroll study.

Scroll initiation and barrier estimates in the main article should be reproduced with identical nanoparticle compositions and edge constraints, because the SI documents parameters but not every geometric variant tested during exploration.

## Reader notes (navigation)

- [[2018bejagam-carbon-134-2-nanoparticle-activated]]
- [[graphene-nanocarbon]]
- [[reaxff-family]]
