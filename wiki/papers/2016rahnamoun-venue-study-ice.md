---
id: paper:2016rahnamoun-venue-study-ice
type: paper
title: "Study of ice cluster impacts on amorphous silica using the ReaxFF reactive force field molecular dynamics simulation method"
updated: "2026-04-20"
confidence: med
canonical_tags:
  - domain:water-silica-geo
  - domain:mechanics-tribology
  - domain:reaxff-lineage
  - method:reaxff
  - material:silicate-glass
  - task:application
  - scale:atomistic
candidate_tags: []
source_refs: []
doi: "10.1063/1.4942997"
year: 2016
authors:
  - "A. Rahnamoun"
venue: "J. Appl. Phys."
pdf_sha256: "6d98de3d50f6099e3101f965173da0fc23186c21b93c454939a2cc113f1b7772"
pdf_path: "papers/Rahnamoun_JAP_2016.pdf"
extraction_quality: good
group_affiliation: false
---

<!-- id:paper:2016rahnamoun-venue-study-ice -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

**ReaxFF MD** is used to simulate **high-velocity impacts of ice clusters** onto **amorphous silica** substrates, targeting **mechanochemical damage** and **hydrogen-bond-mediated contact mechanics** relevant to **icy-body impacts**, **cryogenic engineering**, or **tribological** scenarios involving **water ice + silica**. The publication analyzes **energy dissipation**, **substrate disruption**, and **reactive events** enabled by the **reactive force field** that would be invisible to **fixed-bond silica models**.

## Methods

- **Reactive MD (ReaxFF)** with **cluster impact** initial conditions (mass, velocity, and cluster construction as specified in the article).
- Post-processing of **local densification**, **bond-breaking**, and **ejecta** statistics.

The article further notes that the analysis examines the dynamics of the collisions between amorphous silica structures and amorphous and crystal ice clusters with impact velocities of 1 km/s, 4 km/s, and 7 km/s using the ReaxFF reactive molecular dynamics simulation method. Observing the temperatures of the ice clusters during the collisions indicates that the possibility of electron excitement at impact velocities less than 10 km/s is minimal and ReaxFF reactive molecular dynamics simulation can predict the chemistry of these hypervelocity impacts. However, at impact velocities close to 10 km/s the average temperature of the impacting ice clusters increase to about 2000 K, with individual molecules occasionally reaching temperatures of over 8000 K and thus it will be prudent to consider the concept of electron excitation at these higher impact velocities, which goes beyond the current ReaxFF ability. The complications in the simulations of such interac- tions are related to the high energy transfer to the surface and the changes in the colliding cluster during the collision. The important parameter in these impacts is the stopping force exerted on the colliding species. However, these phenomena can be studied using classical molecular dynamics simulations 0021-8979/2016/119(9)/095901/9/$30.00 VC 2016 AIP Publishing LLC119, 095901-1 JOURNAL OF APPLIED PHYSICS 119, 095901 (2016) Reuse of AIP Publishing content is subject to the terms at: https://publishing.aip.org/authors/rights-and-permissions. The initial ice clusters consist of 150 water molecules for the amorphous ice cluster and 128 water molecules for the crystal ice cluster. The ice clusters are collided on the surface of amorphous fully oxidized and suboxide silica. At 4 km/s and 7 km/s impact velocities, few of the water molecules dissociations are observed. The effect of the second ice cluster impacts on the surfaces which are fully covered with ice, on the mass loss/accumulation is studied.

## Findings

- The article documents how **ice cluster impacts** drive **non-trivial chemistry and mechanical modification** of **a-SiO2** in the simulated parameter ranges (see paper for threshold velocities and damage morphologies).


From the abstract: these simulations show that at 1 km/s impact velocities, all the ice clusters accumulate on the surface and at 4 km/s and 7 km/s impact velocities, some of the ice cluster molecules bounce back from the surface. These studies show that at 1 km/s impacts, the entire ice cluster accumulates on the surface at both ﬁrst and second ice impacts. Collisions of clusters on the surface of spacecrafts can happen at the velocities up to 17 km/s and such collisions can cause thermal activation chemistry with the time scale of the order of vibrations of the nuclei. This means that at such impacts the activation process is thermal and it takes place on a very short time scale. During impact, high relative velocities and high densities for the cluster takes place and the dynamics of such condition should be considered. This stopping force is a function of speed for colliding species, but because of the dependence of the stopping force on the shape of the clusters and the change in the shape of the clusters, the relationship between the stopping force and cluster velocity is quite complex. External kinetic energy is the energy of the clusters as a moving mass while internal kinetic energy is measured in a coordinate system which moves with the clusters center of mass and it is associated with the particles thermal motion. Therefore, the kinetic temperature corresponding to the total kinetic energy of the cluster is divided into two parts, namely, thermal temper ature and translational tem- perature. In this study, we focus on the effects of external kinetic energy on the cluster- surface interactions during the impacts. Due to the complexity of the dynamics of these interac- tions, a straightforward interpretation of experimental results is usually not possible.

## Limitations

- **Classical reactive** treatment of **ice** and **proton disorder** omits **full nuclear quantum effects** unless separately augmented.
- **Cluster geometry / crystallinity** strongly affects outcomes.

## Relevance to group

Corpus **ReaxFF application** connecting **water/ice** chemistry with **silica mechanics**, useful alongside **Langmuir tribochemistry** and **geochemical interface** entries.

## Citations and evidence anchors

- Bibliographic metadata in `normalized/papers/2016rahnamoun-venue-study-ice.json` and abstract in `papers/Rahnamoun_JAP_2016.pdf`; **DOI:** `10.1063/1.4942997`.

## Related topics

- [[reaxff-family]]