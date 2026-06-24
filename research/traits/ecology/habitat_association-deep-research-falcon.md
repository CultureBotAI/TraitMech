---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T20:16:40.623914'
end_time: '2026-06-17T20:46:47.223177'
duration_seconds: 1806.6
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: habitat association
  trait_identifier: traitmech:000047
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: habitat_association
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An ecological classification of the primary environment or niche an
    organism inhabits (e.g. free-living vs host-associated; soil, rhizosphere, gut).
    Microbial taxa show biogeographic structure across such habitats.
  parent_traits: METPO:1000059
  synonyms: niche association
  evidence_summary: 'DOI:10.1038/nrmicro1341:  (Martiny et al., "Microbial biogeography",
    support habitat/niche as a structuring axis of microbial distribution; parent
    of the habitat sub-variants.) | DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing
    the unknown", supports environment-specific microbial community membership (e.g.
    the soil microbiome) underpinning habitat association.)'
  causal_graph_summary: 'habitat_association_biogeographic_structure: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** habitat association
- **METPO identifier:** traitmech:000047
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological classification of the primary environment or niche an organism inhabits (e.g. free-living vs host-associated; soil, rhizosphere, gut). Microbial taxa show biogeographic structure across such habitats.
- **Parent traits:** METPO:1000059
- **Synonyms:** niche association
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al., "Microbial biogeography", support habitat/niche as a structuring axis of microbial distribution; parent of the habitat sub-variants.) | DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", supports environment-specific microbial community membership (e.g. the soil microbiome) underpinning habitat association.)
- **Existing causal graph summary:** habitat_association_biogeographic_structure: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **habitat association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/habitat_association.yaml`.

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
- **Trait label:** habitat association
- **METPO identifier:** traitmech:000047
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological classification of the primary environment or niche an organism inhabits (e.g. free-living vs host-associated; soil, rhizosphere, gut). Microbial taxa show biogeographic structure across such habitats.
- **Parent traits:** METPO:1000059
- **Synonyms:** niche association
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al., "Microbial biogeography", support habitat/niche as a structuring axis of microbial distribution; parent of the habitat sub-variants.) | DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", supports environment-specific microbial community membership (e.g. the soil microbiome) underpinning habitat association.)
- **Existing causal graph summary:** habitat_association_biogeographic_structure: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **habitat association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/habitat_association.yaml`.

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


# Microbial TraitMech Curation Report: Habitat Association (traitmech:000047)

## Scope summary (TraitMech interpretation)
**Habitat association** is an ecological classification capturing the *consistent association of a microbial taxon (or population/strain) with a primary environment or microhabitat* (e.g., freshwater vs saline lakes, mucosa vs lumen, sediment vs water, skin vs oral cavity) as evidenced by non-random occurrence/abundance and community turnover across habitats. A foundational framing is microbial biogeography: the idea that microorganisms show spatial/habitat structure rather than being uniformly distributed, consistent with the Baas–Becking notion that **“the environment selects”** (martiny2006microbialbiogeographyputting pages 1-2, martiny2006microbialbiogeographyputting pages 8-9).

### What the trait includes
* **Habitat-type membership** (categorical): e.g., freshwater/brackish/saline lakes; Antarctic sponge microbiome vs non-Antarctic; surface organs and body sites; biofilm vs planktonic compartments. (feng2024functionaltraitsand pages 1-2, she2024definingthebiogeographical pages 4-7, manriquedelacuba2024evidenceofhabitat pages 1-2)
* **Microhabitat partitioning** (within-habitat): e.g., mucosa vs lumen; different GI regions; site-specific organ niches. (she2024definingthebiogeographical pages 4-7, she2024definingthebiogeographical pages 8-9)
* **Observed biogeographic structure**: compositional similarity decreasing with environmental dissimilarity and/or geographic distance, and measurable turnover (beta diversity) across habitats. (martiny2006microbialbiogeographyputting pages 5-6, martiny2006microbialbiogeographyputting pages 3-4)

### Boundary cases and distinctions from nearby traits
* **Habitat association vs dispersal limitation (historical/province effects):** Martiny et al. distinguish *habitat (“station” = contemporary abiotic+biotic conditions)* from *province* (historical legacies). Dispersal limitation can create spatial structure *independent of current habitat* and thus can confound habitat association if not separated analytically. (martiny2006microbialbiogeographyputting pages 1-2, martiny2006microbialbiogeographyputting pages 2-3)
* **Habitat association vs environmental preference (continuous tolerance/optima):** Environmental preference is defined as growth responses across gradients, including **growth optima and growth ranges** for factors like oxygen, pH, temperature, salinity; this is mechanistically upstream of habitat association but not identical to a categorical habitat label. (ramoneda2024leveraginggenomicinformation pages 1-2)
* **Habitat association vs niche breadth:** Niche breadth is the *range/number of habitats occupied* (generalist vs specialist). It can be computed from occurrence across habitat clusters and treated as a quantitative trait distinct from the habitat class itself. (hao2024cooperationshapesbacterial pages 24-28, sun2024assemblyprocessand pages 6-9)
* **Host association:** Host-associated habitats can be treated as a subset of habitat types, but mechanistically may reflect host factors/biotic interactions; the genome-based environmental-preference perspective explicitly focuses on physicochemical drivers and notes biotic interactions as outside its main scope. (ramoneda2024leveraginggenomicinformation pages 1-2, hao2024cooperationshapesbacterial pages 6-10)

## Current understanding (key concepts)
Microbial habitat association is typically explained by the combined action of:
1. **Environmental selection** (deterministic filtering by physicochemical conditions). (ning2024environmentalstressmediates pages 1-4, martiny2006microbialbiogeographyputting pages 1-2)
2. **Dispersal limitation** and historical contingencies that create provinces and distance effects. (martiny2006microbialbiogeographyputting pages 6-7, martiny2006microbialbiogeographyputting pages 1-2)
3. **Stochastic processes (drift)** and demographic randomness that can dominate at times, depending on stress level and system. (ning2024environmentalstressmediates pages 1-4, sun2024assemblyprocessand pages 6-9)
4. **Biotic interactions** (competition, predation, chemical communication), including specialized metabolites, that can drive local-scale site specificity even where dispersal limitation is weak. (chase2023biogeographicpatternsof pages 1-2)

## Recent developments (prioritizing 2023–2024)
### 1) Large-scale genome atlases link habitat classes to functional gene repertoires
A Tibetan Plateau lake microbiome atlas (169 samples from 54 lakes; 8,271 MAGs; salinity classes **freshwater <0.1%, brackish 0.1–3.5%, saline >3.5%**) connects lake habitat types to functional potential and stresses salinity as a major structuring factor. Freshwater microbiomes are enriched for genes involved in **recalcitrant carbon degradation, carbon fixation, and energy transformation**, whereas saline-lake microbiomes are enriched for **osmolyte transport/synthesis** and genes enabling **anaerobic metabolism**. (feng2024functionaltraitsand pages 1-2, feng2024functionaltraitsand pages 2-4)

### 2) Mechanistic gene systems associated with pH/salinity adaptation are being enumerated at scale
A genome-centric trait–environment study (East African lakes; pH 7.2–10.1; salinity 56–85,318 ppm) identifies explicit gene systems underlying alkaline/saline adaptation, including:
* **Mrp-type Na+:H+ antiporter (mrpABCDEFG)** and **CPA1 family cation:H+ antiporter** (cytoplasmic pH homeostasis). (ren2024microbialstrategiesof pages 11-15)
* Compatible-solute biosynthesis/uptake systems: **ectoine (asd, ectBC)**, **trehalose (otsAB, treP)**, **betaine (betB, cmo)**, and transporters **opuABC** and **proVWX**. (ren2024microbialstrategiesof pages 11-15)
It also proposes an **index of environmental adaptation (iEA)**, reporting significant relationships between the index and species niche optima. (ren2024microbialstrategiesof pages 15-20, ren2024microbialstrategiesof pages 11-15)

### 3) Assembly-process shifts under stress provide a causal framing for habitat-specific structuring
A Nature Microbiology 2024 study of contaminated groundwater frames assembly via Vellend’s processes and reports that stochastic processes average **>60%** of assembly, but **stochasticity decreases with increasing environmental stress**, while **selection** increases with stress; selection is associated with variables including **pH, cobalt, and molybdenum**. (ning2024environmentalstressmediates pages 1-4)

### 4) Microhabitat mapping across human “surface organs” quantifies habitat partitioning and functional differences
A Nature Communications 2024 atlas (1,608 samples, 53 sites, 7 surface organs; 9,473 ASVs) shows strong intra-body biogeography. It attributes low stomach diversity to **low pH limiting bacterial growth**, and demonstrates strong differentiation between **mucosal and luminal** microbiomes (P < 0.0001 in multiple organs) as well as organ-specific functional traits (e.g., **aerobic respiration in skin; pentose-phosphate/sugar catabolism in appendix/large intestine**). (she2024definingthebiogeographical pages 2-4, she2024definingthebiogeographical pages 4-7)
A representative alpha-diversity panel illustrating site-level variation is shown in Figure 2B. (she2024definingthebiogeographical media 3732d8b6)

### 5) Chemical ecology is increasingly incorporated into habitat association
In marine sediments, paired metagenomic-metabolomic analyses find strong **site-specific metabolome signatures** and high local variation in **biosynthetic potential**, supporting a role for specialized-metabolite gene content in fine-scale habitat structuring. (chase2023biogeographicpatternsof pages 1-2)

## Candidate nodes for `data/traits/ecology/habitat_association.yaml`
The following table is curation-oriented (mechanistic + ecological nodes), with suggested grounding where possible.

| Type | Node label | Description/role in habitat association | Suggested ontology grounding | Evidence source |
|---|---|---|---|---|
| Environmental factor | salinity | Major abiotic filter structuring microbial communities across aquatic habitats and lake types; linked to salt-adaptation traits and taxonomic turnover | ENVO:00002009 | (feng2024functionaltraitsand pages 1-2, ramoneda2024leveraginggenomicinformation pages 1-2, feng2024functionaltraitsand pages 2-4) |
| Environmental factor | pH | Contemporary environmental variable shaping habitat association and species pH optima; strong selector in soils, lakes, stomach, and groundwater | CHEBI:18490, GO:0006885 | (ning2024environmentalstressmediates pages 1-4, ramoneda2024leveraginggenomicinformation pages 1-2, she2024definingthebiogeographical pages 2-4, ren2024microbialstrategiesof pages 11-15) |
| Environmental factor | dissolved oxygen | Geochemical factor distinguishing habitats and linked to aerobic vs anaerobic functional differences | CHEBI:15379 | (feng2024functionaltraitsand pages 1-2, she2024definingthebiogeographical pages 4-7) |
| Environmental factor | dissolved organic carbon (DOC) | Resource gradient associated with lake-type metabolic differentiation and habitat-specific functions | CHEBI:unresolved | (feng2024functionaltraitsand pages 1-2) |
| Environmental factor | free ammonia (NH3) | Stressor driving community dissimilarity, reduced richness, and taxon-specific enrichment along aquatic gradients | CHEBI:16134 | (sun2024assemblyprocessand pages 6-9) |
| Environmental factor | cobalt | Environmental stressor associated with selective assembly in contaminated groundwater | CHEBI:27638 | (ning2024environmentalstressmediates pages 1-4) |
| Environmental factor | molybdenum | Environmental stressor associated with selective assembly in contaminated groundwater | CHEBI:33363 | (ning2024environmentalstressmediates pages 1-4) |
| Habitat/microhabitat | mucosa | Host-associated surface microhabitat with distinct community composition and functions relative to lumen | ENVO:01000162 | (she2024definingthebiogeographical pages 4-7, she2024definingthebiogeographical pages 1-2, she2024definingthebiogeographical pages 8-9) |
| Habitat/microhabitat | lumen | Intra-organ microhabitat differing from mucosa in community composition and functional traits | UBERON:0013684 | (she2024definingthebiogeographical pages 4-7, she2024definingthebiogeographical pages 1-2, she2024definingthebiogeographical pages 8-9) |
| Habitat/microhabitat | habitat clusters | Operationally defined groups of related habitats used to annotate species habitat association from occurrence data | unresolved | (hao2024cooperationshapesbacterial pages 24-28, hao2024cooperationshapesbacterial pages 4-6) |
| Community/assembly process | selection | Deterministic assembly process by which environmental stressors and habitat conditions favor adapted taxa | GO:0044403 | (ning2024environmentalstressmediates pages 1-4, martiny2006microbialbiogeographyputting pages 1-2, martiny2006microbialbiogeographyputting pages 5-6) |
| Community/assembly process | dispersal limitation | Historical/spatial process generating habitat-associated biogeographic structure independent of local conditions | GO:0008150 | (ning2024environmentalstressmediates pages 1-4, martiny2006microbialbiogeographyputting pages 5-6, martiny2006microbialbiogeographyputting pages 1-2) |
| Community/assembly process | drift | Stochastic demographic process contributing to community assembly and habitat-associated turnover | GO:0008150 | (sun2024assemblyprocessand pages 6-9, ning2024environmentalstressmediates pages 1-4, martiny2006microbialbiogeographyputting pages 5-6) |
| Genomic feature | osmolyte transport/synthesis genes | Salt-adaptation gene repertoire enriched in saline habitats; supports persistence in high-salinity environments | GO:0015849, GO:1901653 | (feng2024functionaltraitsand pages 1-2) |
| Genomic feature | cooperation genes | Genomic correlates of broader habitat occupancy; higher proportion linked to generalist niche breadth | GO:0044419 | (hao2024cooperationshapesbacterial pages 21-24, hao2024cooperationshapesbacterial pages 6-10) |
| Genomic feature | biosynthetic gene clusters (BGCs) | Genomic potential for specialized metabolite production associated with site-specific biogeographic patterns | MIBiG:unresolved | (chase2023biogeographicpatternsof pages 1-2) |
| Gene/protein system | Mrp-type Na+/H+ antiporter (mrpABCDEFG) | Explicit alkaline/salinity adaptation system supporting cytoplasmic pH homeostasis | GO:0015385 | (ren2024microbialstrategiesof pages 11-15) |
| Gene/protein system | CPA1 family cation:H+ antiporter | Antiporter system implicated in pH homeostasis under alkaline/saline stress | GO:0015299 | (ren2024microbialstrategiesof pages 11-15) |
| Gene/protein system | ectoine biosynthesis genes (asd, ectBC) | Compatible-solute biosynthesis genes supporting osmotic stress tolerance and alkaline adaptation | KEGG:unresolved | (ren2024microbialstrategiesof pages 11-15) |
| Gene/protein system | trehalose genes (otsAB, treP) | Trehalose synthesis/processing genes implicated in compatible-solute accumulation and stress tolerance | KEGG:unresolved | (ren2024microbialstrategiesof pages 11-15) |
| Gene/protein system | betaine genes (betB, cmo) | Betaine-related osmoprotection genes associated with adaptation to alkaline/saline environments | KEGG:unresolved | (ren2024microbialstrategiesof pages 11-15) |
| Gene/protein system | opuABC transporter | ABC transporter for osmoprotectant uptake; explicit compatible-solute accumulation system | GO:0015419 | (ren2024microbialstrategiesof pages 11-15) |
| Gene/protein system | proVWX transporter | Glycine betaine/proline ABC transport system supporting osmotic stress tolerance | GO:0015419 | (ren2024microbialstrategiesof pages 11-15) |
| Gene/protein system | heat shock proteins | Stress-response proteins enriched in CPR adapted to brackish-saline groundwater | GO:0009408 | (wang2024adaptionmechanismand pages 1-2) |
| Metabolic pathway/module | anaerobic metabolism | Functional capacity enriched in saline lakes and linked to lower-oxygen habitats | GO:0009061 | (feng2024functionaltraitsand pages 1-2) |
| Metabolic pathway/module | carbon fixation | Functional capacity enriched in freshwater lake microbiomes and associated with habitat type | GO:0015977 | (feng2024functionaltraitsand pages 1-2) |
| Metabolic pathway/module | recalcitrant carbon degradation | Functional capacity enriched in freshwater habitats; indicates substrate-specific habitat specialization | GO:0019538 | (feng2024functionaltraitsand pages 1-2) |
| Metabolic pathway/module | sulfur reduction | Redox metabolism associated with adaptation to saline/groundwater habitats, especially CPR taxa | GO:0019419 | (wang2024adaptionmechanismand pages 1-2) |
| Metabolic pathway/module | denitrification | Nitrogen-cycle metabolism reported in CPR and deeper/permafrost or saline-associated systems | GO:0055114 | (wang2024adaptionmechanismand pages 1-2) |
| Metabolic pathway/module | specialized metabolite biosynthesis | Metabolic output linked to local site-specific biogeographic structure and biotic interactions | GO:0044550 | (chase2023biogeographicpatternsof pages 1-2) |
| Interaction/biotic factor | host metabolic dependency | CPR reliance on host/partner-derived amino acids, vitamins, and nucleotides can constrain habitat occupancy | GO:0044403 | (wang2024adaptionmechanismand pages 1-2) |
| Interaction/biotic factor | co-occurring partner taxa / metabolic support | Partner interactions provide resource exchange and may enable persistence in stressful habitats | GO:0044419 | (wang2024adaptionmechanismand pages 1-2) |
| Quantitative metric/index | iEA adaptation index | Composite KO-based index quantifying adaptive capacity and correlating with species niche optima across gradients | unresolved | (ren2024microbialstrategiesof pages 1-7, ren2024microbialstrategiesof pages 15-20, ren2024microbialstrategiesof pages 11-15, ren2024microbialstrategiesof pages 7-11) |
| Quantitative metric/index | Levins niche breadth index | Quantifies breadth of habitat occupancy; distinguishes generalists from specialists | unresolved | (sun2024assemblyprocessand pages 6-9) |


*Table: This table lists evidence-backed candidate nodes for a TraitMech causal graph of microbial habitat association, organized by node type and grounded to available ontologies where possible. It is useful for curation because it separates environmental drivers, mechanistic gene systems, pathways, assembly processes, and quantitative indices that have explicit support in the retrieved literature.*

## Candidate causal edges (triples) with evidence
The following table proposes causal edges suitable for TraitMech curation; edges marked as inferred/correlative or preprint-based should be treated cautiously.

| Subject node | Predicate | Object node | Evidence snippet | Reference | Notes/uncertainty |
|---|---|---|---|---|---|
| habitat type / environment | structures | microbial community composition | “free-living microbial taxa exhibit biogeographic patterns” and “the environment selects” for spatial variation in diversity | DOI:10.1038/nrmicro1341 (martiny2006microbialbiogeographyputting pages 1-2) | Foundational, broad review; high-level edge suitable as parent relation |
| salinity | structures | aquatic microbial community composition | Tibetan lake microbiomes were “primarily regulated by salinity”; saline vs freshwater lakes showed distinct taxonomic and functional profiles | DOI:10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2) | Strong system-level evidence; lake-specific but broadly relevant |
| salinity | enriches | osmolyte transport and synthesis genes | Saline-lake microbiomes “possess more genes that encode osmolyte transport and synthesis” | DOI:10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2) | Pathway-category level, not specific genes |
| osmolyte transport and synthesis genes | increases | saline habitat association | Enrichment of osmolyte transport/synthesis genes “match[es] well with the geochemical properties… including… salinity” distinguishing saline lakes | DOI:10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2) | Inferred edge from enrichment in saline habitats |
| salinity | increases | anaerobic metabolism genes | Saline-lake microbiomes “possess more genes that… enable anaerobic metabolism” | DOI:10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2) | Functional-category level |
| dissolved oxygen | correlates_with | anaerobic metabolism gene enrichment | Metabolic differences including anaerobic metabolism “match well with… dissolved oxygen” differences among lakes | DOI:10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2) | Correlative, not direct manipulation |
| dissolved organic carbon | correlates_with | recalcitrant carbon degradation genes | Freshwater microbiomes were enriched in recalcitrant carbon degradation genes, and these features “match well with… dissolved organic carbon” | DOI:10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2) | Correlative habitat-level edge |
| freshwater habitat | enriches | carbon fixation genes | Freshwater lake microbiomes are “enriched with genes involved in… carbon fixation” | DOI:10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2) | Habitat-category level |
| freshwater habitat | enriches | recalcitrant carbon degradation genes | Freshwater lake microbiomes are “enriched with genes involved in recalcitrant carbon degradation” | DOI:10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2) | Habitat-category level |
| pH | selects_for | Mrp-type Na+/H+ antiporter (mrpABCDEFG) | pH-associated adaptation traits explicitly include “Mrp-type Na+:H+ antiporter (mrpABCDEFG)” under “cytoplasmic pH homeostasis” | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 11-15) | Preprint; strong mechanistic specificity |
| pH | selects_for | CPA1 family cation:H+ antiporter | pH-associated traits include “a monovalent cation:H+ antiporter of the CPA1 family” | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 11-15) | Preprint |
| Mrp-type Na+/H+ antiporter (mrpABCDEFG) | increases | alkaline preference | Traits supporting “cytoplasmic pH homeostasis” were identified as important for adaptation to alkalinity; iEA correlated with species pH optima | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 1-7, ren2024microbialstrategiesof pages 11-15) | Mechanistic but generalized from trait class; preprint |
| CPA1 family cation:H+ antiporter | increases | alkaline preference | Antiporters were among pH-associated traits linked to species-level adaptation index and pH optima | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 1-7, ren2024microbialstrategiesof pages 11-15) | Mechanistic but inferred from association; preprint |
| alkaline/saline stress | increases | ectoine biosynthesis genes (asd, ectBC) | Compatible-solute genes explicitly named include “ectoine biosynthesis (asd, ectBC)” | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 11-15) | Preprint; trait-level adaptation gene set |
| alkaline/saline stress | increases | trehalose genes (otsAB, treP) | Named compatible-solute genes include “trehalose biosynthesis/processing (otsAB, treP)” | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 11-15) | Preprint |
| alkaline/saline stress | increases | betaine genes (betB, cmo) | Named compatible-solute genes include “betaine biosynthesis (betB, cmo)” | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 11-15) | Preprint |
| alkaline/saline stress | increases | opuABC transporter | pH/salinity-associated compatible-solute systems explicitly include “transporters opuABC” | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 11-15) | Preprint |
| alkaline/saline stress | increases | proVWX transporter | pH/salinity-associated systems explicitly include “proVWX (osmoprotectant and glycine betaine/proline ABC transport systems)” | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 11-15) | Preprint |
| environmental stress | decreases | drift contribution to community assembly | In groundwater, stochastic processes accounted for >60% on average, but “their relative importance decreased with increasing environmental stress”; drift showed negative correlation with stress | DOI:10.1038/s41564-023-01573-x (ning2024environmentalstressmediates pages 1-4) | Community-assembly edge, not gene-level |
| environmental stress | decreases | dispersal limitation contribution to community assembly | In groundwater, “dispersal limitation… showed negative correlations with stress” | DOI:10.1038/s41564-023-01573-x (ning2024environmentalstressmediates pages 1-4) | Community-assembly edge |
| environmental stress | increases | selection contribution to community assembly | In groundwater, “selection producing more dissimilar communities increased with stress” | DOI:10.1038/s41564-023-01573-x (ning2024environmentalstressmediates pages 1-4) | Strong recent evidence |
| free ammonia (NH3) | decreases | community richness | Under higher NH3, “community Richness and Phylogenetic Distance” decreased significantly | DOI:10.1128/spectrum.01051-24 (sun2024assemblyprocessand pages 6-9) | Aquatic system; pollutant-stressor context |
| free ammonia (NH3) | increases | community dissimilarity | “Bray–Curtis dissimilarity increased with NH3 distance” and higher NH3 caused “increased community dissimilarity” | DOI:10.1128/spectrum.01051-24 (sun2024assemblyprocessand pages 6-9) | Strong quantitative ecological evidence |
| NH3 | selects_for | Actinobacteriaota | “Actinobacteriaota exhibited a very significant increase with the rise of NH3 (P < 0.01)” | DOI:10.1128/spectrum.01051-24 (sun2024assemblyprocessand pages 6-9) | Taxon-specific edge; not universal |
| mucosa | differentiates | lumen community composition | Paired samples showed mucosal communities were significantly different from luminal communities in stomach, small intestine and large intestine (P < 0.0001) | DOI:10.1038/s41467-024-44720-6 (she2024definingthebiogeographical pages 4-7) | Strong host-microhabitat evidence |
| skin habitat | enriches | aerobic respiration functions | Organ-specific functional traits included “aerobic respiration in skin” | DOI:10.1038/s41467-024-44720-6 (she2024definingthebiogeographical pages 4-7) | Host-associated, organ-specific |
| oral cavity habitat | enriches | nucleoside/nucleotide biosynthesis | Organ-specific functional traits included “nucleoside/nucleotide biosynthesis in oral cavity” | DOI:10.1038/s41467-024-44720-6 (she2024definingthebiogeographical pages 4-7) | Host-associated, organ-specific |
| appendix / large intestine habitat | enriches | pentose-phosphate and sugar catabolism | Functional traits differed by organ, with “pentose-phosphate and sugar catabolism in appendix and large intestine” | DOI:10.1038/s41467-024-44720-6 (she2024definingthebiogeographical pages 4-7) | Host-associated, organ-specific |
| biosynthetic gene clusters (BGCs) | correlates_with | site-specific metabolomes | The study found “high variation in biosynthetic potential… reflected uncharacterized chemical space associated with site-specific metabolomes” | DOI:10.1038/s41396-023-01410-3 (chase2023biogeographicpatternsof pages 1-2) | Local marine sediment system |
| site-specific metabolomes | structures | beta diversity / biogeographic patterns | “Biogeographic patterns were driven by local scale processes… high variation in biosynthetic potential… reflected… site-specific metabolomes” | DOI:10.1038/s41396-023-01410-3 (chase2023biogeographicpatternsof pages 1-2) | Edge links chemistry to local beta diversity; somewhat interpretive |
| cooperation genes | increases | niche breadth / habitat generalism | “a positive correlation between the proportion of genes for cooperation and niche breadth”; decreased cooperation “promotes niche contraction” | DOI:10.1101/2024.10.05.616009 (hao2024cooperationshapesbacterial pages 21-24, hao2024cooperationshapesbacterial pages 6-10) | Preprint; broad phylogenetic analysis |
| heat shock proteins | increases | brackish-saline groundwater association | CPR adaptation to high salinity was attributed to “abundant genes associated with heat shock proteins, osmoprotectants, and sulfur reduction” | DOI:10.1038/s41522-024-00615-4 (wang2024adaptionmechanismand pages 1-2) | Trait-level, CPR-focused |
| sulfur reduction | increases | brackish-saline groundwater association | CPR adaptation to high salinity was attributed partly to genes for “sulfur reduction” | DOI:10.1038/s41522-024-00615-4 (wang2024adaptionmechanismand pages 1-2) | CPR-specific; habitat-specific inference |
| host metabolic dependency | constrains | habitat occupancy | CPR have small genomes and rely on extracting “amino acids, vitamins, and nucleotides” from hosts, implying dependency-linked habitat constraints | DOI:10.1038/s41522-024-00615-4 (wang2024adaptionmechanismand pages 1-2) | Inferred ecological edge from metabolic dependency |
| iEA adaptation index | correlates_with | species pH optima | The adaptation index of pH showed “consistently significant positive relationships with species pH optima” | DOI:10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 1-7, ren2024microbialstrategiesof pages 15-20) | Quantitative index, not direct mechanism; preprint |


*Table: This table lists evidence-backed candidate causal edges for curating a TraitMech graph of microbial habitat association. It links environmental factors, microhabitats, genomic systems, pathways, and assembly processes to habitat-structured community patterns, with DOI-first references and uncertainty notes.*

## Statistics and quantitative findings from recent studies
* **Human surface-organ atlas:** 1,608 samples from 53 sites across 7 organs; 9,473 ASVs; mucosa vs lumen differences significant (P < 0.0001) in stomach, small intestine, large intestine. (she2024definingthebiogeographical pages 1-2, she2024definingthebiogeographical pages 4-7)
* **Tibetan lake genome atlas:** 169 lake-water samples from 54 lakes; 8,271 MAGs; salinity thresholds for lake types: <0.1%, 0.1–3.5%, >3.5%; 617 high-quality MAGs (>90% completeness, <5% contamination) and 7,654 medium-quality MAGs (>50% completeness, <10% contamination). (feng2024functionaltraitsand pages 2-4)
* **Groundwater stress/assembly:** stochastic processes >60% on average; increased stress decreases drift and dispersal limitation while increasing selection (variables include pH, cobalt, molybdenum). (ning2024environmentalstressmediates pages 1-4)
* **NH3 gradient (aquatic):** quantified assembly contributions (drift 49.5%, dispersal limitation 35.0%, homogeneous selection 13.1%, heterogeneous selection 2.1% for total community) and demonstrated NH3-driven decreases in richness/phylogenetic distance and increased Bray–Curtis dissimilarity. (sun2024assemblyprocessand pages 6-9)
* **Trait–environment (pH) gene counts:** pH-related gene counts per genome range 10–391 (median 137; 5.32% of coding genes); iEA values observed −0.648 to 0.721; water vs sediment means 0.144 ± 0.301 vs 0.375 ± 0.184 (Wilcoxon p = 1.47e−22). (ren2024microbialstrategiesof pages 11-15)

## Current applications and real-world implementations
### Predictive ecology, cultivation, and microbiome engineering
A 2024 ISME Journal perspective argues that genome-informed inference of environmental preferences can:
* improve **cultivation success** by predicting growth-optimal conditions,
* inform design of **probiotic consortia** tailored to gut physicochemical conditions,
* improve persistence/effectiveness of **agricultural inoculants**, and
* enhance predictions of distribution shifts under global change (e.g., salinization). (ramoneda2024leveraginggenomicinformation pages 1-2)

### Source tracking / provenance and monitoring
A 2024 review summarizes ML-based microbial provenance efforts with reported performance: **city-level classification accuracy 85–89%** and **continental-level accuracy 90–94%** in a geospatial provenance implementation. (kumar2024acomprehensiveoverview pages 7-8)

### Disease/ecosystem classification using habitat-associated signatures
The same review summarizes large-scale meta-analyses and health indices that operationalize habitat- and host-state-associated community structure, including **GMHI built from 4,347 stool metagenomes** and multiple published meta-analyses (e.g., 2,424 datasets; 28 case-control 16S datasets across 10 disease states). (kumar2024acomprehensiveoverview pages 7-8)

## Expert synthesis (authoritative viewpoints)
* **Microbial biogeography framework:** Martiny et al. emphasize that observed habitat-associated patterns can arise from both contemporary environmental selection and historical/dispersal effects; rigorous sampling and methods (e.g., Mantel/partial Mantel tests) are needed to partition these influences. (martiny2006microbialbiogeographyputting pages 5-6, martiny2006microbialbiogeographyputting pages 3-4)
* **Genome-to-preference gap:** Ramoneda & Fierer emphasize that genomic data now exist for many uncultivated taxa, but environmental preference data remain sparse; integrating cultivation-independent genomic prediction with validation is a key direction to generalize habitat association mechanistically. (ramoneda2024leveraginggenomicinformation pages 1-2)

## Warnings / curation cautions
1. **Correlation vs causation:** Many habitat associations are inferred from compositional correlations with environmental gradients (e.g., DO/DOC/salinity; NH3), not direct manipulations; treat edges as “correlates_with” or “associated_with” unless mechanistically demonstrated. (feng2024functionaltraitsand pages 1-2, sun2024assemblyprocessand pages 6-9)
2. **Preprint evidence:** Some of the most explicit gene-level links (antiporters/osmolyte systems; cooperation–niche breadth) are from bioRxiv preprints and should be flagged as provisional until peer review. (ren2024microbialstrategiesof pages 11-15, hao2024cooperationshapesbacterial pages 21-24)
3. **Taxon specificity:** CPR groundwater adaptation (heat shock proteins, sulfur reduction, osmoprotectants) may not generalize across all bacteria; curate with taxon constraints if used. (wang2024adaptionmechanismand pages 1-2)
4. **Host vs abiotic habitat effects:** Organ biogeography edges mix abiotic factors (pH, oxygen) and host-associated variables (mucin, bile salts); consider modeling host factors explicitly rather than attributing solely to “habitat.” (she2024definingthebiogeographical pages 8-9)
5. **Resolution dependence:** Microbial “species” definitions and marker choice can mask or exaggerate habitat specificity; this is a known interpretive issue in microbial biogeography. (martiny2006microbialbiogeographyputting pages 8-9, martiny2006microbialbiogeographyputting pages 5-6)

---

# DOI-first bibliography (with URLs and publication dates)

1. Martiny JBH, et al. **Microbial biogeography: putting microorganisms on the map**. *Nature Reviews Microbiology* (Feb 2006). DOI: **10.1038/nrmicro1341**. URL: https://doi.org/10.1038/nrmicro1341 (martiny2006microbialbiogeographyputting pages 1-2)
2. Chase AB, et al. **Biogeographic patterns of biosynthetic potential and specialized metabolites in marine sediments**. *The ISME Journal* (Apr 2023). DOI: **10.1038/s41396-023-01410-3**. URL: https://doi.org/10.1038/s41396-023-01410-3 (chase2023biogeographicpatternsof pages 1-2)
3. Ning D, et al. **Environmental stress mediates groundwater microbial community assembly**. *Nature Microbiology* (Jan 2024). DOI: **10.1038/s41564-023-01573-x**. URL: https://doi.org/10.1038/s41564-023-01573-x (ning2024environmentalstressmediates pages 1-4)
4. Ramoneda J, et al. **Leveraging genomic information to predict environmental preferences of bacteria**. *The ISME Journal* (Jan 2024). DOI: **10.1093/ismejo/wrae195**. URL: https://doi.org/10.1093/ismejo/wrae195 (ramoneda2024leveraginggenomicinformation pages 1-2)
5. She J-J, et al. **Defining the biogeographical map and potential bacterial translocation of microbiome in human ‘surface organs’**. *Nature Communications* (Jan 2024). DOI: **10.1038/s41467-024-44720-6**. URL: https://doi.org/10.1038/s41467-024-44720-6 (she2024definingthebiogeographical pages 1-2)
6. Baker JL, et al. **The oral microbiome: diversity, biogeography and human health**. *Nature Reviews Microbiology* (Sep 2024). DOI: **10.1038/s41579-023-00963-6**. URL: https://doi.org/10.1038/s41579-023-00963-6 (baker2024theoralmicrobiome pages 1-4)
7. Feng X, et al. **Functional traits and adaptation of lake microbiomes on the Tibetan Plateau**. *Microbiome* (Dec 2024). DOI: **10.1186/s40168-024-01979-7**. URL: https://doi.org/10.1186/s40168-024-01979-7 (feng2024functionaltraitsand pages 1-2)
8. Wang J, et al. **Adaption mechanism and ecological role of CPR bacteria in brackish-saline groundwater**. *NPJ Biofilms and Microbiomes* (Nov 2024). DOI: **10.1038/s41522-024-00615-4**. URL: https://doi.org/10.1038/s41522-024-00615-4 (wang2024adaptionmechanismand pages 1-2)
9. Manrique-de-la-Cuba MF, et al. **Evidence of habitat specificity in sponge microbiomes from Antarctica**. *Environmental Microbiome* (Dec 2024). DOI: **10.1186/s40793-024-00648-4**. URL: https://doi.org/10.1186/s40793-024-00648-4 (manriquedelacuba2024evidenceofhabitat pages 1-2)
10. Sun S, et al. **Assembly process and co-occurrence network of microbial community in response to free ammonia gradient distribution**. *Microbiology Spectrum* (Sep 2024). DOI: **10.1128/spectrum.01051-24**. URL: https://doi.org/10.1128/spectrum.01051-24 (sun2024assemblyprocessand pages 6-9)
11. Kumar B, et al. **A comprehensive overview of microbiome data in the light of machine learning applications: categorization, accessibility, and future directions**. *Frontiers in Microbiology* (Feb 2024). DOI: **10.3389/fmicb.2024.1343572**. URL: https://doi.org/10.3389/fmicb.2024.1343572 (kumar2024acomprehensiveoverview pages 7-8)

## Preprints (flagged)
12. Ren M, et al. **Microbial strategies of environmental adaptation revealed by trait-environmental relationships**. *bioRxiv* (Sep 2024). DOI: **10.1101/2024.09.17.613589**. URL: https://doi.org/10.1101/2024.09.17.613589 (ren2024microbialstrategiesof pages 11-15)
13. Hao C, et al. **Cooperation shapes bacterial niche breadth evolution and patterns of diversification**. *bioRxiv* (Oct 2024). DOI: **10.1101/2024.10.05.616009**. URL: https://doi.org/10.1101/2024.10.05.616009 (hao2024cooperationshapesbacterial pages 21-24)


References

1. (martiny2006microbialbiogeographyputting pages 1-2): Jennifer B. Hughes Martiny, Brendan J.M. Bohannan, James H. Brown, Robert K. Colwell, Jed A. Fuhrman, Jessica L. Green, M. Claire Horner-Devine, Matthew Kane, Jennifer Adams Krumins, Cheryl R. Kuske, Peter J. Morin, Shahid Naeem, Lise Øvreås, Anna-Louise Reysenbach, Val H. Smith, and James T. Staley. Microbial biogeography: putting microorganisms on the map. Nature Reviews Microbiology, 4:102-112, Feb 2006. URL: https://doi.org/10.1038/nrmicro1341, doi:10.1038/nrmicro1341. This article has 3351 citations and is from a highest quality peer-reviewed journal.

2. (martiny2006microbialbiogeographyputting pages 8-9): Jennifer B. Hughes Martiny, Brendan J.M. Bohannan, James H. Brown, Robert K. Colwell, Jed A. Fuhrman, Jessica L. Green, M. Claire Horner-Devine, Matthew Kane, Jennifer Adams Krumins, Cheryl R. Kuske, Peter J. Morin, Shahid Naeem, Lise Øvreås, Anna-Louise Reysenbach, Val H. Smith, and James T. Staley. Microbial biogeography: putting microorganisms on the map. Nature Reviews Microbiology, 4:102-112, Feb 2006. URL: https://doi.org/10.1038/nrmicro1341, doi:10.1038/nrmicro1341. This article has 3351 citations and is from a highest quality peer-reviewed journal.

3. (feng2024functionaltraitsand pages 1-2): Xiaoyuan Feng, Peng Xing, Ye Tao, Xiaojun Wang, Qinglong L. Wu, Yongqin Liu, and Haiwei Luo. Functional traits and adaptation of lake microbiomes on the tibetan plateau. Microbiome, Dec 2024. URL: https://doi.org/10.1186/s40168-024-01979-7, doi:10.1186/s40168-024-01979-7. This article has 13 citations and is from a highest quality peer-reviewed journal.

4. (she2024definingthebiogeographical pages 4-7): Jun-Jun She, Wei-Xin Liu, Xiao-Ming Ding, Gang Guo, Jing Han, Fei-Yu Shi, Harry Cheuk-Hay Lau, Chen-Guang Ding, Wu-Jun Xue, Wen Shi, Gai-Xia Liu, Zhe Zhang, Chen-Hao Hu, Yinnan Chen, Chi Chun Wong, and Jun Yu. Defining the biogeographical map and potential bacterial translocation of microbiome in human ‘surface organs’. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-024-44720-6, doi:10.1038/s41467-024-44720-6. This article has 73 citations and is from a highest quality peer-reviewed journal.

5. (manriquedelacuba2024evidenceofhabitat pages 1-2): Maria F. Manrique-de-la-Cuba, Génesis Parada-Pozo, Susana Rodríguez-Marconi, Marileyxis R. López-Rodríguez, Sebastián Abades, and Nicole Trefault. Evidence of habitat specificity in sponge microbiomes from antarctica. Environmental Microbiome, Dec 2024. URL: https://doi.org/10.1186/s40793-024-00648-4, doi:10.1186/s40793-024-00648-4. This article has 5 citations and is from a peer-reviewed journal.

6. (she2024definingthebiogeographical pages 8-9): Jun-Jun She, Wei-Xin Liu, Xiao-Ming Ding, Gang Guo, Jing Han, Fei-Yu Shi, Harry Cheuk-Hay Lau, Chen-Guang Ding, Wu-Jun Xue, Wen Shi, Gai-Xia Liu, Zhe Zhang, Chen-Hao Hu, Yinnan Chen, Chi Chun Wong, and Jun Yu. Defining the biogeographical map and potential bacterial translocation of microbiome in human ‘surface organs’. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-024-44720-6, doi:10.1038/s41467-024-44720-6. This article has 73 citations and is from a highest quality peer-reviewed journal.

7. (martiny2006microbialbiogeographyputting pages 5-6): Jennifer B. Hughes Martiny, Brendan J.M. Bohannan, James H. Brown, Robert K. Colwell, Jed A. Fuhrman, Jessica L. Green, M. Claire Horner-Devine, Matthew Kane, Jennifer Adams Krumins, Cheryl R. Kuske, Peter J. Morin, Shahid Naeem, Lise Øvreås, Anna-Louise Reysenbach, Val H. Smith, and James T. Staley. Microbial biogeography: putting microorganisms on the map. Nature Reviews Microbiology, 4:102-112, Feb 2006. URL: https://doi.org/10.1038/nrmicro1341, doi:10.1038/nrmicro1341. This article has 3351 citations and is from a highest quality peer-reviewed journal.

8. (martiny2006microbialbiogeographyputting pages 3-4): Jennifer B. Hughes Martiny, Brendan J.M. Bohannan, James H. Brown, Robert K. Colwell, Jed A. Fuhrman, Jessica L. Green, M. Claire Horner-Devine, Matthew Kane, Jennifer Adams Krumins, Cheryl R. Kuske, Peter J. Morin, Shahid Naeem, Lise Øvreås, Anna-Louise Reysenbach, Val H. Smith, and James T. Staley. Microbial biogeography: putting microorganisms on the map. Nature Reviews Microbiology, 4:102-112, Feb 2006. URL: https://doi.org/10.1038/nrmicro1341, doi:10.1038/nrmicro1341. This article has 3351 citations and is from a highest quality peer-reviewed journal.

9. (martiny2006microbialbiogeographyputting pages 2-3): Jennifer B. Hughes Martiny, Brendan J.M. Bohannan, James H. Brown, Robert K. Colwell, Jed A. Fuhrman, Jessica L. Green, M. Claire Horner-Devine, Matthew Kane, Jennifer Adams Krumins, Cheryl R. Kuske, Peter J. Morin, Shahid Naeem, Lise Øvreås, Anna-Louise Reysenbach, Val H. Smith, and James T. Staley. Microbial biogeography: putting microorganisms on the map. Nature Reviews Microbiology, 4:102-112, Feb 2006. URL: https://doi.org/10.1038/nrmicro1341, doi:10.1038/nrmicro1341. This article has 3351 citations and is from a highest quality peer-reviewed journal.

10. (ramoneda2024leveraginggenomicinformation pages 1-2): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 25 citations.

11. (hao2024cooperationshapesbacterial pages 24-28): Chunhui Hao, Naoki Konno, Makoto Ito, Laurence J. Belcher, Wataru Iwasaki, and Stuart A. West. Cooperation shapes bacterial niche breadth evolution and patterns of diversification. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.05.616009, doi:10.1101/2024.10.05.616009. This article has 3 citations.

12. (sun2024assemblyprocessand pages 6-9): Shengjie Sun, Zhiyi Qiao, Kexin Sun, and Da Huo. Assembly process and co-occurrence network of microbial community in response to free ammonia gradient distribution. Sep 2024. URL: https://doi.org/10.1128/spectrum.01051-24, doi:10.1128/spectrum.01051-24. This article has 16 citations and is from a domain leading peer-reviewed journal.

13. (hao2024cooperationshapesbacterial pages 6-10): Chunhui Hao, Naoki Konno, Makoto Ito, Laurence J. Belcher, Wataru Iwasaki, and Stuart A. West. Cooperation shapes bacterial niche breadth evolution and patterns of diversification. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.05.616009, doi:10.1101/2024.10.05.616009. This article has 3 citations.

14. (ning2024environmentalstressmediates pages 1-4): Daliang Ning, Yajiao Wang, Yupeng Fan, Jianjun Wang, Joy D. Van Nostrand, Liyou Wu, Ping Zhang, Daniel J. Curtis, Renmao Tian, Lauren Lui, Terry C. Hazen, Eric J. Alm, Matthew W. Fields, Farris Poole, Michael W. W. Adams, Romy Chakraborty, David A. Stahl, Paul D. Adams, Adam P. Arkin, Zhili He, and Jizhong Zhou. Environmental stress mediates groundwater microbial community assembly. Nature microbiology, 9:490-501, Jan 2024. URL: https://doi.org/10.1038/s41564-023-01573-x, doi:10.1038/s41564-023-01573-x. This article has 217 citations and is from a highest quality peer-reviewed journal.

15. (martiny2006microbialbiogeographyputting pages 6-7): Jennifer B. Hughes Martiny, Brendan J.M. Bohannan, James H. Brown, Robert K. Colwell, Jed A. Fuhrman, Jessica L. Green, M. Claire Horner-Devine, Matthew Kane, Jennifer Adams Krumins, Cheryl R. Kuske, Peter J. Morin, Shahid Naeem, Lise Øvreås, Anna-Louise Reysenbach, Val H. Smith, and James T. Staley. Microbial biogeography: putting microorganisms on the map. Nature Reviews Microbiology, 4:102-112, Feb 2006. URL: https://doi.org/10.1038/nrmicro1341, doi:10.1038/nrmicro1341. This article has 3351 citations and is from a highest quality peer-reviewed journal.

16. (chase2023biogeographicpatternsof pages 1-2): Alexander B Chase, Alexander Bogdanov, Alyssa M Demko, and Paul R Jensen. Biogeographic patterns of biosynthetic potential and specialized metabolites in marine sediments. The ISME Journal, 17:976-983, Apr 2023. URL: https://doi.org/10.1038/s41396-023-01410-3, doi:10.1038/s41396-023-01410-3. This article has 30 citations.

17. (feng2024functionaltraitsand pages 2-4): Xiaoyuan Feng, Peng Xing, Ye Tao, Xiaojun Wang, Qinglong L. Wu, Yongqin Liu, and Haiwei Luo. Functional traits and adaptation of lake microbiomes on the tibetan plateau. Microbiome, Dec 2024. URL: https://doi.org/10.1186/s40168-024-01979-7, doi:10.1186/s40168-024-01979-7. This article has 13 citations and is from a highest quality peer-reviewed journal.

18. (ren2024microbialstrategiesof pages 11-15): Minglei Ren, Ang Hu, Zhonghua Zhao, Xiaolong Yao, Ismael Aaron Kimirei, Lu Zhang, and Jianjun Wang. Microbial strategies of environmental adaptation revealed by trait-environmental relationships. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.17.613589, doi:10.1101/2024.09.17.613589. This article has 0 citations.

19. (ren2024microbialstrategiesof pages 15-20): Minglei Ren, Ang Hu, Zhonghua Zhao, Xiaolong Yao, Ismael Aaron Kimirei, Lu Zhang, and Jianjun Wang. Microbial strategies of environmental adaptation revealed by trait-environmental relationships. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.17.613589, doi:10.1101/2024.09.17.613589. This article has 0 citations.

20. (she2024definingthebiogeographical pages 2-4): Jun-Jun She, Wei-Xin Liu, Xiao-Ming Ding, Gang Guo, Jing Han, Fei-Yu Shi, Harry Cheuk-Hay Lau, Chen-Guang Ding, Wu-Jun Xue, Wen Shi, Gai-Xia Liu, Zhe Zhang, Chen-Hao Hu, Yinnan Chen, Chi Chun Wong, and Jun Yu. Defining the biogeographical map and potential bacterial translocation of microbiome in human ‘surface organs’. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-024-44720-6, doi:10.1038/s41467-024-44720-6. This article has 73 citations and is from a highest quality peer-reviewed journal.

21. (she2024definingthebiogeographical media 3732d8b6): Jun-Jun She, Wei-Xin Liu, Xiao-Ming Ding, Gang Guo, Jing Han, Fei-Yu Shi, Harry Cheuk-Hay Lau, Chen-Guang Ding, Wu-Jun Xue, Wen Shi, Gai-Xia Liu, Zhe Zhang, Chen-Hao Hu, Yinnan Chen, Chi Chun Wong, and Jun Yu. Defining the biogeographical map and potential bacterial translocation of microbiome in human ‘surface organs’. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-024-44720-6, doi:10.1038/s41467-024-44720-6. This article has 73 citations and is from a highest quality peer-reviewed journal.

22. (she2024definingthebiogeographical pages 1-2): Jun-Jun She, Wei-Xin Liu, Xiao-Ming Ding, Gang Guo, Jing Han, Fei-Yu Shi, Harry Cheuk-Hay Lau, Chen-Guang Ding, Wu-Jun Xue, Wen Shi, Gai-Xia Liu, Zhe Zhang, Chen-Hao Hu, Yinnan Chen, Chi Chun Wong, and Jun Yu. Defining the biogeographical map and potential bacterial translocation of microbiome in human ‘surface organs’. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-024-44720-6, doi:10.1038/s41467-024-44720-6. This article has 73 citations and is from a highest quality peer-reviewed journal.

23. (hao2024cooperationshapesbacterial pages 4-6): Chunhui Hao, Naoki Konno, Makoto Ito, Laurence J. Belcher, Wataru Iwasaki, and Stuart A. West. Cooperation shapes bacterial niche breadth evolution and patterns of diversification. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.05.616009, doi:10.1101/2024.10.05.616009. This article has 3 citations.

24. (hao2024cooperationshapesbacterial pages 21-24): Chunhui Hao, Naoki Konno, Makoto Ito, Laurence J. Belcher, Wataru Iwasaki, and Stuart A. West. Cooperation shapes bacterial niche breadth evolution and patterns of diversification. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.05.616009, doi:10.1101/2024.10.05.616009. This article has 3 citations.

25. (wang2024adaptionmechanismand pages 1-2): Jiawen Wang, Haohui Zhong, Qian Chen, and Jinren Ni. Adaption mechanism and ecological role of cpr bacteria in brackish-saline groundwater. NPJ Biofilms and Microbiomes, Nov 2024. URL: https://doi.org/10.1038/s41522-024-00615-4, doi:10.1038/s41522-024-00615-4. This article has 6 citations and is from a peer-reviewed journal.

26. (ren2024microbialstrategiesof pages 1-7): Minglei Ren, Ang Hu, Zhonghua Zhao, Xiaolong Yao, Ismael Aaron Kimirei, Lu Zhang, and Jianjun Wang. Microbial strategies of environmental adaptation revealed by trait-environmental relationships. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.17.613589, doi:10.1101/2024.09.17.613589. This article has 0 citations.

27. (ren2024microbialstrategiesof pages 7-11): Minglei Ren, Ang Hu, Zhonghua Zhao, Xiaolong Yao, Ismael Aaron Kimirei, Lu Zhang, and Jianjun Wang. Microbial strategies of environmental adaptation revealed by trait-environmental relationships. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.17.613589, doi:10.1101/2024.09.17.613589. This article has 0 citations.

28. (kumar2024acomprehensiveoverview pages 7-8): Bablu Kumar, Erika Lorusso, Bruno Fosso, and Graziano Pesole. A comprehensive overview of microbiome data in the light of machine learning applications: categorization, accessibility, and future directions. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1343572, doi:10.3389/fmicb.2024.1343572. This article has 96 citations and is from a peer-reviewed journal.

29. (baker2024theoralmicrobiome pages 1-4): Jonathon L. Baker, Jessica L. Mark Welch, Kathryn M. Kauffman, Jeffrey S. McLean, and Xuesong He. The oral microbiome: diversity, biogeography and human health. Nature reviews. Microbiology, 22:89-104, Sep 2024. URL: https://doi.org/10.1038/s41579-023-00963-6, doi:10.1038/s41579-023-00963-6. This article has 661 citations.