---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-03T23:21:05.833045'
end_time: '2026-08-03T23:27:57.275230'
duration_seconds: 411.44
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: habitat association
  trait_identifier: traitmech:000047
  trait_category: ECOLOGY
  trait_category_slug: ecology
  trait_slug: habitat_association
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An ecological classification of the primary environment or niche an
    organism inhabits (e.g. free-living vs host-associated; soil, rhizosphere, gut).
    Microbial taxa show biogeographic structure across such habitats.
  parent_traits: METPO:1000059
  synonyms: niche association
  evidence_summary: 'DOI:10.1038/nrmicro1341:  (Martiny et al., "Microbial biogeography",
    support habitat/niche as a structuring axis of microbial distribution; parent
    of the habitat sub-variants.) | DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing
    the unknown", supports environment-specific microbial community membership (e.g.
    the soil microbiome) underpinning habitat association.)'
  causal_graph_summary: 'habitat_association_biogeographic_structure: 10 nodes, 8
    edges'
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
- **Trait label:** habitat association
- **METPO identifier:** traitmech:000047
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological classification of the primary environment or niche an organism inhabits (e.g. free-living vs host-associated; soil, rhizosphere, gut). Microbial taxa show biogeographic structure across such habitats.
- **Parent traits:** METPO:1000059
- **Synonyms:** niche association
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al., "Microbial biogeography", support habitat/niche as a structuring axis of microbial distribution; parent of the habitat sub-variants.) | DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", supports environment-specific microbial community membership (e.g. the soil microbiome) underpinning habitat association.)
- **Existing causal graph summary:** habitat_association_biogeographic_structure: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **habitat association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/habitat_association.yaml`.

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
- **Trait label:** habitat association
- **METPO identifier:** traitmech:000047
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An ecological classification of the primary environment or niche an organism inhabits (e.g. free-living vs host-associated; soil, rhizosphere, gut). Microbial taxa show biogeographic structure across such habitats.
- **Parent traits:** METPO:1000059
- **Synonyms:** niche association
- **Existing evidence:** DOI:10.1038/nrmicro1341:  (Martiny et al., "Microbial biogeography", support habitat/niche as a structuring axis of microbial distribution; parent of the habitat sub-variants.) | DOI:10.1038/nrmicro.2017.87:  (Fierer, "Embracing the unknown", supports environment-specific microbial community membership (e.g. the soil microbiome) underpinning habitat association.)
- **Existing causal graph summary:** habitat_association_biogeographic_structure: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **habitat association** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/habitat_association.yaml`.

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


# TraitMech curation report: microbial habitat association

## Executive curation recommendation

**Trait:** habitat association (`traitmech:000047`; ECOLOGY; CLASS; REVIEWED).

Habitat association should be represented as a **context-indexed ecological classification**: the habitat, host compartment, or physicochemical niche in which an organism reproducibly occurs, is enriched, persists, or grows best. It is usually inferred from occupancy or abundance across samples, but can be strengthened by culture-based measurements of growth range or optimum. Current expert usage treats environmental preference as growth responses—including ranges and optima—along gradients such as pH, salinity, oxygen, temperature, moisture, and pressure. It is therefore an emergent phenotype with multiple mechanistic routes, not one molecular function (ramoneda2024leveraginggenomicinformation pages 6-7, ramoneda2024leveraginggenomicinformation pages 1-2).

The strongest graph architecture is:

**environmental/host condition → physiological challenge or cue → sensing/homeostasis/colonization mechanism → survival, growth, or colonization → observed habitat association.**

Directly connecting a gene to the generic trait is usually too broad. Mechanistic subgraphs should instead terminate in a qualified outcome such as **high-salinity persistence**, **low-pH growth**, or **rhizoplane colonization**, which then supports habitat association.

## 1. Scope and boundary cases

### Included

* Free-living versus host-associated lifestyle.
* Association with named environments or compartments: soil, freshwater, marine water, sediment, rhizosphere, rhizoplane, endosphere, or gut.
* Preference along habitat-defining gradients when expressed as occupancy, abundance optimum, growth optimum, or tolerance range.
* Specialist/generalist classifications such as stenohaline versus euryhaline, provided the assay and threshold are recorded. Wu et al. defined stenohaline MAGs by an average relative abundance in one salinity class more than an order of magnitude above both alternatives (wu2024metagenomicinsightsinto pages 1-2).

### Distinguish from nearby traits

* **Environmental tolerance** is a physiological capacity and a cause of persistence, not identical to observed habitat association.
* **Colonization** is a process leading to host-compartment association; transient attachment alone does not establish primary habitat.
* **Host association** does not specify mutualism, commensalism, or pathogenicity.
* **Biogeographic range/dispersal** controls access to habitats but does not itself demonstrate preference.
* **Relative abundance in one survey** is evidence of occurrence, not sufficient alone for a stable trait assertion.
* **Taxonomic provenance** is not mechanism. A 2023 analysis found strain-level differences and showed that physical conditions can override interspecies interactions; habitat preference should not automatically propagate across a genus (ng2023singlestrainbehaviorpredicts pages 1-2).
* **Metabolic pathway presence** indicates potential, not realized habitat association, unless linked to phenotype or repeated environmental distribution.

## 2. Candidate nodes grouped by type

### Trait and ecological outcomes

* Habitat association — `traitmech:000047`.
* Environmental preference; niche optimum; niche breadth — label-only until the project selects an ontology.
* Rhizosphere association; rhizoplane colonization; gut association; high-salinity persistence; low-pH growth; euryhaline/stenohaline lifestyle — preferably composite, context-qualified nodes rather than universal classes.
* Rhizosphere — candidate `ENVO:00005801`; verify against the repository’s ENVO release before commit.

### Environmental and host factors

* pH, salinity, osmolality, oxygen availability, temperature, moisture, pressure.
* Root exudates, including sugars, amino acids, organic acids, sugar alcohols, and flavonoids.
* Host immune filtering, iron limitation, phosphorus limitation, and intermicrobial competition.

The 2024 expert perspective identifies pH, salinity, oxygen, temperature, moisture, and pressure as major dimensions for genome-based environmental-preference prediction (ramoneda2024leveraginggenomicinformation pages 6-7, ramoneda2024leveraginggenomicinformation pages 1-2). Root exudates both provide resources and act as selective signals in the rhizosphere (blancoromero2023adaptionofpseudomonas pages 1-2, liu2024rootcolonizationby pages 3-4).

### Genes, proteins, and complexes

* Trk-type K+ uptake system: COG0168/Trk-associated low-affinity K+ transport; `trkA` where specifically annotated.
* Kdp K+ transporters; Na+/H+ antiporters; urease and urea transporters; proton-consuming decarboxylases and amino-acid deaminases.
* MCP–CheW–CheA chemotaxis receptor/signaling complex and CheY response regulator.
* Flagellar motor and flagellum-biogenesis machinery.
* `amrZ`, `fleQ`, and c-di-GMP synthesis/degradation proteins.
* `fadL`, `exoF`, `exoQ`, `exoP`; distinguish EPS synthesis from polymerization/export.
* Siderophore biosynthesis/uptake systems and type VII secretion/YukE only in explicitly plant-associated subgraphs.

### Chemicals and signals

* Potassium ion — `CHEBI:29103`.
* Proton — `CHEBI:15378`.
* Sodium ion — `CHEBI:29101`.
* Water — `CHEBI:15377`.
* c-di-GMP — use a CHEBI identifier only after exact record verification.
* Compatible solutes: ectoine, glycine betaine, trehalose, and related osmoprotectants; ground each separately after checking CHEBI.
* N-acyl-L-homoserine lactones (AHLs), preferably represented by the exact chain-length species when experimentally known.
* Root-derived glucose, sucrose, galactose, inositol, organic acids, amino acids, and flavonoids.

### Processes and pathways

* Cellular response to osmotic stress — `GO:0071470`.
* Chemotaxis — `GO:0006935`.
* Bacterial-type flagellum-dependent cell motility — candidate `GO:0071973`.
* Biofilm formation — `GO:0042710`.
* Potassium-ion transport — candidate `GO:0006813`.
* Cytoplasmic pH homeostasis, compatible-solute accumulation, salt-in osmoadaptation, EPS polymerization/secretion, quorum sensing, adhesion, root migration, iron acquisition, and host-compartment colonization. Exact GO/MetaCyc/Rhea grounding should be verified during YAML implementation.

## 3. Candidate causal edges

The compact priority set is summarized below.

| subject | predicate | object | evidence class | context/taxon | confidence |
|---|---|---|---|---|---|
| environmental pH | filters / structures | microbial community composition and pH preference | observational + genomic inference; biogeographic gradients and strain assays (ramoneda2023buildingagenomebased pages 1-1, ng2023singlestrainbehaviorpredicts pages 1-2) | soil and freshwater taxa across 1,470 samples; human gut strains | high |
| pH-homeostasis genes (e.g., proton-consuming decarboxylases, urease/urea transport, Kdp K+ transporters, Na+/H+ antiporters) | associated with | bacterial pH preference | observational association; ML feature discovery, not direct causal knockout proof (ramoneda2023buildingagenomebased pages 3-5) | diverse bacteria across soil and freshwater datasets | medium |
| salinity | causes | osmotic stress | experimental/natural-gradient ecological mechanism (wu2024metagenomicinsightsinto pages 1-2) | estuarine microbial communities | high |
| Trk-type K+ transporter (COG0168) | associated with / may promote | persistence in high-salinity habitats | observational metagenomic association; strongest selected feature, not direct intervention (wu2024metagenomicinsightsinto pages 1-2, wu2024metagenomicinsightsinto pages 7-9) | Pearl River estuary MAGs; dominant Actinobacteriota and Proteobacteria | medium |
| compatible-solute strategy | promotes | salinity tolerance | observational/natural-gradient mechanism; “salt-out” osmoregulation features enriched (wu2024metagenomicinsightsinto pages 1-2) | estuarine microbial communities | medium |
| root exudates | activate | MCP-CheA/CheW-CheY chemotaxis signaling | experimental/review synthesis from rhizobacterial studies (liu2024rootcolonizationby pages 3-4) | rhizobacteria including Bacillus spp., Pseudomonas spp. | high |
| MCP-CheA/CheW-CheY chemotaxis signaling | promotes | motility and approach toward roots | experimental/review synthesis (liu2024rootcolonizationby pages 3-4) | rhizobacteria | high |
| motility | promotes | root colonization / site selection | experimental + review synthesis (liu2024rootcolonizationby pages 3-4, blancoromero2023adaptionofpseudomonas pages 1-2) | rhizobacteria; pseudomonads in rhizosphere | high |
| AmrZ/FleQ regulatory hub | regulates switch between | motility and biofilm / extracellular matrix production | experimental genomics + mutant-based review synthesis (blancoromero2023adaptionofpseudomonas pages 1-2) | Pseudomonas ogarae F113 | high |
| c-di-GMP | mediates | AmrZ/FleQ control of motility-biofilm switch | experimental/review synthesis (blancoromero2023adaptionofpseudomonas pages 1-2) | Pseudomonas ogarae F113 | high |
| extracellular long-chain AHLs | increase | surface motility | direct experiment with synthetic AHL mixture and mutants (ji2023rhizobialmigrationtoward pages 1-2) | Sinorhizobium fredii | high |
| extracellular long-chain AHLs | enhance | migration toward roots and rhizoplane colonization | direct experiment (ji2023rhizobialmigrationtoward pages 1-2) | Sinorhizobium fredii on soybean, rice, maize | high |
| exoFQP | promotes | rhizoplane colonization | direct genetics/Tn-seq; mutations caused severe impairment (ji2023rhizobialmigrationtoward pages 1-2) | Sinorhizobium fredii | high |
| fadL-mediated long-chain AHL uptake | modulates | extracellular long-chain AHL levels and rhizoplane colonization | direct genetics/physiology (ji2023rhizobialmigrationtoward pages 1-2) | Sinorhizobium fredii | high |


*Table: This table compiles compact, curation-oriented candidate causal edges for microbial habitat association, distinguishing direct experimental support from observational genomic associations. It is useful for prioritizing which nodes and edges are strongest for TraitMech curation and which should remain uncertain.*

### Curation-ready edge details

| Proposed subject–predicate–object | Reference and supporting snippet | Interpretation and curation status |
|---|---|---|
| **environmental pH —filters→ bacterial community composition** | Ramoneda et al. studied **“1470 samples”** across soil and freshwater gradients and report that pH structures bacterial distributions (DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998), April 2023) (ramoneda2023buildingagenomebased pages 1-1). | Strong ecological edge. Filtering is supported; it does not imply that pH alone determines composition. |
| **pH-homeostasis machinery —supports→ growth/persistence at characteristic pH** | The study identified proton-consuming decarboxylases/deaminases, urease/urea transport, Kdp systems, Na+/H+ antiporters, hydrogenases, and phosphatases among genes associated with inferred pH preference. It found **332 gene types** recurring in at least two datasets and **56** in at least three (ramoneda2023buildingagenomebased pages 3-5). | **Uncertain/associative.** Curate as “associated with” or “candidate mechanism” unless an independent perturbation study supports the particular gene–phenotype edge. |
| **external pH or osmolality —selects for→ tolerant gut strains** | Ng et al. assayed **92 strains from 28 families**; isolated-strain performance predicted survival in complex communities and a mouse model of diet-induced intestinal acidification (DOI: [10.1128/mbio.00753-23](https://doi.org/10.1128/mbio.00753-23), July 2023) (ng2023singlestrainbehaviorpredicts pages 1-2). | Strong condition→survival/abundance edge, with experimental validation. Gene-level predictors remain partly unresolved. |
| **salinity —induces→ osmotic challenge** | Wu et al.: microorganisms endure salinity by **“either the ‘salt-in’ strategy, involving inorganic ion uptake, or the ‘salt-out’ strategy, relying on compatible solutes”** (DOI: [10.1186/s40168-024-01817-w](https://doi.org/10.1186/s40168-024-01817-w), June 2024) (wu2024metagenomicinsightsinto pages 1-2). | General mechanistic edge; applicable broadly, but the downstream strategy varies by taxon. |
| **Trk-type K+ transport —promotes→ high-salinity persistence** | Among **12,162 COGs**, 40 were selected; eight concerned osmoregulation and COG0168 was **“ranked as the most important feature”**, increasing with salinity across metagenomes, stenohaline MAGs, Actinobacteriota, and Proteobacteria (wu2024metagenomicinsightsinto pages 1-2). | **Medium-confidence association**, not direct knockout causality. Prefer `positively_associated_with` until experimentally tested in relevant isolates. |
| **salinity regime —structures→ estuarine taxonomic and functional composition** | The study reconstructed **127 MAGs**: 33 low-, 36 intermediate-, and 44 high-salinity stenohaline MAGs plus 14 euryhaline MAGs. Community separation was significant (ANOSIM `p=0.0098`, 99,999 permutations); stenohaline categories also differed (`p=0.001`) (wu2024metagenomicinsightsinto pages 7-9). | Strong habitat-filtering edge in the Pearl River Estuary; not necessarily transferable quantitatively to other estuaries. |
| **root-exudate ligand —activates→ MCP–CheW–CheA/CheY chemotaxis pathway** | MCPs bind root-exudate ligands, modulate CheA autophosphorylation, transfer the signal to CheY, and thereby control motor proteins (DOI: [10.1093/femsre/fuad066](https://doi.org/10.1093/femsre/fuad066), published online December 2023; 2024 volume) (liu2024rootcolonizationby pages 3-4). | Mechanistically strong pathway edge, but ligand/receptor pairs are species-specific. Create separate edges for experimentally identified pairs. |
| **chemotaxis and motility —determine→ root-zone colonization preference** | The review concludes: **“bacterial chemotaxis and motility determine the site preferences for colonization in different root zones”** (liu2024rootcolonizationby pages 3-4). | Curatable as a rhizosphere/rhizoplane-specific process edge, not a universal habitat-association mechanism. |
| **AmrZ/FleQ hub —regulates→ motility–biofilm transition** | In *Pseudomonas ogarae* F113, AmrZ and FleQ inversely regulate motility, extracellular-matrix production, and iron homeostasis; c-di-GMP is produced under AmrZ control and sensed by FleQ. The system functions in culture and rhizosphere (DOI: [10.3390/microorganisms11041037](https://doi.org/10.3390/microorganisms11041037), 15 April 2023) (blancoromero2023adaptionofpseudomonas pages 1-2). | Strong but **taxon-specific** regulatory subgraph. Do not universalize AmrZ/FleQ to all rhizobacteria. |
| **extracellular long-chain AHLs —increase→ surface motility** | A synthetic long-chain AHL mixture **“can improve rhizobial surface motility”** in *Sinorhizobium fredii* (DOI: [10.1038/s41396-023-01357-5](https://doi.org/10.1038/s41396-023-01357-5), 10 January 2023) (ji2023rhizobialmigrationtoward pages 1-2). | Direct experimental edge; high confidence in this organism and assay. |
| **extracellular long-chain AHLs —enhance→ migration toward roots and rhizoplane colonization** | When the mixture was placed in the rhizosphere, migration and colonization **“were enhanced in a diffusible way”** (ji2023rhizobialmigrationtoward pages 1-2). | Direct intervention. Curate with *S. fredii* and soybean/rice/maize context qualifiers. |
| **exoFQP function —promotes→ rhizoplane colonization** | Mutations in `exoFQP`, encoding EPS polymerization/secretion membrane proteins, **“led to severely impaired colonization rates,”** whereas mutations in EPS-biosynthesis `exo` genes did not show the same result (ji2023rhizobialmigrationtoward pages 1-2). | High-confidence genetic edge. Critically, do not simplify this to “EPS biosynthesis causes colonization”; the paper distinguishes export machinery and migration/AHL effects from bulk EPS quantity. |
| **fadL-mediated long-chain AHL uptake —reduces/modulates→ extracellular long-chain AHLs and colonization** | The `fadL` mutant had elevated extracellular long-chain AHLs and high colonization; genetics and physiology implicated FadL in long-chain AHL uptake (ji2023rhizobialmigrationtoward pages 1-2). | High-confidence in *S. fredii*, but direction should be encoded carefully: FadL promotes uptake, which lowers extracellular signal; the knockout indirectly raises motility/colonization. |
| **siderophore-dependent biofilm competence —supports→ competitive root colonization** | Siderophore-defective *Bacillus* and *Pseudomonas* mutants failed to form biofilms and competitively colonize roots; soluble iron is limiting in many rhizospheres (liu2024rootcolonizationby pages 7-8). | Promising but based here on review synthesis of multiple studies. Retrieve and curate the primary mutant papers before adding a universal edge. |

## 4. Recent developments, applications, and expert analysis

### Genome-to-niche prediction

A major 2023–2024 development is movement from taxonomy-based habitat annotation toward genome-based quantitative prediction. Models have been applied to optimal growth temperature in more than 2,500 cultured strains, pH preference in more than 4,500 taxa spanning 38 phyla, and combined oxygen, temperature, pH, and salinity preferences across more than 85,000 GTDB genomes (ramoneda2024leveraginggenomicinformation pages 6-7). Applications include cultivation-condition design, selection of microbial inoculants or probiotics, species-distribution modeling, and forecasting microbiome responses to environmental change (ramoneda2023buildingagenomebased pages 1-1, ramoneda2024leveraginggenomicinformation pages 1-2).

The authoritative 2024 assessment is cautious: environmental preference is a complex phenotype requiring multiple traits, and robust models should use phylogenetically stratified validation or out-of-clade tests rather than random train/test splits that can exploit shared ancestry (ramoneda2024leveraginggenomicinformation pages 1-2, ramoneda2024leveraginggenomicinformation pages 4-6).

### Natural-gradient metagenomics

Wu et al. operationalized salinity niche breadth directly from MAG abundance and combined this with feature selection. The natural-gradient design supplies ecologically realistic evidence but cannot by itself separate salinity from covarying pH, nutrients, oxygen, or phylogeny. The authors found no clean salinity clustering from whole-MAG COG profiles and explicitly recognized taxonomic effects, reinforcing that COG0168 is a candidate mechanism rather than proven cause (wu2024metagenomicinsightsinto pages 7-9).

### Mechanistic engineering of root association

Root-associated applications include biofertilizer establishment and microbiome engineering. The strongest actionable findings are not generic “biofilm genes,” but specific control points: MCP ligand sensing, motility-to-biofilm switching, AHL availability, EPS-export machinery, and nutrient acquisition. Rhizosphere abundance can reach approximately `10^7–10^8` bacterial CFU per gram of soil—about two orders of magnitude above surrounding soil—yet root filtering can reduce diversity (blancoromero2023adaptionofpseudomonas pages 1-2). This high biomass does not mean every enriched organism is a stable root specialist.

The *S. fredii* work is especially valuable for TraitMech because it combines a roughly **600,000-colony transposon library**, three independent libraries/experiments, four host plants, mutants, synthetic signals, and colonization assays (ji2023rhizobialmigrationtoward pages 1-2). It shows why curation must preserve intermediate mechanisms: `fadL` and `exoFQP` altered extracellular AHL composition and migration, not merely survival or total EPS.

## 5. Recommended minimal graph modules

### Module A: physicochemical environmental filtering

1. pH → imposes proton/homeostasis challenge.
2. Cytoplasmic pH-homeostasis processes → promote growth across a compatible pH range.
3. Compatible growth range → promotes persistence/relative abundance along the pH gradient.
4. Repeated occupancy optimum → supports pH-defined habitat association.

Steps 1, 3, and 4 are well supported. Individual gene→homeostasis edges require primary experimental evidence; the 2023 genome study alone supports association, not causation (ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 1-1).

### Module B: salinity association

1. High external salinity → osmotic stress.
2. Trk-mediated K+ uptake → intracellular ion accumulation (“salt-in”).
3. Compatible-solute synthesis/uptake → osmotic balance (“salt-out”).
4. Osmotic homeostasis → growth/persistence at high salinity.
5. Persistence across salinity classes → stenohaline/euryhaline habitat association.

For the Pearl River graph, the COG0168 edge should carry `evidence_type: metagenomic_association`, not an unqualified causal predicate (wu2024metagenomicinsightsinto pages 1-2).

### Module C: rhizoplane association

1. Root exudate ligand → MCP–CheW–CheA/CheY signaling.
2. Chemotaxis signaling → directional motility toward roots.
3. Long-chain extracellular AHLs → surface motility.
4. Motility → migration from rhizosphere to rhizoplane.
5. Adhesion and regulated motility–biofilm transition → persistent colonization.
6. Persistent rhizoplane colonization → plant-root habitat association.

This module has the strongest intervention-backed edges, but should retain organism and host qualifiers (blancoromero2023adaptionofpseudomonas pages 1-2, liu2024rootcolonizationby pages 3-4, ji2023rhizobialmigrationtoward pages 1-2).

## 6. Warnings: claims not yet suitable for unqualified curation

1. **Do not curate genomic enrichment as causation.** The pH-associated genes, COG0168, and most genome-to-environment machine-learning features are predictive associations.
2. **Do not equate habitat detection with primary habitat.** Contamination, dormant cells, dispersal, sequencing depth, and transient passage can produce occurrence without growth.
3. **Do not propagate strain findings taxonomically.** Both pH/osmolality tolerance and root-colonization mechanisms vary among closely related strains (ng2023singlestrainbehaviorpredicts pages 1-2, liu2024rootcolonizationby pages 3-4).
4. **Do not assert “EPS abundance → colonization” from the *S. fredii* paper.** The decisive phenotype involved `exoFQP`, extracellular AHLs, and migration; EPS-biosynthetic mutants behaved differently (ji2023rhizobialmigrationtoward pages 1-2).
5. **Do not use “host-associated” as equivalent to pathogenic.** The ecological class spans mutualists, commensals, and pathogens.
6. **Do not add genome reduction as a generic cause of host association from the present evidence set.** It is often a consequence of long-term host restriction and dependency; a dedicated primary-literature subgraph is needed to establish direction and taxonomic scope.
7. **Do not merge habitat association with pH, salinity, oxygen, or temperature tolerance.** These are mechanistic component traits and should connect through survival/growth outcomes.
8. **Verify all ontology records against current releases.** No CURIE should be committed solely from label matching; composite outcomes may appropriately remain label-only.
9. **Treat the 2024 trait–environment preprint as provisional.** Its adaptation index is promising but correlation-based and was a bioRxiv preprint in the retrieved evidence (ren2024microbialstrategiesof pages 7-11).

## DOI-first bibliography

1. Ramoneda J, Stallard-Olivera E, Hoffert M, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances* 9 (April 2023). DOI: [10.1126/sciadv.adf8998](https://doi.org/10.1126/sciadv.adf8998). (ramoneda2023buildingagenomebased pages 3-5, ramoneda2023buildingagenomebased pages 1-1)
2. Ng KM, Pannu S, Liu S, et al. **Single-strain behavior predicts responses to environmental pH and osmolality in the gut microbiota.** *mBio* (July 2023). DOI: [10.1128/mbio.00753-23](https://doi.org/10.1128/mbio.00753-23). (ng2023singlestrainbehaviorpredicts pages 1-2)
3. Ji Y-Y, Zhang B, Zhang P, et al. **Rhizobial migration toward roots mediated by FadL-ExoFQP modulation of extracellular long-chain AHLs.** *The ISME Journal* 17:417–431 (published 10 January 2023). DOI: [10.1038/s41396-023-01357-5](https://doi.org/10.1038/s41396-023-01357-5). (ji2023rhizobialmigrationtoward pages 1-2)
4. Blanco-Romero E, Durán D, Garrido-Sanz D, et al. **Adaption of Pseudomonas ogarae F113 to the Rhizosphere Environment—The AmrZ-FleQ Hub.** *Microorganisms* 11:1037 (15 April 2023). DOI: [10.3390/microorganisms11041037](https://doi.org/10.3390/microorganisms11041037). (blancoromero2023adaptionofpseudomonas pages 1-2)
5. Ramoneda J, Hoffert M, Stallard-Olivera E, Casamayor EO, Fierer N. **Leveraging genomic information to predict environmental preferences of bacteria.** *The ISME Journal* 18 (2024). DOI: [10.1093/ismejo/wrae195](https://doi.org/10.1093/ismejo/wrae195). (ramoneda2024leveraginggenomicinformation pages 6-7, ramoneda2024leveraginggenomicinformation pages 1-2, ramoneda2024leveraginggenomicinformation pages 4-6)
6. Wu Z, Li M, Qu L, Zhang C, Xie W. **Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary.** *Microbiome* 12:115 (June 2024). DOI: [10.1186/s40168-024-01817-w](https://doi.org/10.1186/s40168-024-01817-w). (wu2024metagenomicinsightsinto pages 7-9, wu2024metagenomicinsightsinto pages 1-2)
7. Liu Y, Xu Z, Chen L, et al. **Root colonization by beneficial rhizobacteria.** *FEMS Microbiology Reviews* 48 (2024; available online December 2023). DOI: [10.1093/femsre/fuad066](https://doi.org/10.1093/femsre/fuad066). (liu2024rootcolonizationby pages 3-4, liu2024rootcolonizationby pages 7-8)
8. Ren M, Hu A, Zhao Z, et al. **Microbial strategies of environmental adaptation revealed by trait-environmental relationships.** *bioRxiv* (17 September 2024; preprint). DOI: [10.1101/2024.09.17.613589](https://doi.org/10.1101/2024.09.17.613589). (ren2024microbialstrategiesof pages 7-11)

**Overall recommendation:** curate the environmental-filtering and experimentally demonstrated rhizoplane modules now; retain pH-gene and salinity-gene links as qualified associations. The generic `habitat association` node should be the endpoint of context-specific survival, growth, and colonization pathways rather than the direct object of every molecular edge.

References

1. (ramoneda2024leveraginggenomicinformation pages 6-7): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 30 citations.

2. (ramoneda2024leveraginggenomicinformation pages 1-2): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 30 citations.

3. (wu2024metagenomicinsightsinto pages 1-2): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

4. (ng2023singlestrainbehaviorpredicts pages 1-2): Katharine M. Ng, Sagar Pannu, Sijie Liu, Juan C. Burckhardt, Thad Hughes, Will Van Treuren, Jen Nguyen, Kisa Naqvi, Bachviet Nguyen, Charlotte A. Clayton, Deanna M. Pepin, Samuel R. Collins, and Carolina Tropini. Single-strain behavior predicts responses to environmental ph and osmolality in the gut microbiota. mBio, Jul 2023. URL: https://doi.org/10.1128/mbio.00753-23, doi:10.1128/mbio.00753-23. This article has 42 citations and is from a domain leading peer-reviewed journal.

5. (blancoromero2023adaptionofpseudomonas pages 1-2): Esther Blanco-Romero, David Durán, Daniel Garrido-Sanz, Miguel Redondo-Nieto, Marta Martín, and Rafael Rivilla. Adaption of pseudomonas ogarae f113 to the rhizosphere environment—the amrz-fleq hub. Microorganisms, 11:1037, Apr 2023. URL: https://doi.org/10.3390/microorganisms11041037, doi:10.3390/microorganisms11041037. This article has 4 citations.

6. (liu2024rootcolonizationby pages 3-4): Yunpeng Liu, Zhihui Xu, Lin Chen, Weibing Xun, Xia Shu, Yu Chen, Xinli Sun, Zhengqi Wang, Yi Ren, Qirong Shen, and Ruifu Zhang. Root colonization by beneficial rhizobacteria. FEMS Microbiology Reviews, Dec 2024. URL: https://doi.org/10.1093/femsre/fuad066, doi:10.1093/femsre/fuad066. This article has 220 citations and is from a domain leading peer-reviewed journal.

7. (ramoneda2023buildingagenomebased pages 1-1): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

8. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 97 citations and is from a highest quality peer-reviewed journal.

9. (wu2024metagenomicinsightsinto pages 7-9): Ziheng Wu, Minchun Li, Liping Qu, Chuanlun Zhang, and Wei Xie. Metagenomic insights into microbial adaptation to the salinity gradient of a typical short residence-time estuary. Microbiome, Jun 2024. URL: https://doi.org/10.1186/s40168-024-01817-w, doi:10.1186/s40168-024-01817-w. This article has 69 citations and is from a highest quality peer-reviewed journal.

10. (ji2023rhizobialmigrationtoward pages 1-2): Yuan-Yuan Ji, Biliang Zhang, Pan Zhang, Liu-Chi Chen, You-Wei Si, Xi-Yao Wan, Can Li, Ren-He Wang, Yu Tian, Ziding Zhang, and Chang-Fu Tian. Rhizobial migration toward roots mediated by fadl-exofqp modulation of extracellular long-chain ahls. The ISME Journal, 17:417-431, Jan 2023. URL: https://doi.org/10.1038/s41396-023-01357-5, doi:10.1038/s41396-023-01357-5. This article has 27 citations.

11. (liu2024rootcolonizationby pages 7-8): Yunpeng Liu, Zhihui Xu, Lin Chen, Weibing Xun, Xia Shu, Yu Chen, Xinli Sun, Zhengqi Wang, Yi Ren, Qirong Shen, and Ruifu Zhang. Root colonization by beneficial rhizobacteria. FEMS Microbiology Reviews, Dec 2024. URL: https://doi.org/10.1093/femsre/fuad066, doi:10.1093/femsre/fuad066. This article has 220 citations and is from a domain leading peer-reviewed journal.

12. (ramoneda2024leveraginggenomicinformation pages 4-6): Josep Ramoneda, Michael Hoffert, Elias Stallard-Olivera, Emilio O Casamayor, and Noah Fierer. Leveraging genomic information to predict environmental preferences of bacteria. The ISME Journal, Jan 2024. URL: https://doi.org/10.1093/ismejo/wrae195, doi:10.1093/ismejo/wrae195. This article has 30 citations.

13. (ren2024microbialstrategiesof pages 7-11): Minglei Ren, Ang Hu, Zhonghua Zhao, Xiaolong Yao, Ismael Aaron Kimirei, Lu Zhang, and Jianjun Wang. Microbial strategies of environmental adaptation revealed by trait-environmental relationships. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.17.613589, doi:10.1101/2024.09.17.613589. This article has 0 citations.