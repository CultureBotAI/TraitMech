---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:41:17.617098'
end_time: '2026-06-18T03:00:52.276671'
duration_seconds: 1174.66
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: thermotolerant
  trait_identifier: METPO:1000619
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: thermotolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A temperature preference in which growth can occur at elevated temperatures
    without an obligate high-temperature preference.
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1099/00207713-52-6-2203: Pseudomonas thermotolerans sp.
    nov., a thermotolerant species (Organism example: Pseudomonas thermotolerans is
    described as thermotolerant.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to
    irreversible inactivation at high temperatures (Thermostable-protein review supports
    protein-stability features underlying facultative growth at elevated temperatures.)'
  causal_graph_summary: 'thermotolerant_facultative_heat_adaptation: 5 nodes, 3 edges'
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
- **Trait label:** thermotolerant
- **METPO identifier:** METPO:1000619
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at elevated temperatures without an obligate high-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/00207713-52-6-2203: Pseudomonas thermotolerans sp. nov., a thermotolerant species (Organism example: Pseudomonas thermotolerans is described as thermotolerant.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports protein-stability features underlying facultative growth at elevated temperatures.)
- **Existing causal graph summary:** thermotolerant_facultative_heat_adaptation: 5 nodes, 3 edges

## Research Objective

Research the microbial trait **thermotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/thermotolerant.yaml`.

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
- **Trait label:** thermotolerant
- **METPO identifier:** METPO:1000619
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth can occur at elevated temperatures without an obligate high-temperature preference.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1099/00207713-52-6-2203: Pseudomonas thermotolerans sp. nov., a thermotolerant species (Organism example: Pseudomonas thermotolerans is described as thermotolerant.) | DOI:10.1128/MMBR.65.1.1-43.2001: resistant to irreversible inactivation at high temperatures (Thermostable-protein review supports protein-stability features underlying facultative growth at elevated temperatures.)
- **Existing causal graph summary:** thermotolerant_facultative_heat_adaptation: 5 nodes, 3 edges

## Research Objective

Research the microbial trait **thermotolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/thermotolerant.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **thermotolerant** (METPO:1000619)

**Target trait definition (given):** “A temperature preference in which growth can occur at elevated temperatures without an obligate high-temperature preference.” (METPO:1000619)

### Executive scope summary
In TraitMech terms, **thermotolerant** should be curated as a **growth-capable** phenotype at temperatures above typical optima for the organism’s baseline ecology (e.g., mesophiles pushed toward Tmax), distinguishing it from (i) **thermophily**, where organisms *prefer* high temperatures as part of their normal growth range (e.g., 50–80 °C), and (ii) **heat/thermoresistance**, which can be defined by **survival or retention of viability** after otherwise lethal or pasteurizing heat exposures without necessarily supporting active growth. A practical operationalization for curation is: **ability to maintain growth rate/biomass increase/fermentation performance at an elevated temperature** (often 39–42 °C for many mesophilic bacteria/yeasts; higher for thermophiles/thermoacidophiles), using explicitly defined assays and media. (moon2023temperaturemattersbacterial pages 1-3, zhang2023improvingthermotoleranceof pages 1-2, mcguire2023wholegenomesequencinganalysis pages 1-2)

### 1) Trait scope: phenotype boundaries and assay distinctions

#### 1.1 Thermotolerant vs thermophilic
A 2023 bacterial temperature-response review gives explicit thermophile and psychrophile growth ranges: “**thermophiles, that prefer a temperature range of 50–80 °C**… Psychrophiles prefer a temperature range of −20–20 °C…” (Moon et al., 2023; published online 2023-04-03). This supports using *preference/optimum* as a boundary between thermophily and thermotolerance. (moon2023temperaturemattersbacterial pages 1-3)

#### 1.2 Thermotolerant growth vs heat-shock survival (thermoresistance)
The same review emphasizes that heat shock is defined relative to **above the optimal growth temperature**, and uses growth limitations (e.g., “E. coli… grows exponentially at 37 °C but poorly at 44 °C, and becomes frail at ~50 °C”) to highlight that **growth failure and cellular damage** differ from short-term stress responses. (moon2023temperaturemattersbacterial pages 1-3)

A food-safety study on *Staphylococcus aureus* quantifies **survival** under heat after acid pre-exposure using “cross-adaptation area” (min·log10 CFU), indicating a distinct thermoresistance-like assay (survival under heat exposure) rather than growth at high temperature. (liao2023preexposureoffoodborne pages 2-4)

**Curation recommendation:** Keep **METPO:1000619 thermotolerant** focused on **growth/fermentation at elevated temperature**, and treat heat-shock survival metrics as either a separate trait or as **assay-specific evidence** that should be curated as uncertain if used to infer growth thermotolerance.

### 2) Key mechanistic concepts (current understanding, evidence-backed)
Thermotolerant growth is consistently underpinned by a multi-layer response spanning:

1. **Proteostasis / chaperone networks** (GroES/GroEL, DnaK/DnaJ/GrpE, ClpB; small HSPs). (hua2024regulatorymechanismsof pages 11-13, zhang2023improvingthermotoleranceof pages 1-2)
2. **Transcriptional regulation of heat stress** (sigma factors such as RpoH/RpoE in bacteria; HSF1/HsfA in fungi/yeast). (hua2024regulatorymechanismsof pages 11-13, moon2023temperaturemattersbacterial pages 3-5, fabri2023theheatshock pages 6-7)
3. **Membrane and envelope remodeling** to maintain function and integrity at higher temperature (fatty-acid saturation/unsaturation, phospholipid/LPS abundance, membrane protein folding; extracellular polysaccharide layers). (matsumoto2023implicationofamino pages 2-5, hua2024regulatorymechanismsof pages 11-13, fabri2023theheatshock pages 6-7)
4. **Compatible solutes / osmolytes** (trehalose, mannitol; sometimes glycerol/proline) that stabilize proteins and membranes. (foster2024analysisoffermentation pages 78-82, moon2023temperaturemattersbacterial pages 3-5)
5. **Oxidative stress management** (SOD/GPx/thioredoxin reductase, catalase) to mitigate heat-associated ROS damage. (hua2024regulatorymechanismsof pages 11-13, foster2024analysisoffermentation pages 78-82)
6. **Systems-level evolutionary/genetic routes** (adaptive laboratory evolution; large deletions; plasmid-borne chaperone overexpression; master regulator mutations). (mcguire2023wholegenomesequencinganalysis pages 1-2)

### 3) Recent developments (prioritizing 2023–2024)

#### 3.1 Industrial acetic-acid bacteria (AAB) and vinegar fermentation (2024 review)
A 2024 Microbial Cell Factories review frames **high temperature tolerance** as an industrially important phenotype in vinegar production and summarizes mechanisms and engineering strategies (DBTL, gTME, multi-omics). It gives direct experimental evidence claims for chaperones:
- “overexpression of **groES/L** and **grpE-dnaK-dnaJ**… enhanced growth activity at **42 °C**” and “**clpB knockout** strains lost the ability to grow at high temperature,” with RpoH regulation and heat sensitivity upon rpoH deletion. (hua2024regulatorymechanismsof pages 11-13)
It also highlights ROS mitigation and upregulation of antioxidant genes under heat stress in a thermotolerant *A. pasteurianus* strain, plus EPS/polysaccharide layers and membrane remodeling as protective mechanisms. (hua2024regulatorymechanismsof pages 11-13)

#### 3.2 Mechanistic gene-level reconstruction of thermotolerance after experimental adaptation (2023 primary study)
A Journal of Bacteriology 2023 study identifies three mutations sufficient to reproduce thermotolerance in an experimentally evolved *Acetobacter pasteurianus* strain TH-3. It explicitly reports that “**dicarboxylate transporter**, in addition to **asparagine permease**, both… dysfunctional mutations, are involved in thermotolerance… [and] mutation in **glnD (6-base deletion)** was also shown to be involved in thermotolerance,” accompanied by phenotypes including “increased phospholipid (PL) and lipopolysaccharide (LPS) contents, and respiratory activities.” (matsumoto2023implicationofamino pages 2-5)

This is particularly valuable for TraitMech because it links **specific genes → envelope/metabolic phenotypes → thermotolerant growth** using reconstruction and complementation logic. (matsumoto2023implicationofamino pages 2-5)

#### 3.3 Fungal thermotolerance linked to lipid homeostasis and fatty acid desaturation (2023 primary study)
A 2023 Microbiology Spectrum paper demonstrates a regulatory axis connecting heat shock transcription factor HsfA to membrane lipid biosynthesis and unsaturated fatty acid metabolism. It reports: “**hsfA controls sdeA expression**,” and “HsfA is required for the adaptation of the fungal plasma membrane to HS,” while the Δ9 desaturase **SdeA** is essential and required for unsaturated FA biosynthesis. (fabri2023theheatshock pages 6-7)

This provides a strong, mechanistically grounded set of nodes/edges for fungal thermotolerance graphs.

#### 3.4 Engineering thermotolerance for biomanufacturing (2023 yeast synthetic biology)
An RSC Advances 2023 study engineered *S. cerevisiae* with gene circuits expressing small HSPs and found multiple engineered strains had higher growth and viability at **42 °C**; the best performers showed **19.8%** and **17.2%** higher cell density than control. (zhang2023improvingthermotoleranceof pages 1-2)

This directly supports curating **small HSPs → improved growth at elevated temperature** edges.

#### 3.5 Stress cross-adaptation affecting heat survival in foodborne pathogens (2023)
A 2023 Microbiology Spectrum paper quantified acid→heat cross-adaptation in *S. aureus*. It reports that strain J15 exhibited cross-adaptation regions of **6.910**, **6.870**, and **6.360 min·log10 CFU** after different organic acid pretreatments, and links the phenotype to membrane integrity and fatty acid composition shifts (reduced membrane fluidity). (liao2023preexposureoffoodborne pages 2-4)

**Curation note:** This is strong evidence for an **assay-specific thermoresistance/cross-protection** mechanism; it should be flagged as potentially distinct from the METPO thermotolerant growth definition.

#### 3.6 Heat stress adaptation via toxin–antitoxin systems in archaea (2024)
A 2024 mBio study biochemically characterizes the VapBC4 toxin–antitoxin system in *Sulfolobus acidocaldarius*, reporting “**VapC4 toxin expression led to heat-induced persister-like cell formation, allowing the cell to cope with the stress**.” (bhowmick2024roleofvapbc4 pages 1-2)

**Curation note:** This supports edges from TA systems to **heat-stress coping/persistence**, which may trade off with growth (growth stasis). Useful for broader “thermotolerance” definitions, but may be peripheral for strictly growth-based METPO:1000619.

### 4) Current applications and real-world implementations

1. **Vinegar production / acetic acid fermentation:** High temperature tolerance is a key industrial robustness trait in AAB because fermentation environments can involve “consistently high temperatures.” Mechanism-informed approaches (multi-omics, DBTL, gTME) are reviewed as practical strategies to engineer or select robust strains. (Hua et al., 2024). (hua2024regulatorymechanismsof pages 11-13, hua2024regulatorymechanismsof media fe7a5a07)

2. **Biomanufacturing energy/cooling reduction:** Engineering thermotolerant production microbes can reduce cooling water demands. The yeast sHSP circuit paper explicitly motivates thermotolerance as affecting “energy consumption and product synthesis efficiency” and demonstrates improved growth at 42 °C. (zhang2023improvingthermotoleranceof pages 1-2)

3. **Food safety / pasteurization robustness risk:** Acid→heat cross-adaptation in *S. aureus* suggests that pre-exposure to sublethal stresses can compromise thermal inactivation in processing environments, which is relevant for risk assessment and process design. (liao2023preexposureoffoodborne pages 2-4)

4. **Pathogenic fungi / virulence:** For *Aspergillus fumigatus*, thermotolerance is described as a “remarkable virulence attribute,” and mechanistic links between heat-shock regulation and membrane lipid adaptation suggest potential antifungal strategies targeting lipid homeostasis or chaperone systems. (fabri2023theheatshock pages 6-7)

### 5) Candidate causal graph nodes (grouped by type)

#### 5.1 Environmental / experimental factors
- Elevated growth temperature / heat stress (label)
- Acid stress (acetic/citric/lactic), ethanol stress (industrial fermentation context) (label) (hua2024regulatorymechanismsof pages 11-13, liao2023preexposureoffoodborne pages 2-4)
- Adaptive laboratory evolution (ALE) / domestication selection pressure (label) (mcguire2023wholegenomesequencinganalysis pages 1-2, hua2024regulatorymechanismsof pages 11-13)

#### 5.2 Biological processes (GO candidates)
- Heat shock response (GO:0009408) (moon2023temperaturemattersbacterial pages 3-5)
- Protein folding / chaperone-mediated refolding (GO:0006457) (hua2024regulatorymechanismsof pages 11-13)
- Membrane homeostasis / lipid remodeling (label; GO mapping to be determined) (fabri2023theheatshock pages 6-7)
- Oxidative stress response (GO:0006979) (hua2024regulatorymechanismsof pages 11-13)

#### 5.3 Genes/proteins/regulators
**Bacteria (examples):**
- RpoH (sigma-32), RpoE (sigma-24/envelope stress) (hua2024regulatorymechanismsof pages 11-13, moon2023temperaturemattersbacterial pages 3-5)
- GroES/GroEL; DnaK/DnaJ/GrpE; ClpB (hua2024regulatorymechanismsof pages 11-13)
- Transporters: ansP (asparagine permease), dctA (C4-dicarboxylate transporter), glnD (uridylyltransferase PII) (matsumoto2023implicationofamino pages 2-5)

**Yeast/fungi:**
- Small HSPs (e.g., HSP12) (zhang2023improvingthermotoleranceof pages 1-2)
- HSF1 (yeast heat shock transcription factor; label) (salasnavarrete2023adaptiveresponsesof pages 1-2)
- HsfA (fungal heat shock transcription factor), SdeA (Δ9 fatty acid desaturase) (fabri2023theheatshock pages 6-7)

**Archaea:**
- vapBC4; VapC4 (RNase toxin) and VapB4 (antitoxin) (bhowmick2024roleofvapbc4 pages 1-2)

#### 5.4 Chemicals/metabolites (CHEBI candidates)
- Trehalose (CHEBI:16595) (foster2024analysisoffermentation pages 78-82)
- Mannitol (CHEBI:17214) (foster2024analysisoffermentation pages 78-82)
- Reactive oxygen species (ROS; label) and antioxidant systems (SOD/GPx/thioredoxin reductase; labels/GO mapping) (hua2024regulatorymechanismsof pages 11-13)
- Phospholipids (CHEBI class; label) and LPS (label) (matsumoto2023implicationofamino pages 2-5)

#### 5.5 Cellular structures / envelope features
- Plasma membrane integrity / rigidity / fluidity (label) (liao2023preexposureoffoodborne pages 2-4)
- Extracellular polysaccharide layer (EPS; label) (hua2024regulatorymechanismsof pages 11-13, hua2024regulatorymechanismsof media 8d6aa920)

### 6) Evidence-backed candidate causal edges (curation-ready table)
The table below is designed to be directly translatable into a TraitMech YAML edge list (with additional normalization as needed).

| Subject node (CURIE/label) | Predicate | Object node (CURIE/label) | Evidence snippet (verbatim quote) | Taxon/context | Assay/condition | DOI/URL + publication date | Notes/uncertainty for curation |
|---|---|---|---|---|---|---|---|
| groES/groEL (GO:0006457 / GroESL chaperonin system) | positively_regulates | thermotolerant growth at elevated temperature (METPO:1000619) | “In A. pasteurianus NBRC 3283, overexpression of groES/L and grpE-dnaK-dnaJ genes exhibited significantly enhanced growth activity at 42 °C.” (hua2024regulatorymechanismsof pages 11-13) | *Acetobacter pasteurianus* NBRC 3283 / AAB | Growth at 42 °C | DOI:10.1186/s12934-024-02602-y; https://doi.org/10.1186/s12934-024-02602-y; Nov 2024 | Strong edge for AAB; direct overexpression evidence, but taxon-specific. |
| grpE-dnaK-dnaJ (GO:0009408 / heat shock response chaperone system) | positively_regulates | thermotolerant growth at elevated temperature (METPO:1000619) | “In A. pasteurianus NBRC 3283, overexpression of groES/L and grpE-dnaK-dnaJ genes exhibited significantly enhanced growth activity at 42 °C.” (hua2024regulatorymechanismsof pages 11-13) | *Acetobacter pasteurianus* NBRC 3283 / AAB | Growth at 42 °C | DOI:10.1186/s12934-024-02602-y; https://doi.org/10.1186/s12934-024-02602-y; Nov 2024 | Strong but grouped operon-level evidence; gene-specific contributions not separated. |
| clpB (GO:0009408 / ClpB disaggregase) | required_for | high-temperature growth (label) | “Conversely, clpB knockout strains lost the ability to grow at high temperature.” (hua2024regulatorymechanismsof pages 11-13) | AAB review summarizing *A. pasteurianus* work | High-temperature growth | DOI:10.1186/s12934-024-02602-y; https://doi.org/10.1186/s12934-024-02602-y; Nov 2024 | Strong requirement claim, but source is a review summary rather than primary figure here. |
| rpoH (GO:0006355 / sigma-32 heat shock sigma factor) | positively_regulates | groEL,dnaKJ,grpE,clpB expression (label) | “The expression of groEL, dnaKJ, grpE, and clpB were regulated by the sigma factor for RNA polymerase RpoH, whose deletion led to heat sensitivity.” (hua2024regulatorymechanismsof pages 11-13) | AAB review; bacterial heat response | Heat stress / high temperature | DOI:10.1186/s12934-024-02602-y; https://doi.org/10.1186/s12934-024-02602-y; Nov 2024 | Good regulatory edge; curated object may need split into separate targets. |
| rpoH (GO:0006355 / sigma-32 heat shock sigma factor) | positively_regulates | thermotolerance (METPO:1000619) | “The expression of groEL, dnaKJ, grpE, and clpB were regulated by the sigma factor for RNA polymerase RpoH, whose deletion led to heat sensitivity.” (hua2024regulatorymechanismsof pages 11-13) | AAB review; bacterial heat response | Deletion phenotype under heat | DOI:10.1186/s12934-024-02602-y; https://doi.org/10.1186/s12934-024-02602-y; Nov 2024 | Direct phenotype support via deletion; broad/taxon-specific. |
| rpoE (GO:0009408 / envelope stress sigma factor) | positively_regulates | folding of membrane proteins and LPS biosynthesis (label) | “The activated RpoE not only induces expression of heat-shock-related proteins and periplasmic proteases, such as HtrA and DegP, but also induces genes involved in folding of membrane proteins and biosynthesis of lipopolysaccharides.” (moon2023temperaturemattersbacterial pages 3-5) | *Escherichia coli* heat-shock review | Heat shock in periplasm/envelope | DOI:10.1007/s12275-023-00031-x; https://doi.org/10.1007/s12275-023-00031-x; 2023-04-03 | Mechanistic heat-response edge; indirect link to thermotolerant growth rather than direct phenotype. |
| HSP12 (label; small heat shock protein) | positively_regulates | growth at 42 °C (label) | “Among them, No. 7 (YNL247wp-HSP12-SLM5t) and No. 11 (YNL247wp-sHSP-HB8-SLM5t), the two best performing engineered strains, exhibited a 19.8% and 17.2% increase in cell density, respectively, compared to the control strain.” (zhang2023improvingthermotoleranceof pages 1-2) | *Saccharomyces cerevisiae* engineered strains | 42 °C growth/cell viability | DOI:10.1039/d3ra05216h; https://doi.org/10.1039/d3ra05216h; Dec 2023 | Strong engineered-evidence for yeast; strain design context should be noted. |
| HSF1 (label; heat shock transcription factor) | positively_regulates | protein synthesis/folding/rescue genes (label) | “TAT12 and TTY23 ‘overexpressed key genes of protein synthesis, folding, rescue, and refolding’” and “Many chaperones under HSF1 control were upregulated in TAT12” (salasnavarrete2023adaptiveresponsesof pages 8-9) | *S. cerevisiae* ALE thermoacidic strains | Supraoptimal temperature + acid stress | DOI:10.1007/s00253-023-12556-7; https://doi.org/10.1007/s00253-023-12556-7; May 2023 | Useful regulatory edge, but snippet is summary from evidence extraction rather than direct full-text quotation; curate cautiously. |
| HSF1 (label; heat shock transcription factor) | positively_regulates | thermoacidic/thermotolerant phenotype (METPO:1000619) | “Tolerant strain TAT12 mutated genes encoding weak acid and heat response TFs HSF1, SKN7, and WAR1” and “TFs HSF1 and SKN7 likely controlled the transcription of metabolic genes associated to heat and acid tolerance” (salasnavarrete2023adaptiveresponsesof pages 1-2) | *S. cerevisiae* TAT12 | 30–39 °C with acidic pH/acetic acid | DOI:10.1007/s00253-023-12556-7; https://doi.org/10.1007/s00253-023-12556-7; May 2023 | Association is strong but causality partly inferred from evolved mutations/transcriptomics. |
| HsfA (label; fungal heat shock transcription factor) | positively_regulates | sdeA expression (label) | “Also, we demonstrate that hsfA controls sdeA expression” (fabri2023theheatshock pages 6-7) | *Aspergillus fumigatus* | Heat shock / membrane adaptation | DOI:10.1128/spectrum.01627-23; https://doi.org/10.1128/spectrum.01627-23; Jun 2023 | Strong direct regulatory edge in fungus. |
| HsfA (label; fungal heat shock transcription factor) | positively_regulates | plasma membrane adaptation to heat shock (label) | “Our results suggest that HsfA is required for the adaptation of the fungal plasma membrane to HS” (fabri2023theheatshock pages 6-7) | *A. fumigatus* | Heat shock | DOI:10.1128/spectrum.01627-23; https://doi.org/10.1128/spectrum.01627-23; Jun 2023 | Strong phenotype/process edge; object may be represented as biological process node. |
| sdeA / Δ9-fatty acid desaturase (label) | required_for | unsaturated fatty acid biosynthesis (label) | “we studied the A. fumigatus Δ9-fatty acid desaturase sdeA and discovered that this gene is essential and required for unsaturated FA biosynthesis” (fabri2023theheatshock pages 6-7) | *A. fumigatus* | Functional genetics under heat-relevant membrane study | DOI:10.1128/spectrum.01627-23; https://doi.org/10.1128/spectrum.01627-23; Jun 2023 | Strong direct mechanistic edge; thermotolerance link mediated through membrane composition. |
| unsaturated fatty acid biosynthesis (GO:0006636 / candidate) | contributes_to | thermotolerance (METPO:1000619) | “These findings suggest that forced dysregulation of saturated/unsaturated fatty acid balance might represent novel strategies” and “point out a sharp relationship between thermotolerance and FA metabolism in A. fumigatus.” (fabri2023theheatshock pages 6-7) | *A. fumigatus* | Heat shock | DOI:10.1128/spectrum.01627-23; https://doi.org/10.1128/spectrum.01627-23; Jun 2023 | Mechanistically plausible, but wording is partly interpretive; moderate confidence. |
| reduced membrane fluidity / altered fatty-acid composition (label) | positively_regulates | acid-heat cross-adaptation / heat tolerance (label) | “the ratio of anteiso to iso branched-chain fatty acids in the acid-heat-cross-adapted strain J15 decreased and the content of straight-chain fatty acids exhibited a 2.9 to 4.4% increase, contributing to the reduction in membrane fluidity.” (hua2024regulatorymechanismsof pages 11-13) | *Staphylococcus aureus* J15 | Organic acid pretreatment then heat | DOI:10.1128/spectrum.03832-22; https://doi.org/10.1128/spectrum.03832-22; Apr 2023 | Good assay-specific edge for cross-adaptation, not generic thermotolerance. |
| fabH (label; fatty acid biosynthesis enzyme) | positively_regulates | acid-heat cross-adaptation / heat tolerance (label) | “At the molecular level, fabH was overexpressed with preconditioning by organic acid, and its expression was further enhanced with subsequent heat exposure.” (hua2024regulatorymechanismsof pages 11-13) | *S. aureus* J15 | Organic acid preconditioning + heat | DOI:10.1128/spectrum.03832-22; https://doi.org/10.1128/spectrum.03832-22; Apr 2023 | Association strong; direct causal sufficiency not shown. |
| phospholipid + lipopolysaccharide increase (CHEBI/label) | positively_regulates | cell surface integrity (label) | “These mutations resulted in cell envelope modification, including increased phospholipid and lipopolysaccharide synthesis” (matsumoto2023implicationofamino pages 2-5) | *A. pasteurianus* TH-3 reconstructed mutants | 37–40 °C acetic acid fermentation | DOI:10.1128/jb.00101-23; https://doi.org/10.1128/jb.00101-23; Nov 2023 | Strong structural phenotype edge; can be split into PL and LPS nodes. |
| cell surface integrity (label) | positively_regulates | thermotolerance (METPO:1000619) | “The phenotypic changes may cooperatively work to make the adapted cell thermotolerant by enhancing cell surface integrity, nutrient or oxygen availability, and energy generation.” (matsumoto2023implicationofamino pages 2-5) | *A. pasteurianus* TH-3 | High-temperature growth / fermentation | DOI:10.1128/jb.00101-23; https://doi.org/10.1128/jb.00101-23; Nov 2023 | Explicit but author interpretation; suitable as higher-level process edge. |
| ansP / L-asparagine permease (label) loss-of-function | positively_regulates | thermotolerance (METPO:1000619) | “the dct gene (APT_01446) encoding the C4-dicarboxylate transporter of both TI and TH-3 strains had a dysfunctional mutation” and “the ∆ans ∆dct strain was more thermotolerant than each single mutant” (matsumoto2023implicationofamino pages 2-5) | *A. pasteurianus* TH-3-derived mutants | Dot spot + liquid fermentation at 37–40 °C | DOI:10.1128/jb.00101-23; https://doi.org/10.1128/jb.00101-23; Nov 2023 | Edge direction is for loss-of-function allele, not normal gene product. Represent as mutant allele or decreased transport activity. |
| dctA / C4-dicarboxylate transporter loss-of-function (label) | positively_regulates | thermotolerance (METPO:1000619) | “a dct-disrupted mutant, the ∆dct strain, was constructed and examined. It was more thermotolerant than SKU1108” (matsumoto2023implicationofamino pages 2-5) | *A. pasteurianus* | Elevated temperature 39.5–40 °C under fermentation | DOI:10.1128/jb.00101-23; https://doi.org/10.1128/jb.00101-23; Nov 2023 | Strong, but mutation/decreased function should be explicit in node/edge. |
| PMA1 / plasma membrane H+-ATPase (label) | positively_regulates | intracellular pH homeostasis under heat/acid (label) | “All evolved strains overexpress PMA1 (plasma membrane H+-ATPase), which pumps H+ out to counteract cytosolic acidification” (salasnavarrete2023adaptiveresponsesof pages 1-2) | *S. cerevisiae* evolved strains | Supraoptimal temperature plus low pH/acetic acid | DOI:10.1007/s00253-023-12556-7; https://doi.org/10.1007/s00253-023-12556-7; May 2023 | Good mechanism for thermoacidic tolerance; direct thermotolerance alone less isolated. |
| PMA1 / plasma membrane H+-ATPase (label) | positively_regulates | thermoacidic tolerance / growth at supraoptimal temperature (label) | “The integration of results revealed that evolved strains adjust their intracellular pH by H+ and acetic acid transport” (salasnavarrete2023adaptiveresponsesof pages 1-2) | *S. cerevisiae* TTY23/TAT12 | 30–39 °C with low pH/acetic acid | DOI:10.1007/s00253-023-12556-7; https://doi.org/10.1007/s00253-023-12556-7; May 2023 | Inferred from integration of multi-omics; moderate confidence for direct edge. |
| trehalose (CHEBI:16595) accumulation | positively_regulates | thermoadaptive growth / heat tolerance (label) | “high glucose (300 g/L) could effectively stimulate the gene expression of glucose transporters, trehalose synthesis pathways… under a high temperature” and “trehalose (Cmax, 8h = 369.00 ± 17.82 μg/g DCW)” (foster2024analysisoffermentation pages 78-82) | *Zygosaccharomyces rouxii* | 40 °C, high glucose | DOI:10.3390/jof10030185; https://doi.org/10.3390/jof10030185; Feb 2024 | Strong association but no direct knockout/rescue of trehalose pathway in this excerpt. |
| trehalose + mannitol compatible solutes (CHEBI:16595 / CHEBI:17214) | positively_regulates | conidial heat resistance (label) | “accumulation of mannitol and trehalose as the main compatible solutes during spore maturation is a key factor for heat resistance of conidia.” (foster2024analysisoffermentation pages 78-82) | *Aspergillus niger* conidia | Heat resistance of spores | DOI:10.1186/s40694-023-00168-9; https://doi.org/10.1186/s40694-023-00168-9; Nov 2023 | Strong for fungal spores/survival; less directly about vegetative thermotolerant growth. |
| antioxidant defense genes: SOD/GPx/thioredoxin reductase (GO/label) | positively_regulates | mitigation of heat-induced oxidative damage (label) | “genes associated with antioxidant defense, such as superoxide dismutases, glutathione peroxidases, and thioredoxin reductases, were significantly upregulated in A. pasteurianus TCBRC 103, suggesting that the strain can mitigate heat-induced oxidative damage” (hua2024regulatorymechanismsof pages 11-13) | *A. pasteurianus* TCBRC 103 | Heat stress, growth at 42 °C | DOI:10.1186/s12934-024-02602-y; https://doi.org/10.1186/s12934-024-02602-y; Nov 2024 | Good mechanism edge, but transcriptomic source partly unpublished per review. |
| catalase Ctt1 (label) | positively_regulates | oxidative-stress tolerance supporting thermotolerance (label) | “kveik constitutively accumulate high levels of catalase Ctt1 (Log2 fold 3.5–8x in non-stressed state)” (foster2024analysisoffermentation pages 78-82) | Norwegian kveik yeasts | Proteomics; H2O2 tolerance as heat-linked stress priming | Unknown journal/2024 context | Indirect support for thermotolerance via ROS defense; primary publication metadata unclear. |
| VapC4 toxin (label; toxin-antitoxin system) | positively_regulates | persister-like cell formation under heat stress (label) | “VapC4 toxin expression led to heat-induced persister-like cell formation, allowing the cell to cope with the stress.” (bhowmick2024roleofvapbc4 pages 1-2) | *Sulfolobus acidocaldarius* | Heat stress in thermoacidophilic archaeon | DOI:10.1128/mbio.02753-24; https://doi.org/10.1128/mbio.02753-24; 2024-11-13 | Strong direct edge, but mechanism is stress coping/persistence rather than growth promotion. |
| vapBC4 system expression (label) | positively_regulates | heat stress adaptation (label) | “During heat stress, the thermoacidophilic archaeon Sulfolobus acidocaldarius exhibited an increase in the expression of several bicistronic type II vapBC TA systems, with the highest expression observed in the vapBC4 system.” (bhowmick2024roleofvapbc4 pages 1-2) | *S. acidocaldarius* | Heat stress | DOI:10.1128/mbio.02753-24; https://doi.org/10.1128/mbio.02753-24; 2024-11-13 | Good stress-adaptation edge; may belong to persistence subgraph, not core facultative growth graph. |
| plasmid pOF39 carrying groESL (label) | maintained_by_selection_at | high temperature growth selection (label) | “we found that BM28 inexplicitly carries the groESL bearing plasmid pOF39 that was maintained simply by high-temperature selection pressure.” (mcguire2023wholegenomesequencinganalysis pages 1-2) | Heat-evolved *E. coli* BM28 | Adaptive evolution near Tmax | DOI:10.1186/s12864-023-09266-9; https://doi.org/10.1186/s12864-023-09266-9; Mar 2023 | Useful evolution edge; expresses selection relationship more directly than causal growth edge. |
| groESL-bearing plasmid pOF39 (label) | associated_with | thermotolerance evolution (label) | “Consistent with published findings of high GroESL expression in BM28, we found that BM28 inexplicitly carries the groESL bearing plasmid pOF39” (mcguire2023wholegenomesequencinganalysis pages 1-2) | Heat-evolved *E. coli* BM28 | Whole-genome sequencing of heat-evolved strains | DOI:10.1186/s12864-023-09266-9; https://doi.org/10.1186/s12864-023-09266-9; Mar 2023 | Association strong; direct sufficiency of plasmid not demonstrated in this paper. |
| large genomic deletions / regulatory mutations (label) | associated_with | evolved thermotolerance (label) | “We found three large deletions in the BM28 and BM28 ΔlysU strains of 123, 15 and 8.5 kb in length” and “mutations in master regulators such as the RNA polymerase and the transcriptional termination factor Rho.” (mcguire2023wholegenomesequencinganalysis pages 1-2) | Heat-evolved *E. coli* | Adaptive laboratory evolution toward Tmax | DOI:10.1186/s12864-023-09266-9; https://doi.org/10.1186/s12864-023-09266-9; Mar 2023 | Broad association only; individual deletions should not be curated causally without functional validation. |


*Table: This table compiles candidate causal edges for microbial thermotolerance, emphasizing experimentally supported mechanisms across bacteria, fungi, yeasts, and archaea. It is designed to help prioritize curatable nodes and edges for a TraitMech-style causal graph while flagging taxon-specific or indirect claims.*

### 7) Visual evidence (mechanism schematic)
Hua et al. (2024) provides a curated overview figure of **engineering strategies** (DBTL, multi-omics, gTME) and mechanistic themes (chaperones, membrane alteration, EPS) for stress tolerance in AAB that can be referenced during curation decisions. (hua2024regulatorymechanismsof media fe7a5a07, hua2024regulatorymechanismsof media b92d3210, hua2024regulatorymechanismsof media 8d6aa920, hua2024regulatorymechanismsof media 3518d8d5, hua2024regulatorymechanismsof media 6bf28d2f)

### 8) Warnings / claims not yet ready for strong curation
1. **Cross-adaptation survival vs thermotolerant growth:** *S. aureus* “cross-adaptation area” is a survival metric; do not directly equate to growth thermotolerance without growth assay evidence at elevated temperature. (liao2023preexposureoffoodborne pages 2-4)
2. **Review-level mechanistic summaries:** Some strong-sounding causal claims in the AAB review (e.g., clpB knockout abolishes high-T growth; rpoH deletion causes heat sensitivity) are summarized from prior work; ideally confirm with the primary cited studies before encoding as high-confidence universal edges. (hua2024regulatorymechanismsof pages 11-13)
3. **Persistence vs growth:** VapC4-driven persister-like formation indicates survival strategy that may involve growth arrest; include as a separate “heat stress coping” subgraph or mark as uncertain for growth-focused thermotolerant trait. (bhowmick2024roleofvapbc4 pages 1-2)
4. **Unpublished transcriptomic results:** The AAB review notes some “unpublished results” for ROS levels and transcriptomics in a specific strain; those edges should be marked as **uncertain** until corroborated by primary published datasets. (hua2024regulatorymechanismsof pages 11-13)

### DOI-first bibliography (with URLs and publication dates where available)

1. **Hua S, Wang Y, Wang L, et al.** Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. *Microbial Cell Factories*. **2024-11**. DOI: **10.1186/s12934-024-02602-y**. URL: https://doi.org/10.1186/s12934-024-02602-y (hua2024regulatorymechanismsof pages 11-13)
2. **Bhowmick A, Recalde A, Bhattacharyya C, et al.** Role of VapBC4 toxin-antitoxin system of *Sulfolobus acidocaldarius* in heat stress adaptation. *mBio*. **2024-11-13**. DOI: **10.1128/mbio.02753-24**. URL: https://doi.org/10.1128/mbio.02753-24 (bhowmick2024roleofvapbc4 pages 1-2)
3. **Fabri JHTM, Rocha MC, Fernandes CM, et al.** The Heat Shock Transcription Factor HsfA Plays a Role in Membrane Lipids Biosynthesis Connecting Thermotolerance and Unsaturated Fatty Acid Metabolism in *Aspergillus fumigatus*. *Microbiology Spectrum*. **2023-06**. DOI: **10.1128/spectrum.01627-23**. URL: https://doi.org/10.1128/spectrum.01627-23 (fabri2023theheatshock pages 6-7)
4. **Matsumoto N, Matsutani M, Tanimoto Y, et al.** Implication of amino acid metabolism and cell surface integrity for the thermotolerance mechanism in the thermally adapted acetic acid bacterium *Acetobacter pasteurianus* TH-3. *Journal of Bacteriology*. **2023-11**. DOI: **10.1128/jb.00101-23**. URL: https://doi.org/10.1128/jb.00101-23 (matsumoto2023implicationofamino pages 2-5)
5. **McGuire BE, Nano FE.** Whole-genome sequencing analysis of two heat-evolved *Escherichia coli* strains. *BMC Genomics*. **2023-03**. DOI: **10.1186/s12864-023-09266-9**. URL: https://doi.org/10.1186/s12864-023-09266-9 (mcguire2023wholegenomesequencinganalysis pages 1-2)
6. **Moon S, Ham S, Jeong J, et al.** Temperature Matters: Bacterial Response to Temperature Change. *Journal of Microbiology*. Published online **2023-04-03**. DOI: **10.1007/s12275-023-00031-x**. URL: https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 1-3)
7. **Zhang M-L, Zhang H, He Y-X, et al.** Improving thermo-tolerance of *Saccharomyces cerevisiae* by precise regulation of the expression of small HSP. *RSC Advances*. **2023-12**. DOI: **10.1039/d3ra05216h**. URL: https://doi.org/10.1039/d3ra05216h (zhang2023improvingthermotoleranceof pages 1-2)
8. **Liao X, Chen X, Sant’Ana AS, Feng J, Ding T.** Pre-Exposure of Foodborne *Staphylococcus aureus* Isolates to Organic Acids Induces Cross-Adaptation to Mild Heat. *Microbiology Spectrum*. **2023-04**. DOI: **10.1128/spectrum.03832-22**. URL: https://doi.org/10.1128/spectrum.03832-22 (liao2023preexposureoffoodborne pages 2-4)
9. **Salas-Navarrete PCC, Rosas-Santiago P, Suárez-Rodríguez R, Martínez A, Caspeta L.** Adaptive responses of yeast strains tolerant to acidic pH, acetate, and supraoptimal temperature. *Applied Microbiology and Biotechnology*. **2023-05**. DOI: **10.1007/s00253-023-12556-7**. URL: https://doi.org/10.1007/s00253-023-12556-7 (salasnavarrete2023adaptiveresponsesof pages 1-2)

---

### Notes for TraitMech YAML (`data/traits/environment/thermotolerant.yaml`)
- Prefer **growth-based assays** at defined elevated temperatures as primary evidence for METPO:1000619.
- Represent some edges as **allele-specific** (e.g., loss-of-function in ansP/dctA) rather than generic gene function where appropriate. (matsumoto2023implicationofamino pages 2-5)
- Consider a modular graph structure: *heat-shock proteostasis module*, *membrane/homeoviscous adaptation module*, *osmolyte/compatible-solute module*, *ROS defense module*, and *evolution/engineering module*.



References

1. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

2. (zhang2023improvingthermotoleranceof pages 1-2): Mei-ling Zhang, Hui Zhang, Ya-xin He, Zhao-hui Wu, and Ke Xu. Improving thermo-tolerance of saccharomyces cerevisiae by precise regulation of the expression of small hsp. RSC Advances, 13:36254-36260, Dec 2023. URL: https://doi.org/10.1039/d3ra05216h, doi:10.1039/d3ra05216h. This article has 21 citations and is from a peer-reviewed journal.

3. (mcguire2023wholegenomesequencinganalysis pages 1-2): Bailey E. McGuire and Francis E. Nano. Whole-genome sequencing analysis of two heat-evolved escherichia coli strains. BMC Genomics, Mar 2023. URL: https://doi.org/10.1186/s12864-023-09266-9, doi:10.1186/s12864-023-09266-9. This article has 9 citations and is from a peer-reviewed journal.

4. (liao2023preexposureoffoodborne pages 2-4): Xinyu Liao, Xin Chen, Anderson S. Sant'Ana, Jinsong Feng, and Tian Ding. Pre-exposure of foodborne staphylococcus aureus isolates to organic acids induces cross-adaptation to mild heat. Microbiology Spectrum, Apr 2023. URL: https://doi.org/10.1128/spectrum.03832-22, doi:10.1128/spectrum.03832-22. This article has 24 citations and is from a domain leading peer-reviewed journal.

5. (hua2024regulatorymechanismsof pages 11-13): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 44 citations and is from a peer-reviewed journal.

6. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

7. (fabri2023theheatshock pages 6-7): João Henrique Tadini Marilhano Fabri, Marina Campos Rocha, Caroline Mota Fernandes, Jonatas Erick Maimoni Campanella, Anderson Ferreira da Cunha, Maurizio Del Poeta, and Iran Malavazi. The heat shock transcription factor hsfa plays a role in membrane lipids biosynthesis connecting thermotolerance and unsaturated fatty acid metabolism in aspergillus fumigatus. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.01627-23, doi:10.1128/spectrum.01627-23. This article has 21 citations and is from a domain leading peer-reviewed journal.

8. (matsumoto2023implicationofamino pages 2-5): Nami Matsumoto, Minenosuke Matsutani, Yoko Tanimoto, Rina Nakanishi, Shuhei Tanaka, Yu Kanesaki, Gunjana Theeragool, Naoya Kataoka, Toshiharu Yakushi, and Kazunobu Matsushita. Implication of amino acid metabolism and cell surface integrity for the thermotolerance mechanism in the thermally adapted acetic acid bacterium <i>acetobacter pasteurianus</i> th-3. Journal of Bacteriology, Nov 2023. URL: https://doi.org/10.1128/jb.00101-23, doi:10.1128/jb.00101-23. This article has 5 citations and is from a peer-reviewed journal.

9. (foster2024analysisoffermentation pages 78-82): B Foster. Analysis of fermentation capabilities, trehalose metabolism, quantitative proteomics, and hybridisation of norwegian kveik brewing yeast. Unknown journal, 2024.

10. (bhowmick2024roleofvapbc4 pages 1-2): Arghya Bhowmick, Alejandra Recalde, Chandrima Bhattacharyya, Ankita Banerjee, Jagriti Das, Ulises E. Rodriguez-Cruz, Sonja-Verena Albers, and Abhrajyoti Ghosh. Role of vapbc4 toxin-antitoxin system of <i>sulfolobus acidocaldarius</i> in heat stress adaptation. Dec 2024. URL: https://doi.org/10.1128/mbio.02753-24, doi:10.1128/mbio.02753-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (hua2024regulatorymechanismsof media fe7a5a07): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 44 citations and is from a peer-reviewed journal.

12. (salasnavarrete2023adaptiveresponsesof pages 1-2): Prisciluis Caheri Salas-Navarrete, Paul Rosas-Santiago, Ramón Suárez-Rodríguez, Alfredo Martínez, and Luis Caspeta. Adaptive responses of yeast strains tolerant to acidic ph, acetate, and supraoptimal temperature. Applied Microbiology and Biotechnology, 107:4051-4068, May 2023. URL: https://doi.org/10.1007/s00253-023-12556-7, doi:10.1007/s00253-023-12556-7. This article has 40 citations and is from a domain leading peer-reviewed journal.

13. (hua2024regulatorymechanismsof media 8d6aa920): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 44 citations and is from a peer-reviewed journal.

14. (salasnavarrete2023adaptiveresponsesof pages 8-9): Prisciluis Caheri Salas-Navarrete, Paul Rosas-Santiago, Ramón Suárez-Rodríguez, Alfredo Martínez, and Luis Caspeta. Adaptive responses of yeast strains tolerant to acidic ph, acetate, and supraoptimal temperature. Applied Microbiology and Biotechnology, 107:4051-4068, May 2023. URL: https://doi.org/10.1007/s00253-023-12556-7, doi:10.1007/s00253-023-12556-7. This article has 40 citations and is from a domain leading peer-reviewed journal.

15. (hua2024regulatorymechanismsof media b92d3210): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 44 citations and is from a peer-reviewed journal.

16. (hua2024regulatorymechanismsof media 3518d8d5): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 44 citations and is from a peer-reviewed journal.

17. (hua2024regulatorymechanismsof media 6bf28d2f): Shengkai Hua, Yuqin Wang, Leyi Wang, Qinxuan Zhou, Zhitao Li, Peng Liu, Ke Wang, Yuanyuan Zhu, Dong Han, and Yongjian Yu. Regulatory mechanisms of acetic acid, ethanol and high temperature tolerances of acetic acid bacteria during vinegar production. Microbial Cell Factories, Nov 2024. URL: https://doi.org/10.1186/s12934-024-02602-y, doi:10.1186/s12934-024-02602-y. This article has 44 citations and is from a peer-reviewed journal.