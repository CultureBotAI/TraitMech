---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T10:56:46.874164'
end_time: '2026-08-04T11:05:22.669003'
duration_seconds: 515.79
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemoorganotrophic
  trait_identifier: METPO:1000663
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemoorganotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy through chemical
    oxidation of organic compounds that also serve as the carbon source for biosynthesis.
  parent_traits: METPO:1000631
  synonyms: chemoorganotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia
    chapter classifies chemotrophy by chemical rather than light energy sources.)
    | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review
    supports respiratory-chain energy conservation from redox reactions.)'
  causal_graph_summary: 'chemoorganotrophic_organic_oxidation_energy: 17 nodes, 15
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoorganotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000663
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy through chemical oxidation of organic compounds that also serve as the carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical rather than light energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory-chain energy conservation from redox reactions.)
- **Existing causal graph summary:** chemoorganotrophic_organic_oxidation_energy: 17 nodes, 15 edges

## Research Objective

Research the microbial trait **chemoorganotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganotrophic.yaml`.

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
- **Trait label:** chemoorganotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000663
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy through chemical oxidation of organic compounds that also serve as the carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoorganotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: chemical energy (Encyclopedia chapter classifies chemotrophy by chemical rather than light energy sources.) | DOI:10.1016/j.bbabio.2008.09.008: membrane-bound electron transport chain (Review supports respiratory-chain energy conservation from redox reactions.)
- **Existing causal graph summary:** chemoorganotrophic_organic_oxidation_energy: 17 nodes, 15 edges

## Research Objective

Research the microbial trait **chemoorganotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoorganotrophic.yaml`.

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


# Curation report: chemoorganotrophic

## 1. Trait scope

**Trait:** chemoorganotrophic  
**Identifier:** **“METPO:1000663”**  
**Category/kind/status:** PHYSIOLOGY / CLASS / REVIEWED  
**Parent:** METPO:1000631  
**Synonym:** chemoorganotroph

### Working definition

Chemoorganotrophy is a trophic strategy in which **organic compounds supply both chemical energy and carbon for biosynthesis**. The defining feature is therefore the coupling of organic-substrate catabolism to cellular energy conservation and biomass formation—not the use of any particular substrate, pathway, electron acceptor, respiratory complex, or oxygen regime. Organic matter may be processed by respiration or fermentation. A recent soil-carbon review similarly describes organic substances as energy sources for chemoorganotrophs and notes that respiration oxidizes their carbon and returns CO₂ to the atmosphere. (azevedo2024microbialcontributionto pages 1-2)

The most defensible TraitMech architecture is consequently a **small universal core with alternative respiratory and fermentative modules**:

1. organic compound availability and uptake;
2. intracellular organic-substrate catabolism;
3. generation of carbon intermediates and reduced electron carriers;
4. energy conservation by either respiratory phosphorylation, substrate-level phosphorylation, or both;
5. ATP and precursor supply supporting biosynthesis and growth.

### Boundaries and nearby traits

- **Versus phototrophy:** chemoorganotrophy derives energy from chemical oxidation, whereas phototrophy derives energy from light. An organism may switch between these modes; *Chloroflexus* and related Chloroflexota include photoheterotrophic and dark chemoheterotrophic states. Such facultative organisms should receive both traits only when each state is supported independently. (freches2024thebiotechnologicalpotential pages 1-4, freches2024thebiotechnologicalpotential pages 12-14)
- **Versus chemolithotrophy:** chemolithotrophs use inorganic electron donors. The mere presence of an organic carbon assimilation pathway does not establish chemoorganotrophy if energy is derived from H₂, sulfide, ammonia, Fe²⁺, or another inorganic donor.
- **Versus heterotrophy:** heterotrophy specifies reliance on organic carbon; chemoorganotrophy additionally specifies chemical energy from organic-compound oxidation. In routine microbiological descriptions, “chemoheterotroph” and “chemoorganoheterotroph” are often used nearly synonymously with chemoorganotroph, but ontology mappings should preserve the energy-source and carbon-source axes.
- **Respiration is not required:** aerobic and anaerobic respiration are valid realizations, but fermentation is also chemoorganotrophic when an organic substrate supplies the energy and carbon.
- **Fermentation boundary:** the canonical definition is anaerobic catabolism in which organic compounds act as both electron donor and acceptor, with ATP produced mainly by substrate-level phosphorylation. Nitrate and sulfur respiration, hydrogenotrophic homoacetogenesis, hydrogenotrophic methanogenesis, and anaerobic phototrophy are not fermentation. Proton-, CO₂-, and H₂-linked cases complicate this simple boundary. (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 2-3)
- **Mixotrophy:** organisms simultaneously or conditionally using organic and inorganic donors should not be assigned a universal organic-donor mechanism without growth or flux evidence showing that organic oxidation contributes energy.
- **Assimilation alone is insufficient:** incorporation of acetate or another organic molecule into biomass does not prove that its oxidation conserves energy.

## 2. Current mechanistic understanding

### Respiratory branch

Organic carbon catabolism through pathways such as glycolysis and the tricarboxylic-acid cycle extracts electrons into NADH and protein-bound FADH₂. Electrons then pass through membrane-associated redox cofactors and complexes to a terminal acceptor. The free energy of electron transfer generates an electrochemical ion gradient—usually a proton-motive force—which drives ATP synthesis. Proton pumping, quinone/quinol cycling, and redox loops are alternative mechanisms for building that gradient. (simon2008theorganisationof pages 1-3)

Bacterial Complex I illustrates this coupling: it transfers electrons reversibly from NADH to membrane-bound quinone while generating proton-motive force. It is important but **not universal**. A survey found Complex I in approximately half of representative bacterial genomes; its direction, donor, and physiological role differ among taxa. In *Escherichia coli* it supports anaerobic fumarate respiration, whereas in phototrophic *Rhodobacter capsulatus* it can run in reverse. (spero2015phylogenomicanalysisand pages 1-2)

### Fermentative branch

Fermentation uses internal redox balancing rather than an obligatory external terminal acceptor. Glycolytic or pentose-phosphate entry commonly produces pyruvate, which feeds diverse routes producing acetate, lactate, ethanol, formate, succinate, propionate, butyrate, CO₂, and H₂. ATP is commonly generated by substrate-level phosphorylation. Electron-transport chains should not, however, be excluded categorically: a 2024 synthesis reports that electron transport plus ATP synthase can supply as much as one-third of total ATP in at least one studied fermenter. (hackmann2024thevastlandscape pages 3-4, hackmann2024thevastlandscape pages 4-5)

### Environmental modulation

The trait itself is not an environmental preference. Oxygen availability instead selects among aerobic respiration, anaerobic respiration, fermentation, or metabolic switching. Temperature, moisture, pH, nutrient status, redox potential, and organic-matter quality regulate microbial organic-carbon processing in soils. These should be represented as contextual modifiers rather than necessary components of chemoorganotrophy. (azevedo2024microbialcontributionto pages 1-2)

## 3. Candidate nodes

Only identifiers that can be assigned confidently are given below; unresolved entities should remain label-only until checked against the target ontology release.

### Trait and process nodes

- chemoorganotrophic — **METPO:1000663**
- organic-compound catabolic process — **GO:1901575**
- glycolytic process — **GO:0006096**
- tricarboxylic-acid cycle — **GO:0006099**
- cellular respiration — **GO:0045333**
- aerobic respiration — **GO:0009060**
- anaerobic respiration — **GO:0009061**
- fermentation — **GO:0006113**
- oxidative phosphorylation — **GO:0006119**
- ATP synthesis coupled proton transport — **GO:0015986**
- substrate-level phosphorylation — label-only pending ontology validation
- organic-carbon mineralization — label-only
- biomass biosynthesis/growth — label-only or more assay-specific GO term

### Chemicals and energetic entities

- oxygen — **CHEBI:15379**
- water — **CHEBI:15377**
- carbon dioxide — **CHEBI:16526**
- ATP — **CHEBI:15422**
- ADP — **CHEBI:16761**
- NADH — **CHEBI:16908**
- NAD⁺ — **CHEBI:15846**
- pyruvate — **CHEBI:15361**
- glucose — **CHEBI:17234**
- proton — **CHEBI:15378**
- organic compound, organic electron donor, quinone pool, quinol pool, FADH₂, fermentation products, and biomass precursors — retain as labels until the exact intended chemical class or species is selected
- alternative terminal acceptors: nitrate, fumarate, ferric iron, sulfur compounds, and extracellular minerals—add only to explicitly supported taxon/pathway modules

### Proteins, complexes, and molecular functions

- proton-translocating NADH:quinone oxidoreductase/respiratory Complex I — **GO:0008137** for NADH dehydrogenase (ubiquinone) activity; the bacterial core is commonly encoded by **nuoA–nuoN**
- respiratory-chain complex I — **GO:0045271**
- proton-transporting ATP synthase complex — **GO:0045259**
- electron-transfer activity — **GO:0009055**
- quinone-reactive respiratory complexes, terminal oxidases, terminal reductases, succinate dehydrogenase, cytochrome complexes, substrate transporters, extracellular hydrolases, glycolytic enzymes, and fermentation kinases — label or family-specific nodes until the organism and reaction are fixed

Complex I should not be treated as a required marker. Its occurrence and function vary substantially across bacteria, and some organisms use alternative dehydrogenases or modified Complex I enzymes. (spero2015phylogenomicanalysisand pages 1-2)

### Cellular locations

- plasma membrane — **GO:0005886**
- cytoplasm — **GO:0005737**
- extracellular region — **GO:0005576**
- periplasmic space — **GO:0042597**
- mitochondrial inner membrane — **GO:0005743**, relevant only to microbial eukaryotes

### Environmental and experimental factors

- organic-substrate identity and concentration
- oxygen concentration/headspace
- supplied terminal electron acceptor
- temperature, pH, salinity, moisture, and redox potential
- light/dark condition for facultative phototrophs
- growth, substrate depletion, CO₂ evolution, O₂ consumption, ATP yield, reduced-product formation, respiratory-inhibitor response, and isotope-tracer incorporation

These factors should normally be encoded as assay context or regulatory nodes—not as definitional parts of the phenotype.

### Example taxonomic/context nodes

- Bacteria — **NCBITaxon:2**
- *Escherichia coli* — **NCBITaxon:562**, contextual Complex-I/fumarate-respiration example
- Chloroflexota — phylum-level label pending verification against the NCBI taxonomy release used by TraitMech
- Anaerolineae — class-level label; recent review describes members as strictly anaerobic chemoorganotrophs isolated from digesters, hot springs, and subseafloor sediments. (freches2024thebiotechnologicalpotential pages 1-4)

## 4. Candidate causal edges

The compact high-confidence set is summarized first.

| subject | predicate | object | branch | evidence DOI | confidence/applicability |
|---|---|---|---|---|---|
| chemoorganotrophy (METPO:1000663) | has_energy_source | organic compounds (CHEBI:59999) | core | 10.1515/psr-2016-0118 | High; direct definition that chemoorganotrophs use organic compounds for energy and as carbon source; broad microbial applicability (briski2017environmentalmicrobiology pages 1-3) |
| organic carbon catabolism | generates | NADH | core | 10.1016/j.bbabio.2008.09.008 | High; review states electrons are extracted from organic carbon during glycolysis/TCA and passed via NADH; broad respiration applicability (simon2008theorganisationof pages 1-3) |
| organic carbon catabolism | generates | FADH2 | core | 10.1016/j.bbabio.2008.09.008 | High; same review explicitly names FADH2 as carrier feeding electron transport; broad respiration applicability (simon2008theorganisationof pages 1-3) |
| glycolysis | causally_upstream_of | pyruvate formation | core | 10.1093/femsre/fuae016 | High; 2024 review maps glucose fermentation with glycolytic entry to pyruvate as central intermediate; broad prokaryotic applicability (hackmann2024thevastlandscape pages 1-2, hackmann2024thevastlandscape pages 4-5) |
| NADH:quinone oxidoreductase (Complex I) | oxidizes | NADH | aerobic respiration | 10.1128/mbio.00389-15 | High; direct mechanistic statement for bacterial Complex I; broad but not universal across chemoorganotrophs (spero2015phylogenomicanalysisand pages 1-2) |
| NADH:quinone oxidoreductase (Complex I) | reduces | quinone | aerobic respiration | 10.1128/mbio.00389-15 | High; direct mechanistic statement that Complex I transfers electrons from NADH to membrane-bound quinone; broad but not universal (spero2015phylogenomicanalysisand pages 1-2) |
| electron transport chain | generates | proton motive force | aerobic respiration | 10.1016/j.bbabio.2008.09.008 | High; authoritative review states membrane-bound electron transport transduces redox energy into electrochemical ion gradient; broad aerobic/anaerobic respiratory applicability (simon2008theorganisationof pages 1-3) |
| proton motive force | drives | ATP synthase | aerobic respiration | 10.1016/j.bbabio.2008.09.008 | High; direct review statement that pmf drives ATP synthesis; broad respiratory applicability (simon2008theorganisationof pages 1-3) |
| electron transport pathway | ultimately reduces | oxygen (CHEBI:15379) to water (CHEBI:15377) | aerobic respiration | 10.1016/j.bbabio.2008.09.008 | High; direct statement for aerobic respiration branch only (simon2008theorganisationof pages 1-3) |
| fumarate respiration | requires | Complex I | anaerobic respiration | 10.1128/mbio.00389-15 | Medium; direct but taxon-specific to *Escherichia coli* anaerobic fumarate respiration, so curate as contextual/example edge only (spero2015phylogenomicanalysisand pages 1-2) |
| fermentation | uses_as_electron_donor | organic compound | fermentation | 10.1093/femsre/fuae016 | High; 2024 review definition of fermentation as anaerobic catabolism with organic compound electron donor; broad fermentative applicability (hackmann2024thevastlandscape pages 2-3) |
| fermentation | uses_as_electron_acceptor | organic compound | fermentation | 10.1093/femsre/fuae016 | High; same 2024 review defines organic compound as electron acceptor in canonical fermentation; broad but note edge cases with H+, H2, CO2 (hackmann2024thevastlandscape pages 2-3) |
| fermentation | produces_ATP_via | substrate-level phosphorylation | fermentation | 10.1093/femsre/fuae016 | High; direct 2024 review definition, though review notes some fermenters also gain ATP via ETC/ATP synthase; broad with caveat (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 3-4) |
| complex organic matter degradation | supplies_substrates_for | chemoorganotrophic metabolism | core | 10.1128/aem.01756-23 | Medium; supported in Chloroflexota examples degrading complex organic compounds, useful as ecological input edge but currently taxon-skewed (freches2024thebiotechnologicalpotential pages 1-4, freches2024thebiotechnologicalpotential pages 12-14) |


*Table: This table compiles 14 high-confidence, curation-oriented causal edges for chemoorganotrophy, spanning core substrate use, respiratory energy conservation, and fermentation. It is useful as a compact starting set for TraitMech graph curation because each edge is tied to available evidence contexts and notes on breadth versus taxon-specificity.*

The following expanded table supplies curation snippets and caveats. Quotation marks denote short excerpts or close source wording.

| # | Proposed subject–predicate–object | Evidence and supporting snippet | Curation note |
|---|---|---|---|
| 1 | **chemoorganotrophy — has energy source — organic compounds** | DOI **10.1515/psr-2016-0118** (2017): “chemoorganotrophs use organic compounds for energy and as a carbon source.” (briski2017environmentalmicrobiology pages 1-3) | **High confidence; definitional.** Organic-compound class needs ontology verification. |
| 2 | **chemoorganotrophy — has carbon source — organic compounds** | Same direct definition above. (briski2017environmentalmicrobiology pages 1-3) | **High confidence; definitional.** Do not infer that every atom of biomass derives from the same individual substrate. |
| 3 | **organic-substrate catabolism — generates — biosynthetic carbon intermediates** | The soil review states organic substances are both energy sources and carbon stocks and are transformed through catabolic and anabolic activity. DOI **10.36783/18069657rbcs20230065** (2024). (azevedo2024microbialcontributionto pages 1-2) | **High-level core edge.** A specific precursor pathway requires organism-level evidence. |
| 4 | **organic-carbon catabolism — generates — NADH** | DOI **10.1016/j.bbabio.2008.09.008** (2008): electrons are extracted from organic carbon through “glycolysis and the tricarboxylic acid cycle” and passed via carriers “such as NADH.” (simon2008theorganisationof pages 1-3) | **High for respiratory central metabolism; not universal to every substrate or organism.** |
| 5 | **organic-carbon catabolism — generates — FADH₂-bound reducing equivalents** | Same review names protein-bound FADH₂ among carriers entering electron transport. (simon2008theorganisationof pages 1-3) | **Moderate–high.** Prefer enzyme-bound flavin wording; free FADH₂ can be chemically misleading. |
| 6 | **glycolysis — produces — pyruvate** | The 2024 fermentation synthesis identifies glycolytic entry to pyruvate and subsequent product-forming routes. DOI **10.1093/femsre/fuae016** (May 2024). (hackmann2024thevastlandscape pages 4-5) | **High for glucose-utilizing branch, not universal to all organotrophs.** |
| 7 | **Complex I — oxidizes — NADH** | DOI **10.1128/mbio.00389-15** (2015): “Complex I catalyzes the reversible transfer of electrons from…NADH to membrane-bound quinone.” (spero2015phylogenomicanalysisand pages 1-2) | **High mechanism; optional module.** Direction can reverse in some physiological contexts. |
| 8 | **Complex I — reduces — quinone** | Same direct mechanistic statement. (spero2015phylogenomicanalysisand pages 1-2) | **High but not universal.** Quinone species varies among taxa. |
| 9 | **Complex I — contributes to generation of — proton-motive force** | The reaction is explicitly described as coupled to PMF generation. (spero2015phylogenomicanalysisand pages 1-2) | **High for forward respiratory operation.** |
| 10 | **respiratory electron-transfer reaction — generates — electrochemical ion gradient** | DOI **10.1016/j.bbabio.2008.09.008**: free redox energy is transduced into an electrochemical ion, usually proton, gradient. (simon2008theorganisationof pages 1-3) | **High; broad respiratory edge.** Some organisms use Na⁺ or non-proton-motive redox loops. |
| 11 | **quinone/quinol cycling — contributes to — proton-motive force** | The same review names “proton pumping, quinone/quinol cycling or…a redox loop” as PMF-building mechanisms. (simon2008theorganisationof pages 1-3) | **High as one alternative mechanism, not obligatory.** |
| 12 | **proton-motive force — drives — ATP synthesis** | The respiratory review states that the electrochemical gradient “drives ATP synthesis.” (simon2008theorganisationof pages 1-3) | **High.** ATP synthase is the mechanistic mediator and should be represented explicitly. |
| 13 | **respiratory electron-transfer pathway — reduces — O₂ to H₂O** | Electrons migrate through membrane-associated redox cofactors and “ultimately reduce oxygen to water.” (simon2008theorganisationof pages 1-3) | **High for aerobic-respiration branch only.** |
| 14 | **alternative terminal electron acceptor availability — enables — anaerobic respiration** | Bacteria can couple diverse donors to oxygen or “other terminal electron acceptors”; *E. coli* Complex I supports fumarate respiration. (spero2015phylogenomicanalysisand pages 1-2) | **General relation plus taxon-specific example.** Curate each acceptor with direct organism-level evidence. |
| 15 | **fermentation — uses electron donor — organic compound** | DOI **10.1093/femsre/fuae016**: “anaerobic catabolism in which an organic compound is both an electron donor and an electron acceptor.” (hackmann2024thevastlandscape pages 2-3) | **High for canonical fermentation.** |
| 16 | **fermentation — uses electron acceptor — organic compound** | Same definition. (hackmann2024thevastlandscape pages 2-3) | **High with boundary caveat:** H⁺ or CO₂ can participate in some accepted fermentation cases. |
| 17 | **fermentative pathway — produces ATP via — substrate-level phosphorylation** | The 2024 review states ATP is produced by substrate-level phosphorylation. (hackmann2024thevastlandscape pages 2-3) | **High but not exclusive.** Do not assert absence of ETC-based energy conservation. |
| 18 | **fermentative pyruvate metabolism — produces — reduced organic end products** | The review lists acetate, lactate, formate, ethanol, succinate, propionate, and butyrate among products. (hackmann2024thevastlandscape pages 4-5) | **High at class level; individual products are pathway/taxon dependent.** |
| 19 | **fermentative electron transport plus ATP synthase — contributes to — ATP production** | ETC and ATP synthase can contribute “up to 1/3” of ATP in one studied organism. (hackmann2024thevastlandscape pages 3-4) | **Uncertain/taxon-specific.** Do not elevate to a universal fermentation edge. |
| 20 | **complex-organic-matter degradation — supplies — fermentable/respirable substrates** | A 2024 Chloroflexota review reports carbohydrate hydrolysis, proteolysis, and degradation of recalcitrant organic matter. DOI **10.1128/aem.01756-23**. (freches2024thebiotechnologicalpotential pages 12-14) | **Ecologically plausible but currently taxon-skewed.** Separate extracellular depolymerization from intracellular chemoorganotrophy. |
| 21 | **chemoorganotrophic organic-carbon oxidation — produces — CO₂ efflux** | The 2024 soil review states respiration oxidizes carbon and emits CO₂ and links microbial mineralization to soil-carbon efflux. (azevedo2024microbialcontributionto pages 1-2) | **High for complete/mineralizing oxidation, not for all growth conditions.** |
| 22 | **oxygen availability — modulates — respiratory/fermentative strategy** | Chloroflexota span aerobic and anaerobic conditions; their diversity is shaped by interplay among oxygen availability, temperature, and energy metabolism. (freches2024thebiotechnologicalpotential pages 1-4) | **Moderate; contextual, phylum-focused evidence.** |
| 23 | **temperature/moisture/pH/redox/organic-matter quality — modulate — microbial organic-carbon flux** | These factors are explicitly identified in the 2024 soil review. (azevedo2024microbialcontributionto pages 1-2) | **High environmentally, but not a universal molecular mechanism.** Encode as context or regulatory edges. |
| 24 | **organic-substrate catabolism — supplies energy and precursors for — growth/biomass synthesis** | The definitional source and soil review jointly support organic compounds as energy and carbon sources. (briski2017environmentalmicrobiology pages 1-3, azevedo2024microbialcontributionto pages 1-2) | **High phenotype-level endpoint.** Avoid claiming growth without an assay-specific observation. |

## 5. Recent developments and quantitative evidence

The major 2024 conceptual development is recognition that fermentation is much more diverse—and mechanistically less separable from membrane bioenergetics—than older textbook definitions imply. Analysis of descriptions for **8,300 prokaryotes** found that **more than one-quarter** ferment; fermentation was reported across **162 genera**, using **46 chemically defined substrates**, producing **55 end products**, and yielding nearly **300 product combinations**. The same review maps more than **120 biochemical reactions** associated with glucose fermentation. (hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 1-2)

Recent genomics and enzymology are also exposing pathway variants hidden by phenotype labels. Examples include distinct acetate-forming enzymes and ferredoxin-linked redox-balancing systems in particular taxa. These findings argue against making a single enzyme or canonical glucose pathway necessary for the broad chemoorganotrophic class. (hackmann2024thevastlandscape pages 4-5)

A 2024 synthesis of Chloroflexota illustrates ecophysiological breadth: members occur under aerobic, anaerobic, thermophilic, and microaerophilic conditions and use carbohydrates, volatile fatty acids, and complex organic matter. Reported examples include Anaerolineae abundances of approximately **5–25%** in some sediment communities, growth temperatures reaching **72.5–75°C** for Thermoflexia, and microaerophilic growth at approximately **1% O₂**. These are useful contextual data but must not be generalized to all chemoorganotrophs. (freches2024thebiotechnologicalpotential pages 6-9)

## 6. Applications and real-world implementation

- **Wastewater and anaerobic digestion:** chemoorganotrophic consortia hydrolyze and ferment complex organic matter, generate volatile fatty acids, and support respiratory or methanogenic partner guilds. Chloroflexota are repeatedly associated with digesters and wastewater systems; reported respiratory components include NADH dehydrogenase, succinate dehydrogenase, and oxygen reductases. These are community- and taxon-specific implementations, not universal trait markers. (freches2024thebiotechnologicalpotential pages 1-4, freches2024thebiotechnologicalpotential pages 14-15)
- **Bioremediation:** metabolic versatility supports transformation of xenobiotics and recalcitrant organic contaminants; particular organisms can couple organic oxidation to oxygen, nitrate, ferric iron, or extracellular acceptors. Chloroflexota applications include treatment of organic and metal contamination and sediment decontamination. (freches2024thebiotechnologicalpotential pages 12-14, freches2024thebiotechnologicalpotential pages 14-15)
- **Industrial fermentation:** fermentative chemoorganotrophs produce biofuels, commodity chemicals, foods, and value-added metabolites. Current manipulation strategies include genetic engineering, electrofermentation, probiotics, and enzyme inhibition. (hackmann2024thevastlandscape pages 1-2)
- **Agriculture and host systems:** fermenters influence livestock nutrition and human gut metabolism, while soil chemoorganotrophs regulate decomposition, nutrient release, carbon storage, and CO₂ efflux. (azevedo2024microbialcontributionto pages 1-2, hackmann2024thevastlandscape pages 1-2)
- **Microbial fuel cells and biocatalysis:** recent Chloroflexota literature describes sugar-fed microbial-fuel-cell associations and enzymes of industrial interest, but evidence is presently organism- or community-specific. (freches2024thebiotechnologicalpotential pages 6-9)

## 7. Expert interpretation for TraitMech

The broad trait should be modeled as a **disjunctive phenotype**, not as one linear universal pathway. The universal causal commitment is limited to:

**organic compound availability → organic-substrate catabolism → chemical energy conservation + organic-carbon precursor supply → ATP/reducing power/biomass production.**

Respiration and fermentation should be child modules. Complex I, quinones, oxygen, nitrate, fumarate, terminal oxidases, terminal reductases, extracellular hydrolases, and specific fermentation products are optional or contextual. This interpretation is supported by the documented diversity of respiratory-chain architecture and by the 2024 finding that fermentation spans dozens of substrates and products and can sometimes include membrane-based energy conservation. (simon2008theorganisationof pages 1-3, spero2015phylogenomicanalysisand pages 1-2, hackmann2024thevastlandscape pages 3-4, hackmann2024thevastlandscape pages 2-3)

## 8. Warnings: claims not yet suitable for unconditional curation

1. **Do not make Complex I necessary or sufficient.** It is widespread but absent from many bacteria and can function in forward or reverse directions. (spero2015phylogenomicanalysisand pages 1-2)
2. **Do not equate chemoorganotrophy with aerobic respiration.** Anaerobic respiration and fermentation are valid realizations.
3. **Do not require oxygen, a complete TCA cycle, glycolysis, or a specific terminal acceptor.** Each is branch- or substrate-dependent.
4. **Do not define fermentation solely by absence of an electron-transport chain.** Some fermenters use ETC/ATP-synthase energy conservation. (hackmann2024thevastlandscape pages 3-4)
5. **Do not infer the trait from an organic-carbon transporter, catabolic gene, or genome annotation alone.** Presence does not establish expression, flux, energy conservation, or growth.
6. **Do not infer chemoorganotrophy from organic-carbon assimilation alone.** The organic compound must contribute chemical energy as well as carbon under the relevant condition.
7. **Do not generalize Chloroflexota examples to all microbes.** Temperature, salinity, oxygen tolerance, denitrification, pollutant degradation, and particular enzyme complements are taxon-specific. (freches2024thebiotechnologicalpotential pages 12-14, freches2024thebiotechnologicalpotential pages 6-9, freches2024thebiotechnologicalpotential pages 14-15)
8. **Treat environmental correlations as modifiers, not defining causes.** Soil moisture, pH, temperature, and redox state alter activity but do not define the trophic class. (azevedo2024microbialcontributionto pages 1-2)
9. **Verify every CURIE against the versions used by TraitMech.** Broad chemical labels such as “organic compound,” “quinone pool,” and “biomass precursor” should remain label-only until their intended semantic scope is fixed.
10. **Preserve assay context.** Growth on glucose in air, substrate disappearance without growth, CO₂ evolution, fermentation-product formation, and genomic pathway prediction provide different levels of evidence.

## 9. DOI-first bibliography

1. Hackmann TJ. **The vast landscape of carbohydrate fermentation in prokaryotes.** *FEMS Microbiology Reviews.* Published May 2024. DOI: [10.1093/femsre/fuae016](https://doi.org/10.1093/femsre/fuae016). (hackmann2024thevastlandscape pages 3-4, hackmann2024thevastlandscape pages 2-3, hackmann2024thevastlandscape pages 1-2)
2. Freches A, Costa Fradinho J. **The biotechnological potential of the Chloroflexota phylum.** *Applied and Environmental Microbiology.* Published 6 May 2024; June 2024 issue. DOI: [10.1128/aem.01756-23](https://doi.org/10.1128/aem.01756-23). (freches2024thebiotechnologicalpotential pages 1-4, freches2024thebiotechnologicalpotential pages 12-14)
3. Azevedo LCB, et al. **Microbial contribution to the carbon flux in the soil: A literature review.** *Revista Brasileira de Ciência do Solo.* 2024;48:e0230065. Received 5 June 2023; approved 21 November 2023. DOI: [10.36783/18069657rbcs20230065](https://doi.org/10.36783/18069657rbcs20230065). (azevedo2024microbialcontributionto pages 1-2)
4. Spero MA, Aylward FO, Currie CR, Donohue TJ. **Phylogenomic analysis and predicted physiological role of the proton-translocating NADH:quinone oxidoreductase (Complex I) across bacteria.** *mBio.* Published March–April 2015. DOI: [10.1128/mbio.00389-15](https://doi.org/10.1128/mbio.00389-15). (spero2015phylogenomicanalysisand pages 1-2)
5. Simon J, van Spanning RJM, Richardson DJ. **The organisation of proton motive and non-proton motive redox loops in prokaryotic respiratory systems.** *Biochimica et Biophysica Acta.* Published December 2008; available online 30 September 2008. DOI: [10.1016/j.bbabio.2008.09.008](https://doi.org/10.1016/j.bbabio.2008.09.008). (simon2008theorganisationof pages 1-3)
6. Briški F, Vuković Domanovac M. **Environmental microbiology.** *Physical Sciences Reviews.* Published October 2017. DOI: [10.1515/psr-2016-0118](https://doi.org/10.1515/psr-2016-0118). (briski2017environmentalmicrobiology pages 1-3)

### Recommended initial YAML strategy

Curate the definitional organic-energy and organic-carbon edges plus a common endpoint in ATP/precursor-supported growth. Represent **respiration**, **fermentation**, and **extracellular polymer degradation** as optional subgraphs. Add Complex I, terminal acceptors, individual enzymes, products, and environmental modifiers only with explicit taxon and experimental-condition qualifiers.

References

1. (azevedo2024microbialcontributionto pages 1-2): Lucas Carvalho Basilio Azevedo, Simone Cristina Braga Bertini, Adão Siqueira Ferreira, Nathalia Silva Rodovalho, Luiz Fernando Romanholo Ferreira, and Ajay Kumar. Microbial contribution to the carbon flux in the soil: a literature review. Revista Brasileira de Ciência do Solo, Jan 2024. URL: https://doi.org/10.36783/18069657rbcs20230065, doi:10.36783/18069657rbcs20230065. This article has 30 citations.

2. (freches2024thebiotechnologicalpotential pages 1-4): André Freches and Joana Costa Fradinho. The biotechnological potential of the <i>chloroflexota</i> phylum. Jun 2024. URL: https://doi.org/10.1128/aem.01756-23, doi:10.1128/aem.01756-23. This article has 129 citations and is from a peer-reviewed journal.

3. (freches2024thebiotechnologicalpotential pages 12-14): André Freches and Joana Costa Fradinho. The biotechnological potential of the <i>chloroflexota</i> phylum. Jun 2024. URL: https://doi.org/10.1128/aem.01756-23, doi:10.1128/aem.01756-23. This article has 129 citations and is from a peer-reviewed journal.

4. (hackmann2024thevastlandscape pages 1-2): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

5. (hackmann2024thevastlandscape pages 2-3): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

6. (simon2008theorganisationof pages 1-3): Jörg Simon, Rob J.M. van Spanning, and David J. Richardson. The organisation of proton motive and non-proton motive redox loops in prokaryotic respiratory systems. Biochimica et biophysica acta, 1777 12:1480-90, Dec 2008. URL: https://doi.org/10.1016/j.bbabio.2008.09.008, doi:10.1016/j.bbabio.2008.09.008. This article has 233 citations.

7. (spero2015phylogenomicanalysisand pages 1-2): Melanie A. Spero, Frank O. Aylward, Cameron R. Currie, and Timothy J. Donohue. Phylogenomic analysis and predicted physiological role of the proton-translocating nadh:quinone oxidoreductase (complex i) across bacteria. mBio, May 2015. URL: https://doi.org/10.1128/mbio.00389-15, doi:10.1128/mbio.00389-15. This article has 67 citations and is from a domain leading peer-reviewed journal.

8. (hackmann2024thevastlandscape pages 3-4): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

9. (hackmann2024thevastlandscape pages 4-5): Timothy J Hackmann. The vast landscape of carbohydrate fermentation in prokaryotes. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae016, doi:10.1093/femsre/fuae016. This article has 27 citations and is from a domain leading peer-reviewed journal.

10. (briski2017environmentalmicrobiology pages 1-3): Felicita Briški and Marija Vuković Domanovac. Environmental microbiology. Physical Sciences Reviews, Oct 2017. URL: https://doi.org/10.1515/psr-2016-0118, doi:10.1515/psr-2016-0118. This article has 31 citations and is from a peer-reviewed journal.

11. (freches2024thebiotechnologicalpotential pages 6-9): André Freches and Joana Costa Fradinho. The biotechnological potential of the <i>chloroflexota</i> phylum. Jun 2024. URL: https://doi.org/10.1128/aem.01756-23, doi:10.1128/aem.01756-23. This article has 129 citations and is from a peer-reviewed journal.

12. (freches2024thebiotechnologicalpotential pages 14-15): André Freches and Joana Costa Fradinho. The biotechnological potential of the <i>chloroflexota</i> phylum. Jun 2024. URL: https://doi.org/10.1128/aem.01756-23, doi:10.1128/aem.01756-23. This article has 129 citations and is from a peer-reviewed journal.