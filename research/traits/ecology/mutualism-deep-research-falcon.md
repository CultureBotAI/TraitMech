---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T14:47:02.055259'
end_time: '2026-08-04T14:53:53.058220'
duration_seconds: 411.0
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mutualism
  trait_identifier: traitmech:000041
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: mutualism
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A symbiosis in which both the microorganism and its host or partner
    benefit from the association, often through exchange of nutrients or services.
  parent_traits: traitmech:000040
  synonyms: mutualist
  evidence_summary: "DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document widespread\
    \ mutually beneficial host-microbe associations across animals.) | DOI:10.1126/science.1104816:\
    \  (B\xE4ckhed et al., \"Host-bacterial mutualism in the human intestine\", supports\
    \ reciprocal benefit (nutrient harvest for the host, habitat for the microbes)\
    \ as the defining feature of mutualism.)"
  causal_graph_summary: 'mutualism_reciprocal_benefit: 10 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mutualism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000041
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which both the microorganism and its host or partner benefit from the association, often through exchange of nutrients or services.
- **Parent traits:** traitmech:000040
- **Synonyms:** mutualist
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document widespread mutually beneficial host-microbe associations across animals.) | DOI:10.1126/science.1104816:  (Bäckhed et al., "Host-bacterial mutualism in the human intestine", supports reciprocal benefit (nutrient harvest for the host, habitat for the microbes) as the defining feature of mutualism.)
- **Existing causal graph summary:** mutualism_reciprocal_benefit: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **mutualism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/mutualism.yaml`.

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
- **Trait label:** mutualism
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000041
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which both the microorganism and its host or partner benefit from the association, often through exchange of nutrients or services.
- **Parent traits:** traitmech:000040
- **Synonyms:** mutualist
- **Existing evidence:** DOI:10.1073/pnas.1218525110:  (McFall-Ngai et al. document widespread mutually beneficial host-microbe associations across animals.) | DOI:10.1126/science.1104816:  (Bäckhed et al., "Host-bacterial mutualism in the human intestine", supports reciprocal benefit (nutrient harvest for the host, habitat for the microbes) as the defining feature of mutualism.)
- **Existing causal graph summary:** mutualism_reciprocal_benefit: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **mutualism** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/mutualism.yaml`.

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


# TraitMech curation report: microbial mutualism

## Record and scope summary

- **Trait label:** mutualism
- **Trait identifier:** **`traitmech:000041`**
- **Category / kind / status:** ECOLOGY / CLASS / REVIEWED
- **Parent:** `traitmech:000040`
- **Synonym:** mutualist

For TraitMech, **mutualism should represent an ecological interaction outcome, not a single constitutive microbial capability**. The minimum criterion is a contextually demonstrated **positive net fitness effect on both partners (+/+)**, whether microbe–microbe or host–microbe. A graph should therefore terminate in two benefit branches—one for each partner—and record the environmental or experimental context in which both benefits were observed. The current definition, “a symbiosis in which both the microorganism and its host or partner benefit,” is consistent with contemporary usage.

Cross-feeding is a mechanism, not automatically mutualism: it can be mutualistic (+/+), commensal (+/0), or exploitative (+/−), depending on measured fitness effects. **Syntrophy** is the narrower case of obligate mutualistic metabolism in which partners jointly metabolize a substrate or sustain growth that neither can accomplish independently. “Cooperation” additionally implies an evolved or active investment that benefits another organism; incidental by-product exchange can produce mutual benefit without demonstrating cooperative adaptation. Parasitism/exploitation differs by a negative effect on one partner. These distinctions are emphasized in the 2023 authoritative review by Culp and Goodman. (culp2023crossfeedinginthe pages 2-4, culp2023crossfeedinginthe pages 1-2)

Mutualism is also **state- and environment-dependent**. The same pair can compete in nutrient-rich conditions but become obligately mutualistic under nutrient limitation. Mycorrhizal interactions similarly range from mutualism to parasitism with soil fertility, developmental stage, partner genotype, and physiology. Thus, “mutualist” should not be inferred solely from taxonomy, co-occurrence, colonization, or metabolite transfer. (culp2023crossfeedinginthe pages 2-4, pena2024mycorrhizalsymbiosisand pages 1-3)

## Current understanding and recent developments

### 1. Reciprocal metabolite exchange is a major mechanistic backbone

The strongest generalizable model is:

**partner A metabolic activity → extracellular metabolite/service → partner B uptake or response → increased B fitness; partner B activity → reciprocal resource/service → increased A fitness → mutualism.**

Recent gut-microbiome synthesis treats amino acids, vitamins, cofactors, fermentation products, electron carriers, and metals as major exchanged currencies. Such exchanges can support division of labor, coexistence, resilience, and invasion resistance, but their ecological sign must be measured rather than assumed. (culp2023crossfeedinginthe pages 15-17, culp2023crossfeedinginthe pages 1-2, culp2023crossfeedinginthe pages 23-26)

A 2022 systematic experiment provides useful quantitative context: four amino-acid-auxotrophic genotypes from two recipient species were paired with donors from 25 bacterial species. **Sixty-three of 100 combinations showed unidirectional cross-feeding, and in approximately 40% of all analyzed cases both recipient and autonomous donor gained significant growth advantages.** Reciprocity therefore arose frequently, but not universally, in this assay. (giri2022prevalentemergenceof pages 1-2, giri2022prevalentemergenceof pages 2-3)

### 2. Genetics can establish causal rather than correlational edges

Isogenic mutants provide particularly strong graph evidence. In a gnotobiotic gut system, *Bifidobacterium breve* `fucP` was required to form 1,2-propanediol from fucose, whereas the *Limosilactobacillus reuteri* `pduCDE` operon encoded utilization of that metabolite. The operon imposed a burden when substrate was absent but improved ecological performance when the producer and upstream mucin degrader were present. This demonstrates genotype × community × resource dependence. (cheng2020ecologicalimportanceof pages 13-15)

In a synthetic anaerobic mutualism, *Escherichia coli* supplied glucose-fermentation products as carbon to *Rhodopseudomonas palustris*, while engineered *R. palustris* fixed N₂ and excreted NH₄⁺ for *E. coli*. RB-TnSeq identified hundreds of mutualism-dependent *E. coli* fitness determinants; the NtrC-mediated nitrogen-starvation response was crucial, and coculture unexpectedly rescued an *E. coli* purine auxotroph. This shows why graph curation should accommodate secondary exchanges rather than assume one currency per partnership. (lasarre2020covertcrossfeedingrevealed pages 1-2)

### 3. Host benefit can be coupled to microbe–microbe exchange

In *Drosophila*, isotope-resolved metabolomics showed that *Lactobacillus plantarum* produced lactate used by *Acetobacter pomorum*; *A. pomorum* then produced and excreted isoleucine and other amino acids needed by *L. plantarum* on an imbalanced diet. Lactate was necessary and sufficient, in the presence of *A. pomorum*, to suppress host protein appetite; the community also affected reproduction and dietary resilience. This is a strong tripartite graph, but it is specific to the strains, defined diet, and fly model. (henriques2020metaboliccrossfeedingin pages 1-2)

### 4. The 2024 plant–fungus–bacterium model expands graphs beyond pairwise interactions

A 2024 *Nature Reviews Microbiology* synthesis describes top-down carbon and bottom-up mineral flows across the plant–arbuscular-mycorrhizal-fungus–bacterium continuum. The peri-arbuscular space is the plant–fungus exchange interface, while the hyphosphere is the fungus–bacterium interface. Plants were estimated to allocate approximately **6% of net photosynthate**, especially sugars and fatty acids, to arbuscular mycorrhizal fungi (AMF); peri-arbuscular-membrane SWEET-family proteins can export sugars. In return, fungal networks acquire mineral nutrients for plants, while hyphal exudates support bacteria. Hyphospheric bacteria reported across studies encompassed **26 phyla**. (duan2024crosskingdomnutrientexchange pages 3-4)

The same review frames AMF and associated bacteria as prospective agricultural biostimulants, but partner identity, soil chemistry, climate, native communities, and establishment success remain major implementation constraints. (duan2024crosskingdomnutrientexchange pages 3-4)

A separate September 2024 forest review defines ectomycorrhizal exchange as plant carbon for fungal nitrogen and phosphorus, while emphasizing a continuum from invested benefits to resource appropriation. Approximately **2% of vascular plant species (~8,500 species)** form ectomycorrhizal symbioses; temperate and boreal tree hosts comprise about **60% of global tree stems** and may associate with more than **20,000 fungal species**. These are global association estimates, not estimates that every pairing is mutually beneficial under every condition. (pena2024mycorrhizalsymbiosisand pages 1-3)

## Candidate nodes grouped by type

### Trait and interaction outcomes

- mutualism — `traitmech:000041`
- reciprocal benefit / positive fitness effect on both partners — label-only candidate
- microbial fitness increase — label-only candidate
- host nutrient acquisition, growth, reproduction, stress resilience, or altered feeding behavior — preferably represented as separate measurable outcome nodes
- mutualism–parasitism continuum — label-only contextual node

### Organisms and ecological participants

Ground these to exact NCBITaxon identifiers only after strain/species reconciliation in the source:

- *Escherichia coli*
- *Rhodopseudomonas palustris*
- *Bifidobacterium breve*, *Bifidobacterium bifidum*
- *Limosilactobacillus reuteri* (source may use former name *Lactobacillus reuteri*)
- *Lactobacillus plantarum*, *Acetobacter pomorum*
- *Drosophila melanogaster*
- arbuscular mycorrhizal fungi / Glomeromycotina
- ectomycorrhizal fungi
- plant or forest-tree host
- hyphospheric bacteria

### Chemicals and nutrient currencies

High-confidence CHEBI candidates, subject to identifier validation during YAML preparation:

- lactate — **CHEBI:24996**
- L-isoleucine — **CHEBI:24898**
- 1,2-propanediol — **CHEBI:16997**
- L-fucose — **CHEBI:2181**
- ammonium — **CHEBI:28938**
- dinitrogen — **CHEBI:17997**
- phosphate — use the exact protonation-state CHEBI term required by the experiment
- glucose — **CHEBI:17234**
- succinate — **CHEBI:30031**
- fumarate — **CHEBI:18012**
- malate — select the experimentally relevant stereochemical/protonation form
- butyrate, purines, amino acids, fatty acids, sugars, siderophores, heme, sialic acid — validate exact chemical forms before grounding

### Genes, proteins, transporters, and regulatory systems

- `fucP`: L-fucose permease; species-specific gene/protein grounding required
- `pduCDE`: propanediol dehydratase operon; represent the operon plus encoded enzyme complex only if the schema permits
- `ntrC` / NtrC: nitrogen-response regulator; species-specific UniProt accession required
- SWEET-family sugar transporters: family-level node unless a source identifies a specific paralogue
- Hbp hemoglobin protease and siderophore-production systems: candidate nodes from the 2023 gut review, but curate only in their malnutrition/inflammation/pathobiont context (culp2023crossfeedinginthe pages 15-17)

### Pathways, processes, and modules

- metabolic cross-feeding
- amino-acid biosynthesis and export
- lactate production and utilization
- fucose fermentation to 1,2-propanediol
- 1,2-propanediol utilization
- glucose fermentation
- biological nitrogen fixation — **GO:0009399**
- ammonium export and assimilation
- nitrogen-starvation response
- purine biosynthesis/cross-feeding
- photosynthate allocation
- sugar export across the peri-arbuscular membrane
- fungal phosphate/nitrogen acquisition and transfer
- extracellular depolymerization of host mucin
- anaerobic respiration using malate/fumarate-associated metabolic niches

### Compartments and environmental factors

- extracellular space — **GO:0005576**, where biologically appropriate
- peri-arbuscular membrane, peri-arbuscular space, intraradical and extraradical hyphae — specialized label-only candidates pending ontology review
- host intestine / gut environment
- mucus or mucin-associated habitat
- hyphosphere, rhizosphere, soil micropore, forest soil
- anaerobiosis, iron limitation, nitrogen limitation, phosphorus availability
- nutrient-rich versus nutrient-poor medium
- imbalanced or essential-amino-acid-deficient diet
- malnutrition and inflammation
- high fertilization, seedling developmental stage, partner-genotype mismatch
- spatial proximity and metabolite-transport limitation

## Candidate causal edges

The table below contains the strongest directly actionable edges. “High” means the direction is supported by genetic perturbation, isotope tracing, defined coculture, or a recent authoritative synthesis; it does not imply universality across taxa.

| confidence | subject | predicate | object | system/context | evidence snippet (short quotation) | DOI |
|---|---|---|---|---|---|---|
| high | *Lactobacillus plantarum* lactate | enables production of | amino acids essential to *Lactobacillus plantarum* by *Acetobacter pomorum* | *Drosophila melanogaster* gut; imbalanced/essential-amino-acid-poor diet | “Ap uses the lactate produced by Lp to supply amino acids that are essential to Lp, allowing it to grow in imbalanced diets.” (henriques2020metaboliccrossfeedingin pages 1-2) | 10.1038/s41467-020-18049-9 |
| high | lactate | is necessary and sufficient for | *Acetobacter pomorum* alteration of host protein appetite | *Drosophila melanogaster* gut-host mutualism context | “Lactate is also necessary and sufficient for Ap to alter the fly’s protein appetite.” (henriques2020metaboliccrossfeedingin pages 1-2) | 10.1038/s41467-020-18049-9 |
| high | *Bifidobacterium breve* fucP | required for formation of | 1,2-propanediol from fucose | gnotobiotic mouse gut; three-species mucin/fucose network | “the l-fucose permease (fucP) gene in *B. breve*, which is required for 1,2-propanediol formation from fucose” (cheng2020ecologicalimportanceof pages 13-15) | 10.1128/AEM.00190-20 |
| high | 1,2-propanediol | enhances growth of | *Limosilactobacillus reuteri* | vertebrate/gnotobiotic mouse gut cross-feeding | “in vitro growth of *Lactobacillus reuteri* ... is enhanced through 1,2-propanediol produced by *Bifidobacterium breve*” (cheng2020ecologicalimportanceof pages 13-15) | 10.1128/AEM.00190-20 |
| high | *Limosilactobacillus reuteri* pduCDE operon | encodes ability to use | 1,2-propanediol | vertebrate/gnotobiotic mouse gut cross-feeding | “the trophic interaction is dependent on the pduCDE operon in *L. reuteri*, which encodes the ability to use 1,2-propanediol” (cheng2020ecologicalimportanceof pages 13-15) | 10.1128/AEM.00190-20 |
| high | *Escherichia coli* fermentation products | provide carbon to | *Rhodopseudomonas palustris* | synthetic anaerobic coculture mutualism | “*E. coli* provides carbon to *R. palustris* in the form of glucose fermentation products” (lasarre2020covertcrossfeedingrevealed pages 1-2) | 10.1128/AEM.00543-20 |
| high | *Rhodopseudomonas palustris* N2 fixation / NH4+ excretion | provides nitrogen to | *Escherichia coli* | synthetic anaerobic coculture mutualism | “*R. palustris* fixes N2 gas and provides nitrogen to *E. coli* in the form of NH4+” (lasarre2020covertcrossfeedingrevealed pages 1-2) | 10.1128/AEM.00543-20 |
| medium | NtrC-mediated nitrogen starvation response | is crucial for fitness in | *Escherichia coli* during coculture | synthetic mutualism; gene-level fitness determinant | “the *E. coli* NtrC-mediated nitrogen starvation response (NSR) is crucial for fitness in coculture” (lasarre2020covertcrossfeedingrevealed pages 1-2) | 10.1128/AEM.00543-20 |
| high | plant photosynthates (fatty acids and sugars) | are provided to | arbuscular mycorrhizal fungi | plant–AMF continuum | “plants provide approximately 6% of their net photosynthates (particularly fatty acids and sugars) to AMF” (duan2024crosskingdomnutrientexchange pages 3-4) | 10.1038/s41579-024-01073-7 |
| high | SWEET family transporters | export | sugars to peri-arbuscular interface / AMF | plant–AMF nutrient exchange interface | “Sugars can be exported extracellularly via members of the SWEET ... family localized in the peri-arbuscular membrane” (duan2024crosskingdomnutrientexchange pages 3-4) | 10.1038/s41579-024-01073-7 |
| high | arbuscular mycorrhizal fungi | provide mineral nutrients to | plants | plant–AMF–bacterium continuum | “plants acquire mineral nutrients necessary for growth, and AMF, as well as its associated bacteria, obtain C for metabolism, thus improving the fitness of all members.” (duan2024crosskingdomnutrientexchange pages 3-4) | 10.1038/s41579-024-01073-7 |
| medium | ectomycorrhizal fungi | transfer nitrogen and phosphorus to | plant host | forest tree ectomycorrhizal mutualism | “The mycorrhizal fungus obtains carbon (C) from the plant, which, in exchange, receives soil nutrients, mainly nitrogen (N) and phosphorus (P) from the fungus” (pena2024mycorrhizalsymbiosisand pages 1-3) | 10.1007/s00253-024-13298-w |
| high | low-nutrient / imbalanced diet | shifts interaction toward | syntrophic mutualism | fly gut microbial community | “a syntrophic relationship is established to overcome detrimental host diets” (henriques2020metaboliccrossfeedingin pages 1-2) | 10.1038/s41467-020-18049-9 |
| high | nutrient availability | can switch cross-feeding outcome between | competition and obligate mutualism | gut microbiome ecology, general principle | “the same strain pairs shift interaction type based on nutrient availability (high nutrients→competition; low nutrients→obligate mutualism)” (culp2023crossfeedinginthe pages 2-4) | 10.1016/j.chom.2023.03.016 |
| high | environmental and physiological context | modulates position on | mutualism–parasitism continuum | mycorrhizal symbiosis | “The interaction can range from mutualistic to parasitic depending on environmental and physiological contexts.” (pena2024mycorrhizalsymbiosisand pages 1-3) | 10.1007/s00253-024-13298-w |


*Table: This table compiles the strongest source-backed causal edges for curating traitmech:000041 microbial mutualism, emphasizing reciprocal nutrient exchange, named genes/transporters, and context dependence. It is useful as a compact starting point for TraitMech node and edge selection with direct evidence citations.*

Additional graph candidates supported by quantitative community studies are:

| Proposed triple | Reference and supporting snippet | Curation note |
|---|---|---|
| *Bacteroides caecimuris* / *Muribaculum intestinale* → **supply** → carbon metabolites to consortium members | The OMM study identified these Bacteroidetes as primary carbon suppliers. DOI: [10.1128/msystems.01484-21](https://doi.org/10.1128/msystems.01484-21), published April 2022. (escriva2022distinctnand pages 1-2) | Medium confidence for `mutualism`: recipient benefit is clear, but bilateral benefit must be demonstrated for each pair. |
| succinate → **is converted to** → butyrate | Isotope tracing validated succinate-to-butyrate conversion. (escriva2022distinctnand pages 1-2) | High confidence as a metabolic edge; not by itself evidence of +/+ mutualism. |
| malate/fumarate availability → **supports** → consumer physiological benefit/anaerobic respiration | The consortium study identified strong benefits from these dicarboxylates. (escriva2022distinctnand pages 5-6) | Assay-specific; ground exact species and reactions from the primary paper before curation. |
| bidirectional metabolite exchange → **increases probability of** → mutualistic cooperation | Around 40% of tested combinations benefited both partners; reciprocal positive feedback can favor costly metabolite investment. DOI: [10.1038/s43705-022-00155-y](https://doi.org/10.1038/s43705-022-00155-y), accepted 5 July 2022. (giri2022prevalentemergenceof pages 1-2) | Curate as an ecological/evolutionary relationship, not a deterministic molecular edge. |
| high nutrient availability → **shifts interaction toward** → competition | “The same strain pairs shift interaction type based on nutrient availability.” DOI: [10.1016/j.chom.2023.03.016](https://doi.org/10.1016/j.chom.2023.03.016), published April 2023. (culp2023crossfeedinginthe pages 2-4) | General contextual edge; retain as conditional/uncertain unless linked to a specific experiment. |
| severe nitrogen limitation → **can shift** → ectomycorrhizal nutrient exchange toward resource appropriation | Fungi may retain N while securing plant carbon under severe N limitation. DOI: [10.1007/s00253-024-13298-w](https://doi.org/10.1007/s00253-024-13298-w), published 9 September 2024. (pena2024mycorrhizalsymbiosisand pages 1-3) | Strong warning against treating mycorrhizal association as constitutive mutualism. |

## Recommended graph architecture

A robust replacement or extension for the existing 10-node/7-edge graph should use a **generic core plus evidence-specific modules**:

1. **Environmental/resource context** regulates partner metabolic activity.
2. Partner A produces, externalizes, or makes available resource/service A.
3. Partner B imports or uses resource A through a named transporter/pathway.
4. Resource A increases a measured B fitness or host-performance outcome.
5. Partner B provides resource/service B.
6. Partner A imports or responds to B through a named mechanism.
7. Resource/service B increases measured A fitness.
8. The conjunction of positive A and B outcomes supports `traitmech:000041`.

Do **not** collapse the two benefit branches into “cross-feeding causes mutualism.” Keeping separate fitness outcomes makes the graph falsifiable and permits a relationship to be reclassified as commensal or exploitative when context changes.

The most defensible first YAML module is the engineered *E. coli–R. palustris* system because both essential currencies and dependencies are explicit. A second strong module is the diet-dependent *L. plantarum–A. pomorum–Drosophila* graph, which adds host-level consequences. The `fucP–1,2-propanediol–pduCDE` module is mechanistically excellent for donor-to-recipient cross-feeding but should not be labeled mutualism unless the reciprocal benefit branch is represented and evidenced. (cheng2020ecologicalimportanceof pages 13-15, henriques2020metaboliccrossfeedingin pages 1-2, lasarre2020covertcrossfeedingrevealed pages 1-2)

## Applications and real-world implementation

1. **Rational microbial consortia and microbiome engineering.** Defined strains can be selected for complementary nutrient production and uptake. The 12-member Oligo-Mouse-Microbiota analysis found **142 interactions involving 76 cross-fed metabolites among 10 analyzed species**; consumed-metabolite number correlated with genome size at **r = 0.80**. This supports metabolomics-guided design, while the observed asymmetry warns that most exchange edges are not automatically mutualistic. (escriva2022distinctnand pages 5-6)

2. **Diet-responsive microbiome interventions.** The fly study demonstrates a proof of principle in which lactate-driven microbial metabolism changes microbial persistence and host appetite under amino-acid imbalance. Translation to humans would require species-specific mechanistic and clinical validation. (henriques2020metaboliccrossfeedingin pages 1-2)

3. **Sustainable agriculture.** AMF and hyphospheric bacteria are being developed as biostimulants to improve phosphorus/nitrogen acquisition, plant growth, stress tolerance, and fertilizer efficiency. The 2024 synthesis explicitly identifies this application while emphasizing three-kingdom interaction complexity. (duan2024crosskingdomnutrientexchange pages 3-4)

4. **Forest restoration and climate resilience.** Ectomycorrhizal functional diversity may support complementary nitrogen acquisition and tree nutrition, informing restoration and resilience planning. However, management must account for the mutualism–parasitism continuum rather than maximizing inoculation indiscriminately. (pena2024mycorrhizalsymbiosisand pages 1-3)

5. **Synthetic ecology and biotechnology.** Carbon–nitrogen exchange can stabilize engineered cocultures for bioproduction, and genome-wide fitness screens can identify genes that improve or destabilize community performance. Unexpected purine exchange in a deliberately simple two-species consortium illustrates both the opportunity and predictability limits. (lasarre2020covertcrossfeedingrevealed pages 1-2)

## Expert interpretation

The strongest expert consensus is that microbial mutualism is **an emergent, conditional property of an interaction**, not a taxonomic label. Culp and Goodman’s 2023 framework makes partner fitness the classification criterion; Duan and colleagues’ 2024 synthesis extends the unit of analysis to spatially organized, three-kingdom nutrient networks; and Pena and Tibbett’s 2024 review explicitly treats mutualism and parasitism as points on a resource-dependent continuum. Together, these sources favor graphs containing context, exchange mechanism, and independently evidenced benefits over broad “beneficial microbe” assertions. (culp2023crossfeedinginthe pages 2-4, pena2024mycorrhizalsymbiosisand pages 1-3, duan2024crosskingdomnutrientexchange pages 3-4)

The evidence also argues against equating reciprocity with active cooperation. Giri and colleagues distinguish passive metabolite release, unidirectional by-product use, spontaneous reciprocity, and evolved costly investment. A TraitMech graph can curate mutualism at the reciprocal-benefit stage, but should only use “cooperative secretion” when production is shown to be an evolved or regulated investment rather than leakage or waste disposal. (giri2022prevalentemergenceof pages 1-2)

## Warnings: claims not yet suitable for curation

- **Do not infer mutualism from co-occurrence, correlation, network centrality, or physical association.** Both partner benefits must be measured or strongly demonstrated.
- **Do not treat every cross-feeding edge as reciprocal.** The OMM network contains many synergistic recipient effects, but donor benefits are not established for every pair. (escriva2022distinctnand pages 1-2, escriva2022distinctnand pages 5-6)
- **Do not universalize strain-specific genes.** `fucP`, `pduCDE`, `ntrC`, Hbp, and individual SWEET paralogues require organism- and sequence-specific grounding.
- **Do not curate `pduCDE → mutualism` directly.** Its value is conditional: it is burdensome without 1,2-propanediol and beneficial when substrate-producing partners are present. (cheng2020ecologicalimportanceof pages 13-15)
- **Do not label all host-associated microbiota as mutualists.** A host habitat may benefit microbes while some microbes are neutral or harmful to the host.
- **Do not treat host behavioral change as necessarily beneficial.** In the fly model, altered protein appetite is mechanistically demonstrated, but whether it increases host fitness depends on diet and outcome; reproduction should be represented separately. (henriques2020metaboliccrossfeedingin pages 1-2)
- **Do not treat all mycorrhizae as constitutively mutualistic.** Fertilization, severe N limitation, developmental stage, and genotype mismatch can produce weak, neutral, or parasitic outcomes. (pena2024mycorrhizalsymbiosisand pages 1-3)
- **Avoid unverified CURIEs.** Specialized interfaces such as peri-arbuscular space and hyphosphere, operons such as `pduCDE`, and broad metabolite classes should remain label-only until checked against the target ontology release.
- **Separate natural from engineered mutualism.** The *R. palustris* NH₄⁺ donor was engineered; its edge is experimentally strong but should not be represented as a universal wild-type phenotype. (lasarre2020covertcrossfeedingrevealed pages 1-2)
- **Mark review-derived mechanistic edges as secondary evidence.** Where feasible, follow the 2023–2024 reviews to their primary perturbational studies before final YAML acceptance.

## DOI-first bibliography

1. **10.1038/s41579-024-01073-7** — Duan S. et al. “Cross-kingdom nutrient exchange in the plant-arbuscular mycorrhizal fungus-bacterium continuum.” *Nature Reviews Microbiology* 22:773–790. Published July 2024. [https://doi.org/10.1038/s41579-024-01073-7](https://doi.org/10.1038/s41579-024-01073-7). (duan2024crosskingdomnutrientexchange pages 3-4)
2. **10.1007/s00253-024-13298-w** — Pena R., Tibbett M. “Mycorrhizal symbiosis and the nitrogen nutrition of forest trees.” *Applied Microbiology and Biotechnology* 108:461. Published online 9 September 2024. [https://doi.org/10.1007/s00253-024-13298-w](https://doi.org/10.1007/s00253-024-13298-w). (pena2024mycorrhizalsymbiosisand pages 1-3)
3. **10.1016/j.chom.2023.03.016** — Culp E.J., Goodman A.L. “Cross-feeding in the gut microbiome: ecology and mechanisms.” *Cell Host & Microbe* 31:485–499. Published April 2023. [https://doi.org/10.1016/j.chom.2023.03.016](https://doi.org/10.1016/j.chom.2023.03.016). (culp2023crossfeedinginthe pages 15-17, culp2023crossfeedinginthe pages 1-2)
4. **10.1038/s43705-022-00155-y** — Giri S. et al. “Prevalent emergence of reciprocity among cross-feeding bacteria.” *ISME Communications*. Accepted 5 July 2022; published August 2022. [https://doi.org/10.1038/s43705-022-00155-y](https://doi.org/10.1038/s43705-022-00155-y). (giri2022prevalentemergenceof pages 1-2)
5. **10.1128/msystems.01484-21** — Pérez Escriva P., Fuhrer T., Sauer U. “Distinct N and C cross-feeding networks in a synthetic mouse gut consortium.” *mSystems*. Published April 2022. [https://doi.org/10.1128/msystems.01484-21](https://doi.org/10.1128/msystems.01484-21). (escriva2022distinctnand pages 1-2, escriva2022distinctnand pages 5-6)
6. **10.1128/AEM.00190-20** — Cheng C.C. et al. “Ecological importance of cross-feeding of the intermediate metabolite 1,2-propanediol between bacterial gut symbionts.” *Applied and Environmental Microbiology* 86. Published May 2020. [https://doi.org/10.1128/AEM.00190-20](https://doi.org/10.1128/AEM.00190-20). (cheng2020ecologicalimportanceof pages 13-15)
7. **10.1038/s41467-020-18049-9** — Henriques S.F. et al. “Metabolic cross-feeding in imbalanced diets allows gut microbes to improve reproduction and alter host behaviour.” *Nature Communications* 11:4236. Published August 2020. [https://doi.org/10.1038/s41467-020-18049-9](https://doi.org/10.1038/s41467-020-18049-9). (henriques2020metaboliccrossfeedingin pages 1-2)
8. **10.1128/AEM.00543-20** — LaSarre B. et al. “Covert cross-feeding revealed by genome-wide analysis of fitness determinants in a synthetic bacterial mutualism.” *Applied and Environmental Microbiology* 86:e00543-20. Published 17 June 2020. [https://doi.org/10.1128/AEM.00543-20](https://doi.org/10.1128/AEM.00543-20). (lasarre2020covertcrossfeedingrevealed pages 1-2)
9. **10.3389/fmicb.2021.780469** — Mataigne V. et al. “Microbial systems ecology to understand cross-feeding in microbiomes.” *Frontiers in Microbiology* 12. Published December 2021. [https://doi.org/10.3389/fmicb.2021.780469](https://doi.org/10.3389/fmicb.2021.780469). (mataigne2021microbialsystemsecology pages 4-6)
10. **10.1073/pnas.1218525110** — McFall-Ngai M. et al. “Animals in a bacterial world, a new imperative for the life sciences.” *PNAS* 110:3229–3236. Published February 2013. [https://doi.org/10.1073/pnas.1218525110](https://doi.org/10.1073/pnas.1218525110).
11. **10.1126/science.1104816** — Bäckhed F. et al. “Host-bacterial mutualism in the human intestine.” *Science* 307:1915–1920. Published March 2005. [https://doi.org/10.1126/science.1104816](https://doi.org/10.1126/science.1104816).

References

1. (culp2023crossfeedinginthe pages 2-4): Elizabeth J. Culp and Andrew L. Goodman. Cross-feeding in the gut microbiome: ecology and mechanisms. Cell host & microbe, 31 4:485-499, Apr 2023. URL: https://doi.org/10.1016/j.chom.2023.03.016, doi:10.1016/j.chom.2023.03.016. This article has 566 citations and is from a highest quality peer-reviewed journal.

2. (culp2023crossfeedinginthe pages 1-2): Elizabeth J. Culp and Andrew L. Goodman. Cross-feeding in the gut microbiome: ecology and mechanisms. Cell host & microbe, 31 4:485-499, Apr 2023. URL: https://doi.org/10.1016/j.chom.2023.03.016, doi:10.1016/j.chom.2023.03.016. This article has 566 citations and is from a highest quality peer-reviewed journal.

3. (pena2024mycorrhizalsymbiosisand pages 1-3): Rodica Pena and Mark Tibbett. Mycorrhizal symbiosis and the nitrogen nutrition of forest trees. Applied Microbiology and Biotechnology, Sep 2024. URL: https://doi.org/10.1007/s00253-024-13298-w, doi:10.1007/s00253-024-13298-w. This article has 55 citations and is from a domain leading peer-reviewed journal.

4. (culp2023crossfeedinginthe pages 15-17): Elizabeth J. Culp and Andrew L. Goodman. Cross-feeding in the gut microbiome: ecology and mechanisms. Cell host & microbe, 31 4:485-499, Apr 2023. URL: https://doi.org/10.1016/j.chom.2023.03.016, doi:10.1016/j.chom.2023.03.016. This article has 566 citations and is from a highest quality peer-reviewed journal.

5. (culp2023crossfeedinginthe pages 23-26): Elizabeth J. Culp and Andrew L. Goodman. Cross-feeding in the gut microbiome: ecology and mechanisms. Cell host & microbe, 31 4:485-499, Apr 2023. URL: https://doi.org/10.1016/j.chom.2023.03.016, doi:10.1016/j.chom.2023.03.016. This article has 566 citations and is from a highest quality peer-reviewed journal.

6. (giri2022prevalentemergenceof pages 1-2): Samir Giri, Ghada Yousif, Shraddha Shitut, Leonardo Oña, and Christian Kost. Prevalent emergence of reciprocity among cross-feeding bacteria. ISME Communications, Aug 2022. URL: https://doi.org/10.1038/s43705-022-00155-y, doi:10.1038/s43705-022-00155-y. This article has 41 citations and is from a peer-reviewed journal.

7. (giri2022prevalentemergenceof pages 2-3): Samir Giri, Ghada Yousif, Shraddha Shitut, Leonardo Oña, and Christian Kost. Prevalent emergence of reciprocity among cross-feeding bacteria. ISME Communications, Aug 2022. URL: https://doi.org/10.1038/s43705-022-00155-y, doi:10.1038/s43705-022-00155-y. This article has 41 citations and is from a peer-reviewed journal.

8. (cheng2020ecologicalimportanceof pages 13-15): Christopher C. Cheng, Rebbeca M. Duar, Xiaoxi Lin, Maria Elisa Perez-Munoz, Stephanie Tollenaar, Jee-Hwan Oh, Jan-Peter van Pijkeren, Fuyong Li, Douwe van Sinderen, Michael G. Gänzle, and Jens Walter. Ecological importance of cross-feeding of the intermediate metabolite 1,2-propanediol between bacterial gut symbionts. May 2020. URL: https://doi.org/10.1128/aem.00190-20, doi:10.1128/aem.00190-20. This article has 80 citations and is from a peer-reviewed journal.

9. (lasarre2020covertcrossfeedingrevealed pages 1-2): Breah LaSarre, Adam M. Deutschbauer, Crystal E. Love, and James B. McKinlay. Covert cross-feeding revealed by genome-wide analysis of fitness determinants in a synthetic bacterial mutualism. Jun 2020. URL: https://doi.org/10.1128/aem.00543-20, doi:10.1128/aem.00543-20. This article has 32 citations and is from a peer-reviewed journal.

10. (henriques2020metaboliccrossfeedingin pages 1-2): Sílvia F. Henriques, Darshan B. Dhakan, Lúcia Serra, Ana Patrícia Francisco, Zita Carvalho-Santos, Célia Baltazar, Ana Paula Elias, Margarida Anjos, Tong Zhang, Oliver D. K. Maddocks, and Carlos Ribeiro. Metabolic cross-feeding in imbalanced diets allows gut microbes to improve reproduction and alter host behaviour. Nature Communications, Aug 2020. URL: https://doi.org/10.1038/s41467-020-18049-9, doi:10.1038/s41467-020-18049-9. This article has 167 citations and is from a highest quality peer-reviewed journal.

11. (duan2024crosskingdomnutrientexchange pages 3-4): Shilong Duan, Gu Feng, Erik Limpens, Paola Bonfante, Xianan Xie, and Lin Zhang. Cross-kingdom nutrient exchange in the plant-arbuscular mycorrhizal fungus-bacterium continuum. Nature reviews. Microbiology, 22:773-790, Jul 2024. URL: https://doi.org/10.1038/s41579-024-01073-7, doi:10.1038/s41579-024-01073-7. This article has 264 citations.

12. (escriva2022distinctnand pages 1-2): Pau Pérez Escriva, Tobias Fuhrer, and Uwe Sauer. Distinct n and c cross-feeding networks in a synthetic mouse gut consortium. Apr 2022. URL: https://doi.org/10.1128/msystems.01484-21, doi:10.1128/msystems.01484-21. This article has 39 citations and is from a peer-reviewed journal.

13. (escriva2022distinctnand pages 5-6): Pau Pérez Escriva, Tobias Fuhrer, and Uwe Sauer. Distinct n and c cross-feeding networks in a synthetic mouse gut consortium. Apr 2022. URL: https://doi.org/10.1128/msystems.01484-21, doi:10.1128/msystems.01484-21. This article has 39 citations and is from a peer-reviewed journal.

14. (mataigne2021microbialsystemsecology pages 4-6): Victor Mataigne, Nathan Vannier, Philippe Vandenkoornhuyse, and Stéphane Hacquard. Microbial systems ecology to understand cross-feeding in microbiomes. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.780469, doi:10.3389/fmicb.2021.780469. This article has 71 citations and is from a peer-reviewed journal.