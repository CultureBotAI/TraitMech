---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T03:29:01.540497'
end_time: '2026-06-18T03:59:13.885214'
duration_seconds: 1812.34
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mobile genetic element
  trait_identifier: traitmech:000089
  trait_category: GENOMICS
  trait_category_slug: genomics
  trait_slug: mobile_genetic_element
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A genomics trait describing possession of DNA segments that can move
    within or between genomes and mediate horizontal gene transfer, including plasmids,
    prophages, transposable elements, and genomic islands.
  parent_traits: METPO:1000188
  synonyms: MGE
  evidence_summary: 'DOI:10.1038/nrmicro1235:  (Frost et al. review mobile genetic
    elements as the agents of horizontal gene transfer and genome plasticity; parent
    of the plasmid, prophage, transposable- element, and genomic-island sub-variants.)
    | DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review insertion
    sequences as a major class of mobile genetic elements shaping bacterial genomes.)'
  causal_graph_summary: 'mge_horizontal_gene_transfer: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 57
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mobile genetic element
- **METPO identifier:** traitmech:000089
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of DNA segments that can move within or between genomes and mediate horizontal gene transfer, including plasmids, prophages, transposable elements, and genomic islands.
- **Parent traits:** METPO:1000188
- **Synonyms:** MGE
- **Existing evidence:** DOI:10.1038/nrmicro1235:  (Frost et al. review mobile genetic elements as the agents of horizontal gene transfer and genome plasticity; parent of the plasmid, prophage, transposable- element, and genomic-island sub-variants.) | DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review insertion sequences as a major class of mobile genetic elements shaping bacterial genomes.)
- **Existing causal graph summary:** mge_horizontal_gene_transfer: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mobile genetic element** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/mobile_genetic_element.yaml`.

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
- **Trait label:** mobile genetic element
- **METPO identifier:** traitmech:000089
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of DNA segments that can move within or between genomes and mediate horizontal gene transfer, including plasmids, prophages, transposable elements, and genomic islands.
- **Parent traits:** METPO:1000188
- **Synonyms:** MGE
- **Existing evidence:** DOI:10.1038/nrmicro1235:  (Frost et al. review mobile genetic elements as the agents of horizontal gene transfer and genome plasticity; parent of the plasmid, prophage, transposable- element, and genomic-island sub-variants.) | DOI:10.1111/1574-6976.12067:  (Siguier, Gourbeyre & Chandler review insertion sequences as a major class of mobile genetic elements shaping bacterial genomes.)
- **Existing causal graph summary:** mge_horizontal_gene_transfer: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **mobile genetic element** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/mobile_genetic_element.yaml`.

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


## Research report: Microbial trait “mobile genetic element” (TraitMech / METPO)

**Target trait:** mobile genetic element (MGE); **METPO identifier:** traitmech:000089; **Category:** Genomics; **Definition (curation-ready):** microbial genomic segments that **move within and/or between genomes** and thereby mediate horizontal gene transfer (HGT), including **plasmids, prophages/phages, insertion sequences/transposons, integrative elements (ICE/IME/CIME/AICE), genomic islands, and integrons**. (weisberg2023mobilegeneticelement pages 1-2, tokuda2024microbialevolutionthrough pages 1-3)

### 1) Trait scope (what it represents; boundary cases)

**Core meaning for TraitMech.** In current usage, “mobile genetic elements” are defined by **mobility (intracellular or intercellular) and capacity to mobilize genes** rather than a single molecular form. Weisberg & Chang (Annual Review of Microbiology, Sep 2023) explicitly define MGEs as elements that “can move within and between genomes,” and enumerate classes including plasmids, ICEs/IMEs, integrons, transposons/IS, and phages. (weisberg2023mobilegeneticelement pages 1-2)

**Key boundary distinctions relevant for curation.**

1. **Extrachromosomal vs chromosomally integrated.** Plasmids are defined as “an extrachromosomal replicon, circular or linear, that is often replicated independent of the chromosome,” while ICEs/IMEs are chromosomally integrating MGEs. (weisberg2023mobilegeneticelement pages 1-2, tokuda2024microbialevolutionthrough pages 3-4)
2. **Self-transmissible vs mobilizable vs non-transferable.** Plasmids can be “conjugative, mobilizable, or nonmobilizable.” ciMGE classes also separate by autonomy: ICEs encode an intact conjugation apparatus (self-transmissible), IMEs encode excision/integration but **lack** full conjugation apparatus (mobilizable in trans), and CIMEs lack key genes and are non-autonomous. (weisberg2023mobilegeneticelement pages 1-2, botelho2023defensesystemsare pages 1-2, tokuda2024microbialevolutionthrough pages 3-4)
3. **Transposable vs conjugative vs phage-mediated mobility.** Tokuda & Shintani (Microbial Biotechnology, Jan 2024) emphasize that MGEs can mediate HGT by moving **between replicons** (e.g., transposons/IS, integrons) or **between bacterial cells** (e.g., plasmids/ICEs via conjugation; phages via transduction). (tokuda2024microbialevolutionthrough pages 1-3)
4. **Integrons as a boundary case (“immobile platform”).** Integrons are described as cassette capture/expression systems that are “not transposed or transferred like transposons or ciMGEs” and are often found on transferable plasmids, i.e., they are frequently **mobilized by association** with other MGEs rather than being independently mobile. (tokuda2024microbialevolutionthrough pages 3-4, fahy2024fromspeciesto pages 4-5)

**Practical “trait observation.”** For TraitMech, the phenotype is usually inferred from **genomic detection**: presence of hallmark modules (integrase/relaxase/T4SS for ICEs; intI/attI/Pc for integrons; transposases for IS/Tn; prophage hallmark genes), or empirical demonstration of excision/circularization/transfer (e.g., ICE circular forms). (lee2024genomicanalysisof pages 1-2, wang2024iceberg3.0functional pages 1-2)

### 2) Key concepts & mechanistic entities (current understanding)

MGEs are often conceptualized as **modular systems**: **core genes** for “maintenance and transmission” plus **accessory (cargo) genes** that can be “shuffled extensively” and recombined among MGEs, enabling rapid ecological adaptation (e.g., antimicrobial resistance, defense, metabolic traits). (weisberg2023mobilegeneticelement pages 2-4)

#### 2.1 ICE/IME lifecycle (excision → circularization → conjugative transfer → integration)

A concise, source-backed lifecycle for ICEs (and similarly for IMEs, with dependence on other conjugation systems) is given in Lee et al. (Applied and Environmental Microbiology, Oct 2024): induction of ICE gene expression; **excision** mediated by an **integrase** and **excisionase/RDF**; **circular dsDNA intermediate** formation; relaxase nicking/unwinding at **oriT** with covalent attachment; ssDNA transfer through an element-encoded **type IV secretion system (T4SS)** with rolling-circle replication; recipient circularization/dsDNA conversion and chromosomal integration. (lee2024genomicanalysisof pages 1-2)

A mechanistic schematic for ICEclc (Pseudomonas putida) directly labels these entities and steps, including **attL/attR/attP**, **int**, **traI**, and T4SS components including **VirB4/VirD4 homologs**. (daveri2023characterizationofan media 9a925cd0)

#### 2.2 Plasmid mobility classes and dependence networks

Plasmids span a continuum from fully conjugative (encode relaxase + mating pair formation/T4SS genes) to mobilizable (encode oriT + relaxase but depend on other conjugation machinery) to non-transferable. A large genomic survey in E. coli and S. aureus shows that only ~1/4 of plasmids encode full conjugation machinery (MPF), mobilizable plasmids are similarly frequent, and ~half lack both relaxase and MPF; nevertheless, by identifying oriT-like regions and dependencies, mechanisms can be proposed for ~90% of plasmids. (aresarroyo2023originsoftransfer pages 1-2)

#### 2.3 Integron cassette capture and expression

Integrons are defined mechanistically by the trio **integrase (intI), recombination site (attI), and promoter (Pc)**, with gene cassettes integrated by site-specific recombination between **attI and attC** assisted by the integron integrase. (fahy2024fromspeciesto pages 4-5, tokuda2024microbialevolutionthrough pages 3-4)

#### 2.4 Transposons/insertion sequences and transposition

Transposons/IS are described as elements that excise/transpose within genomes; they frequently serve as “highly connected” mobilizing agents in mobilome networks, and can mobilize cargo genes (including AMR genes) especially when nested on conjugative plasmids or ICEs. (weisberg2023mobilegeneticelement pages 2-4, tokuda2024microbialevolutionthrough pages 1-3)

#### 2.5 Prophages/transduction

Phage-mediated HGT includes generalized transduction and host DNA packaging during prophage induction. Wolput et al. (Nucleic Acids Research, Jun 2024) provide a concrete example where host regions were “highly packaged and transduced during both P22 prophage induction and lytic infection,” and identify pac-like sequences that bias high-frequency transfer of downstream chromosomal regions. (botelho2023defensesystemsare pages 2-3)

### 3) Candidate causal-graph nodes (grouped by type)

| Type | Node label | Suggested ontology grounding | Notes/examples |
|---|---|---|---|
| MGE classes | mobile genetic element | traitmech:000089 | Parent trait covering DNA elements that move within or between genomes; includes plasmids, prophages, transposons/IS, integrative elements, genomic islands, and integrons (weisberg2023mobilegeneticelement pages 1-2, tokuda2024microbialevolutionthrough pages 1-3) |
| MGE classes | plasmid | un-grounded | Extrachromosomal replicon; may be conjugative, mobilizable, or nonmobilizable; key vehicle for AMR and other cargo genes (weisberg2023mobilegeneticelement pages 1-2, fahy2024fromspeciesto pages 4-5) |
| MGE classes | prophage / bacteriophage-derived MGE | un-grounded | Phage genomes can integrate into chromosomes and mediate HGT by excision/transduction; relevant boundary with viral elements (tokuda2024microbialevolutionthrough pages 3-4, tokuda2024microbialevolutionthrough pages 1-3) |
| MGE classes | insertion sequence (IS) | un-grounded | Small transposable element; can mobilize resistance genes as part of composite transposons (fahy2024fromspeciesto pages 4-5, weisberg2023mobilegeneticelement pages 2-4) |
| MGE classes | transposon | un-grounded | DNA element moving between replicons via transposase; intracellular mobility unless carried on plasmids/ICEs (tokuda2024microbialevolutionthrough pages 4-5, weisberg2023mobilegeneticelement pages 2-4) |
| MGE classes | integrative and conjugative element (ICE) | un-grounded | Chromosomally integrated, self-transmissible conjugative element with integrase, relaxase, and T4SS functions (botelho2023defensesystemsare pages 1-2, tokuda2024microbialevolutionthrough pages 3-4) |
| MGE classes | integrative and mobilizable element (IME) | un-grounded | Integrated element encoding excision/integration but lacking full conjugation machinery; mobilized in trans (botelho2023defensesystemsare pages 1-2, tokuda2024microbialevolutionthrough pages 3-4) |
| MGE classes | actinomycete ICE (AICE) | un-grounded | ICE subset lacking T4SS but encoding integrase/replication/AICE translocation proteins (botelho2023defensesystemsare pages 1-2) |
| MGE classes | cis-mobilizable element (CIME) | un-grounded | Flanked by attL/attR but lacking conjugation/recombination genes; non-autonomous chromosomal island (botelho2023defensesystemsare pages 1-2, tokuda2024microbialevolutionthrough pages 3-4) |
| MGE classes | genomic island (GI) | un-grounded | Broad class of horizontally acquired chromosomal islands; some are self-transmissible, mobilizable, or nonmobilizable (audrey2023asystematicapproach pages 1-2, audrey2023asystematicapproach pages 6-8) |
| MGE classes | integron | un-grounded | Gene-capture platform with integrase, attI, and promoter Pc; generally immobile, often borne on plasmids/transposons (tokuda2024microbialevolutionthrough pages 3-4, fahy2024fromspeciesto pages 4-5) |
| Molecular functions/processes | conjugative transfer | GO:0000746 | Cell-to-cell DNA transfer process used by plasmids and ICEs (lee2024genomicanalysisof pages 1-2, tokuda2024microbialevolutionthrough pages 1-3) |
| Molecular functions/processes | excision from chromosome | GO:0016446 | Core ICE/IME/prophage step preceding mobility; often integrase/RDF-mediated (daveri2023characterizationofan pages 1-2, lee2024genomicanalysisof pages 1-2) |
| Molecular functions/processes | circularization of excised element | un-grounded | Formation of extrachromosomal circular dsDNA intermediate before transfer (daveri2023characterizationofan pages 1-2, lee2024genomicanalysisof pages 1-2) |
| Molecular functions/processes | integration into chromosome | GO:0015074 | Reintegration of ICE/prophage into recipient chromosome (tokuda2024microbialevolutionthrough pages 3-4) |
| Molecular functions/processes | oriT nicking / relaxosome processing | GO:0006310 | Relaxase-mediated nicking/unwinding at origin of transfer (lee2024genomicanalysisof pages 1-2, aresarroyo2023originsoftransfer pages 1-2) |
| Molecular functions/processes | rolling-circle transfer replication | GO:0006278 | ssDNA transfer intermediate for many conjugative elements (lee2024genomicanalysisof pages 1-2) |
| Molecular functions/processes | type IV secretion-mediated DNA transport | GO:1901678 | T4SS-dependent DNA translocation during conjugation (daveri2023characterizationofan pages 1-2, aresarroyo2023originsoftransfer pages 1-2) |
| Molecular functions/processes | transposition | GO:0032197 | Movement of IS/transposons within or between replicons (tokuda2024microbialevolutionthrough pages 4-5, weisberg2023mobilegeneticelement pages 2-4) |
| Molecular functions/processes | site-specific recombination | GO:0006310 | Integrase/IntI-mediated recombination at att sites or integron cassette sites (tokuda2024microbialevolutionthrough pages 3-4, fahy2024fromspeciesto pages 4-5) |
| Molecular functions/processes | integron cassette capture/excision | un-grounded | IntI-mediated insertion/excision of gene cassettes at attI/attC (tokuda2024microbialevolutionthrough pages 3-4, fahy2024fromspeciesto pages 4-5) |
| Molecular functions/processes | transduction | GO:0009291 | Phage-mediated transfer of bacterial DNA, including host DNA packaging after prophage induction (tokuda2024microbialevolutionthrough pages 3-4, botelho2023defensesystemsare pages 2-3) |
| Genes/proteins/complexes | integrase (ICE/prophage) | GO:0015074 | Recombination enzyme for excision/integration; common marker for integrated MGEs (lee2024genomicanalysisof pages 1-2, botelho2023defensesystemsare pages 1-2) |
| Genes/proteins/complexes | excisionase / recombination directionality factor (RDF) | un-grounded | Promotes excision directionality with integrase (lee2024genomicanalysisof pages 1-2, audrey2023asystematicapproach pages 6-8) |
| Genes/proteins/complexes | relaxase | GO:0015074 | DNA-processing enzyme for conjugation; key plasmid/ICE mobility marker (lee2024genomicanalysisof pages 1-2, aresarroyo2023originsoftransfer pages 1-2) |
| Genes/proteins/complexes | TraI relaxase | un-grounded | Specific relaxase exemplar required for ICEclc transfer and common in F-like systems (daveri2023characterizationofan pages 1-2, daveri2023characterizationofan media 9a925cd0) |
| Genes/proteins/complexes | type IV coupling protein (T4CP) | un-grounded | Substrate receptor linking relaxase-DNA complex to T4SS; includes VirD4/TraD-like proteins (aresarroyo2023originsoftransfer pages 1-2, daveri2023characterizationofan media 9a925cd0) |
| Genes/proteins/complexes | VirD4 | un-grounded | Canonical T4CP component in conjugative transfer (daveri2023characterizationofan pages 1-2, daveri2023characterizationofan media 9a925cd0) |
| Genes/proteins/complexes | VirB4 | un-grounded | T4SS ATPase and hallmark of conjugative machinery (daveri2023characterizationofan pages 1-2, daveri2023characterizationofan media 9a925cd0) |
| Genes/proteins/complexes | type IV secretion system (T4SS) complex | GO:0030254 | Conjugation nanomachine for transfer of DNA/protein substrates (daveri2023characterizationofan pages 1-2, botelho2023defensesystemsare pages 1-2) |
| Genes/proteins/complexes | transposase | GO:0004803 | Catalyzes movement of transposons/ISs between genomic locations (tokuda2024microbialevolutionthrough pages 4-5, weisberg2023mobilegeneticelement pages 2-4) |
| Genes/proteins/complexes | integron integrase IntI1 | un-grounded | Class 1 integron integrase; recognizes attI/attC and catalyzes cassette recombination (tokuda2024microbialevolutionthrough pages 3-4, fahy2024fromspeciesto pages 4-5) |
| Genes/proteins/complexes | RocRp transformation inhibitor RNA | un-grounded | Plasmid-encoded inhibitor associated with reduced transformation in Legionella; taxon-specific conflict node (mazzamurro2024intragenomicconflictswith pages 10-12) |
| Genomic features/sites | origin of transfer (oriT) | un-grounded | Cis-acting transfer origin recognized by relaxase (lee2024genomicanalysisof pages 1-2, aresarroyo2023originsoftransfer pages 1-2) |
| Genomic features/sites | attI site | un-grounded | Integron recombination site for cassette insertion (tokuda2024microbialevolutionthrough pages 3-4, fahy2024fromspeciesto pages 4-5) |
| Genomic features/sites | attC site | un-grounded | Gene cassette recombination site recognized by IntI integrase (tokuda2024microbialevolutionthrough pages 3-4, fahy2024fromspeciesto pages 4-5) |
| Genomic features/sites | Pc promoter | un-grounded | Integron promoter driving expression of inserted cassettes (tokuda2024microbialevolutionthrough pages 3-4, fahy2024fromspeciesto pages 4-5) |
| Genomic features/sites | attL | un-grounded | Left attachment site flanking integrated ICE/CIME (daveri2023characterizationofan media 9a925cd0, tokuda2024microbialevolutionthrough pages 3-4) |
| Genomic features/sites | attR | un-grounded | Right attachment site flanking integrated ICE/CIME (daveri2023characterizationofan media 9a925cd0, tokuda2024microbialevolutionthrough pages 3-4) |
| Genomic features/sites | attP | un-grounded | Attachment site on excised circular ICE/prophage intermediate (daveri2023characterizationofan media 9a925cd0) |
| Genomic features/sites | pac-like sequence | un-grounded | Host/chromosome sequence directing high-frequency phage packaging and transduction (botelho2023defensesystemsare pages 2-3) |
| Genomic features/sites | defense island | un-grounded | Clustered defense-system region often enriched on ICEs/IMEs/GIs (botelho2023defensesystemsare pages 1-2, audrey2023asystematicapproach pages 6-8) |
| Defense systems | restriction-modification system | GO:0009307 | Major class of anti-phage defense enriched on genomic islands and ciMGEs (audrey2023asystematicapproach pages 6-8, botelho2023defensesystemsare pages 1-2) |
| Defense systems | toxin-antitoxin system | GO:1903508 | Defense/maintenance module found on ciMGEs; may stabilize elements and contribute to conflict (botelho2023defensesystemsare pages 1-2, botelho2023theeskapemobilome pages 13-15) |
| Defense systems | CRISPR-Cas system | GO:0098542 | Adaptive defense sometimes encoded on MGEs; involved in inter-MGE conflict (botelho2023theeskapemobilome pages 13-15) |
| Defense systems | abortive infection (Abi) system | un-grounded | Anti-phage defense class found on some genomic islands (audrey2023asystematicapproach pages 6-8) |
| Defense systems | anti-CRISPR protein | un-grounded | Enriched on ESKAPE MGEs, especially prophage-associated conflict systems (botelho2023theeskapemobilome pages 13-15) |
| Defense systems | BREX system | un-grounded | Example ICE-encoded anti-phage defense cataloged in ICEberg 3.0 (wang2024iceberg3.0functional pages 1-2) |
| Environmental/experimental factors | antibiotic selective pressure | CHEBI:33281 | Selects for accumulation/spread of AMR cargo on self-transmissible ICEs/GIs/plasmids (audrey2023asystematicapproach pages 6-8, botelho2023defensesystemsare pages 1-2) |
| Environmental/experimental factors | phage infection / phage predation | GO:0046718 | Can spur ICE excision and transfer; selects for defense cargo on MGEs (botelho2023defensesystemsare pages 1-2, audrey2023asystematicapproach pages 6-8) |
| Environmental/experimental factors | hospital / clinical setting | ENVO:00002173 | High-transfer, high-selection environment for AMR-carrying MGEs and genomic surveillance (fahy2024fromspeciesto pages 2-4, fahy2024fromspeciesto pages 4-5) |
| Environmental/experimental factors | wastewater treatment plant environment | ENVO:01000993 | Major reservoir/entry point for integrons and ARGs; relevant for environmental MGE surveillance (ali2024integronsinthe pages 9-10) |
| Environmental/experimental factors | human microbiome | ENVO:02000098 | Important reservoir/network for ICE cargo exchange; large ICEberg 3.0 human-microbiome module (wang2024iceberg3.0functional pages 1-2) |
| Environmental/experimental factors | non-transformable host state | un-grounded | State associated with MGE carriage/intragenomic conflict in some taxa (mazzamurro2024intragenomicconflictswith pages 10-12) |
| Environmental/experimental factors | transfer-competent subpopulation | un-grounded | Specialized donor subpopulation in ICEclc lifecycle (daveri2023characterizationofan pages 1-2) |
| Cargo phenotypes | antimicrobial resistance | GO:0046677 | Most prominent clinically relevant cargo phenotype associated with plasmids, integrons, ICEs, and GIs (wang2024iceberg3.0functional pages 1-2, fahy2024fromspeciesto pages 2-4) |
| Cargo phenotypes | virulence factor carriage | GO:0009405 | Common cargo class on mobile islands and plasmids affecting pathogenicity (wang2024iceberg3.0functional pages 1-2, audrey2023asystematicapproach pages 1-2) |
| Cargo phenotypes | heavy metal resistance | GO:0010038 | Frequently co-carried cargo class on MGEs/integrons/plasmids (lee2024genomicanalysisof pages 1-2, wang2024iceberg3.0functional pages 1-2) |
| Cargo phenotypes | anti-phage defense cargo | un-grounded | RM, CRISPR, Abi, BREX, and related systems enriched on ICEs/IMEs/GIs (audrey2023asystematicapproach pages 6-8, wang2024iceberg3.0functional pages 1-2) |
| Cargo phenotypes | symbiosis functions | GO:0044403 | ICEberg 3.0 cargo category; relevant especially outside pathogens (wang2024iceberg3.0functional pages 1-2) |
| Cargo phenotypes | metabolic/degradation functions | GO:0008152 | Accessory gene modules enabling niche adaptation; part of broader MGE cargo concept (wang2024iceberg3.0functional pages 1-2, weisberg2023mobilegeneticelement pages 2-4) |


*Table: This table lists candidate causal-graph nodes for curating the microbial trait 'mobile genetic element', grouped by entity type and annotated with suggested ontology grounding and recent evidence-based notes. It is useful as a starting node inventory for TraitMech YAML curation and edge construction.*

### 4) Evidence-backed candidate causal edges (triples) for TraitMech curation

The following edge table is designed to be directly translated into `mobile_genetic_element.yaml` candidates (with uncertainty flags where claims are general or taxon-specific).

| Edge (subject—predicate—object) | Mechanistic context | Example entities/notes | Evidence snippet (short quote) | Source (DOI + URL + year) |
|---|---|---|---|---|
| integrase + excisionase — enables — ICE excision and circularization | Core ICE/IME lifecycle step before transfer | ICEs/IMEs encode recombinase + RDF/excisionase; circular dsDNA intermediate | “excision mediated by an integrase (recombinase) and an excisionase… formation of a circular dsDNA intermediate” (lee2024genomicanalysisof pages 1-2) | 10.1128/AEM.01360-24; https://doi.org/10.1128/AEM.01360-24; 2024 |
| ICE excision — produces — extrachromosomal circular ICE | Integrated ICE switches to transferable circular form | attL/attR → attP; int-labeled lifecycle schematic for ICEclc | “remain mostly integrated in their host genome, and occasionally excise” and “ICEclc (circular)” (daveri2023characterizationofan pages 1-2, daveri2023characterizationofan media 9a925cd0) | 10.1093/nar/gkad024; https://doi.org/10.1093/nar/gkad024; 2023 |
| relaxase — nicks/unwinds at — oriT | DNA processing for conjugation | Relaxase covalently binds 5′ end; rolling-circle transfer intermediate | “nicking/unwinding by a relaxase at oriT, covalent attachment of relaxase to the 5' end” (lee2024genomicanalysisof pages 1-2) | 10.1128/AEM.01360-24; https://doi.org/10.1128/AEM.01360-24; 2024 |
| TraI relaxase — required for — ICE/plasmid transfer | Specific relaxase exemplar for conjugative MGEs | traI in ICEclc; also common plasmid relaxase class | “Transfer of ICEclc is dependent on the TraI relaxase” (daveri2023characterizationofan pages 1-2) | 10.1093/nar/gkad024; https://doi.org/10.1093/nar/gkad024; 2023 |
| VirD4-like coupling protein — recruits substrate to — T4SS | DNA/protein substrate receptor in conjugation | VirD4 / TraD / T4CP connects relaxase-DNA to mating pore | “the secretion apparatus by the cognate coupling protein TraD” and “type IV coupling proteins (T4CPs)” (aresarroyo2023originsoftransfer pages 1-2) | 10.1128/IAI.00436-22; https://doi.org/10.1128/IAI.00436-22; 2023 |
| VirB4/VirD4-containing T4SS — mediates — conjugative DNA transfer | Transfer apparatus spanning donor/recipient | ICEclc encodes iceB4 (VirB4 homolog), iceD4 (VirD4 homolog) | “VirB4 and VirD4 ATPases of the Type IV secretion system (T4SS)” (daveri2023characterizationofan pages 1-2, daveri2023characterizationofan media 9a925cd0) | 10.1093/nar/gkad024; https://doi.org/10.1093/nar/gkad024; 2023 |
| ICE transfer to recipient — followed by — chromosomal integration | End of ICE lifecycle after ssDNA transfer | Recipient circularization, dsDNA conversion, reintegration | “transfer of a single-stranded DNA molecule, followed by integration into the recipient chromosome” (tokuda2024microbialevolutionthrough pages 3-4) | 10.1111/1751-7915.14408; https://doi.org/10.1111/1751-7915.14408; 2024 |
| IntI1 integron integrase — catalyzes — attI/attC recombination | Integron cassette capture/excision mechanism | Class 1 integron core: intI1, attI, Pc | “IntI1 recognises attI/attC and catalyses site-specific recombination inserting cassettes” (tokuda2024microbialevolutionthrough pages 3-4) | 10.1111/1751-7915.14408; https://doi.org/10.1111/1751-7915.14408; 2024 |
| gene cassette integration — occurs between — attI and attC sites | Structural basis of cassette capture | Often captures ARG cassettes lacking own promoters | “integrated by site-specific recombination between attI and attC assisted by the integron integrase” (fahy2024fromspeciesto pages 4-5) | 10.3390/antibiotics13070661; https://doi.org/10.3390/antibiotics13070661; 2024 |
| Pc promoter — drives expression of — integrated gene cassettes | Explains phenotype after cassette capture | Integron promoter within 5′ conserved segment | “three core features (integrase encoded by intI, recombination site attI, and promoter Pc)” (fahy2024fromspeciesto pages 4-5) | 10.3390/antibiotics13070661; https://doi.org/10.3390/antibiotics13070661; 2024 |
| insertion sequence / transposon — enables — excision and transposition | Transposition within/between replicons | General MGE mechanism; includes IS and composite transposons | “transposons and insertion sequences… ‘excise and move’ or ‘excise and transpose between regions of the genome’” (weisberg2023mobilegeneticelement pages 2-4) | 10.1146/annurev-micro-032521-022006; https://doi.org/10.1146/annurev-micro-032521-022006; 2023 |
| IS elements — mobilize — resistance genes **[uncertain/general]** | Review-level claim; often via composite transposons/promoters | Example given for IS1999/blaOXA-48-like in review | “ISs able to move resistance genes as part of composite transposons” (fahy2024fromspeciesto pages 4-5) | 10.3390/antibiotics13070661; https://doi.org/10.3390/antibiotics13070661; 2024 |
| phage infection/predation — spurs — ICE excision and conjugative transfer | Ecological trigger linking defense and mobility | Important environment-driven edge for mobilization | “phage infection itself spurs the excision of integrative and conjugative elements (ICEs) and subsequent transfer by conjugation” (botelho2023defensesystemsare pages 1-2) | 10.1093/nar/gkad282; https://doi.org/10.1093/nar/gkad282; 2023 |
| prophage induction/lytic infection — increases — transduction of host DNA | Phage-mediated HGT mechanism | pac-like sequences can bias high-frequency packaging | “packaged and transduced during both P22 prophage induction and lytic infection” (botelho2023defensesystemsare pages 2-3) | 10.1093/nar/gkae489; https://doi.org/10.1093/nar/gkae489; 2024 |
| defense systems — are enriched on — ICEs/IMEs/genomic islands | Cargo bias on mobile islands | RM, CRISPR-Cas, Abi; anti-phage defense islands | “~20% of IMEs and ~30% of ICEs carry >=1 [anti-phage defense] system” (audrey2023asystematicapproach pages 6-8) | 10.1093/nar/gkad644; https://doi.org/10.1093/nar/gkad644; 2023 |
| restriction-modification systems — comprise large fraction of — GI anti-phage defenses | Specific defense-system enrichment | RM types I/II/IIG/III/IV dominate known GI defenses | “RM systems… make up 40.9% of anti-phage systems” (audrey2023asystematicapproach pages 6-8) | 10.1093/nar/gkad644; https://doi.org/10.1093/nar/gkad644; 2023 |
| toxin-antitoxin systems — occur in — ciMGE defense islands **[uncertain/general]** | Broad defense/maintenance role on MGEs | TA listed among defense systems on ciMGEs | “Specific marker systems mentioned include… toxin-antitoxin” (botelho2023defensesystemsare pages 1-2) | 10.1093/nar/gkad282; https://doi.org/10.1093/nar/gkad282; 2023 |
| antibiotic selective pressure — enriches — AMR genes on self-transmissible ICEs/GIs | Selection shapes mobile cargo content | Stronger in ICEs than IMEs/AICEs | “The authors explicitly tie antibiotic selective pressure to the accumulation and spread of resistance on self-transmissible ICEs” (audrey2023asystematicapproach pages 6-8) | 10.1093/nar/gkad644; https://doi.org/10.1093/nar/gkad644; 2023 |
| pOriT / conjugation-dependent plasmid mobility — associates with — high AMR gene density | Functional dependency networks for transfer | pOriT highest AMR density among plasmid mobility classes | “pOriT plasmids… carry the highest densities of antimicrobial resistance genes” (aresarroyo2023originsoftransfer pages 1-2) | 10.1093/nar/gkac1079; https://doi.org/10.1093/nar/gkac1079; 2023 |
| MGE burden — negatively associates with — natural transformation | Intragenomic conflict between incoming DNA systems | Seen across plasmids, prophages, transposons, conjugative elements | “GWAS confirmed systematic negative associations between transformation and MGEs” and “transformable strains have fewer MGEs” (mazzamurro2024intragenomicconflictswith pages 10-12) | 10.1371/journal.pbio.3002814; https://doi.org/10.1371/journal.pbio.3002814; 2024 |
| plasmids / prophages / transposable elements — inhibit or reduce — transformation **[uncertain/taxon-specific]** | Species-specific conflict patterns | Legionella: plasmids/conjugative elements; Acinetobacter: prophages; both: transposons | “negative associations between transformation and MGEs: plasmids and other conjugative elements in Lp, prophages in Ab, and transposable elements in both” (mazzamurro2024intragenomicconflictswith pages 10-12) | 10.1371/journal.pbio.3002814; https://doi.org/10.1371/journal.pbio.3002814; 2024 |


*Table: This table compiles candidate causal edges for the mobile genetic element trait, emphasizing mechanisms directly useful for TraitMech curation. It prioritizes recent sources and flags broad review-level or taxon-specific claims as uncertain where appropriate.*

### 5) Recent developments & latest research (prioritizing 2023–2024)

**Large-scale “mobilome” catalogs and distributions.** Botelho (NAR, Mar 2023) scanned >20,000 genomes and identified 13,274 chromosomally integrated MGEs (ciMGEs), reporting that **36.5% of bacterial genomes** (8000/21,897) and **3.7% of archaeal genomes** (16/437) carried ≥1 ciMGE; IMEs were most frequent, and ICEs were larger on average (consistent with encoding full conjugation machinery). (botelho2023defensesystemsare pages 2-3)

**Quantitative cargo patterns on genomic islands.** A genomic island mobility classification study reported that ~6% of IMEs and ~30% of ICEs carry at least one antibiotic resistance determinant; anti-phage defenses were present in ~20% of IMEs and ~30% of ICEs, with restriction–modification systems comprising ~40.9% of annotated GI anti-phage defenses. (audrey2023asystematicapproach pages 6-8)

**Conflict and coevolution with host defense and transformation.** Intragenomic conflicts can shape competence: across Legionella pneumophila and Acinetobacter baumannii, GWAS found systematic negative associations between transformation and MGEs, and “transformable strains have fewer MGEs”; negative associations differed by MGE type across taxa (e.g., prophages in Ab). (mazzamurro2024intragenomicconflictswith pages 10-12)

**Integron prevalence and environmental persistence.** A 2024 integron review reports that ~15% of sequenced bacterial genomes carry integrons, and highlights wastewater treatment plants and hospital effluent as major reservoirs/entry points where integron removal can be incomplete or variable depending on measurement (e.g., normalized copy numbers sometimes unchanged). (ali2024integronsinthe pages 9-10)

### 6) Current applications and real-world implementations

**6.1 Databases and detection tools (operationalizing the trait).**

- **ICEberg 3.0 / ICEfinder 2.0 (NAR Database Issue, Oct 2024):** ICEberg 3.0 contains **2065 ICEs, 607 IMEs, 275 CIMEs**, including **430 with experimental support**; it also curated **1386 putative ICEs** from 2405 human microbiome samples. (wang2024iceberg3.0functional pages 1-2)
- **Genome-scale ICE/IME discovery in microbiomes:** A study of oral streptococci analyzed **551 genomes** and identified **486 cciMGEs** (173 ICEs, 233 IMEs), using tools such as ICEfinder and CONJscan; it also provided evidence that predicted elements can excise/circularize (a prerequisite for transfer). (lee2024genomicanalysisof pages 1-2)
- **Plasmid mobility inference (pOriT networks):** large-scale oriT screening provides an approach to infer transfer mechanisms for plasmids that lack obvious conjugation genes and helps interpret AMR dissemination potential. (aresarroyo2023originsoftransfer pages 1-2)
- **Short-read MGE insertion mapping:** MGEfinder was described as identifying integrative MGEs and insertion sites from short reads without requiring full assembly, enabling monitoring of insertion hotspots relevant to resistance and adaptation. (fahy2024fromspeciesto pages 4-5)

**6.2 Public-health surveillance and epidemiology.**

- In ESKAPE pathogens, AMR genes are **~5× more likely** to be found on MGEs than in masked genomes (gene-count normalized), and anti-CRISPR proteins are **~15× more abundant** on MGEs, supporting prioritization of mobilome-aware surveillance. (botelho2023theeskapemobilome pages 13-15)
- Studies emphasize that pangenome/mobilome-aware approaches can add biological context to genomic surveillance because gain/loss of MGEs drives non-random pangenome structure and affects AMR dynamics. (fahy2024fromspeciesto pages 4-5)

### 7) Statistics and data highlights (recent)

- **ciMGE prevalence:** 36.5% of bacterial genomes (8000/21,897) carry ≥1 ciMGE in a >20k-genome screen. (botelho2023defensesystemsare pages 2-3)
- **ciMGE counts:** 13,274 ciMGEs discovered across 34 phyla; IMEs outnumber ICEs, but ICEs are larger (mean ~109 kb vs ~27 kb IMEs). (botelho2023defensesystemsare pages 2-3)
- **Integron prevalence:** ~15% of sequenced bacterial genomes carry integrons (review). (ali2024integronsinthe pages 9-10)
- **ICEberg 3.0:** 2065 ICEs, 607 IMEs, 275 CIMEs; 430 experimentally supported entries. (wang2024iceberg3.0functional pages 1-2)
- **Oral streptococci cciMGEs:** 486 cciMGEs found in 551 genomes. (lee2024genomicanalysisof pages 1-2)
- **Genomic island cargo:** ~30% of ICEs carry ≥1 antibiotic resistance determinant; RM systems comprise 40.9% of annotated GI anti-phage defenses. (audrey2023asystematicapproach pages 6-8)
- **ESKAPE enrichment:** AMR genes ~5× and anti-CRISPRs ~15× enriched on MGEs vs masked genomes. (botelho2023theeskapemobilome pages 13-15)

### 8) Expert synthesis (authoritative opinions/analysis)

Recent authoritative reviews emphasize MGEs as a **hierarchical, modular “mobilome”** with emergent properties (flexibility/robustness/genetic capacitance) that complicate tracking but also explain rapid trait innovation in microbes. (weisberg2023mobilegeneticelement pages 1-2, weisberg2023mobilegeneticelement pages 2-4)

Mechanistically, current consensus frameworks treat MGE-mediated HGT as the superposition of: (i) **DNA processing and transfer machineries** (relaxase–oriT–T4SS for conjugation; phage packaging for transduction), (ii) **site-specific recombination systems** (integrases; integron IntI), and (iii) **selection regimes** (antibiotic pressure, phage predation) shaping MGE cargo. (lee2024genomicanalysisof pages 1-2, audrey2023asystematicapproach pages 6-8, botelho2023defensesystemsare pages 1-2)

### 9) Warnings / curation cautions (claims not yet ready to curate as strong edges)

1. **Taxon-specific conflict edges:** “MGE presence → reduced transformation” is supported in specific taxa (Legionella, Acinetobacter) with different implicated MGE classes; it should be curated with taxon constraints or flagged uncertain if used generically. (mazzamurro2024intragenomicconflictswith pages 10-12)
2. **Integron removal in WWTPs:** claims such as “90% of integrons removed” coexist with statements that normalized copy numbers remain unchanged; these should be represented as context-dependent and assay-dependent. (ali2024integronsinthe pages 9-10)
3. **IS-mediated AMR mobilization:** while widely accepted, some statements are review-level and should be curated with careful wording (“can mobilize,” not “always mobilizes”), unless linked to specific IS/Tn cases. (fahy2024fromspeciesto pages 4-5)
4. **Tool-derived mobility predictions:** bioinformatic classification (ICE/IME/GI mobility signatures) should be separated from experimentally demonstrated transfer; ICEberg distinguishes experimentally supported entries and could be used to strengthen curation. (wang2024iceberg3.0functional pages 1-2)

### 10) DOI-first bibliography (with URLs and publication dates)

| Topic area | Full citation | Publication date | DOI | URL |
|---|---|---|---|---|
| MGE evolution principles | Weisberg AJ, Chang JH. *Mobile Genetic Element Flexibility as an Underlying Principle to Bacterial Evolution*. Annual Review of Microbiology 77:603-624. (weisberg2023mobilegeneticelement pages 1-2, weisberg2023mobilegeneticelement pages 2-4) | Sep 2023 | 10.1146/annurev-micro-032521-022006 | https://doi.org/10.1146/annurev-micro-032521-022006 |
| Mobilome/ciMGE catalog | Botelho J. *Defense systems are pervasive across chromosomally integrated mobile genetic elements and are inversely correlated to virulence and antimicrobial resistance*. Nucleic Acids Research 51:4385-4397. (botelho2023defensesystemsare pages 1-2) | Mar 2023 | 10.1093/nar/gkad282 | https://doi.org/10.1093/nar/gkad282 |
| Mobilome/ciMGE catalog | Botelho J, Cazares A, Schulenburg H. *The ESKAPE mobilome contributes to the spread of antimicrobial resistance and CRISPR-mediated conflict between mobile genetic elements*. Nucleic Acids Research 51:236-252. (botelho2023theeskapemobilome pages 13-15, botelho2023theeskapemobilome pages 1-2) | Jan 2023 | 10.1093/nar/gkac1220 | https://doi.org/10.1093/nar/gkac1220 |
| ICE/IME | Daveri A, Benigno V, van der Meer JR. *Characterization of an atypical but widespread type IV secretion system for transfer of the integrative and conjugative element (ICEclc) in Pseudomonas putida*. Nucleic Acids Research 51:2345-2362. (daveri2023characterizationofan pages 1-2, daveri2023characterizationofan media 9a925cd0) | Feb 2023 | 10.1093/nar/gkad024 | https://doi.org/10.1093/nar/gkad024 |
| Genomic islands | Bioteau A, Cellier N, White F, Jacques P-É, Burrus V. *A systematic approach to classify and characterize genomic islands driven by conjugative mobility using protein signatures*. Nucleic Acids Research 51:8402-8412. (audrey2023asystematicapproach pages 6-8, audrey2023asystematicapproach pages 1-2) | Aug 2023 | 10.1093/nar/gkad644 | https://doi.org/10.1093/nar/gkad644 |
| Plasmid mobility | Ares-Arroyo M, Coluzzi C, Rocha EPC. *Origins of transfer establish networks of functional dependencies for plasmid transfer by conjugation*. Nucleic Acids Research 51:3001-3016. (aresarroyo2023originsoftransfer pages 1-2) | Nov 2023 | 10.1093/nar/gkac1079 | https://doi.org/10.1093/nar/gkac1079 |
| ICE/IME | Lee E, Priutt E, Woods S, Quick A, King S, McLellan LK, Shields RC. *Genomic analysis of conjugative and chromosomally integrated mobile genetic elements in oral streptococci*. Applied and Environmental Microbiology 90(10). (lee2024genomicanalysisof pages 1-2) | Oct 2024 | 10.1128/AEM.01360-24 | https://doi.org/10.1128/AEM.01360-24 |
| MGE surveillance/tools | Wang M, Liu G, Liu M, Tai C, Deng Z, Song J, Ou H-Y. *ICEberg 3.0: functional categorization and analysis of the integrative and conjugative elements in bacteria*. Nucleic Acids Research 52:D732-D737. (wang2024iceberg3.0functional pages 1-2) | Oct 2024 | 10.1093/nar/gkad935 | https://doi.org/10.1093/nar/gkad935 |
| MGE surveillance/tools | Tokuda M, Shintani M. *Microbial evolution through horizontal gene transfer by mobile genetic elements*. Microbial Biotechnology 17(1). (tokuda2024microbialevolutionthrough pages 3-4, tokuda2024microbialevolutionthrough pages 1-3) | Jan 2024 | 10.1111/1751-7915.14408 | https://doi.org/10.1111/1751-7915.14408 |
| MGE surveillance/tools | Fahy S, O’Connor JA, Sleator RD, Lucey B. *From Species to Genes: A New Diagnostic Paradigm*. Antibiotics 13:661. (fahy2024fromspeciesto pages 4-5, fahy2024fromspeciesto pages 2-4) | Jul 2024 | 10.3390/antibiotics13070661 | https://doi.org/10.3390/antibiotics13070661 |
| Integrons | Ali N, Ali I, Din AU, Akhtar K, He B, Wen R. *Integrons in the Age of Antibiotic Resistance: Evolution, Mechanisms, and Environmental Implications: A Review*. Microorganisms 12:2579. (ali2024integronsinthe pages 9-10) | Dec 2024 | 10.3390/microorganisms12122579 | https://doi.org/10.3390/microorganisms12122579 |
| Mobilome/ciMGE catalog | Mazzamurro F, Chirakadavil JB, Durieux I, Poiré L, Plantade J, Ginevra C, Jarraud S, Wilharm G, Charpentier X, Rocha EPC. *Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species*. PLOS Biology 22:e3002814. (mazzamurro2024intragenomicconflictswith pages 10-12) | Oct 2024 | 10.1371/journal.pbio.3002814 | https://doi.org/10.1371/journal.pbio.3002814 |
| Prophage/transduction | Wolput S, Lood C, Fillol-Salom A, Casters Y, Albasiony A, Cenens W, Vanoirbeek K, Kerremans A, Lavigne R, Penadés JR, Aertsen A. *Phage-host co-evolution has led to distinct generalized transduction strategies*. Nucleic Acids Research 52:7780-7791. (botelho2023defensesystemsare pages 2-3) | Jun 2024 | 10.1093/nar/gkae489 | https://doi.org/10.1093/nar/gkae489 |


*Table: This table compiles the core recent sources used for the mobile genetic element report, organized by topic area and formatted for quick DOI-first lookup. It is useful for curation, verification, and building the final bibliography section.*

### 11) Visual evidence (mechanism schematic)

A curated schematic of ICEclc showing **excision/circularization (attL/attR/attP), integrase (int), relaxase (traI), and T4SS components including VirB4/VirD4 homologs** was retrieved and can be used as a mechanistic anchor for the ICE subgraph. (daveri2023characterizationofan media 9a925cd0)


References

1. (weisberg2023mobilegeneticelement pages 1-2): Alexandra J. Weisberg and Jeff H. Chang. Mobile genetic element flexibility as an underlying principle to bacterial evolution. Annual Review of Microbiology, 77:603-624, Sep 2023. URL: https://doi.org/10.1146/annurev-micro-032521-022006, doi:10.1146/annurev-micro-032521-022006. This article has 95 citations and is from a peer-reviewed journal.

2. (tokuda2024microbialevolutionthrough pages 1-3): Maho Tokuda and Masaki Shintani. Microbial evolution through horizontal gene transfer by mobile genetic elements. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14408, doi:10.1111/1751-7915.14408. This article has 242 citations and is from a peer-reviewed journal.

3. (tokuda2024microbialevolutionthrough pages 3-4): Maho Tokuda and Masaki Shintani. Microbial evolution through horizontal gene transfer by mobile genetic elements. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14408, doi:10.1111/1751-7915.14408. This article has 242 citations and is from a peer-reviewed journal.

4. (botelho2023defensesystemsare pages 1-2): João Botelho. Defense systems are pervasive across chromosomally integrated mobile genetic elements and are inversely correlated to virulence and antimicrobial resistance. Nucleic Acids Research, 51:4385-4397, Mar 2023. URL: https://doi.org/10.1093/nar/gkad282, doi:10.1093/nar/gkad282. This article has 59 citations and is from a highest quality peer-reviewed journal.

5. (fahy2024fromspeciesto pages 4-5): Sinead Fahy, James A. O’Connor, Roy D. Sleator, and Brigid Lucey. From species to genes: a new diagnostic paradigm. Antibiotics, 13:661, Jul 2024. URL: https://doi.org/10.3390/antibiotics13070661, doi:10.3390/antibiotics13070661. This article has 4 citations.

6. (lee2024genomicanalysisof pages 1-2): Erica Lee, Erin Priutt, Seth Woods, Allison Quick, Shawn King, Lisa K. McLellan, and Robert C. Shields. Genomic analysis of conjugative and chromosomally integrated mobile genetic elements in oral streptococci. Applied and Environmental Microbiology, Oct 2024. URL: https://doi.org/10.1128/aem.01360-24, doi:10.1128/aem.01360-24. This article has 6 citations and is from a peer-reviewed journal.

7. (wang2024iceberg3.0functional pages 1-2): Meng Wang, Guitian Liu, Meng Liu, Cui Tai, Zixin Deng, Jiangning Song, and Hong-Yu Ou. Iceberg 3.0: functional categorization and analysis of the integrative and conjugative elements in bacteria. Nucleic Acids Research, 52:D732-D737, Oct 2024. URL: https://doi.org/10.1093/nar/gkad935, doi:10.1093/nar/gkad935. This article has 101 citations and is from a highest quality peer-reviewed journal.

8. (weisberg2023mobilegeneticelement pages 2-4): Alexandra J. Weisberg and Jeff H. Chang. Mobile genetic element flexibility as an underlying principle to bacterial evolution. Annual Review of Microbiology, 77:603-624, Sep 2023. URL: https://doi.org/10.1146/annurev-micro-032521-022006, doi:10.1146/annurev-micro-032521-022006. This article has 95 citations and is from a peer-reviewed journal.

9. (daveri2023characterizationofan media 9a925cd0): Andrea Daveri, Valentina Benigno, and Jan Roelof van der Meer. Characterization of an atypical but widespread type iv secretion system for transfer of the integrative and conjugative element (iceclc) in pseudomonas putida. Nucleic Acids Research, 51:2345-2362, Feb 2023. URL: https://doi.org/10.1093/nar/gkad024, doi:10.1093/nar/gkad024. This article has 16 citations and is from a highest quality peer-reviewed journal.

10. (aresarroyo2023originsoftransfer pages 1-2): Manuel Ares-Arroyo, Charles Coluzzi, and Eduardo P C Rocha. Origins of transfer establish networks of functional dependencies for plasmid transfer by conjugation. Nucleic Acids Research, 51:3001-3016, Nov 2023. URL: https://doi.org/10.1093/nar/gkac1079, doi:10.1093/nar/gkac1079. This article has 83 citations and is from a highest quality peer-reviewed journal.

11. (botelho2023defensesystemsare pages 2-3): João Botelho. Defense systems are pervasive across chromosomally integrated mobile genetic elements and are inversely correlated to virulence and antimicrobial resistance. Nucleic Acids Research, 51:4385-4397, Mar 2023. URL: https://doi.org/10.1093/nar/gkad282, doi:10.1093/nar/gkad282. This article has 59 citations and is from a highest quality peer-reviewed journal.

12. (tokuda2024microbialevolutionthrough pages 4-5): Maho Tokuda and Masaki Shintani. Microbial evolution through horizontal gene transfer by mobile genetic elements. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14408, doi:10.1111/1751-7915.14408. This article has 242 citations and is from a peer-reviewed journal.

13. (audrey2023asystematicapproach pages 1-2): Bioteau Audrey, Nicolas Cellier, Frédérique White, Pierre-Étienne Jacques, and Vincent Burrus. A systematic approach to classify and characterize genomic islands driven by conjugative mobility using protein signatures. Nucleic Acids Research, 51:8402-8412, Aug 2023. URL: https://doi.org/10.1093/nar/gkad644, doi:10.1093/nar/gkad644. This article has 26 citations and is from a highest quality peer-reviewed journal.

14. (audrey2023asystematicapproach pages 6-8): Bioteau Audrey, Nicolas Cellier, Frédérique White, Pierre-Étienne Jacques, and Vincent Burrus. A systematic approach to classify and characterize genomic islands driven by conjugative mobility using protein signatures. Nucleic Acids Research, 51:8402-8412, Aug 2023. URL: https://doi.org/10.1093/nar/gkad644, doi:10.1093/nar/gkad644. This article has 26 citations and is from a highest quality peer-reviewed journal.

15. (daveri2023characterizationofan pages 1-2): Andrea Daveri, Valentina Benigno, and Jan Roelof van der Meer. Characterization of an atypical but widespread type iv secretion system for transfer of the integrative and conjugative element (iceclc) in pseudomonas putida. Nucleic Acids Research, 51:2345-2362, Feb 2023. URL: https://doi.org/10.1093/nar/gkad024, doi:10.1093/nar/gkad024. This article has 16 citations and is from a highest quality peer-reviewed journal.

16. (mazzamurro2024intragenomicconflictswith pages 10-12): Fanny Mazzamurro, Jason Baby Chirakadavil, Isabelle Durieux, Ludovic Poiré, Julie Plantade, Christophe Ginevra, Sophie Jarraud, Gottfried Wilharm, Xavier Charpentier, and Eduardo P. C. Rocha. Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species. PLOS Biology, 22:e3002814, Oct 2024. URL: https://doi.org/10.1371/journal.pbio.3002814, doi:10.1371/journal.pbio.3002814. This article has 21 citations and is from a highest quality peer-reviewed journal.

17. (botelho2023theeskapemobilome pages 13-15): João Botelho, Adrian Cazares, and Hinrich Schulenburg. The eskape mobilome contributes to the spread of antimicrobial resistance and crispr-mediated conflict between mobile genetic elements. Nucleic Acids Research, 51:236-252, Jan 2023. URL: https://doi.org/10.1093/nar/gkac1220, doi:10.1093/nar/gkac1220. This article has 64 citations and is from a highest quality peer-reviewed journal.

18. (fahy2024fromspeciesto pages 2-4): Sinead Fahy, James A. O’Connor, Roy D. Sleator, and Brigid Lucey. From species to genes: a new diagnostic paradigm. Antibiotics, 13:661, Jul 2024. URL: https://doi.org/10.3390/antibiotics13070661, doi:10.3390/antibiotics13070661. This article has 4 citations.

19. (ali2024integronsinthe pages 9-10): Niyaz Ali, Izhar Ali, Ahmad Ud Din, Kashif Akhtar, Bing He, and Ronghui Wen. Integrons in the age of antibiotic resistance: evolution, mechanisms, and environmental implications: a review. Microorganisms, 12:2579, Dec 2024. URL: https://doi.org/10.3390/microorganisms12122579, doi:10.3390/microorganisms12122579. This article has 38 citations.

20. (botelho2023theeskapemobilome pages 1-2): João Botelho, Adrian Cazares, and Hinrich Schulenburg. The eskape mobilome contributes to the spread of antimicrobial resistance and crispr-mediated conflict between mobile genetic elements. Nucleic Acids Research, 51:236-252, Jan 2023. URL: https://doi.org/10.1093/nar/gkac1220, doi:10.1093/nar/gkac1220. This article has 64 citations and is from a highest quality peer-reviewed journal.