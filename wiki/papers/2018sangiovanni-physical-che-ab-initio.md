---
id: paper:2018sangiovanni-physical-che-ab-initio
type: paper
title: 'Ab initio molecular dynamics of atomic-scale surface reactions: insights into
  metal organic chemical vapor deposition of AlN on graphene'
updated: "2026-04-20"
confidence: med
canonical_tags:
- domain:catalysis-surfaces
- domain:2d-layered
- material:graphene-carbon-nano
- material:widegap-semiconductor
- method:aimd
- task:application
- scale:atomistic
paper_keywords:
- keyword:aimd
- keyword:dft-static
- keyword:graphene-carbon
- keyword:catalysis-surface
candidate_tags: []
source_refs: []
doi: 10.1039/C8CP02786B
year: 2018
authors:
- D. G. Sangiovanni
- G. K. Gueorguiev
- A. Kakanakova-Georgieva
venue: Phys. Chem. Chem. Phys.
pdf_sha256: eff62eaf2d722eba49c4f3e8e39bf24edcc117eea0e3bc83dba034b535aa7d78
pdf_path: papers/Others/PCCP-20-17751-AIMD AlN-on-graphene.pdf
extraction_quality: good
group_affiliation: false
---
<!-- id:paper:2018sangiovanni-physical-che-ab-initio -->

## Summary

Supercells use ~27 Å vacuum, 6×6 graphene unit cells (72 C atoms), fixed in-plane lattice parameter 2.465 Å, Γ-point sampling, 300 eV plane-wave cutoff, total-energy convergence 10⁻⁵ eV/atom, and 0.1 fs / 1 fs timesteps depending on whether hydrogen dynamics are active. The elevated temperature accelerates rare surface reactions relative to typical MOCVD temperatures yet targets qualitative pathways on pristine graphene.

AlN MOCVD on graphene-related templates couples precursor pyrolysis with nucleation on sp\(^2\) carbon; *ab initio* MD at strongly elevated temperature accelerates rare events to sample trimethylaluminum, ammonia, and adduct chemistry on a model graphene slab. The reported VASP LDA + DFT-D3 setup with tight timesteps for hydrogen motion targets qualitative reaction sequences ahead of lower-temperature kinetics refinements. Consult the peer-reviewed PDF and any Supporting Information for authoritative tables, figures, and numerical diagnostics behind the summaries above.
## Methods

**Static QM / DFT setup (VASP).** **Density-functional** *ab initio* calculations use **VASP** with **LDA** (Ceperley–Alder as parametrized by Perdew–Zunger), **PAW** potentials, **Grimme DFT-D3** dispersion, and **Gaussian** electronic smearing at \(k_BT\) as reported. **Numerical settings** include a **300 eV** plane-wave cutoff, **Γ-only** **Brillouin** sampling, and **\(10^{-5}\) eV/atom** electronic convergence thresholds for the setups summarized on this page.

**AIMD application (Born–Oppenheimer trajectories).** **AIMD** explores gas-phase and surface reactions of **trimethylaluminum**, **ammonia**, and **adduct-derived (CH\(_3\))\(_2\)AlNH\(_2\)** on a **periodic** graphene **slab** with **~27 Å** vacuum separation, using a **6×6** graphene **unit cell** (**72 C atoms**) and an in-plane lattice constant **2.465 Å** as stated. **Temperature** is elevated to **\(T = 4300\) K** in the reported “hot dynamics” protocol to accelerate rare events while staying below the authors’ cited graphene-melting concern. **Integration timesteps** are **0.1 fs** when **H** motion is active and **1 fs** for lighter **Al/C** adatom diffusion studies. **Sampling** is finite-temperature **Born–Oppenheimer molecular dynamics** in the **canonical** sense used for constant-\(T\) *ab initio* sampling in **VASP** (**N/A — the exact thermostat implementation string and total trajectory lengths in ps** should be copied from the *PCCP* **Methods** rather than inferred from the p1–2 extract alone). **PBC:** **three-dimensional periodic** boundary conditions for the **slab** supercell. **Ensemble / pressure:** **constant-volume** **supercell** with controlled **temperature** (**N/A — explicit NPT barostat and external stress control** not used in the AIMD description excerpted here). **Electric field:** **N/A — not used** as an MD bias in the indexed excerpt. **Enhanced sampling:** **N/A — umbrella / metadynamics / replica exchange** not indicated for the AIMD sets described on pages 1–2 of the extract; the study instead relies on **high-temperature** **AIMD** to access rare reactive events.
## Findings

AIMD highlights precursor fragmentation and surface delivery pathways for Al, C, and mixed Al–C–N hydrogenic species on graphene, with charge-transfer arguments for Al attachment. Carbon adatoms exchange with graphene lattice atoms, enabling through-sheet transport with Arrhenius parameters reported in the abstract (~0.28 ± 0.13 eV barrier, ~2.1 THz prefactor at experimental-referenced conditions). NH3 does not strongly activate pristine graphene in the simulated trajectories, suggesting limited N delivery without defects.

**Comparisons and caveats.** The abstract explicitly connects simulated **rates** and **activation energies** for **C** exchange/permeation to **Arrhenius** analysis and **experimentally referenced** temperature scales, while stressing that **AIMD** is used as an interpretive tool for **MOCVD** chemistry rather than a direct room-temperature production **kinetic** model. **Sensitivity:** the study’s conclusions depend strongly on the chosen **elevated temperature** acceleration strategy and on the **LDA + DFT-D3** treatment of **graphene** and **precursor** chemistry—**limitations** of **LDA** for **reaction** energetics are discussed in the article framing. **Corpus honesty:** this page is grounded in the checked-in **PDF**/`normalized/extracts/2018sangiovanni-physical-che-ab-initio_p1-2.txt`; **figures**, **longer trajectories**, and **complete parameter tables** should be taken from the **version-of-record** **PDF** on `pdf_path`.
## Limitations

Very high simulation temperature and short trajectories trade realism of kinetics for sampling; LDA errors for chemistry and graphene electronic structure are acknowledged implicitly by the authors’ validation narrative.

## Relevance to group

Provides AIMD reference chemistry for III-nitride growth on carbon supports, adjacent to ReaxFF/MOCVD workflows.

## Citations and evidence anchors

- DOI: [10.1039/C8CP02786B](https://doi.org/10.1039/C8CP02786B)

## Related topics

- [[reaxff-family]]
- [[graphene-nanocarbon]]
