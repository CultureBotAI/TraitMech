---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T09:05:44.567164'
end_time: '2026-08-04T09:34:25.989824'
duration_seconds: 1721.42
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mycelial growth
  trait_identifier: traitmech:000074
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: mycelial_growth
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A morphology trait in which a bacterium grows as branching, filamentous
    hyphae that form a mycelium, often with subsequent differentiation into aerial
    hyphae and spores, as in Streptomyces.
  parent_traits: METPO:1000059
  synonyms: mycelium-forming, hyphal growth
  evidence_summary: "DOI:10.1038/nrmicro1968:  (Fl\xE4rdh & Buttner describe Streptomyces\
    \ growth as a branching hyphal mycelium with subsequent morphological differentiation.)\
    \ | DOI:10.1038/nrmicro3178:  (Claessen et al. treat filamentous/mycelial growth\
    \ as a bacterial solution to multicellularity.)"
  causal_graph_summary: 'mycelial_branching_hyphal_growth: 13 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mycelial growth
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000074
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which a bacterium grows as branching, filamentous hyphae that form a mycelium, often with subsequent differentiation into aerial hyphae and spores, as in Streptomyces.
- **Parent traits:** METPO:1000059
- **Synonyms:** mycelium-forming, hyphal growth
- **Existing evidence:** DOI:10.1038/nrmicro1968:  (Flärdh & Buttner describe Streptomyces growth as a branching hyphal mycelium with subsequent morphological differentiation.) | DOI:10.1038/nrmicro3178:  (Claessen et al. treat filamentous/mycelial growth as a bacterial solution to multicellularity.)
- **Existing causal graph summary:** mycelial_branching_hyphal_growth: 13 nodes, 9 edges

## Research Objective

Research the microbial trait **mycelial growth** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/mycelial_growth.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mycelial growth
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000074
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which a bacterium grows as branching, filamentous hyphae that form a mycelium, often with subsequent differentiation into aerial hyphae and spores, as in Streptomyces.
- **Parent traits:** METPO:1000059
- **Synonyms:** mycelium-forming, hyphal growth
- **Existing evidence:** DOI:10.1038/nrmicro1968:  (Flärdh & Buttner describe Streptomyces growth as a branching hyphal mycelium with subsequent morphological differentiation.) | DOI:10.1038/nrmicro3178:  (Claessen et al. treat filamentous/mycelial growth as a bacterial solution to multicellularity.)
- **Existing causal graph summary:** mycelial_branching_hyphal_growth: 13 nodes, 9 edges

## Research Objective

Research the microbial trait **mycelial growth** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/mycelial_growth.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


# Curation report: bacterial mycelial growth

## Executive summary

**Target:** `traitmech:000074` (quote verbatim)  
**Label:** mycelial growth  
**Category:** MORPHOLOGY  
**Parent:** `METPO:1000059`  
**Recommended graph scope:** the capacity of a bacterium—principally a filamentous actinomycete such as *Streptomyces*—to produce a **branched vegetative mycelium by polarized hyphal-tip extension and establishment of new lateral growth zones**. Vegetative hyphae are branched, hydrophilic, and generally multinucleoid; aerial hyphae are reproductive, comparatively unbranched and hydrophobic, and later septate into spores. Thus, aerial-hypha formation and sporulation are downstream developmental phenotypes, not necessary components of the core trait. (schlimpert2023thebestof pages 8-10, bhowmick2023osmoticstressresponses pages 1-2)

The most defensible core mechanism is:

> DivIVA-containing apical polarisome → spatial recruitment of cell-wall synthesis/remodeling machinery → polarized peptidoglycan insertion → hyphal-tip extension; budding or establishment of additional polarity centers → lateral branch formation → branched vegetative mycelium.

Recent work adds CglA-dependent cell-wall glycopolymer attachment as a determinant of normal hyphal width and branching morphology. By contrast, SepIVA localizes with DivIVA but is dispensable under the tested conditions and should not be represented as required for mycelial growth. c-di-GMP primarily controls whether *Streptomyces* remains in vegetative mycelial growth or enters aerial development; it is better modeled as a developmental-state regulator than as a direct generator of branches. (sen2024adispensablesepiva pages 1-2, gallagher2024howcdigmpcontrols pages 1-3, bhowmick2024cellshapeand pages 1-2)

## 1. Trait scope and boundaries

### Included phenotype

The trait comprises:

1. germ-tube or hyphal establishment;
2. persistent cell-wall growth at hyphal apices;
3. lateral establishment of new growth zones;
4. repeated extension and branching to form a connected vegetative filament network.

A 2024 account states that vegetative *Streptomyces* hyphae “extend by polar cell wall growth and create new growth zones by lateral branching,” while clusters of DivIVA at tips form polarisomes involved in both apical growth and de novo branch establishment. (sen2024adispensablesepiva pages 1-2)

### Excluded or separately modeled boundary cases

| Nearby phenotype | Relationship to `traitmech:000074` | Curation decision |
|---|---|---|
| Aerial-mycelium formation | Reproductive transition from vegetative growth; aerial hyphae differ in surface properties and branching pattern | Model as a downstream/alternative developmental state, not as part of the defining trait |
| Sporulation and spore-chain formation | Septation and differentiation of aerial hyphae | Exclude from the core graph; connect through developmental-transition edges if useful |
| Exploratory growth | Rapid surface expansion can involve long, relatively nonbranching vegetative hyphae after glucose depletion | Separate phenotype; it does not necessarily satisfy the branched-mycelium definition (schlimpert2023thebestof pages 8-10) |
| Linear chains of divided cells | Filamentous appearance without apical hyphal growth and lateral branching | Exclude |
| Wall-less S-cells | Vesicles extruded from tips under hyperosmotic or cell-wall stress | Stress-induced alternative morphology, not mycelial growth (schlimpert2023thebestof pages 8-10) |
| Pellets, clumps, dispersed mycelia | Macroscopic submerged-culture architectures formed by aggregation and branching | Treat as assay/bioprocess phenotypes downstream of mycelial growth, not synonyms |
| Fungal mycelium | Morphologically analogous but taxonomically and mechanistically distinct | Exclude from this bacterial trait graph |
| Filamentous cyanobacteria | Usually chains of communicating cells produced by division rather than *Streptomyces*-type polar hyphal extension | Exclude unless the trait definition is deliberately broadened |

## 2. Candidate nodes

### Trait and taxa

- `traitmech:000074` — mycelial growth.
- `METPO:1000059` — supplied parent trait.
- *Streptomyces* spp.; key experimental systems: *S. coelicolor* and *S. venezuelae*.
- *Streptomyces variegatus* — taxon used in the ROS/pyrogallol branching work.
- *Lentzea aerocolonigenes* — application-relevant filamentous actinomycete.

Taxon CURIEs should be added only after checking the current NCBI Taxonomy records for the precise strain; strain-level identifiers are not inferred here.

### Proteins and complexes

- **DivIVA** — essential polarity determinant; central polarisome scaffold.
- **Scy** — coiled-coil polarisome-associated scaffold affecting polarisome organization/branching.
- **FilP** — intermediate-filament-like protein providing mechanical organization to growing hyphae.
- **AfsK** — Ser/Thr protein kinase that phosphorylates DivIVA during cell-wall stress.
- **Polarisome** — DivIVA-centered apical multiprotein complex; label-only candidate pending ontology review.
- **CglA / Vnz_13690** — LCP–LytR_C cell-wall glycopolymer ligase in *S. venezuelae*.
- **SepIVA** — DivIVA-interacting, tip-localized protein; association node, not a required causal component.
- **DisA** — diadenylate cyclase producing c-di-AMP from ATP.
- **AtaC** — c-di-AMP phosphodiesterase.
- **BldD** — c-di-GMP-dependent master repressor of developmental entry.
- **WhiG and RsiG** — sigma/anti-sigma pair controlling later sporulation differentiation.
- **Peptidoglycan synthases, hydrolases and PBPs** — classes of cell-wall enzymes recruited to growth zones.
- **FtsZ** — informative for septation and CglA phenotypes, but not a core driver of vegetative tip extension.

Gene/protein CURIEs should be assigned from the reviewed UniProt entry for each species and strain. A gene symbol alone must not be treated as species-independent grounding.

### Chemicals and environmental factors

- Peptidoglycan; `GO:0009252` — peptidoglycan biosynthetic process.
- `GO:0009274` — peptidoglycan-based cell wall.
- ATP; `CHEBI:15422`.
- Hydrogen peroxide; `CHEBI:16240`.
- c-di-GMP and c-di-AMP — retain as labels until the exact ChEBI records are verified.
- Pyrogallol — label-only pending ChEBI verification.
- Bacitracin and vancomycin — cell-wall synthesis inhibitors that activate the AfsK/DivIVA stress response.
- High salt/hyperosmotic stress, nutrient depletion, glucose depletion and cell-wall stress — environmental/experimental nodes.
- Glass microparticles and soy lecithin — bioprocess interventions, not native causal components.

### Processes and cellular locations

- Polar/apical cell-wall growth.
- Hyphal-tip extension.
- Lateral branch initiation.
- Polarisome splitting/budding.
- Cell-wall glycopolymer attachment.
- Vegetative mycelium formation.
- Aerial-hypha formation and sporulation—downstream developmental processes.
- Hyphal tip, lateral branch site, cytoplasmic membrane and cell wall—location nodes; ontology IDs should be verified before ingestion.

## 3. Candidate causal edges

The predicates below are deliberately simple and YAML-friendly. “Core” denotes recommended inclusion; “context” denotes useful but non-defining regulation; “hold” denotes evidence insufficient for a positive causal assertion.

| # | Proposed subject–predicate–object | Evidence snippet | Reference | Strength and curation notes |
|---:|---|---|---|---|
| 1 | **DivIVA — enables → polar hyphal growth** | “the filamentous and mycelial mode of growth of streptomycetes depends on clusters of DivIVA at hyphal tips” | DOI: [10.1186/s12866-024-03625-6](https://doi.org/10.1186/s12866-024-03625-6), November 2024 | **Core; high confidence.** Supported by current synthesis and earlier genetic work; taxon scope is streptomycetes. (sen2024adispensablesepiva pages 1-2) |
| 2 | **DivIVA-containing polarisome — localizes/directs → apical cell-wall synthesis** | “Apical growth is directed by…DivIVA…[forming] the polarisome, which is needed for proper localization of peptidoglycan synthases, hydrolases, and other proteins involved in cell wall assembly” | DOI: [10.1128/mbio.01492-24](https://doi.org/10.1128/mbio.01492-24), published 9 September 2024 | **Core; high confidence.** This is the central spatial-mechanism edge. (bhowmick2024cellshapeand pages 1-2) |
| 3 | **apical peptidoglycan synthesis/remodeling — produces → hyphal-tip extension** | *Streptomyces* “gain biomass by apical extension of their filaments”; polarisome localizes PG synthases and hydrolases | DOI: 10.1128/mbio.01492-24 | **Core; high confidence**, although individual synthases are not resolved by this source. (bhowmick2024cellshapeand pages 1-2) |
| 4 | **lateral DivIVA/polarisome focus formation — initiates → hyphal branch** | Lateral branches “emerge from small foci of DivIVA,” most formed by “budding off as daughter polarisomes from the apical polarisome” | DOI: 10.1186/s12866-024-03625-6 | **Core; high confidence for spatial precedence.** The 2024 paper cites prior live-cell studies and directly observes analogous SepIVA focus dynamics. (sen2024adispensablesepiva pages 8-10) |
| 5 | **tip extension plus repeated branching — produces → vegetative mycelium** | Vegetative mycelium is described as long multicellular filaments used for nutrient scavenging; cells “grow by tip extension and through initiation of new branches” | DOI: [10.1093/femsml/uqad020](https://doi.org/10.1093/femsml/uqad020), April 2023 | **Core; high confidence; definition-level edge.** (bhowmick2023osmoticstressresponses pages 1-2) |
| 6 | **Scy — contributes to → polarisome organization/branching** | DivIVA works with “Scy and FilP…to form the polarisome”; Scy colocalizes with DivIVA and acts as a scaffold | DOI: 10.1093/femsml/uqad020 | **Core but qualified.** Use “contributes_to,” not “required_for,” unless the primary mutant paper is attached. (bhowmick2023osmoticstressresponses pages 1-2, kato2023redoxactivecompoundgenerated pages 15-20) |
| 7 | **FilP — contributes to → hyphal mechanical organization/polar growth** | FilP is part of the polarisome-associated system and “provides mechanical support” | DOI: 10.1093/femsml/uqad020; ROS paper DOI below | **Core but qualified.** Directness is weaker than for DivIVA; avoid making FilP a cell-wall enzyme. (bhowmick2023osmoticstressresponses pages 1-2, kato2023redoxactivecompoundgenerated pages 15-20) |
| 8 | **AfsK — phosphorylates → DivIVA** | “AfsK…colocalizes with DivIVA and phosphorylates it in response to cell wall stress signals” | DOI: 10.1093/femsml/uqad020 | **Core regulatory edge; high confidence.** Foundational primary DOI: [10.1073/pnas.1207409109](https://doi.org/10.1073/pnas.1207409109). (bhowmick2023osmoticstressresponses pages 1-2) |
| 9 | **increased DivIVA phosphorylation — increases → polarisome disassembly/new-polarisome formation** | Constitutive AfsK activity causes high DivIVA phosphorylation, “polarisome disassembly and increased new polarisome formation” | DOI: 10.1093/femsml/uqad020 | **Core regulatory edge; taxon/perturbation specific.** (bhowmick2023osmoticstressresponses pages 1-2) |
| 10 | **increased new-polarisome formation — increases → hyphal branching** | The same condition produces a “hyperbranching phenotype” | DOI: 10.1093/femsml/uqad020 | **Core regulatory consequence; high confidence in the manipulated strain.** Do not infer that all AfsK activation always increases net mycelial growth. (bhowmick2023osmoticstressresponses pages 1-2) |
| 11 | **CglA — catalyzes/contributes to → cell-wall glycopolymer attachment** | CglA was identified as the “key enzyme needed for the attachment of glycopolymers to the cell wall” | DOI: 10.1128/mbio.01492-24 | **Core supporting module; high confidence in *S. venezuelae*.** (bhowmick2024cellshapeand pages 1-2) |
| 12 | **CglA function — maintains → normal vegetative hyphal width and branching morphology** | Deletion caused “striking enlargement,” “anomalous branching,” and swollen tips; mutant width was **2.14 ± 0.420 µm** versus **0.98 ± 0.099 µm** in wild type | DOI: 10.1128/mbio.01492-24 | **Core; high confidence and quantitative.** Complementation restored macrocolony development. (bhowmick2024cellshapeand pages 10-12, bhowmick2024cellshapeand pages 5-8) |
| 13 | **CglA — localizes to → hyphal tips and branch points** | YPet-CglA localized “at hyphal tips and branching points of growing hyphae” | DOI: 10.1128/mbio.01492-24 | **Association/location edge; high confidence.** Do not claim direct membership in the polarisome: two-hybrid tests found no interaction with DivIVA, Scy or FilP. (bhowmick2024cellshapeand pages 10-12) |
| 14 | **cglA deletion — disrupts → FtsZ-ring positioning/septum placement** | The approximately twofold-wider mutant failed to form regular FtsZ ladders and had misplaced septa | DOI: 10.1128/mbio.01492-24 | **High confidence but downstream of core vegetative morphology.** Better placed in a linked sporulation graph. Sporulation efficiency was **13%** of wild type; complementation restored **46.6%**. (bhowmick2024cellshapeand pages 5-8) |
| 15 | **SepIVA — interacts/colocalizes with → DivIVA at growing tips** | mNG-SepIVA accumulated at vegetative tips, colocalized with DivIVA-mCherry, and interacted with DivIVA in bacterial two-hybrid assays | DOI: 10.1186/s12866-024-03625-6 | **Association only.** Useful interaction/location edges, not proof that SepIVA drives growth. (sen2024adispensablesepiva pages 1-2, sen2024adispensablesepiva pages 8-10) |
| 16 | **SepIVA — required for → mycelial growth** | Deletion was “dispensable for growth, cell division and sporulation,” with no detectable phenotype | DOI: 10.1186/s12866-024-03625-6 | **Do not curate as a positive edge.** If negative evidence is supported, record `not_required_under_condition` for MYM, chitin agar and MOPS-glucose conditions. (sen2024adispensablesepiva pages 1-2, sen2024adispensablesepiva pages 8-10) |
| 17 | **high c-di-GMP — stabilizes → vegetative developmental state** | DGC overexpression blocked development; high c-di-GMP “trapp[ed] Streptomyces in vegetative growth,” whereas PDE overexpression caused precocious hypersporulation | DOI: [10.1016/j.mib.2024.102516](https://doi.org/10.1016/j.mib.2024.102516), August 2024 | **Context edge; high confidence.** This maintains the vegetative state but does not directly prove enhanced branching or biomass. (gallagher2024howcdigmpcontrols pages 1-3) |
| 18 | **c-di-GMP binding — activates/stabilizes → BldD DNA-repressor function** | BldD DNA binding “requires complex formation with c-di-GMP,” which acts as a developmental “brake” | DOI: 10.1016/j.mib.2024.102516 | **Context edge; high confidence.** Connects vegetative growth to repression of aerial/sporulation genes. (gallagher2024howcdigmpcontrols pages 1-3) |
| 19 | **DisA — synthesizes → c-di-AMP** | DisA “produces c-di-AMP out of…ATP,” whereas AtaC degrades it | DOI: 10.1128/mbio.01492-24 | **Supporting metabolic edge; high confidence.** (bhowmick2024cellshapeand pages 1-2) |
| 20 | **c-di-AMP availability — enables → growth under high salt** | A disA deletion/inactivation strain had a growth defect on nutrient agar with high salt | DOI: 10.1128/mbio.01492-24 | **Context edge; condition-specific.** It supports osmotic fitness, not specifically branch initiation. (bhowmick2024cellshapeand pages 1-2) |
| 21 | **low c-di-AMP — increases → c-di-AMP-riboswitch-controlled hydrolase expression** | At low c-di-AMP, the *rpfA* riboswitch is on, increasing RpfA; authors suggest the same for five other hydrolases | DOI: 10.1128/mbio.01492-24 | **Partly supported.** Curate *rpfA* specifically; treat extension to all six hydrolases as uncertain. (bhowmick2024cellshapeand pages 10-12) |
| 22 | **pyrogallol-generated H₂O₂/ROS — increases → hyphal branching** | Catalase diminished pyrogallol activity, while direct H₂O₂ treatment produced similar branching | DOI: [10.1101/2023.01.12.523877](https://doi.org/10.1101/2023.01.12.523877), January 2023 | **Hold/uncertain:** mechanistically suggestive but a non-peer-reviewed preprint, species- and dose-specific. The strongest decomposition is pyrogallol → H₂O₂/ROS → increased branching. (kato2023redoxactivecompoundgenerated pages 1-7) |
| 23 | ***B. subtilis* 2,3-dihydroxybenzoate plus *M. septicum* NahG activity — produces → pyrogallol** | Knockout/co-culture and heterologous-expression results implicated a bacillibactin intermediate and a NahG homolog | DOI: 10.1101/2023.01.12.523877 | **Hold.** Interesting interspecies environmental module, but retain outside the core graph until peer-reviewed confirmation. (kato2023redoxactivecompoundgenerated pages 1-7) |

## 4. Current research and applications

### Cell-envelope mechanisms

The strongest 2024 advance is recognition that mycelial morphology depends not only on peptidoglycan deposition but also on cell-wall glycopolymer attachment. CglA loss nearly doubled abnormal hyphal width, altered branching and swollen-tip morphology, disturbed septation, and reduced viable-spore output. The study explicitly notes that the detailed coupling between LCP proteins, glycopolymers and morphogenesis remains unresolved, and its proposed c-di-AMP–hydrolase–wall-stability model is still a hypothesis. (bhowmick2024cellshapeand pages 10-12, bhowmick2024cellshapeand pages 5-8)

The SepIVA study provides an important expert corrective: tip localization and protein interaction are not equivalent to causal necessity. Despite SepIVA–DivIVA interaction and apical colocalization, a clean deletion caused no detectable growth, division or sporulation defect under several media conditions. This argues for conservative graph predicates and explicit negative evidence. (sen2024adispensablesepiva pages 1-2, sen2024adispensablesepiva pages 8-10)

### Developmental signaling

The 2024 c-di-GMP synthesis places BldD and WhiG as direct c-di-GMP effectors controlling two distinct transitions: vegetative-to-aerial development and aerial-hypha-to-spore differentiation. In *S. venezuelae*, five of ten c-di-GMP metabolic proteins contain both GGDEF and EAL domains, emphasizing that environmental inputs into this network remain incompletely defined. c-di-GMP falls to a minimum at approximately **14 h** in liquid sporulation medium as differentiation begins, then rises during spore formation. (gallagher2024howcdigmpcontrols pages 1-3)

### Industrial morphology engineering

Filamentous morphology directly affects mixing, oxygen and nutrient transfer, viscosity, pellet viability and specialized-metabolite output. However, pellet architecture is an emergent submerged-culture phenotype rather than the same ontological trait as cellular mycelial growth.

A 2023 *Lentzea aerocolonigenes* study used glass microparticles with median diameter **7.9 µm** at **10 g·L⁻¹**, producing looser, lower-density pellets and up to a **fourfold** increase in rebeccamycin synthesis. Combining microparticles with **7.5 g·L⁻¹** soy lecithin yielded **213 mg·L⁻¹ after 10 days**, reported as the highest microparticle-supplemented shake-flask titer then available. These are application edges—microparticles alter pellet architecture and productivity—not intrinsic nodes in the bacterial trait mechanism. (dinius2023morphologyengineeringfor pages 1-2)

A 2024 bioprocess review reports that microparticle treatment of pamamycin-producing *Streptomyces albus* reduced pellet size, loosened internal structure and improved final product concentration approximately sixfold. It also emphasizes an expert consensus that no universal “optimal” morphology exists across organisms and products; effects can arise indirectly through mass transfer and directly through altered physiology or gene expression. (dinius2024intensificationofbioprocesses pages 14-16, dinius2024intensificationofbioprocesses pages 26-29)

## 5. Recommended minimal YAML graph

A conservative first implementation should contain these nine core edges:

1. `DivIVA -> enables -> polarisome assembly/localization`
2. `polarisome -> localizes -> peptidoglycan synthesis and remodeling at hyphal tip`
3. `apical peptidoglycan synthesis/remodeling -> causes -> hyphal tip extension`
4. `daughter/lateral polarisome establishment -> causes -> lateral branch initiation`
5. `hyphal tip extension -> contributes_to -> branched vegetative mycelium`
6. `lateral branch initiation -> contributes_to -> branched vegetative mycelium`
7. `AfsK -> phosphorylates -> DivIVA`
8. `elevated DivIVA phosphorylation -> increases -> new polarisome formation/hyperbranching`
9. `CglA-mediated wall glycopolymer attachment -> maintains -> normal hyphal morphology`

Scy and FilP can be added with `contributes_to` predicates. c-di-GMP/BldD and c-di-AMP/osmotic-fitness modules should be linked as contextual regulators. SepIVA should be represented only by localization/interaction or explicit negative-evidence statements. ROS/pyrogallol edges should remain provisional.

## 6. Warnings and non-curatable claims

1. **Do not equate aerial mycelium with the core trait.** Aerial development and sporulation are regulated downstream states.
2. **Do not equate pellets with mycelial growth.** Pellets are culture-scale aggregates whose size and density depend on medium, shear and inoculation.
3. **Do not curate SepIVA as required for growth.** The 2024 deletion study found the opposite under tested conditions. (sen2024adispensablesepiva pages 1-2)
4. **Do not assert that CglA is physically part of the polarisome.** Its localization is compatible with that model, but bacterial two-hybrid assays detected no interaction with DivIVA, Scy or FilP. (bhowmick2024cellshapeand pages 10-12)
5. **Do not curate the proposed c-di-AMP–hydrolase–glycopolymer mechanism as established.** The authors explicitly describe it as a hypothesis requiring future testing. (bhowmick2024cellshapeand pages 10-12)
6. **Do not make c-di-GMP a direct branching signal.** Available evidence primarily concerns developmental-state transitions.
7. **Treat pyrogallol/H₂O₂ branching as provisional.** The retrieved source is a 2023 bioRxiv preprint with taxon- and assay-specific results. (kato2023redoxactivecompoundgenerated pages 1-7)
8. **Avoid unverified ontology identifiers.** Use label-only candidates until ChEBI, GO, UniProt and NCBI Taxonomy records are checked for exact chemical forms, protein species and strains.
9. **Separate direct experiments from review synthesis.** DivIVA, Scy, FilP and AfsK edges should ideally retain both a current review and the relevant primary study in the YAML evidence block.

## DOI-first bibliography

1. Bhowmick S, Viveros RP, Latoscha A, et al. **Cell shape and division septa positioning in filamentous *Streptomyces* require a functional cell wall glycopolymer ligase CglA.** *mBio*. Published 9 September 2024;15(10). DOI: [10.1128/mbio.01492-24](https://doi.org/10.1128/mbio.01492-24). (bhowmick2024cellshapeand pages 1-2, bhowmick2024cellshapeand pages 5-8)
2. Sen BC, Mavi PS, Irazoki O, et al. **A dispensable SepIVA orthologue in *Streptomyces venezuelae* is associated with polar growth and not cell division.** *BMC Microbiology*. November 2024;24:481. DOI: [10.1186/s12866-024-03625-6](https://doi.org/10.1186/s12866-024-03625-6). (sen2024adispensablesepiva pages 1-2, sen2024adispensablesepiva pages 8-10)
3. Gallagher KA, Tschowri N, Brennan RG, Schumacher MA, Buttner MJ. **How c-di-GMP controls progression through the *Streptomyces* life cycle.** *Current Opinion in Microbiology*. August 2024;80:102516. DOI: [10.1016/j.mib.2024.102516](https://doi.org/10.1016/j.mib.2024.102516). (gallagher2024howcdigmpcontrols pages 1-3)
4. Schlimpert S, Elliot MA. **The best of both worlds—*Streptomyces coelicolor* and *Streptomyces venezuelae* as model species for studying antibiotic production and bacterial multicellular development.** *Journal of Bacteriology*. July 2023;205(7). DOI: [10.1128/jb.00153-23](https://doi.org/10.1128/jb.00153-23). (schlimpert2023thebestof pages 8-10)
5. Bhowmick S, Shenouda ML, Tschowri N. **Osmotic stress responses and the biology of the second messenger c-di-AMP in *Streptomyces*.** *microLife*. April 2023;4. DOI: [10.1093/femsml/uqad020](https://doi.org/10.1093/femsml/uqad020). (bhowmick2023osmoticstressresponses pages 1-2)
6. Dinius A, Schrinner K, Schrader M, et al. **Morphology engineering for novel antibiotics: effect of glass microparticles and soy lecithin on rebeccamycin production and cellular morphology of filamentous actinomycete *Lentzea aerocolonigenes*.** *Frontiers in Bioengineering and Biotechnology*. Published 6 April 2023;11:1171055. DOI: [10.3389/fbioe.2023.1171055](https://doi.org/10.3389/fbioe.2023.1171055). (dinius2023morphologyengineeringfor pages 1-2)
7. Dinius A, Kozanecka ZJ, Hoffmann KP, Krull R. **Intensification of bioprocesses with filamentous microorganisms.** *Physical Sciences Reviews*. February 2024;9:777–823. DOI: [10.1515/psr-2022-0112](https://doi.org/10.1515/psr-2022-0112). (dinius2024intensificationofbioprocesses pages 14-16)
8. Kato M, Asamizu S, Onaka H. **Redox-active compound generated by bacterial crosstalk induces hypha branching in *Streptomyces* species.** bioRxiv preprint, January 2023. DOI: [10.1101/2023.01.12.523877](https://doi.org/10.1101/2023.01.12.523877). **Not peer reviewed in the retrieved record.** (kato2023redoxactivecompoundgenerated pages 1-7)
9. Hempel AM, Cantlay S, Molle V, et al. **The Ser/Thr protein kinase AfsK regulates polar growth and hyphal branching in the filamentous bacteria *Streptomyces*.** *Proceedings of the National Academy of Sciences*. 2012;109:E2371–E2379. DOI: [10.1073/pnas.1207409109](https://doi.org/10.1073/pnas.1207409109). This is the foundational primary source for AfsK–DivIVA regulation, as summarized in the 2023 review. (bhowmick2023osmoticstressresponses pages 1-2)

**Overall recommendation:** curate a compact DivIVA–polarisome–cell-wall synthesis–branch establishment core, add AfsK and CglA as supported regulatory/structural modules, and keep developmental second messengers, environmental ROS, sporulation and fermentation pellet morphology in explicitly labeled contextual subgraphs.

References

1. (schlimpert2023thebestof pages 8-10): Susan Schlimpert and Marie A. Elliot. The best of both worlds—streptomyces coelicolor and streptomyces venezuelae as model species for studying antibiotic production and bacterial multicellular development. Journal of Bacteriology, Jul 2023. URL: https://doi.org/10.1128/jb.00153-23, doi:10.1128/jb.00153-23. This article has 59 citations and is from a peer-reviewed journal.

2. (bhowmick2023osmoticstressresponses pages 1-2): Sukanya Bhowmick, Mary L. Shenouda, and Natalia Tschowri. Osmotic stress responses and the biology of the second messenger c-di-amp in streptomyces. microLife, Apr 2023. URL: https://doi.org/10.1093/femsml/uqad020, doi:10.1093/femsml/uqad020. This article has 17 citations and is from a peer-reviewed journal.

3. (sen2024adispensablesepiva pages 1-2): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 6 citations and is from a peer-reviewed journal.

4. (gallagher2024howcdigmpcontrols pages 1-3): Kelley A Gallagher, Natalia Tschowri, Richard G Brennan, Maria A Schumacher, and Mark J Buttner. How c-di-gmp controls progression through the streptomyces life cycle. Current Opinion in Microbiology, 80:102516, Aug 2024. URL: https://doi.org/10.1016/j.mib.2024.102516, doi:10.1016/j.mib.2024.102516. This article has 25 citations and is from a peer-reviewed journal.

5. (bhowmick2024cellshapeand pages 1-2): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (sen2024adispensablesepiva pages 8-10): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 6 citations and is from a peer-reviewed journal.

7. (kato2023redoxactivecompoundgenerated pages 15-20): Manami Kato, Shumpei Asamizu, and Hiroyasu Onaka. Redox-active compound generated by bacterial crosstalk induces hypha branching in streptomyces species. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.12.523877, doi:10.1101/2023.01.12.523877. This article has 0 citations.

8. (bhowmick2024cellshapeand pages 10-12): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

9. (bhowmick2024cellshapeand pages 5-8): Sukanya Bhowmick, Ruth P. Viveros, Andreas Latoscha, Fabian M. Commichau, Christoph Wrede, Mahmoud M. Al-Bassam, and Natalia Tschowri. Cell shape and division septa positioning in filamentous <i>streptomyces</i> require a functional cell wall glycopolymer ligase cgla. Oct 2024. URL: https://doi.org/10.1128/mbio.01492-24, doi:10.1128/mbio.01492-24. This article has 4 citations and is from a domain leading peer-reviewed journal.

10. (kato2023redoxactivecompoundgenerated pages 1-7): Manami Kato, Shumpei Asamizu, and Hiroyasu Onaka. Redox-active compound generated by bacterial crosstalk induces hypha branching in streptomyces species. bioRxiv, Jan 2023. URL: https://doi.org/10.1101/2023.01.12.523877, doi:10.1101/2023.01.12.523877. This article has 0 citations.

11. (dinius2023morphologyengineeringfor pages 1-2): Anna Dinius, Kathrin Schrinner, Marcel Schrader, Zuzanna Justyna Kozanecka, Henry Brauns, Leon Klose, Hannah Weiß, Arno Kwade, and Rainer Krull. Morphology engineering for novel antibiotics: effect of glass microparticles and soy lecithin on rebeccamycin production and cellular morphology of filamentous actinomycete lentzea aerocolonigenes. Frontiers in Bioengineering and Biotechnology, Apr 2023. URL: https://doi.org/10.3389/fbioe.2023.1171055, doi:10.3389/fbioe.2023.1171055. This article has 12 citations.

12. (dinius2024intensificationofbioprocesses pages 14-16): Anna Dinius, Zuzanna J. Kozanecka, Kevin P. Hoffmann, and Rainer Krull. Intensification of bioprocesses with filamentous microorganisms. Physical Sciences Reviews, 9:777-823, Feb 2024. URL: https://doi.org/10.1515/psr-2022-0112, doi:10.1515/psr-2022-0112. This article has 21 citations and is from a peer-reviewed journal.

13. (dinius2024intensificationofbioprocesses pages 26-29): Anna Dinius, Zuzanna J. Kozanecka, Kevin P. Hoffmann, and Rainer Krull. Intensification of bioprocesses with filamentous microorganisms. Physical Sciences Reviews, 9:777-823, Feb 2024. URL: https://doi.org/10.1515/psr-2022-0112, doi:10.1515/psr-2022-0112. This article has 21 citations and is from a peer-reviewed journal.