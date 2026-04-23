---
id: paper:2023bertolini-j-phys-chem-unraveling-molecular
type: paper
title: "Unraveling the Molecular Dynamics of Glucose Oxidase Desorption Induced by Argon Cluster Collision"
updated: "2026-04-22"
confidence: high
canonical_tags:
  - domain:methods-software
  - method:reaxff
  - task:application
  - material:polymer-organic
  - scale:atomistic
paper_keywords:
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:reactive-md
candidate_tags:
  - "protein-desorption"
source_refs: []
doi: "10.1021/acs.jpcb.3c04857"
year: 2023
authors:
  - "Samuel Bertolini"
  - "Arnaud Delcorte"
venue: "Journal of Physical Chemistry B 127, 9074–9081 (2023)"
pdf_sha256: "6ab41f283c69193d2a086c26078d95c8e4edb24b0f5d1a63efc2a84831ba9a7b"
pdf_path: "papers/ReaxFF_others/bertolini-delcorte-2023-unraveling-the-molecular-dynamics-of-glucose-oxidase-desorption-induced-by-argon-cluster.pdf"
extraction_quality: "good"
group_affiliation: false
---
<!-- id:paper:2023bertolini-j-phys-chem-unraveling-molecular -->

## Summary

Secondary ion mass spectrometry and related cluster-beam methods can desorb large biomolecules from surfaces, but predicting how much native structure survives requires atomistic models that capture bond breaking and reformation during energetic collisions. This Journal of Physical Chemistry B article applies LAMMPS with ReaxFF to simulate argon cluster bombardment of glucose oxidase (GOx) on gold and on a lysozyme organic underlayer, motivated by cluster-induced soft landing and ion-beam contexts. The authors refine ReaxFF parameters against density functional theory dissociation energetics for fragments where nitrogen–sulfur and oxygen–sulfur interactions matter in the protein. Cluster sizes span **1000 to 10 000** argon atoms at incident kinetic energies of **1.5** and **3.0 eV per atom**, bracketing regimes where desorption becomes probable but damage remains a concern. Large protein systems push ReaxFF to its practical limits, so the paper is as much a methods stress test as an application note for SIMS community readers.

## Methods

### ReaxFF refinement against QM (A)

- **Targets:** **DFT** **dissociation** curves for **fragments** where **N–S** and **O–S** interactions matter in **glucose oxidase** chemistry; **ReaxFF** parameters are adjusted accordingly (see *J. Phys. Chem. B* **Methods/SI** for **functional/basis** of reference data).

### Cluster–surface collision MD (B)

- **Engine:** **LAMMPS** with **ReaxFF** for **protein**/**Au**/**organic** interactions.
- **Projectiles:** **Ar** clusters from **1000** to **10 000** atoms; incident energies **1.5** and **3.0 eV per atom** (per abstract).
- **Substrates:** **GOx** on **Au(111)**-like **metal** vs **GOx** on **lysozyme** organic **underlayers**.
- **Analysis:** **Backbone** integrity, **fragment** distributions, **desorption** vs **damage**; **sampling** limits and **replicate** counts are discussed in the article.

### MD application (integrated)

**Engine / code:** **LAMMPS** with **ReaxFF**. **System & composition:** **GOx** on **Au(111)**-like **metal** vs **GOx** on **lysozyme** **underlayers**; **Ar** projectiles from **1000** to **10 000** atoms; **N/A — full atom counts and box vectors** in the paper’s *Computational* section (not repeated here). **PBC** as in the **J. Phys. Chem. B** setup. **Ensemble:** pre-collision **NVT** or **NVE**-style equilibration and **collision** **dynamics** as in the article; **N/A — which stage is strictly NVE vs thermostated** in every segment—**see PDF**. **Timestep, multi-stage equilibration/collision, thermostat/barostat, total simulated time (ps/ns):** **N/A in this wiki line item**—read the **version-of-record** PDF. **Initial/target temperature (K), pressure, stress control:** as in the article; **N/A — exact** **K**/**bar** on this stub. **N/A — static electric field; N/A — umbrella / metadynamics / replica exchange** (not the collision protocol here).

## Findings

### Cluster size threshold

Clusters **≥ ~7000 Ar atoms** can **desorb GOx** from **bare Au** under the modeled conditions, often with **heavy fragmentation** or **denaturation**.

### Soft underlayer effect

**Organic** **underlayers** decouple rigid **Au** constraints and enable **desorption** with **greater structural preservation**, aligning with **SIMS** community experience that **compliant** supports reduce **collisional damage**.

### Reparameterization takeaway

Tailored **ReaxFF** terms for **N–S**/**O–S** interactions address gaps in **default** **biomolecular** training sets for these **heteroatom**-rich **collision** scenarios. **Experimental** **SIMS** context is discussed in the **article**; **comparisons** to measured **yields** are **qualitative** at the MD level.

## Limitations

ReaxFF remains approximate for proteins; quantitative agreement with experiment requires cross-validation. Large-system reactive MD is expensive, so statistical convergence is limited. Cluster impact simulations may require multiple random seeds to estimate desorption probabilities robustly. Substrate temperature coupling may differ between Au and organic underlayers in extended studies.

## Relevance to group

Shows ReaxFF applied to biomolecule collisional desorption in SIMS-adjacent regimes.

## Citations and evidence anchors

- DOI: [10.1021/acs.jpcb.3c04857](https://doi.org/10.1021/acs.jpcb.3c04857)

## Related topics

- [[reaxff-family]]
