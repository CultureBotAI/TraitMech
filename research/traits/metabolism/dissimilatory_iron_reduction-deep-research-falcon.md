---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:50:37.336538'
end_time: '2026-08-04T05:57:23.811974'
duration_seconds: 406.48
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: dissimilatory iron reduction
  trait_identifier: traitmech:000031
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: dissimilatory_iron_reduction
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An anaerobic respiratory metabolism in which an organism conserves energy
    for growth by coupling the oxidation of organic matter or hydrogen to the reduction
    of Fe(III) as a terminal electron acceptor. Characteristic of Geobacter and Shewanella,
    often via extracellular electron transfer.
  parent_traits: traitmech:000039
  synonyms: ferric iron respiration, dissimilatory Fe(III) reduction
  evidence_summary: 'DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter
    coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical
    reactions in aquatic sediments, soils, and groundwater (Lovley review establishes
    dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration
    coupling organic-matter oxidation to metal reduction.) | PMID:7826009:  (Nealson
    & Saffarini, "Iron and manganese in anaerobic respiration", supports Fe(III) and
    Mn(IV) as terminal electron acceptors competitive with nitrate.)'
  causal_graph_summary: 'dir_ferric_iron_respiration: 8 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dissimilatory iron reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000031
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of Fe(III) as a terminal electron acceptor. Characteristic of Geobacter and Shewanella, often via extracellular electron transfer.
- **Parent traits:** traitmech:000039
- **Synonyms:** ferric iron respiration, dissimilatory Fe(III) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration coupling organic-matter oxidation to metal reduction.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports Fe(III) and Mn(IV) as terminal electron acceptors competitive with nitrate.)
- **Existing causal graph summary:** dir_ferric_iron_respiration: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **dissimilatory iron reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_iron_reduction.yaml`.

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
- **Trait label:** dissimilatory iron reduction
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000031
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An anaerobic respiratory metabolism in which an organism conserves energy for growth by coupling the oxidation of organic matter or hydrogen to the reduction of Fe(III) as a terminal electron acceptor. Characteristic of Geobacter and Shewanella, often via extracellular electron transfer.
- **Parent traits:** traitmech:000039
- **Synonyms:** ferric iron respiration, dissimilatory Fe(III) reduction
- **Existing evidence:** DOI:10.1128/mr.55.2.259-287.1991: The oxidation of organic matter coupled to the reduction of Fe(III) or Mn(IV) is one of the most important biogeochemical reactions in aquatic sediments, soils, and groundwater (Lovley review establishes dissimilatory Fe(III)/Mn(IV) reduction as energy-conserving anaerobic respiration coupling organic-matter oxidation to metal reduction.) | PMID:7826009:  (Nealson & Saffarini, "Iron and manganese in anaerobic respiration", supports Fe(III) and Mn(IV) as terminal electron acceptors competitive with nitrate.)
- **Existing causal graph summary:** dir_ferric_iron_respiration: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **dissimilatory iron reduction** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dissimilatory_iron_reduction.yaml`.

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


# Curation report: dissimilatory iron reduction

## Trait record and scope

- **Trait label:** dissimilatory iron reduction
- **Trait identifier:** `traitmech:000031`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `traitmech:000039`
- **Synonyms:** ferric iron respiration; dissimilatory Fe(III) reduction

### Recommended scope

This trait denotes an **energy-conserving anaerobic respiratory capacity** in which oxidation of an electron donor—commonly organic carbon or H₂—supplies electrons to Fe(III), which functions as the terminal electron acceptor and is reduced to Fe(II). For poorly soluble Fe(III) (oxyhydr)oxides, the phenotype normally requires extracellular electron transfer (EET). The canonical *Shewanella oneidensis* pathway transfers electrons from central metabolism through CymA, periplasmic cytochromes, and an outer-membrane porin–cytochrome conduit to extracellular acceptors. (beblawy2018extracellularreductionof pages 6-9)

The class should require evidence that Fe(III) reduction is linked to respiration, energy conservation, growth, or physiologically meaningful anaerobic survival. A colorimetric increase in Fe(II) alone is insufficient because Fe(III) can also be reduced abiotically by sulfide, reduced metabolites, or biogenic Fe(II).

### Boundary cases

**Include:**

1. Respiration of soluble Fe(III) complexes such as Fe(III)-citrate.
2. Reduction of insoluble ferrihydrite and other Fe(III) oxides through direct-contact EET, conductive appendages, or diffusible electron shuttles.
3. Taxon-specific respiratory architectures in bacteria and archaea, provided that Fe(III) is the acceptor supporting energy conservation.

**Exclude or represent separately:**

- **Assimilatory iron reduction/uptake:** Fe is reduced for acquisition and incorporated into biomass rather than serving as the respiratory acceptor.
- **Fe(II) oxidation:** reverse redox direction and a different metabolism.
- **Generic EET to an electrode:** anode reduction demonstrates exoelectrogenicity but not necessarily Fe(III) respiration. Substrate-specific differences are experimentally documented; for example, some *Geobacter* deletions impair ferrihydrite reduction while minimally affecting anode reduction. (jiang2023thevariedroles pages 1-2)
- **Direct interspecies electron transfer:** mechanistically related but not itself dissimilatory Fe(III) reduction.
- **Fermentative survival aided by EET without demonstrated respiratory growth:** useful supporting evidence, not sufficient alone for the trait.
- **Indirect or abiotic Fe(III) reduction:** do not assign the microbial trait unless the biological electron-transfer step and energetic coupling are established.
- **Iron assimilation genes or community enrichment alone:** these are contextual correlates, not proof of the phenotype. A 2024 sediment study found that community changes did not necessarily track functional-gene abundance. (shi2024responseoffe(iii)reducing pages 10-11, shi2024responseoffe(iii)reducing pages 1-2)

## Candidate causal-graph nodes

Ontology mappings below are deliberately conservative. Protein names should be grounded to **taxon-specific UniProt accessions during implementation**, because a generic gene symbol is not an adequate universal protein identifier.

### Trait, process, and function nodes

| Candidate node | Type | Suggested grounding | Curation note |
|---|---|---|---|
| dissimilatory iron reduction | trait/process | `traitmech:000031` | Target node; retain identifier verbatim. |
| anaerobic respiration | biological process | GO term candidate; verify exact current GO record | Parent physiological process. |
| extracellular electron transfer | biological process | GO term candidate or label-only | Broader mechanism; not synonymous with the target trait. |
| electron transfer activity | molecular function | GO candidate | Prefer more specific cytochrome/electron-carrier functions where available. |
| energy conservation / growth | phenotype/process | label-only pending model choice | Essential scope criterion. |
| Fe(III) reduction rate | assay phenotype | label-only | Context-dependent quantitative output. |
| Fe(II) production | assay output | label-only plus Fe(II) chemical node | Useful proximal readout, but not alone diagnostic of respiratory growth. |

### Chemicals and environmental factors

| Candidate node | Type | Suggested grounding | Role |
|---|---|---|---|
| Fe(III), ferric ion | electron acceptor | ChEBI; verify exact ferric-ion CURIE | Terminal electron acceptor. |
| Fe(II), ferrous ion | product | ChEBI; verify exact ferrous-ion CURIE | Reduction product. |
| ferrihydrite | mineral/electron acceptor | ChEBI or mineral ontology candidate; otherwise label-only | Insoluble Fe(III) (oxyhydr)oxide used in many assays. |
| Fe(III)-citrate | soluble acceptor complex | ChEBI candidate; verify | Highly bioavailable experimental acceptor. |
| Fe(III)-EDTA | soluble acceptor complex | ChEBI candidate; verify | Artificial chelated acceptor; environmental interpretation requires caution. |
| acetate | electron donor/carbon source | ChEBI; verify exact CURIE | Canonical *Geobacter* donor. |
| lactate | electron donor/carbon source | ChEBI; verify stereochemistry | Canonical *Shewanella* donor in many assays. |
| hydrogen | electron donor | ChEBI candidate | Included in trait definition but mechanism is taxon-dependent. |
| flavins/riboflavin | electron shuttle/cofactor | ChEBI candidates | Particularly relevant to *Shewanella* mediated EET. |
| anoxic condition | environmental factor | ENVO candidate | Required environmental context for canonical respiration. |
| lake sediment, aquatic sediment, soil, groundwater | environment | ENVO terms after lookup | Natural habitats; use specific ENVO CURIEs only after verification. |
| Fe(III) solubility/bioavailability | physicochemical factor | label-only | Strongly controls apparent rates. |

### *Shewanella* pathway components

| Node | Type/localization | Mechanistic role |
|---|---|---|
| CymA | inner-membrane tetraheme c-type cytochrome | Receives electrons from the quinol pool/central metabolism and distributes them into anaerobic respiratory pathways. |
| STC/CctA | soluble periplasmic tetraheme cytochrome | Major periplasmic redox shuttle/hub. |
| FccA | periplasmic flavocytochrome c/fumarate reductase | Redundant or alternative carrier between CymA and outer-membrane systems. |
| MtrA | periplasm-facing decaheme c-type cytochrome | Inner cytochrome component of the Mtr conduit. |
| MtrB | outer-membrane β-barrel porin | Houses/organizes trans-outer-membrane electron transfer. |
| MtrC | extracellular-facing decaheme c-type cytochrome | Terminal surface electron-transfer component. |
| OmcA | outer-surface decaheme c-type cytochrome | Accessory terminal reductive interface. |
| MtrCAB–OmcA complex | outer-membrane EET module | Transfers electrons across the outer membrane to extracellular Fe(III). |
| MtrFED, DmsEFA and related conduits | alternative modules | Potentially redundant EET routes; curate only with taxon-specific evidence. |

The review evidence describes CymA, periplasmic ScyA/FccA/STC, and MtrCAB as a connected pathway. MtrCAB contains two multiheme cytochromes and spans approximately 170 Å; reconstituted systems support bidirectional transfer and rapid iron-oxide reduction. Functional redundancy is important, especially between STC and FccA. (beblawy2018extracellularreductionof pages 6-9)

### *Geobacter* pathway components

| Node | Type/localization | Curation position |
|---|---|---|
| PilA-N/PilA | pilin/filament-associated protein | Strong mutant evidence links native conductive filament properties to Fe(III)-oxide reduction, but structural interpretation remains disputed. |
| electrically conductive pili (“e-pili”) | extracellular structure | Candidate long-range EET conduit; mark model-dependent. |
| OmcE, OmcS, OmcT, OmcZ | outer-surface multiheme c-type cytochromes | Individual contributions vary by acceptor, strain, and experimental background. |
| OmcS/OmcZ cytochrome filaments | extracellular structures | Proposed nanowires, but physiological necessity is actively contested. |
| porin–cytochrome conduits | outer-membrane complexes | General mechanism candidate; individual gene clusters require species-level evidence. |

A 2023 systematic deletion study found that deleting `pilA-N`, `omcE`, `omcS`, `omcT`, or `omcZ` impaired ferrihydrite reduction to different degrees and that deleting the full tested set abolished it. (jiang2023thevariedroles pages 1-2) In contrast, a 2024 study reported that strains lacking cytochrome-filament genes retained Fe(III)-oxide reduction, whereas substitution with poorly conductive PilA strongly inhibited it. That study concluded that rigorous physiological evidence for cytochrome filaments as the primary long-range conduit was lacking. (schwarz2024lackofphysiological pages 2-4, schwarz2024lackofphysiological pages 4-8)

### Taxa

Use NCBITaxon records after accession verification for:

- *Shewanella oneidensis* MR-1 — model for Mtr-dependent extracellular Fe(III) reduction.
- *Geobacter sulfurreducens* — model for direct EET and the conductive-filament controversy.
- *Geobacter* spp., *Shewanella* spp., *Rhodoferax*, *Geothrix*, *Desulfuromonas*, and Fe(III)-reducing archaea — broader candidate taxa, but avoid inferring the trait solely from genus membership.
- *Clostridium* enrichment with Fe(III)-citrate should not be interpreted automatically as canonical EET-mediated respiration; fermentation and indirect reduction remain plausible. (shi2024responseoffe(iii)reducing pages 8-10)

## Evidence-backed candidate edges

The compact curation artifact below gives the highest-priority triples and flags contested claims.

| subject | predicate | object | taxon/context | evidence strength | DOI |
|---|---|---|---|---|---|
| Fe(III) | serves_as_terminal_electron_acceptor_for | anaerobic respiration / dissimilatory iron reduction | General trait definition; anaerobic metabolism in metal-reducing microbes (beblawy2018extracellularreductionof pages 6-9) | Strong review-level | 10.1111/mmi.14067 |
| dissimilatory Fe(III) reduction | produces | Fe(II) | Lake-sediment microcosms with ferrihydrite, Fe(III)-citrate, or Fe(III)-EDTA; Fe(II) accumulated in all amended treatments (shi2024responseoffe(iii)reducing pages 4-5, shi2024responseoffe(iii)reducing pages 2-4) | Strong experimental | 10.1007/s10533-024-01186-4 |
| CymA | transfers_electrons_to | STC / FccA periplasmic cytochromes | *Shewanella oneidensis* MR-1 anaerobic metal respiration pathway (beblawy2018extracellularreductionof pages 6-9) | Strong review-level | 10.1111/mmi.14067 |
| STC / FccA | transfer_electrons_to | MtrA in MtrCAB outer-membrane conduit | *Shewanella oneidensis* MR-1 periplasm-to-outer-membrane EET (beblawy2018extracellularreductionof pages 6-9) | Strong review-level | 10.1111/mmi.14067 |
| MtrCAB complex | enables_electron_transfer_to | extracellular solid Fe(III) acceptors | *Shewanella oneidensis* MR-1; extracellular reduction of solid electron acceptors (beblawy2018extracellularreductionof pages 6-9) | Strong review-level | 10.1111/mmi.14067 |
| Fe(III)-citrate | increases_rate_of | Fe(III) reduction relative to ferrihydrite | Lake-sediment microcosms; 5.43 vs 0.27 mmol L−1 day−1, ~20-fold faster (shi2024responseoffe(iii)reducing pages 4-5) | Strong experimental | 10.1007/s10533-024-01186-4 |
| Fe(III)-EDTA | increases_rate_of | Fe(III) reduction relative to ferrihydrite | Lake-sediment microcosms; 1.15 vs 0.27 mmol L−1 day−1, ~4-fold faster (shi2024responseoffe(iii)reducing pages 4-5) | Strong experimental | 10.1007/s10533-024-01186-4 |
| Fe(III)-EDTA amendment | enriches_for | *Geobacter* | Lake sediment community response (shi2024responseoffe(iii)reducing pages 10-11, shi2024responseoffe(iii)reducing pages 1-2, shi2024responseoffe(iii)reducing pages 8-10) | Strong experimental | 10.1007/s10533-024-01186-4 |
| ferrihydrite treatment | is_associated_with_detection_of | mtrC | Lake sediment; *Shewanella*-related marker detected only with ferrihydrite treatment (shi2024responseoffe(iii)reducing pages 10-11) | Moderate, context-specific | 10.1007/s10533-024-01186-4 |
| pilA-N deletion | impairs | ferrihydrite reduction | *Geobacter sulfurreducens* mutant phenotype (jiang2023thevariedroles pages 1-2) | Strong experimental | 10.3389/fmicb.2023.1251346 |
| omcE deletion | impairs | ferrihydrite reduction | *Geobacter sulfurreducens* mutant phenotype (jiang2023thevariedroles pages 1-2) | Strong experimental | 10.3389/fmicb.2023.1251346 |
| omcS deletion | diminishes | ferrihydrite reduction | *Geobacter sulfurreducens* mutant phenotype (jiang2023thevariedroles pages 1-2) | Strong experimental | 10.3389/fmicb.2023.1251346 |
| omcT deletion | impairs | ferrihydrite reduction | *Geobacter sulfurreducens* mutant phenotype (jiang2023thevariedroles pages 1-2) | Strong experimental | 10.3389/fmicb.2023.1251346 |
| omcZ deletion | impairs | ferrihydrite reduction | *Geobacter sulfurreducens* mutant phenotype (jiang2023thevariedroles pages 1-2) | Strong experimental but contested by later study | 10.3389/fmicb.2023.1251346 |
| deletion of pilA-N + omcE + omcS + omcT + omcZ set | abolishes | ferrihydrite reduction | *Geobacter sulfurreducens* combined deletion background (jiang2023thevariedroles pages 1-2) | Strong experimental | 10.3389/fmicb.2023.1251346 |
| poorly conductive pili (PilA-modified) | impairs | Fe(III) oxide reduction | *Geobacter sulfurreducens*; supports conductive-pili model (schwarz2024lackofphysiological pages 2-4, schwarz2024lackofphysiological pages 4-8) | Strong experimental | 10.1128/mbio.00690-24 |
| omcS deletion | does_not_necessarily_impair | Fe(III) oxide reduction | *Geobacter sulfurreducens*; later strain-specific reevaluation (schwarz2024lackofphysiological pages 2-4) | Strong experimental, conflicting with earlier reports | 10.1128/mbio.00690-24 |
| omcE or omcZ deletion | does_not_necessarily_inhibit | Fe(III) oxide reduction | *Geobacter sulfurreducens*; argues against cytochrome filaments as essential conduits (schwarz2024lackofphysiological pages 4-8) | Strong experimental, conflicting with Jiang 2023 for ferrihydrite | 10.1128/mbio.00690-24 |
| conductive pili (e-pili) | may_be_required_for | long-range extracellular electron transfer to Fe(III) oxide | *Geobacter sulfurreducens* controversy: supported by 2024 physiological study, opposed by cytochrome-filament model (schwarz2024lackofphysiological pages 2-4, schwarz2024lackofphysiological pages 4-8) | Strong but controversial | 10.1128/mbio.00690-24 |
| cytochrome filaments (OmcS/OmcZ) | proposed_as_conduits_for | extracellular electron transfer | *Geobacter sulfurreducens* controversy; proposal challenged by later physiology (jiang2023thevariedroles pages 1-2, schwarz2024lackofphysiological pages 2-4, schwarz2024lackofphysiological pages 4-8) | Moderate, controversial | 10.3389/fmicb.2023.1251346; 10.1128/mbio.00690-24 |


*Table: This table summarizes the strongest source-backed candidate edges for curation of traitmech:000031, emphasizing core respiration logic, the canonical Shewanella extracellular electron transfer chain, and contested Geobacter ferrihydrite/Fe(III) oxide mechanisms. It is useful as a compact starting point for deciding which claims are strong enough to encode and which should be flagged as controversial or context-specific.*

Additional implementation-ready triples are listed below. “Enables” should be represented with the project’s controlled causal predicate rather than copied literally if TraitMech has a fixed predicate vocabulary.

| Subject | Predicate | Object | Supporting snippet | Reference | Notes/confidence |
|---|---|---|---|---|---|
| anaerobic condition | enables | dissimilatory Fe(III) reduction | “during anaerobic growth”; respiratory electrons are conveyed to the cell surface | [Beblawy et al., July 2018](https://doi.org/10.1111/mmi.14067) | **High**, but oxygen tolerance and regulation are taxon-specific. (beblawy2018extracellularreductionof pages 6-9) |
| oxidation of organic donor/H₂ | supplies electrons to | Fe(III) respiration | Electrons from central metabolism reach CymA and extracellular acceptors | [Beblawy et al., July 2018](https://doi.org/10.1111/mmi.14067) | **High at pathway level**; donor-specific edges need organism-specific experiments. (beblawy2018extracellularreductionof pages 6-9) |
| CymA | transfers electrons to | STC/FccA | “CymA receives electrons from central metabolism”; periplasmic cytochromes mediate transfer | [Beblawy et al., July 2018](https://doi.org/10.1111/mmi.14067) | **High; *S. oneidensis*-specific.** (beblawy2018extracellularreductionof pages 6-9) |
| STC/FccA | transfers electrons to | MtrA/MtrCAB | STC and FccA provide routes to the outer-membrane complex | [Beblawy et al., July 2018](https://doi.org/10.1111/mmi.14067) | **High**, with redundancy; avoid encoding either as universally indispensable. (beblawy2018extracellularreductionof pages 6-9) |
| MtrB | organizes/enables | trans-outer-membrane electron transfer | MtrCAB is characterized as a porin–cytochrome conduit spanning the outer membrane | [Beblawy et al., July 2018](https://doi.org/10.1111/mmi.14067) | **High; taxon-specific.** (beblawy2018extracellularreductionof pages 6-9) |
| MtrC/OmcA | transfers electrons to | extracellular Fe(III) | MtrCAB–OmcA supports rapid iron-oxide reduction | [Beblawy et al., July 2018](https://doi.org/10.1111/mmi.14067) | **High for *S. oneidensis* architecture**, though exact mineral-contact mechanism remains incompletely resolved. (beblawy2018extracellularreductionof pages 6-9) |
| Fe(III)-citrate | increases | Fe(III)-reduction rate relative to ferrihydrite | 5.43 versus 0.27 mmol L⁻¹ d⁻¹; approximately 20-fold faster | [Shi et al., October 2024](https://doi.org/10.1007/s10533-024-01186-4) | **High within this lake-sediment microcosm.** Do not universalize the fold change. (shi2024responseoffe(iii)reducing pages 4-5) |
| Fe(III)-EDTA | increases | Fe(III)-reduction rate relative to ferrihydrite | 1.15 versus 0.27 mmol L⁻¹ d⁻¹; approximately fourfold faster | [Shi et al., October 2024](https://doi.org/10.1007/s10533-024-01186-4) | **High but artificial-chelator-specific.** (shi2024responseoffe(iii)reducing pages 4-5) |
| Fe(III) solubility/bioavailability | positively influences | Fe(III)-reduction rate | Dissolved Fe(III)-organic-matter complexes reduced faster than solid ferrihydrite | [Shi et al., October 2024](https://doi.org/10.1007/s10533-024-01186-4) | **Moderate–high** as an inferred explanatory edge. (shi2024responseoffe(iii)reducing pages 1-2) |
| Fe(III)-EDTA amendment | enriches | *Geobacter* | “Geobacter dominated in Fe(III)-EDTA treatments” | [Shi et al., October 2024](https://doi.org/10.1007/s10533-024-01186-4) | **High association, not a universal causal mechanism.** (shi2024responseoffe(iii)reducing pages 10-11) |
| Fe(III)-citrate amendment | enriches | *Clostridium* | “Clostridium was enriched with Fe(III)-citrate” | [Shi et al., October 2024](https://doi.org/10.1007/s10533-024-01186-4) | **Association only**; citrate is also carbon substrate/chelator, so do not equate enrichment with respiratory Fe reduction. (shi2024responseoffe(iii)reducing pages 10-11, shi2024responseoffe(iii)reducing pages 8-10) |
| ferrihydrite amendment | increases | iron-reduction/assimilation gene copy numbers | Ferrihydrite significantly increased relevant gene copies over the longer experiment | [Shi et al., October 2024](https://doi.org/10.1007/s10533-024-01186-4) | **Assay-specific association**; gene abundance is not phenotype. (shi2024responseoffe(iii)reducing pages 10-11) |
| ferrihydrite treatment | associated with detection of | `mtrC` | `mtrC` was detected only in the ferrihydrite treatment | [Shi et al., October 2024](https://doi.org/10.1007/s10533-024-01186-4) | **Moderate and community-specific**; do not encode `mtrC` as a universal marker. (shi2024responseoffe(iii)reducing pages 10-11) |
| native conductive PilA filament properties | enable | long-range Fe(III)-oxide reduction | Poorly conductive PilA substitution severely impaired reduction | [Schwarz et al., May 2024](https://doi.org/10.1128/mbio.00690-24) | **Strong within tested strains**, but retain a controversy flag. (schwarz2024lackofphysiological pages 2-4, schwarz2024lackofphysiological pages 4-8) |
| OmcS/OmcZ filaments | enable | long-range Fe(III)-oxide electron transfer | Proposed as conductive cytochrome nanowires in one model | [Jiang et al., October 2023](https://doi.org/10.3389/fmicb.2023.1251346) | **Uncertain/contested**; not suitable as an unqualified causal edge. (jiang2023thevariedroles pages 1-2) |
| deletion of `omcE`/`omcZ` | does not necessarily inhibit | Fe(III)-oxide reduction | 2024 mutants retained reduction | [Schwarz et al., May 2024](https://doi.org/10.1128/mbio.00690-24) | **Strong negative evidence**, conflicting with the 2023 ferrihydrite study; assay, strain, and mutant construction may matter. (schwarz2024lackofphysiological pages 4-8) |

## Recent developments and quantitative evidence

### Substrate chemistry is a major causal variable

Shi et al. used 25 g lake sediment and 25 mL lake water in 100-mL serum bottles, incubated at 25°C in darkness, with 20 mM ferrihydrite, Fe(III)-citrate, or Fe(III)-EDTA in triplicate. Metagenomes were sequenced at approximately 6 Gb raw data per sample. (shi2024responseoffe(iii)reducing pages 2-4)

The measured reduction rates were **5.43 mmol L⁻¹ d⁻¹ for Fe(III)-citrate, 1.15 for Fe(III)-EDTA, and 0.27 for ferrihydrite**. The soluble complexes approached equilibrium in about four days, compared with about 60 days for ferrihydrite. Final Fe(II) production from 20 mM Fe(III) was approximately 20 mM for citrate (100%), 6 mM for EDTA (30%), and 12 mM for ferrihydrite (60%). These data show that rate and final extent are distinct phenotypes: citrate was both fastest and most complete, whereas EDTA was faster than ferrihydrite but less completely reduced. (shi2024responseoffe(iii)reducing pages 4-5)

The same paper summarized earlier systems in which Fe(III)-citrate and Fe(III)-EDTA reduction rates were respectively 5–24-fold and 2–6-fold above ferrihydrite; a cited paddy-soil comparison reported approximately 14-fold and 2.3-fold stimulation. These literature-derived fold changes should not be copied as universal constants. (shi2024responseoffe(iii)reducing pages 8-10)

### The *Geobacter* nanowire mechanism remains unsettled

The authoritative interpretation is not consensus. Jiang et al. (2023) found substrate-dependent impairment across `pilA-N`, `omcE`, `omcS`, `omcT`, and `omcZ` mutants, supporting a distributed and partly redundant network. (jiang2023thevariedroles pages 1-2) Schwarz et al. (2024), however, reported effective Fe(III)-oxide reduction after deleting filament-forming cytochromes and strong impairment when pili were engineered to be poorly conductive; they argued that cytochrome filaments lack rigorous physiological evidence as the primary conduit. (schwarz2024lackofphysiological pages 2-4, schwarz2024lackofphysiological pages 4-8)

For TraitMech, the defensible graph should therefore encode **multiple surface cytochromes and conductive extracellular structures as context-dependent contributors**, not a single universal “nanowire” mechanism.

## Current applications and real-world implementation

1. **Biogeochemical modeling.** The trait controls Fe mineral transformation and couples iron cycling to carbon turnover in anoxic sediments, soils, and groundwater. The 2024 sediment data demonstrate that acceptor speciation can change rates by approximately an order of magnitude or more, so environmental models should not treat all Fe(III) pools as equally bioavailable. (shi2024responseoffe(iii)reducing pages 1-2, shi2024responseoffe(iii)reducing pages 4-5)
2. **Bioremediation.** Fe-reducing organisms and EET pathways can influence contaminant sorption, oxidation state, mobility, and co-precipitation. However, contaminant transformation is often an indirect consequence of biogenic Fe(II), so it should not automatically be placed inside the core trait graph.
3. **Bioelectrochemical systems.** Mtr and *Geobacter* EET components are exploited in microbial fuel cells and electrode biofilms. Electrode reduction is a useful engineering analogue, but its causal graph should be connected to—not conflated with—Fe(III) respiration because gene requirements can differ by extracellular acceptor. (jiang2023thevariedroles pages 1-2)
4. **Synthetic biology.** Transfer of EET modules into heterologous hosts is being explored to connect intracellular metabolism with solid materials. For TraitMech curation, heterologous current production should count as mechanistic support for an electron-transfer module, not by itself as proof of dissimilatory iron-reducing growth.
5. **Biogenic materials and mineral synthesis.** Controlled extracellular reduction can produce Fe-bearing minerals and other inorganic nanomaterials. This is an application of the EET machinery rather than a defining component of the trait.

## Recommended minimal graph expansion

The existing eight-node/six-edge graph can be expanded conservatively around this backbone:

1. **organic donor or H₂ → supplies electrons to → quinone/quinol pool**
2. **quinol oxidation → supplies electrons to → inner-membrane EET hub**
3. **inner-membrane hub → reduces → periplasmic electron carriers**
4. **periplasmic carriers → reduce → outer-membrane porin–cytochrome conduit**
5. **outer-surface cytochromes/conductive structures → transfer electrons to → extracellular Fe(III)**
6. **Fe(III) reduction → produces → Fe(II)**
7. **electron-transport chain → supports → energy conservation/growth under anoxia**
8. **Fe(III) solubility/mineralogy → modulates → reduction rate**

Implement the inner/outer-membrane nodes as **taxon-specific alternatives**: CymA–STC/FccA–MtrCAB/OmcA for *Shewanella*; porin–cytochrome pathways plus surface cytochromes/conductive filaments for *Geobacter*. Do not merge these into a fictitious universal gene pathway.

## Warnings: claims not ready for unqualified TraitMech curation

1. **Do not assert that OmcS or OmcZ cytochrome filaments are the universal long-range conduit.** The 2024 physiological study directly disputes that interpretation. (schwarz2024lackofphysiological pages 2-4, schwarz2024lackofphysiological pages 4-8)
2. **Do not assert that e-pili are universally required across iron reducers.** The evidence is strongest for particular *G. sulfurreducens* backgrounds, not all taxa.
3. **Do not use `mtrC`, `omcS`, or any single gene as a universal trait marker.** Functional redundancy, non-orthologous architectures, and community-level false positives are substantial. (beblawy2018extracellularreductionof pages 6-9, shi2024responseoffe(iii)reducing pages 10-11)
4. **Do not generalize ferrihydrite deletion phenotypes to electrodes or soluble Fe(III).** The 2023 study itself found acceptor-dependent gene requirements. (jiang2023thevariedroles pages 1-2)
5. **Do not curate Fe(III)-EDTA as a natural universal substrate.** It is an informative experimental chelate but often an artificial environmental condition.
6. **Do not infer respiratory growth from Fe(II) production alone.** Require growth yield, ATP/biomass, donor-dependent stoichiometry, respiratory inhibition, or genetics connecting the reduction to electron transport.
7. **Do not assign causality from taxonomic enrichment alone.** Citrate can act as chelator and carbon source, while indirect reduction can occur through fermentation products. (shi2024responseoffe(iii)reducing pages 8-10)
8. **Do not invent ontology identifiers.** Resolve exact ChEBI, GO, ENVO, NCBITaxon, and UniProt accessions against their current releases during YAML implementation.

## DOI-first bibliography

1. **Schwarz IA et al.** “Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer.” *mBio* 15, May 2024. DOI: [10.1128/mbio.00690-24](https://doi.org/10.1128/mbio.00690-24). (schwarz2024lackofphysiological pages 2-4, schwarz2024lackofphysiological pages 4-8)
2. **Shi T et al.** “Response of Fe(III)-reducing kinetics, microbial community structure and Fe(III)-related functional genes to Fe(III)-organic matter complexes and ferrihydrite in lake sediment.” *Biogeochemistry* 167:1553–1565, October 2024. DOI: [10.1007/s10533-024-01186-4](https://doi.org/10.1007/s10533-024-01186-4). (shi2024responseoffe(iii)reducing pages 10-11, shi2024responseoffe(iii)reducing pages 1-2, shi2024responseoffe(iii)reducing pages 8-10, shi2024responseoffe(iii)reducing pages 4-5, shi2024responseoffe(iii)reducing pages 2-4)
3. **Jiang J et al.** “The varied roles of pilA-N, omcE, omcS, omcT, and omcZ in extracellular electron transfer by *Geobacter sulfurreducens*.” *Frontiers in Microbiology* 14, October 2023. DOI: [10.3389/fmicb.2023.1251346](https://doi.org/10.3389/fmicb.2023.1251346). (jiang2023thevariedroles pages 1-2)
4. **Beblawy S et al.** “Extracellular reduction of solid electron acceptors by *Shewanella oneidensis*.” *Molecular Microbiology* 109:571–583, July 2018. DOI: [10.1111/mmi.14067](https://doi.org/10.1111/mmi.14067). (beblawy2018extracellularreductionof pages 6-9)
5. **Conley BE et al.** “A hybrid extracellular electron transfer pathway enhances the survival of *Vibrio natriegens*.” *Applied and Environmental Microbiology* 86, September 2020. DOI: [10.1128/AEM.01253-20](https://doi.org/10.1128/AEM.01253-20). This paper supports taxonomic diversity and the CymA/PdsA/MtrCAB module but should be treated as a *Vibrio*-specific survival/Fe-reduction example rather than the universal architecture. (conley2020ahybridextracellular pages 29-31)

**Curation judgment:** the core Fe(III)-as-acceptor → Fe(II)-production → energy-conservation chain is mature enough for REVIEWED status. The *Shewanella* Mtr pathway is suitable as a taxon-specific mechanistic branch. The *Geobacter* surface-conduit branch should retain explicit provenance, acceptor/strain context, and uncertainty annotations until the conductive-pili versus cytochrome-filament dispute is resolved.

References

1. (beblawy2018extracellularreductionof pages 6-9): Sebastian Beblawy, Thea Bursac, Catarina Paquete, Ricardo Louro, Thomas A. Clarke, and Johannes Gescher. Extracellular reduction of solid electron acceptors by shewanella oneidensis. Molecular Microbiology, 109:571-583, Jul 2018. URL: https://doi.org/10.1111/mmi.14067, doi:10.1111/mmi.14067. This article has 141 citations and is from a domain leading peer-reviewed journal.

2. (jiang2023thevariedroles pages 1-2): Jie Jiang, Pengchen He, Ying Luo, Zhao-Kuai Peng, Yongguang Jiang, Yidan Hu, Lei Qi, Xiuzhu Dong, Yiran Dong, and Liang Shi. The varied roles of pila-n, omce, omcs, omct, and omcz in extracellular electron transfer by geobacter sulfurreducens. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1251346, doi:10.3389/fmicb.2023.1251346. This article has 41 citations and is from a peer-reviewed journal.

3. (shi2024responseoffe(iii)reducing pages 10-11): Tingyang Shi, Chao Peng, Lu Lu, Zhen Yang, Yundang Wu, Zimeng Wang, and Andreas Kappler. Response of fe(iii)-reducing kinetics, microbial community structure and fe(iii)-related functional genes to fe(iii)-organic matter complexes and ferrihydrite in lake sediment. Biogeochemistry, 167:1553-1565, Oct 2024. URL: https://doi.org/10.1007/s10533-024-01186-4, doi:10.1007/s10533-024-01186-4. This article has 12 citations and is from a peer-reviewed journal.

4. (shi2024responseoffe(iii)reducing pages 1-2): Tingyang Shi, Chao Peng, Lu Lu, Zhen Yang, Yundang Wu, Zimeng Wang, and Andreas Kappler. Response of fe(iii)-reducing kinetics, microbial community structure and fe(iii)-related functional genes to fe(iii)-organic matter complexes and ferrihydrite in lake sediment. Biogeochemistry, 167:1553-1565, Oct 2024. URL: https://doi.org/10.1007/s10533-024-01186-4, doi:10.1007/s10533-024-01186-4. This article has 12 citations and is from a peer-reviewed journal.

5. (schwarz2024lackofphysiological pages 2-4): Ingrid A. Schwarz, Baha Alsaqri, Yassir Lekbach, Kathryn Henry, Sydney Gorman, Trevor Woodard, Laura Dion, Lauren Real, Dawn E. Holmes, Jessica A. Smith, and Derek R. Lovley. Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer. mBio, May 2024. URL: https://doi.org/10.1128/mbio.00690-24, doi:10.1128/mbio.00690-24. This article has 15 citations and is from a domain leading peer-reviewed journal.

6. (schwarz2024lackofphysiological pages 4-8): Ingrid A. Schwarz, Baha Alsaqri, Yassir Lekbach, Kathryn Henry, Sydney Gorman, Trevor Woodard, Laura Dion, Lauren Real, Dawn E. Holmes, Jessica A. Smith, and Derek R. Lovley. Lack of physiological evidence for cytochrome filaments functioning as conduits for extracellular electron transfer. mBio, May 2024. URL: https://doi.org/10.1128/mbio.00690-24, doi:10.1128/mbio.00690-24. This article has 15 citations and is from a domain leading peer-reviewed journal.

7. (shi2024responseoffe(iii)reducing pages 8-10): Tingyang Shi, Chao Peng, Lu Lu, Zhen Yang, Yundang Wu, Zimeng Wang, and Andreas Kappler. Response of fe(iii)-reducing kinetics, microbial community structure and fe(iii)-related functional genes to fe(iii)-organic matter complexes and ferrihydrite in lake sediment. Biogeochemistry, 167:1553-1565, Oct 2024. URL: https://doi.org/10.1007/s10533-024-01186-4, doi:10.1007/s10533-024-01186-4. This article has 12 citations and is from a peer-reviewed journal.

8. (shi2024responseoffe(iii)reducing pages 4-5): Tingyang Shi, Chao Peng, Lu Lu, Zhen Yang, Yundang Wu, Zimeng Wang, and Andreas Kappler. Response of fe(iii)-reducing kinetics, microbial community structure and fe(iii)-related functional genes to fe(iii)-organic matter complexes and ferrihydrite in lake sediment. Biogeochemistry, 167:1553-1565, Oct 2024. URL: https://doi.org/10.1007/s10533-024-01186-4, doi:10.1007/s10533-024-01186-4. This article has 12 citations and is from a peer-reviewed journal.

9. (shi2024responseoffe(iii)reducing pages 2-4): Tingyang Shi, Chao Peng, Lu Lu, Zhen Yang, Yundang Wu, Zimeng Wang, and Andreas Kappler. Response of fe(iii)-reducing kinetics, microbial community structure and fe(iii)-related functional genes to fe(iii)-organic matter complexes and ferrihydrite in lake sediment. Biogeochemistry, 167:1553-1565, Oct 2024. URL: https://doi.org/10.1007/s10533-024-01186-4, doi:10.1007/s10533-024-01186-4. This article has 12 citations and is from a peer-reviewed journal.

10. (conley2020ahybridextracellular pages 29-31): Bridget E. Conley, Matthew T. Weinstock, Daniel R. Bond, and Jeffrey A. Gralnick. A hybrid extracellular electron transfer pathway enhances the survival of vibrio natriegens. Sep 2020. URL: https://doi.org/10.1128/aem.01253-20, doi:10.1128/aem.01253-20. This article has 40 citations and is from a peer-reviewed journal.