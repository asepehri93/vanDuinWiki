---
id: paper:2009auger-venue-paper
type: paper
title: "Mechanisms of Auger-induced chemistry derived from wave packet dynamics"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:carbon-hydrocarbon, domain:methods-software, method:reactive-md-generic, scale:atomistic, task:application]
candidate_tags: []
source_refs: []
doi: "10.1073/pnas.0812087106"
year: 2009
authors: ["Su, Julius T.", "Goddard, William A., III"]
venue: "Proceedings of the National Academy of Sciences"
pdf_sha256: "9ad920f4eaabb8e5544142cb63b323f4e46ded2711aa32eaf47a6b49f54bb96e"
pdf_path: "papers/Others/Auger_eFF_Su_PNAS.pdf"
extraction_quality: "partial"
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

**Model system and scientific question.** The study applies the **electron force field (eFF)** to a hydrogen-terminated diamondoid cluster **C\(_{197}\)H\(_{112}\)** (Fig. 1A in the article). Core electrons are **selectively ionized** at the **surface** and at **variable depths below the surface** so the authors can compare how **relaxation distance** and **energy flow** influence **which atomic species desorb**.

**eFF dynamics (QM-inspired wave-packet + nuclear dynamics).** In eFF, **valence and core electrons** are represented as **spherical Gaussian wave packets** with variable **positions**, **sizes**, and **momenta**, while **nuclei** move as **classical** charges in the mean field of the electrons. A **Pauli exclusion** potential between wave packets is parameterized (three parameters) to reproduce **ground-state geometries** of small molecules such as **CH\(_4\)**, **C\(_2\)H\(_6\)**, **LiH**, and **B\(_2\)H\(_6\)**; the same parameter set is used for all electrons and systems in the excerpted description. The Hamiltonian includes **electrostatics**, **electron kinetic** terms that penalize overly compact Gaussians, and the Pauli term (see the article’s Materials and Methods for the full energy expression). **Effective electron mass** \(m_{\mathrm{elec}}\) can be varied; the excerpt reports **multiple fixed** \(m_{\mathrm{elec}}\) choices to probe time scaling while preserving the **sequence of events** (core-hole filling, secondary electron ejection, subsequent excitation).

**1 — MD application (classical production MD checklist).** This is **not** a classical fixed-charge or ReaxFF MD benchmark. **N/A — classical timestep, thermostat/barostat, PBC supercell vectors, and NVE/NVT/NPT control** are not the organizing variables in the indexed pages; integration details beyond the eFF equations belong in the full **PNAS** PDF. **N/A — hydrostatic pressure / stress tensor control** for the nanoparticle studies. **N/A — external electric field** as a controlled MD bias. **N/A — umbrella / metadynamics / replica exchange**. **Femtosecond-scale** dynamics are discussed for **Auger** primary steps.

**2 — Force-field training.** **N/A —** eFF is a distinct model class from empirical **bond-order/ReaxFF** fits; training/validation against **HF**/**DFT** references is discussed qualitatively in the excerpt (e.g. **B3LYP/6-311G\*\*** electron-density comparisons along **C–H** and **C–C** bonds in **methane/ethane**).

**3 — Static QM / DFT-only block.** **N/A —** DFT appears as a **reference** for ground-state densities/energies, not as the main dynamics engine for the large nanoparticle trajectories excerpted here.

**Checklist closure (indexed pages).** **Engine / workflow:** the model is positioned as comparable in spirit to tools used for **classical molecular dynamics**, but implemented as **eFF wave-packet dynamics** (not a named MD package here). **Duration / stages:** primary Auger events are discussed on **femtosecond** scales with follow-on dynamics illustrated to **~50 fs** (**~0.05 ps**). **Temperature:** **300 K** appears for the quoted **CH\(_4\)** core-hole lifetime statistics in the excerpt.

## Findings

**Primary mechanistic distinction.** **Surface** core ionizations tend to drive **fragment and proton emission** through a **direct Auger** picture, whereas **deeper** core ionizations lead to **hydride** emission via **“remote heating,”** described as **consistent with photon-stimulated desorption** literature cited in the abstract.

**Illustrative excited-state trajectory content (indexed pages).** For a **C\(_{196}\)H\(_{112}\)** illustration, a **core-hole** configuration evolves within **femtoseconds** toward a **two-valence-hole** situation; one electron can depart as an **Auger electron**, be **re-trapped ~3 Å** away after about **20 fs**, and dissipate energy into the remaining electronic bath, while other electrons remain **highly excited** after **50 fs** in the quoted figure narrative.

**Model validation snippets.** Ground states can be obtained by **damped electron dynamics** or **direct minimization** over electron parameters. **eFF vs HF (Boys-localized)** potential energies for **ethane** valence/core-like assignments are quoted in the text (e.g. **237, 13.8, 17.7 eV** from eFF vs **305, 17.5, 18.5 eV** from HF for the 1s/CH/CC-like entries as printed), with the authors noting **~20% underbinding** for CH/core channels attributed partly to **Gaussian cusp limitations**.

**Corpus honesty.** Statements here track **`pdf_path`** and `normalized/extracts/2009auger-venue-paper_p1-2.txt` (early article + partial Results). **Materials and Methods** integration parameters, statistics over large trajectory ensembles, and PSD quantitative comparisons require the **full PDF**.

## Limitations

- The normalized record marks extraction as **partial**; quantitative numbers beyond the excerpt should be verified in the full PDF.
- This is **not** a ReaxFF study; methodology is eFF-specific and should not be conflated with reactive bond-order force fields.

## Relevance to group

Provides a precedent for **large-scale excited-state surface chemistry** modeling using inexpensive dynamical models, complementary to reactive FF workflows used elsewhere in the corpus for ground-state bond making/breaking.

## Citations and evidence anchors

- Opening abstract and introduction: Auger mechanisms, C₁₉₇H₁₁₂ model, PSD comparison (PDF pp. 1–2 per extract scope).

## Related topics

- [[reaxff-family]]
