---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T05:23:41.410401'
end_time: '2026-08-04T05:31:59.336140'
duration_seconds: 497.93
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Acetogenesis
  trait_identifier: METPO:1000845
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: acetogenesis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism that produces acetate as the primary end product through
    the reduction of carbon dioxide or other carbon compounds using the Wood-Ljungdahl
    pathway, typically performed by acetogenic bacteria under anaerobic conditions.
  parent_traits: METPO:1000060
  synonyms: Acetate fermentation
  evidence_summary: 'DOI:10.1016/j.bbapap.2008.08.012: Acetogenesis and the Wood-Ljungdahl
    Pathway of CO2 Fixation (Review supports acetogenesis via the Wood-Ljungdahl CO2-fixation
    pathway.) | DOI:10.1196/annals.1419.015: convert carbon dioxide and CO into acetyl-CoA
    (Supports acetyl-CoA formation from CO2 and CO in acetogens.)'
  causal_graph_summary: 'acetogenesis_wood_ljungdahl: 13 nodes, 14 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Acetogenesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000845
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that produces acetate as the primary end product through the reduction of carbon dioxide or other carbon compounds using the Wood-Ljungdahl pathway, typically performed by acetogenic bacteria under anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Acetate fermentation
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012: Acetogenesis and the Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogenesis via the Wood-Ljungdahl CO2-fixation pathway.) | DOI:10.1196/annals.1419.015: convert carbon dioxide and CO into acetyl-CoA (Supports acetyl-CoA formation from CO2 and CO in acetogens.)
- **Existing causal graph summary:** acetogenesis_wood_ljungdahl: 13 nodes, 14 edges

## Research Objective

Research the microbial trait **Acetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/acetogenesis.yaml`.

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
- **Trait label:** Acetogenesis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000845
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism that produces acetate as the primary end product through the reduction of carbon dioxide or other carbon compounds using the Wood-Ljungdahl pathway, typically performed by acetogenic bacteria under anaerobic conditions.
- **Parent traits:** METPO:1000060
- **Synonyms:** Acetate fermentation
- **Existing evidence:** DOI:10.1016/j.bbapap.2008.08.012: Acetogenesis and the Wood-Ljungdahl Pathway of CO2 Fixation (Review supports acetogenesis via the Wood-Ljungdahl CO2-fixation pathway.) | DOI:10.1196/annals.1419.015: convert carbon dioxide and CO into acetyl-CoA (Supports acetyl-CoA formation from CO2 and CO in acetogens.)
- **Existing causal graph summary:** acetogenesis_wood_ljungdahl: 13 nodes, 14 edges

## Research Objective

Research the microbial trait **Acetogenesis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/acetogenesis.yaml`.

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


# TraitMech Curation Report: Acetogenesis

## 1. Curation target and scope

- **Trait:** Acetogenesis
- **Trait identifier:** **METPO:1000845**
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** METPO:1000060
- **Recommended operational definition:** an anaerobic physiological capacity in which the Wood–Ljungdahl pathway (WLP; reductive acetyl-CoA pathway) functions in carbon assimilation and redox/energy conservation, producing acetyl-CoA from C1 carbon and normally disposing of that acetyl-CoA principally as acetate.

Two CO₂ molecules supply the methyl and carbonyl carbons of acetyl-CoA. In the methyl branch, CO₂ is reduced through formate and tetrahydrofolate-bound intermediates to methyl-THF. In the carbonyl branch, CO₂ is reduced to CO, or exogenous CO is used directly. CODH/ACS joins the methyl group, CO, and CoA to form acetyl-CoA; conversion through acetyl phosphate to acetate produces ATP by substrate-level phosphorylation. Acetogens also require chemiosmotic energy conservation because ATP consumption in the methyl branch leaves the core substrate-level pathway near net-zero ATP. Rnf- or Ech-generated ion gradients drive ATP synthase. A recent review estimates approximately **0.3 mol ATP per mol acetate** for Na⁺-dependent *Acetobacterium woodii* growing with H₂/CO₂. (bae2024harnessingacetogenicbacteria pages 2-3)

### Inclusion criteria

A strain or community should be assigned **METPO:1000845** when evidence shows:

1. operation of the WLP in the reductive direction;
2. acetyl-CoA synthesis from CO₂, CO, formate, methanol-derived C1 units, or fermentatively generated reducing equivalents;
3. acetate as the primary or characteristic reduced end product; and
4. preferably, physiological evidence such as growth, isotope incorporation, stoichiometric acetate production, transcript/protein expression, or flux through both WLP branches.

The WLP is a defining feature because it can serve simultaneously in acetyl-CoA synthesis, terminal electron acceptance, energy conservation, and carbon fixation. Approximately 200 genes may support autotrophy even though the core WLP genes occupy a much smaller locus; therefore, trait inference should not be based on one marker alone. (fackler2021steppingonthe pages 1-5)

### Boundary cases

- **Ordinary acetate fermentation is not automatically acetogenesis.** Glycolytic or amino-acid fermentation may produce acetate through acetyl-CoA without reductive WLP operation. “Acetate fermentation,” although listed as a synonym, is consequently too broad for automated inference.
- **Acetogenic bacteria need not be taxonomically monophyletic.** The phenotype is metabolic, not a clade designation. More than 100 acetogenic species have been described from soils, sediments, sludge, and intestinal systems. (bae2024harnessingacetogenicbacteria pages 2-3)
- **WLP presence is not sufficient.** Methanogens use related acetyl-CoA pathway modules, and some organisms use the pathway for assimilation without acetate being the principal end product.
- **Reverse WLP is not acetogenesis.** Syntrophic acetate oxidation consumes acetate and runs the pathway in the oxidative direction.
- **CODH alone is insufficient.** In a 2024 human-gut survey, over 1,000 representative genomes encoded putative nickel CODH, but **79%** of WLP-like gene sets lacked the formate-producing step. Such genomes may use CO for biosynthesis or possess a degenerate, heterotrophic WLP rather than perform canonical autotrophic acetogenesis. (katayama2024phylogeneticdiversityofa pages 1-7, katayama2024phylogeneticdiversityof pages 16-16)
- **Non-acetate products require phenotype-level qualification.** *Clostridium autoethanogenum* can produce ethanol and other products from gases. Such strains retain acetogenic metabolism, but a condition in which ethanol or an engineered chemical dominates should not be represented as “acetate is the primary product” without measurements. (bae2024harnessingacetogenicbacteria pages 2-3, davin2024clostridiumautoethanogenumalters pages 1-2)

## 2. Candidate causal-graph nodes

Identifiers below are conservative suggestions. Labels without a verified stable identifier should remain label-only rather than receive an inferred CURIE.

### Trait and pathway nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| Acetogenesis | **METPO:1000845** | Target trait; preserve CURIE verbatim. |
| Wood–Ljungdahl pathway | MetaCyc:CODH-PWY; KEGG module candidate M00377 | Verify database-version semantics before committing; pathway may occur outside acetogenic phenotypes. |
| Methyl branch of WLP | Label-only candidate | CO₂/formate to methyl-THF. |
| Carbonyl branch of WLP | Label-only candidate | CO₂ to CO, or direct exogenous CO utilization. |
| Substrate-level phosphorylation during acetate formation | GO:0006084 is acetate metabolism, but not an exact representation | Prefer a process label plus explicit reaction edges. |
| Chemiosmotic energy conservation | GO:0015986 is ATP synthesis coupled proton transport | Na⁺-coupled systems require more precise representation. |

### Chemicals and cofactors

| Node | Suggested CURIE |
|---|---|
| carbon dioxide | CHEBI:16526 |
| carbon monoxide | CHEBI:17245 |
| dihydrogen | CHEBI:18276 |
| formate | CHEBI:15740 |
| acetate | CHEBI:30089 |
| acetyl-CoA | CHEBI:15351 |
| coenzyme A | CHEBI:15346 |
| ATP | CHEBI:15422 |
| ADP | CHEBI:16761 |
| tetrahydrofolate | CHEBI:20506 |
| 10-formyl-tetrahydrofolate | CHEBI:15637 |
| 5,10-methylene-tetrahydrofolate | CHEBI:1989 |
| 5-methyl-tetrahydrofolate | CHEBI:15641 |
| acetyl phosphate | CHEBI:15350 |
| reduced ferredoxin / oxidized ferredoxin | Label-only unless the graph’s chemical/protein convention is fixed |
| proton gradient | Label-only process/state node |
| sodium-ion gradient | Label-only process/state node |

### Enzymes, proteins, and complexes

| Node | Suggested grounding | Typical gene labels / caution |
|---|---|---|
| formate dehydrogenase | EC:1.17.1.9 or reaction-specific alternative | `fdh`, `fdhF`; cofactor and electron-donor specificity vary. |
| formate–tetrahydrofolate ligase | EC:6.3.4.3 | `fhs`; ATP-consuming step. |
| methenyltetrahydrofolate cyclohydrolase | EC:3.5.4.9 | `fchA` or bifunctional `folD`. |
| methylenetetrahydrofolate dehydrogenase | EC:1.5.1.5 | Often `folD`; NAD(P) specificity varies. |
| methylenetetrahydrofolate reductase | EC:1.5.1.20 | `metF`/acetogen-specific complexes; do not assume a universal electron donor. |
| corrinoid iron–sulfur protein | Label-only complex | Often AcsC/AcsD; cobalt/corrinoid-dependent methyl carrier. |
| methyltransferase | Label-only or reaction-specific EC | Commonly AcsE transfers methyl from methyl-THF to CFeSP. |
| anaerobic nickel-containing carbon-monoxide dehydrogenase | EC:1.2.7.4 | Commonly AcsA/Codh; distinguish from aerobic Mo-CODH. |
| acetyl-CoA synthase | EC:2.3.1.169 | AcsB; part of CODH/ACS complex. |
| CODH/ACS complex | Label-only complex | Stronger phenotype marker than CODH alone, but still not sufficient by itself. |
| phosphate acetyltransferase | EC:2.3.1.8 | `pta`. |
| acetate kinase | EC:2.7.2.1 | `ackA`. |
| Rnf complex | GO:0048038 is quinone-related and not necessarily appropriate | Use label-only “ferredoxin:NAD⁺ oxidoreductase, ion-translocating” unless a suitable complex ontology term is verified. |
| Ech complex | Label-only | Energy-converting [NiFe]-hydrogenase; taxon-specific alternative to Rnf. |
| electron-bifurcating hydrogenase | Label-only complex | Electron-bifurcation architecture differs among acetogens. |
| F-type or V-type ATP synthase | GO:0045259 / complex-specific ontology term | Proton versus sodium coupling is organism-specific. |

### Environmental, cellular, and taxonomic nodes

- **Anaerobic/anoxic condition:** ENVO:00002040 is commonly used for anaerobic sediment, but “anoxic condition” should be represented with the ontology term appropriate to the graph’s environmental model.
- **Habitats:** soils, sediments, sewage sludge/anaerobic digesters, gastrointestinal tracts, termite hindguts, hydrothermal systems, and hypersaline sediments. The broad ecological distribution is supported, but habitat membership is not diagnostic by itself. (bae2024harnessingacetogenicbacteria pages 2-3, katayama2024phylogeneticdiversityof pages 16-16)
- **Cellular localization:** soluble methyl- and carbonyl-branch enzymes are generally cytoplasmic; Rnf/Ech and ATP synthase are membrane-associated. These localization edges should be curated at protein-complex or taxon level rather than asserted universally.
- **Reference taxa:** *Acetobacterium woodii* and *Clostridium autoethanogenum* are strong model nodes. Species-level NCBITaxon identifiers should be retrieved from NCBI Taxonomy during YAML implementation rather than entered from memory.

## 3. Candidate causal edges

The following graph skeleton contains the highest-confidence pathway edges.

| subject | predicate | object | confidence | DOI evidence |
|---|---|---|---|---|
| anaerobic conditions | enables | acetogenesis / Wood–Ljungdahl pathway operation | high | 10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) |
| CO2 | is reduced by formate dehydrogenase | formate | high | 10.1196/annals.1419.015; 10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3, katayama2024phylogeneticdiversityofa pages 1-7) |
| formate + THF + ATP | is converted by formyl-THF synthetase | formyl-THF | high | 10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) |
| THF-bound C1 intermediates | are reduced via Fch/Mthfd/Mthfr | methyl-THF | high | 10.1039/d4cb00099d; 10.1146/annurev-chembioeng-120120-021122 (bae2024harnessingacetogenicbacteria pages 2-3, fackler2021steppingonthe pages 1-5) |
| methyl-THF | transfers methyl to | corrinoid iron-sulfur protein / CFeSP | high | 10.1186/s13068-024-02554-w (davin2024clostridiumautoethanogenumalters pages 1-2) |
| CO2 | is reduced by Ni-CODH | CO | high | 10.1101/2023.10.23.563559 (katayama2024phylogeneticdiversityofa pages 1-7) |
| CODH/ACS complex | combines carbonyl + methyl + CoA | acetyl-CoA | high | 10.1196/annals.1419.015; 10.1186/s13068-024-02554-w (davin2024clostridiumautoethanogenumalters pages 1-2, katayama2024phylogeneticdiversityofa pages 1-7) |
| acetyl-CoA | is converted to | acetyl-phosphate | high | 10.1039/d4cb00099d; 10.1007/s40726-024-00337-3 (bae2024harnessingacetogenicbacteria pages 2-3, neto2024exploringthepotential pages 2-4) |
| acetyl-phosphate | is converted by acetate kinase to | acetate + ATP | high | 10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) |
| H2 oxidation | supplies electrons for | CO2 reduction in the WLP | high | 10.1021/acs.accounts.4c00226; 10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) |
| electron bifurcation | generates | reduced ferredoxin for acetogenesis | high | 10.1021/acs.accounts.4c00226; 10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) |
| Rnf complex | generates | transmembrane H+/Na+ ion gradient | high | 10.1039/d4cb00099d; 10.1101/2023.10.23.563559 (bae2024harnessingacetogenicbacteria pages 2-3, katayama2024phylogeneticdiversityofa pages 1-7) |
| Ech complex | generates | ion motive force from reduced ferredoxin | high | 10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) |
| ATP synthase | uses ion gradient to synthesize | ATP | high | 10.1039/d4cb00099d (bae2024harnessingacetogenicbacteria pages 2-3) |
| elevated H2:CO uptake ratio (>2:1; 11:1 tested) | increases | carbon efficiency / CO2-derived ethanol carbon | high | 10.1186/s13068-024-02554-w (davin2024clostridiumautoethanogenumalters pages 1-2) |


*Table: This table summarizes compact, high-confidence causal triples for a TraitMech curation of acetogenesis, emphasizing the Wood–Ljungdahl pathway core, energy conservation, and a recent process-condition effect. The DOI evidence is restricted to sources already gathered in context.*

### Evidence snippets and interpretation

| Proposed triple | Supporting snippet or tightly faithful excerpt | Reference | Curation note |
|---|---|---|---|
| anaerobic condition — **enables** → WLP-dependent acetogenesis | “Acetogens are strictly anaerobic organisms that fix CO₂ via the WLP.” | Bae et al., July 2024, DOI [10.1039/d4cb00099d](https://doi.org/10.1039/d4cb00099d) | High confidence; oxygen tolerance varies, so do not encode “any oxygen abolishes trait.” (bae2024harnessingacetogenicbacteria pages 2-3) |
| CO₂ — **is reduced by formate dehydrogenase to** → formate | “First, formate dehydrogenase converts CO₂ to formate”; recent work likewise describes Fdh synthesis of formate from CO₂ and reductants such as H₂. | Ragsdale, March 2008, DOI [10.1196/annals.1419.015](https://doi.org/10.1196/annals.1419.015); Katayama et al., 2024 | Core methyl-branch reaction. Enzyme cofactor/electron-donor details are taxon-specific. (katayama2024phylogeneticdiversityofa pages 1-7) |
| formate + THF + ATP — **are converted by Fhs to** → formyl-THF | The methyl branch includes “formate activation to formyl-THF by formyl-THF synthetase (Fhs) using ATP.” | Bae et al., July 2024, DOI [10.1039/d4cb00099d](https://doi.org/10.1039/d4cb00099d) | High confidence. (bae2024harnessingacetogenicbacteria pages 2-3) |
| formyl-THF — **is sequentially converted/reduced to** → methyl-THF | Fch, Mthfd, and Mthfr mediate the sequential THF-bound conversions to methyl-THF. | Bae et al., July 2024; Fackler et al., June 2021, DOI [10.1146/annurev-chembioeng-120120-021122](https://doi.org/10.1146/annurev-chembioeng-120120-021122) | Prefer separate reaction edges if reaction-level curation is desired. (bae2024harnessingacetogenicbacteria pages 2-3, fackler2021steppingonthe pages 1-5) |
| methyl-THF — **donates methyl via methyltransferase to** → CFeSP | The methyl group is transferred “via methyltransferase onto a corrinoid iron-sulfur protein.” | Fackler et al., June 2021, DOI [10.1146/annurev-chembioeng-120120-021122](https://doi.org/10.1146/annurev-chembioeng-120120-021122) | High confidence; represent methylated CFeSP as an intermediate if graph granularity permits. (fackler2021steppingonthe pages 1-5) |
| CO₂ — **is reduced by Ni-CODH to** → CO | The carbonyl branch reduces CO₂ to CO with nickel-containing CODH under anaerobic conditions. | Katayama et al., March 2024, DOI [10.1101/2023.10.23.563559](https://doi.org/10.1101/2023.10.23.563559) | High-confidence chemistry; the cited source is a preprint, but the result is consistent with foundational enzymology. (katayama2024phylogeneticdiversityofa pages 1-7) |
| exogenous CO — **enters through** → carbonyl branch/CODH–ACS | The WLP can “convert carbon dioxide and CO into acetyl-CoA.” | Ragsdale, March 2008, DOI [10.1196/annals.1419.015](https://doi.org/10.1196/annals.1419.015) | High confidence; CO can also act as electron donor after oxidation. |
| carbonyl + methyl-CFeSP + CoA — **are condensed by ACS to** → acetyl-CoA | CODH/ACS “combines the methyl group with CO to form acetyl-CoA”; related descriptions explicitly include CoA. | Davin et al., September 2024, DOI [10.1186/s13068-024-02554-w](https://doi.org/10.1186/s13068-024-02554-w); Katayama et al., 2024 | High confidence. (davin2024clostridiumautoethanogenumalters pages 1-2, katayama2024phylogeneticdiversityofa pages 1-7) |
| acetyl-CoA — **is converted through** → acetyl phosphate | Acetate formation proceeds “acetyl-CoA → acetyl-phosphate → acetate.” | Neto et al., November 2024, DOI [10.1007/s40726-024-00337-3](https://doi.org/10.1007/s40726-024-00337-3) | Add phosphate acetyltransferase as catalyst. (neto2024exploringthepotential pages 2-4) |
| acetyl phosphate — **is converted by acetate kinase to** → acetate + ATP | Acetyl-CoA is converted to acetate via acetyl phosphate, “with ATP generation through acetate kinase.” | Bae et al., July 2024, DOI [10.1039/d4cb00099d](https://doi.org/10.1039/d4cb00099d) | High-confidence trait-output edge. (bae2024harnessingacetogenicbacteria pages 2-3) |
| H₂ oxidation — **supplies reducing equivalents to** → WLP | In acetogens growing on H₂, electron bifurcation supplies reduced ferredoxin required for the pathway. | Mrnjavac et al., July 2024, DOI [10.1021/acs.accounts.4c00226](https://doi.org/10.1021/acs.accounts.4c00226) | High confidence at process level; hydrogenase architecture is taxon-specific. (bae2024harnessingacetogenicbacteria pages 2-3) |
| electron bifurcation — **couples favorable electron transfer to reduction of** → ferredoxin | Bifurcation couples exergonic H₂→NAD⁺ electron transfer with endergonic H₂→ferredoxin reduction. | Bae et al., July 2024, DOI [10.1039/d4cb00099d](https://doi.org/10.1039/d4cb00099d) | High confidence for relevant acetogens, not universal architecture. (bae2024harnessingacetogenicbacteria pages 2-3) |
| reduced ferredoxin oxidation by Rnf — **drives formation of** → H⁺/Na⁺ gradient | Rnf is described as an ion-translocating ferredoxin:NAD⁺ oxidoreductase that generates H⁺ or Na⁺ gradients. | Bae et al., July 2024 | High-confidence module; ion identity must be assigned by species. (bae2024harnessingacetogenicbacteria pages 2-3) |
| reduced ferredoxin oxidation by Ech — **drives formation of** → ion motive force/H₂ | Ech is a ferredoxin:H⁺ oxidoreductase used as the alternative respiratory energy-conserving system. | Bae et al., July 2024 | Do not assign Ech and Rnf simultaneously to every acetogen. (bae2024harnessingacetogenicbacteria pages 2-3) |
| transmembrane ion gradient — **drives ATP synthase to produce** → ATP | “ATP synthase couples these gradients to ATP synthesis.” | Bae et al., July 2024 | High confidence; specify Na⁺ or H⁺ only with taxon-specific evidence. (bae2024harnessingacetogenicbacteria pages 2-3) |
| WLP — **acts as** → electron sink / terminal electron-accepting process | The WLP is described as a “key metabolic component…where it acts as an electron sink,” and as supporting terminal electron acceptance and energy conservation. | Vulcano et al., May 2023, DOI [10.1111/1758-2229.13168](https://doi.org/10.1111/1758-2229.13168); Fackler et al., 2021 | The archaeal Korarchaeia conclusion was genome-based and should be marked inferred. (fackler2021steppingonthe pages 1-5) |
| elevated H₂:CO uptake ratio — **increases** → CO₂ utilization/carbon capture | Uptake ratios above 2:1 achieved reported 100% carbon efficiency; at 11:1, at least 75% of ethanol carbon came from CO₂, versus about 50% at 5:1. | Davin et al., September 2024 | Strong, condition- and strain-specific chemostat evidence; not a universal acetogenesis edge. (davin2024clostridiumautoethanogenumalters pages 1-2) |
| H₂-rich syngas — **increases specificity toward** → acetate | A 2024 trickle-bed mixed-culture study reported **86% of C-mol production** as acetic acid and **9.0 g LEBV⁻¹ day⁻¹** under H₂-rich syngas. | Quintela et al., November 2024, DOI [10.3390/molecules29235653](https://doi.org/10.3390/molecules29235653) | Assay-, reactor-, and community-specific; curate only in an experimental-condition subgraph. |

## 4. Recent developments, applications, and expert analysis

### Industrial gas fermentation

Acetogens are used to convert CO-rich industrial off-gases or CO₂/H₂ into acetate, ethanol, fuels, and chemical precursors. Peer-reviewed 2024 reviews state that syngas-to-ethanol fermentation has reached industrial production and identify *C. autoethanogenum* commercialization by LanzaTech. This is a real-world implementation of WLP-based C1 valorization, although the commercial product phenotype may be solventogenesis rather than acetate-dominant acetogenesis. (bae2024harnessingacetogenicbacteria pages 2-3)

The current expert consensus is that gas–liquid mass transfer, dissolved CO/H₂ measurement, energetic limitations, strain selection, and redox control are major bottlenecks. A 2024 kinetic analysis assembled **37 chemostat steady states** for *C. autoethanogenum* but concluded that absent dissolved-gas measurements prevent robust determination of CO-uptake dependencies. That limitation should temper graph edges connecting bulk gas composition directly to intracellular flux.

### Carbon-capture and feed-gas optimization

Davin et al. showed that high H₂ supply can shift product carbon toward CO₂ fixation without a wholesale increase in WLP protein abundance. At an **11:1 H₂:CO uptake ratio**, at least **75% of ethanol carbon** originated from CO₂, compared with approximately **50%** at 5:1. Changes in redox metabolism, cofactor synthesis, and lysine acetylation suggest that post-translational regulation fine-tunes flux. This supports an experimental edge from feed-gas ratio to carbon partitioning, but not a universal gene-expression edge. (davin2024clostridiumautoethanogenumalters pages 1-2)

### Metabolic engineering and expanded products

Acetogen engineering now targets ethanol, 2,3-butanediol, lactate, butanol, butyrate, caproate, and other chemicals. Expert reviews emphasize that the WLP’s low ATP yield is simultaneously its ecological advantage and its engineering constraint: high-value products impose ATP and reducing-equivalent demands that can impair growth. Current strategies include enhancing ATP/redox availability, adaptive evolution, mixotrophy, electricity-assisted conversion, and light-supported systems. (bae2024harnessingacetogenicbacteria pages 2-3)

### Environmental and microbiome findings

Recent genome-resolved studies broaden the known ecological distribution while also exposing annotation risks. Human-gut analysis found putative nickel-CODH genes across **8 phyla, 82 genera, and 248 species**, with transcripts in **97.3% of 110** healthy-faecal metatranscriptomes. Yet 79% of WLP-like genomes lacked the canonical formate-producing gene, demonstrating why CODH or partial-WLP calls should not be equated with acetogenesis. (katayama2024phylogeneticdiversityofa pages 1-7, katayama2024phylogeneticdiversityof pages 16-16)

In gastrointestinal acetogens, reduced or absent formate-dehydrogenase repertoires have been interpreted as adaptation to formate-rich habitats, where externally supplied or cross-fed formate may bypass the first methyl-branch reaction. This supports a conditional edge from environmental formate availability to reduced dependence on endogenous CO₂-to-formate capacity, but the evolutionary claim should not be converted into a universal mechanistic edge.

Dark, hypersaline Great Salt Lake sediments provide another 2024 example: communities shifted toward anaerobic autotrophy with depth, and WLP-encoding organisms were interpreted as favored because the WLP has exceptionally low energetic demand. These results are metagenome- and activity-based ecological inferences rather than isolate-level demonstrations of acetate production.

## 5. Recommended TraitMech graph architecture

A practical YAML graph should separate four layers:

1. **Environmental inputs:** anoxia, CO₂, H₂, CO, formate, pH, salinity, gas-transfer conditions.
2. **Molecular mechanism:** methyl branch, carbonyl branch, CFeSP methyl transfer, CODH/ACS condensation, Pta–Ack acetate formation.
3. **Energy conservation:** electron bifurcation, reduced ferredoxin, Rnf **or** Ech, ion gradient, ATP synthase, substrate-level phosphorylation.
4. **Trait readout:** acetate accumulation as primary product, growth supported by the pathway, C1-carbon incorporation, and anaerobic physiological capacity.

Taxon-specific alternatives should be represented as conditional subgraphs rather than merged into one universal route. In particular, Rnf versus Ech, H⁺ versus Na⁺ coupling, NADH versus NADPH specificity, and formate uptake versus endogenous formate production should remain explicit alternatives.

## 6. Claims not yet safe to curate

1. **“Any genome containing CODH is acetogenic.”** Reject. CODH participates in multiple CO metabolisms, and incomplete WLPs are widespread. (katayama2024phylogeneticdiversityofa pages 1-7, katayama2024phylogeneticdiversityof pages 16-16)
2. **“A complete computationally reconstructed WLP proves acetogenesis.”** Mark inferred until acetate production, growth, isotope flux, or expression evidence is available.
3. **“All acetogens are bacteria.”** Avoid. Acetogen is historically bacterial terminology, but 2023 studies infer homoacetogenic WLP function in archaeal lineages; those claims remain genome-based and should be separately qualified.
4. **“All acetogens use Rnf.”** Reject. Rnf and Ech are alternative energy-conserving systems, and additional cytochrome/quinone-linked mechanisms may occur.
5. **“All acetogens are Na⁺ dependent.”** Reject. Ion coupling is species-specific.
6. **“Oxygen is an absolute binary inhibitor.”** Overstated. The pathway is fundamentally anaerobic and its metalloenzymes are oxygen-sensitive, but organismal aerotolerance and transient exposure differ.
7. **“Acetate is always the dominant product under every condition.”** Reject. Product distributions shift with pH, gas composition, growth rate, redox state, and engineering. (bae2024harnessingacetogenicbacteria pages 2-3, davin2024clostridiumautoethanogenumalters pages 1-2)
8. **“High H₂:CO universally causes 100% carbon efficiency.”** Reject. This result is specific to controlled *C. autoethanogenum* conditions. (davin2024clostridiumautoethanogenumalters pages 1-2)
9. **“Formate-dehydrogenase absence means the WLP is nonfunctional.”** Not universally safe. Formate-rich habitats and alternative formate production can support truncated or remodeled pathways. (katayama2024phylogeneticdiversityofa pages 1-7)
10. **Methanogenic WLP and syntrophic acetate oxidation edges.** Do not merge into this trait without explicit directionality and product constraints.

## 7. DOI-first bibliography

1. **Bae J, et al.** “Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production.” *RSC Chemical Biology* 5:812–832. **July 2024.** DOI: [10.1039/d4cb00099d](https://doi.org/10.1039/d4cb00099d). Principal recent mechanistic and engineering review. (bae2024harnessingacetogenicbacteria pages 2-3)
2. **Davin ME, et al.** “*Clostridium autoethanogenum* alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated H₂:CO feedstock ratios…” *Biotechnology for Biofuels and Bioproducts* 17. **September 2024.** DOI: [10.1186/s13068-024-02554-w](https://doi.org/10.1186/s13068-024-02554-w). (davin2024clostridiumautoethanogenumalters pages 1-2)
3. **Katayama YA, et al.** “Phylogenetic diversity of putative nickel-containing carbon monoxide dehydrogenase-encoding prokaryotes in the human gut microbiome.” *Microbial Genomics* 10. **August 2024.** DOI: [10.1099/mgen.0.001285](https://doi.org/10.1099/mgen.0.001285). (katayama2024phylogeneticdiversityof pages 16-16)
4. **Neto AS, et al.** “Exploring the Potential of Syngas Fermentation for Recovery of High-Value Resources.” *Current Pollution Reports*. **November 2024.** DOI: [10.1007/s40726-024-00337-3](https://doi.org/10.1007/s40726-024-00337-3). (neto2024exploringthepotential pages 2-4)
5. **Mrnjavac N, et al.** “Chemical Antiquity in Metabolism.” *Accounts of Chemical Research* 57:2267–2278. **July 2024.** DOI: [10.1021/acs.accounts.4c00226](https://doi.org/10.1021/acs.accounts.4c00226). Supports evolutionary and electron-bifurcation interpretation. (bae2024harnessingacetogenicbacteria pages 2-3)
6. **Vulcano F, et al.** “Potential for homoacetogenesis via the Wood–Ljungdahl pathway in Korarchaeia lineages…” *Environmental Microbiology Reports* 15:698–707. **May 2023.** DOI: [10.1111/1758-2229.13168](https://doi.org/10.1111/1758-2229.13168).
7. **Fackler N, et al.** “Stepping on the Gas to a Circular Economy…” *Annual Review of Chemical and Biomolecular Engineering* 12:439–470. **June 2021.** DOI: [10.1146/annurev-chembioeng-120120-021122](https://doi.org/10.1146/annurev-chembioeng-120120-021122). (fackler2021steppingonthe pages 1-5)
8. **Ragsdale SW.** “Enzymology of the Wood–Ljungdahl Pathway of Acetogenesis.” *Annals of the New York Academy of Sciences* 1125:129–136. **March 2008.** DOI: [10.1196/annals.1419.015](https://doi.org/10.1196/annals.1419.015).
9. **Ragsdale SW, Pierce E.** “Acetogenesis and the Wood–Ljungdahl pathway of CO₂ fixation.” *Biochimica et Biophysica Acta*. **2008.** DOI: [10.1016/j.bbapap.2008.08.012](https://doi.org/10.1016/j.bbapap.2008.08.012). Foundational source supplied with the trait record.

**Curation conclusion:** the existing 13-node/14-edge graph should be expanded primarily by resolving the methyl branch, carbonyl branch, acetate-forming substrate-level phosphorylation, and the Rnf/Ech–ion-gradient–ATP-synthase energy module. The strongest trait-defining path is: **anoxia + C1 substrate/electron donor → reductive WLP → acetyl-CoA → acetyl phosphate → acetate + ATP**, with phenotype-level validation required before assigning **METPO:1000845** from genomic evidence alone.

References

1. (bae2024harnessingacetogenicbacteria pages 2-3): Jiyun Bae, Chanho Park, Hyunwoo Jung, Sangrak Jin, and Byung-Kwan Cho. Harnessing acetogenic bacteria for one-carbon valorization toward sustainable chemical production. RSC Chemical Biology, 5:812-832, Jul 2024. URL: https://doi.org/10.1039/d4cb00099d, doi:10.1039/d4cb00099d. This article has 23 citations and is from a peer-reviewed journal.

2. (fackler2021steppingonthe pages 1-5): Nick Fackler, Björn D. Heijstra, Blake J. Rasor, Hunter Brown, Jacob Martin, Zhuofu Ni, Kevin M. Shebek, Rick R. Rosin, Séan D. Simpson, Keith E. Tyo, Richard J. Giannone, Robert L. Hettich, Timothy J. Tschaplinski, Ching Leang, Steven D. Brown, Michael C. Jewett, and Michael Köpke. Stepping on the gas to a circular economy: accelerating development of carbon-negative chemical production from gas fermentation. Annual Review of Chemical and Biomolecular Engineering, 12:439-470, Jun 2021. URL: https://doi.org/10.1146/annurev-chembioeng-120120-021122, doi:10.1146/annurev-chembioeng-120120-021122. This article has 83 citations and is from a peer-reviewed journal.

3. (katayama2024phylogeneticdiversityofa pages 1-7): Yuka Adachi Katayama, Ryoma Kamikawa, and Takashi Yoshida. Phylogenetic diversity of the carbon monoxide-utilizing prokaryotes and their divergent carbon monoxide metabolisms in the human gut microbiome. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2023.10.23.563559, doi:10.1101/2023.10.23.563559. This article has 1 citations.

4. (katayama2024phylogeneticdiversityof pages 16-16): Yuka Adachi Katayama, Ryoma Kamikawa, and Takashi Yoshida. Phylogenetic diversity of putative nickel-containing carbon monoxide dehydrogenase-encoding prokaryotes in the human gut microbiome. Aug 2024. URL: https://doi.org/10.1099/mgen.0.001285, doi:10.1099/mgen.0.001285. This article has 11 citations and is from a peer-reviewed journal.

5. (davin2024clostridiumautoethanogenumalters pages 1-2): Megan E. Davin, R. Adam Thompson, Richard J. Giannone, Lucas W. Mendelson, Dana L. Carper, Madhavi Z. Martin, Michael E. Martin, Nancy L. Engle, Timothy J. Tschaplinski, Steven D. Brown, and Robert L. Hettich. Clostridium autoethanogenum alters cofactor synthesis, redox metabolism, and lysine-acetylation in response to elevated h2:co feedstock ratios for enhancing carbon capture efficiency. Biotechnology for Biofuels and Bioproducts, Sep 2024. URL: https://doi.org/10.1186/s13068-024-02554-w, doi:10.1186/s13068-024-02554-w. This article has 19 citations and is from a domain leading peer-reviewed journal.

6. (neto2024exploringthepotential pages 2-4): Alvaro S. Neto, Steven Wainaina, Konstantinos Chandolias, Pawel Piatek, and Mohammad J. Taherzadeh. Exploring the potential of syngas fermentation for recovery of high-value resources: a comprehensive review. Current Pollution Reports, Nov 2024. URL: https://doi.org/10.1007/s40726-024-00337-3, doi:10.1007/s40726-024-00337-3. This article has 48 citations and is from a peer-reviewed journal.