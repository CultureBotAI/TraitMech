---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:21:47.236482'
end_time: '2026-06-18T02:31:41.710846'
duration_seconds: 594.47
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range
  trait_identifier: METPO:1000306
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature phenotype with numerical limits that bounds the minimum
    and maximum ambient temperatures supporting growth of an organism.
  parent_traits: METPO:1000533, METPO:1000535
  synonyms: ''
  evidence_summary: 'DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of
    high temperature (Thermophile-adaptation review supports the bounded ambient-temperature
    span over which membrane, enzyme, and bioenergetic adaptations sustain growth
    as the basis of the temperature-range phenotype.) | DOI:10.1038/sj.embor.7400662:
    decreased membrane fluidity (Psychrophile review supports cold-end membrane stress
    as a lower-bound growth constraint that low-temperature tolerance must overcome.)'
  causal_graph_summary: 'temperature_range_bounded_adaptation: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range
- **METPO identifier:** METPO:1000306
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that bounds the minimum and maximum ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the bounded ambient-temperature span over which membrane, enzyme, and bioenergetic adaptations sustain growth as the basis of the temperature-range phenotype.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as a lower-bound growth constraint that low-temperature tolerance must overcome.)
- **Existing causal graph summary:** temperature_range_bounded_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **temperature range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range.yaml`.

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
- **Trait label:** temperature range
- **METPO identifier:** METPO:1000306
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature phenotype with numerical limits that bounds the minimum and maximum ambient temperatures supporting growth of an organism.
- **Parent traits:** METPO:1000533, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/s0300-9629(97)00003-0: adapted to environments of high temperature (Thermophile-adaptation review supports the bounded ambient-temperature span over which membrane, enzyme, and bioenergetic adaptations sustain growth as the basis of the temperature-range phenotype.) | DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cold-end membrane stress as a lower-bound growth constraint that low-temperature tolerance must overcome.)
- **Existing causal graph summary:** temperature_range_bounded_adaptation: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **temperature range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **Temperature range** (METPO:1000306)

### 1) Scope summary (trait meaning, boundary cases, nearby traits)

**Trait definition (curation-ready):** *Temperature range* is the **bounded interval** of ambient temperatures **[Tmin, Tmax]** that **supports microbial growth** under specified assay conditions (medium composition, oxygen availability, salinity/pH, growth mode, etc.). The trait is conceptually distinct from **temperature optimum (TOPT)** (the temperature maximizing growth rate) and from categorical ecological labels (psychrophile/mesophile/thermophile), which are coarse descriptors rather than explicit numerical bounds. Reviews emphasize that the **upper bound** is often reached when “specific enzymes or systems” become inactivated, whereas the **lower bound** involves membrane rigidification and constraints on transcription/translation that organisms must actively overcome. (purwar2024adaptationsofpsychrophilic pages 3-4, grunberger2023uncoveringthetemporal pages 1-2)

**Boundary cases to explicitly handle in curation:**
- **Psychrotrophs vs psychrophiles:** Psychrotrophs are operationally defined by their ability to grow at refrigeration temperatures (e.g., “below 7°C”) but may have higher optima and may not thrive at very low temperatures. (oh2024psychrotrophicbacteriathreatening pages 1-5)
- **Thermophiles/hyperthermophiles:** Thermophiles can have relatively high **Tmin** (i.e., they cannot grow at typical ambient temperatures), so “temperature range” must not be conflated with “temperature optimum.” Hyperthermophile evidence (Pyrococcus) illustrates organismal survival/growth within a very high-temperature band and distinct stress responses to heat vs cold shock. (grunberger2023uncoveringthetemporal pages 1-2)

**Assay-dependent nature (warning for curation):** Tmin/Tmax are **condition-dependent**; literature shows they shift with interacting stressors (pH, energy availability, salinity) and growth mode (planktonic vs biofilm). Thus, any curated edge should record its experimental context when possible. (chiu2023membranelipidand pages 2-3, dessenne2024lipidomicanalysesreveal pages 1-2)

---

### 2) Current mechanistic understanding (key concepts and definitions)

Microbial temperature range is best modeled as an emergent phenotype constrained by multiple coupled modules:

1. **Membrane physical state and homeoviscous adaptation (HVA)**
   - A unifying concept is **homeoviscous adaptation**: cells adjust membrane lipid composition to maintain membrane fluidity and function across temperatures. Cold tends to rigidify membranes; adaptation frequently includes increased unsaturated/branched/short-chain lipids that lower melting points. (moon2023temperaturemattersbacterial pages 7-9, purwar2024adaptationsofpsychrophilic pages 8-10, maiti2024extrememakeoverthe pages 3-4)

2. **Cold-shock constraints on transcription/translation**
   - Cold stabilizes nucleic acid secondary structures and can impede transcription and translation; adaptive responses include **cold-shock proteins** (RNA chaperones) and **RNA helicases** to resolve structures, as well as broader translational reprogramming (e.g., ribosomal protein induction). (moon2023temperaturemattersbacterial pages 7-9, grunberger2023uncoveringthetemporal pages 1-2)

3. **Heat-shock/proteostasis constraints at upper temperatures**
   - Upper-bound growth requires preventing protein denaturation and aggregation via the **heat shock response**, including chaperones (e.g., DnaK/GroEL) and regulators (e.g., archaeal heat-shock regulator Phr). (moon2023temperaturemattersbacterial pages 14-15, grunberger2023uncoveringthetemporal pages 1-2)

4. **DNA topology and high-temperature nucleic-acid stability**
   - Thermophiles frequently use **positive supercoiling** (reverse gyrase) and nucleoid-associated factors to stabilize DNA at high temperatures; DNA supercoiling also appears in reviews as a regulatory lever for cold genes. (grunberger2023uncoveringthetemporal pages 1-2, ramon2023ageneraloverview pages 1-2)

5. **Cryoprotection and ice interaction (near-freezing constraints)**
   - Approaching freezing, growth/survival constraints include ice formation and recrystallization; microbes employ **ice-binding/antifreeze proteins** (thermal hysteresis; ice recrystallization inhibition) and extracellular polysaccharides (EPS). (purwar2024adaptationsofpsychrophilic pages 6-7, ramon2023ageneraloverview pages 1-2)

6. **Compatible solutes and metabolic/oxidative stress coupling**
   - Reviews identify **compatible solutes** (e.g., glycine betaine, trehalose, glycerol) as cryoprotective osmolytes; low temperature can increase **ROS**, requiring oxidative-stress defenses. (purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 8-10)

---

### 3) Recent developments (prioritizing 2023–2024)

#### 3.1 Membrane remodeling links genes to temperature-bound phenotypes (2023–2024)
- **A. baumannii lipidomics at 18°C vs 37°C** showed systematic increases in specific unsaturated fatty acids (C16:1 in most strains) and identified genomic determinants (presence of **FabA** and multiple candidate desaturases) that may underlie strain-to-strain differences in low-temperature membrane remodeling. (dessenne2024lipidomicanalysesreveal pages 1-2)
- **Archaeal GDGT cyclization and ring synthases (grsA/grsB)**: Controlled experiments in *Saccharolobus islandicus* compared **76°C (optimal)** vs **66°C (cold stress)** and linked stress to impaired growth and reduced GDGT cyclization; grsB is highlighted as generating highly cyclized GDGTs (≥5 rings) and is differentially expressed under acid and cold stress, while transcription did not always predict lipid output. (chiu2023membranelipidand pages 2-3, chiu2023membranelipidand pages 1-2)
- A 2024 feature article synthesizes how lipid features (unsaturation/branching/headgroup remodeling) prevent cold-induced gel transitions and reviews computational/experimental evidence for temperature-dependent membrane behavior. (maiti2024extrememakeoverthe pages 3-4, maiti2024extrememakeoverthe pages 4-5)

#### 3.2 High-resolution temporal stress-response mapping in a hyperthermophile (2023)
- Integrated **RNA-seq + proteomics** in *Pyrococcus furiosus* (mBio 2023) highlighted **distinct heat- vs cold-shock programs**: heat shock involves rapid transcriptome reprogramming orchestrated by regulator **Phr** with sustained protein-level upregulation; cold shock at **4°C** showed translation-related signatures (ribosomal proteins; 5′-leadered sequences), supporting translation regulation as an adaptive axis affecting Tmin. (grunberger2023uncoveringthetemporal pages 1-2)

#### 3.3 Applied high-temperature adaptation in wastewater nitrogen removal (2024 preprint)
- Anammox processes are widely applied at **30–35°C** and also in mainstream systems at **10–25°C**, but many industrial wastewaters exceed **35°C**. A 2024 preprint adapted *Candidatus Brocadia* from **30→40°C**, reporting that successful adaptation required **reducing loading rate** (≤ half the specific anammox activity) and involved **chaperone upregulation** plus a novel **increased ladderane lipid cyclization** signature. (christina2024mechanismsofanammox pages 1-5)

---

### 4) Candidate nodes grouped by type (for `temperature_range.yaml`)

| Group | Candidate node | Role in temperature-range graph | Suggested ontology grounding (CURIE) | Evidence basis |
|---|---|---|---|---|
| Phenotypes/traits | temperature range | Target trait: bounded minimum and maximum temperatures supporting growth | METPO:1000306 | Defined as bounded growth-supporting ambient temperatures; lower and upper limits are mechanistically constrained by multiple cellular systems (grunberger2023uncoveringthetemporal pages 1-2, ramon2023ageneraloverview pages 1-2) |
| Phenotypes/traits | minimum growth temperature (Tmin) | Lower bound of growth-supporting interval |  | Psychrophile/psychrotroph literature and cold-shock studies treat this as constrained by membrane fluidity, translation, cryoprotection, and oxidative stress (purwar2024adaptationsofpsychrophilic pages 8-10, ramon2023ageneraloverview pages 1-2) |
| Phenotypes/traits | maximum growth temperature (Tmax) | Upper bound of growth-supporting interval |  | Thermophile/hyperthermophile literature treats this as constrained by protein/DNA stability, membrane properties, and heat-shock systems (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 14-15) |
| Phenotypes/traits | temperature optimum (TOPT) | Nearby trait; distinct from range bounds |  | Recent evolution experiment in a thermophile discusses TOPT shift separately from Tmin/Tmax (mondal2024aquificaeovercomescompetition pages 1-2) |
| Phenotypes/traits | psychrotrophic growth at refrigeration temperature | Boundary-case phenotype related to low-end range |  | Food-safety review defines psychrotrophs by growth below 7°C, distinguishing them from broader range concepts (oh2024psychrotrophicbacteriathreatening pages 1-5, oh2024psychrotrophicbacteriathreatening pages 5-9) |
| Environmental & experimental factors | decreased ambient temperature / cold shock | Primary external factor decreasing fluidity and impeding RNA/protein function | ENVO:09200013 | Cold shock experiments and reviews show distinct transcriptomic/proteomic responses and membrane remodeling under low temperature (grunberger2023uncoveringthetemporal pages 1-2, ramon2023ageneraloverview pages 1-2) |
| Environmental & experimental factors | elevated ambient temperature / heat shock | Primary external factor increasing membrane/protein/DNA stress | ENVO:09200013 | Heat-shock studies in bacteria and archaea show extensive reprogramming and chaperone induction (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 14-15) |
| Environmental & experimental factors | freezing-thawing stress | Extreme low-temperature experimental factor near lower limit |  | Freeze-thaw studies and psychrophile reviews implicate cryoprotectants, pigments, and ice-binding proteins (purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 11-13) |
| Environmental & experimental factors | refrigerated food storage | Real-world assay/implementation context selecting psychrotrophs | ENVO:01000925 | Refrigeration allows psychrotroph growth and spoilage of animal-derived foods (oh2024psychrotrophicbacteriathreatening pages 1-5, oh2024psychrotrophicbacteriathreatening pages 5-9) |
| Environmental & experimental factors | growth at 18°C vs 37°C | Concrete bacterial temperature comparison for membrane remodeling |  | A. baumannii lipidomics directly compared these temperatures (dessenne2024lipidomicanalysesreveal pages 1-2) |
| Environmental & experimental factors | growth at 66°C vs 76°C | Concrete archaeal temperature comparison for GDGT adaptation |  | S. islandicus cold-stress experiment compared 66°C to optimal 76°C (chiu2023membranelipidand pages 2-3, chiu2023membranelipidand pages 1-2) |
| Environmental & experimental factors | reactor adaptation from 30°C to 40°C | Applied high-temperature adaptation regime |  | Anammox adaptation study ramped one reactor from 30 to 40°C (christina2024mechanismsofanammox pages 1-5) |
| Environmental & experimental factors | boiling spring environment (85°C) | Natural high-temperature habitat constraining community range | ENVO:00000051 | Boiling spring microbiome provides in situ context for thermal adaptation genes (mondal2024aquificaeovercomescompetition pages 1-2) |
| Environmental & experimental factors | pH stress | Important interacting factor that co-varies with temperature responses | ENVO:09200019 | Archaeal membrane-cyclization study tested acid and cold stress together; pH affects GDGT responses (chiu2023membranelipidand pages 2-3, chiu2023membranelipidand pages 17-18) |
| Cellular processes | homeoviscous adaptation | Central process linking temperature change to membrane-state compensation | GO:0006935 | Multiple recent reviews/studies identify HVA as a core mechanism across temperature extremes (purwar2024adaptationsofpsychrophilic pages 8-10, maiti2024extrememakeoverthe pages 5-6) |
| Cellular processes | membrane fluidity homeostasis | Immediate physical determinant of low/high temperature tolerance | GO:0016042 | Membrane fluidity changes are a recurring mechanistic theme across bacteria and archaea (moon2023temperaturemattersbacterial pages 7-9, dessenne2024lipidomicanalysesreveal pages 1-2) |
| Cellular processes | fatty-acid desaturation | Effector process increasing unsaturation at low temperature | GO:0006636 | Desaturases and unsaturated fatty-acid synthesis maintain fluidity in cold (purwar2024adaptationsofpsychrophilic pages 8-10, dessenne2024lipidomicanalysesreveal pages 1-2) |
| Cellular processes | GDGT cyclization | Archaeal membrane adaptation process affecting packing/permeability |  | Temperature and other stresses alter average GDGT cyclization (chiu2023membranelipidand pages 2-3, chiu2023membranelipidand pages 1-2) |
| Cellular processes | ladderane lipid cyclization | Candidate high-temperature adaptation process in anammox |  | Preprint reports doubled ladderane cyclization during adaptation to 40°C (christina2024mechanismsofanammox pages 1-5) |
| Cellular processes | two-component temperature sensing | Regulatory sensing of membrane-state changes | GO:0007165 | Cold sensing via membrane state activating two-component systems is emphasized in reviews (ramon2023ageneraloverview pages 1-2, moon2023temperaturemattersbacterial pages 7-9) |
| Cellular processes | heat-shock response | Upper-bound survival program for proteostasis | GO:0009408 | Heat shock induces major transcriptome/proteome reprogramming (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 14-15) |
| Cellular processes | cold-shock response | Lower-bound survival program for translation/RNA maintenance | GO:0009409 | Cold shock triggers specific RNA/protein-level responses and translational regulation (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 7-9) |
| Cellular processes | protein folding / chaperone-mediated refolding | Prevents thermal denaturation or cold-induced folding failure | GO:0006457 | Chaperones are repeatedly implicated at both temperature extremes (moon2023temperaturemattersbacterial pages 14-15, purwar2024adaptationsofpsychrophilic pages 15-16) |
| Cellular processes | translation regulation during cold stress | Protects lower-temperature growth capacity | GO:0006412 | Upregulation of ribosomal proteins and leadered transcripts indicates translation-level control (grunberger2023uncoveringthetemporal pages 1-2) |
| Cellular processes | RNA chaperoning / RNA helicase activity | Resolves inhibitory RNA secondary structures at low temperature | GO:0003723, GO:0004386 | CspA and CsdA are highlighted as supporting cold translation (moon2023temperaturemattersbacterial pages 7-9) |
| Cellular processes | DNA topological change / positive supercoiling | Protects nucleic acids at high temperature, regulates cold genes | GO:0006265 | Reverse gyrase and DNA supercoiling are linked to thermophile DNA stability and cold regulation (grunberger2023uncoveringthetemporal pages 1-2, ramon2023ageneraloverview pages 1-2) |
| Cellular processes | response to oxidative stress | Mitigates ROS generated under temperature stress | GO:0006979 | Low temperature can increase ROS; thermophiles also encode oxidative-damage protection (purwar2024adaptationsofpsychrophilic pages 8-10, mondal2024aquificaeovercomescompetition pages 1-2) |
| Cellular processes | cryoprotection / ice recrystallization inhibition | Extends growth or survival near freezing |  | IBPs/AFPs and solutes are cited as preventing ice damage (purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 10-11) |
| Genes/proteins/complexes | DesK | Membrane thickness/fluidity sensor kinase for cold response |  | Bacillus DesK directly senses membrane state and activates cold adaptation pathway (moon2023temperaturemattersbacterial pages 7-9) |
| Genes/proteins/complexes | DesR | Response regulator activating desaturase expression |  | DesR receives phosphate from DesK and induces des genes (moon2023temperaturemattersbacterial pages 7-9) |
| Genes/proteins/complexes | Des / Δ5-desaturase | Lipid desaturase increasing unsaturated fatty acids |  | Named downstream enzyme in Bacillus cold adaptation (moon2023temperaturemattersbacterial pages 7-9) |
| Genes/proteins/complexes | FabA | Unsaturated-fatty-acid synthesis enzyme candidate affecting low-T adaptation |  | Found in some A. baumannii strains with distinctive low-temperature lipid responses (dessenne2024lipidomicanalysesreveal pages 1-2) |
| Genes/proteins/complexes | candidate desaturases | Candidate enzymes for strain-specific low-T lipid remodeling |  | A. baumannii ABVal2 harbored five candidate desaturases (dessenne2024lipidomicanalysesreveal pages 1-2) |
| Genes/proteins/complexes | GrsA | GDGT ring synthase introducing early cyclopentane rings |  | Archaeal radical SAM ring synthase for GDGT cyclization (chiu2023membranelipidand pages 2-3) |
| Genes/proteins/complexes | GrsB | GDGT ring synthase linked to highly cyclized GDGTs |  | Differentially expressed under cold/acid stress; forms GDGTs with ≥5 rings (chiu2023membranelipidand pages 2-3, chiu2023membranelipidand pages 1-2) |
| Genes/proteins/complexes | DnaK (Hsp70) | Heat/cold proteostasis chaperone |  | Named in reviews and stress-response discussions as temperature adaptation factor (moon2023temperaturemattersbacterial pages 14-15, purwar2024adaptationsofpsychrophilic pages 6-7) |
| Genes/proteins/complexes | GroEL | Chaperonin supporting folding under temperature stress |  | Recurrently cited among temperature-response chaperones (moon2023temperaturemattersbacterial pages 14-15, purwar2024adaptationsofpsychrophilic pages 6-7) |
| Genes/proteins/complexes | GroES | Co-chaperonin in cold adaptation literature |  | Named alongside GroEL/DnaK in psychrophile adaptation review (purwar2024adaptationsofpsychrophilic pages 6-7) |
| Genes/proteins/complexes | Hsc66 | Hsp70-family chaperone in psychrophile proteostasis |  | Mentioned as molecular chaperone supporting folding/stability under temperature stress (purwar2024adaptationsofpsychrophilic pages 8-10) |
| Genes/proteins/complexes | trigger factor | Cold-overexpressed folding factor |  | Reported as ~40-fold overexpressed at low temperatures in bacterial review (moon2023temperaturemattersbacterial pages 7-9) |
| Genes/proteins/complexes | PPIases | Support protein folding when prolyl isomerization is slow in the cold |  | Cold-adapted proteins reduce proline and overexpress PPIases (moon2023temperaturemattersbacterial pages 7-9) |
| Genes/proteins/complexes | CspA | Cold-shock RNA chaperone |  | Classic CSP supporting low-temperature translation (moon2023temperaturemattersbacterial pages 7-9) |
| Genes/proteins/complexes | CsdA | RNA helicase supporting translation at low temperature |  | Explicitly named as translation-supporting helicase in cold (moon2023temperaturemattersbacterial pages 7-9) |
| Genes/proteins/complexes | Phr | Archaeal transcriptional regulator orchestrating heat-shock response |  | Identified as key heat-shock regulator in P. furiosus (grunberger2023uncoveringthetemporal pages 1-2) |
| Genes/proteins/complexes | reverse gyrase | Thermophile marker enzyme for positive DNA supercoiling |  | Directly associated with high-temperature DNA stabilization in thermophiles (grunberger2023uncoveringthetemporal pages 1-2) |
| Genes/proteins/complexes | ribosomal proteins | Cold-responsive translation machinery components |  | Upregulated during cold shock in P. furiosus (grunberger2023uncoveringthetemporal pages 1-2) |
| Genes/proteins/complexes | methionine sulfoxide reductase | Oxidative-damage protection candidate in hot environments |  | Found among thermal-adaptation genes in boiling spring metagenome (mondal2024aquificaeovercomescompetition pages 1-2) |
| Genes/proteins/complexes | universal stress proteins (USPs) | Non-classical stress proteins contributing to low-T adaptation |  | Rhodococcus low-temperature adaptation study highlights USPs/HSPs rather than only CSPs (purwar2024adaptationsofpsychrophilic pages 11-13) |
| Lipid/chemical entities | unsaturated fatty acids | Increase fluidity at low temperature | CHEBI:27208 | Broad class repeatedly associated with cold adaptation (purwar2024adaptationsofpsychrophilic pages 8-10, dessenne2024lipidomicanalysesreveal pages 1-2) |
| Lipid/chemical entities | palmitoleic acid (C16:1) | Low-temperature-enriched fatty acid in A. baumannii | CHEBI:36021 | Increased at 18°C in five strains (dessenne2024lipidomicanalysesreveal pages 1-2) |
| Lipid/chemical entities | oleic acid (C18:1) | Alternative low-temperature-enriched fatty acid | CHEBI:16196 | Increased at 18°C in strain ABVal2 (dessenne2024lipidomicanalysesreveal pages 1-2) |
| Lipid/chemical entities | cis-vaccenic acid | Example low-temperature unsaturated fatty acid in E. coli | CHEBI:30823 | Increased in cold according to review (moon2023temperaturemattersbacterial pages 7-9) |
| Lipid/chemical entities | phosphatidylethanolamine (PE) | Major GPL altered with temperature | CHEBI:16038 | PE composition shifts with low-temperature growth in A. baumannii (dessenne2024lipidomicanalysesreveal pages 1-2) |
| Lipid/chemical entities | phosphatidylglycerol (PG) | Major GPL altered with temperature | CHEBI:17517 | PG composition shifts with low-temperature growth in A. baumannii (dessenne2024lipidomicanalysesreveal pages 1-2) |
| Lipid/chemical entities | glycerophospholipids (GPLs) | Membrane lipid class remodeled across temperatures | CHEBI:37739 | Central output of lipidomic adaptation studies (dessenne2024lipidomicanalysesreveal pages 1-2) |
| Lipid/chemical entities | branched-chain fatty acids | Cold-adaptation lipids that lower melting point | CHEBI:35819 | Reviews cite branched and methyl-branched FAs in psychrophiles (purwar2024adaptationsofpsychrophilic pages 8-10, maiti2024extrememakeoverthe pages 3-4) |
| Lipid/chemical entities | polyunsaturated fatty acids (PUFAs) | Cold-protective membrane fluidizers | CHEBI:26208 | EPA/DHA and other PUFAs are cited as supporting low-temperature growth (purwar2024adaptationsofpsychrophilic pages 10-11, maiti2024extrememakeoverthe pages 4-5) |
| Lipid/chemical entities | cyclopropane fatty acids | Membrane modifiers affecting stress tolerance | CHEBI:61127 | Discussed as temperature/stress-relevant membrane modifications (maiti2024extrememakeoverthe pages 5-6, maiti2024extrememakeoverthe pages 4-5) |
| Lipid/chemical entities | GDGTs | Archaeal tetraether membrane lipids whose cyclization shifts with stress |  | Core archaeal membrane entities in S. islandicus study (chiu2023membranelipidand pages 2-3, chiu2023membranelipidand pages 1-2) |
| Lipid/chemical entities | ladderane lipids | Unique anammox membrane lipids implicated in high-T adaptation |  | High-temperature adaptation associated with increased ladderane cyclization (christina2024mechanismsofanammox pages 1-5) |
| Lipid/chemical entities | glycine betaine | Compatible solute / cryoprotectant | CHEBI:17750 | Named solute in psychrophile and food-spoilage reviews (purwar2024adaptationsofpsychrophilic pages 10-11, oh2024psychrotrophicbacteriathreatening pages 1-5) |
| Lipid/chemical entities | trehalose | Compatible solute / cryoprotectant | CHEBI:18128 | Listed among cold-protective solutes (purwar2024adaptationsofpsychrophilic pages 10-11) |
| Lipid/chemical entities | glycerol | Compatible solute / cryoprotectant | CHEBI:17754 | Listed among cryoprotective metabolites in psychrophiles (purwar2024adaptationsofpsychrophilic pages 10-11) |
| Lipid/chemical entities | reactive oxygen species (ROS) | Damaging molecules elevated under low-T stress | CHEBI:26523 | Review notes ROS increase during low-temperature stress (purwar2024adaptationsofpsychrophilic pages 8-10) |
| Lipid/chemical entities | extracellular polysaccharides (EPS) | Surface/cryoprotective material aiding cold endurance | CHEBI:62962 | EPS noted as cold-protective in psychrophiles (purwar2024adaptationsofpsychrophilic pages 6-7, ramon2023ageneraloverview pages 1-2) |
| Lipid/chemical entities | antifreeze proteins / ice-binding proteins | Cryoprotective molecules inhibiting ice recrystallization |  | Strongly featured in psychrophile adaptations and applications (purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 3-4) |
| Pathways/modules | unsaturated fatty-acid biosynthesis | Produces fluidizing membrane lipids at low temperature | KEGG:map00061 | Implied by FabA/desaturase-based adaptation and review summaries (purwar2024adaptationsofpsychrophilic pages 8-10, dessenne2024lipidomicanalysesreveal pages 1-2) |
| Pathways/modules | membrane lipid remodeling module | Aggregate module for temperature-dependent lipid composition changes |  | Supported across bacterial and archaeal studies (maiti2024extrememakeoverthe pages 5-6, dessenne2024lipidomicanalysesreveal pages 1-2) |
| Pathways/modules | heat-shock regulon | Coordinated gene program protecting upper growth bound |  | Includes Phr-mediated archaeal response and bacterial chaperone systems (grunberger2023uncoveringthetemporal pages 1-2, moon2023temperaturemattersbacterial pages 14-15) |
| Pathways/modules | cold-shock regulon | Coordinated low-temperature adaptation module |  | Includes CSPs, helicases, and translation-related genes (ramon2023ageneraloverview pages 1-2, moon2023temperaturemattersbacterial pages 7-9) |
| Pathways/modules | compatible-solute accumulation | Accumulates cryoprotective osmolytes |  | General low-temperature adaptation strategy across psychrophiles/psychrotrophs (purwar2024adaptationsofpsychrophilic pages 10-11, oh2024psychrotrophicbacteriathreatening pages 1-5) |
| Pathways/modules | oxidative-stress defense module | Detoxifies ROS arising during temperature stress |  | Includes glutathione-linked protection and methionine sulfoxide reductases (purwar2024adaptationsofpsychrophilic pages 10-11, mondal2024aquificaeovercomescompetition pages 1-2) |
| Pathways/modules | sulfur oxidation (Sox) | Energy metabolism supporting thermophile ecosystem persistence | KEGG:map00920 | Dominant bioenergetic mechanism in 85°C spring metagenome (mondal2024aquificaeovercomescompetition pages 1-2) |
| Pathways/modules | reductive TCA cycle | Carbon fixation module in boiling spring thermophiles | KEGG:map00720 | Predominant carbon-fixation pathway in the hot-spring community (mondal2024aquificaeovercomescompetition pages 1-2) |
| Pathways/modules | anammox high-temperature adaptation module | Applied module for reactor adaptation above mesophilic range |  | Combines chaperone upregulation and ladderane cyclization in high-temperature wastewater adaptation (christina2024mechanismsofanammox pages 1-5) |


*Table: This table inventories candidate nodes for a microbial temperature-range causal graph, organized by entity type and grounded to available ontology CURIEs where possible. It is useful for converting recent literature on thermal adaptation into curatable TraitMech graph components.*

---

### 5) Evidence-backed candidate causal edges (triples) for TraitMech curation

| Edge (S–P–O) | Node grounding suggestions (CURIEs where known) | Evidence snippet (short quote) | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|
| Decreased ambient temperature → increases → membrane lipid unsaturation / homeoviscous adaptation | ENVO:temperature; GO:0016042 lipid catabolic/biosynthetic process; CHEBI:unsaturated fatty acid | “E. coli increases unsaturated cis-vaccenic acid and decreases palmitic acid with cold” (moon2023temperaturemattersbacterial pages 7-9) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | Broad bacterial mechanism affecting lower growth bound; generic node may be safer than species-specific lipid names. |
| DesK sensor kinase → positively regulates → DesR response regulator phosphorylation | UniProt/GO candidate: DesK histidine kinase; DesR response regulator; GO:0000155 two-component sensor activity | “DesK phosphorylates DesR to activate des genes when temperature falls” (moon2023temperaturemattersbacterial pages 7-9) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | Strong mechanistic edge for cold sensing in Bacillus; taxon-specific. |
| DesR → activates expression of → lipid desaturase des | des lipid desaturase; GO:0006636 unsaturated fatty acid biosynthetic process | “a D5-desaturase is induced downstream of membrane sensor DesK/response regulator DesR” (moon2023temperaturemattersbacterial pages 7-9) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | Good gene-level edge for membrane remodeling; species-specific to Bacillus system. |
| Lipid desaturase activity → increases → membrane fluidity at low temperature | EC candidate for fatty acid desaturase; GO:0006636; GO:0016042 | “upregulation of genes for… fatty acid synthesis/desaturation… maintain membrane fluidity” (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Review-level evidence; mechanistically strong but not always tied to one named enzyme. |
| FabA / candidate desaturases → contributes to → low-temperature unsaturated fatty-acid profile | KEGG/UniProt candidate: FabA; fatty acid desaturase | “FabA… was found in both ABVal2 and ABVal3… ABVal2 contains five candidate desaturases that may contribute to its lipid profile” (dessenne2024lipidomicanalysesreveal pages 1-2) | 10.1128/spectrum.00757-24, 2024, https://doi.org/10.1128/spectrum.00757-24 | Useful but somewhat inferential (“may contribute”); curate as uncertain/taxon-specific. |
| Cold stress → decreases → average GDGT cyclization | CHEBI:caldarchaeol/GDGT candidate; GO:0016042 | “acid and cold stress produced impaired growth and lower average GDGT cyclization” (chiu2023membranelipidand pages 1-2) | 10.3389/fmicb.2023.1219779, 2023, https://doi.org/10.3389/fmicb.2023.1219779 | Archaeal membrane adaptation edge; stress tested at 66°C vs 76°C in S. islandicus. |
| grsB (GDGT ring synthase) expression → modulates → highly cyclized GDGT formation | grsB; radical SAM enzyme; GO candidate lipid modification process | “grsB forms GDGTs with ≥5 rings” and “shows differential expression under both acid and cold stress” (chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 2-3) | 10.3389/fmicb.2023.1219779, 2023, https://doi.org/10.3389/fmicb.2023.1219779 | Strong candidate node; note transcript abundance did not perfectly predict lipid output. |
| Increased GDGT cyclization → increases → membrane packing / heat stability | CHEBI:GDGT; GO:membrane organization | “higher cyclization as increasing membrane packing, decreasing permeability, and enhancing heat stability” (chiu2023membranelipidand pages 1-2) | 10.3389/fmicb.2023.1219779, 2023, https://doi.org/10.3389/fmicb.2023.1219779 | Mechanistic interpretation from archaeal membrane literature summarized in study. |
| Heat shock / elevated temperature → induces → DnaK / GroEL chaperone systems | UniProt candidate: DnaK, GroEL; GO:0006457 protein folding | “Molecular chaperones… DnaK/Hsp70” and “GroEL” are implicated in survival at high temperatures (moon2023temperaturemattersbacterial pages 14-15) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | Review-level, broad across bacteria. |
| Phr transcriptional regulator → orchestrates → heat-shock gene expression | Phr regulator; GO:0006355 regulation of transcription | “Heat shock triggers extensive transcriptome reprogramming, orchestrated by the transcriptional regulator Phr” (grunberger2023uncoveringthetemporal pages 1-2) | 10.1128/mbio.02174-23, 2023, https://doi.org/10.1128/mbio.02174-23 | Strong archaeal regulatory edge in Pyrococcus furiosus. |
| Cold shock → induces → ribosomal proteins / translation regulation | GO:0006412 translation; ribosomal proteins | “upregulation of ribosomal proteins… suggest that translation regulation is important during cold shock adaption” (grunberger2023uncoveringthetemporal pages 1-2) | 10.1128/mbio.02174-23, 2023, https://doi.org/10.1128/mbio.02174-23 | Good process-level edge for lower-bound adaptation in hyperthermophile subjected to 4°C shock. |
| CspA cold-shock protein → acts as → RNA chaperone supporting low-temperature translation | UniProt candidate: CspA; GO:0003723 RNA binding | “cold-shock proteins (CspA) that act as RNA chaperones” (moon2023temperaturemattersbacterial pages 7-9) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | Classical bacterial cold-response edge; strong but taxon-rich rather than universal. |
| CsdA helicase → supports → translation under cold stress | UniProt candidate: CsdA; GO:0004386 helicase activity | “translation is supported by CsdA helicase” (moon2023temperaturemattersbacterial pages 7-9) | 10.1007/s12275-023-00031-x, 2023, https://doi.org/10.1007/s12275-023-00031-x | Useful named gene/protein edge for cold-end limit. |
| Positive DNA supercoiling / reverse gyrase → stabilizes → DNA at high temperature | GO:0006265 DNA topological change; reverse gyrase; EC candidate DNA topoisomerase | “positive DNA supercoiling by reverse gyrase” supports upper-temperature tolerance (grunberger2023uncoveringthetemporal pages 1-2) | 10.1128/mbio.02174-23, 2023, https://doi.org/10.1128/mbio.02174-23 | Strong concept for thermophile upper bound; may need direct primary citation for graph if wanting non-review support. |
| DNA supercoiling changes → regulate → cold-shock and cold-adaptation genes | GO:0006265 DNA topological change; cold-shock regulon | “induction of cold-shock and cold-adaptation genes mediated by DNA supercoiling” (ramon2023ageneraloverview pages 1-2) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | Review evidence; suitable as process-level edge for lower-bound regulation. |
| Compatible solutes (e.g., glycine betaine, trehalose, glycerol) → protect against → low-temperature / freezing stress | CHEBI:glycine betaine; CHEBI:trehalose; CHEBI:glycerol | “glycine, betaine, glycerol, trehalose… act as cryoprotectants and osmolytes” (purwar2024adaptationsofpsychrophilic pages 10-11) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Strong broad mechanism for low-end growth; compounds can be represented individually. |
| Compatible solute accumulation → enables → growth at refrigerated temperatures | CHEBI:glycine betaine; METPO:1000306 | “They can maintain the membrane fluidity even at low temperatures… compatible solutes” (oh2024psychrotrophicbacteriathreatening pages 1-5) | 10.5851/kosfa.2024.e70, 2024, https://doi.org/10.5851/kosfa.2024.e70 | Application-focused review on psychrotrophs in food; indirect but relevant to trait bounds. |
| Low temperature → increases → reactive oxygen species (ROS) | CHEBI:reactive oxygen species; GO:0006979 response to oxidative stress | “glycolysis ↑, TCA ↓, electron transport ↓, ROS ↑” under low temperature (purwar2024adaptationsofpsychrophilic pages 8-10) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Process-level edge from review; lower-temperature stress mechanism. |
| Oxidative-stress protection systems → support → thermal adaptation / survival | GO:0006979 response to oxidative stress; methionine sulfoxide reductase | “genes linked to thermal adaptation — … methionine sulfoxide reductases… enzymes protecting against oxidative damage” (mondal2024aquificaeovercomescompetition pages 1-2) | 10.1371/journal.pone.0310595, 2024, https://doi.org/10.1371/journal.pone.0310595 | Metagenomic evidence from 85°C spring; function inferred from gene content, so curate cautiously. |
| Chaperone upregulation → supports → adaptation of anammox to high temperatures | GO:0006457 protein folding; chaperone proteins | “The most notable adaptation mechanisms included: (1) upregulation of chaperones” (christina2024mechanismsofanammox pages 1-5) | 10.1101/2024.07.23.604647, 2024, https://doi.org/10.1101/2024.07.23.604647 | Preprint; promising but should be marked uncertain until peer reviewed. |
| Increased ladderane lipid cyclization → supports → high-temperature anammox adaptation | ladderane lipid candidate; GO:membrane organization | “doubled ladderane cyclization… presents crucial indicators in anammox adaptation to high-temperature wastewaters” (christina2024mechanismsofanammox pages 1-5) | 10.1101/2024.07.23.604647, 2024, https://doi.org/10.1101/2024.07.23.604647 | Preprint and system-specific; strong application relevance for 30→40°C adaptation. |
| Ice-binding / antifreeze proteins → prevent → ice damage at low temperature | antifreeze protein; ice-binding protein; GO:cold acclimation candidate | “ice-binding proteins (AFGPs/IBPs/IRIPs) that bind ice and provide thermal hysteresis and ice recrystallization inhibition” (purwar2024adaptationsofpsychrophilic pages 6-7) | 10.37256/amtt.5220244537, 2024, https://doi.org/10.37256/amtt.5220244537 | Supports lower-bound extension near/freezing conditions; mostly psychrophile-focused. |
| Membrane liquid-crystalline state change → activates → two-component cold sensing | GO:0007165 signal transduction; two-component system | “cold sensing via changes in the liquid-crystalline membrane state that activate two-component signal transduction” (ramon2023ageneraloverview pages 1-2) | 10.1007/s42770-023-01057-4, 2023, https://doi.org/10.1007/s42770-023-01057-4 | Good generic edge linking physical membrane state to regulatory response. |


*Table: This table lists evidence-backed candidate causal edges for microbial temperature range bounds, spanning lower- and upper-temperature mechanisms relevant to TraitMech curation. It emphasizes named regulators, membrane adaptations, nucleic-acid/translation factors, compatible solutes, and stress-response systems, with uncertainty notes for taxon-specific or preprint-based claims.*

---

### 6) Current applications and real-world implementations (with recent statistics)

#### 6.1 Food safety and cold-chain spoilage by psychrotrophs (2024)
- **Definition relevant to Tmin:** psychrotrophic bacteria can grow at refrigerated temperatures (e.g., “below 7°C”) and up to ~20°C, creating a low-temperature growth window that challenges refrigeration-based control. (oh2024psychrotrophicbacteriathreatening pages 1-5)
- **Quantitative shift in microbial community:** in raw milk, compared to mesophiles, “the quantity of psychrotrophic bacteria increased by over 10%” under refrigeration conditions (reviewed evidence). (oh2024psychrotrophicbacteriathreatening pages 1-5)
- **Contamination and load statistics for pathogens at cold temperatures:** *Listeria monocytogenes* prevalence in animal-derived foods is reported (e.g., 11.0% raw milk; 13.5% RTE meat; 19.5% uncooked processed meat) and concentrations of 4–6 Log CFU/g are cited in the review context. (oh2024psychrotrophicbacteriathreatening pages 5-9)

#### 6.2 Cold-active enzymes and low-temperature biotechnology (2024)
- Reviews highlight industrially relevant cold-active enzymes (e.g., **α-amylases, proteases, lipases, DNA polymerases, cellulases**) as having “high specific activities at low temperatures,” supporting processes where heating is undesirable (food processing, textiles, molecular biology, cold fermentation). (purwar2024adaptationsofpsychrophilic pages 3-4, purwar2024adaptationsofpsychrophilic pages 13-15)

#### 6.3 Thermophile ecosystems as sources of thermal-adaptation modules (2024)
- A boiling (85°C) hot-spring metagenome reported **microbial cell density ~8.5×10^4 mL−1** and **live:dead ratio 1.7**, and identified broad suites of thermal-adaptation genes (heat shock proteins, chaperonins, DNA gyrase modulators, fatty acid desaturases, oxidative-damage protection). These data support real-world sourcing of candidate genes/modules for engineering temperature tolerance. (mondal2024aquificaeovercomescompetition pages 1-2)

#### 6.4 High-temperature anammox for wastewater (2024)
- Thermophilic/heat-adapted anammox is motivated by industrial wastewaters exceeding 35°C; the 30→40°C adaptation regime provides an implementation-relevant operational constraint (loading rate reduction) and candidate molecular indicators (chaperones, ladderane cyclization). (christina2024mechanismsofanammox pages 1-5)

---

### 7) Expert synthesis and curation notes (what is “safe to curate” vs “needs caution”)

**High-confidence (mechanistically explicit, gene-level):**
- **DesK → DesR → des** cold-sensing/desaturation cascade (Bacillus model) with direct mechanistic description suitable for graph edges, though taxon-specific. (moon2023temperaturemattersbacterial pages 7-9)
- **Phr-regulated heat-shock reprogramming** in *Pyrococcus furiosus* (heat-shock regulator + transcriptome/proteome evidence). (grunberger2023uncoveringthetemporal pages 1-2)
- **CspA/CsdA** as cold translation-supporting factors (named proteins with clear function). (moon2023temperaturemattersbacterial pages 7-9)

**Moderate confidence (good biology but review-level generalization):**
- Broad edges linking **membrane lipid unsaturation ↔ membrane fluidity ↔ Tmin** and **chaperones ↔ Tmax** are strongly supported across reviews but may not specify a single universally conserved gene. (purwar2024adaptationsofpsychrophilic pages 8-10, moon2023temperaturemattersbacterial pages 14-15, ramon2023ageneraloverview pages 1-2)

**Caution / uncertainty flags:**
- **Metagenomic presence ≠ causal effect**: hot-spring metagenome genes “linked to thermal adaptation” support candidate nodes but not direct causal edges without expression/phenotype validation. (mondal2024aquificaeovercomescompetition pages 1-2)
- **Preprint evidence** (anammox ladderane cyclization/chaperones) is promising but should be curated as **uncertain until peer-reviewed**. (christina2024mechanismsofanammox pages 1-5)
- Statements like “candidate desaturases may contribute” in A. baumannii lipidomics imply causality but remain partially inferential; curate with an uncertainty qualifier and/or require follow-up functional validation. (dessenne2024lipidomicanalysesreveal pages 1-2)

---

## DOI-first bibliography (2023–2024 prioritized; includes URLs and publication months when available)

1. **Moon S, Ham S, Jeong J, et al.** *Temperature Matters: Bacterial Response to Temperature Change.* **Journal of Microbiology** (Mar **2023**). DOI: **10.1007/s12275-023-00031-x**. URL: https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 14-15, moon2023temperaturemattersbacterial pages 7-9)
2. **Grünberger F, Schmid G, Ahmad ZE, et al.** *Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics.* **mBio** (Dec **2023**). DOI: **10.1128/mbio.02174-23**. URL: https://doi.org/10.1128/mbio.02174-23 (grunberger2023uncoveringthetemporal pages 1-2)
3. **Ramón A, Esteves A, Villadóniga C, et al.** *A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.* **Brazilian Journal of Microbiology** (Jul **2023**). DOI: **10.1007/s42770-023-01057-4**. URL: https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2)
4. **Chiu BK, Waldbauer J, Elling FJ, et al.** *Membrane lipid and expression responses of Saccharolobus islandicus REY15A to acid and cold stress.* **Frontiers in Microbiology** (Aug **2023**). DOI: **10.3389/fmicb.2023.1219779**. URL: https://doi.org/10.3389/fmicb.2023.1219779 (chiu2023membranelipidand pages 2-3, chiu2023membranelipidand pages 1-2, chiu2023membranelipidand pages 17-18)
5. **Purwar S, Srivastava S.** *Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.* **Applied Microbiology: Theory & Technology** (Oct **2024**). DOI: **10.37256/amtt.5220244537**. URL: https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 3-4, purwar2024adaptationsofpsychrophilic pages 11-13, purwar2024adaptationsofpsychrophilic pages 13-15, purwar2024adaptationsofpsychrophilic pages 1-3)
6. **Oh H, Lee J.** *Psychrotrophic Bacteria Threatening the Safety of Animal-Derived Foods: Characteristics, Contamination, and Control Strategies.* **Food Science of Animal Resources** (Sep **2024**). DOI: **10.5851/kosfa.2024.e70**. URL: https://doi.org/10.5851/kosfa.2024.e70 (oh2024psychrotrophicbacteriathreatening pages 1-5, oh2024psychrotrophicbacteriathreatening pages 5-9)
7. **Dessenne C, Ménart B, Acket S, et al.** *Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of Acinetobacter baumannii.* **Microbiology Spectrum** (Oct **2024**). DOI: **10.1128/spectrum.00757-24**. URL: https://doi.org/10.1128/spectrum.00757-24 (dessenne2024lipidomicanalysesreveal pages 1-2)
8. **Maiti A, Erimban S, Daschakraborty S.** *Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments.* **Chemical Communications** (Aug **2024**). DOI: **10.1039/d4cc03114h**. URL: https://doi.org/10.1039/d4cc03114h (maiti2024extrememakeoverthe pages 3-4, maiti2024extrememakeoverthe pages 4-5, maiti2024extrememakeoverthe pages 5-6)
9. **Mondal N, Dutta S, Chatterjee S, et al.** *Aquificae overcomes competition… to dominate the boiling vent-water…* **PLOS ONE** (Oct **2024**). DOI: **10.1371/journal.pone.0310595**. URL: https://doi.org/10.1371/journal.pone.0310595 (mondal2024aquificaeovercomescompetition pages 1-2)
10. **Christina K, Navrátilová K, Behner A, et al.** *Mechanisms of Anammox Adaptation to High Temperatures: Increased Cyclization of Ladderane Lipids and Proteomic Insights.* **bioRxiv preprint** (Jul **2024**). DOI: **10.1101/2024.07.23.604647**. URL: https://doi.org/10.1101/2024.07.23.604647 (christina2024mechanismsofanammox pages 1-5)

---

## Warnings / “do not yet curate” candidates

1. **Metagenome-only functional inference** (e.g., “thermal adaptation genes” in a hot-spring metagenome) should not be curated as strong causal edges to Tmin/Tmax without expression, knockout, or comparative phenotype evidence. (mondal2024aquificaeovercomescompetition pages 1-2)
2. **Preprint mechanistic claims** (anammox ladderane cyclization and chaperone signatures) should be marked *uncertain* until peer review and replication. (christina2024mechanismsofanammox pages 1-5)
3. **General membrane-adaptation summaries** (e.g., “more unsaturation improves cold growth”) are curatable at the **process level** (lipid desaturation → membrane fluidity) but should not be forced into a single gene unless supported in the target taxon. (purwar2024adaptationsofpsychrophilic pages 8-10, ramon2023ageneraloverview pages 1-2)


References

1. (purwar2024adaptationsofpsychrophilic pages 3-4): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

2. (grunberger2023uncoveringthetemporal pages 1-2): Felix Grünberger, Georg Schmid, Zubeir El Ahmad, Martin Fenk, Katharina Vogl, Robert Reichelt, Winfried Hausner, Henning Urlaub, Christof Lenz, and Dina Grohmann. Uncovering the temporal dynamics and regulatory networks of thermal stress response in a hyperthermophile using transcriptomics and proteomics. Dec 2023. URL: https://doi.org/10.1128/mbio.02174-23, doi:10.1128/mbio.02174-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

3. (oh2024psychrotrophicbacteriathreatening pages 1-5): Hyemin Oh and Jeeyeon Lee. Psychrotrophic bacteria threatening the safety of animal-derived foods: characteristics, contamination, and control strategies. Food Science of Animal Resources, 44:1011-1027, Sep 2024. URL: https://doi.org/10.5851/kosfa.2024.e70, doi:10.5851/kosfa.2024.e70. This article has 38 citations.

4. (chiu2023membranelipidand pages 2-3): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

5. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

6. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

7. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

8. (maiti2024extrememakeoverthe pages 3-4): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

9. (moon2023temperaturemattersbacterial pages 14-15): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

10. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

11. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

12. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

13. (chiu2023membranelipidand pages 1-2): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

14. (maiti2024extrememakeoverthe pages 4-5): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

15. (christina2024mechanismsofanammox pages 1-5): Karmann Christina, Navrátilová Klára, Behner Adam, Noor Tayyaba, Danner Stella, Majchrzak Anastasia, Šantrůček Jiří, Podzimek Tomáš, Marin Lopez Marco A., Hajšlová Jana, Lipovová Petra, Bartáček Jan, and Kouba Vojtěch. Mechanisms of anammox adaptation to high temperatures: increased cyclization of ladderane lipids and proteomic insights. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.23.604647, doi:10.1101/2024.07.23.604647. This article has 1 citations.

16. (mondal2024aquificaeovercomescompetition pages 1-2): Nibendu Mondal, Subhajit Dutta, Sumit Chatterjee, Jagannath Sarkar, Mahamadul Mondal, Chayan Roy, Ranadhir Chakraborty, and Wriddhiman Ghosh. Aquificae overcomes competition by archaeal thermophiles, and crowding by bacterial mesophiles, to dominate the boiling vent-water of a trans-himalayan sulfur-borax spring. PLOS ONE, 19(10):e0310595, Oct 2024. URL: https://doi.org/10.1371/journal.pone.0310595, doi:10.1371/journal.pone.0310595. This article has 11 citations and is from a peer-reviewed journal.

17. (oh2024psychrotrophicbacteriathreatening pages 5-9): Hyemin Oh and Jeeyeon Lee. Psychrotrophic bacteria threatening the safety of animal-derived foods: characteristics, contamination, and control strategies. Food Science of Animal Resources, 44:1011-1027, Sep 2024. URL: https://doi.org/10.5851/kosfa.2024.e70, doi:10.5851/kosfa.2024.e70. This article has 38 citations.

18. (purwar2024adaptationsofpsychrophilic pages 11-13): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

19. (chiu2023membranelipidand pages 17-18): Beverly K. Chiu, Jacob Waldbauer, Felix J. Elling, Öykü Z. Mete, Lichun Zhang, Ann Pearson, Erin M. Eggleston, and William D. Leavitt. Membrane lipid and expression responses of saccharolobus islandicus rey15a to acid and cold stress. Frontiers in Microbiology, Aug 2023. URL: https://doi.org/10.3389/fmicb.2023.1219779, doi:10.3389/fmicb.2023.1219779. This article has 5 citations and is from a peer-reviewed journal.

20. (maiti2024extrememakeoverthe pages 5-6): Archita Maiti, Shakkira Erimban, and Snehasis Daschakraborty. Extreme makeover: the incredible cell membrane adaptations of extremophiles to harsh environments. Chemical communications, 60:10280-10294, Aug 2024. URL: https://doi.org/10.1039/d4cc03114h, doi:10.1039/d4cc03114h. This article has 13 citations and is from a domain leading peer-reviewed journal.

21. (purwar2024adaptationsofpsychrophilic pages 15-16): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

22. (purwar2024adaptationsofpsychrophilic pages 13-15): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

23. (purwar2024adaptationsofpsychrophilic pages 1-3): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.