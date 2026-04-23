---
id: concept:theme-oxides-silica-ceramics
type: concept
title: "Theme: oxides, silica, and ceramic surfaces (ReaxFF corpus)"
updated: "2026-04-23"
confidence: med
canonical_tags:
  - domain:oxides-ceramics
  - method:reaxff
  - task:review
candidate_tags: []
source_refs:
  - paper_id: "paper:2013muri-venue-jp3086649"
    note: "O₂ + hydroxylated silica; ReaxFF SiO extension"
  - paper_id: "paper:2014zou-acta-materia-molecular-dynamics"
    note: "Ni oxidation and O diffusion in metal"
  - paper_id: "paper:2015lloyd-surface-scie-development-reaxff"
    note: "Surface science oriented ReaxFF development"
  - paper_id: "paper:2013verners-venue-paper"
    note: "Al₂O₃ nanoslab / oxide surfaces"
  - paper_id: "paper:2015verners-computationa-al2o3-nanoslab"
    note: "Alumina nanoslab extension and surface behavior"
  - paper_id: "paper:2018aral-physical-che-oxyhydroxide-metallic"
    note: "Oxyhydroxide / metallic interfaces"
  - paper_id: "paper:2019hahn-j-phys-chem-surface-reactivity"
    note: "Silicate glass surface reactivity"
  - paper_id: "paper:2014sen-nat-oxidation-assisted-ductility"
    note: "Oxidation-assisted ductility"
  - paper_id: "paper:2013newsome-venue-jp307680t"
    note: "Oxide-related ReaxFF application"
  - paper_id: "paper:2018ho-venue-paper"
    note: "Additional silicate and oxide surface context in this corpus"
  - paper_id: "paper:2018shin-physical-che-development-reaxff"
    note: "Battery-relevant oxide chemistry and ReaxFF development"
  - paper_id: "paper:2015broqvist-venue-jp5b01597"
    note: "Catalyst support and surface reaction overlap"
  - paper_id: "paper:2013neyts-venue-c3nr00153a"
    note: "Catalysis-adjacent oxide/surface reaction overlap"
supported_by:
  - "paper:2013muri-venue-jp3086649"
  - "paper:2014zou-acta-materia-molecular-dynamics"
  - "paper:2015lloyd-surface-scie-development-reaxff"
  - "paper:2013verners-venue-paper"
  - "paper:2015verners-computationa-al2o3-nanoslab"
  - "paper:2018aral-physical-che-oxyhydroxide-metallic"
  - "paper:2019hahn-j-phys-chem-surface-reactivity"
  - "paper:2014sen-nat-oxidation-assisted-ductility"
---

<!-- id:concept:theme-oxides-silica-ceramics -->

!!! abstract "TL;DR"

    This theme page organizes the oxides, silica, and ceramic-surface portion of the ReaxFF corpus where bond-breaking surface chemistry is central. Across the linked paper notes, the dominant threads are oxygen interactions with silica, oxidation pathways in Ni-O systems, alumina surface models, and surface-science-motivated parameter development that connects to batteries, catalysis, and water-facing silica interfaces.

## Scope (in / out)

This hub includes corpus notes that use reactive simulation lineages (primarily ReaxFF) to study oxide and ceramic chemistry where bond formation and bond breaking at surfaces or near-surface regions are part of the central claim. The covered systems are concentrated in Si/O/H, Ni/O, and Al/O chemistries, with emphasis on oxidation, hydroxylation, and thin-oxide interfacial behavior.

This hub does not attempt to be a complete oxide simulation survey, and it does not elevate non-reactive force-field studies unless those papers are explicitly used as parameter or comparison anchors in linked notes.

## How this theme is organized in the corpus

The literature is organized by mechanism-facing system families rather than by year: silica oxygen chemistry, metal oxidation (especially Ni-O), and alumina or related ceramic surfaces. A short overlap section then maps where these papers connect to batteries, catalysis, and water-silica themes so retrieval can route users toward adjacent hubs when their query intent broadens.

## Literature review (this knowledge base)

This is a corpus-bounded literature review. It synthesizes what the linked vanDuinWiki paper pages report, rather than making a claim of complete external literature coverage.

### Silica, oxygen, and gas–surface Si/O chemistry

The silica-centered line is anchored by [[2013muri-venue-jp3086649]], which is described in this KB as a QM-informed extension path for oxygen interaction with hydroxylated silica and related Si/O parameterization behavior. The same cluster is reinforced by surface-science-oriented development context in [[2015lloyd-surface-scie-development-reaxff]] and by silicate-surface reactivity notes such as [[2019hahn-j-phys-chem-surface-reactivity]] and [[2018ho-venue-paper]]. Together, these pages frame silica chemistry as a recurring testbed for how oxide-surface reactivity is represented in reactive force-field workflows.

### Metals, Ni–O, oxidation initiation, and internal oxidation

The Ni-O oxidation line is centered on [[2014zou-acta-materia-molecular-dynamics]], which the corpus uses as a key note for oxygen diffusion, oxidation initiation, and validation-heavy reactive modeling of metal oxidation behavior. The same mechanistic direction is extended by [[2014sen-nat-oxidation-assisted-ductility]], where oxidation is linked to mechanical response, and by [[2018aral-physical-che-oxyhydroxide-metallic]], which broadens the interface setting toward oxyhydroxide and metallic coupling. These linked notes collectively indicate that oxidation mechanism claims in this corpus are most robust when interpreted within each paper’s system setup and validation scope.

### Alumina and ceramic surface model development

Alumina and ceramic-surface parameter context appears in [[2013verners-venue-paper]] and [[2015verners-computationa-al2o3-nanoslab]], where the corpus records nanoslab and oxide-surface modeling lines relevant to Al/O chemistry. In this hub, these papers function as bridge references between silica-heavy and metal-oxidation-heavy threads, because they preserve the surface-reaction emphasis while changing composition and structural motifs.

### Overlap with batteries, water, and catalysis

This oxide-ceramic theme connects directly to battery-interface questions through [[batteries-interfaces-reaxff]] and linked development notes such as [[2018shin-physical-che-development-reaxff]] when oxide reactivity is discussed in electrochemical settings. It also overlaps with aqueous-interface interpretation in [[theme-water-silica-geo]], especially where silica hydroxylation and oxygen chemistry are shared motifs. Catalysis-facing retrieval should route to [[theme-catalysis-surfaces]] and its linked papers, including [[2015broqvist-venue-jp5b01597]] and [[2013neyts-venue-c3nr00153a]], when support effects and surface reaction networks become the primary user intent.

## Analysis and cross-cutting patterns

A recurring cross-cutting pattern is that oxidation and hydroxylation narratives reuse closely related parameter families within Si/O/H or Ni/O chemistry, while each paper’s confidence remains tied to its own training or validation envelope. For that reason, this KB treats quantitative barrier or diffusivity comparisons as local unless a page explicitly reports cross-model calibration under matched conditions. A second pattern is that surface composition, hydroxyl coverage, and interfacial geometry often act as first-order interpretation levers, which is why this domain hub should be read together with [[theme-reactive-md-corpus]] for method-level caveats.

## Debates, tensions, and limitations

The most persistent tension in this corpus is transferability: a single reactive parameter set may perform well for one oxide environment while remaining underconstrained for phase changes, defect populations, or chemistry shifts that were not represented in its training path. Related debate pages such as [[transferability-reactive-ff]], [[reaxff-vs-mlip-accuracy]], and [[reaxff-family]] capture this issue at method scope, while paper-level notes provide system-specific evidence.

Another limitation is that many claims in this hub are routed through page summaries rather than uniformly complete protocol detail across every linked paper. As those paper pages mature under the Methods/Findings blueprint, this theme can support sharper cross-paper comparisons without overextending beyond source-grounded statements.

## Gaps and open directions (corpus view)

Many `domain:oxides-ceramics` papers listed in [[paper-index-by-domain]] are still only lightly integrated into this narrative, so current synthesis depth is uneven across subdomains. The near-term corpus direction is to expand evidence-grounded coverage of underlinked oxide slugs, especially where they can clarify when mechanistic conclusions transfer and when they remain system-specific.

Non-ReaxFF oxide studies are present elsewhere in the KB but are only included here when they are explicitly connected to the reactive modeling line. This boundary should be preserved so this page remains a clear retrieval hub for reactive oxide and ceramic surface questions rather than becoming a generic oxide compendium.

## Representative entry points (short list)

Readers who want a silica-first pathway should start with [[2013muri-venue-jp3086649]] and then compare against [[2019hahn-j-phys-chem-surface-reactivity]]. Readers focused on metal oxidation should start with [[2014zou-acta-materia-molecular-dynamics]] and then read [[2014sen-nat-oxidation-assisted-ductility]] for mechanics-linked interpretation. For alumina and ceramic-surface model context, [[2013verners-venue-paper]] and [[2015verners-computationa-al2o3-nanoslab]] provide the most direct entry points in this cluster.

## Methods and limitations

ReaxFF parameter sets in this theme are element-range and training-distribution specific, so quantitative comparisons of barriers, defect energetics, and diffusion metrics should be validated against DFT or experiment when those references are available in the linked paper notes. Surface reconstructions, hydroxyl coverage, and finite-cell choices are recurrent sensitivity factors in oxide chemistry, so interpretation should remain coupled to each publication’s explicit model setup rather than assumed to transfer unchanged.

??? info "MAS / retrieval"

    **id:** `concept:theme-oxides-silica-ceramics`. Prefer `domain:oxides-ceramics` for hub-level routing, and pair with method/task tags when a new paper changes interpretation scope (for example, oxidation mechanism, interface chemistry, or validation regime). Refresh `source_refs` and `supported_by` whenever new linked paper pages add substantive evidence to this narrative.
