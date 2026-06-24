---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:23:49.900858'
end_time: '2026-06-18T02:38:33.314668'
duration_seconds: 883.41
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: temperature range low
  trait_identifier: METPO:1000449
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: temperature_range_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature range phenotype in which the growth-supporting ambient\
    \ temperature range spans approximately 10\u201322 \xB0C, characteristic of psychrophilic\
    \ or psychrotolerant physiology."
  parent_traits: METPO:1000306
  synonyms: Psychrophile, Psychrotolerant, TR_10_to_22
  evidence_summary: "DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile\
    \ review supports cool-temperature membrane and enzyme adaptation as the basis\
    \ of growth in the 10\u201322 \xB0C range.)"
  causal_graph_summary: 'temperature_range_low_psychrotolerant: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range low
- **METPO identifier:** METPO:1000449
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 10–22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, Psychrotolerant, TR_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cool-temperature membrane and enzyme adaptation as the basis of growth in the 10–22 °C range.)
- **Existing causal graph summary:** temperature_range_low_psychrotolerant: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_low.yaml`.

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
- **Trait label:** temperature range low
- **METPO identifier:** METPO:1000449
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 10–22 °C, characteristic of psychrophilic or psychrotolerant physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Psychrophile, Psychrotolerant, TR_10_to_22
- **Existing evidence:** DOI:10.1038/sj.embor.7400662: decreased membrane fluidity (Psychrophile review supports cool-temperature membrane and enzyme adaptation as the basis of growth in the 10–22 °C range.)
- **Existing causal graph summary:** temperature_range_low_psychrotolerant: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_low.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Temperature range low (METPO:1000449)

### Scope summary (trait semantics and boundaries)
The **temperature range low** trait (METPO:1000449) denotes organisms whose **growth-supporting ambient temperature range spans ~10–22 °C**, consistent with **psychrophilic or psychrotolerant/psychrotrophic physiology**. Psychrophiles are typically described as able to grow at **0 °C** with optima near **~15 °C** and **not growing at 20 °C**, whereas **psychrotolerant/psychrotrophs** can grow at **~4 °C** but have **optimal growth temperatures above 20 °C**. This distinction matters for curating “temperature range low” because some strains can grow in the 10–22 °C interval but are not obligate cold specialists. (ramon2023ageneraloverview pages 1-2)

A complementary recent definition notes psychrotrophs as “capable of thriving at **7 °C or lower**” and psychrophiles as “capable of growth at **0 °C or below**, with an **optimal range typically between 15 °C and 20 °C.” (purwar2024adaptationsofpsychrophilic pages 1-3)

**Assay interpretation for curation:** the phenotype is usually inferred from growth curves, OD600, CFU counts, colony formation, and/or “growth/no growth” screens across temperature points (e.g., 5/13/20/25/30 °C). Antarctic isolates enriched at 13 °C achieved ~**1.5×10^9 CFU/mL** by day 14, whereas incubation at 30 °C reduced biomass and yielded no colonies. (son2023morphologicalandphysiological pages 2-3)

**Boundary cases / nearby traits:**
- Organisms with optimum >22 °C but capable of growth at 10–22 °C are better treated as **psychrotolerant/psychrotrophic**, not obligate psychrophiles. (ramon2023ageneraloverview pages 1-2)
- Ice-binding/antifreeze mechanisms are most directly relevant to freezing/subzero survival; they can be present in cold-adapted organisms but may be **context-dependent** for a 10–22 °C trait definition (still useful as auxiliary nodes/edges for cold habitats). (purwar2024adaptationsofpsychrophilic pages 6-7, ramasamy2023comprehensiveinsightson pages 3-4)

---

## Current understanding: key concepts and mechanistic definition
Low-temperature growth is multifactorial, but converges on a few core bottlenecks:

1. **Membrane phase behavior (homeoviscous adaptation):** cold reduces membrane fluidity; organisms restore function via changes in lipid chain length, branching, and unsaturation. Cold sensing can occur through membrane physical state and trigger signaling (e.g., two-component systems). (purwar2024adaptationsofpsychrophilic pages 8-10, ramon2023ageneraloverview pages 1-2)

2. **RNA/translation bottlenecks:** cold stabilizes RNA secondary structure and slows ribosome function; cold-adapted microbes deploy **cold shock proteins (CSPs)** as RNA chaperones and often encode **DEAD-box helicases** and **ribosome-binding factors** that support translation at low temperature. (ramasamy2023comprehensiveinsightson pages 3-4, hu2023comparativegenomicanalysis pages 8-11)

3. **Protein folding and stress homeostasis:** cold can promote misfolding/cold-denaturation and oxidative stress; organisms express chaperones (e.g., GroEL/DnaK/Hsp70) and oxidative-stress defenses. (purwar2024adaptationsofpsychrophilic pages 6-7, son2023morphologicalandphysiological pages 7-7)

4. **Cryoprotection and extracellular matrix:** compatible solutes and EPS can protect membranes/proteins and buffer freezing-associated stresses; AFP/IBP systems inhibit ice recrystallization and crystal growth. (ramasamy2023comprehensiveinsightson pages 3-4, yang2023insightintothe pages 4-7, purwar2024adaptationsofpsychrophilic pages 6-7)

---

## Candidate nodes (entities) for `temperature_range_low.yaml`
| Group | Label | Node type | Brief role in low-temperature growth | Suggested ontology grounding | Supporting citation IDs |
|---|---|---|---|---|---|
| Environmental factors/assay conditions | low temperature (10–22 °C; often tested at 5, 13, 20, 22 °C) | environmental condition | Core external condition selecting for psychrophilic/psychrotolerant growth physiology and cold-response programs | ENVO:cold environment (candidate); label-only temperature assay condition | (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 1-3, yang2023insightintothe pages 2-4, son2023morphologicalandphysiological pages 1-2) |
| Environmental factors/assay conditions | growth/no-growth temperature assay | assay condition | Operational phenotype measurement using OD600, CFU, or colony formation across temperature gradients | label-only assay node | (son2023morphologicalandphysiological pages 2-3, son2023morphologicalandphysiological pages 1-2, yang2023insightintothe pages 2-4) |
| Environmental factors/assay conditions | refrigerated/cold aquatic habitat | environment | Natural source environment enriching cold-adapted microbes and enzymes | ENVO:cold habitat (candidate); ENVO:marine habitat (candidate) | (kuddus2024cold‐activemicrobialenzymes pages 1-2, purwar2024adaptationsofpsychrophilic pages 1-3) |
| Cellular properties | membrane fluidity | cellular property | Central biophysical property that falls at low temperature and must be restored for growth | label-only property node | (purwar2024adaptationsofpsychrophilic pages 8-10, ramon2023ageneraloverview pages 1-2) |
| Cellular properties | increased unsaturated fatty acid proportion | cellular property | Raises membrane fluidity during cold growth | CHEBI:35566 unsaturated fatty acid | (yang2023insightintothe pages 4-7, yang2023insightintothe pages 1-2, liu2023psychrophilicyeastsinsights pages 4-5) |
| Cellular properties | branched/anteiso fatty acid enrichment | cellular property | Supports homeoviscous adaptation in cold membranes | label-only branched-chain fatty acid node | (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7, son2023morphologicalandphysiological pages 7-7) |
| Cellular properties | ATP accumulation under cold | cellular property | Energy buffering/support for cold survival and low-temperature metabolism | CHEBI:15422 ATP | (yang2023insightintothe pages 2-4, yang2023insightintothe media 8155f514) |
| Cellular properties | reduced motility / increased aggregation | cellular property | Energy-saving and stress-associated phenotype under cold or temperature stress | GO:0048870 cell motility; label-only aggregation | (yang2023insightintothe pages 4-7, son2023morphologicalandphysiological pages 3-4) |
| Genes/proteins/complexes | CspA family cold-shock protein | protein family | RNA chaperone supporting transcription/translation at low temperature | UniProt family: Cold shock domain proteins; GO:0003723 RNA binding | (gupta2023psychrophilesasa pages 9-10, ramasamy2023comprehensiveinsightson pages 3-4, hu2023comparativegenomicanalysis pages 8-11) |
| Genes/proteins/complexes | CspC family cold-shock protein | protein family | Cold-response RNA-binding protein abundant in psychrotolerant genomes | UniProt family: Cold shock domain proteins | (hu2023comparativegenomicanalysis pages 8-11, son2023morphologicalandphysiological pages 7-7, son2023morphologicalandphysiological pages 3-4) |
| Genes/proteins/complexes | DEAD-box RNA helicase DeaD | protein | Helps maintain RNA metabolism/transcription/translation in the cold | GO:0004386 helicase activity; label: DeaD | (hu2023comparativegenomicanalysis pages 8-11, hu2023comparativegenomicanalysis pages 7-8) |
| Genes/proteins/complexes | DEAD-box RNA helicase RhlE | protein | Supports RNA remodeling under low-temperature stress | GO:0004386 helicase activity; label: RhlE | (hu2023comparativegenomicanalysis pages 8-11, hu2023comparativegenomicanalysis pages 7-8) |
| Genes/proteins/complexes | RNA helicase DbpA | protein | Ribosome/RNA remodeling factor in cold-adapted genomes | GO:0004386 helicase activity; label: DbpA | (hu2023comparativegenomicanalysis pages 8-11) |
| Genes/proteins/complexes | ribosome-binding factor A (RbfA) | protein | Cold-induced ribosome biogenesis/function factor | UniProtKB:RbfA family; GO:0042254 ribosome biogenesis | (hu2023comparativegenomicanalysis pages 8-11) |
| Genes/proteins/complexes | GroEL chaperonin | protein complex/family | Protects against protein misfolding during temperature stress; abundant in cold-adapted strains | UniProt family: GroEL; GO:0006457 protein folding | (purwar2024adaptationsofpsychrophilic pages 6-7, son2023morphologicalandphysiological pages 7-7, son2023morphologicalandphysiological pages 3-4) |
| Genes/proteins/complexes | DnaK/Hsp70 chaperone | protein family | Assists folding/stability of proteins under cold stress | UniProt family: DnaK/Hsp70; GO:0006457 protein folding | (ramasamy2023comprehensiveinsightson pages 3-4, purwar2024adaptationsofpsychrophilic pages 6-7, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Genes/proteins/complexes | RimJ acetyltransferase | protein | Proposed ribosomal protein acetylation/ribosome stabilization factor enriched in obligate cold strain YJ56 | label: RimJ; EC candidate not assigned here | (son2023morphologicalandphysiological pages 1-2, son2023morphologicalandphysiological pages 3-4, son2023morphologicalandphysiological pages 4-7) |
| Genes/proteins/complexes | FoF1 ATP synthase | protein complex | Supports ATP accumulation/energy balance under cold conditions | GO:0046933 proton-transporting ATP synthase complex | (yang2023insightintothe pages 2-4) |
| Genes/proteins/complexes | cytochrome c oxidase | protein complex | Increased respiratory activity associated with cold adaptation in B. simplex H-b | EC:7.1.1.9; GO:0022904 respiratory electron transport chain | (yang2023insightintothe pages 2-4) |
| Genes/proteins/complexes | BetS transporter | transporter | Osmoprotectant uptake, linked to compatible-solute based cold tolerance | label: BetS transporter | (son2023morphologicalandphysiological pages 7-7, son2023morphologicalandphysiological pages 3-4) |
| Genes/proteins/complexes | ProX/ProW/ProY glycine betaine-proline transporter system | transporter complex | Imports compatible solutes for osmoprotection and cryoprotection | label: ProX; label: ProW; label: ProY | (hu2023comparativegenomicanalysis pages 8-11, hu2023comparativegenomicanalysis pages 7-8) |
| Genes/proteins/complexes | antifreeze protein / ice-binding protein | protein family | Inhibits ice crystal growth/recrystallization and protects cells in freezing-associated cold | label: antifreeze protein; label: ice-binding protein | (ramasamy2023comprehensiveinsightson pages 3-4, purwar2024adaptationsofpsychrophilic pages 6-7) |
| Pathways/modules | homeoviscous adaptation | biological process/module | Global membrane-remodeling response restoring membrane function at low temperature | label-only process node | (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Pathways/modules | unsaturated fatty acid biosynthesis | pathway | Produces membrane UFAs that improve fluidity in cold conditions | GO:0006636 unsaturated fatty acid biosynthetic process | (purwar2024adaptationsofpsychrophilic pages 8-10, liu2023psychrophilicyeastsinsights pages 4-5, yang2023insightintothe pages 4-7) |
| Pathways/modules | branched-chain fatty acid biosynthesis | pathway | Generates branched lipids supporting cold membrane fluidity | label-only pathway node | (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7) |
| Pathways/modules | trehalose biosynthesis (TreX/TreY/TreS) | pathway/module | Produces compatible solute linked to cold/osmotic protection | KEGG/MetaCyc candidate; label: TreX/TreY/TreS pathway | (hu2023comparativegenomicanalysis pages 8-11, hu2023comparativegenomicanalysis pages 7-8) |
| Pathways/modules | extracellular polymeric substance biosynthesis | pathway/module | Produces protective matrix associated with cryoprotection and stress tolerance | label-only EPS biosynthesis node | (yang2023insightintothe pages 4-7, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Pathways/modules | glycolysis | pathway | Often maintained or increased to support energy generation during cold adaptation | KEGG: Glycolysis / GO:0006096 glycolytic process | (purwar2024adaptationsofpsychrophilic pages 8-10) |
| Pathways/modules | TCA cycle downregulation / glyoxylate shunt use | pathway/module | Metabolic reprogramming observed in some cold-adapted taxa | GO:0006099 tricarboxylic acid cycle; GO:0006097 glyoxylate cycle | (purwar2024adaptationsofpsychrophilic pages 10-11, purwar2024adaptationsofpsychrophilic pages 8-10) |
| Pathways/modules | nitrogen assimilation | pathway/process | Favored over dissimilatory denitrification in B. simplex H-b at low temperature | label-only nitrogen assimilation node | (yang2023insightintothe pages 1-2, yang2023insightintothe pages 2-4) |
| Pathways/modules | denitrification | pathway/process | Important applied low-temperature metabolism in psychrotolerant wastewater strains | GO:0019645 anaerobic electron transport?; label-only denitrification | (hu2023comparativegenomicanalysis pages 7-8, hu2023comparativegenomicanalysis pages 12-14, yang2023insightintothe pages 2-4) |
| Metabolites/chemicals | polyunsaturated fatty acids (PUFAs; e.g., C18:3/C18:4) | metabolite class | Increase membrane fluidity in psychrophiles/psychrotolerants | CHEBI:26208 polyunsaturated fatty acid | (liu2023psychrophilicyeastsinsights pages 4-5, purwar2024adaptationsofpsychrophilic pages 10-11) |
| Metabolites/chemicals | glycine betaine | metabolite | Compatible solute protecting proteins and membranes and lowering effective freezing stress | CHEBI:17750 glycine betaine | (ramasamy2023comprehensiveinsightson pages 3-4, yang2023insightintothe pages 4-7, hu2023comparativegenomicanalysis pages 8-11) |
| Metabolites/chemicals | trehalose | metabolite | Compatible solute/cryoprotectant in cold adaptation | CHEBI:16589 trehalose | (ramasamy2023comprehensiveinsightson pages 3-4, purwar2024adaptationsofpsychrophilic pages 10-11, hu2023comparativegenomicanalysis pages 8-11) |
| Metabolites/chemicals | glycerol | metabolite | Osmolyte/cryoprotectant and enriched metabolic capability in psychrophiles | CHEBI:17754 glycerol | (ramasamy2023comprehensiveinsightson pages 3-4, liu2023psychrophilicyeastsinsights pages 4-5, purwar2024adaptationsofpsychrophilic pages 10-11) |
| Metabolites/chemicals | sucrose | metabolite | Reported compatible solute in cold-adaptation reviews | CHEBI:17992 sucrose | (ramasamy2023comprehensiveinsightson pages 3-4, purwar2024adaptationsofpsychrophilic pages 10-11) |
| Metabolites/chemicals | mannitol | metabolite | Compatible solute associated with low-temperature protection | CHEBI:16899 mannitol | (ramasamy2023comprehensiveinsightson pages 3-4, purwar2024adaptationsofpsychrophilic pages 10-11) |
| Metabolites/chemicals | sarcosine | metabolite | Example cold-accumulated solute in Mesorhizobium at 4 °C | CHEBI:17819 sarcosine | (purwar2024adaptationsofpsychrophilic pages 10-11) |
| Metabolites/chemicals | ATP | metabolite | Elevated ATP pools support cold survival in some bacteria | CHEBI:15422 ATP | (yang2023insightintothe pages 2-4, yang2023insightintothe media 8155f514, gupta2023psychrophilesasa pages 9-10) |
| Extracellular structures | extracellular polymeric substances (EPS) | extracellular structure | Cryoprotective matrix; can reduce freeze-thaw damage and support survival in cold habitats | label-only EPS node | (purwar2024adaptationsofpsychrophilic pages 8-10, ramasamy2023comprehensiveinsightson pages 3-4, yang2023insightintothe pages 4-7) |
| Extracellular structures | mannose-rich EPS / mannan-rich extracellular polysaccharide | extracellular structure | Specific EPS class associated with freeze-thaw and desiccation protection | CHEBI:62017 mannan (candidate) | (purwar2024adaptationsofpsychrophilic pages 8-10, liu2023psychrophilicyeastsinsights pages 4-5) |
| Extracellular structures | ice-binding extracellular proteins | extracellular structure/protein | Surface-active protective proteins that limit damaging ice crystal behavior | label: extracellular ice-binding protein | (ramasamy2023comprehensiveinsightson pages 3-4, purwar2024adaptationsofpsychrophilic pages 6-7) |


*Table: This table lists candidate entities for curating a causal graph for METPO:1000449 temperature range low. It organizes evidence-backed nodes by biological type and suggests ontology grounding where available.*

---

## Evidence-backed candidate causal edges (triples)
| Edge (subject–predicate–object) | Entity types | Suggested grounding | Evidence snippet | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| low temperature → decreases → membrane fluidity | environment → process/property → cell envelope property | ENVO:cold environment?; GO:0005886 plasma membrane; label: membrane fluidity | “cold reduces membrane fluidity” and cells respond by lipid remodeling; “changes in membrane physical state” mediate cold sensing | 10.37256/amtt.5220244537 (2024) https://doi.org/10.37256/amtt.5220244537; 10.1007/s42770-023-01057-4 (2023) https://doi.org/10.1007/s42770-023-01057-4 (purwar2024adaptationsofpsychrophilic pages 8-10, ramon2023ageneraloverview pages 1-2) | Strong review-supported edge; membrane fluidity is a phenotype/property node rather than a discrete molecule. |
| fatty acid desaturase activity → increases → membrane fluidity | enzyme/process → process/property | EC:1.14.19.- fatty acid desaturases; GO:0006636 unsaturated fatty acid biosynthetic process; label: membrane fluidity | “genes for…desaturation…are upregulated”; psychrophilic yeasts have diverse FAD genes (δ6/δ9/δ12/δ15) and “may be able to enhance the fluidity of cell membranes” by PUFA synthesis | 10.37256/amtt.5220244537 (2024) https://doi.org/10.37256/amtt.5220244537; 10.3390/genes14010158 (2023) https://doi.org/10.3390/genes14010158 (purwar2024adaptationsofpsychrophilic pages 8-10, liu2023psychrophilicyeastsinsights pages 4-5) | Mechanistically strong but gene family membership and exact isoenzymes vary by taxon; curate as generic desaturase unless strain-specific evidence is needed. |
| increased branched-chain fatty acids / altered anteiso:isofatty-acid ratio → increases → membrane fluidity | metabolite class/process → property | CHEBI:branched-chain fatty acid?; label: anteiso-fatty acid; label: iso-fatty acid; label: membrane fluidity | “favoring shorter-chain, methyl-branched…lipids” and “Changing the proportion of anteiso to isofatty acid” to maintain fluidity | 10.37256/amtt.5220244537 (2024) https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 8-10, purwar2024adaptationsofpsychrophilic pages 6-7) | Broadly supported in reviews; exact lipid species often unresolved. Candidate node may remain label-only. |
| low temperature → increases → unsaturated fatty acid proportion | environment → metabolite composition/process | CHEBI:unsaturated fatty acid; GO:0006636 unsaturated fatty acid biosynthetic process | “the proportion of unsaturated fatty acids was higher in strains cultured at low temperatures”; “UFAs increased at low temperature” while long-chain SFAs decreased | 10.1128/aem.01928-22 (2023) https://doi.org/10.1128/aem.01928-22 (yang2023insightintothe pages 1-2, yang2023insightintothe pages 4-7, yang2023insightintothe media 8155f514) | Strong primary-study support; specific UFA identities not always provided in bacteria. |
| cspA/cspC family cold-shock proteins → act as → RNA chaperones supporting translation at low temperature | gene/protein → molecular function/process | UniProt family: cold shock proteins; GO:0003723 RNA binding; GO:0006412 translation; label: RNA chaperone activity | “Cold shock proteins (Csps) can function as RNA chaperones”; cspA homologs were “constitutively expressed at 4°C and 22°C”; YJ56 carries “six copies of cold-shock csp genes” | 10.1186/s12864-023-09638-1 (2023) https://doi.org/10.1186/s12864-023-09638-1; 10.3389/fmicb.2023.1197797 (2023) https://doi.org/10.3389/fmicb.2023.1197797; 10.1038/s41598-023-42179-x (2023) https://doi.org/10.1038/s41598-023-42179-x (hu2023comparativegenomicanalysis pages 8-11, ramasamy2023comprehensiveinsightson pages 3-4, son2023morphologicalandphysiological pages 7-7) | Strong for CSP class; direct causal linkage to the trait can be taxon-specific. Prefer family-level node unless a specific ortholog is curated. |
| DEAD-box RNA helicases (DeaD/RhlE/DbpA) → maintain → transcription/translation under low temperature | gene/protein → process | GO:0004386 helicase activity; GO:0006412 translation; GO:0006351 transcription, DNA-templated; label: DeaD; label: RhlE; label: DbpA | “genes encoding DbpA, RhlE and DeaD were also observed” and “These DEAD-box RNA helicases can increase transcription levels under low temperature stress” | 10.1186/s12864-023-09638-1 (2023) https://doi.org/10.1186/s12864-023-09638-1 (hu2023comparativegenomicanalysis pages 8-11) | Strong genomic/mechanistic support, but direct perturbation evidence is limited in these strains; mark moderate confidence. |
| ribosome binding factor A (RbfA) → supports → ribosome function during cold growth | protein → biological process | UniProtKB:RbfA family; GO:0042254 ribosome biogenesis | “a cold-induced protein ribosome binding factor A (RbfA) was found” | 10.1186/s12864-023-09638-1 (2023) https://doi.org/10.1186/s12864-023-09638-1 (hu2023comparativegenomicanalysis pages 8-11) | Presence-based evidence in cold-adapted genomes; direct edge to low-temperature growth is plausible but somewhat inferred. |
| glycine betaine / trehalose / glycerol → provide → cryoprotection and protein/membrane stabilization | metabolite → process | CHEBI:17750 glycine betaine; CHEBI:16589 trehalose; CHEBI:17754 glycerol | compatible osmolytes “preventing cell shrinkage, lowering freezing point, scavenging free radicals, preventing aggregation, improving folding and stabilizing membranes/proteins” | 10.3389/fmicb.2023.1197797 (2023) https://doi.org/10.3389/fmicb.2023.1197797; 10.37256/amtt.5220244537 (2024) https://doi.org/10.37256/amtt.5220244537 (ramasamy2023comprehensiveinsightson pages 3-4, purwar2024adaptationsofpsychrophilic pages 10-11) | Strong class-level evidence; exact dominant solute differs by species and medium. |
| extracellular polymeric substances (EPS) → provide → cryoprotection | polymer/process → process | GO:0045226 extracellular matrix structural constituent?; label: extracellular polymeric substances | EPS “provide cryoprotection”; at low temperature, epsC/epsM/epsN were upregulated with “increased EPS content” | 10.37256/amtt.5220244537 (2024) https://doi.org/10.37256/amtt.5220244537; 10.1128/aem.01928-22 (2023) https://doi.org/10.1128/aem.01928-22 (purwar2024adaptationsofpsychrophilic pages 8-10, yang2023insightintothe pages 4-7, yang2023insightintothe media 8155f514) | Good support for protective role; EPS chemistry is taxon- and medium-dependent. |
| antifreeze proteins / ice-binding proteins → inhibit → ice recrystallization | protein → process | label: antifreeze protein; label: ice-binding protein; GO:0043205? ice binding not consistently grounded | AFPs/IBPs “bind ice crystal surfaces and inhibit recrystallization/produce thermal hysteresis”; “inhibit ice-crystal growth” and show “ice recrystallization inhibition (IRI)” | 10.37256/amtt.5220244537 (2024) https://doi.org/10.37256/amtt.5220244537; 10.3389/fmicb.2023.1197797 (2023) https://doi.org/10.3389/fmicb.2023.1197797 (purwar2024adaptationsofpsychrophilic pages 6-7, ramasamy2023comprehensiveinsightson pages 3-4) | Strong mechanism for freezing-associated cold stress; for the 10–22 °C trait this may be auxiliary and context-dependent, especially above 0 °C. |
| GroEL / DnaK chaperones → prevent → protein misfolding at low temperature | protein → process | UniProt family: GroEL; UniProt family: DnaK; GO:0051082 unfolded protein binding; GO:0006457 protein folding | chaperones are “upregulated at low temperatures to prevent cold-denaturation, misfolding”; GroEL was “extremely overproduced (2.1 to 7.0-fold)” under temperature stress | 10.37256/amtt.5220244537 (2024) https://doi.org/10.37256/amtt.5220244537; 10.1038/s41598-023-42179-x (2023) https://doi.org/10.1038/s41598-023-42179-x (purwar2024adaptationsofpsychrophilic pages 6-7, son2023morphologicalandphysiological pages 7-7) | Strong for chaperone class, but Son et al. measured heat-stress upregulation at 25 °C in an obligate cold strain; curate carefully as temperature-stress homeostasis, not exclusively cold-induced. |
| increased respiratory electron transport / FoF1-ATPase expression → increases → ATP accumulation under cold | process/protein complex → metabolite pool | GO:0022904 respiratory electron transport chain; GO:0046933 proton-transporting ATP synthase complex; CHEBI:15422 ATP | “cytochrome c oxidase expression increased ~4.33–4.85× and FoF1 ATPase ~1.58–2.33× at 5°C vs 30°C,” and “intracellular ATP increased as temperature decreased” | 10.1128/aem.01928-22 (2023) https://doi.org/10.1128/aem.01928-22 (yang2023insightintothe pages 2-4, yang2023insightintothe pages 4-7, yang2023insightintothe media 8155f514) | Strong primary-study support in Bacillus simplex H-b; may reflect one adaptive strategy rather than a universal low-temperature mechanism. |
| low temperature → favors → nitrogen assimilation over dissimilation | environment → metabolic process | GO:0015696 ammonium transport?; GO:0015706 nitrate transport?; label: nitrogen assimilation; label: denitrification/dissimilatory nitrate reduction | “At low temperatures, more nitrogen was utilized for assimilation…rather than transforming inorganic nitrogen in the dissimilation pathway” | 10.1128/aem.01928-22 (2023) https://doi.org/10.1128/aem.01928-22 (yang2023insightintothe pages 1-2, yang2023insightintothe pages 2-4) | Strong but system-specific to aerobic denitrifying Bacillus simplex H-b; should be marked uncertain/taxon-specific for generic TraitMech curation. |


*Table: This table lists evidence-backed candidate causal edges for curating the microbial trait 'temperature range low' (~10–22 °C) into TraitMech. It emphasizes mechanisms with recent 2023–2024 support, while flagging taxon-specific or context-dependent claims for cautious curation.*

---

## Recent developments and latest research (2023–2024 prioritized)

### A. Genomics/proteomics of cold-adapted bacteria (strain-level evidence)
**Pseudarthrobacter psychrotolerans YJ56 (Antarctic isolate; psychrophilic growth phenotype)**
- YJ56 shows superior growth at **13 °C** and **cannot grow at 30 °C**, making it a strong exemplar of low-temperature growth specialization. (son2023morphologicalandphysiological pages 1-2)
- Genomics provides concrete candidate node/edge material: YJ56 carries **12 rimJ copies** (vs. 3–4 in related strains), **six cold-shock csp genes** (five cspC + one cspA), and **six betS** copies (osmolyte uptake). (son2023morphologicalandphysiological pages 3-4, son2023morphologicalandphysiological pages 7-7)
- Proteomic temperature-stress responses include GroEL overproduction (**2.1–7.0-fold**) and KatE detection under higher temperature stress (25 °C), emphasizing that protein homeostasis systems may be key determinants of narrow growth windows. (son2023morphologicalandphysiological pages 7-7)

### B. Cold-tolerant functional microbiology with quantitative physiology
**Aerobic denitrifying Bacillus simplex H-b (wastewater-relevant psychrotolerance)**
- Demonstrated nitrate-N (60 mg/L initial) removal at low temperature: **27.22% at 5 °C** (vs. 84.71% at 20 °C and 76.22% at 37 °C), highlighting performance constraints and adaptation needs in cold wastewater contexts. (yang2023insightintothe pages 2-4)
- Low temperature is associated with **ATP accumulation**, **increased EPS**, and **higher UFA proportion** (membrane adaptation) relative to warmer cultures. (yang2023insightintothe pages 1-2, yang2023insightintothe pages 4-7, yang2023insightintothe media 8155f514)
- Transcriptomic evidence supports mechanistic edges linking cold to altered transport/metabolism and EPS biosynthesis (epsC/epsM/epsN up), and lipid composition shifts (long-chain SFAs down; UFAs up). (yang2023insightintothe pages 4-7)

### C. Comparative genomics of psychrotrophic denitrifiers
**Arctic Pseudomonas strains with low-temperature denitrification potential**
- Genomes encode multiple cold-adaptation functions: CSPs (CspA/CspC/CspD), DEAD-box helicases (DbpA/RhlE/DeaD), RbfA, trehalose biosynthesis genes, and compatible-solute transport (ProX/ProW/ProY). (hu2023comparativegenomicanalysis pages 8-11)
- The paper links these strains’ ecology to **aerobic denitrification in cold environments**, though the connection between specific cold genes and denitrification performance is primarily genomic/co-occurrence rather than demonstrated by targeted gene perturbation. (hu2023comparativegenomicanalysis pages 7-8, hu2023comparativegenomicanalysis pages 12-14)

### D. Cross-domain expansions: psychrophilic yeasts genomics
Psychrophilic yeasts show expansion/diversification of fatty-acid desaturases (δ6/δ9/δ12/δ15), enabling **PUFA synthesis** (e.g., C18:3/C18:4), supporting membrane fluidity at low temperatures. (liu2023psychrophilicyeastsinsights pages 4-5)

---

## Current applications and real-world implementations

### 1) Industrial use of cold-active enzymes (real-world deployment)
Cold-active enzymes enable processes at low/moderate temperatures, reducing heating needs and protecting volatile or heat-labile components. A 2024 review summarizes broad applications in **food processing, detergents, textiles, wastewater treatment, biopulping, bioremediation in cold climates, biotransformation, and molecular biology**. (kuddus2024cold‐activemicrobialenzymes pages 1-2)

**Statistics and examples from 2024 review evidence:**
- Cold ecosystems constitute a major fraction of Earth: cold habitats cover **>70%** of Earth’s total area and “about **85%** of Earth is covered by various cold habitats,” underscoring why low-temperature metabolism is globally relevant. (kuddus2024cold‐activemicrobialenzymes pages 1-2, kuddus2024cold‐activemicrobialenzymes pages 2-4)
- A cold-active β-galactosidase example is reported to digest **>80% of lactose in raw milk at 20 °C and pH 6.5**, illustrating direct low-temperature food-processing functionality within the 10–22 °C range. (kuddus2024cold‐activemicrobialenzymes pages 2-4)
- A biostimulation/bioremediation case reports **75% pollutant removal in 40 days**, indicating practical cold-environment remediation potential (though substrate/location specifics should be checked before curation as a generic statistic). (kuddus2024cold‐activemicrobialenzymes pages 10-12)

### 2) Cold-region wastewater nitrogen removal
Cold-tolerant aerobic denitrifiers are being investigated for sewage/wastewater treatment in winter/cold climates. Bacillus simplex H-b provides a quantitative benchmark: **27.22% nitrate-N removal at 5 °C** under tested conditions, and molecular evidence that cold triggers coordinated membrane/EPS/energy changes. (yang2023insightintothe pages 2-4, yang2023insightintothe media 8155f514)

---

## Expert synthesis (authoritative interpretation)
Recent reviews converge on a mechanistic picture in which low-temperature growth is governed by **(i) restoration of membrane function**, **(ii) safeguarding RNA/translation**, **(iii) proteostasis and oxidative-stress management**, and **(iv) extracellular/solute-mediated cryoprotection**, with metabolism reprogrammed to maintain energy and precursor supply. These are described as “multifactorial adaptation” strategies involving membrane-driven sensing, induction of cold-shock genes, and protective macromolecules/solutes. (ramon2023ageneraloverview pages 1-2, purwar2024adaptationsofpsychrophilic pages 8-10)

---

## Curation warnings (do not curate without stronger support)
1. **Ice-binding/antifreeze proteins as core edges for 10–22 °C:** While strongly supported for freezing-associated cold stress, their necessity for growth specifically in 10–22 °C conditions is context-dependent; curate as auxiliary edges unless the trait definition explicitly includes freeze–thaw conditions. (purwar2024adaptationsofpsychrophilic pages 6-7, ramasamy2023comprehensiveinsightson pages 3-4)

2. **Chaperone directionality (cold vs heat stress):** GroEL and other chaperones are stress-response hubs; in YJ56, GroEL upregulation was observed at **25 °C** (a higher/stress temperature for an obligate cold strain), so the edge should be represented as **temperature stress → chaperones → proteostasis** rather than strictly “cold → chaperones.” (son2023morphologicalandphysiological pages 7-7)

3. **Denitrification-specific edges as generic trait edges:** Nitrogen assimilation vs dissimilation shifts are robust in Bacillus simplex H-b, but may not generalize across taxa; treat as **taxon- and niche-specific** (wastewater functional trait), not a universal determinant of low-temperature growth. (yang2023insightintothe pages 1-2, yang2023insightintothe pages 2-4)

---

## DOI-first bibliography (publication date and URL)
- Ramón A, Esteves A, Villadóniga C, Chalar C, Castro-Sowinski S. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies**. *Brazilian Journal of Microbiology*. **2023-07**. DOI: **10.1007/s42770-023-01057-4**. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2)
- Ramasamy KP, et al. **Comprehensive insights on environmental adaptation strategies in Antarctic bacteria and biotechnological applications of cold adapted molecules**. *Frontiers in Microbiology*. **2023-06**. DOI: **10.3389/fmicb.2023.1197797**. https://doi.org/10.3389/fmicb.2023.1197797 (ramasamy2023comprehensiveinsightson pages 3-4)
- Hu Y-Q, et al. **Comparative genomic analysis of two Arctic Pseudomonas strains reveals insights into the aerobic denitrification in cold environments**. *BMC Genomics*. **2023-09**. DOI: **10.1186/s12864-023-09638-1**. https://doi.org/10.1186/s12864-023-09638-1 (hu2023comparativegenomicanalysis pages 8-11)
- Son Y, Min J, Shin Y, Park W. **Morphological and physiological adaptations of psychrophilic Pseudarthrobacter psychrotolerans YJ56 under temperature stress**. *Scientific Reports*. **2023-09**. DOI: **10.1038/s41598-023-42179-x**. https://doi.org/10.1038/s41598-023-42179-x (son2023morphologicalandphysiological pages 1-2)
- Yang Q, et al. **Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: Bacillus simplex H-b**. *Applied and Environmental Microbiology*. **2023-02**. DOI: **10.1128/aem.01928-22**. https://doi.org/10.1128/aem.01928-22 (yang2023insightintothe pages 2-4)
- Liu H, et al. **Psychrophilic Yeasts: Insights into Their Adaptability to Extremely Cold Environments**. *Genes*. **2023-01**. DOI: **10.3390/genes14010158**. https://doi.org/10.3390/genes14010158 (liu2023psychrophilicyeastsinsights pages 4-5)
- Kuddus M, et al. **Cold-active microbial enzymes and their biotechnological applications**. *Microbial Biotechnology*. **2024-04**. DOI: **10.1111/1751-7915.14467**. https://doi.org/10.1111/1751-7915.14467 (kuddus2024cold‐activemicrobialenzymes pages 1-2)
- Purwar S, Srivastava S. **Adaptations of Psychrophilic Microorganism to Low-Temperature Environments**. *Applied Microbiology: Theory & Technology*. **2024-10**. DOI: **10.37256/amtt.5220244537**. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 1-3)

---

### Visual evidence used
Physiological differences across temperatures (ATP, EPS, fatty acid composition) and nitrogen utilization are shown in figures from Yang et al. 2023 (AEM) as retrieved images. (yang2023insightintothe media 8155f514, yang2023insightintothe media 353a4394)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (purwar2024adaptationsofpsychrophilic pages 1-3): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

3. (son2023morphologicalandphysiological pages 2-3): Yongjun Son, Jihyeon Min, Yoonjae Shin, and Woojun Park. Morphological and physiological adaptations of psychrophilic pseudarthrobacter psychrotolerans yj56 under temperature stress. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42179-x, doi:10.1038/s41598-023-42179-x. This article has 17 citations and is from a peer-reviewed journal.

4. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

5. (ramasamy2023comprehensiveinsightson pages 3-4): Kesava Priyan Ramasamy, Lovely Mahawar, Raju Rajasabapathy, Kottilil Rajeshwari, Cristina Miceli, and Sandra Pucciarelli. Comprehensive insights on environmental adaptation strategies in antarctic bacteria and biotechnological applications of cold adapted molecules. Frontiers in Microbiology, Jun 2023. URL: https://doi.org/10.3389/fmicb.2023.1197797, doi:10.3389/fmicb.2023.1197797. This article has 69 citations and is from a peer-reviewed journal.

6. (purwar2024adaptationsofpsychrophilic pages 8-10): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

7. (hu2023comparativegenomicanalysis pages 8-11): Yong-Qiang Hu, Yin-Xin Zeng, Yu Du, Wei Zhao, Hui-Rong Li, Wei Han, Ting Hu, and Wei Luo. Comparative genomic analysis of two arctic pseudomonas strains reveals insights into the aerobic denitrification in cold environments. BMC Genomics, Sep 2023. URL: https://doi.org/10.1186/s12864-023-09638-1, doi:10.1186/s12864-023-09638-1. This article has 15 citations and is from a peer-reviewed journal.

8. (son2023morphologicalandphysiological pages 7-7): Yongjun Son, Jihyeon Min, Yoonjae Shin, and Woojun Park. Morphological and physiological adaptations of psychrophilic pseudarthrobacter psychrotolerans yj56 under temperature stress. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42179-x, doi:10.1038/s41598-023-42179-x. This article has 17 citations and is from a peer-reviewed journal.

9. (yang2023insightintothe pages 4-7): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Applied and Environmental Microbiology, Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

10. (yang2023insightintothe pages 2-4): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Applied and Environmental Microbiology, Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

11. (son2023morphologicalandphysiological pages 1-2): Yongjun Son, Jihyeon Min, Yoonjae Shin, and Woojun Park. Morphological and physiological adaptations of psychrophilic pseudarthrobacter psychrotolerans yj56 under temperature stress. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42179-x, doi:10.1038/s41598-023-42179-x. This article has 17 citations and is from a peer-reviewed journal.

12. (kuddus2024cold‐activemicrobialenzymes pages 1-2): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

13. (yang2023insightintothe pages 1-2): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Applied and Environmental Microbiology, Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

14. (liu2023psychrophilicyeastsinsights pages 4-5): Haisheng Liu, Guiliang Zheng, Zhongwei Chen, Xiaoya Ding, Jinran Wu, Haili Zhang, and Shulei Jia. Psychrophilic yeasts: insights into their adaptability to extremely cold environments. Genes, 14:158, Jan 2023. URL: https://doi.org/10.3390/genes14010158, doi:10.3390/genes14010158. This article has 21 citations.

15. (yang2023insightintothe media 8155f514): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Applied and Environmental Microbiology, Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

16. (son2023morphologicalandphysiological pages 3-4): Yongjun Son, Jihyeon Min, Yoonjae Shin, and Woojun Park. Morphological and physiological adaptations of psychrophilic pseudarthrobacter psychrotolerans yj56 under temperature stress. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42179-x, doi:10.1038/s41598-023-42179-x. This article has 17 citations and is from a peer-reviewed journal.

17. (gupta2023psychrophilesasa pages 9-10): Varsha Gupta, Pranav Bhaskar, Jeancolar Thoudam, Shiwali Bisht, Anita Sharma, and Rashmi Tripathi. Psychrophiles as a novel and promising source of cold-adapted industrial enzymes. The Applied Biology &amp; Chemistry Journal, pages 54-68, Jun 2023. URL: https://doi.org/10.52679/tabcj.2023.0006, doi:10.52679/tabcj.2023.0006. This article has 10 citations.

18. (hu2023comparativegenomicanalysis pages 7-8): Yong-Qiang Hu, Yin-Xin Zeng, Yu Du, Wei Zhao, Hui-Rong Li, Wei Han, Ting Hu, and Wei Luo. Comparative genomic analysis of two arctic pseudomonas strains reveals insights into the aerobic denitrification in cold environments. BMC Genomics, Sep 2023. URL: https://doi.org/10.1186/s12864-023-09638-1, doi:10.1186/s12864-023-09638-1. This article has 15 citations and is from a peer-reviewed journal.

19. (son2023morphologicalandphysiological pages 4-7): Yongjun Son, Jihyeon Min, Yoonjae Shin, and Woojun Park. Morphological and physiological adaptations of psychrophilic pseudarthrobacter psychrotolerans yj56 under temperature stress. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-42179-x, doi:10.1038/s41598-023-42179-x. This article has 17 citations and is from a peer-reviewed journal.

20. (purwar2024adaptationsofpsychrophilic pages 10-11): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.

21. (hu2023comparativegenomicanalysis pages 12-14): Yong-Qiang Hu, Yin-Xin Zeng, Yu Du, Wei Zhao, Hui-Rong Li, Wei Han, Ting Hu, and Wei Luo. Comparative genomic analysis of two arctic pseudomonas strains reveals insights into the aerobic denitrification in cold environments. BMC Genomics, Sep 2023. URL: https://doi.org/10.1186/s12864-023-09638-1, doi:10.1186/s12864-023-09638-1. This article has 15 citations and is from a peer-reviewed journal.

22. (kuddus2024cold‐activemicrobialenzymes pages 2-4): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

23. (kuddus2024cold‐activemicrobialenzymes pages 10-12): Mohammed Kuddus, Roohi, Naushin Bano, Gouse Basha Sheik, Babu Joseph, Burhan Hamid, Raveendran Sindhu, and Aravind Madhavan. Cold‐active microbial enzymes and their biotechnological applications. Microbial Biotechnology, Apr 2024. URL: https://doi.org/10.1111/1751-7915.14467, doi:10.1111/1751-7915.14467. This article has 61 citations and is from a peer-reviewed journal.

24. (yang2023insightintothe media 353a4394): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Applied and Environmental Microbiology, Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.