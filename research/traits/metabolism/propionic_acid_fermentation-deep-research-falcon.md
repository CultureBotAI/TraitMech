---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T06:45:52.061257'
end_time: '2026-08-04T06:56:27.563937'
duration_seconds: 635.5
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: propionic acid fermentation
  trait_identifier: traitmech:000029
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: propionic_acid_fermentation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A fermentation that produces propionate (with acetate and CO2) from
    sugars or lactate, typically via the Wood-Werkman (methylmalonyl-CoA) pathway.
    Characteristic of propionibacteria (e.g. Propionibacterium freudenreichii).
  parent_traits: METPO:1002005
  synonyms: propionate fermentation
  evidence_summary: 'DOI:10.3390/molecules31020333:  (Review of classical fermentations
    describes propionic acid fermentation (acetic acid, propionic acid, CO2) and propionibacteria
    as its agents, including the Wood-Werkman route.) | DOI:10.3389/fmicb.2021.703525:  (Review
    of fermentative energy conservation supports propionate formation as a redox-balancing,
    energy-conserving fermentation route.)'
  causal_graph_summary: 'propionic_acid_fermentation_propionate: 15 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** propionic acid fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000029
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation that produces propionate (with acetate and CO2) from sugars or lactate, typically via the Wood-Werkman (methylmalonyl-CoA) pathway. Characteristic of propionibacteria (e.g. Propionibacterium freudenreichii).
- **Parent traits:** METPO:1002005
- **Synonyms:** propionate fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes propionic acid fermentation (acetic acid, propionic acid, CO2) and propionibacteria as its agents, including the Wood-Werkman route.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports propionate formation as a redox-balancing, energy-conserving fermentation route.)
- **Existing causal graph summary:** propionic_acid_fermentation_propionate: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **propionic acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/propionic_acid_fermentation.yaml`.

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
- **Trait label:** propionic acid fermentation
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000029
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A fermentation that produces propionate (with acetate and CO2) from sugars or lactate, typically via the Wood-Werkman (methylmalonyl-CoA) pathway. Characteristic of propionibacteria (e.g. Propionibacterium freudenreichii).
- **Parent traits:** METPO:1002005
- **Synonyms:** propionate fermentation
- **Existing evidence:** DOI:10.3390/molecules31020333:  (Review of classical fermentations describes propionic acid fermentation (acetic acid, propionic acid, CO2) and propionibacteria as its agents, including the Wood-Werkman route.) | DOI:10.3389/fmicb.2021.703525:  (Review of fermentative energy conservation supports propionate formation as a redox-balancing, energy-conserving fermentation route.)
- **Existing causal graph summary:** propionic_acid_fermentation_propionate: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **propionic acid fermentation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/propionic_acid_fermentation.yaml`.

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


# Curation report: propionic acid fermentation

## Trait record and scope

- **Trait label:** propionic acid fermentation
- **Trait identifier:** `traitmech:000029`
- **Category / kind / status:** METABOLISM / CLASS / REVIEWED
- **Parent:** `METPO:1002005`
- **Synonym:** propionate fermentation

### Recommended scope

This trait should represent an organism’s experimentally demonstrable capacity for **net fermentative production of propionate from sugars or lactate**, canonically in dairy propionibacteria through the Wood–Werkman, or methylmalonyl-CoA, pathway. The classical overall lactate stoichiometry is:

**3 lactate → 2 propionate + acetate + CO₂ + H₂O.**

The pathway couples pyruvate reduction to oxidation elsewhere in metabolism, consumes glycolysis-derived NADH, conserves energy as ATP, and commonly produces acetate and CO₂ with propionate. Theoretical Wood–Werkman fermentation from glucose has been estimated at up to 0.7 g propionate/g glucose (1.71 mol/mol) with supplemented reducing equivalents; the commonly cited pathway-level product ratio is approximately 2:1 propionate:acetate and estimated energy yield is 4 ATP/glucose. These are model/theoretical values rather than universal assay thresholds. (bucher2021propionicacidbacteria pages 3-5, gonzalezgarcia2017microbialpropionicacid pages 8-10, gonzalezgarcia2017microbialpropionicacid pages 3-5)

The best-supported exemplar is *Propionibacterium freudenreichii*. Native propionibacteria are regarded as strong biological-production candidates because propionate is a major fermentation product and the Wood–Werkman route is energetically efficient, although slow growth, acid inhibition, coproduct formation, and downstream recovery remain barriers. (gonzalezgarcia2017microbialpropionicacid pages 1-3)

### Boundaries and nearby traits

1. **Propionate presence alone is insufficient.** Propionate may arise through the acrylate, succinate/sodium-pumping, or 1,2-propanediol pathways, through amino-acid catabolism, or through engineered aerobic biosynthesis. Those routes should not automatically instantiate this narrowly defined Wood–Werkman-centered trait. (gonzalezgarcia2017microbialpropionicacid pages 6-8, gonzalezgarcia2017microbialpropionicacid pages 1-3, gonzalezgarcia2017microbialpropionicacid pages 5-6)
2. **Net production must be distinguished from consumption.** Under oxygen exposure, *P. freudenreichii* can consume previously formed propionate and acetate. Thus detection of pathway enzymes does not prove net fermentation under every condition. (loivamaa2024aerobicadaptationand pages 6-9, dank2021propionibacteriumfreudenreichiithrives pages 3-4)
3. **Gut Bacteroidia are a boundary case.** They frequently use a succinate route and show species-specific bicarbonate dependence. Their phenotype may merit a broader “fermentative propionate production” parent or a separate mechanistic child rather than direct assignment to this canonical class. (doring2024propionateproductionby pages 1-2, doring2024propionateproductionby pages 4-5)
4. **Engineered aerobic propionate production is out of scope.** An engineered *Pseudomonas taiwanensis* strain accumulated 2.8 g/L propionate aerobically using introduced succinyl-CoA-catabolic genes and an acyl-CoA hydrolase. This is propionate biosynthesis, but not classical propionic acid fermentation. (neves2024expandingpseudomonastaiwanensis pages 1-2)
5. **Assay recommendation:** require substrate depletion plus net propionate accumulation under anoxic or explicitly fermentative conditions. Acetate and CO₂ strengthen identification but should not be mandatory because ratios vary with strain, medium, redox state, and cofactors. (bucher2021propionicacidbacteria pages 3-5, doring2024propionateproductionby pages 4-5)

## Candidate nodes

Ontology identifiers below are restricted to identifiers directly supported by the retrieved literature. Chemical and gene identifiers should remain **label-only until independently checked against current ChEBI, Rhea, KEGG, MetaCyc, UniProt, and NCBI Taxonomy releases**; this avoids inventing or misassigning CURIEs.

### Trait and pathway modules

| Candidate node | Type | Grounding recommendation |
|---|---|---|
| propionic acid fermentation | Trait class | `traitmech:000029` |
| metabolism parent | Trait class | `METPO:1002005` |
| Wood–Werkman cycle | Pathway/module | Label-only pending MetaCyc/KEGG verification |
| glycolysis | Pathway/module | Label-only pending pathway-database verification |
| fermentative redox balancing | Biological process | Label-only; pathway-level interpretation |
| ATP generation during fermentation | Biological process | Label-only; do not assign a reaction-level identifier without verification |

### Organisms and taxonomic exemplars

- *Propionibacterium freudenreichii*: canonical dairy propionibacterium and principal exemplar.
- *Acidipropionibacterium acidipropionici*: native producer used in current high-density bioprocess research.
- Other dairy propionibacteria, including *Acidipropionibacterium jensenii* and *A. thoenii*: plausible taxon-specific instances, not universal mechanistic proxies.
- *Bacteroides propionicifaciens* and *Bacteroides graminisolvens*: succinate-route boundary exemplars.
- *Clostridium propionicum*, *Megasphaera elsdenii*, and *Prevotella ruminicola*: acrylate-route boundary exemplars.
- *Veillonella*, *Propionigenium*, and *Selenomonas*: succinate/sodium-coupled route boundary taxa. (gonzalezgarcia2017microbialpropionicacid pages 6-8, gonzalezgarcia2017microbialpropionicacid pages 5-6)

### Chemicals and metabolic roles

**Inputs/electron donors:** glucose and other fermentable sugars; lactate; glycerol in process-specific cofermentations.

**Central intermediates:** pyruvate, oxaloacetate, malate, fumarate, succinate, succinyl-CoA, methylmalonyl-CoA, propionyl-CoA.

**Outputs:** propionate/propionic acid; acetate/acetic acid; carbon dioxide; water. Succinate and lactate may remain as strain- and process-dependent coproducts.

**Energy/redox entities:** NADH and ATP.

**Cofactors/nutrients:** biotin and cobalamin/vitamin B12. The literature explicitly associates biotin with methylmalonyl-CoA carboxytransferase and B12 with methylmalonyl-CoA mutase. (bucher2021propionicacidbacteria pages 3-5)

### Enzymes, proteins, and candidate genes

| Enzyme/node | Verified grounding | Curation role |
|---|---|---|
| methylmalonyl-CoA carboxytransferase / transcarboxylase | `EC:2.1.3.1` | Transfers a carboxyl group from methylmalonyl-CoA to pyruvate, forming propionyl-CoA and oxaloacetate; biotin-dependent |
| methylmalonyl-CoA mutase | `EC:5.4.99.2` | Converts succinyl-CoA to methylmalonyl-CoA; vitamin-B12-dependent |
| malate dehydrogenase | Label-only | Candidate intermediate-reduction step; retrieved evidence names the enzyme but does not establish a precise gene/protein CURIE |
| fumarate hydratase/fumarase | Label-only | Candidate malate–fumarate step |
| fumarate reductase | Label-only | Mechanistically plausible fumarate-to-succinate step, but not sufficiently resolved in the retrieved snippets for direct curation |
| succinyl-CoA transferase | Label-only | Candidate succinate/succinyl-CoA step; requires reaction- and taxon-level confirmation |
| propionate CoA-transferase | Label-only | Candidate terminal propionyl-CoA-to-propionate step; requires direct canonical-route evidence |
| methylmalonyl-CoA epimerase | Label-only | Mentioned in pathway comparisons; exact canonical role and gene grounding require verification |

The two EC-grounded reactions are the strongest enzyme-level nodes. The retrieved sources do not support reliable canonical gene symbols, UniProt accessions, operon structure, or universal orthology assignments for *P. freudenreichii*. These should not yet be curated. (bucher2021propionicacidbacteria pages 3-5, gonzalezgarcia2017microbialpropionicacid pages 15-17)

### Environmental and experimental factors

- Anoxic/anaerobic cultivation: supports net accumulation of propionate and acetate in the canonical phenotype.
- Oxygen availability: condition-dependent boundary that can redirect metabolism toward respiration and propionate/acetate consumption.
- Substrate concentration and composition: affect yield and coproduct profile.
- pH control: important process variable but not sufficiently supported here as a universal causal mechanism.
- Cell recycling/high cell density: process intervention that increases volumetric productivity.
- Biotin supplementation: process-specific enhancer that can also increase acetate coproduct.
- NaHCO₃/CO₂ availability: taxon-specific requirement in some succinate-route Bacteroidia, not a universal Wood–Werkman requirement.
- Iron and α-ketoglutarate: enhance aerobic growth in one *P. freudenreichii* experiment, but concern respiratory adaptation rather than the core fermentation trait. (dishisha2024highcelldensity pages 1-2, doring2024propionateproductionby pages 1-2, loivamaa2024aerobicadaptationand pages 1-2)

### Localization

The canonical soluble Wood–Werkman reactions should provisionally be represented at the **cellular/cytoplasmic metabolic-process level only if separately verified**. The retrieved evidence does not provide adequate localization experiments or ontology-grounded compartment assignments. Sodium-pumping methylmalonyl-CoA decarboxylase variants in other taxa are mechanistically distinct and should not be used to infer membrane localization for the *P. freudenreichii* cycle. (gonzalezgarcia2017microbialpropionicacid pages 8-10)

## Candidate causal edges

The following table is the compact graph proposal. “Snippet” text is a short evidence extract or close source-backed précis; it should be retained with the DOI and qualifier in the YAML evidence record.

| subject | predicate | object | confidence | evidence DOI | curation qualifier |
|---|---|---|---|---|---|
| sugars | feeds | pyruvate | medium | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | canonical; substrate-to-central-metabolite link summarized in review |
| lactate | feeds | pyruvate | medium | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | canonical; lactate-supported fermentation in propionibacteria |
| pyruvate | is substrate for | Wood-Werkman cycle | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | canonical |
| Wood-Werkman cycle | produces | propionate | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | canonical |
| Wood-Werkman cycle | produces | acetate | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | canonical coproduct |
| Wood-Werkman cycle | produces | carbon dioxide | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | canonical coproduct |
| NADH | is consumed by | Wood-Werkman cycle | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | redox-balancing claim from review |
| Wood-Werkman cycle | generates | ATP | medium | 10.1111/1541-4337.12804, 10.3390/fermentation3020021 (bucher2021propionicacidbacteria pages 3-5, gonzalezgarcia2017microbialpropionicacid pages 8-10) | energetic summary; pathway-level rather than single-reaction curation |
| EC:5.4.99.2 methylmalonyl-CoA mutase | converts | succinyl-CoA to methylmalonyl-CoA | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | canonical enzyme step |
| cobalamin (vitamin B12) | enables activity of | EC:5.4.99.2 methylmalonyl-CoA mutase | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | cofactor dependence |
| EC:2.1.3.1 methylmalonyl-CoA carboxytransferase | transfers carboxyl group from | methylmalonyl-CoA to pyruvate | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | canonical transfer reaction |
| biotin | enables activity of | EC:2.1.3.1 methylmalonyl-CoA carboxytransferase | high | 10.1111/1541-4337.12804 (bucher2021propionicacidbacteria pages 3-5) | cofactor dependence |
| anaerobic conditions | favor net accumulation of | propionate and acetate | medium | 10.1128/msystems.00615-24, 10.1111/1462-2920.15532 (loivamaa2024aerobicadaptationand pages 6-9, dank2021propionibacteriumfreudenreichiithrives pages 3-4) | physiology-level boundary; species/assay specific |
| aerobic or microaerobic oxygen availability | suppresses or reverses net propionate accumulation | propionate fermentation output | high | 10.1128/msystems.00615-24, 10.1111/1462-2920.15532 (loivamaa2024aerobicadaptationand pages 6-9, dank2021propionibacteriumfreudenreichiithrives pages 3-4) | strong boundary; propionate switch in P. freudenreichii |
| cell recycling in high-cell-density fermentation | increases | propionic acid productivity | high | 10.1186/s12934-024-02366-5 (dishisha2024highcelldensity pages 1-2) | process-factor; Acidipropionibacterium acidipropionici specific |
| biotin supplementation | increases | propionic acid productivity | medium | 10.1186/s12934-024-02366-5 (dishisha2024highcelldensity pages 1-2) | process-factor; A. acidipropionici specific |
| biotin supplementation | increases | acetic acid coproduct formation | medium | 10.1186/s12934-024-02366-5 (dishisha2024highcelldensity pages 1-2) | process-factor; acetate also doubled |
| external bicarbonate (NaHCO3) availability | enables efficient propionate production in | Bacteroidia species such as B. graminisolvens | medium | 10.1186/s13068-024-02539-9 (doring2024propionateproductionby pages 1-2) | taxon-specific boundary; not canonical Propionibacterium trait-wide |
| Wood-Werkman cycle | is distinct from | acrylate and 1,2-propanediol propionate pathways | high | 10.3390/fermentation3020021, 10.3389/fmolb.2022.949563 (gonzalezgarcia2017microbialpropionicacid pages 6-8, gonzalezgarcia2017microbialpropionicacid pages 1-3) | scope/boundary edge; avoid conflation in curation |


*Table: This table compiles compact candidate subject-predicate-object edges for curating traitmech:000029, emphasizing canonical Wood-Werkman mechanisms plus environmental and process boundaries. It is useful as a quick screening aid for which claims appear robust enough for graph inclusion and which should be marked taxon- or assay-specific.*

### Additional explicit triples and supporting snippets

| Subject–predicate–object | Reference and supporting snippet | Curation notes |
|---|---|---|
| lactate —is fermented to→ propionate + acetate + CO₂ | DOI: [10.3390/fermentation3020021](https://doi.org/10.3390/fermentation3020021), May 2017: “3 moles of lactic acid” yield “2 moles of propionic acid, 1 mole acetic acid, 1 mole CO₂, and 1 mole H₂O.” (gonzalezgarcia2017microbialpropionicacid pages 3-5) | **High confidence** as classical overall stoichiometry. Product ratios can deviate experimentally. |
| pyruvate —is reduced through→ Wood–Werkman cycle | DOI: [10.1111/1541-4337.12804](https://doi.org/10.1111/1541-4337.12804), August 2021: pyruvate is reduced to propionate through the cycle while glycolytic NADH is used and ATP is formed. (bucher2021propionicacidbacteria pages 3-5) | **High confidence**, pathway-level edge. |
| Wood–Werkman cycle —consumes→ NADH | Same review: “NADH from glycolysis” is utilized during pyruvate reduction. (bucher2021propionicacidbacteria pages 3-5) | **High confidence** for redox balancing; do not attach all NADH consumption to one enzyme without reaction evidence. |
| Wood–Werkman cycle —generates→ ATP | The 2021 review reports ATP generation; energetic analysis estimates 4 ATP/glucose for the Wood–Werkman route. (bucher2021propionicacidbacteria pages 3-5, gonzalezgarcia2017microbialpropionicacid pages 8-10) | **Medium confidence** because 4 ATP/glucose is a pathway model, not a universal measured yield. |
| succinyl-CoA —is converted by EC:5.4.99.2→ methylmalonyl-CoA | DOI: [10.1111/1541-4337.12804](https://doi.org/10.1111/1541-4337.12804): B12-dependent methylmalonyl-CoA mutase “converts succinyl-CoA to methylmalonyl-CoA.” (bucher2021propionicacidbacteria pages 3-5) | **High confidence**, direct enzyme edge. Direction can depend on biochemical context; retain pathway-direction qualifier. |
| cobalamin —is required by→ methylmalonyl-CoA mutase | Same source describes the mutase as “vitamin B12-dependent.” (bucher2021propionicacidbacteria pages 3-5) | **High confidence**, direct cofactor edge. |
| methylmalonyl-CoA + pyruvate —are substrates of EC:2.1.3.1→ propionyl-CoA + oxaloacetate | Same source: carboxyl transfer “from methylmalonyl-CoA to pyruvic acid” forms “propionyl-CoA and oxaloacetic acid.” (bucher2021propionicacidbacteria pages 3-5) | **High confidence**, direct reaction edge. Prefer a verified Rhea identifier when available. |
| biotin —is required by→ methylmalonyl-CoA carboxytransferase | Same source identifies the enzyme as biotin-dependent. (bucher2021propionicacidbacteria pages 3-5) | **High confidence**, direct cofactor edge. |
| oxygen exposure —reduces net accumulation of→ propionate | DOI: [10.1128/msystems.00615-24](https://doi.org/10.1128/msystems.00615-24), October 2024: anaerobic cultures accumulated propionate and acetate; at 20% pO₂, propionate remained low and fell below detection in stationary phase. (loivamaa2024aerobicadaptationand pages 6-9) | **High confidence but strain/assay-specific** to *P. freudenreichii* DSM 20271. This is a boundary-condition edge, not a universal inhibition constant. |
| microaerobic metabolism —can switch from production to consumption of→ propionate | DOI: [10.1111/1462-2920.15532](https://doi.org/10.1111/1462-2920.15532), May 2021: lactate initially yielded propionate and acetate; after lactate depletion, propionate and then acetate were consumed. (dank2021propionibacteriumfreudenreichiithrives pages 3-4) | **High confidence, taxon/condition-specific**. Useful negative evidence for phenotype calls. |
| high-cell-density cell recycling —increases→ propionate productivity | DOI: [10.1186/s12934-024-02366-5](https://doi.org/10.1186/s12934-024-02366-5), March 2024: nine glucose batches averaged 18.76 ± 1.34 g/L propionate, yield 0.59 g/g, and maximum rate 1.15 g/L·h. (dishisha2024highcelldensity pages 1-2) | **High confidence process edge**, specific to *A. acidipropionici* and the tested reactor configuration. |
| biotin supplementation —increases→ biomass and propionate productivity | The same study reports 0.75 mg/L biotin increased biomass to 21.89 gCDW/L and productivity from 0.35 to 0.48 g/L·h. (dishisha2024highcelldensity pages 1-2) | **Medium confidence**, single process context. |
| biotin supplementation —also increases→ acetate coproduct | The same experiment reports that acetate concentration doubled. (dishisha2024highcelldensity pages 1-2) | **Medium confidence**, important trade-off; do not generalize to all strains. |
| external NaHCO₃ —is required for robust production by→ *B. graminisolvens* | DOI: [10.1186/s13068-024-02539-9](https://doi.org/10.1186/s13068-024-02539-9), July 2024: among the two best producers, only *B. graminisolvens* depended on externally added NaHCO₃. (doring2024propionateproductionby pages 1-2) | **Uncertain for this trait** because this is a succinate-route, species-specific boundary case. |

## Recent developments and quantitative findings

### High-cell-density renewable-feedstock fermentation

The strongest 2024 process advance used sequential high-cell-density fermentation with cell recycling and heat-treated potato juice as nitrogen source. With 40 g/L glucose, *A. acidipropionici* produced 18.76 ± 1.34 g/L propionate per batch at 0.59 g/g yield and a maximum 1.15 g/L·h; maximum biomass was 39.89 gCDW/L and the PA:succinate:acetate mass ratio was 100:23:25. A crude glycerol/glucose feed produced 35.36 ± 2.17 g/L per batch at 0.51 g/g and 0.35 g/L·h, with a 100:29:3 coproduct ratio. The authors characterized this as the highest reported productivity for glycerol/glucose cofermentation using predominantly industrial by-products. (dishisha2024highcelldensity pages 1-2)

This study supports current expert emphasis on **reactor intensification, cell retention, renewable substrates, and coproduct control**, rather than merely adding pathway genes. It also shows why productivity, titer, yield, and product selectivity must be represented separately in assay metadata.

### Species-resolved propionate physiology

A 2024 comparison of ten Bacteroidia species found substantial interspecies variation despite broadly similar major catabolic pathways. *B. propionicifaciens* reached 0.39 g propionate/g glucose, 119 mM propionate from 130 mM glucose, and OD₆₀₀ 8.1; *B. graminisolvens* reached 0.25 g/g, 33 mM propionate from 105 mM glucose, and OD₆₀₀ 9.8, while also producing 25 mM lactate. Under defined conditions, *B. propionicifaciens* generated propionate and acetate at an approximately 2.0–2.1 molar ratio. (doring2024propionateproductionby pages 1-2, doring2024propionateproductionby pages 4-5)

The curation implication is that genome-level pathway presence should not be treated as quantitatively predictive. Carbon routing, bicarbonate dependence, residual succinate/lactate, and substrate concentration materially alter the observed phenotype.

### Oxygen as a phenotype-switching variable

In 2024, controlled 20% pO₂ increased *P. freudenreichii* DSM 20271 final OD₆₀₀ 3.2-fold and viable counts 1.4-fold relative to anaerobic culture after 72 hours, but propionate remained low and disappeared in stationary phase; acetate was also depleted. Lactate disappeared faster anaerobically (32 versus 52 hours). Aerobic growth strongly suppressed B12 accumulation, whereas microaerobic conditions in a related setup could increase B12 relative to strict anaerobiosis. (loivamaa2024aerobicadaptationand pages 6-9, loivamaa2024aerobicadaptationand pages 1-2)

This supports an expert interpretation of propionic acid fermentation as a **condition-dependent physiological state**, not a constitutive consequence of possessing pathway genes.

## Applications and implementation relevance

1. **Cheese manufacture:** dairy propionibacteria generate propionate, acetate, and CO₂; CO₂ contributes eye formation and the acids contribute flavor. The taxonomic distinction between dairy *Propionibacterium/Acidipropionibacterium* and cutaneous *Cutibacterium* should be respected in annotation. (bucher2021propionicacidbacteria pages 3-5)
2. **Food preservation and platform chemicals:** propionate is used as a preservative and as a chemical precursor. Biological production still does not broadly compete with petrochemical routes because of low productivity/titer, acid inhibition, coproducts, and purification costs. (doring2024propionateproductionby pages 1-2, gonzalezgarcia2017microbialpropionicacid pages 1-3)
3. **Waste and by-product valorization:** crude glycerol and potato-processing streams can support intensified fermentation, connecting the trait to circular-bioprocess applications. (dishisha2024highcelldensity pages 1-2)
4. **Vitamin B12-associated bioprocessing:** *P. freudenreichii* is also an industrial B12 producer, and B12 is mechanistically relevant to methylmalonyl-CoA mutase. Nevertheless, B12 production and propionate fermentation should be represented as linked but distinct traits, especially because oxygen can affect them differently. (loivamaa2024aerobicadaptationand pages 6-9, bucher2021propionicacidbacteria pages 3-5)
5. **Metabolic engineering:** engineered propionyl-CoA pools can support odd-chain products. The 2024 *Pseudomonas* example demonstrates a 2.8 g/L aerobic propionate titer, but should be modeled as engineered biosynthesis rather than evidence for native fermentation. (neves2024expandingpseudomonastaiwanensis pages 1-2)

## Recommended minimal graph for YAML

The most defensible first-pass graph is:

1. `lactate` **is substrate for** `propionic acid fermentation`.
2. `fermentable sugar` **is substrate for** `glycolysis`.
3. `glycolysis` **produces** `pyruvate`.
4. `glycolysis` **produces** `NADH`.
5. `pyruvate` **enters** `Wood–Werkman cycle`.
6. `Wood–Werkman cycle` **consumes** `NADH`.
7. `Wood–Werkman cycle` **produces** `propionate`.
8. `Wood–Werkman cycle` **produces** `acetate`.
9. `Wood–Werkman cycle` **produces** `carbon dioxide`.
10. `Wood–Werkman cycle` **supports generation of** `ATP`.
11. `methylmalonyl-CoA mutase [EC:5.4.99.2]` **converts** `succinyl-CoA` **to** `methylmalonyl-CoA`.
12. `cobalamin` **is cofactor for** `methylmalonyl-CoA mutase [EC:5.4.99.2]`.
13. `methylmalonyl-CoA carboxytransferase [EC:2.1.3.1]` **uses** `methylmalonyl-CoA + pyruvate` **to produce** `propionyl-CoA + oxaloacetate`.
14. `biotin` **is cofactor for** `methylmalonyl-CoA carboxytransferase [EC:2.1.3.1]`.
15. `oxygen availability` **negatively regulates net accumulation of** `propionate` in *P. freudenreichii* DSM 20271.

Edges 1–10 are pathway-level; edges 11–14 are direct biochemical relations; edge 15 must carry a taxon- and assay-specific qualifier. (bucher2021propionicacidbacteria pages 3-5, loivamaa2024aerobicadaptationand pages 6-9, gonzalezgarcia2017microbialpropionicacid pages 3-5)

## Warnings: claims not ready for TraitMech curation

- **Do not curate unverified ChEBI, GO, Rhea, KEGG, MetaCyc, UniProt, or NCBITaxon CURIEs.** The retrieved articles supplied names and two EC identifiers, but not authoritative identifiers for the other nodes. (bucher2021propionicacidbacteria pages 3-5)
- **Do not add a complete intermediate-by-intermediate Wood–Werkman chain from the current evidence alone.** Malate, fumarate, succinate, and several enzymes are mentioned, but the retrieved text did not directly document every reaction, direction, cofactor, and taxon-specific isoenzyme. (bucher2021propionicacidbacteria pages 3-5, gonzalezgarcia2017microbialpropionicacid pages 15-17)
- **Do not assert universal gene symbols or operons.** Gene nomenclature and orthology vary among taxa; no source here validates a canonical *P. freudenreichii* gene set for every reaction.
- **Do not conflate fermentation with aerobic engineered synthesis.** The *Pseudomonas* `scpA/argK/scpB` system is an engineered boundary case, not evidence for the native trait. (neves2024expandingpseudomonastaiwanensis pages 1-2)
- **Do not merge acrylate, 1,2-propanediol, amino-acid, and sodium-pumping succinate pathways into the core graph.** They produce the same endpoint by different causal mechanisms. The putative lactate branch within the propanediol route was specifically reported to lack biochemical evidence. (gonzalezgarcia2017microbialpropionicacid pages 15-17, gonzalezgarcia2017microbialpropionicacid pages 6-8)
- **Do not make bicarbonate dependence universal.** It differed even between two high-producing Bacteroidia species. (doring2024propionateproductionby pages 1-2)
- **Do not treat biotin supplementation as universally beneficial.** It improved productivity in one process but doubled acetate, illustrating a context-dependent trade-off. (dishisha2024highcelldensity pages 1-2)
- **Do not encode 2:1 propionate:acetate or 4 ATP/glucose as defining assay cutoffs.** They are useful canonical/theoretical expectations, but strains and culture conditions generate different ratios. (bucher2021propionicacidbacteria pages 3-5, doring2024propionateproductionby pages 4-5, gonzalezgarcia2017microbialpropionicacid pages 8-10)
- **Do not assign membrane or cytoplasmic localization without separate evidence.** Mechanistically distinct sodium-pumping pathways cannot establish localization for the classical cycle.

## DOI-first bibliography

1. Dishisha T, Jain M, Hatti-Kaul R. “High cell density sequential batch fermentation for enhanced propionic acid production…” *Microbial Cell Factories*. **March 2024**. DOI: [10.1186/s12934-024-02366-5](https://doi.org/10.1186/s12934-024-02366-5). (dishisha2024highcelldensity pages 1-2)
2. Döring C, Basen M. “Propionate production by Bacteroidia gut bacteria and its dependence on substrate concentrations differs among species.” *Biotechnology for Biofuels and Bioproducts*. **July 2024**. DOI: [10.1186/s13068-024-02539-9](https://doi.org/10.1186/s13068-024-02539-9). (doring2024propionateproductionby pages 1-2)
3. Loivamaa I, et al. “Aerobic adaptation and metabolic dynamics of *Propionibacterium freudenreichii* DSM 20271.” *mSystems*. **October 2024**. DOI: [10.1128/msystems.00615-24](https://doi.org/10.1128/msystems.00615-24). (loivamaa2024aerobicadaptationand pages 6-9, loivamaa2024aerobicadaptationand pages 1-2)
4. Neves D, et al. “Expanding *Pseudomonas taiwanensis* VLB120’s acyl-CoA portfolio: Propionate production in mineral salt medium.” *Microbial Biotechnology*. **August 2024**. DOI: [10.1111/1751-7915.14309](https://doi.org/10.1111/1751-7915.14309). (neves2024expandingpseudomonastaiwanensis pages 1-2)
5. Bücher C, Burtscher J, Domig KJ. “Propionic acid bacteria in the food industry: An update on essential traits and detection methods.” *Comprehensive Reviews in Food Science and Food Safety*. **August 2021**. DOI: [10.1111/1541-4337.12804](https://doi.org/10.1111/1541-4337.12804). (bucher2021propionicacidbacteria pages 3-5)
6. Dank A, et al. “*Propionibacterium freudenreichii* thrives in microaerobic conditions by complete oxidation of lactate to CO₂.” *Environmental Microbiology*. **May 2021**. DOI: [10.1111/1462-2920.15532](https://doi.org/10.1111/1462-2920.15532). (dank2021propionibacteriumfreudenreichiithrives pages 3-4)
7. Gonzalez-Garcia R, et al. “Microbial Propionic Acid Production.” *Fermentation*. **May 2017**. DOI: [10.3390/fermentation3020021](https://doi.org/10.3390/fermentation3020021). (gonzalezgarcia2017microbialpropionicacid pages 8-10, gonzalezgarcia2017microbialpropionicacid pages 1-3, gonzalezgarcia2017microbialpropionicacid pages 3-5)

### Curation verdict

`traitmech:000029` is suitable for a compact, reviewed causal graph centered on the Wood–Werkman pathway, its two strongly supported cofactor-dependent reactions, NADH/ATP coupling, and the propionate–acetate–CO₂ output phenotype. The graph should remain deliberately narrower than generic microbial propionate production and should encode oxygen, substrate, and process observations as qualified context edges rather than universal components.

References

1. (bucher2021propionicacidbacteria pages 3-5): Carola Bücher, Johanna Burtscher, and Konrad J. Domig. Propionic acid bacteria in the food industry: an update on essential traits and detection methods. Comprehensive reviews in food science and food safety, 20:4299-4323, Aug 2021. URL: https://doi.org/10.1111/1541-4337.12804, doi:10.1111/1541-4337.12804. This article has 75 citations and is from a domain leading peer-reviewed journal.

2. (gonzalezgarcia2017microbialpropionicacid pages 8-10): R. Gonzalez-Garcia, Tim McCubbin, Laura Navone, Chris Stowers, Lars Nielsen, and Esteban Marcellin. Microbial propionic acid production. Fermentation, 3:21, May 2017. URL: https://doi.org/10.3390/fermentation3020021, doi:10.3390/fermentation3020021. This article has 342 citations.

3. (gonzalezgarcia2017microbialpropionicacid pages 3-5): R. Gonzalez-Garcia, Tim McCubbin, Laura Navone, Chris Stowers, Lars Nielsen, and Esteban Marcellin. Microbial propionic acid production. Fermentation, 3:21, May 2017. URL: https://doi.org/10.3390/fermentation3020021, doi:10.3390/fermentation3020021. This article has 342 citations.

4. (gonzalezgarcia2017microbialpropionicacid pages 1-3): R. Gonzalez-Garcia, Tim McCubbin, Laura Navone, Chris Stowers, Lars Nielsen, and Esteban Marcellin. Microbial propionic acid production. Fermentation, 3:21, May 2017. URL: https://doi.org/10.3390/fermentation3020021, doi:10.3390/fermentation3020021. This article has 342 citations.

5. (gonzalezgarcia2017microbialpropionicacid pages 6-8): R. Gonzalez-Garcia, Tim McCubbin, Laura Navone, Chris Stowers, Lars Nielsen, and Esteban Marcellin. Microbial propionic acid production. Fermentation, 3:21, May 2017. URL: https://doi.org/10.3390/fermentation3020021, doi:10.3390/fermentation3020021. This article has 342 citations.

6. (gonzalezgarcia2017microbialpropionicacid pages 5-6): R. Gonzalez-Garcia, Tim McCubbin, Laura Navone, Chris Stowers, Lars Nielsen, and Esteban Marcellin. Microbial propionic acid production. Fermentation, 3:21, May 2017. URL: https://doi.org/10.3390/fermentation3020021, doi:10.3390/fermentation3020021. This article has 342 citations.

7. (loivamaa2024aerobicadaptationand pages 6-9): Iida Loivamaa, Annika Sillanpää, Paulina Deptula, Bhawani Chamlagain, Minnamari Edelmann, Petri Auvinen, Tuula A. Nyman, Kirsi Savijoki, Vieno Piironen, and Pekka Varmanen. Aerobic adaptation and metabolic dynamics of <i>propionibacterium freudenreichii</i> dsm 20271: insights from comparative transcriptomics and surfaceome analysis. Oct 2024. URL: https://doi.org/10.1128/msystems.00615-24, doi:10.1128/msystems.00615-24. This article has 7 citations and is from a peer-reviewed journal.

8. (dank2021propionibacteriumfreudenreichiithrives pages 3-4): Alexander Dank, Oscar van Mastrigt, Sjef Boeren, Søren K. Lillevang, Tjakko Abee, and Eddy J. Smid. Propionibacterium freudenreichii thrives in microaerobic conditions by complete oxidation of lactate to co2. Environmental Microbiology, 23:3116-3129, May 2021. URL: https://doi.org/10.1111/1462-2920.15532, doi:10.1111/1462-2920.15532. This article has 34 citations and is from a domain leading peer-reviewed journal.

9. (doring2024propionateproductionby pages 1-2): Carolin Döring and Mirko Basen. Propionate production by bacteroidia gut bacteria and its dependence on substrate concentrations differs among species. Biotechnology for Biofuels and Bioproducts, Jul 2024. URL: https://doi.org/10.1186/s13068-024-02539-9, doi:10.1186/s13068-024-02539-9. This article has 27 citations and is from a domain leading peer-reviewed journal.

10. (doring2024propionateproductionby pages 4-5): Carolin Döring and Mirko Basen. Propionate production by bacteroidia gut bacteria and its dependence on substrate concentrations differs among species. Biotechnology for Biofuels and Bioproducts, Jul 2024. URL: https://doi.org/10.1186/s13068-024-02539-9, doi:10.1186/s13068-024-02539-9. This article has 27 citations and is from a domain leading peer-reviewed journal.

11. (neves2024expandingpseudomonastaiwanensis pages 1-2): Dário Neves, Daniel Meinen, Tobias B. Alter, Lars M. Blank, and Birgitta E. Ebert. Expanding pseudomonas taiwanensis vlb120's acyl‐coa portfolio: propionate production in mineral salt medium. Microbial Biotechnology, Aug 2024. URL: https://doi.org/10.1111/1751-7915.14309, doi:10.1111/1751-7915.14309. This article has 3 citations and is from a peer-reviewed journal.

12. (gonzalezgarcia2017microbialpropionicacid pages 15-17): R. Gonzalez-Garcia, Tim McCubbin, Laura Navone, Chris Stowers, Lars Nielsen, and Esteban Marcellin. Microbial propionic acid production. Fermentation, 3:21, May 2017. URL: https://doi.org/10.3390/fermentation3020021, doi:10.3390/fermentation3020021. This article has 342 citations.

13. (dishisha2024highcelldensity pages 1-2): Tarek Dishisha, Mridul Jain, and Rajni Hatti-Kaul. High cell density sequential batch fermentation for enhanced propionic acid production from glucose and glycerol/glucose mixture using acidipropionibacterium acidipropionici. Microbial Cell Factories, Mar 2024. URL: https://doi.org/10.1186/s12934-024-02366-5, doi:10.1186/s12934-024-02366-5. This article has 15 citations and is from a peer-reviewed journal.

14. (loivamaa2024aerobicadaptationand pages 1-2): Iida Loivamaa, Annika Sillanpää, Paulina Deptula, Bhawani Chamlagain, Minnamari Edelmann, Petri Auvinen, Tuula A. Nyman, Kirsi Savijoki, Vieno Piironen, and Pekka Varmanen. Aerobic adaptation and metabolic dynamics of <i>propionibacterium freudenreichii</i> dsm 20271: insights from comparative transcriptomics and surfaceome analysis. Oct 2024. URL: https://doi.org/10.1128/msystems.00615-24, doi:10.1128/msystems.00615-24. This article has 7 citations and is from a peer-reviewed journal.