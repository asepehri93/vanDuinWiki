---
id: paper:2019khajeh-j-phys-chem-statistical-analysis
type: paper
title: "Statistical Analysis of Tri-Cresyl Phosphate Conversion on an Iron Oxide Surface Using Reactive Molecular Dynamics Simulations"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:catalysis-surfaces
  - domain:mechanics-tribology
  - method:reaxff
  - task:parameterization
  - task:application
candidate_tags: []
paper_keywords:
  - keyword:reaxff-parameterization
  - keyword:qm-training-data
  - keyword:reaxff-application
  - keyword:lammps
  - keyword:tribology
source_refs: []
doi: "10.1021/acs.jpcc.9b02394"
year: 2019
authors:
  - "Arash Khajeh"
  - "Xiaoli Hu"
  - "Karen Mohammadtabar"
  - "Yun Kyung Shin"
  - "Adri C. T. van Duin"
  - "Stephen Berkebile"
  - "Ashlie Martini"
venue: "The Journal of Physical Chemistry C"
pdf_sha256: "572f469a0bde9d7ff2f8776262f5b53d43dc078af73c94df795ac2e8f63cfac9"
pdf_path: "papers/Khajeh_FeO_Phosphate_JPCC_2019.pdf"
extraction_quality: "good"
group_affiliation: true
---
<!-- id:paper:2019khajeh-j-phys-chem-statistical-analysis -->

The authors fit ReaxFF parameters for Fe–P–O chemistry relevant to tri-cresyl phosphate (TCP) on amorphous iron oxide, then run one hundred independent LAMMPS replicas to build temperature-resolved statistics of which TCP atoms form load-bearing bonds to the surface.

## Summary

The paper develops a ReaxFF description of Fe/P/O interactions for TCP chemisorption on passivated amorphous iron oxide and applies it in one hundred parallel NVT molecular dynamics simulations, each containing a single TCP molecule above the same substrate realization. Initial orientations split evenly between P=O-down and P=O-up poses. Simulations follow a temperature ladder from 300 K to 700 K in 100 K steps, with up to one nanosecond per stage until bond populations plateau, higher-temperature runs restarted from lower-temperature final frames, and Nosé–Hoover thermostats acting on non-fixed atoms. The study contextualizes site-resolved bonding statistics with experimental TCP tribofilm formation under oxygen-poor conditions.

## Methods

**Force-field training (2).** **Parent / scope:** new **ReaxFF** terms for **Fe–P–O** chemistry. **DFT** reference: training data for **Fe–O–P** angles, **Fe–P** dissociation, **Fe(II)/Fe(III)–O–P** bending, and **P/PO** adsorption on **iron** facets; **Table 1** and **Figure 2** give **ReaxFF** vs **DFT** errors; parameters in **SI**. **Optimization / fit:** standard **ReaxFF** **least-squares** optimization as described in the article. **Substrate:** one **passivated amorphous** **Fe\(_x\)O\(_y\)** slab.

**MD application (1).** **Engine:** **LAMMPS** **RMD** with **0.25 fs** timestep; **bond order** every **1.25 ps** (cutoff **0.3**). **System / composition:** one **TCP** per cell on the **oxide** slab; **100** independent replicas, **P=O**-down vs **P=O**-up **50/50** initial orientations. **Boundaries / PBC** and fixed **substrate** atoms as in the **PDF** (periodic in-plane; bottom layers **frozen** or constrained per article). **Ensemble:** **NVT**; **Nose–Hoover thermostat** on **non-fixed** atoms. **Barostat / mean pressure / stress control:** **N/A** — **NVT** only. **Duration:** **temperature** ladder **300–700 K** in **100 K** steps, **~1 ns** per stage to plateau; **last ~25 ps** of each steady window averaged. **Electric field:** **N/A**. **Replica / parallel ensemble:** 100 **replica** **MD** (not **metadynamics** or **replica exchange** for enhanced sampling — **N/A** for those).

**DFT (3).** **Training** **DFT** is cited above; this paper is **RMD**-centered, not a standalone static **QM** **benchmark** study.
## Findings

Among heteroatom bonds tracked for film-growth metrics, Fe–C contacts are the most probable, while hydrogen-mediated contacts are excluded as non-load-bearing. Raising temperature from 300 K to 700 K increases overall TCP–surface bonding but shifts the dominant attachment sites from aryl carbons (notably C5/C6) toward phosphoryl oxygens at the highest temperature. The replica ensemble produces site-resolved histograms that short single trajectories cannot sample reliably. The abstract notes that parallel replica statistics should preserve relative reaction probabilities compared with one long serial trajectory, echoing prior work cited in the introduction on time-parallel MD for surface chemistry.

## Limitations

Only one disordered oxide morphology is modeled, and the simulations omit shear or pressure from sliding contact, so tribological load transfer is represented through static thermal sampling rather than mechanochemical conditions.

## Relevance to group

**van Duin** / **Shin** **ReaxFF** **development** for **aviation** **lubricant** **additive** chemistry on **ferrous** **surfaces**.

## Citations and evidence anchors

- `papers/Khajeh_FeO_Phosphate_JPCC_2019.pdf`

## Related topics

- [[reaxff-family]]

## Reader notes (navigation)

- Sibling **proof** PDF: [[2019khajeh-x-statistical-analysis]]; cite **VOR** for final figure pagination.
