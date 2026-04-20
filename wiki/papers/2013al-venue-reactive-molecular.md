---
id: paper:2013al-venue-reactive-molecular
type: paper
title: "Reactive molecular dynamics simulations of oxygen species in a liquid water layer of interest for plasma medicine"
updated: "2026-04-20"
confidence: med
canonical_tags: [domain:water-silica-geo, domain:reactive-md, method:reaxff, task:application, scale:atomistic]
candidate_tags: []
source_refs: []
doi: "10.1088/0022-3727/47/2/025205"
year: 2014
authors: ["Yusupov, M.", "Neyts, E. C.", "Simon, P.", "Berdiyorov, G.", "Snoeckx, R.", "van Duin, A. C. T.", "Bogaerts, A."]
venue: "Journal of Physics D: Applied Physics"
pdf_sha256: "5bc2241aadaaeee20dd7883c7173dbe0312f11b75a81ee6126a0dc43f21b4729"
pdf_path: "papers/Yusupov_JPhysD_2013.pdf"
extraction_quality: good
group_affiliation: true
---

<!-- id:paper:2013al-venue-reactive-molecular -->


## Evidence and attribution

!!! note "Authority of statements"

    Prose sections below (**Summary**, **Methods**, **Findings**, etc.) are **curated summaries of the publication** identified by `doi`, `title`, and `pdf_path` in the front matter above. They are **not** new primary claims by this wiki.

    For **definitive** numerical values, reaction schemes, and interpretations, use the **peer-reviewed article** (and optional records under `normalized/papers/` when present)—not this page alone.

## Summary

The study uses **ReaxFF reactive MD** (C/H/O/N **glycine/water** parameter set cited as **Rahaman et al.**) to probe **ROS** (**O, OH, HO₂, H₂O₂**) impinging on a **liquid water** film as a surrogate for the aqueous layer around **bacteria** in **cold atmospheric plasma (CAP)** applications. The abstract reports **OH, HO₂, and H₂O₂** can penetrate deeply into the liquid, while **O, OH, and HO₂** undergo **H-abstraction** from water; **H₂O₂** does **not** show H-abstraction in the stated simulations. The motivation is to clarify whether plasma species reach biomolecules directly or react en route through the biofilm water.

## Methods

- **ReaxFF MD** with explicit **ROS** insertion/impact into water films; comparison framed against reaction–diffusion modeling limitations.

The article further notes that it is known that most bio-organisms, including bacteria, are coated by a liquid ﬁlm surrounding them, and there might be many interactions between plasma species and the liquid layer before the plasma species reach the surface of the bio-organisms. Therefore, it is essential to study the behaviour of the reactive species in a liquid ﬁlm, in order to determine whether these species can travel through this layer and reach the biomolecules, or whether new species are formed along the way. In this work, we investigate the interaction of reactive oxygen species (i.e.

## Findings

- Depth penetration of selected species and qualitative reaction channels (H-abstraction) differentiated by species.


From the abstract: our computational investigations show that OH, HO 2 and H2O2 can travel deep into the liquid layer and are hence in principle able to reach the bio-organism. O, OH, HO 2 and H2O2) with water, which is assumed as a simple model system for the liquid layer surrounding biomolecules. Furthermore, O, OH and HO 2 radicals react with water molecules through hydrogen-abstraction reactions, whereas no H-abstraction reaction takes place in the case of H 2O2. This study is important to gain insight into the fundamental operating mechanisms in plasma medicine, in general, and the interaction mechanisms of plasma species with a liquid ﬁlm, in particular. (Some ﬁgures may appear in colour only in the online journal).

## Limitations

- Force-field coverage explicitly notes **O₃ and RNS** are **not** included due to **accuracy limits** for those reactions with water at the time of writing.

## Relevance to group

Connects **ReaxFF** to **plasma–liquid–biomolecule** transport chemistry—a distinct application area from solid-state materials, but methodologically aligned.

## Citations and evidence anchors

- Abstract and Secs. 1–2: motivation, species list, force-field citation, simulation rationale (J. Phys. D: Appl. Phys. 47 (2014) 025205; PDF pp. 1–2 per extract).

## Related topics

- [[reaxff-family]]