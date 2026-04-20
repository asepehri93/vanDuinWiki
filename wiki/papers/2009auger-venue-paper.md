---
id: paper:2009auger-venue-paper
type: paper
title: "Mechanisms of Auger-induced chemistry derived from wave packet dynamics"
updated: "2026-04-20"
confidence: low
canonical_tags: [domain:carbon-hydrocarbon, domain:methods-software, method:reactive-md-generic, scale:atomistic, task:application]
candidate_tags: []
source_refs: []
doi: "10.1073/pnas.0812087106"
year: 2009
authors: ["Su, Julius T.", "Goddard, William A., III"]
venue: "Proceedings of the National Academy of Sciences"
pdf_sha256: "9ad920f4eaabb8e5544142cb63b323f4e46ded2711aa32eaf47a6b49f54bb96e"
pdf_path: "papers/Others/Auger_eFF_Su_PNAS.pdf"
extraction_quality: partial
group_affiliation: false
---

<!-- id:paper:2009auger-venue-paper -->



## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

This PNAS contribution uses the **electron force field (eFF)**—a dynamics model in which electrons are represented as floating Gaussian wave packets and nuclei move classically—to follow Auger-related relaxation after core ionization in a hydrogen-terminated diamond nanoparticle **C₁₉₇H₁₁₂**. The work distinguishes **surface** core ionizations (leading toward fragment and proton emission via a direct Auger picture) from **deeper** ionizations (hydrides emitted via “remote heating”), and discusses consistency with photon-stimulated desorption literature. The opening pages also summarize the eFF equations of motion and show ground-state electron density comparisons to DFT for simple hydrocarbons.

## Methods

- **eFF / fermionic molecular dynamics:** Valence and core electrons are modeled as spherical Gaussian wave packets; a Pauli exclusion term controls overlap-dependent repulsion; parameters are referenced as fitted to small-molecule ground-state data in the article.
- **System:** Hydrogenated diamond nanoparticle **C₁₉₇H₁₁₂** with selective core removal at surface vs subsurface sites to probe distance-dependent relaxation and desorption channels.
- **Core-hole lifetime:** The extract reports a modeled CH₄ core-hole lifetime example and compares to experimental linewidth-based estimates.

<!-- enrich-from-extract:v2 -->

- In our simple model, we account for the possible variation ofm elec by performing simulations for multiple ﬁxed melec .
- The Pauli potential is a function of the overlap between electrons, as well as their respec- tive sizes, and contains three parameters set to reproduce the ground-state geometries of small molecules such as CH 4,C 2H6, LiH, and B 2H6.
- For diamond and hydrocarbons, the eFF Pauli potential causes the electrons to segregate naturally into core and valence shells, with electron density proﬁles similar to density functional theory (Fig. 1 B).
- (B) Comparison of electron densities between eFF and density functional theory (B3LYP/6-311g**) along a carbon–hydrogen bond in methane, and along a carbon–carbon bond in ethane. electrons, only one (green) wins; the others bounce away from the now-ﬁlled core.
- We report now the application of eFF to study Auger processes in a hydrogenated diamond nanoparticle C 197H112 (Fig. 1A).
- In the Auger process, ionization of a core electron leads to the collapse of a valence electron into the core hole, together with the ejection of another valence electron, all over several femtoseconds (5).
- Dur- ing and after this time, secondary processes occur, causing protons, hydrides, and other species to desorb from hydrogen-terminated surfaces (1).
- We study the coupled electron-nuclear dynamics of both the primary Auger and accompanying secondary processes, ionizing core electrons both at the diamondoid surface and at dif- ferent depths below the surface.
- In this way, we determine how the distance over which an Auger excitation relaxes and propa- gates affects the energies of electrons and composition of atomic species desorbed from the surface.
- In eFF , all electrons, valence and core, are modeled as spherical Gaussian wave packets: /Psi1(r) ∝ ∏ i exp [ − ( 1 s2 i − 2ps,i si i ) (r − xi)2 ] · exp[ipx,i · r], while nuclei are modeled as classical charged particles moving in the mean ﬁeld of the electrons.


## Findings

- Surface vs depth-dependent core ionization is argued to produce qualitatively different desorption channels (direct Auger-related emission vs heating-driven emission), linking simulation to experimental PSD themes.
- Illustrative dynamics on the nanoparticle show core-hole filling, secondary electron ejection, and lingering valence excitation over tens of femtoseconds in the excerpted trajectory discussion.

### Additional results (article abstract)

- The positions xi and sizes si of the electrons are continuously variable, giving them the ﬂexibility to participate in covalent, ionic, multicenter, and even metallic bond- ing; p x,i and ps,i are the corresponding conjugate momenta.
- The parameters are the same for all electrons, and for all systems studied (4). eFF may be viewed as an elaboration of fermionic molecu- lar dynamics methods (7, 8), using a Pauli potential accurate enough that condensed systems with Z > 1 can be described; or as an approximate and time-dependent version of ab initio ﬂoat- ing spherical Gaussian orbital (FSGO) theory (9), with exchange energy estimated as a pairwise sum.
- Fig. 2 shows for a C 196H112 nanoparticle the dynamics of a core hole state evolving continuously into a two valence hole state.
- One electron (red) feels the strongest repulsion, causing it to break free as an Auger electron, only to be trapped 20 fs later in the particle ∼ 3 Å away, with its energy dissipated among the other electrons of the solid (not shown in the ﬁgure).
- Results Ground states may be obtained from damped electron dynamics, or more efﬁciently by minimizing the overall energy with respect to the electron parameters.
- Potential energies of eFF electrons may be compared with the energies of Hartree–Fock (HF) Boys-localized orbitals: for the 1 s, CH, and CC electrons of ethane, we have from eFF 237, 13.8, and 17.7 eV and from HF 305, 17.5, and 18.5 eV .
- Hence, CC electrons are properly bound, but CH and core electrons are underbound by ∼ 20%, probably from the limited ability of single Gaussian functions to form cusps at nuclear centers (for H atom this leads to an error of 15%).
- At time zero, a 1s electron with down spin is removed from the central carbon of the nanoparticle, which induces the down-spin electrons in the surrounding bonds to race inward to ﬁll the hole.
- Of the four Author contributions: J.T.S. and W.A.G. designed research; J.T.S. performed research; and J.T.S. and W.A.G. wrote the paper.
- The authors declare no conﬂict of interest. 1 To whom correspondence should be addressed.


## Limitations

- The normalized record marks extraction as **partial**; quantitative numbers beyond the excerpt should be verified in the full PDF.
- This is **not** a ReaxFF study; methodology is eFF-specific and should not be conflated with reactive bond-order force fields.

## Relevance to group

Provides a precedent for **large-scale excited-state surface chemistry** modeling using inexpensive dynamical models, complementary to reactive FF workflows used elsewhere in the corpus for ground-state bond making/breaking.

## Citations and evidence anchors

- Opening abstract and introduction: Auger mechanisms, C₁₉₇H₁₁₂ model, PSD comparison (PDF pp. 1–2 per extract scope).

## Related topics

- [[reaxff-family]]
