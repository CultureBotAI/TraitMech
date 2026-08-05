---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:33:03.793825'
end_time: '2026-08-04T05:41:41.280227'
duration_seconds: 517.49
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: Cable bacteria metabolism
  trait_identifier: METPO:1002003
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: cable_bacteria_metabolism
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which electrons are transferred over centimeter-scale
    distances through multicellular filaments.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1073/pnas.1800367115: Long-distance electron transport
    in individual, living cable bacteria (Study directly demonstrates long-distance
    electron transport in cable bacteria.) | DOI:10.3389/fmars.2017.00028: oxidize
    sulfide in deeper sediments (Study supports electrogenic sulfur oxidation with
    sulfide oxidation and oxygen reduction zones.)'
  causal_graph_summary: 'cable_bacteria_long_distance_electron_transport: 14 nodes,
    14 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Cable bacteria metabolism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1002003
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred over centimeter-scale distances through multicellular filaments.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1800367115: Long-distance electron transport in individual, living cable bacteria (Study directly demonstrates long-distance electron transport in cable bacteria.) | DOI:10.3389/fmars.2017.00028: oxidize sulfide in deeper sediments (Study supports electrogenic sulfur oxidation with sulfide oxidation and oxygen reduction zones.)
- **Existing causal graph summary:** cable_bacteria_long_distance_electron_transport: 14 nodes, 14 edges

## Research Objective

Research the microbial trait **Cable bacteria metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cable_bacteria_metabolism.yaml`.

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
- **Trait label:** Cable bacteria metabolism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1002003
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which electrons are transferred over centimeter-scale distances through multicellular filaments.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1073/pnas.1800367115: Long-distance electron transport in individual, living cable bacteria (Study directly demonstrates long-distance electron transport in cable bacteria.) | DOI:10.3389/fmars.2017.00028: oxidize sulfide in deeper sediments (Study supports electrogenic sulfur oxidation with sulfide oxidation and oxygen reduction zones.)
- **Existing causal graph summary:** cable_bacteria_long_distance_electron_transport: 14 nodes, 14 edges

## Research Objective

Research the microbial trait **Cable bacteria metabolism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cable_bacteria_metabolism.yaml`.

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


# Curation-focused research report: Cable bacteria metabolism

## Trait record and scope

- **Trait label:** Cable bacteria metabolism
- **Trait identifier:** **METPO:1002003**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** METPO:1000060
- **Operational definition:** a filament-level metabolism in which oxidation and reduction half-reactions occur in spatially separated cells and are coupled by electronic transport over millimetre-to-centimetre distances.

The canonical phenotype is **electrogenic sulfur oxidation**: cells in deeper anoxic sediment oxidize sulfide, electrons travel through a multicellular filament, and cells near an oxic boundary reduce oxygen. Nitrate can substitute as an acceptor in some taxa or conditions. This division of labor distinguishes the trait from ordinary intracellular respiration and short-range extracellular electron transfer. Direct Raman experiments showed a cytochrome-redox gradient along individual living filaments; removing oxygen or laser-cutting the filament immediately collapsed the gradient, establishing that electron flow depends on an intact connection between donor and acceptor zones (bjerg2018longdistanceelectrontransport pages 1-2).

The trait should be represented at the **whole-filament level**, because no single cell necessarily contains both terminal half-reactions. Genomic and physiological models distinguish anoxic “anodic” cells from oxic “cathodic” cells and place energy conservation principally in sulfide-oxidizing cells; cathodic oxygen reduction without energy conservation remains a well-supported model rather than a completely resolved molecular mechanism (kjeldsen2019ontheevolution pages 1-1, wang2024electrogenicsulfuroxidation pages 2-3).

### Boundary cases

1. **Sulfur disproportionation** by groundwater cable bacteria is metabolic capacity adjacent to, but not identical with, the defining long-distance metabolism. Curate it as a taxon/condition-specific branch rather than as necessary for `METPO:1002003`.
2. **Nitrate reduction/DNRA** is an alternative cathodic module, not required for every cable-bacterium filament. The 2024 synthesis describes nitrate reduction toward ammonium, but taxon and assay context should be retained (wang2024electrogenicsulfuroxidation pages 2-3).
3. **Electrode respiration/EET** is an experimentally demonstrated extension of cable-bacterium metabolism, but electrode use is not part of the trait definition. In 2024, living filaments moved toward +200 mV carbon electrodes and withdrew when the potential was removed (bonne2024interactionofliving pages 1-2, bonne2024interactionofliving pages 2-5).
4. Generic nanowire production, conductive biofilms, sulfate reduction, and sulfur oxidation by non-cable filamentous bacteria are insufficient. The diagnostic feature is centimeter-scale conduction through a multicellular cable-bacterium filament.

## Current mechanistic model

Anoxic cells oxidize reduced sulfur and pass electrons into a periplasmic transport system. A continuous network of parallel conductive fibers traverses cells and cell–cell junctions. Direct electrode measurements detected nanoampere currents across intact filaments as long as 10.1 mm and more than 2,000 cells; isolated fiber networks reached conductivities up to 79 S cm⁻¹. Conductance persisted under vacuum but fell to approximately 2% after 30 minutes in air, demonstrating electronic rather than ionic charge transport (meysman2019ahighlyconductive pages 1-2).

At the acceptor end, electrons are discharged to oxygen, or in some organisms to nitrate. Periplasmic c-type cytochromes show redox gradients and are plausible interfaces between metabolism and the conductive fibers, but their status as the principal long-range carrier is not established. Likewise, the precise terminal oxygen reductase is unresolved and may vary among cable-bacterium lineages (wang2024electrogenicsulfuroxidation pages 2-3, wang2024electrogenicsulfuroxidation pages 3-3).

The leading 2019 metabolic reconstruction proposed sulfide oxidation by reversal of the canonical dissimilatory sulfate-reduction pathway and autotrophic carbon fixation through the Wood–Ljungdahl pathway. Because more than half of the genes in the analyzed genomes were then unknown and pure cultures were unavailable, these pathway directions should be encoded as proposed rather than definitive catalytic steps (kjeldsen2019ontheevolution pages 1-1). Recent genomic work continues to reveal lineage-specific alternatives; for example, a 2025 strain encodes a complete reductive Dsr repertoire, Psr/PhsABC, a Nap system, and a truncated hemoglobin proposed for oxygen reduction, underscoring that genome presence alone does not establish reaction direction (hiralal2025anovelcable pages 10-13).

A major development is the identification of a **sulfur-ligated nickel cofactor** in the conductive protein core. Oxidation or removal of nickel reduces conductivity, and 2024 comparative genomics found marked adaptations in nickel import, export, binding, and chaperoning. These results support a causal nickel-dependent conduction module, although the exact conductive protein sequence and electron-transfer chemistry remain unresolved (zhuang2024electrontransferin pages 6-8, wang2024electrogenicsulfuroxidation pages 3-3).

## Candidate nodes grouped by type

### Trait, organism, and habitat nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| Cable bacteria metabolism | **METPO:1002003** | Root trait node; quote identifier verbatim in YAML. |
| Cable bacteria | NCBITaxon label search required | Include *Candidatus Electrothrix* and *Candidatus Electronema* as organism contexts; do not invent taxon CURIEs. |
| Multicellular cable-bacterium filament | Label-only candidate | Functional unit spanning donor and acceptor zones. |
| Anodic cell / cathodic cell | Label-only candidates | Physiological states/locations, not established stable cell types. |
| Aquatic sediment | ENVO grounding recommended after registry lookup | Marine, estuarine, freshwater, and groundwater contexts should remain distinguishable. |
| Anoxic sulfidic sediment zone | ENVO label candidate | Donor-side microenvironment. |
| Oxic sediment surface zone | ENVO label candidate | Oxygen-acceptor microenvironment. |
| Suboxic zone | ENVO label candidate | Geochemical phenotype between O₂ and H₂S fronts. |

Cable bacteria occur in marine and freshwater sediments and can generate 1–4 cm zones lacking both detectable oxygen and sulfide, with characteristic pH separation between cathodic and anodic regions (kjeldsen2019ontheevolution pages 1-1).

### Chemicals and electron-transfer roles

| Node | Suggested CURIE | Role |
|---|---|---|
| Hydrogen sulfide | CHEBI:16136 | Canonical electron donor/substrate. |
| Sulfide | CHEBI registry verification required for protonation-specific form | Reduced-sulfur donor pool. |
| Oxygen | CHEBI:15379 | Canonical terminal electron acceptor. |
| Nitrate | CHEBI:17632 | Alternative acceptor in supported taxa/conditions. |
| Nitrite | CHEBI:16301 | Candidate DNRA intermediate. |
| Ammonium | CHEBI:28938 | Candidate nitrate-reduction product. |
| Sulfate | CHEBI:16189 | Net oxidized sulfur product. |
| Elemental sulfur | CHEBI:33403 | Taxon/assay-specific donor or disproportionation substrate. |
| Thiosulfate | CHEBI:26977 | Taxon/assay-specific sulfur substrate. |
| Carbon dioxide | CHEBI:16526 | Candidate autotrophic carbon source. |
| Nickel atom/ion | CHEBI grounding should be chosen according to measured chemical state | Structural/biosynthetic requirement for conductive fibers. |
| Electron | CHEBI:10545 | Transported entity. |
| Carbon electrode/anode | Label-only experimental node | Extracellular terminal acceptor in bioelectrochemical assays. |

### Pathways and biological processes

- Long-distance electron transport—defining process; retain label-only if no exact GO term is available.
- Electrogenic sulfur oxidation—central metabolic module.
- Sulfide oxidation to sulfate—net donor-side transformation.
- Dissimilatory sulfate-reduction pathway operating in reverse—**uncertain directionality**.
- Wood–Ljungdahl pathway / reductive acetyl-CoA pathway—candidate carbon-fixation module.
- Oxygen reduction—cathodic module; exact enzyme unresolved.
- Nitrate reduction to ammonium/DNRA—alternative, taxon-specific cathodic module.
- Sulfur disproportionation—boundary-case module.
- Extracellular electron transfer to electrodes—experimentally supported extension.
- Nickel uptake, chaperoning, and export—supporting homeostasis module.
- Electronic conduction—molecular function of the fiber network.

Use GO or pathway CURIEs only after exact ontology lookup; broad terms can lose the distinctive centimeter-scale and multicellular semantics.

### Genes, proteins, complexes, and structures

| Candidate | Status |
|---|---|
| Conductive periplasmic fiber network | Directly localized and electrically characterized; label-only node recommended. |
| Conductive protein core and insulating shell | Structurally supported; constituent protein identities incompletely resolved. |
| Sulfur-ligated NiBiD-like nickel cofactor | Strong spectroscopic/conductivity evidence; exact ontology grounding uncertain. |
| Periplasmic c-type cytochromes | Redox-active candidates; do not assert that they form the long-range wire. |
| SQR, sulfide:quinone oxidoreductase | Proposed donor-side entry enzyme; pathway placement remains uncertain. |
| DsrAB and associated Dsr proteins | Genomically supported; oxidative direction should be marked inferred. |
| Sat, AprAB, QmoABC | Candidate reverse sulfate-reduction-pathway components. |
| NapAB / nap operon | Candidate periplasmic nitrate-reduction module; strain-specific evidence. |
| Truncated hemoglobin | Candidate oxygen reductase in some strains; not universal. |
| RcnA and nickel import/chaperone systems | Strong 2024 comparative-genomic candidates supporting nickel homeostasis. |
| Quinone pool | Proposed intermediate between sulfur oxidation and periplasmic transfer. |

The strongest curation-ready edges are summarized below.

| subject | predicate | object | evidence strength (direct/proposed) | key quantitative or experimental support | DOI |
|---|---|---|---|---|---|
| cable bacteria anodic cells in anoxic sediment | oxidize sulfide and release electrons for filament transport | long-distance electron transport along filament | proposed | Genomic/physiological model places sulfide oxidation in anodic cells in deeper anoxic layers and coupling to distant cathodic reduction; trait-defining phenotype reproduced across studies, but immediate electron-release step is mechanistic inference rather than directly visualized in a single assay (kjeldsen2019ontheevolution pages 1-1, wang2024electrogenicsulfuroxidation pages 2-3) | 10.1073/pnas.1903514116; 10.1016/j.ese.2023.100371 |
| conductive periplasmic fibers embedded in cable bacteria cell envelope | conduct electrons over centimeter distances | cathodic end of filament | direct | Direct electrode measurements showed nanoampere currents in intact filaments up to 10.1 mm long through >2000 cells; parallel periplasmic fibers reached conductivity up to 79 S cm^-1; charge transfer remained stable under vacuum but declined to ~2% after 30 min air exposure (meysman2019ahighlyconductive pages 1-2) | 10.1038/s41467-019-12115-7 |
| long-distance electrons in cable bacteria filament | enable oxygen reduction in cathodic cells near oxic zone | oxygen | direct/proposed | Resonance Raman microscopy showed cytochrome redox gradients along living filaments connected to both H2S and O2, supporting electron flow from sulfide zone to oxic zone; oxygen reduction in terminal/cathodic cells is strongly supported physiologically, while exact terminal reductase remains unresolved (bjerg2018longdistanceelectrontransport pages 1-2, kjeldsen2019ontheevolution pages 1-1) | 10.1073/pnas.1800367115; 10.1073/pnas.1903514116 |
| oxygen removal or laser cutting of connected filament | collapses | cytochrome redox gradient along filament | direct | In living individual filaments, the cytochrome redox-state gradient immediately broke down upon oxygen removal or laser cutting, demonstrating dependence on intact long-distance electron transport between donor and acceptor zones (bjerg2018longdistanceelectrontransport pages 1-2, wang2024electrogenicsulfuroxidation pages 3-3) | 10.1073/pnas.1800367115; 10.1016/j.ese.2023.100371 |
| sulfur-ligated nickel cofactor in fiber core | supports | periplasmic fiber conductivity | direct | Conductive fibers contain a protein core with sulfur-ligated nickel; nickel oxidation or removal decreased conductivity; 2024 comparative genomics found cable bacteria enriched in nickel-homeostasis genes, consistent with nickel-dependent conduction biology (wang2024electrogenicsulfuroxidation pages 3-3, zhuang2024electrontransferin pages 6-8) | 10.1016/j.ese.2023.100371; 10.3390/life14050591 |
| poised carbon electrode (+200 mV) | attracts and accepts electrons from | living cable bacteria | direct | Live cable bacteria moved toward carbon felt/fiber electrodes poised at +200 mV and retracted when potential was switched off; currents ranged ~17-78 uA; qPCR found cable bacteria 490-fold more abundant on poised electrodes than sediment and 640-fold more abundant than unpoised controls (bonne2024interactionofliving pages 1-2, bonne2024interactionofliving pages 2-5) | 10.1128/aem.00795-24 |
| cable bacteria attached to BMFC anode | transfer electrons to | anode as terminal acceptor under anoxia | direct | In benthic microbial fuel cells, cable bacteria were identified attached to anodes poised at ~170-250 mV vs SHE, consistent with long-distance extracellular electron transport to electrodes in anaerobic sediment (reimers2017theidentificationof pages 1-2) | 10.3389/fmicb.2017.02055 |


*Table: This table compiles the strongest candidate causal triples for METPO:1002003 with emphasis on direct experiments and key quantitative support. It is useful as a compact starting point for TraitMech edge curation while clearly separating direct evidence from mechanistic proposals.*

## Expanded candidate causal edges

“Direct” denotes intervention, electrical measurement, imaging, or condition-dependent physiological evidence. “Proposed” denotes genomic reconstruction or mechanistic interpretation.

| Subject | Predicate | Object | Reference and supporting snippet | Curation notes |
|---|---|---|---|---|
| Intact cable-bacterium filament | transports | electrons over millimetre-to-centimetre distances | Bjerg et al.: cytochrome gradients “immediately broke down upon oxygen removal or laser cutting”; DOI 10.1073/pnas.1800367115 (bjerg2018longdistanceelectrontransport pages 1-2) | **Direct; core edge.** |
| Conductive periplasmic fibers | enable | centimeter-scale electron transport | Meysman et al.: currents across “10.1 mm” and “>2000 adjacent cells”; conductivity “up to 79 S cm⁻¹”; DOI 10.1038/s41467-019-12115-7 (meysman2019ahighlyconductive pages 1-2) | **Direct; core edge.** |
| Laser cutting of filament | disrupts | cytochrome redox gradient | Gradient broke down after cutting; DOI 10.1073/pnas.1800367115 (bjerg2018longdistanceelectrontransport pages 1-2) | **Direct perturbation; high confidence.** |
| Oxygen removal | causes | reduction of filament cytochromes / collapse of redox gradient | Electrons accumulated when oxygen was unavailable; DOI 10.1073/pnas.1800367115 (bjerg2018longdistanceelectrontransport pages 1-2) | Direct evidence that oxygen drains transported electrons. |
| Sulfide oxidation in anodic cells | supplies | electrons to long-distance transport | Genomic/physiological model places sulfide oxidation in deeper anoxic cells; DOI 10.1073/pnas.1903514116 (kjeldsen2019ontheevolution pages 1-1) | **Proposed mechanistic edge**, although net coupling is strongly established. |
| Long-distance electron transport | couples | sulfide oxidation to oxygen reduction | Spatially separated half-reactions across the filament; DOI 10.1073/pnas.1903514116 and 10.1016/j.ese.2023.100371 (kjeldsen2019ontheevolution pages 1-1, wang2024electrogenicsulfuroxidation pages 2-3) | Core trait relation; represent as a process-level edge. |
| Oxygen | accepts | filament-transported electrons | Oxygen removal collapses redox gradient; DOI 10.1073/pnas.1800367115 (bjerg2018longdistanceelectrontransport pages 1-2) | Direct at physiological level; terminal enzyme unknown. |
| Nitrate | acts as alternative acceptor for | cable-bacterium electron transport | 2024 synthesis reports oxygen and nitrate as terminal acceptors and DNRA to ammonium; DOI 10.1016/j.ese.2023.100371 (wang2024electrogenicsulfuroxidation pages 2-3) | **Taxon-/condition-specific; moderate confidence.** |
| Reverse Dsr pathway | oxidizes | sulfide toward sulfate | 2019 genomes/proteomes “suggest” reversal of canonical sulfate reduction; DOI 10.1073/pnas.1903514116 (kjeldsen2019ontheevolution pages 1-1) | **Uncertain direction; do not encode as established enzyme-by-enzyme causation.** |
| Wood–Ljungdahl pathway | fixes | carbon dioxide | 2019 metabolic reconstruction; DOI 10.1073/pnas.1903514116 (kjeldsen2019ontheevolution pages 1-1) | Genomic/proteomic support; not defining for the trait. |
| Sulfur-ligated nickel cofactor | supports | conductive-fiber conductivity | Nickel oxidation/removal decreased conductivity; DOI 10.1016/j.ese.2023.100371 (wang2024electrogenicsulfuroxidation pages 3-3) | Strong functional association; exact protein and chemistry unresolved. |
| Nickel-homeostasis gene repertoire | enables biosynthetic support for | nickel-dependent conduction | 2024 comparative-genomic evidence across cable-bacterium genomes; DOI 10.1186/s12864-024-10594-7 (zhuang2024electrontransferin pages 6-8) | Genotype-to-trait edge remains inferential. |
| +200 mV carbon electrode | attracts | living cable bacteria | Filaments approached poised electrodes and retracted when potential was switched off; DOI 10.1128/aem.00795-24 (bonne2024interactionofliving pages 1-2) | Direct behavior; “electrotaxis” should be used cautiously unless authors establish sensing mechanism. |
| Cable bacteria | transfer electrons to | poised carbon electrode under anoxia | Currents of approximately 17–78 µA and biotic redox peaks; DOI 10.1128/aem.00795-24 (bonne2024interactionofliving pages 2-5) | Direct system-level EET; community/enrichment context. |
| BMFC anode at approximately 170–250 mV vs SHE | serves as | anaerobic electron acceptor | Cable bacteria identified attached to the anode; DOI 10.3389/fmicb.2017.02055 (reimers2017theidentificationof pages 1-2) | Direct association; exact EET route not resolved. |
| Cable-bacterium e-SOx | alters | sulfur, iron, manganese, nitrogen, and phosphorus cycling | 2024 ecological synthesis; DOI 10.1016/j.ese.2023.100371 (wang2024electrogenicsulfuroxidation pages 2-3, wang2024electrogenicsulfuroxidation pages 3-3) | Use effect-specific primary studies before adding detailed geochemical edges. |
| Cable-bacterium e-SOx | suppresses | methane production/emission | Reported in 2024 synthesis; DOI 10.1016/j.ese.2023.100371 (wang2024electrogenicsulfuroxidation pages 2-3) | **Do not curate without the cited primary experiment and context.** |

## Recent developments, applications, and statistics

### 2024 developments

1. **Nickel physiology:** comparative analysis covered 38 cable-bacterium genomes, including six closed genomes, and identified adaptations in nickel importers, nickel-binding proteins, chaperones, and a distinctive RcnA exporter. This aligns genomic resource allocation with nickel-dependent conduction, but does not identify the complete fiber biosynthetic pathway (zhuang2024electrontransferin pages 6-8).
2. **Closed genomes:** a 2024 metagenomic workflow produced a 5.09-Mbp circular genome containing 1,109 newly identified genes, illustrating how incomplete assemblies had constrained mechanistic annotation.
3. **Electrode implementation:** +200 mV poised carbon electrodes enriched cable bacteria 490-fold relative to sediment and 640-fold relative to unpoised controls; measured currents were approximately 17–78 µA. This provides a practical route for electronic control, enrichment, and metabolism assays (bonne2024interactionofliving pages 1-2, bonne2024interactionofliving pages 2-5).
4. **Ecological synthesis:** recent reviews converge on cable bacteria as sediment ecosystem engineers that alter sulfur, iron, manganese, phosphorus, and nitrogen transformations and can suppress methanogenesis, while emphasizing that many molecular steps remain unresolved (wang2024electrogenicsulfuroxidation pages 2-3, wang2024electrogenicsulfuroxidation pages 3-3).

### Current and prospective applications

- **Bioelectrochemical cultivation and control:** poised electrodes can attract and enrich living filaments, potentially overcoming the lack of pure cultures and enabling controlled physiological experiments (bonne2024interactionofliving pages 1-2, bonne2024interactionofliving pages 2-5).
- **Benthic microbial fuel cells:** cable bacteria can colonize anodes and potentially deliver electrons from deeper sulfide-rich layers under anaerobic conditions (reimers2017theidentificationof pages 1-2).
- **Biosensing and bioremediation:** electrode attraction and redox activity suggest sensors for sulfide/redox conditions and treatment systems that exploit spatially separated donors and acceptors. These remain development-stage applications rather than established commercial implementations (bonne2024interactionofliving pages 1-2).
- **Biodegradable bioelectronics:** centimeter-scale protein conductors with conductivities up to 79 S cm⁻¹ motivate interconnect and transistor-channel concepts, but stability in air is a major engineering limitation (meysman2019ahighlyconductive pages 1-2).
- **Sediment management:** manipulation of cable-bacterium activity may immobilize or remobilize iron-bound phosphorus, remove sulfide, and influence methane. Outcomes are strongly sediment- and redox-dependent; “environmental protection” should not be encoded as a universal causal consequence (wang2024electrogenicsulfuroxidation pages 2-3, wang2024electrogenicsulfuroxidation pages 3-3).

## Expert assessment for TraitMech

The best-supported graph backbone is intentionally small:

**sulfide availability → anodic sulfur oxidation → electron injection into periplasmic fiber network → centimeter-scale electronic conduction → cathodic oxygen reduction**, with **intact filament continuity** as a necessary structural condition and **nickel-containing conductive cores** as a molecular requirement.

The direct experiments establish conduction, spatial coupling, oxygen dependence, and conductive-fiber localization much more firmly than they establish enzyme-level electron routing. Consequently, a robust YAML graph should distinguish:

- **observed phenotype/process edges** from
- **proposed molecular implementation edges**, and
- **universal trait components** from **taxon-, environment-, or assay-specific branches**.

The current 14-node/14-edge graph should be expanded only where this distinction can be represented. Adding numerous Dsr, cytochrome, nitrate, or ecological edges without evidence qualifiers would create false mechanistic precision.

## Warnings: claims not yet suitable for unqualified curation

1. **Do not identify c-type cytochromes as the conductive fibers.** Their redox states track electron flow, but direct proof that they are the main centimeter-scale carrier is lacking (wang2024electrogenicsulfuroxidation pages 3-3, wang2024electrogenicsulfuroxidation pages 2-3).
2. **Do not assign a universal terminal oxygen reductase.** Periplasmic cytochromes, terminal oxidases, and truncated hemoglobins have been proposed in different contexts; the conserved mechanism is unresolved (kjeldsen2019ontheevolution pages 1-1, hiralal2025anovelcable pages 10-13).
3. **Do not encode reverse Dsr as settled.** Genome content supports sulfur metabolism, but gene presence does not determine catalytic direction; label pathway direction as inferred (kjeldsen2019ontheevolution pages 1-1).
4. **Do not make nitrate/DNRA universal.** Retain organism and experimental context (wang2024electrogenicsulfuroxidation pages 2-3).
5. **Do not make elemental sulfur, thiosulfate, hydrogen, or sulfur disproportionation defining donors/processes.** These are groundwater- or strain-specific boundary cases.
6. **Do not infer exact nickel species or invent a cofactor CURIE.** Use a label-only NiBiD/sulfur-ligated nickel cofactor node pending authoritative ontology coverage.
7. **Do not equate electrode attraction with a proven sensory mechanism.** The voltage-dependent movement is direct, but its molecular basis is unknown (bonne2024interactionofliving pages 1-2).
8. **Do not curate methane suppression, phosphorus retention, metal mobilization, or remediation benefit as universal.** Retrieve and annotate the primary sediment-specific studies first (wang2024electrogenicsulfuroxidation pages 2-3, wang2024electrogenicsulfuroxidation pages 3-3).
9. **Pure-culture limitations matter.** Many results derive from enrichment cultures, single filaments, metagenomes, or sediment communities; contamination and community-level alternatives must remain visible in evidence metadata (kjeldsen2019ontheevolution pages 1-1, bonne2024interactionofliving pages 2-5).

## DOI-first bibliography

1. **Bjerg JT et al.** “Long-distance electron transport in individual, living cable bacteria.” *PNAS*. Published May 2018. DOI: [10.1073/pnas.1800367115](https://doi.org/10.1073/pnas.1800367115). Direct Raman/filament-interruption evidence (bjerg2018longdistanceelectrontransport pages 1-2).
2. **Meysman FJR et al.** “A highly conductive fibre network enables centimetre-scale electron transport in multicellular cable bacteria.” *Nature Communications*. Published September 2019. DOI: [10.1038/s41467-019-12115-7](https://doi.org/10.1038/s41467-019-12115-7). Direct electrical and structural characterization (meysman2019ahighlyconductive pages 1-2).
3. **Kjeldsen KU et al.** “On the evolution and physiology of cable bacteria.” *PNAS*. Published August 2019. DOI: [10.1073/pnas.1903514116](https://doi.org/10.1073/pnas.1903514116). Genomic, proteomic, and physiological model (kjeldsen2019ontheevolution pages 1-1).
4. **Wang Z et al.** “Electrogenic sulfur oxidation mediated by cable bacteria and its ecological effects.” *Environmental Science and Ecotechnology* 20:100371. Online 2023; issue July 2024. DOI: [10.1016/j.ese.2023.100371](https://doi.org/10.1016/j.ese.2023.100371). Current mechanistic/ecological review (wang2024electrogenicsulfuroxidation pages 2-3, wang2024electrogenicsulfuroxidation pages 3-3).
5. **Hiralal A et al.** “Comparative genomic analysis of nickel homeostasis in cable bacteria.” *BMC Genomics*. Published July 2024. DOI: [10.1186/s12864-024-10594-7](https://doi.org/10.1186/s12864-024-10594-7). Comparative genomics of nickel dependence (zhuang2024electrontransferin pages 6-8).
6. **Bonné R et al.** “Interaction of living cable bacteria with carbon electrodes in bioelectrochemical systems.” *Applied and Environmental Microbiology*. Published August 2024. DOI: [10.1128/aem.00795-24](https://doi.org/10.1128/aem.00795-24). Electrode attraction and EET assays (bonne2024interactionofliving pages 1-2, bonne2024interactionofliving pages 2-5).
7. **Zhuang X, Wang S, Wu S.** “Electron Transfer in the Biogeochemical Sulfur Cycle.” *Life*. Published May 2024. DOI: [10.3390/life14050591](https://doi.org/10.3390/life14050591). Recent broader review (zhuang2024electrontransferin pages 6-8).
8. **Reimers CE et al.** “The Identification of Cable Bacteria Attached to the Anode of a Benthic Microbial Fuel Cell.” *Frontiers in Microbiology*. Published October 2017. DOI: [10.3389/fmicb.2017.02055](https://doi.org/10.3389/fmicb.2017.02055) (reimers2017theidentificationof pages 1-2).

**Recommended curation priority:** first encode the direct filament-continuity, fiber-conduction, sulfide/oxygen spatial-coupling, and nickel-conductivity edges. Add reverse-Dsr, cytochrome-interface, nitrate/DNRA, electrode, and ecosystem-effect branches only with explicit `proposed`, `taxon_specific`, `assay_specific`, or `uncertain` qualifiers.

References

1. (bjerg2018longdistanceelectrontransport pages 1-2): Jesper T. Bjerg, Henricus T. S. Boschker, Steffen Larsen, David Berry, Markus Schmid, Diego Millo, Paula Tataru, Filip J. R. Meysman, Michael Wagner, Lars Peter Nielsen, and Andreas Schramm. Long-distance electron transport in individual, living cable bacteria. Proceedings of the National Academy of Sciences, 115:5786-5791, May 2018. URL: https://doi.org/10.1073/pnas.1800367115, doi:10.1073/pnas.1800367115. This article has 187 citations and is from a highest quality peer-reviewed journal.

2. (kjeldsen2019ontheevolution pages 1-1): Kasper U. Kjeldsen, Lars Schreiber, Casper A. Thorup, Thomas Boesen, Jesper T. Bjerg, Tingting Yang, Morten S. Dueholm, Steffen Larsen, Nils Risgaard-Petersen, Marta Nierychlo, Markus Schmid, Andreas Bøggild, Jack van de Vossenberg, Jeanine S. Geelhoed, Filip J. R. Meysman, Michael Wagner, Per H. Nielsen, Lars Peter Nielsen, and Andreas Schramm. On the evolution and physiology of cable bacteria. Proceedings of the National Academy of Sciences, 116:19116-19125, Aug 2019. URL: https://doi.org/10.1073/pnas.1903514116, doi:10.1073/pnas.1903514116. This article has 216 citations and is from a highest quality peer-reviewed journal.

3. (wang2024electrogenicsulfuroxidation pages 2-3): Zhenyu Wang, Leonid Digel, Yongqiang Yuan, Hui Lu, Yonggang Yang, Carsten Vogt, Hans-Hermann Richnow, and Lars Peter Nielsen. Electrogenic sulfur oxidation mediated by cable bacteria and its ecological effects. Jul 2024. URL: https://doi.org/10.1016/j.ese.2023.100371, doi:10.1016/j.ese.2023.100371. This article has 13 citations.

4. (bonne2024interactionofliving pages 1-2): Robin Bonné, Ian P. G. Marshall, Jesper J. Bjerg, Ugo Marzocchi, Jean Manca, Lars Peter Nielsen, and Kartik Aiyer. Interaction of living cable bacteria with carbon electrodes in bioelectrochemical systems. Aug 2024. URL: https://doi.org/10.1128/aem.00795-24, doi:10.1128/aem.00795-24. This article has 16 citations and is from a peer-reviewed journal.

5. (bonne2024interactionofliving pages 2-5): Robin Bonné, Ian P. G. Marshall, Jesper J. Bjerg, Ugo Marzocchi, Jean Manca, Lars Peter Nielsen, and Kartik Aiyer. Interaction of living cable bacteria with carbon electrodes in bioelectrochemical systems. Aug 2024. URL: https://doi.org/10.1128/aem.00795-24, doi:10.1128/aem.00795-24. This article has 16 citations and is from a peer-reviewed journal.

6. (meysman2019ahighlyconductive pages 1-2): Filip J. R. Meysman, Rob Cornelissen, Stanislav Trashin, Robin Bonné, Silvia Hidalgo Martinez, Jasper van der Veen, Carsten J. Blom, Cheryl Karman, Ji-Ling Hou, Raghavendran Thiruvallur Eachambadi, Jeanine S. Geelhoed, Karolien De Wael, Hubertus J. E. Beaumont, Bart Cleuren, Roland Valcke, Herre S. J. van der Zant, Henricus T. S. Boschker, and Jean V. Manca. A highly conductive fibre network enables centimetre-scale electron transport in multicellular cable bacteria. Nature Communications, Sep 2019. URL: https://doi.org/10.1038/s41467-019-12115-7, doi:10.1038/s41467-019-12115-7. This article has 194 citations and is from a highest quality peer-reviewed journal.

7. (wang2024electrogenicsulfuroxidation pages 3-3): Zhenyu Wang, Leonid Digel, Yongqiang Yuan, Hui Lu, Yonggang Yang, Carsten Vogt, Hans-Hermann Richnow, and Lars Peter Nielsen. Electrogenic sulfur oxidation mediated by cable bacteria and its ecological effects. Jul 2024. URL: https://doi.org/10.1016/j.ese.2023.100371, doi:10.1016/j.ese.2023.100371. This article has 13 citations.

8. (hiralal2025anovelcable pages 10-13): Anwar Hiralal, Philip Ley, Jesper R. van Dijk, Cheng Li, Dmitrii Pankratov, Jiji Alingapoyil Choyikutty, Galina Pankratova, Jeanine S. Geelhoed, Diana Vasquez-Cardenas, Clare E. Reimers, and Filip J. R. Meysman. A novel cable bacteria species with a distinct morphology and genomic potential. May 2025. URL: https://doi.org/10.1128/aem.02502-24, doi:10.1128/aem.02502-24. This article has 5 citations and is from a peer-reviewed journal.

9. (zhuang2024electrontransferin pages 6-8): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 25 citations.

10. (reimers2017theidentificationof pages 1-2): Clare E. Reimers, Cheng Li, Michael F. Graw, Paul S. Schrader, and Michael Wolf. The identification of cable bacteria attached to the anode of a benthic microbial fuel cell: evidence of long distance extracellular electron transport to electrodes. Frontiers in Microbiology, Oct 2017. URL: https://doi.org/10.3389/fmicb.2017.02055, doi:10.3389/fmicb.2017.02055. This article has 85 citations and is from a peer-reviewed journal.