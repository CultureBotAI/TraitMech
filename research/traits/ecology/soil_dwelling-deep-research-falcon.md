---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:47:06.193280'
end_time: '2026-08-03T23:56:34.207750'
duration_seconds: 568.01
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: soil-dwelling
  trait_identifier: traitmech:000050
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: soil_dwelling
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A habitat association in which an organism's primary environment is
    soil, a complex and highly diverse microbial habitat central to terrestrial biogeochemical
    cycling.
  parent_traits: traitmech:000047
  synonyms: soil-associated
  evidence_summary: 'DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown",
    characterizes the soil microbiome as a distinct, complex microbial habitat.) |
    DOI:10.1038/nrmicro1341:  (Martiny et al. support soil communities as biogeographically
    structured microbial habitats.)'
  causal_graph_summary: 'soil_dwelling_biogeochemistry: 14 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** soil-dwelling
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000050
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism's primary environment is soil, a complex and highly diverse microbial habitat central to terrestrial biogeochemical cycling.
- **Parent traits:** traitmech:000047
- **Synonyms:** soil-associated
- **Existing evidence:** DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", characterizes the soil microbiome as a distinct, complex microbial habitat.) | DOI:10.1038/nrmicro1341:  (Martiny et al. support soil communities as biogeographically structured microbial habitats.)
- **Existing causal graph summary:** soil_dwelling_biogeochemistry: 14 nodes, 8 edges

## Research Objective

Research the microbial trait **soil-dwelling** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/soil_dwelling.yaml`.

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
- **Trait label:** soil-dwelling
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000050
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A habitat association in which an organism's primary environment is soil, a complex and highly diverse microbial habitat central to terrestrial biogeochemical cycling.
- **Parent traits:** traitmech:000047
- **Synonyms:** soil-associated
- **Existing evidence:** DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", characterizes the soil microbiome as a distinct, complex microbial habitat.) | DOI:10.1038/nrmicro1341:  (Martiny et al. support soil communities as biogeographically structured microbial habitats.)
- **Existing causal graph summary:** soil_dwelling_biogeochemistry: 14 nodes, 8 edges

## Research Objective

Research the microbial trait **soil-dwelling** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/soil_dwelling.yaml`.

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


# TraitMech curation report: soil-dwelling

**Trait:** `traitmech:000050`  
**Category / kind:** ECOLOGY / CLASS  
**Parent:** `traitmech:000047`  
**Recommended primary grounding:** soil environmental material, `ENVO:00001998`

## 1. Scope summary

`traitmech:000050` should represent a **sustained ecological association with soil as the organism’s primary habitat**, encompassing growth, persistence, dormancy, resuscitation, and recurring activity within soil pores, aggregates, mineral–organic interfaces, or soil-associated biological structures. Soil is not homogeneous: micrometre-to-millimetre microhabitats—including aggregate interiors, rhizospheres, drilospheres, photic surfaces, and depth horizons—differ in water, oxygen/redox state, substrates, and microbial activity. A gram of soil can contain thousands of microbial taxa, but most remain undescribed. (fierer2017embracingtheunknown pages 1-2)

The class should **not** mean that every soil-dwelling organism possesses one defining pathway. Current evidence instead supports a habitat-association phenotype produced by alternative life-history strategies: stress tolerance and dormancy, rapid environmental response, resource acquisition, nutrient recycling, competition, or combinations thereof. A 2023 analysis of 128 global soil metagenomes resolved two major genomic trait dimensions explaining 29% and 21% of variation; pH, C:N ratio, and precipitation jointly predicted the dominant strategy. (piton2023lifehistorystrategies pages 11-14, piton2023lifehistorystrategies pages 1-5)

### Operational inclusion criteria

Prefer at least one of the following:

1. repeated isolation or reproducible enrichment from independent soil samples;
2. evidence of in-soil growth or activity, such as stable-isotope incorporation, RNA/protein expression, replication estimates, or substrate turnover;
3. demonstrated persistence followed by resuscitation in soil;
4. comparative ecological evidence that soil is preferred over alternative habitats;
5. experimentally measured fitness, colonization, or reproduction in a soil microhabitat.

### Boundary cases

- **DNA detection alone is insufficient.** Soil DNA can include extracellular/relic DNA, and inactive cells may dominate some samples; one seasonally dry grassland study noted that up to 75% of cells may be inactive at a given time. Activity-sensitive methods such as quantitative stable-isotope probing are therefore stronger evidence of residency. (nicolas2023asubsetof pages 1-2)
- **Dormant organisms may still qualify.** Dormancy followed by recurrent in-soil resuscitation is evidence of a resident life cycle, not absence of habitat association. (imminger2024survivalandrapid pages 1-2)
- **Rhizosphere-associated is narrower than soil-dwelling.** A root specialist can also be soil-dwelling, but root colonization or endophytism should not automatically be generalized to bulk soil.
- **Biological soil crust organisms are specialized soil dwellers.** Biocrust evidence should carry a dryland/soil-surface qualifier.
- **“Isolated from soil” is weak evidence.** Spores, airborne cells, contaminants, pathogens shed into soil, and transient aquatic organisms should not be assigned the class without persistence or activity evidence.
- **Functions are not definitions.** Nitrogen fixation, phosphate solubilization, sporulation, antibiotic production, and biofilm formation can support soil fitness but are neither necessary nor sufficient individually.

## 2. Candidate nodes and ontology grounding

Only identifiers that can be assigned conservatively are given. Composite ecological states are intentionally left label-only rather than assigned speculative CURIEs.

### Habitat and environmental nodes

| Candidate node | Suggested grounding | Curation role |
|---|---|---|
| soil | `ENVO:00001998` | Primary environmental material and trait object |
| rhizosphere | ENVO term should be verified against the project’s pinned ontology release | Soil microhabitat; do not equate with bulk soil |
| biological soil crust | ENVO term should be verified | Dryland soil-surface microhabitat |
| soil aggregate interior / pore | Label-only pending exact ENVO mapping | Microscale low-O₂ or water-retaining habitat |
| soil pH | Label-only environmental quality | Major community-level selector |
| soil moisture / water availability | Label-only environmental quality | Activity, dormancy, osmotic stress, and diffusion driver |
| precipitation amount and seasonality | Label-only climate variable | Community life-history selector |
| oxygen / redox status | `CHEBI:15379` for dioxygen; redox state label-only | Electron acceptor availability and microsite selector |
| soil organic carbon | Label-only mixture | Carbon and energy supply |
| soil C:N ratio | Label-only ratio | Resource-stoichiometry selector |
| N, P, and S availability | Element/chemical-specific CHEBI identifiers only when the measured species is known | Nutrient limitation and metabolic regulation |
| salinity / metal(loid) stress | Label-only unless the causal ion is specified | Environmental selection and resistance |
| organic fertilization | Label-only experimental/management factor | Anthropogenic selector; not intrinsic to the trait |

Broad surveys identify pH, organic-carbon quantity and quality, O₂/redox, moisture, N/P availability, structure, temperature, and plant identity as interacting selectors; bulk measurements nevertheless explain only part of community variation because soil is spatially heterogeneous. (fierer2017embracingtheunknown pages 5-6)

### Processes and pathways

| Candidate node | Suggested grounding | Scope note |
|---|---|---|
| sporulation | `GO:0043934` | Taxon-restricted persistence strategy |
| biofilm formation | `GO:0042710` | Often microhabitat- or rhizosphere-specific |
| chemotaxis | `GO:0006935` | Supports movement toward resources where motility is possible |
| motility | Label-only or taxon-appropriate GO child | Not universal; constrained by pore connectivity and water films |
| dormancy | Label-only pending project-approved ontology | Includes spore and non-spore states |
| resuscitation | Label-only | Transition from dormancy/inactivity to activity |
| osmotic-stress response | GO term should be verified for the organismal context | Particularly relevant to drying/rewetting |
| DNA, protein, and membrane repair | Use exact GO processes only where measured | Central after rewetting in dryland communities |
| extracellular-polymeric-substance production | Label-only composite | Matrix formation and desiccation protection |
| carbohydrate catabolism | Use substrate-specific GO/EC/MetaCyc term | Resource acquisition and decomposition |
| extracellular depolymerization | Use enzyme-specific EC/GO terms | Cellulose, chitin, and other polymer breakdown |
| nitrogen fixation | `GO:0009399` | Functional module, not universal soil trait |
| nitrification / denitrification | Exact GO/MetaCyc modules after pathway evidence | Biogeochemical outcomes |
| phosphate solubilization | Label-only unless reaction is specified | Often assay-defined and chemically heterogeneous |
| siderophore-mediated iron acquisition | Ground to exact siderophore pathway/transport system when known | Nutrient acquisition and competition |
| specialized-metabolite biosynthesis | Use BGC product-specific identifiers where validated | Predicted BGCs alone establish potential, not activity |
| microbial biomass turnover / necromass recycling | Label-only composite | Connects mortality to soil C and nutrients |
| viral lytic cycle | Use virus-process ontology term after verification | Community turnover mechanism |

### Chemicals and molecular structures

- Water: `CHEBI:15377`.
- Dioxygen: `CHEBI:15379`.
- Carbon dioxide: `CHEBI:16526`.
- Ammonium: `CHEBI:28938`; nitrate: `CHEBI:17632`; nitrite: `CHEBI:16301`.
- Orthophosphate: use the protonation-state-specific CHEBI term matching the assay; do not collapse all “phosphate” measurements automatically.
- Iron: ground the measured species, such as Fe²⁺ versus Fe³⁺, rather than generic “iron.”
- Cellulose: `CHEBI:28748`; chitin: verify the current CHEBI record before curation.
- Exopolysaccharide, humic substances, soil organic matter, and microbial necromass: retain as label-only mixtures unless chemically resolved.
- Antibiotics, siderophores, terpenes, non-ribosomal peptides, RiPPs, surfactin, plipastatin, 2,4-diacetylphloroglucinol, and rhamnolipids: assign compound-specific CHEBI/ChEBI-family identifiers only after confirming the exact product.

### Genes, proteins, transporters, and complexes

High-value candidates include `sinR` and `ywcC` biofilm regulators; EPS biosynthetic operons; `tasA`, `tapA`, and `bslA`; sporulation genes; chemotaxis and flagellar modules; carbohydrate-active enzymes; extracellular cellulases/chitinases; siderophore synthesis and uptake systems; TonB-dependent transport; RND efflux systems; nitrogenase genes; and phosphate uptake/regulation systems. These should be linked to exact UniProt accessions only for a specified strain and to GO/EC/Rhea reactions only where experimentally or curator-validated.

In *Bacillus subtilis*, the root-biofilm matrix includes EPS, TasA/TapA protein fibres, and BslA. Plant polysaccharides and malate can inhibit SinR-mediated repression and induce matrix genes, but this is a rhizosphere mechanism rather than a universal soil-dwelling program. (pomerleau2024adaptivelaboratoryevolution pages 1-2)

## 3. Candidate causal edges

The strongest compact set is summarized below.

| subject | predicate | object | evidence class | confidence | DOI |
|---|---|---|---|---|---|
| soil pH | shapes | soil bacterial life-history strategy across global biomes | observational; community-level | high | 10.1038/s41564-023-01465-0 (piton2023lifehistorystrategies pages 11-14, piton2023lifehistorystrategies pages 1-5) |
| precipitation pattern | shapes | soil bacterial life-history strategy across global biomes | observational; community-level | high | 10.1038/s41564-023-01465-0 (piton2023lifehistorystrategies pages 11-14, piton2023lifehistorystrategies pages 1-5) |
| soil C:N ratio | shapes | soil bacterial life-history strategy across global biomes | observational; community-level | medium-high | 10.1038/s41564-023-01465-0 (piton2023lifehistorystrategies pages 1-5) |
| soil rewetting | resuscitates | dormant resident soil microbes | direct experiment; desert/rewetting-specific | high | 10.1038/s41467-024-46920-6 (imminger2024survivalandrapid pages 1-2) |
| soil rewetting | increases | viral lysis-driven microbial biomass turnover | direct experiment; seasonally dry grassland-specific | high | 10.1038/s41467-023-40835-4 (nicolas2023asubsetof pages 1-2) |
| dormancy | supports persistence in | desert soil microbial communities | direct experiment + interpretation; desert-specific | medium-high | 10.1038/s41467-024-46920-6 (imminger2024survivalandrapid pages 1-2) |
| loss of SinR/YwcC-mediated repression | increases | Bacillus subtilis biofilm formation and root colonization | direct experiment; rhizosphere/taxon-specific | high | 10.1128/msystems.00843-23 (pomerleau2024adaptivelaboratoryevolution pages 1-2) |
| fluctuating nutrient availability (C/N/P/S) | selects for | broad substrate utilization and diverse intra-/extracellular enzyme capacity in Streptomyces | review; taxon-specific | medium | 10.3390/microorganisms12081571 (krysenko2024roleofcarbon pages 1-2) |
| specialized metabolites | promote | nutrient acquisition, motility, biofilm production, and competitive inhibition in soil bacteria | review + metagenomic inference; stronger in desert soils | medium | 10.1128/msphere.00192-24 (andreanigerard2024biosyntheticgeneclusters pages 1-2) |
| soil microbial decomposition / organic matter turnover | contributes to | carbon and nitrogen cycling in soil | review | high | 10.3390/microorganisms12081571 (krysenko2024roleofcarbon pages 1-2) |
| organic fertilization | co-selects | genetically linked ARG-MRG-carrying contigs in agricultural soil microbiomes | observational; agroecosystem-specific | high | 10.1038/s41467-024-49165-5 (liu2024organicfertilizationcoselects pages 1-2) |


*Table: This table summarizes the strongest candidate causal edges for curating the soil-dwelling trait, emphasizing broad habitat selectors first and clearly flagging desert-, rhizosphere-, agroecosystem-, and taxon-specific mechanisms. It is useful as a compact starting set for TraitMech graph curation with confidence and scope constraints.*

The following expanded table provides curation-ready triples and supporting snippets. “Curate” means suitable if the indicated scope qualifier is retained.

| Subject — predicate — object | Evidence and supporting snippet | Curation interpretation |
|---|---|---|
| **soil pH — shapes — dominant soil-bacterial life-history strategy** | Piton et al. analyzed 128 global soil metagenomes and identified pH and precipitation as primary drivers; the paper reports that “soil pH, C:N ratio and precipitation patterns together drive the dominant life history strategy.” DOI: [10.1038/s41564-023-01465-0](https://doi.org/10.1038/s41564-023-01465-0), October 2023. (piton2023lifehistorystrategies pages 11-14, piton2023lifehistorystrategies pages 1-5) | **Curate as community-level observational association**, not an organism-level deterministic edge. |
| **precipitation regime — shapes — environmental responsiveness versus nutrient-recycling strategy** | Reduced/fluctuating precipitation was associated with environmental responsiveness, whereas high precipitation and low seasonality were associated with nutrient-recycling profiles. (piton2023lifehistorystrategies pages 8-11) | **Curate with observational/inferred qualifier.** Avoid “precipitation causes soil-dwelling.” |
| **soil C:N ratio — shapes — community genomic strategy** | Random-forest analysis identified C:N together with pH and precipitation as predictors; the first two trait axes explained 29% and 21% of variation. (piton2023lifehistorystrategies pages 1-5) | **Curate as correlational community edge.** |
| **arid/productivity conditions — reduce — bacterial growth potential** | Across 176 soil metagenomes from 11 biomes and six continents, estimated growth potential was lowest at arid subtropical latitudes; latitude explained approximately 15% of variation. DOI: [10.1038/s41467-024-50382-1](https://doi.org/10.1038/s41467-024-50382-1), August 2024. (osburn2024globalpatternsin pages 1-2) | **Curate as global association**, not direct physiology. |
| **investment in carbohydrate acquisition — trades off with — maximum growth potential** | Growth potential was “negatively correlated with the relative abundances of genes involved in carbohydrate metabolism”; the authors interpret a growth–resource-acquisition trade-off. (osburn2024globalpatternsin pages 1-2) | **Curate with inferred-mechanism qualifier.** Codon usage estimates potential, not measured in-situ growth. |
| **drought — promotes — dormant/inactive state** | Desert activity is confined largely to short rain episodes, and the study states that “long-term persistence, facilitated by dormancy, is critical.” DOI: [10.1038/s41467-024-46920-6](https://doi.org/10.1038/s41467-024-46920-6), April 2024. (imminger2024survivalandrapid pages 1-2) | **Curate only as dryland/biocrust-specific.** The authors also caution that spore formation is not common among desert bacteria. |
| **soil rewetting — resuscitates — inactive biocrust microorganisms** | Simulated rain caused nearly all measured populations to resuscitate “within minutes,” investing in repair and energy generation; median replication times were 6–19 days. (imminger2024survivalandrapid pages 1-2) | **Strong direct experimental edge**, but restricted to Negev biocrust and simulated rain. |
| **soil rewetting — increases — viral lysis and microbial biomass turnover** | In seasonally dry California grassland soil, viral richness fell 50% within 24 h, viral biomass increased fourfold within one week, and viral lysis accounted for up to 46% of microbial death after one week. DOI: [10.1038/s41467-023-40835-4](https://doi.org/10.1038/s41467-023-40835-4), September 2023. (nicolas2023asubsetof pages 1-2) | **Strong direct community-process edge.** Do not promote viral lysis to a necessary feature of all soil habitats. |
| **viral lysis — contributes to — post-wet-up CO₂ efflux** | The study concludes that viruses contribute to biomass turnover and the widely observed mineralized-CO₂ pulse following wet-up. (nicolas2023asubsetof pages 1-2) | **Curate as supported contribution**, not sole cause. |
| **loss of `sinR`/`ywcC` repression — increases — biofilm formation and root colonization** | Independent adaptive-evolution lineages carried nonsynonymous mutations in `ywcC` or `sinR`; “mutations that facilitated the formation of robust biofilms on roots were predominant.” DOI: [10.1128/msystems.00843-23](https://doi.org/10.1128/msystems.00843-23), published 11 January 2024. (pomerleau2024adaptivelaboratoryevolution pages 1-2) | **High-confidence direct edge**, explicitly *B. subtilis* and rhizosphere-specific. |
| **EPS/TasA–TapA/BslA matrix — supports — *B. subtilis* root biofilm robustness** | The matrix composition and importance of poly-γ-glutamate for robustness/root colonization are described directly. (pomerleau2024adaptivelaboratoryevolution pages 1-2) | **Curate taxon- and microhabitat-specific**, not as a universal soil mechanism. |
| **bulk-soil exposure — induces — rapid *B. subtilis* sporulation** | The article notes that *B. subtilis* “rapidly sporulate[s] when cells were introduced in bulk soil,” limiting its beneficial effect. (pomerleau2024adaptivelaboratoryevolution pages 1-2) | **Useful boundary edge:** sporulation supports persistence but can reduce active agricultural function. Evidence is taxon/assay-specific. |
| **fluctuating C/N/P/S availability — selects for/supports — broad substrate and enzyme repertoires in *Streptomyces*** | “Their remarkable ability to adapt to fluctuating nutrient conditions is possible through the utilization of a large amount of substrates by diverse intracellular and extracellular enzymes.” DOI: [10.3390/microorganisms12081571](https://doi.org/10.3390/microorganisms12081571), published 31 July 2024. (krysenko2024roleofcarbon pages 1-2) | **Curate as review-supported and genus-specific.** “Selects for” remains evolutionary inference; “supports adaptation” is safer. |
| ***Streptomyces*/Actinomycetota decomposition — contributes to — organic-matter turnover and C/N cycling** | Actinomycetes decompose chitin and cellulose and “play an important role in the nitrogen and carbon cycles.” (krysenko2024roleofcarbon pages 1-2) | **Curate with taxonomic scope.** Use substrate-specific enzymes/reactions where possible. |
| **nutrient availability — regulates — specialized-metabolite production in *Streptomyces*** | Carbon-, nitrogen-, and phosphate-containing compounds modulate antibiotic production through precursor supply from primary metabolism. (krysenko2024roleofcarbon pages 1-2) | **Curate genus-specific regulatory edge.** Exact nutrient–regulator–BGC links require primary studies. |
| **specialized metabolites — support — nutrient acquisition, biofilm, motility, inhibition, and stress tolerance** | The Atacama study states that pigments, antibiotics, antifungals, and siderophores trigger survival strategies including “nutrient acquisition, motility and biofilm production, growth inhibition, and tolerance mechanisms.” DOI: [10.1128/msphere.00192-24](https://doi.org/10.1128/msphere.00192-24), published 17 September 2024. (andreanigerard2024biosyntheticgeneclusters pages 1-2) | **Curate only at a broad review-supported level.** Individual product-to-function edges need experimental validation. |
| **siderophores — increase — iron uptake under low bioavailability** | The same source states that siderophores enhance iron uptake where bioavailability is limited. (andreanigerard2024biosyntheticgeneclusters pages 1-2) | **Mechanistically plausible and broadly supported**, but exact siderophore/receptor should be specified when possible. |
| **desert-soil bacterial genomes — encode — diverse BGCs** | Six Atacama communities yielded 38 MAGs and 168 predicted BGCs, mainly NRP, RiPP, and terpene classes. (andreanigerard2024biosyntheticgeneclusters pages 1-2) | **Curate as genomic potential only**, not metabolite production or causal soil fitness. |
| **organic fertilization — co-selects — genetically linked ARG–MRG contigs** | Across 511 agricultural-soil metagenomes from 17 countries, organically fertilized soils had 63 ARG–MRG contig types versus 22 without organic fertilization; ARG, risk-ARG, and MRG richness were also higher. DOI: [10.1038/s41467-024-49165-5](https://doi.org/10.1038/s41467-024-49165-5), June 2024. (liu2024organicfertilizationcoselects pages 1-2) | **Curate as agroecosystem pressure/risk edge**, not as a positive soil-adaptation mechanism or defining trait. |

## 4. Recent developments, applications, and expert analysis

### Trait-based global ecology

The strongest current conceptual advance is movement from taxon lists toward **community-aggregated genomic traits**. Piton and colleagues found a triangular strategy space ranging from streamlined genomes to expanded metabolic capacities, with the latter differentiating toward environmental responsiveness or nutrient recycling. Average genome size strongly loaded on the first axis (`R² = 0.64`), but only approximately 5–15% of metagenomic reads could be annotated, demonstrating how much soil functional diversity remains unresolved. (piton2023lifehistorystrategies pages 11-14, piton2023lifehistorystrategies pages 1-5)

Osburn and colleagues independently connected codon-usage-derived growth potential to biome productivity. Their 176-metagenome analysis suggests that high growth and broad resource-acquisition machinery are competing investments, reinforcing the expert view that “soil-dwelling” should be represented as a **strategy ensemble**, not a single molecular module. (osburn2024globalpatternsin pages 1-2)

### Activity-resolved soil ecology

Stable-isotope tracing, NanoSIMS, metatranscriptomics, and time-resolved viromics now distinguish active residents from dormant cells and relic DNA. The 2023 California wet-up experiment used 234 metagenomes and 18 triplicated viromes across time and resolved hundreds of MAGs; it quantified both resuscitation-associated dynamics and viral mortality. (nicolas2023asubsetof pages 1-2) The 2024 Negev study showed rapid, nearly community-wide resuscitation but slow median replication, indicating that **repair and persistence—not necessarily rapid population growth—can dominate soil fitness**. (imminger2024survivalandrapid pages 1-2)

### Agricultural implementation

Applications include microbial inoculants, synthetic communities, biofertilizers, biocontrol organisms, microbiome engineering, and soil-health indicators. A 2024 open-field tomato study applied nitrogen-fixing bacteria (*Azospirillum*, *Azotobacter*, and *Rhizobium*) alone or with mycorrhizal fungi and *Bacillus* species; inoculation significantly changed rhizosphere alpha and beta diversity and supported production under reduced fertilizer input. DOI: [10.3390/biology13060400](https://doi.org/10.3390/biology13060400), published 31 May 2024. (novello2024theimpactof pages 1-2)

However, controlled-condition success does not guarantee field efficacy. Inoculants may sporulate in bulk soil, fail to establish amid resident competitors, or express beneficial traits only in root-associated conditions. Adaptive evolution of *B. subtilis* improved root colonization through biofilm-regulatory mutations, illustrating a promising engineering route but also showing that the selected phenotype is **root colonization**, not generic soil dwelling. (pomerleau2024adaptivelaboratoryevolution pages 1-2)

Soil-management interventions also have risks. Organic fertilizers can introduce antibiotics and metals and select genetically linked resistance determinants. The 2024 global analysis found lower microbial Shannon diversity but greater network robustness and substantially greater ARG/MRG richness in organically fertilized soils, emphasizing that microbiome interventions require resistome and mobile-element surveillance. (liu2024organicfertilizationcoselects pages 1-2)

### Natural-product discovery and biogeochemistry

Uncultivated soil organisms remain a major source of specialized-metabolic potential. The Atacama analysis identified 168 BGCs in only 38 MAGs, but the authors stress that ecological functions remain difficult to infer from sequence alone. (andreanigerard2024biosyntheticgeneclusters pages 1-2) *Streptomyces* exemplifies the link between soil nutrient fluctuation, broad catabolic repertoires, decomposition, and secondary metabolism; more than two-thirds of known antibiotics are attributed to the genus, and computational estimates cited in the 2024 review suggest over 150,000 additional antimicrobial compounds may remain unknown. (krysenko2024roleofcarbon pages 1-2)

## 5. Recommended minimal graph architecture

For `data/traits/ecology/soil_dwelling.yaml`, a defensible structure would separate:

1. **Trait anchor:** organism — `has_primary_habitat` — soil.
2. **Environmental filtering:** pH, moisture/precipitation, C:N, oxygen/redox, nutrient availability, structure, and plant inputs — `shapes` — community composition/life-history strategy.
3. **Persistence module:** drying/resource limitation — `induces_or_selects_for` — dormancy, repair, osmotic tolerance, EPS, or sporulation; rewetting — `resuscitates` — inactive residents.
4. **Resource module:** polymeric organic matter — extracellular enzymes/transporters — assimilable C and nutrients — growth or maintenance.
5. **Competition/cooperation module:** siderophores, antibiotics, specialized metabolites, biofilms, and cross-feeding — resource capture/community assembly.
6. **Biogeochemical outputs:** decomposition, nutrient mineralization, biomass turnover, necromass production, CO₂ release, N/P/S transformations.
7. **Qualified subgraphs:** rhizosphere, biocrust, agricultural soil, and taxon-specific mechanisms.

Predicates should distinguish **direct causation** (`activates`, `inhibits`, `converts`, `resuscitates`) from **ecological association** (`associated_with`, `predicts`, `shapes_distribution_of`) and **functional potential** (`encodes_potential_for`).

## 6. Claims not yet ready for unqualified TraitMech curation

1. **“Sporulation causes soil-dwelling.”** Sporulation is absent from many successful soil taxa and may suppress active inoculant function. Curate only lineage-specific edges.
2. **“EPS/biofilm is required for soil residency.”** Evidence is strong for particular roots, aggregates, and desiccation contexts, not universal.
3. **“Large genomes are soil adaptations.”** Global studies show environment-dependent trade-offs; streamlined genomes can dominate arid systems.
4. **“A predicted BGC promotes soil fitness.”** BGC presence demonstrates biosynthetic potential, not expression, product identity, ecological target, or fitness benefit.
5. **“Metagenomic detection proves soil dwelling.”** Relic DNA, inactive cells, and transient propagules remain major confounders.
6. **“A rhizosphere or endosphere phenotype applies to bulk soil.”** Preserve microhabitat qualifiers.
7. **“pH directly causes a specific organism to be soil-dwelling.”** Most global evidence concerns community composition and aggregated genomic traits; indirect effects through plants, fungi, metals, and nutrient chemistry are substantial.
8. **“Phosphate solubilization” as one molecular reaction.** It is an assay-level umbrella covering acidification, chelation, enzymatic mineralization, and mineral-specific chemistry.
9. **Generic taxonomic edges.** Associations for Actinomycetota, Acidobacteriota, Proteobacteria, or *Streptomyces* should not automatically propagate to every member.
10. **Agricultural benefit without field context.** Inoculant performance is conditional on soil, climate, crop, resident microbiota, formulation, and persistence; resistance-gene co-selection must also be considered.

## 7. DOI-first bibliography

1. Piton G, et al. **Life history strategies of soil bacterial communities across global terrestrial biomes.** *Nature Microbiology* 8, 2093–2102. Published October 2023. DOI: [10.1038/s41564-023-01465-0](https://doi.org/10.1038/s41564-023-01465-0). (piton2023lifehistorystrategies pages 11-14, piton2023lifehistorystrategies pages 1-5)
2. Osburn ED, et al. **Global patterns in the growth potential of soil bacterial communities.** *Nature Communications* 15, 6881. Published August 2024. DOI: [10.1038/s41467-024-50382-1](https://doi.org/10.1038/s41467-024-50382-1). (osburn2024globalpatternsin pages 1-2)
3. Imminger S, et al. **Survival and rapid resuscitation permit limited productivity in desert microbial communities.** *Nature Communications* 15, 3056. Published April 2024. DOI: [10.1038/s41467-024-46920-6](https://doi.org/10.1038/s41467-024-46920-6). (imminger2024survivalandrapid pages 1-2)
4. Nicolas AM, et al. **A subset of viruses thrives following microbial resuscitation during rewetting of a seasonally dry California grassland soil.** *Nature Communications* 14, 5835. Published September 2023. DOI: [10.1038/s41467-023-40835-4](https://doi.org/10.1038/s41467-023-40835-4). (nicolas2023asubsetof pages 1-2)
5. Pomerleau M, et al. **Adaptive laboratory evolution reveals regulators involved in repressing biofilm development as key players in *Bacillus subtilis* root colonization.** *mSystems* 9. Published 11 January 2024. DOI: [10.1128/msystems.00843-23](https://doi.org/10.1128/msystems.00843-23). (pomerleau2024adaptivelaboratoryevolution pages 1-2)
6. Krysenko S, Wohlleben W. **Role of Carbon, Nitrogen, Phosphate and Sulfur Metabolism in Secondary Metabolism Precursor Supply in *Streptomyces* spp.** *Microorganisms* 12, 1571. Published 31 July 2024. DOI: [10.3390/microorganisms12081571](https://doi.org/10.3390/microorganisms12081571). (krysenko2024roleofcarbon pages 1-2)
7. Andreani-Gerard CM, et al. **Biosynthetic gene clusters from uncultivated soil bacteria of the Atacama Desert.** *mSphere* 9. Published 17 September 2024. DOI: [10.1128/msphere.00192-24](https://doi.org/10.1128/msphere.00192-24). (andreanigerard2024biosyntheticgeneclusters pages 1-2)
8. Liu Z-T, et al. **Organic fertilization co-selects genetically linked antibiotic and metal(loid) resistance genes in global soil microbiome.** *Nature Communications* 15, 5168. Published June 2024. DOI: [10.1038/s41467-024-49165-5](https://doi.org/10.1038/s41467-024-49165-5). (liu2024organicfertilizationcoselects pages 1-2)
9. Novello G, et al. **The Impact of Nitrogen-Fixing Bacteria-Based Biostimulant…: An Open-Field Trial.** *Biology* 13, 400. Published 31 May 2024. DOI: [10.3390/biology13060400](https://doi.org/10.3390/biology13060400). (novello2024theimpactof pages 1-2)
10. Chandrakasan G, et al. **Mapping, Distribution, Function, and High-Throughput Methodological Strategies for Soil Microbial Communities in the Agroecosystem.** *Spanish Journal of Soil Science* 14. Published October 2024. DOI: [10.3389/sjss.2024.12080](https://doi.org/10.3389/sjss.2024.12080). (chandrakasan2024mappingdistributionfunction pages 9-11, chandrakasan2024mappingdistributionfunction pages 2-3)
11. Fierer N. **Embracing the unknown: disentangling the complexities of the soil microbiome.** *Nature Reviews Microbiology* 15, 579–590. Published August 2017. DOI: [10.1038/nrmicro.2017.87](https://doi.org/10.1038/nrmicro.2017.87). (fierer2017embracingtheunknown pages 1-2, fierer2017embracingtheunknown pages 5-6, fierer2017embracingtheunknown pages 8-9)
12. Berg G, et al. **Microbiome definition re-visited: old concepts and new challenges.** *Microbiome* 8, 103. Published June 2020. DOI: [10.1186/s40168-020-00875-0](https://doi.org/10.1186/s40168-020-00875-0). This supports treating a microbiome as organisms plus their habitat and “theatre of activity,” rather than a sequence list alone. (berg2020microbiomedefinitionrevisited pages 4-5)

**Curation conclusion:** The most defensible core graph should anchor `traitmech:000050` to sustained association with `ENVO:00001998`, use pH–moisture–resource–redox factors as community-level selectors, and represent dormancy/resuscitation, resource acquisition, decomposition, competition, and biomass turnover as alternative, qualified mechanisms. Taxon-specific genes and rhizosphere or desert findings should remain scoped subgraphs rather than inherited requirements of the class.

References

1. (fierer2017embracingtheunknown pages 1-2): Noah Fierer. Embracing the unknown: disentangling the complexities of the soil microbiome. Nature Reviews Microbiology, 15:579-590, Aug 2017. URL: https://doi.org/10.1038/nrmicro.2017.87, doi:10.1038/nrmicro.2017.87. This article has 4065 citations and is from a highest quality peer-reviewed journal.

2. (piton2023lifehistorystrategies pages 11-14): Gabin Piton, Steven D. Allison, Mohammad Bahram, Falk Hildebrand, Jennifer B. H. Martiny, Kathleen K. Treseder, and Adam C. Martiny. Life history strategies of soil bacterial communities across global terrestrial biomes. Nature Microbiology, 8:2093-2102, Oct 2023. URL: https://doi.org/10.1038/s41564-023-01465-0, doi:10.1038/s41564-023-01465-0. This article has 178 citations and is from a highest quality peer-reviewed journal.

3. (piton2023lifehistorystrategies pages 1-5): Gabin Piton, Steven D. Allison, Mohammad Bahram, Falk Hildebrand, Jennifer B. H. Martiny, Kathleen K. Treseder, and Adam C. Martiny. Life history strategies of soil bacterial communities across global terrestrial biomes. Nature Microbiology, 8:2093-2102, Oct 2023. URL: https://doi.org/10.1038/s41564-023-01465-0, doi:10.1038/s41564-023-01465-0. This article has 178 citations and is from a highest quality peer-reviewed journal.

4. (nicolas2023asubsetof pages 1-2): Alexa M. Nicolas, Ella T. Sieradzki, Jennifer Pett-Ridge, Jillian F. Banfield, Michiko E. Taga, Mary K. Firestone, and Steven J. Blazewicz. A subset of viruses thrives following microbial resuscitation during rewetting of a seasonally dry california grassland soil. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-40835-4, doi:10.1038/s41467-023-40835-4. This article has 61 citations and is from a highest quality peer-reviewed journal.

5. (imminger2024survivalandrapid pages 1-2): Stefanie Imminger, Dimitri V. Meier, Arno Schintlmeister, Anton Legin, Jörg Schnecker, Andreas Richter, Osnat Gillor, Stephanie A. Eichorst, and Dagmar Woebken. Survival and rapid resuscitation permit limited productivity in desert microbial communities. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-46920-6, doi:10.1038/s41467-024-46920-6. This article has 52 citations and is from a highest quality peer-reviewed journal.

6. (fierer2017embracingtheunknown pages 5-6): Noah Fierer. Embracing the unknown: disentangling the complexities of the soil microbiome. Nature Reviews Microbiology, 15:579-590, Aug 2017. URL: https://doi.org/10.1038/nrmicro.2017.87, doi:10.1038/nrmicro.2017.87. This article has 4065 citations and is from a highest quality peer-reviewed journal.

7. (pomerleau2024adaptivelaboratoryevolution pages 1-2): Maude Pomerleau, Vincent Charron-Lamoureux, Lucille Léonard, Frédéric Grenier, Sébastien Rodrigue, and Pascale B. Beauregard. Adaptive laboratory evolution reveals regulators involved in repressing biofilm development as key players in <i>bacillus subtilis</i> root colonization. Feb 2024. URL: https://doi.org/10.1128/msystems.00843-23, doi:10.1128/msystems.00843-23. This article has 38 citations and is from a peer-reviewed journal.

8. (krysenko2024roleofcarbon pages 1-2): Sergii Krysenko and Wolfgang Wohlleben. Role of carbon, nitrogen, phosphate and sulfur metabolism in secondary metabolism precursor supply in streptomyces spp. Microorganisms, 12:1571, Jul 2024. URL: https://doi.org/10.3390/microorganisms12081571, doi:10.3390/microorganisms12081571. This article has 62 citations.

9. (andreanigerard2024biosyntheticgeneclusters pages 1-2): Constanza M. Andreani-Gerard, Verónica Cambiazo, and Mauricio González. Biosynthetic gene clusters from uncultivated soil bacteria of the atacama desert. Oct 2024. URL: https://doi.org/10.1128/msphere.00192-24, doi:10.1128/msphere.00192-24. This article has 11 citations and is from a peer-reviewed journal.

10. (liu2024organicfertilizationcoselects pages 1-2): Zi-Teng Liu, Rui-Ao Ma, Dong Zhu, Konstantinos T. Konstantinidis, Yong-guan Zhu, and Si-Yu Zhang. Organic fertilization co-selects genetically linked antibiotic and metal(loid) resistance genes in global soil microbiome. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49165-5, doi:10.1038/s41467-024-49165-5. This article has 159 citations and is from a highest quality peer-reviewed journal.

11. (piton2023lifehistorystrategies pages 8-11): Gabin Piton, Steven D. Allison, Mohammad Bahram, Falk Hildebrand, Jennifer B. H. Martiny, Kathleen K. Treseder, and Adam C. Martiny. Life history strategies of soil bacterial communities across global terrestrial biomes. Nature Microbiology, 8:2093-2102, Oct 2023. URL: https://doi.org/10.1038/s41564-023-01465-0, doi:10.1038/s41564-023-01465-0. This article has 178 citations and is from a highest quality peer-reviewed journal.

12. (osburn2024globalpatternsin pages 1-2): Ernest D. Osburn, Steven G. McBride, Mohammad Bahram, and Michael S. Strickland. Global patterns in the growth potential of soil bacterial communities. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-50382-1, doi:10.1038/s41467-024-50382-1. This article has 43 citations and is from a highest quality peer-reviewed journal.

13. (novello2024theimpactof pages 1-2): Giorgia Novello, Elisa Bona, Martina Nasuelli, Nadia Massa, Cristina Sudiro, Daniela Cristina Campana, Susanna Gorrasi, Marie Louise Hochart, Adriano Altissimo, Francesco Vuolo, and Elisa Gamalero. The impact of nitrogen-fixing bacteria-based biostimulant alone or in combination with commercial inoculum on tomato native rhizosphere microbiota and production: an open-field trial. Biology, 13:400, May 2024. URL: https://doi.org/10.3390/biology13060400, doi:10.3390/biology13060400. This article has 15 citations.

14. (chandrakasan2024mappingdistributionfunction pages 9-11): Gobinath Chandrakasan, Markus Gastauer, and Gabriel Marcus. Mapping, distribution, function, and high-throughput methodological strategies for soil microbial communities in the agroecosystem in the last decades. Spanish Journal of Soil Science, Oct 2024. URL: https://doi.org/10.3389/sjss.2024.12080, doi:10.3389/sjss.2024.12080. This article has 4 citations.

15. (chandrakasan2024mappingdistributionfunction pages 2-3): Gobinath Chandrakasan, Markus Gastauer, and Gabriel Marcus. Mapping, distribution, function, and high-throughput methodological strategies for soil microbial communities in the agroecosystem in the last decades. Spanish Journal of Soil Science, Oct 2024. URL: https://doi.org/10.3389/sjss.2024.12080, doi:10.3389/sjss.2024.12080. This article has 4 citations.

16. (fierer2017embracingtheunknown pages 8-9): Noah Fierer. Embracing the unknown: disentangling the complexities of the soil microbiome. Nature Reviews Microbiology, 15:579-590, Aug 2017. URL: https://doi.org/10.1038/nrmicro.2017.87, doi:10.1038/nrmicro.2017.87. This article has 4065 citations and is from a highest quality peer-reviewed journal.

17. (berg2020microbiomedefinitionrevisited pages 4-5): Gabriele Berg, Daria Rybakova, Doreen Fischer, Tomislav Cernava, Marie-Christine Champomier Vergès, Trevor Charles, Xiaoyulong Chen, Luca Cocolin, Kellye Eversole, Gema Herrero Corral, Maria Kazou, Linda Kinkel, Lene Lange, Nelson Lima, Alexander Loy, James A. Macklin, Emmanuelle Maguin, Tim Mauchline, Ryan McClure, Birgit Mitter, Matthew Ryan, Inga Sarand, Hauke Smidt, Bettina Schelkle, Hugo Roume, G. Seghal Kiran, Joseph Selvin, Rafael Soares Correa de Souza, Leo van Overbeek, Brajesh K. Singh, Michael Wagner, Aaron Walsh, Angela Sessitsch, and Michael Schloter. Microbiome definition re-visited: old concepts and new challenges. Microbiome, Jun 2020. URL: https://doi.org/10.1186/s40168-020-00875-0, doi:10.1186/s40168-020-00875-0. This article has 3323 citations and is from a highest quality peer-reviewed journal.