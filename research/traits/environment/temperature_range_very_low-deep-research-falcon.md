---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:38:30.124586'
end_time: '2026-06-18T02:52:57.312932'
duration_seconds: 867.19
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range very low
  trait_identifier: METPO:1000448
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_very_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which growth extends to ambient temperatures\
    \ at or below approximately 10 \xB0C, characteristic of psychrophilic growth ranges."
  parent_traits: METPO:1000306
  synonyms: Psychrophile, TR_<=10
  evidence_summary: 'DOI:10.1038/sj.embor.7400662: growing well at temperatures around
    the freezing point of water (Psychrophile review supports growth at very low temperatures
    as the psychrophilic range.)'
  causal_graph_summary: 'temperature_range_very_low_psychrophile: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range very low
- **METPO identifier:** METPO:1000448
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which growth extends to ambient temperatures at or below approximately 10 °C, characteristic of psychrophilic growth ranges.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, TR_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic range.)
- **Existing causal graph summary:** temperature_range_very_low_psychrophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_very_low.yaml`.

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
- **Trait label:** temperature range very low
- **METPO identifier:** METPO:1000448
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which growth extends to ambient temperatures at or below approximately 10 °C, characteristic of psychrophilic growth ranges.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, TR_<=10
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: growing well at temperatures around the freezing point of water (Psychrophile review supports growth at very low temperatures as the psychrophilic range.)
- **Existing causal graph summary:** temperature_range_very_low_psychrophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_very_low.yaml`.

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


## Curation-focused research report: METPO:1000448 “temperature range very low” (psychrophilic growth; TR_<=10)

### 0) Scope summary (curation intent)
The METPO trait **temperature range very low** represents the **capacity for active growth at ambient temperatures at or below ~10 °C**, consistent with *psychrophilic* growth ranges. Recent reviews emphasize that psychrophily is not merely survival: it implies **sustained cellular function and growth** under low thermal energy and high viscosity, requiring coordinated changes in membranes, proteins, nucleic acids, extracellular matrices, and stress-response systems. (ramon2023ageneraloverview pages 1-2, damico2006psychrophilicmicroorganismschallenges pages 1-2)

### 1) Trait scope, key concepts, and boundary cases

#### 1.1 Definitions and thresholds (operationalizable for curation)
* **Psychrophiles**: defined in a recent synthesis as organisms that **can grow at 0 °C**, have **optimum growth temperature near ~15 °C**, and **do not grow at 20 °C**. (ramon2023ageneraloverview pages 1-2)
* **Psychrotolerant / psychrotrophs**: can **grow at ~4 °C** but have **optimal growth temperatures above 20 °C**, distinguishing them from true psychrophiles by *Topt* and *Tmax*. (ramon2023ageneraloverview pages 1-2)
* **Kinetic boundary framing**: one review states psychrophiles “**maintain linearity down to 0 °C**,” while psychrotolerants show linearity only between **~5–10 °C** (mesophiles ~20 °C), providing an assay-adjacent criterion. (purwar2024adaptationsofpsychrophilic pages 8-10)
* Foundational framing (EMBO Reports): uses “psychrophiles” to denote microorganisms “**growing well at temperatures around the freezing point of water**,” providing exemplar data (e.g., *Moritella profunda* maximal growth at **2 °C** and maximum growth temperature **12 °C**) and noting a continuum with psychrotolerants depending on optimum growth temperature. (damico2006psychrophilicmicroorganismschallenges pages 1-2)

#### 1.2 Boundary cases and nearby traits (what not to over-include)
* **Psychrotolerance vs psychrophily**: organisms that merely *grow slowly* at 4–10 °C but have *Topt* in mesophilic range should be captured by psychrotolerant traits rather than METPO:1000448. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10)
* **Freezing survival without growth** (e.g., persistence during freeze–thaw) should not be conflated with this trait unless growth is shown at ≤10 °C; many protective mechanisms (EPS/AFPs/osmolytes) support both survival and growth but must be tied to growth phenotypes for strongest curation. (ramasamy2023comprehensiveinsightson pages 3-4, ramon2023ageneraloverview pages 1-2)

### 2) Current understanding: mechanistic architecture for very-low-temperature growth
Psychrophilic growth emerges from a *multi-layer causal program* addressing cold-induced failures: membrane rigidification and transport limitations; slowed transcription/translation; protein misfolding/cold-denaturation; intracellular and extracellular ice damage; and elevated oxidative stress and DNA damage. (damico2006psychrophilicmicroorganismschallenges pages 1-2, ramon2023ageneraloverview pages 1-2)

A concise visual summary of cold-adaptation mechanisms suitable for curator review is available as a table from Ramón et al. 2023. (ramon2023ageneraloverview media 025060c3)

### 3) Candidate causal-graph nodes (grouped) 
Candidate nodes for a TraitMech graph are provided below; a machine-curation-friendly list with suggested grounding is included as an embedded artifact.

| Node label | Node type | Suggested grounding | Notes on relevance to psychrophilic growth <=10°C | Key supporting citation IDs |
|---|---|---|---|---|
| low temperature <=10 °C | environmental factor | label-only | Primary external condition defining the trait; cold stress drives all downstream adaptations. | (ramon2023ageneraloverview pages 1-2, damico2006psychrophilicmicroorganismschallenges pages 1-2) |
| sea ice / frozen habitat | environmental factor | ENVO:00000186 | Common psychrophile habitat associated with freezing, salinity, and ice-crystal stress. | (ramasamy2023comprehensiveinsightson pages 3-4, ramasamy2023comprehensiveinsightson pages 1-2) |
| membrane fluidity | cellular component | GO:0016042 | Maintenance of membrane fluidity is a central requirement for growth at very low temperature. | (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10) |
| homeoviscous adaptation | process | GO:0043487 | Lipid remodeling process that counteracts cold-induced membrane rigidification. | (ramasamy2023comprehensiveinsightson pages 2-3, ramon2023ageneraloverview pages 1-2) |
| fatty acid desaturation | process | GO:0033559 | Increased unsaturation supports membrane function at low temperature. | (purwar2024adaptationsofpsychrophilic pages 8-10, jing2024transcriptomeresponseof pages 8-10) |
| fatty acid desaturase | gene/protein family | EC:1.14.19.- | Generic desaturase family repeatedly implicated in cold adaptation. | (purwar2024adaptationsofpsychrophilic pages 8-10) |
| FAD2 omega-6 fatty acid desaturase | gene/protein family | label-only | Specific desaturase upregulated under low temperature in S. marinoi; useful exemplar node. | (jing2024transcriptomeresponseof pages 8-10) |
| branched-chain fatty acid biosynthesis | pathway/module | label-only | Shorter, branched fatty acids are associated with cold-active membrane remodeling. | (purwar2024adaptationsofpsychrophilic pages 8-10) |
| unsaturated fatty acids | metabolite/chemical | CHEBI:27208 | Increased abundance is a recurrent biochemical signature of psychrophilic membranes. | (li2024mechanismsunderlyingthe pages 5-7, purwar2024adaptationsofpsychrophilic pages 8-10) |
| cold-shock protein family (CspA-like) | gene/protein family | label-only | RNA-binding cold-acclimation proteins help resolve inhibitory nucleic-acid structures and sustain translation. | (damico2006psychrophilicmicroorganismschallenges pages 1-2, ramon2023ageneraloverview pages 1-2) |
| RNA chaperone activity | process | GO:0003729 | Functional abstraction for CSP/TRAM/RBP-mediated support of translation in the cold. | (gupta2023psychrophilesasa pages 9-10, ramon2023ageneraloverview pages 1-2) |
| TRAM-domain cold-response proteins | gene/protein family | label-only | Proposed RNA chaperones upregulated at low temperature in psychrophiles. | (gupta2023psychrophilesasa pages 9-10) |
| glycine-rich RNA-binding proteins | gene/protein family | label-only | Additional cold-induced RNA-binding factors implicated in adaptation. | (gupta2023psychrophilesasa pages 9-10) |
| protein folding | process | GO:0006457 | Cold slows folding and increases misfolding risk, requiring enhanced proteostasis. | (damico2006psychrophilicmicroorganismschallenges pages 1-2, purwar2024adaptationsofpsychrophilic pages 6-7) |
| DnaK (Hsp70 family) | gene/protein family | label-only | Frequently induced/accumulated chaperone supporting protein stability during cold growth. | (ramasamy2023comprehensiveinsightson pages 4-6, li2024mechanismsunderlyingthe pages 9-10) |
| GroEL chaperonin | gene/protein family | label-only | Core chaperone repeatedly reported in cold-adapted proteostasis responses. | (damico2006psychrophilicmicroorganismschallenges pages 1-2, li2024mechanismsunderlyingthe pages 4-5) |
| GroES cochaperonin | gene/protein family | label-only | Acts with GroEL in cold-shock folding protection. | (purwar2024adaptationsofpsychrophilic pages 6-7) |
| Clp protease/chaperone system | gene/protein family | label-only | Supports protein quality control under low-temperature stress. | (purwar2024adaptationsofpsychrophilic pages 6-7) |
| trigger factor (TF) | gene/protein family | label-only | Ribosome-associated chaperone listed among cold-upregulated folding factors. | (purwar2024adaptationsofpsychrophilic pages 6-7) |
| extracellular polymeric substances (EPS) | metabolite/chemical | GO:0045226 | Protective extracellular matrix with cryoprotective and ice-associated functions. | (ramasamy2023comprehensiveinsightson pages 3-4, ramon2023ageneraloverview pages 1-2) |
| biofilm formation | process | GO:0042710 | Increased at low temperature in RCBS9; may improve protection and nutrient capture. | (ramasamy2023comprehensiveinsightson pages 3-4, li2024mechanismsunderlyingthe pages 5-7) |
| c-di-GMP synthase / diguanylate cyclase | gene/protein family | EC:2.7.7.65 | Regulatory node linked to enhanced biofilm-related responses under cold stress. | (li2024mechanismsunderlyingthe pages 7-9) |
| antifreeze proteins (AFP) | gene/protein family | label-only | Bind ice, inhibit crystal growth, and produce thermal hysteresis; major cryoprotective mechanism. | (ramasamy2023comprehensiveinsightson pages 3-4, purwar2024adaptationsofpsychrophilic pages 6-7) |
| ice-binding proteins (IBP) | gene/protein family | label-only | Broad family of ice-active proteins that protect against recrystallization and freezing damage. | (purwar2024adaptationsofpsychrophilic pages 6-7) |
| DUF3494 ice-binding domain proteins | gene/protein family | label-only | Domain-level candidate for type I IBPs; useful when species-specific protein IDs are unavailable. | (purwar2024adaptationsofpsychrophilic pages 6-7) |
| trehalose | metabolite/chemical | CHEBI:16589 | Compatible solute and cryoprotectant reported among cold-protective osmolytes. | (ramasamy2023comprehensiveinsightson pages 3-4) |
| glycine betaine | metabolite/chemical | CHEBI:17750 | Compatible solute that stabilizes proteins/membranes and lowers freezing-related damage. | (ramasamy2023comprehensiveinsightson pages 3-4) |
| glycerol | metabolite/chemical | CHEBI:17522 | Classical cryoprotective solute mentioned among psychrophile osmolytes. | (ramasamy2023comprehensiveinsightson pages 3-4) |
| compatible solute biosynthetic process | process | GO:0006972 | Higher-level node covering osmolyte accumulation for freezing and osmotic protection. | (ramasamy2023comprehensiveinsightson pages 3-4, li2024mechanismsunderlyingthe pages 1-3) |
| superoxide dismutase (SOD) | gene/protein family | EC:1.15.1.1 | Strongly implicated in detoxifying elevated ROS during low-temperature growth. | (li2024mechanismsunderlyingthe pages 9-10, li2024mechanismsunderlyingthe pages 7-9) |
| peroxidase system (PX/GPX/Prx) | gene/protein family | EC:1.11.1.- | Alternative peroxide-scavenging enzymes induced in cold adaptation. | (li2024mechanismsunderlyingthe pages 9-10, li2024mechanismsunderlyingthe pages 7-9) |
| oxidative stress response | process | GO:0006979 | Cold-associated ROS increase necessitates antioxidant defenses. | (li2024mechanismsunderlyingthe pages 1-3, li2024mechanismsunderlyingthe pages 4-5) |
| carotenoids | metabolite/chemical | CHEBI:23044 | Pigments acting as antioxidants, cryoprotectants, and membrane stabilizers. | (ramasamy2023comprehensiveinsightson pages 3-4, li2024mechanismsunderlyingthe pages 4-5) |
| DNA repair | process | GO:0006281 | Repair systems counter oxidative and cold-associated DNA damage. | (li2024mechanismsunderlyingthe pages 1-3, li2024mechanismsunderlyingthe pages 7-9) |
| RecA-family recombination proteins | gene/protein family | label-only | Central SOS/recombination proteins induced under low temperature. | (li2024mechanismsunderlyingthe pages 7-9) |
| LexA repressor | gene/protein family | label-only | SOS regulator upregulated in RCBS9 cold response datasets. | (li2024mechanismsunderlyingthe pages 9-10, li2024mechanismsunderlyingthe pages 7-9) |
| ABC transporters | gene/protein family | GO:0043190 | Upregulated transport capacity likely compensates for cold-limited uptake and membrane effects. | (li2024mechanismsunderlyingthe pages 5-7, li2024mechanismsunderlyingthe pages 9-10) |
| glycolysis | pathway/module | GO:0006096 | Often upregulated during low-temperature metabolic rewiring. | (purwar2024adaptationsofpsychrophilic pages 8-10) |
| beta-oxidation | pathway/module | GO:0006635 | Reported as upregulated, supporting energy generation and fatty-acid recycling in the cold. | (li2024mechanismsunderlyingthe pages 9-10, purwar2024adaptationsofpsychrophilic pages 8-10) |
| tricarboxylic acid cycle | pathway/module | GO:0006099 | Often downregulated under low-temperature adaptation, so useful as a negatively shifted pathway node. | (purwar2024adaptationsofpsychrophilic pages 8-10) |
| electron transport chain | pathway/module | GO:0022900 | Frequently reduced in cold-adaptation metabolic rewiring. | (purwar2024adaptationsofpsychrophilic pages 8-10) |
| ribosome / translation machinery | pathway/module | GO:0006412 | Translation capacity and ribosome-related genes are a major cold-responsive module. | (jing2024transcriptomeresponseof pages 4-7, jing2024transcriptomeresponseof pages 2-4) |
| porphyrin and chlorophyll metabolism | pathway/module | label-only | Upregulated in the 12°C diatom transcriptome; relevant for phototrophic cold adaptation. | (jing2024transcriptomeresponseof pages 4-7, jing2024transcriptomeresponseof pages 8-10) |


*Table: This table lists candidate nodes for a TraitMech-style causal graph of very-low-temperature growth, grouped across environmental, molecular, metabolic, and cellular levels. It is useful for curation because it pairs each proposed node with suggested ontology grounding and the evidence IDs supporting inclusion.*

### 4) Evidence-backed candidate causal edges (triples)
The following edges are proposed as *curation candidates* for `temperature_range_very_low` graphs. They are mechanistically plausible and explicitly supported by the cited sources; edges that are species- or study-specific are noted accordingly.

| Edge (subject–predicate–object) | Mechanism/Interpretation | Evidence snippet (short quote or close paraphrase) | Source (DOI, year) | Citation ID |
|---|---|---|---|---|
| low temperature → alters physical state of membrane → two-component cold signaling | Cold is sensed through membrane rigidification/liquid-crystalline changes that trigger regulatory responses. DesK/DesR is a canonical example, but broad review evidence is strongest at pathway level. | “Cold sensing occurs via changes in the liquid-crystalline state of membranes that activate two-component signaling systems.” | 10.1007/s42770-023-01057-4, 2023 | (ramon2023ageneraloverview pages 1-2) |
| membrane fatty-acid desaturation → increases → membrane fluidity at low temperature | Homeoviscous adaptation is a core mechanism enabling membranes to remain functional in the cold. | “Cells adapt membrane composition (increasing double bonds in lipids…) to maintain fluidity and function.” | 10.1007/s42770-023-01057-4, 2023 | (ramon2023ageneraloverview pages 1-2) |
| fatty-acid synthesis/desaturation genes → support → psychrophilic growth | Upregulation of lipid remodeling genes is repeatedly linked to low-temperature survival and growth. | “fatty acid synthesis, fatty acid desaturation, and production of branched-chain fatty acids are upregulated in cold-adapted [microorganisms].” | 10.37256/amtt.5220244537, 2024 | (purwar2024adaptationsofpsychrophilic pages 8-10) |
| DesK histidine kinase → activates → low-temperature response regulons | Taxon-specific mechanistic support from Rhodococcus indicates membrane-linked cold signaling contributes to adaptation. | “cold activates the membrane histidine kinase DesK” | 10.3389/fmicb.2024.1465627, 2024 | (li2024mechanismsunderlyingthe pages 7-9) |
| cold-shock proteins (CspA-family) → act on → mRNA/RNA secondary structure | RNA chaperoning helps maintain translation under cold-induced stabilization of nucleic acid structures. | “cold-shock proteins (CSPs) [act] on mRNAs”; “increased levels of nucleic-acid-binding proteins (CspA-related proteins)” | 10.1007/s42770-023-01057-4, 2023; 10.1038/sj.embor.7400662, 2006 | (ramon2023ageneraloverview pages 1-2, damico2006psychrophilicmicroorganismschallenges pages 1-2) |
| TRAM-domain and glycine-rich RNA-binding proteins → promote → cold adaptation | Additional RNA chaperones likely complement CSPs in preserving translation at very low temperature. | “TRAM-domain ‘Ctr’ proteins and glycine-rich RNA-binding proteins… are upregulated at low temperature and assist cold adaptation.” | 10.52679/tabcj.2023.0006, 2023 | (gupta2023psychrophilesasa pages 9-10) |
| DnaK/GroEL/GroES/trigger factor/Clp proteases → preserve → protein folding and proteostasis in the cold | Cold weakens folding kinetics and increases misfolding risk; constitutive or induced chaperone systems counter this. | “Specific chaperones (Clp proteases, GroEL, DnaK, GroES, TF) are upregulated during cold shock”; psychrophiles “constitutively synthesize molecular chaperones.” | 10.37256/amtt.5220244537, 2024; 10.3389/fmicb.2023.1197797, 2023 | (purwar2024adaptationsofpsychrophilic pages 6-7, ramasamy2023comprehensiveinsightson pages 4-6) |
| compatible solutes (glycine betaine/trehalose/glycerol) → stabilize → proteins and membranes | Osmolytes lower freezing damage and protect macromolecules, supporting growth near/below 0 °C. | “Accumulation of compatible osmolytes (glycine betaine, trehalose, glycerol, etc.) prevents cell shrinkage, lowers cytoplasmic freezing point… and stabilizes proteins and membranes.” | 10.3389/fmicb.2023.1197797, 2023 | (ramasamy2023comprehensiveinsightson pages 3-4) |
| extracellular polymeric substances (EPS) → inhibit/reduce → ice damage around cells | EPS acts as cryoprotective matrix and habitat stabilizer, often with ice-binding/IRI activity. | “EPS mediate adhesion, surface protection and biofilm formation and have ice-binding and ice recrystallization inhibition activities.” | 10.3389/fmicb.2023.1197797, 2023 | (ramasamy2023comprehensiveinsightson pages 3-4) |
| low temperature → increases → biofilm production | Biofilms can enhance nutrient capture and local protection in cold environments. | “relative biofilm content is higher at 10°C… suggesting biofilm production as a low-temperature/nutrient-capture strategy.” | 10.3389/fmicb.2024.1465627, 2024 | (li2024mechanismsunderlyingthe pages 5-7) |
| ice-binding/antifreeze proteins → inhibit → ice-crystal growth/recrystallization | AFPs/IBPs directly prevent damaging ice growth and are major psychrophile cold-protection factors. | “AFPs bind ice, inhibit ice-crystal growth, produce thermal hysteresis… and show IRI activity.” | 10.3389/fmicb.2023.1197797, 2023 | (ramasamy2023comprehensiveinsightson pages 3-4) |
| DUF3494-containing type I IBPs → mediate → ice binding | Domain-level candidate node for curation when specific gene products are not yet pinned to a species-neutral node. | “Type I IBPs often contain the DUF3494 domain and may have spread by horizontal gene transfer.” | 10.37256/amtt.5220244537, 2024 | (purwar2024adaptationsofpsychrophilic pages 6-7) |
| Marinomonas primoryensis multidomain AFP → binds → ice surfaces | Strong taxon-specific example of AFP-mediated cold adaptation; useful as exemplar but not universal. | “a multidomain ice-adhesion AFP was identified in Marinomonas primoryensis” | 10.3389/fmicb.2023.1197797, 2023 | (ramasamy2023comprehensiveinsightson pages 3-4) |
| superoxide dismutase/peroxidases/glutathione systems → reduce → cold-associated oxidative stress | ROS detoxification is repeatedly induced because low temperature increases oxidative stress burden. | “all SOD genes are upregulated; PX, GPX and Prx are induced”; antioxidants are “key to [the] ability to adapt to low temperature.” | 10.3389/fmicb.2024.1465627, 2024 | (li2024mechanismsunderlyingthe pages 7-9, li2024mechanismsunderlyingthe pages 1-3) |
| DNA repair/SOS genes (RecA/RecC/RecF/RecG/RecX/LexA/dinB) → repair → cold-induced DNA damage | Cold stress is associated with oxidative DNA damage, and repair systems are upregulated to maintain viability. | “DNA repair and SOS/recombination genes (RecC, RecF, RecG, RecX, LexA, dinB, etc.) are highly upregulated.” | 10.3389/fmicb.2024.1465627, 2024 | (li2024mechanismsunderlyingthe pages 9-10) |
| low temperature → upregulates → ABC transporters and other uptake systems | Increased transporter capacity likely compensates for reduced membrane permeability and supports substrate acquisition in the cold. | “GO/KEGG show upregulation of transporters (including ABC transporters)… interpreted as increased energetic and transporter demand.” | 10.3389/fmicb.2024.1465627, 2024 | (li2024mechanismsunderlyingthe pages 5-7) |
| low temperature → upregulates → glycolysis and beta-oxidation | Central metabolism is rewired toward pathways that better support low-temperature survival and energy balance. | “glycolysis and beta-oxidation are upregulated, TCA cycle and electron transport are downregulated.” | 10.37256/amtt.5220244537, 2024 | (purwar2024adaptationsofpsychrophilic pages 8-10) |
| low temperature → downregulates → TCA cycle/electron transport/ribosome-heavy biosynthesis | Reduced high-cost biosynthesis and respiration are part of adaptive energy conservation under cold stress. | “TCA cycle and electron transport are downregulated”; RCBS9 shows “downregulation of ribosomal/biomolecule synthesis genes.” | 10.37256/amtt.5220244537, 2024; 10.3389/fmicb.2024.1465627, 2024 | (purwar2024adaptationsofpsychrophilic pages 8-10, li2024mechanismsunderlyingthe pages 5-7) |


*Table: This table compiles candidate causal edges for curating the trait ‘temperature range very low’ (psychrophilic growth at or below ~10 °C). It emphasizes mechanisms with direct literature support and flags where evidence is broad, taxon-specific, or pathway-level rather than universally gene-specific.*

### 5) Recent developments (2023–2024 prioritized)

#### 5.1 Omics-enabled mechanistic refinement
* **Transcriptomics in a cold-stressed bacterium (10 °C vs 25 °C)**: *Rhodococcus* sp. RCBS9 shows broad differential expression at 10 °C (reported **~2,012 genes upregulated** and **~1,926 downregulated**), with functional enrichment supporting increased transporter and energy-demand modules and reduced ribosome-heavy biosynthesis, consistent with energy-conserving cold adaptation. (li2024mechanismsunderlyingthe pages 5-7)
* **Physiology + transcriptomics + targeted validation pipeline**: the same study measured cold-associated oxidative stress and membrane changes, and identified specific candidate cold-survival genes (e.g., sHsp, DPS, GroEL, USPs, Cu/Zn-SOD) for cloning and expression testing—supporting a workflow for moving from association to causality, even when not all functional results are shown in the excerpt. (li2024mechanismsunderlyingthe pages 4-5, li2024mechanismsunderlyingthe pages 1-3)
* **Eukaryotic phototroph transcriptomics at 12 °C**: *Skeletonema marinoi* RNA-seq identified **573 DEGs** (with **414 upregulated** at low temperature) and strong induction of **ribosome/translation**, **fatty-acid metabolism** (including an upregulated **FAD2 omega-6 desaturase**), and **porphyrin/chlorophyll metabolism** genes—demonstrating that cold-growth programs extend beyond bacteria and include photosynthetic pigment/translation modules. (jing2024transcriptomeresponseof pages 1-2, jing2024transcriptomeresponseof pages 2-4, jing2024transcriptomeresponseof pages 8-10)

#### 5.2 Expanded mechanistic repertoire emphasized in recent reviews
Across 2023–2024 reviews, the most consistently emphasized modules are:
* **Membrane lipid remodeling/homeoviscous adaptation** (unsaturation; branching; chain length changes; lipid A remodeling; hopanoids/pigments). (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10)
* **RNA-level cold acclimation** via cold shock proteins and other RNA-binding proteins. (ramon2023ageneraloverview pages 1-2, gupta2023psychrophilesasa pages 9-10)
* **Proteostasis systems** (DnaK/GroEL/Clp/trigger factor) and constitutive chaperone capacity. (ramasamy2023comprehensiveinsightson pages 4-6, purwar2024adaptationsofpsychrophilic pages 6-7)
* **Ice-active systems** (AFPs/IBPs, EPS with IRI activity) and **compatible solutes** that stabilize proteins and membranes and reduce freezing damage. (ramasamy2023comprehensiveinsightson pages 3-4)
* **Oxidative stress management and DNA repair** as central to cold growth rather than peripheral stress responses. (li2024mechanismsunderlyingthe pages 7-9, li2024mechanismsunderlyingthe pages 9-10)

### 6) Applications and real-world implementations

#### 6.1 Cold-active enzymes (“psychrozymes”) in industry
Psychrophile enzymes are repeatedly highlighted for **high catalytic efficiency at low temperature** (often paired with **lower thermal stability**), enabling:
* **Food processing**: low-temperature lactose hydrolysis (β-galactosidases), pectin degradation, and other quality-preserving steps. (ramasamy2023comprehensiveinsightson pages 6-7)
* **Detergents**: cold-active proteases/lipases enabling effective washing at lower temperatures (energy savings). (ramasamy2023comprehensiveinsightson pages 6-7)
* **Bioremediation**: cold-active hydrolases aiding hydrocarbon degradation where mesophilic enzymes are ineffective. (ramasamy2023comprehensiveinsightson pages 6-7)
* **Molecular biology reagents**: cold-adapted enzymes active near **~4 °C** (e.g., DNA ligases, uracil DNA N-glycosylases) enabling low-temperature workflows. (ramasamy2023comprehensiveinsightson pages 6-7)

#### 6.2 Cryoprotection and ice-management technologies
Ice-binding/antifreeze proteins and related cryoprotectants are increasingly implemented via recombinant production; a food-cryopreservation review summarizes that AFPs/IBPs **deform ice crystals, inhibit recrystallization, and generate thermal hysteresis**, and notes recombinant expression feasibility in microbial hosts (with caveats such as inclusion bodies in prokaryotic systems). (wu2025applicationofantifreeze pages 5-6)

#### 6.3 Environmental and climate-relevant applications
A 2023 Antarctic bacteria review ties psychrophile mechanisms to applied domains including biodegradation/bioremediation and cold-active biocatalysis, and explicitly promotes **omics and machine learning** as emerging approaches to discover and engineer cold-adapted molecules for a sustainable bioeconomy. (ramasamy2023comprehensiveinsightson pages 1-2, ramasamy2023comprehensiveinsightson pages 2-3)

### 7) Expert opinions and analysis (authoritative synthesis positions)
* Ramón et al. (2023) emphasize cold adaptation as **multifactorial**, highlighting membranes as central sensing/functional platforms and describing coupled regulation (DNA supercoiling/promoter signatures/CSP action) that coordinates metabolic and structural change—consistent with a *causal graph* framing rather than single-gene determinism. (ramon2023ageneraloverview pages 1-2)
* D’Amico et al. (EMBO Reports) argue that **increased protein flexibility** is a dominant evolutionary solution in psychrophiles, detailing recurring structural changes (e.g., fewer ion pairs/hydrogen bonds, altered core packing) that raise catalytic activity at low temperature (often trading off substrate affinity), reinforcing “enzyme flexibility → catalytic efficiency at low T → growth near freezing” as a key mechanistic axis. (damico2006psychrophilicmicroorganismschallenges pages 3-4)

### 8) Recent statistics and quantitative data points suitable for curation notes
* **Thermal niche thresholds**: psychrophiles grow at **0 °C**, *Topt* ~**15 °C**, and fail at **20 °C** (contrasting with psychrotolerants with *Topt* >20 °C). (ramon2023ageneraloverview pages 1-2)
* **Example psychrophile Tmax**: *Moritella profunda* reported with maximum growth temperature **12 °C** and maximal growth at **2 °C**. (damico2006psychrophilicmicroorganismschallenges pages 1-2)
* **Ecological prevalence**: one review states **“Over 75% of Earth’s biosphere… [is] below 5 °C,”** motivating trait relevance for global biogeochemical cycles (note: this is a review-level estimate, not a primary measurement). (purwar2024adaptationsofpsychrophilic pages 1-3)
* **Cold transcriptome scale (diatom)**: **20,319 unigenes**, **573 DEGs** under 12 °C, and strong induction of ribosome and fatty-acid metabolism modules including **FAD2** desaturase. (jing2024transcriptomeresponseof pages 1-2, jing2024transcriptomeresponseof pages 8-10)
* **Cold physiology + membrane lipid shift (bacterium)**: at 10 °C, RCBS9 shows **increased unsaturated fatty acids**, including a specific FA species increasing **~11×**, consistent with homeoviscous adaptation (taxon- and assay-specific but mechanistically direct). (li2024mechanismsunderlyingthe pages 5-7)

### 9) Warnings / claims to treat as uncertain (do not over-curate)
* **DesK as a universal psychrophile cold sensor**: DesK is cited as cold-activated in RCBS9 context; however, DesK/DesR is not universal across taxa. Curate as **taxon-specific** (or as a representative two-component cold-sensing node) unless broader comparative evidence is added. (li2024mechanismsunderlyingthe pages 7-9)
* **Metabolic rewiring directionality** (e.g., “glycolysis up; TCA/ETC down”) is supported by reviews and at least one study context, but is expected to vary by organism, substrate, and oxygen regime. Curate as **context-dependent** edges unless linked to defined experimental conditions. (purwar2024adaptationsofpsychrophilic pages 8-10, li2024mechanismsunderlyingthe pages 5-7)
* **EPS and AFP/IBP functions**: strong evidence supports ice binding/IRI and cryoprotection, but whether these are *necessary for growth at ≤10 °C* vs primarily for *subzero survival* can be organism- and niche-specific; prioritize curation when growth phenotypes are explicitly shown under those conditions. (ramasamy2023comprehensiveinsightson pages 3-4)
* **Review-derived global statistics** (e.g., “75% of biosphere <5 °C”) should be tagged as **secondary-source estimates** rather than direct measurements. (purwar2024adaptationsofpsychrophilic pages 1-3)

---

## DOI-first bibliography (with URLs and publication dates)

1. Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology* (Jul 2023). DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2)

2. Ramasamy KP, Mahawar L, Rajasabapathy R, Rajeshwari K, Miceli C, Pucciarelli S. **Comprehensive insights on environmental adaptation strategies in Antarctic bacteria and biotechnological applications of cold adapted molecules.** *Frontiers in Microbiology* (Jun 2023). DOI: **10.3389/fmicb.2023.1197797**. https://doi.org/10.3389/fmicb.2023.1197797 (ramasamy2023comprehensiveinsightson pages 3-4)

3. Gupta V, Bhaskar P, Thoudam J, Bisht S, Sharma A, Tripathi R. **Psychrophiles as a novel and promising source of cold-adapted industrial enzymes.** *The Applied Biology & Chemistry Journal* (Jun 2023). DOI: **10.52679/tabcj.2023.0006**. https://doi.org/10.52679/tabcj.2023.0006 (gupta2023psychrophilesasa pages 9-10)

4. Purwar S, Srivastava S. **Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.** *Applied Microbiology: Theory & Technology* (Oct 2024). DOI: **10.37256/amtt.5220244537**. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 8-10)

5. Li Q, Pan H, Hao P, et al. **Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain Rhodococcus sp. RCBS9: insights from physiological and transcriptomic analyses.** *Frontiers in Microbiology* (Nov 2024). DOI: **10.3389/fmicb.2024.1465627**. https://doi.org/10.3389/fmicb.2024.1465627 (li2024mechanismsunderlyingthe pages 1-3)

6. Jing X, Zhen Y, Mi T, Yu Z, Wang Y, Wang X. **Transcriptome response of diatom Skeletonema marinoi to lower temperature.** *Marine Biology* (Apr 2024). DOI: **10.1007/s00227-024-04434-1**. https://doi.org/10.1007/s00227-024-04434-1 (jing2024transcriptomeresponseof pages 1-2)

7. D’Amico S, Collins T, Marx J‑C, Feller G, Gerday C. **Psychrophilic microorganisms: challenges for life.** *EMBO reports* (Apr 2006). DOI: **10.1038/sj.embor.7400662**. https://doi.org/10.1038/sj.embor.7400662 (damico2006psychrophilicmicroorganismschallenges pages 1-2)

8. (Application-focused, not psychrophile-specific) Wu M, Xu Q, Ding H, et al. **Application of antifreeze substances in food cryopreservation.** *Foods* (Jun 2025). DOI: **10.3390/foods14122089**. https://doi.org/10.3390/foods14122089 (wu2025applicationofantifreeze pages 5-6)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (damico2006psychrophilicmicroorganismschallenges pages 1-2): Salvino D'Amico, Tony Collins, Jean‐Claude Marx, Georges Feller, Charles Gerday, and Charles Gerday. Psychrophilic microorganisms: challenges for life. EMBO reports, 7:385-389, Apr 2006. URL: https://doi.org/10.1038/sj.embor.7400662, doi:10.1038/sj.embor.7400662. This article has 1134 citations and is from a highest quality peer-reviewed journal.

3. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

4. (ramasamy2023comprehensiveinsightson pages 3-4): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 70 citations and is from a peer-reviewed journal.

5. (ramon2023ageneraloverview media 025060c3): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

6. (ramasamy2023comprehensiveinsightson pages 1-2): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 70 citations and is from a peer-reviewed journal.

7. (ramasamy2023comprehensiveinsightson pages 2-3): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 70 citations and is from a peer-reviewed journal.

8. (jing2024transcriptomeresponseof pages 8-10): Xiaoli Jing, Yu Zhen, Tie-zhu Mi, Zhigang Yu, Yucheng Wang, and Xiaohong Wang. Transcriptome response of diatom skeletonema marinoi to lower temperature. Marine Biology, Apr 2024. URL: https://doi.org/10.1007/s00227-024-04434-1, doi:10.1007/s00227-024-04434-1. This article has 3 citations and is from a peer-reviewed journal.

9. (li2024mechanismsunderlyingthe pages 5-7): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

10. (gupta2023psychrophilesasa pages 9-10): Varsha Gupta, Pranav Bhaskar, Jeancolar Thoudam, Shiwali Bisht, Anita Sharma, and Rashmi Tripathi. Psychrophiles as a novel and promising source of cold-adapted industrial enzymes. The Applied Biology &amp; Chemistry Journal, pages 54-68, Jun 2023. URL: https://doi.org/10.52679/tabcj.2023.0006, doi:10.52679/tabcj.2023.0006. This article has 10 citations.

11. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

12. (ramasamy2023comprehensiveinsightson pages 4-6): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 70 citations and is from a peer-reviewed journal.

13. (li2024mechanismsunderlyingthe pages 9-10): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

14. (li2024mechanismsunderlyingthe pages 4-5): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

15. (li2024mechanismsunderlyingthe pages 7-9): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

16. (li2024mechanismsunderlyingthe pages 1-3): Qiannan Li, Hanyu Pan, Peng Hao, Zhenhua Ma, Xiaojun Liang, Lianyu Yang, and Yunhang Gao. Mechanisms underlying the low-temperature adaptation of 17β-estradiol-degrading bacterial strain rhodococcus sp. rcbs9: insights from physiological and transcriptomic analyses. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1465627, doi:10.3389/fmicb.2024.1465627. This article has 6 citations and is from a peer-reviewed journal.

17. (jing2024transcriptomeresponseof pages 4-7): Xiaoli Jing, Yu Zhen, Tie-zhu Mi, Zhigang Yu, Yucheng Wang, and Xiaohong Wang. Transcriptome response of diatom skeletonema marinoi to lower temperature. Marine Biology, Apr 2024. URL: https://doi.org/10.1007/s00227-024-04434-1, doi:10.1007/s00227-024-04434-1. This article has 3 citations and is from a peer-reviewed journal.

18. (jing2024transcriptomeresponseof pages 2-4): Xiaoli Jing, Yu Zhen, Tie-zhu Mi, Zhigang Yu, Yucheng Wang, and Xiaohong Wang. Transcriptome response of diatom skeletonema marinoi to lower temperature. Marine Biology, Apr 2024. URL: https://doi.org/10.1007/s00227-024-04434-1, doi:10.1007/s00227-024-04434-1. This article has 3 citations and is from a peer-reviewed journal.

19. (jing2024transcriptomeresponseof pages 1-2): Xiaoli Jing, Yu Zhen, Tie-zhu Mi, Zhigang Yu, Yucheng Wang, and Xiaohong Wang. Transcriptome response of diatom skeletonema marinoi to lower temperature. Marine Biology, Apr 2024. URL: https://doi.org/10.1007/s00227-024-04434-1, doi:10.1007/s00227-024-04434-1. This article has 3 citations and is from a peer-reviewed journal.

20. (ramasamy2023comprehensiveinsightson pages 6-7): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 70 citations and is from a peer-reviewed journal.

21. (wu2025applicationofantifreeze pages 5-6): Mengxia Wu, Qin Xu, Han Ding, Dumin Zhao, Ying Wang, and Baocai Xu. Application of antifreeze substances in food cryopreservation. Foods, 14:2089, Jun 2025. URL: https://doi.org/10.3390/foods14122089, doi:10.3390/foods14122089. This article has 6 citations.

22. (damico2006psychrophilicmicroorganismschallenges pages 3-4): Salvino D'Amico, Tony Collins, Jean‐Claude Marx, Georges Feller, Charles Gerday, and Charles Gerday. Psychrophilic microorganisms: challenges for life. EMBO reports, 7:385-389, Apr 2006. URL: https://doi.org/10.1038/sj.embor.7400662, doi:10.1038/sj.embor.7400662. This article has 1134 citations and is from a highest quality peer-reviewed journal.

23. (purwar2024adaptationsofpsychrophilic pages 1-3): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.