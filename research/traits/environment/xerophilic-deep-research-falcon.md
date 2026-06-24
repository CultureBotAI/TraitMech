---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:53:11.044587'
end_time: '2026-06-18T03:10:51.886638'
duration_seconds: 1060.84
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: xerophilic
  trait_identifier: traitmech:000011
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: xerophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental growth preference in which an organism grows at low
    water activity (low aw), such as in desiccated, high-sugar, or high-solute substrates.
  parent_traits: METPO:1000059
  synonyms: xerotolerant
  evidence_summary: 'DOI:10.1098/rstb.2004.1502: some of which are capable of growth
    at a water activity (aw) of 0.61, the lowest aw value for growth recorded to date
    (Low-water-activity review supports growth at very low aw as the defining feature
    of xerophiles.) | DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life
    without water) is predominantly described as the ability of some organisms to
    lose all or almost all water and enter a state of suspension where the metabolism
    comes to a reversible standstill (Anhydrobiosis review supports low-water-activity
    adaptation as the physiological context distinguishing xerophilic growth from
    desiccation survival.)'
  causal_graph_summary: 'xerophilic_low_water_activity_growth: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** xerophilic
- **METPO identifier:** traitmech:000011
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows at low water activity (low aw), such as in desiccated, high-sugar, or high-solute substrates.
- **Parent traits:** METPO:1000059
- **Synonyms:** xerotolerant
- **Existing evidence:** DOI:10.1098/rstb.2004.1502: some of which are capable of growth at a water activity (aw) of 0.61, the lowest aw value for growth recorded to date (Low-water-activity review supports growth at very low aw as the defining feature of xerophiles.) | DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without water) is predominantly described as the ability of some organisms to lose all or almost all water and enter a state of suspension where the metabolism comes to a reversible standstill (Anhydrobiosis review supports low-water-activity adaptation as the physiological context distinguishing xerophilic growth from desiccation survival.)
- **Existing causal graph summary:** xerophilic_low_water_activity_growth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **xerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/xerophilic.yaml`.

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
- **Trait label:** xerophilic
- **METPO identifier:** traitmech:000011
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental growth preference in which an organism grows at low water activity (low aw), such as in desiccated, high-sugar, or high-solute substrates.
- **Parent traits:** METPO:1000059
- **Synonyms:** xerotolerant
- **Existing evidence:** DOI:10.1098/rstb.2004.1502: some of which are capable of growth at a water activity (aw) of 0.61, the lowest aw value for growth recorded to date (Low-water-activity review supports growth at very low aw as the defining feature of xerophiles.) | DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without water) is predominantly described as the ability of some organisms to lose all or almost all water and enter a state of suspension where the metabolism comes to a reversible standstill (Anhydrobiosis review supports low-water-activity adaptation as the physiological context distinguishing xerophilic growth from desiccation survival.)
- **Existing causal graph summary:** xerophilic_low_water_activity_growth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **xerophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/xerophilic.yaml`.

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


## Microbial TraitMech Curation Report: **xerophilic** (METPO traitmech:000011)

**Target trait**: xerophilic (syn. xerotolerant; mapping status REVIEWED)

### Scope summary (what the trait represents)
**Xerophilic** should be curated as an *active growth/reproduction* phenotype under **low water activity (aw)**, not merely survival during drying. A recent Aspergillus-focused review defines xerophilic fungi as organisms that “tolerate and/or require reduced water activity,” and further states that xerophilic and xerotolerant species “tolerate or reproduce under low water activity values (aw < 0.85)”—explicitly tying the concept to reproduction/growth rather than dormancy. (pocsi2024biotechnologicalpotentialof pages 1-2)

**Key boundary distinctions**:
- **Xerophilic vs. xerotolerant**: In indoor mycology, fungi are grouped by moisture requirements (hydrophilic/mesophilic/xerophilic) with an *intermediate* “xerotolerant” category between mesophilic and xerophilic; this is a pragmatic classification for growth minima on surfaces/materials. (loukou2024dampbuildingsassociated pages 4-5, loukou2024dampbuildingsassociated media 56a4b8db)
- **Xerophilic vs. osmophilic/halophilic**: Osmophilic/osmotolerant taxa are linked to growth at high osmotic pressure (high solute, often sugar), while halophilic/halotolerant taxa are those that grow at high salt (typically NaCl). These states reduce effective aw but also introduce solute-specific chemistry (ionic toxicity, chaotropicity), so they should be treated as related-but-distinct environmental drivers or child traits rather than synonyms. (pocsi2024biotechnologicalpotentialof pages 1-2)
- **Xerophilic growth vs. desiccation tolerance/anhydrobiosis**: Anhydrobiosis is defined as the ability to enter “a state of reversible ametabolism or suspended metabolism due to cell desiccation,” and “desiccation tolerance is synonymous with anhydrobiosis” for vegetative cells—i.e., survival via metabolic suspension rather than growth. The same review emphasizes terminological ambiguity of “xerotolerance” across literatures (sometimes used as desiccation tolerance, partial dehydration tolerance, drought tolerance, or an umbrella term). For TraitMech, **xerophilic** should remain anchored to *growth at low aw*, and links to anhydrobiosis should be flagged as a nearby/related trait or contextual mechanism, not conflated. (grzyb2022introductiontobacterial pages 2-3)

### Current understanding & key quantitative limits (statistics/data)
**Water activity (aw) is the central physicochemical axis** for xerophily.

**Extreme lower bounds in fungi (recently summarized):**
- *Aspergillus penicillioides*: observed **cell division at aw = 0.585**, and a **theoretical germination minimum aw = 0.565** as summarized in Pócsi et al. 2024 (citing Stevenson et al.). (pocsi2024biotechnologicalpotentialof pages 1-2, pocsi2024biotechnologicalpotentialof pages 2-5)
- The same review adopts an operational cutoff of **0.80 aw** for xerophily (stricter than Pitt’s older 0.85), emphasizing curator-relevant thresholding choices. (pocsi2024biotechnologicalpotentialof pages 2-5)

**Built environment growth minima (species-specific):**
Loukou et al. 2024 emphasize that each fungus has minimum/maximum/optimum aw, with optima typically **0.90–0.99**, and that **aw ≈ 0.75** is often cited as a critical threshold for growth, though some species can grow near **aw ≈ 0.60**. Table 1 provides minimum aw ranges for representative building-associated taxa (image evidence). (loukou2024dampbuildingsassociated pages 4-5, loukou2024dampbuildingsassociated media 56a4b8db)

**Food/industrial context thresholds:**
A food-microbiology review states xerophilic molds and osmophilic yeasts can grow at very low aw and lists a “lower limit” for xerophilic molds at **aw 0.61** and osmophilic/xerophilic yeasts also at **aw 0.61**, contrasting with typical bacteria requiring much higher aw. (preetha2020factorsinfluencingthe pages 6-7)

### Recent developments & authoritative analyses (prioritizing 2023–2024)
#### 1) Solute chemistry matters beyond aw (chaotropicity as a boundary factor)
Pócsi et al. 2024 report that even for xerophiles, **glycerol-only** low-aw environments can become **chaotropic** and inhibit growth: **7.65 M glycerol** (aw = 0.644; reported chaotropic activity 20.88 kJ kg−1) “prevented mycelial growth.” This supports a curation warning that *aw alone* is insufficient to predict xerophilic growth; **solute identity and chaotropic/kosmotropic balance** should be explicit nodes/edges. (pocsi2024biotechnologicalpotentialof pages 2-5)

#### 2) Mechanistic repertoire in xerophilic/halophilic fungi
Across 2024 reviews, repeated mechanistic themes include:
- **Compatible solute production/accumulation** (e.g., glycerol, trehalose) and upregulation of glycerol-related enzymes/pathways. (pocsi2024biotechnologicalpotentialof pages 5-7)
- **Osmotic-stress signaling** (HOG pathway; HogA MAPK) described as part of adaptation in halophilic fungi and xerophilic/halophilic Aspergillus. (agrawal2024hiddentreasurehalophilic pages 1-2, pocsi2024biotechnologicalpotentialof pages 5-7)
- **Cell envelope remodeling** (cell wall strengthening/composition shifts; membrane composition/fluidity). (pocsi2024biotechnologicalpotentialof pages 5-7, agrawal2024hiddentreasurehalophilic pages 1-2)

#### 3) Built environment: standardized detection/inspection and aw-based grouping
Loukou et al. 2024 highlight a practical, real-world need: building inspections lack standardization, and fungal detection depends on **media water activity** and moisture history. They recommend using media spanning aw ranges (V8, MEA, DG18, MY40G/MY50G), and they emphasize that **time-of-wetness and wet–dry fluctuations** strongly influence contamination dynamics. (loukou2024dampbuildingsassociated pages 4-5)

### Current applications & real-world implementations
1) **Food spoilage and preservation**: Xerophilic Aspergilli can colonize low-aw processed foods and “spoil low/medium aw foods and produce mycotoxins,” motivating preservation technologies. (pocsi2024biotechnologicalpotentialof pages 11-12)

2) **Industrial biotechnology & environmental applications**: Xerophilic/salt-tolerant Aspergillus spp. are described as rich resources of salt-tolerant enzymes (e.g., hydrolases, oxidoreductases) and secondary metabolites, with applications including dye decolorization, xenobiotic degradation, and ion removal in high-salt environments. (pocsi2024biotechnologicalpotentialof pages 1-2)

3) **Built environment / indoor mycology**: aw-based fungal grouping and aw-specific media (DG18, MY40G/MY50G) are used to detect xerophilic and xerotolerant fungi on building materials; this is an implementation-relevant assay layer that should appear in the causal graph as “experimental/assay factors → observed growth.” (loukou2024dampbuildingsassociated pages 4-5, loukou2024dampbuildingsassociated media 56a4b8db)

### Candidate nodes (grouped; curation-ready)
| Category | Label | Node type | Brief description | Suggested ontology CURIE(s) | Key support |
|---|---|---|---|---|---|
| Trait/Phenotype | xerophilic growth | phenotype | Growth and reproduction at low water activity; recent review notes xerophilic/xerotolerant fungi tolerate or reproduce at aw < 0.85, with extreme cases much lower | METPO:traitmech:000011; label-only candidate for phenotype | (pocsi2024biotechnologicalpotentialof pages 1-2, loukou2024dampbuildingsassociated pages 4-5) |
| Trait/Phenotype | xerotolerant | phenotype | Intermediate/related phenotype between mesophilic and xerophilic fungi used in building-mycology classification | label-only candidate | (loukou2024dampbuildingsassociated pages 4-5) |
| Trait/Phenotype | halophilic | phenotype | Related but distinct trait requiring/tolerating high salt rather than low aw per se | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 1-2, agrawal2024hiddentreasurehalophilic pages 1-2) |
| Trait/Phenotype | osmophilic | phenotype | Related phenotype for growth in high-solute/high-osmotic-pressure media | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 1-2) |
| Environmental/Experimental factors | low water activity (aw) | environmental factor | Core physicochemical driver of trait; measure of free/available water for growth | label-only candidate | (raghavendra2026growthofmicroorganisms pages 1-2, loukou2024dampbuildingsassociated pages 4-5) |
| Environmental/Experimental factors | aw 0.75 threshold | experimental factor | Frequently cited critical threshold for fungal growth in buildings, though some fungi grow near 0.60 | label-only candidate | (loukou2024dampbuildingsassociated pages 4-5) |
| Environmental/Experimental factors | aw 0.585 | experimental factor | Observed cell-division limit for Aspergillus penicillioides in extreme xerophily studies summarized in 2024 review | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 2-5, pocsi2024biotechnologicalpotentialof pages 1-2) |
| Environmental/Experimental factors | theoretical germination minimum aw 0.565 | experimental factor | Theoretical minimum for A. penicillioides germination cited in 2024 review | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 2-5, pocsi2024biotechnologicalpotentialof pages 1-2) |
| Environmental/Experimental factors | high salinity / NaCl stress | environmental factor | Lowers aw and imposes osmotic and ionic stress; often overlaps with xerophily studies | CHEBI:26710 | (agrawal2024hiddentreasurehalophilic pages 1-2, pocsi2024biotechnologicalpotentialof pages 11-12) |
| Environmental/Experimental factors | high glycerol medium | experimental factor | Non-ionic low-aw medium used to test xerophilic growth; excessive glycerol-only media can be chaotropic and inhibitory | CHEBI:17754 | (pocsi2024biotechnologicalpotentialof pages 2-5, pocsi2024biotechnologicalpotentialof pages 11-12) |
| Environmental/Experimental factors | chaotropicity | environmental factor | Destabilizing solute property affecting growth at low aw; glycerol-only media can become too chaotropic | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 2-5, dijksterhuis2025fungalspoilageof pages 16-17, pocsi2024biotechnologicalpotentialof pages 1-2) |
| Environmental/Experimental factors | kosmotropic solutes | environmental factor | Solutes that stabilize macromolecular interactions; contrasted with chaotropes in low-aw growth studies | label-only candidate | (dijksterhuis2025fungalspoilageof pages 16-17, pocsi2024biotechnologicalpotentialof pages 1-2) |
| Environmental/Experimental factors | relative humidity | environmental factor | External humidity shapes surface water availability and fungal contamination dynamics | ENVO:01000203 | (loukou2024dampbuildingsassociated pages 4-5) |
| Environmental/Experimental factors | time-of-wetness / wet-dry fluctuation | experimental factor | Duration and fluctuation of moisture exposure strongly affect fungal growth in buildings | label-only candidate | (loukou2024dampbuildingsassociated pages 4-5) |
| Environmental/Experimental factors | saturated salt solution control | assay control | Standard method for creating fixed humidity / aw points in low-aw laboratory experiments | label-only candidate | (raghavendra2026growthofmicroorganisms pages 13-14) |
| Cellular processes | osmotic adjustment | biological process | Physiological adjustment to reduced water availability via solute accumulation and related responses | GO:0006970 | (dijksterhuis2025fungalspoilageof pages 16-17, agrawal2024hiddentreasurehalophilic pages 1-2) |
| Cellular processes | compatible solute accumulation | biological process | Intracellular build-up of osmoprotective small molecules under low aw/high salinity | GO:0015948 (candidate, osmotic stress response); label-only candidate | (preetha2020factorsinfluencingthe pages 6-7, pocsi2024biotechnologicalpotentialof pages 5-7, agrawal2024hiddentreasurehalophilic pages 1-2) |
| Cellular processes | extracellular compatible-solute secretion | biological process | Xerophiles can secrete polyols such as glycerol in addition to intracellular accumulation | label-only candidate | (dijksterhuis2025fungalspoilageof pages 16-17) |
| Cellular processes | modulation of membrane fluidity/composition | biological process | Halophilic/xerophilic fungi alter plasma membrane properties during low-aw/high-salt adaptation | GO:0006644 (candidate, phospholipid metabolic process); label-only candidate | (preetha2020factorsinfluencingthe pages 6-7, pocsi2024biotechnologicalpotentialof pages 5-7, agrawal2024hiddentreasurehalophilic pages 1-2) |
| Cellular processes | cell wall strengthening/remodeling | biological process | Increased chitin/alpha-glucan and wall restructuring support stress tolerance | GO:0071555 | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Cellular processes | extracellular polysaccharide production | biological process | Reported as part of adaptation repertoire in xerophilic/halophilic Aspergillus | GO:0033692 (candidate, cellular polysaccharide biosynthetic process) | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Cellular processes | ion/metabolite transport adjustment | biological process | Transport systems are adjusted during halophilic/xerophilic adaptation | GO:0006810 | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Pathways/Signaling | high osmolarity glycerol (HOG) pathway | signaling pathway | Canonical osmotic-stress signaling pathway highlighted in halophilic fungi review | label-only candidate | (agrawal2024hiddentreasurehalophilic pages 1-2) |
| Pathways/Signaling | HogA MAPK signaling | protein/pathway node | HogA MAPK explicitly cited as part of osmotic-stress signaling in xerophilic/halophilic Aspergillus | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Pathways/Signaling | glycerol biosynthesis pathway | metabolic pathway | Upregulated pathway supporting low-aw adaptation through glycerol production | MetaCyc/KEGG label-only candidate | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Metabolites/Compatible solutes | glycerol | metabolite | Major compatible solute/polyol; effective for osmotic adjustment and often secreted in xerophiles | CHEBI:17754 | (pocsi2024biotechnologicalpotentialof pages 5-7, dijksterhuis2025fungalspoilageof pages 16-17) |
| Metabolites/Compatible solutes | trehalose | metabolite | Compatible solute reported in xerophilic Aspergillus, though less effective than smaller polyols in saturated solutions | CHEBI:16588 | (pocsi2024biotechnologicalpotentialof pages 5-7, dijksterhuis2025fungalspoilageof pages 16-17) |
| Metabolites/Compatible solutes | erythritol | metabolite | Low-molecular-weight polyol reported as effective for osmotic adjustment | CHEBI:17113 | (dijksterhuis2025fungalspoilageof pages 16-17) |
| Metabolites/Compatible solutes | arabitol | metabolite | Low-molecular-weight polyol reported as effective for osmotic adjustment | CHEBI:17306 | (dijksterhuis2025fungalspoilageof pages 16-17) |
| Metabolites/Compatible solutes | mannitol | metabolite | Compatible solute discussed as less effective in saturated solutions because of relatively high aw | CHEBI:17138 | (dijksterhuis2025fungalspoilageof pages 16-17) |
| Metabolites/Compatible solutes | proline | metabolite | Bacterial compatible solute/osmolyte used under low aw/high salinity | CHEBI:17203 | (preetha2020factorsinfluencingthe pages 6-7) |
| Metabolites/Compatible solutes | glycine betaine | metabolite | Widely used bacterial osmoprotectant/compatible solute | CHEBI:17750 | (preetha2020factorsinfluencingthe pages 6-7) |
| Metabolites/Compatible solutes | carnitine | metabolite | Example bacterial compatible solute listed in food low-aw review | CHEBI:16347 | (preetha2020factorsinfluencingthe pages 6-7) |
| Cell structures | plasma membrane | cellular component | Target of adaptive fluidity/composition changes in halophilic fungi | GO:0005886 | (agrawal2024hiddentreasurehalophilic pages 1-2) |
| Cell structures | fungal cell wall | cellular component | Structural barrier remodeled in hypersaline/low-aw adaptation | GO:0005618 | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Cell structures | chitin | structural polymer | Cell wall component increased during adaptation in Aspergillus sydowii | CHEBI:27674 | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Cell structures | alpha-glucan | structural polymer | Added to cell wall in hypersaline adaptation, increasing stiffness/hydrophobicity | CHEBI:60196 (candidate, glucan) | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Genes/Proteins | HogA | gene/protein | MAP kinase implicated in osmotic-stress signaling of xerophilic/halophilic Aspergillus | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Genes/Proteins | glycerol-3-phosphate dehydrogenase | enzyme | Upregulated enzyme linked to glycerol production under low-aw stress | EC:1.1.1.8 | (pocsi2024biotechnologicalpotentialof pages 5-7) |
| Genes/Proteins | AgGlpF aquaglyceroporin | gene/protein | Aspergillus glpF homolog highlighted for heterologous transfer of stress tolerance | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 11-12) |
| Genes/Proteins | gfdB | gene | Aspergillus nidulans gene linked to oxidative stress and cell wall integrity defenses; transfer only partially affected osmophily | label-only candidate | (pocsi2024biotechnologicalpotentialof pages 11-12) |
| Taxon examples | Aspergillus penicillioides | taxon | Canonical extreme xerophile with experimentally summarized aw minima down to 0.585 | NCBITaxon:5457 | (pocsi2024biotechnologicalpotentialof pages 2-5, dijksterhuis2025fungalspoilageof pages 16-17, pocsi2024biotechnologicalpotentialof pages 1-2) |
| Taxon examples | Xeromyces bisporus | taxon | Extreme xerophile frequently cited with very low aw growth limits | NCBITaxon:183093 | (pocsi2024biotechnologicalpotentialof pages 2-5, dijksterhuis2025fungalspoilageof pages 16-17, pocsi2024biotechnologicalpotentialof pages 1-2) |
| Taxon examples | Aspergillus sydowii | taxon | Salt-tolerant/xerophilic Aspergillus with cell wall adaptation evidence | NCBITaxon:227321 | (pocsi2024biotechnologicalpotentialof pages 5-7, pocsi2024biotechnologicalpotentialof pages 2-5) |
| Taxon examples | Wallemia ichthyophaga | taxon | Model halophilic fungus cited as showing osmoadaptive traits relevant to low aw | NCBITaxon:495036 | (agrawal2024hiddentreasurehalophilic pages 1-2) |
| Taxon examples | Aspergillus wentii | taxon | Reported growth in concentrated glycerol media in xerophily review | NCBITaxon:5062 | (pocsi2024biotechnologicalpotentialof pages 2-5) |
| Assays/Media | DG18 | assay/media | Dichloran-glycerol agar recommended for detecting fungi at lower aw | label-only candidate | (loukou2024dampbuildingsassociated pages 4-5) |
| Assays/Media | MY40G / MY50G | assay/media | Very-low-aw media recommended for xerophilic fungi, especially archive materials | label-only candidate | (loukou2024dampbuildingsassociated pages 4-5) |
| Assays/Media | MEA | assay/media | Malt extract agar used across aw ranges for building-associated fungi surveys | label-only candidate | (loukou2024dampbuildingsassociated pages 4-5) |
| Assays/Media | V8 agar | assay/media | Higher-aw medium recommended as part of multi-media survey strategy | label-only candidate | (loukou2024dampbuildingsassociated pages 4-5) |


*Table: This table compiles curation-ready candidate nodes for a xerophilic TraitMech graph, grouped by biological and experimental category. It highlights phenotype boundaries, environmental drivers, mechanistic processes, metabolites, structures, genes, taxa, and assay media with suggested grounding and source support.*

### Candidate causal edges (triples) with evidence
| Theme | Subject | Predicate | Object | Evidence snippet quote | Reference | Citation IDs | Notes |
|---|---|---|---|---|---|---|---|
| Environmental driver → phenotype | low water activity (aw) | enables | xerophilic growth | "xerophilic/xerotolerant fungi as organisms that tolerate or reproduce at low water activity (aw < 0.85)" | Pócsi et al., 2024, DOI:10.1007/s00253-024-13338-5, https://doi.org/10.1007/s00253-024-13338-5 | (pocsi2024biotechnologicalpotentialof pages 1-2) | Scope/definition edge; broad review-level support. |
| Environmental driver → phenotype | aw = 0.585 | enables | cell division of *Aspergillus penicillioides* | "observed A. penicillioides cell-division at aw = 0.585" | Pócsi et al., 2024, DOI:10.1007/s00253-024-13338-5, https://doi.org/10.1007/s00253-024-13338-5 | (pocsi2024biotechnologicalpotentialof pages 1-2, pocsi2024biotechnologicalpotentialof pages 2-5) | Strong but taxon-specific; useful for extreme xerophile boundary. |
| Environmental driver → phenotype | theoretical germination minimum aw = 0.565 | enables | germination of *Aspergillus penicillioides* | "a theoretical germination minimum of aw = 0.565" | Pócsi et al., 2024, DOI:10.1007/s00253-024-13338-5, https://doi.org/10.1007/s00253-024-13338-5 | (pocsi2024biotechnologicalpotentialof pages 1-2, pocsi2024biotechnologicalpotentialof pages 2-5) | Theoretical/inferred rather than directly observed; mark uncertain. |
| Environmental driver → phenotype | high glycerol-only medium (7.65 M; aw 0.644) | decreases | mycelial growth | "glycerol-only media at 7.65 M (aw = 0.644; chaotropic activity 20.88 kJ kg−1) prevented mycelial growth" | Pócsi et al., 2024, DOI:10.1007/s00253-024-13338-5, https://doi.org/10.1007/s00253-024-13338-5 | (pocsi2024biotechnologicalpotentialof pages 2-5) | Assay-specific; suggests solute chemistry matters beyond aw alone. |
| Osmotic/chaotropic stress → compatible solutes | low aw | increases | compatible-solute accumulation | "microbes respond to low aw primarily via intracellular accumulation of compatible solutes (osmolytes)" | Preetha & Narayanan, 2020, DOI:10.34293/sijash.v7i3.473, https://doi.org/10.34293/sijash.v7i3.473 | (preetha2020factorsinfluencingthe pages 6-7) | Broad cross-microbial statement; good high-level causal edge. |
| Osmotic/chaotropic stress → compatible solutes | high osmolarity and ionic toxicity in hypersaline environments | causes | generation and accumulation of compatible solutes | "halophilic fungi employ physiological adaptations including altering plasma membrane fluidity, generating and accumulating compatible solutes" | Agrawal et al., 2024, DOI:10.3390/jof10040290, https://doi.org/10.3390/jof10040290 | (agrawal2024hiddentreasurehalophilic pages 1-2) | Related halophilic evidence; relevant because low aw often co-occurs with hypersalinity. |
| Compatible solutes/polyols → osmotic adjustment | glycerol, erythritol, and arabitol | enables | osmotic adjustment | "Polyols with lower molecular weight such as glycerol, erythritol, and arabitol were more effective for osmotic adjustment" | Dijksterhuis & Houbraken, 2025, DOI:10.1007/978-3-031-81904-9_3, https://doi.org/10.1007/978-3-031-81904-9_3 | (dijksterhuis2025fungalspoilageof pages 16-17) | Strong mechanistic edge for fungal polyols; review summarizing primary studies. |
| Compatible solutes/polyols → osmotic adjustment | glycerol secretion | increases | osmotic adjustment capacity | "The fungus produces and secretes copious amounts of glycerol" | Dijksterhuis & Houbraken, 2025, DOI:10.1007/978-3-031-81904-9_3, https://doi.org/10.1007/978-3-031-81904-9_3 | (dijksterhuis2025fungalspoilageof pages 16-17) | Taxon-specific in original studies; extracellular as well as intracellular role. |
| Compatible solutes/polyols → osmotic adjustment | mannitol and trehalose | decreases | effectiveness in saturated solutions | "mannitol and trehalose are less effective in saturated solutions because of their high water-activity values (0.978 and 0.970 at 25 °C)" | Dijksterhuis & Houbraken, 2025, DOI:10.1007/978-3-031-81904-9_3, https://doi.org/10.1007/978-3-031-81904-9_3 | (dijksterhuis2025fungalspoilageof pages 16-17) | Comparative mechanistic edge; context-dependent, not a general anti-xerophile claim. |
| Signaling → metabolic pathway | high osmolarity glycerol (HOG) pathway | increases | osmotic adaptation | "activating the high osmolarity glycerol (HOG) pathway" | Agrawal et al., 2024, DOI:10.3390/jof10040290, https://doi.org/10.3390/jof10040290 | (agrawal2024hiddentreasurehalophilic pages 1-2) | Pathway-level edge; halophilic fungi review, relevant but not exclusive to xerophiles. |
| Signaling → glycerol biosynthesis | HogA MAPK signaling | increases | glycerol biosynthesis pathway | "Mechanisms enabling xerophily/halophily include production of compatible solutes (glycerol, trehalose), upregulation of glycerol-3-phosphate dehydrogenase and glycerol biosynthesis pathways, HogA MAPK/osmotic stress signaling" | Pócsi et al., 2024, DOI:10.1007/s00253-024-13338-5, https://doi.org/10.1007/s00253-024-13338-5 | (pocsi2024biotechnologicalpotentialof pages 5-7) | Mechanistically plausible but bundled review statement; curate with moderate confidence. |
| Enzyme → metabolite | glycerol-3-phosphate dehydrogenase | increases | glycerol production | "upregulation of glycerol-3-phosphate dehydrogenase and glycerol biosynthesis pathways" | Pócsi et al., 2024, DOI:10.1007/s00253-024-13338-5, https://doi.org/10.1007/s00253-024-13338-5 | (pocsi2024biotechnologicalpotentialof pages 5-7) | Enzyme-level candidate; gene/protein grounding may require taxon-specific follow-up. |
| Low aw → membrane/cell wall remodeling | hypersaline/low-aw stress | increases | plasma membrane fluidity alteration | "halophilic fungi employ physiological adaptations including altering plasma membrane fluidity" | Agrawal et al., 2024, DOI:10.3390/jof10040290, https://doi.org/10.3390/jof10040290 | (agrawal2024hiddentreasurehalophilic pages 1-2) | Broad fungal adaptation edge; likely relevant across low-aw settings. |
| Low aw → membrane/cell wall remodeling | hypersaline conditions | increases | chitin biosynthesis | "When exposed to hypersaline conditions, A. sydowii enhances chitin biosynthesis" | Fernando et al., 2023, DOI:10.5281/zenodo.10001628, https://doi.org/10.5281/zenodo.10001628 | (pocsi2024biotechnologicalpotentialof pages 5-7) | Species-specific (*A. sydowii*); dataset/preprint-like evidence, use cautiously. |
| Cell wall remodeling → stress tolerance | alpha-glucan incorporation into cell wall | enables | adaptation to hypersaline and salt-deprived conditions | "incorporates α-glucan to create thick, stiff, and hydrophobic cell walls. Such structural rearrangements enable the fungus to adapt to both hypersaline and salt-deprived conditions" | Fernando et al., 2023, DOI:10.5281/zenodo.10001628, https://doi.org/10.5281/zenodo.10001628 | (pocsi2024biotechnologicalpotentialof pages 5-7) | Structural mechanism; species-specific and from dataset summary. |
| Assay/media → observed growth | DG18 and MY40G/MY50G media | used_to_measure | xerophilic fungal growth | "recommends media across aw ranges (V8, MEA, DG18, MY40G/MY50G) with very-low-aw media for archives" | Loukou et al., 2024, DOI:10.3390/jof10020108, https://doi.org/10.3390/jof10020108 | (loukou2024dampbuildingsassociated pages 4-5) | Assay edge; measures phenotype rather than mechanism. |
| RH/time-of-wetness → observed growth | time-of-wetness and wet–dry fluctuations | increases | contamination dynamics | "Time-of-wetness and wet–dry fluctuations strongly affect contamination dynamics" | Loukou et al., 2024, DOI:10.3390/jof10020108, https://doi.org/10.3390/jof10020108 | (loukou2024dampbuildingsassociated pages 4-5) | Built-environment observational edge; useful environmental modifier. |
| Application: food spoilage | xerophilic Aspergilli | causes | spoilage of low/medium-aw foods | "xerophilic Aspergilli can spoil low/medium aw foods and produce mycotoxins" | Pócsi et al., 2024, DOI:10.1007/s00253-024-13338-5, https://doi.org/10.1007/s00253-024-13338-5 | (pocsi2024biotechnologicalpotentialof pages 11-12) | Application edge; strong practical relevance for food preservation. |
| Application: biotechnology | salt-tolerant and xerophilic *Aspergillus* spp. | enables | production of salt-tolerant enzymes and biotechnological use | "production of diverse salt-tolerant enzymes (proteases, glycosidases, lipases, oxidoreductases), a reservoir of secondary metabolites, applications in dye decolorization, xenobiotic degradation, ion removal" | Pócsi et al., 2024, DOI:10.1007/s00253-024-13338-5, https://doi.org/10.1007/s00253-024-13338-5 | (pocsi2024biotechnologicalpotentialof pages 1-2) | Application edge; broad review summary rather than single mechanism. |


*Table: This table lists curation-ready subject–predicate–object edges for a xerophilic TraitMech graph, with verbatim evidence snippets, DOI-first references, and notes on uncertainty or taxon specificity. It is useful for deciding which relationships are strong enough for immediate curation versus those needing follow-up primary evidence.*

### Key image evidence (table)
Loukou et al. 2024 Table 1 (minimum aw for building-associated fungi) provides curated, species-level minimum aw ranges relevant to moisture-classification and boundary cases. (loukou2024dampbuildingsassociated media 56a4b8db)

### Warnings / “do not curate yet” flags
1) **Do not equate “xerotolerant” across domains**: In desiccation/anhydrobiosis literature, “xerotolerance” is used inconsistently (sometimes meaning anhydrobiosis/desiccation tolerance rather than growth at low aw). Treat as a potentially ambiguous synonym and only curate where the source clearly links it to **growth/reproduction at low aw**. (grzyb2022introductiontobacterial pages 2-3)

2) **Solute-specific inhibition (chaotropicity) is assay- and solute-dependent**: Growth failure in glycerol-only low-aw media suggests that “low aw → growth” edges require additional conditions (solute identity, chaotropicity). Curation should include modifiers or qualify edges as conditional. (pocsi2024biotechnologicalpotentialof pages 2-5)

3) **Some mechanistic statements are bundled review summaries** (e.g., HogA→glycerol biosynthesis phrasing). For high-confidence gene-level edges in TraitMech, follow-up with the primary sources cited by reviews may be needed (e.g., to map specific genes to specific phenotypic assays and aw values). (pocsi2024biotechnologicalpotentialof pages 5-7)

---

## DOI-first bibliography (with dates and URLs)

1) **Pócsi I., Dijksterhuis J., Houbraken J., de Vries R.P.** (2024-11). *Biotechnological potential of salt tolerant and xerophilic species of Aspergillus.* **Applied Microbiology and Biotechnology**. DOI: **10.1007/s00253-024-13338-5**. https://doi.org/10.1007/s00253-024-13338-5 (pocsi2024biotechnologicalpotentialof pages 1-2, pocsi2024biotechnologicalpotentialof pages 2-5, pocsi2024biotechnologicalpotentialof pages 11-12)

2) **Loukou E., Jensen N.F., Rohde L., Andersen B.** (2024-01). *Damp Buildings: Associated Fungi and How to Find Them.* **Journal of Fungi** 10:108. DOI: **10.3390/jof10020108**. https://doi.org/10.3390/jof10020108 (loukou2024dampbuildingsassociated pages 4-5, loukou2024dampbuildingsassociated media 56a4b8db)

3) **Agrawal S., Chavan P., Dufossé L.** (2024-04). *Hidden Treasure: Halophilic Fungi as a Repository of Bioactive Lead Compounds.* **Journal of Fungi** 10:290. DOI: **10.3390/jof10040290**. https://doi.org/10.3390/jof10040290 (agrawal2024hiddentreasurehalophilic pages 1-2)

4) **Grzyb T., Skłodowska A.** (2022-02). *Introduction to Bacterial Anhydrobiosis: A General Perspective and the Mechanisms of Desiccation-Associated Damage.* **Microorganisms** 10:432. DOI: **10.3390/microorganisms10020432**. https://doi.org/10.3390/microorganisms10020432 (grzyb2022introductiontobacterial pages 2-3)

5) **Preetha S.S., Narayanan R.** (2020-01). *Factors influencing the development of microbes in food.* **Shanlax International Journal of Arts, Science and Humanities** 7:57–77. DOI: **10.34293/sijash.v7i3.473**. https://doi.org/10.34293/sijash.v7i3.473 (preetha2020factorsinfluencingthe pages 6-7)

6) **Dijksterhuis J., Houbraken J.** (2025-01). *Fungal Spoilage of Crops and Food.* In **The Mycota**. DOI: **10.1007/978-3-031-81904-9_3**. https://doi.org/10.1007/978-3-031-81904-9_3 (dijksterhuis2025fungalspoilageof pages 16-17)

7) **Fernando L.D. et al.** (2023-10). *Structural Adaptation of Fungal Cell Wall in Hypersaline Environment.* **Zenodo dataset**. DOI: **10.5281/zenodo.10001628**. https://doi.org/10.5281/zenodo.10001628 (pocsi2024biotechnologicalpotentialof pages 5-7)

## Notes on evidence gaps
This report prioritizes 2024 fungal reviews and an indoor-fungal 2024 review for recent authoritative synthesis. Some gene-level and pathway-level claims (e.g., HogA→glycerol biosynthesis; cell wall remodeling specifics) are present as review summaries; for TraitMech YAML curation at high confidence, retrieving and quoting the underlying primary studies cited by these reviews would strengthen edge specificity (gene ↔ aw condition ↔ growth assay). (pocsi2024biotechnologicalpotentialof pages 5-7)

References

1. (pocsi2024biotechnologicalpotentialof pages 1-2): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

2. (loukou2024dampbuildingsassociated pages 4-5): Evangelia Loukou, Nickolaj Feldt Jensen, Lasse Rohde, and Birgitte Andersen. Damp buildings: associated fungi and how to find them. Journal of Fungi, 10:108, Jan 2024. URL: https://doi.org/10.3390/jof10020108, doi:10.3390/jof10020108. This article has 37 citations.

3. (loukou2024dampbuildingsassociated media 56a4b8db): Evangelia Loukou, Nickolaj Feldt Jensen, Lasse Rohde, and Birgitte Andersen. Damp buildings: associated fungi and how to find them. Journal of Fungi, 10:108, Jan 2024. URL: https://doi.org/10.3390/jof10020108, doi:10.3390/jof10020108. This article has 37 citations.

4. (grzyb2022introductiontobacterial pages 2-3): Tomasz Grzyb and Aleksandra Skłodowska. Introduction to bacterial anhydrobiosis: a general perspective and the mechanisms of desiccation-associated damage. Microorganisms, 10:432, Feb 2022. URL: https://doi.org/10.3390/microorganisms10020432, doi:10.3390/microorganisms10020432. This article has 31 citations.

5. (pocsi2024biotechnologicalpotentialof pages 2-5): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

6. (preetha2020factorsinfluencingthe pages 6-7): S S Preetha and Rita Narayanan. Factors influencing the development of microbes in food. Shanlax International Journal of Arts, Science and Humanities, 7:57-77, Jan 2020. URL: https://doi.org/10.34293/sijash.v7i3.473, doi:10.34293/sijash.v7i3.473. This article has 62 citations.

7. (pocsi2024biotechnologicalpotentialof pages 5-7): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

8. (agrawal2024hiddentreasurehalophilic pages 1-2): Shivankar Agrawal, Pruthviraj Chavan, and Laurent Dufossé. Hidden treasure: halophilic fungi as a repository of bioactive lead compounds. Journal of Fungi, 10:290, Apr 2024. URL: https://doi.org/10.3390/jof10040290, doi:10.3390/jof10040290. This article has 14 citations.

9. (pocsi2024biotechnologicalpotentialof pages 11-12): István Pócsi, Jan Dijksterhuis, Jos Houbraken, and Ronald P. de Vries. Biotechnological potential of salt tolerant and xerophilic species of aspergillus. Applied Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.1007/s00253-024-13338-5, doi:10.1007/s00253-024-13338-5. This article has 18 citations and is from a domain leading peer-reviewed journal.

10. (raghavendra2026growthofmicroorganisms pages 1-2): Jyothi Basapathi Raghavendra, Maria‑Paz Zorzano, and Javier Martin‑Torres. Growth of microorganisms in a martian regolith simulant at reduced water activity. Scientific Reports, Mar 2026. URL: https://doi.org/10.1038/s41598-026-35595-2, doi:10.1038/s41598-026-35595-2. This article has 1 citations and is from a peer-reviewed journal.

11. (dijksterhuis2025fungalspoilageof pages 16-17): Jan Dijksterhuis and Jos Houbraken. Fungal spoilage of crops and food. The Mycota, pages 31-66, Jan 2025. URL: https://doi.org/10.1007/978-3-031-81904-9\_3, doi:10.1007/978-3-031-81904-9\_3. This article has 8 citations.

12. (raghavendra2026growthofmicroorganisms pages 13-14): Jyothi Basapathi Raghavendra, Maria‑Paz Zorzano, and Javier Martin‑Torres. Growth of microorganisms in a martian regolith simulant at reduced water activity. Scientific Reports, Mar 2026. URL: https://doi.org/10.1038/s41598-026-35595-2, doi:10.1038/s41598-026-35595-2. This article has 1 citations and is from a peer-reviewed journal.