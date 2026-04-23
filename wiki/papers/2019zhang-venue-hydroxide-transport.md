---
id: paper:2019zhang-venue-hydroxide-transport
type: paper
title: "Hydroxide transport and chemical degradation in anion exchange membranes: a combined reactive and non-reactive molecular simulation study"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:batteries-electrochemistry
  - domain:classical-ff-specialized
  - method:reaxff
  - material:polymer-organic
  - task:application
  - scale:atomistic
paper_keywords:
  - keyword:batteries-interfaces
  - keyword:polarizable-ff
  - keyword:charge-equilibration
  - keyword:water-interfaces
  - keyword:galley-or-proof-pdf
candidate_tags: []
source_refs: []
doi: "10.1039/C8TA10651G"
year: 2019
authors:
  - "Zhang, Weiwei"
  - "Dong, Dengpan"
  - "Bedrov, Dmitry"
  - "van Duin, Adri C. T."
venue: "J. Mater. Chem. A"
pdf_sha256: "55f37b597a40f7554fe2296df9df9c081df21bf98843b3ab765ae1ac085b5f5e"
pdf_path: "papers/Zhang_JMatChemA_2019_proof.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2019zhang-venue-hydroxide-transport -->

!!! note "Corpus note"

The local PDF is a publisher proof; scientific claims below follow the published article abstract and citation.

## Summary

The paper studies hydroxide transport and chemical degradation in model anion-exchange membranes (AEMs) using atomistic molecular dynamics that combine a polarizable, non-reactive force field (APPLE&P) with reactive ReaxFF simulations, including proton-hopping-enabled reactive dynamics for hydroxide and water. Four AEM chemistries built on poly(phenylene oxide) backbones with different cationic side-chain architectures are compared to separate transport bottlenecks from chemical stability trends relevant to alkaline membrane fuel cells. Aqueous OH\(^-\) in concentrated base shows hypercoordinated solvation motifs that stress fixed-charge and legacy water models; the authors position updated ReaxFF water parametrization (with proton hopping) as a practical bridge where full *ab initio* Grotthuss sampling is too costly at membrane-relevant length scales. Tables and run parameters belong in the peer-reviewed PDF and SI.

## Methods

Molecular dynamics (LAMMPS-class engine as in the manuscript) is applied to hydrated poly(phenylene oxide)–based AEM **supercells** with 3D periodic boundaries, concentrated **KOH**/**NaOH** solutions, and **temperature** near **300 K** for classical NVT legs with Nose–Hoover–style thermostats; production timescales are **ns**-order in *J. Mater. Chem. A* **Methods**. System size and **stoichiometry** follow the four AEM chemistries in the paper. Non-reactive polarizable **APPLE&P** runs report structure, water self-diffusion, and OH⁻ mobility. Parallel **ReaxFF** simulations, including a proton-hopping extension, explore reactive hydroxide transport and **degradation** selectivity; the study contrasts APPLE&P and ReaxFF to separate Grotthuss-like pathways from bond-making/breaking limits. **N/A** on this page for the full per-leg **timestep** and NVT vs NPT split—use the article and **SI**. **Barostat**/**osmotic** **pressure** matching: **N/A** here unless the text uses NPT. **External electric field** in MD: **N/A** unless stated. **Umbrella**/**metadynamics**: **N/A**; rare-event behavior is encoded in the **FF** choice, not a separate **enhanced sampling** method in the abstract-level summary.

## Findings

Comparisons between APPLE&P and ReaxFF results emphasize the importance of Grotthuss-type mechanisms for hydroxide and associated water dynamics in congested channels. With proton hopping enabled in ReaxFF, hydroxide traverses bottlenecks more readily without shedding coordinating waters to the same extent as in simulations lacking that physics. Reactive screening of degradation suggests improved **chemical** **stability** for **cations** attached to **larger** **hydrophobic** **moieties**, motivating **trade-offs** between **ion** **transport** and **backbone** **durability**. The authors connect **trends** in **Grotthuss**-like **OH⁻** **mobility** to **bottleneck** **morphology** in **AEMs**; **sensitivity** is to **concentration**/**hydration** **state** in the **simulated** **cell**, not a single **experimental** **current** **sweep** on this page. **Corpus honesty:** this file tracks a **proof**-stage **PDF**; for **version-of-record** **numbering** use the final **J. Mater. Chem. A** issue once aligned in your library.

## Limitations

Proof-stage PDFs can differ slightly from the version of record; numerical parameters (system sizes, simulation lengths, thermostat algorithms) should be confirmed against the final publication and supporting information.

## Relevance to group

Core van Duin-group contribution on eReaxFF/ReaxFF treatment of hydroxide and water in polymer electrolytes, directly relevant to electrochemical interface modeling in the corpus.

## Citations and evidence anchors

- https://doi.org/10.1039/C8TA10651G

## Related topics

- [[reaxff-family]]
- [[batteries-interfaces-reaxff]]
