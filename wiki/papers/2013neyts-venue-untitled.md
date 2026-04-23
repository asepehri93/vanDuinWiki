---
id: paper:2013neyts-venue-untitled
type: paper
title: "Defect healing and enhanced nucleation of carbon nanotubes by low-energy ion bombardment"
updated: "2026-04-20"
confidence: high
canonical_tags:
  - domain:2d-layered
  - domain:reaxff-lineage
  - method:reaxff
  - material:graphene-carbon-nano
  - task:experiment-integrated
  - task:application
  - scale:atomistic
candidate_tags: []
paper_keywords:
  - keyword:reaxff-application
  - keyword:graphene-carbon
  - keyword:reactive-md
  - keyword:nvt-simulation
  - keyword:berendsen-thermostat
  - keyword:validation-experiment
source_refs: []
doi: "10.1103/PhysRevLett.110.065501"
year: 2013
authors:
  - "E. C. Neyts"
  - "K. Ostrikov"
  - "Z. J. Han"
  - "S. Kumar"
  - "A. C. T. van Duin"
  - "A. Bogaerts"
venue: "Physical Review Letters"
pdf_sha256: "b07853c02eeb14db2e1d9185a83a00af5dacce035f5b94a81acf9071aff4b367"
pdf_path: "papers/Neyts_CNT_collision_formation_PRL_2013.pdf"
extraction_quality: "good"
group_affiliation: true
---

<!-- id:paper:2013neyts-venue-untitled -->

## Evidence and attribution

!!! note "Evidence"

    Prose below summarizes the **peer-reviewed letter** (**DOI `10.1103/PhysRevLett.110.065501`**).

## Summary

**Ion bombardment experiments** and **reactive MD (ReaxFF)** on **growing SWCNT caps** show that **low-energy ions** can **heal** **intrinsic nucleation defects** and **enhance cap growth**—a **nonthermal** pathway distinct from high-\(T\) annealing. Matching **ion energy** windows appear in **simulation** and **experiment** under comparable **temperature** and **energy** settings, supporting a **nonthermal ion-induced network restructuring** picture rather than purely thermal annealing. The letter frames this as reconciling **growth** and **defect control** in **plasma-assisted** nanotube synthesis, where **ions** are ubiquitous but their **chemical** versus **thermal** roles are often debated.

## Methods

**Reactive MD** used **ReaxFF** for **C–C**, **C–Ni**, and **Ni–Ni** interactions (as in prior **CNT growth** work cited), with **Ar–C** and **Ar–Ni** interactions represented by a **purely repulsive Molière** pair potential (**Firsov** constants per the article). The initial structure is a **defected nascent SWCNT cap** on a **surface-bound Ni\(_{40}\)** cluster from earlier **field-enhanced growth** simulations, thermalized at **1000 K** with a **Berendsen** thermostat (**100 fs** coupling).

**Ar** impacts span **5–50 eV** in **5 eV** steps (**10** energies), with **200** consecutive impacts per run; each energy was repeated **10×** for statistics (**2000** impacts total in the aggregate protocol described). Each impact was integrated for **2.0 ps** with **0.1 fs** time step (**1.6 ps** **NVE** followed by **0.4 ps** dissipation to a bath), and the cluster was **rethermalized to 1000 K** between impacts. **Experiments** expose **CNTs** to low-energy ions under conditions chosen to match **temperature** and **energy** scales explored in simulation.

**System size & composition:** **Defected nascent SWCNT cap** on a **surface-bound Ni\(_{40}\)** cluster from prior **field-enhanced growth** simulations (as cited in the letter). **N/A —** full periodic cell vectors / total **atom** count beyond this cluster motif are not expanded on this wiki page—see **`papers/Neyts_CNT_collision_formation_PRL_2013.pdf`**.

**Boundaries / periodicity:** **N/A —** not restated here beyond the **cluster** framing in the indexed summary; confirm **PBC** usage in the **PRL** **Methods**.

**Barostat / pressure control:** **N/A —** **constant-volume** **cluster** dynamics with **NVE** segments per impact; no **NPT** hydrostatic control summarized for the impact legs.

**Electric field / enhanced sampling:** **N/A —** no applied **electric field**; no umbrella/metadynamics—statistics come from **repeated impacts**.

## Findings

**Outcomes and mechanisms:** Both **simulation** and **ion-beam experiments** support a **nonthermal** window in which **defect healing** and **enhanced cap/nucleation** occur, rather than only **net damage**. The letter emphasizes **quantitative** alignment between **model** and **experiment** when **process temperature** and **ion energy** are matched, interpreting the effect as **ion-induced network restructuring** rather than conventional high-\(T\) annealing alone.

**Comparisons:** **Simulation** vs **experiment** under matched **temperature** and **ion energy** scales; **Ar**–**C**/–**Ni** repulsion treated separately from **ReaxFF** as described in **## Methods**.

**Sensitivity / design levers:** **Ion energy** (**5–50 eV** window explored) and **process temperature** (**1000 K** bath in the simulation protocol described) are the primary knobs discussed for crossing between **healing**/**growth enhancement** vs damage regimes.

**Limitations and outlook:** **Reactive FF** limits capture of **electronic excitations**; **Ar**-only beams simplify real **plasmas** with multiple species (**## Limitations**).

**Corpus honesty:** **`normalized/extracts/2013neyts-venue-untitled_p1-2.txt`** supports the numerical **impact** protocol quoted above; **PRL**-length compression means additional validation lives in the **full text**/SI.

## Limitations

Reactive FF limits electronic excitation physics; experimental plasmas contain multiple ion/radical species beyond single **Ar**. The simulations also simplify **catalyst** and **substrate** complexity to a **cluster** model appropriate for **mechanistic** comparison rather than quantitative **throughput** predictions for industrial **furnace** conditions. **PRL**-length articles compress **protocol** detail; consult the **full text** and any **supporting** material for **complete** **impact** statistics, **thermostat** choices, and **convergence** tests that underpin the **quantitative** comparisons emphasized in the letter. For **external** **citation**, treat this wiki note as a **navigation** aid and rely on the **DOI-resolved** article for **pagination** and **figure** reproduction.

## Reader notes (navigation)

- [[reaxff-family]]
- [[graphene-nanocarbon]]
