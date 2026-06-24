---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:24:51.123431'
end_time: '2026-06-17T21:46:23.952523'
duration_seconds: 1292.83
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cobalt tolerant
  trait_identifier: traitmech:000015
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: cobalt_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metal tolerance in which an organism grows in the presence of elevated
    cobalt (Co2+) concentrations, typically via cation-efflux resistance systems such
    as the czc and cnr determinants.
  parent_traits: traitmech:000012
  synonyms: ''
  evidence_summary: 'DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition
    metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system
    of Cupriavidus metallidurans confers cobalt resistance.) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cobalt
    to a MIC of 20 mM.)'
  causal_graph_summary: 'cobalt_tolerance_czc_cnr_efflux: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cobalt tolerant
- **METPO identifier:** traitmech:000015
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cobalt (Co2+) concentrations, typically via cation-efflux resistance systems such as the czc and cnr determinants.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cobalt resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cobalt to a MIC of 20 mM.)
- **Existing causal graph summary:** cobalt_tolerance_czc_cnr_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cobalt tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cobalt_tolerant.yaml`.

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
- **Trait label:** cobalt tolerant
- **METPO identifier:** traitmech:000015
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated cobalt (Co2+) concentrations, typically via cation-efflux resistance systems such as the czc and cnr determinants.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers cobalt resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates cobalt to a MIC of 20 mM.)
- **Existing causal graph summary:** cobalt_tolerance_czc_cnr_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cobalt tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/cobalt_tolerant.yaml`.

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


## Microbial TraitMech Curation Report: **cobalt tolerant** (METPO:traitmech:000015)

### 1) Scope summary (trait definition, boundaries, and assays)

**Trait meaning (operational phenotype).** *Cobalt tolerant* is best treated as an **assay-observed growth phenotype**: the organism can grow/survive under elevated extracellular Co(II) (often as CoCl2), typically quantified as a tolerated concentration or MIC-like threshold. A clear primary example is *E. coli* where “growth arrest occurred at … 30 µM CoCl2” in an rcnA mutant vs “50 µM CoCl2” in wild type, and multicopy expression can increase resistance dramatically (rodrigue2005identificationofrcna pages 1-2).

**Mechanistic interpretation.** Across Gram-negative bacteria, the trait is most consistently tied to **active export/efflux** of Co2+ (often together with Zn2+/Cd2+ and/or Ni2+), especially via **tripartite HME-RND systems** and **CDF/MFS exporters** (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 9-11).

**Boundary cases / nearby traits.**
- **Cobalt homeostasis vs. cobalt tolerance:** homeostasis includes trace-level cobalt acquisition/handling for metalloproteins; tolerance is survival under excess cobalt stress. Recent work highlights that efflux systems can serve homeostatic roles even without added metals (e.g., CzcCBA present without added metals) and can be induced under metal-starvation contexts, complicating a strict “resistance-only” framing (galea2024linkingthetranscriptome pages 9-10).
- **General heavy-metal resistance vs cobalt-specific tolerance:** many systems are multi-metal (CzcCBA exports Cd2+/Zn2+/Co2+), so cobalt specificity may be inferred by **(i)** explicit Co2+ substrate preference (DmeF), **(ii)** Co2+-induced gene expression (rcnA), and/or **(iii)** plasmid determinants whose phenotypes are reported with cobalt concentrations (cnr/czc/ncc) (siunova2025potentialofnickel pages 5-7, rodrigue2005identificationofrcna pages 1-2).
- **Uptake vs efflux:** uptake systems (e.g., low-specificity cation importers) are important background physiology but are not themselves sufficient to define cobalt tolerance; in curation, they are best kept as contextual nodes unless directly shown to drive tolerance phenotypes in cobalt (siunova2025potentialofnickel pages 1-3).

### 2) Key concepts and mechanistic entities (current understanding)

Core conceptual layers consistent with current reviews and recent primary work:

1. **Transenvelope HME-RND efflux (dominant high-level tolerance in many Gram-negatives):** tripartite exporter spanning inner membrane–periplasm–outer membrane, typically operating via chemiosmotic potential and often functioning after an initial cytoplasm→periplasm transfer step (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 9-11).
2. **CDF-family exporters:** single inner-membrane metal exporters (e.g., CzcD, DmeF, FieF). DmeF is highlighted as cobalt-preferred (siunova2025potentialofnickel pages 5-7).
3. **MFS-family Ni/Co exporters (lower-level tolerance):** e.g., NreB-like proteins; importantly, induction can be metal-specific (nreB induced by Ni but not Co) (siunova2025potentialofnickel pages 5-7).
4. **Regulatory control:** two-component systems and metal sensors tune expression to avoid unnecessary loss of essential ions; for czc, regulation by CzcS/CzcR and associated cross-talk systems is now characterized in detail (olenska2025bacteriaundermetal pages 9-11, grosse2023interplaybetweentwocomponent pages 1-3).

### 3) Candidate nodes for TraitMech causal graph (grouped by type)

A curation-oriented node inventory with grounding suggestions is provided in the embedded artifact.

| Node label | Node type | Suggested grounding | Brief definition/role | Key supporting citation context IDs |
|---|---|---|---|---|
| cobalt tolerant | Trait | METPO:traitmech:000015 | Growth/survival phenotype in elevated Co(II), typically operationalized by growth in Co-supplemented medium or strain-specific resistance thresholds. | (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 9-11) |
| Co(II) resistance / cobalt tolerance | Trait | label-only candidate | Closely related phenotype label used in primary/review literature for resistance to excess cobalt ions; useful synonym-like graph node if needed. | (siunova2025potentialofnickel pages 5-7, rodrigue2005identificationofrcna pages 1-2) |
| cobalt(2+) | Chemicals | CHEBI:48828 | Core toxic/essential transition-metal cation whose excess drives the trait; substrate of multiple efflux systems. | (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 9-11) |
| nickel(2+) | Chemicals | CHEBI:28112 | Frequently co-handled with cobalt by cnr, ncc, rcnA, DmeF/FieF-related systems; nearby but distinct trait context. | (siunova2025potentialofnickel pages 5-7, rodrigue2005identificationofrcna pages 1-2) |
| zinc(2+) | Chemicals | CHEBI:29105 | Common co-substrate with cobalt in czc/CzcD-linked systems; important boundary metal for distinguishing broad vs cobalt-focused tolerance. | (olenska2025bacteriaundermetal pages 9-11, houdt2021adaptationofcupriavidus pages 1-2) |
| cadmium(2+) | Chemicals | CHEBI:22977 | Common co-substrate in czc/ncc/CzcD systems; helps define multi-metal rather than cobalt-exclusive determinants. | (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 9-11) |
| cobalt(II) chloride | Chemicals | CHEBI:53300 | Common assay chemical for measuring cobalt sensitivity/resistance in growth assays. | (rodrigue2005identificationofrcna pages 1-2) |
| nickel(II) chloride | Chemicals | CHEBI:53301 | Common paired assay chemical used alongside cobalt chloride in resistance tests. | (rodrigue2005identificationofrcna pages 1-2) |
| EDTA | Environmental/assay factors | CHEBI:42191 | Metal chelator used to create metal-starvation conditions and reveal homeostasis/efflux responses such as ZniCBA upregulation. | (galea2024linkingthetranscriptome pages 9-10, grosse2024antisensetranscriptionis pages 2-2) |
| elevated cobalt exposure | Environmental/assay factors | label-only candidate | Experimental or environmental condition of excess Co(II) that selects for the trait. | (siunova2025potentialofnickel pages 5-7, rodrigue2005identificationofrcna pages 1-2) |
| metal-starvation conditions | Environmental/assay factors | label-only candidate | Assay state that reveals homeostatic and compensatory metal transport functions related to cobalt/zinc balance. | (galea2024linkingthetranscriptome pages 9-10, grosse2024antisensetranscriptionis pages 2-2) |
| biofilm | Environmental/assay factors | GO:0042710 | Microbial growth mode emphasized in recent co-selection literature as a hotspot for gene exchange and pollutant interaction. | (balta2025theinterplaybetween pages 15-15) |
| microplastics | Environmental/assay factors | ENVO:01000814 | Environmental matrix proposed to concentrate heavy metals and resistant bacteria, enhancing co-selection and transfer contexts. | (balta2025theinterplaybetween pages 15-15) |
| heavy-metal-contaminated environment | Environmental/assay factors | ENVO:00002297 | Natural/industrial setting selecting for cobalt-tolerant organisms and mobile resistance determinants. | (grosse2023interplaybetweentwocomponent pages 1-3, houdt2021adaptationofcupriavidus pages 1-2) |
| active metal efflux | Pathways/processes | GO:0043215 | Central mechanism of cobalt tolerance; lowers intracellular/periplasmic toxic metal burden. | (olenska2025bacteriaundermetal pages 9-11, siunova2025potentialofnickel pages 5-7) |
| cobalt ion transmembrane export | Pathways/processes | GO:0030002 | Specific transport process underlying cobalt tolerance determinants such as CzcCBA, DmeF, and RcnA-like exporters. | (siunova2025potentialofnickel pages 5-7, rodrigue2005identificationofrcna pages 1-2) |
| HME-RND efflux | Pathways/processes | label-only candidate | Two-step, transenvelope heavy-metal export process in Gram-negatives; major high-level cobalt tolerance route. | (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 9-11) |
| CDF-family metal export | Pathways/processes | label-only candidate | Cation diffusion facilitator-mediated efflux, often contributing to Co/Zn/Ni/Cd homeostasis and tolerance. | (siunova2025potentialofnickel pages 5-7) |
| MFS-mediated metal export | Pathways/processes | label-only candidate | Major facilitator superfamily route for lower-level Ni/Co export in NreB/CnrT/NcrA-like systems. | (siunova2025potentialofnickel pages 5-7) |
| periplasmic metal sensing | Pathways/processes | GO:0007165 | Upstream sensory process for two-component regulators such as CzcS/CzcR that control efflux gene expression. | (olenska2025bacteriaundermetal pages 9-11, grosse2023interplaybetweentwocomponent pages 1-3) |
| horizontal gene transfer | Pathways/processes | GO:0018995 | Major evolutionary mechanism spreading cobalt/heavy-metal resistance determinants and co-selection modules. | (grosse2023interplaybetweentwocomponent pages 1-3, gillieatt2024unravellingthemechanisms pages 14-15) |
| co-selection with antibiotic resistance | Pathways/processes | label-only candidate | Recent ecological framework linking heavy-metal resistance loci with antibiotic resistance maintenance and spread. | (balta2025theinterplaybetween pages 7-7, gillieatt2024unravellingthemechanisms pages 14-15) |
| czcCBA | Genes/proteins/complexes | label-only candidate | Tripartite RND/MFP/OMF transenvelope efflux complex exporting Co2+/Zn2+/Cd2+; core high-level cobalt-tolerance node. | (olenska2025bacteriaundermetal pages 9-11, galea2024linkingthetranscriptome pages 9-10) |
| czcA | Genes/proteins/complexes | label-only candidate | Inner membrane RND transporter component of CzcCBA. | (olenska2025bacteriaundermetal pages 9-11, houdt2021adaptationofcupriavidus pages 1-2) |
| czcB | Genes/proteins/complexes | label-only candidate | Membrane fusion/adaptor component of CzcCBA. | (olenska2025bacteriaundermetal pages 9-11, galea2024linkingthetranscriptome pages 9-10) |
| czcC | Genes/proteins/complexes | label-only candidate | Outer membrane factor component of CzcCBA. | (olenska2025bacteriaundermetal pages 9-11, galea2024linkingthetranscriptome pages 9-10) |
| czcD | Genes/proteins/complexes | label-only candidate | CDF-family transporter with broad specificity including cobalt in some taxa; may support resistance/homeostasis. | (siunova2025potentialofnickel pages 5-7, houdt2021adaptationofcupriavidus pages 1-2) |
| czcP | Genes/proteins/complexes | label-only candidate | PIB4-type ATPase in the czc region; strong evidence for Zn export/resistance enhancement, cobalt relevance plausible but weaker in provided evidence. | (houdt2021adaptationofcupriavidus pages 1-2) |
| czcN | Genes/proteins/complexes | label-only candidate | Accessory czc-region gene upstream of core efflux genes and under CzcR-linked control. | (grosse2023interplaybetweentwocomponent pages 1-3) |
| czcI | Genes/proteins/complexes | label-only candidate | Accessory czc-region gene/periplasm-related control component implicated in Czc activity modulation. | (olenska2025bacteriaundermetal pages 9-11, galea2024linkingthetranscriptome pages 9-10) |
| czcE | Genes/proteins/complexes | label-only candidate | Periplasmic protein in czc locus, independently transcribed in response to Zn and involved in promoter control. | (olenska2025bacteriaundermetal pages 9-11) |
| cnrCBA | Genes/proteins/complexes | label-only candidate | Tripartite cobalt/nickel resistance efflux complex on pMOL28. | (siunova2025potentialofnickel pages 5-7, galea2024linkingthetranscriptome pages 9-10) |
| cnrCBAYXHT operon | Genes/proteins/complexes | label-only candidate | Full cobalt/nickel resistance determinant conferring 5 mM Co resistance in C. metallidurans CH34. | (siunova2025potentialofnickel pages 5-7) |
| cnrA | Genes/proteins/complexes | label-only candidate | RND transporter component of CnrCBA. | (siunova2025potentialofnickel pages 5-7) |
| cnrB | Genes/proteins/complexes | label-only candidate | Membrane fusion component of CnrCBA; detected in recent CH34 proteomics. | (galea2024linkingthetranscriptome pages 9-10) |
| cnrC | Genes/proteins/complexes | label-only candidate | Outer membrane factor component of CnrCBA. | (siunova2025potentialofnickel pages 5-7, galea2024linkingthetranscriptome pages 9-10) |
| cnrT | Genes/proteins/complexes | label-only candidate | Low-level Ni resistance MFS-associated protein in C. metallidurans CH34; nearby/related cobalt graph node with weaker Co specificity. | (siunova2025potentialofnickel pages 5-7) |
| nccCBA | Genes/proteins/complexes | label-only candidate | Tripartite Ni/Co/Cd resistance efflux complex in strain 31A. | (siunova2025potentialofnickel pages 5-7, grosse2024antisensetranscriptionis pages 2-2) |
| nccCBAYXN operon | Genes/proteins/complexes | label-only candidate | Full determinant mediating high Co resistance (20 mM) in strain 31A. | (siunova2025potentialofnickel pages 5-7) |
| DmeF | Genes/proteins/complexes | label-only candidate | CDF-family exporter whose preferred substrate is Co2+; strong candidate core cobalt-specific node. | (siunova2025potentialofnickel pages 5-7, siunova2025potentialofnickel pages 3-5) |
| FieF | Genes/proteins/complexes | label-only candidate | Exporter involved in Fe2+ excretion and homeostasis of Co2+, Ni2+, and lesser Cd2+. | (siunova2025potentialofnickel pages 5-7, siunova2025potentialofnickel pages 3-5) |
| RcnA / YohM | Genes/proteins/complexes | label-only candidate | E. coli membrane efflux protein conferring resistance to cobalt and nickel; foundational single-protein cobalt exporter. | (rodrigue2005identificationofrcna pages 1-2, siunova2025potentialofnickel pages 5-7) |
| NreB | Genes/proteins/complexes | label-only candidate | MFS-family transporter conferring strong Ni resistance and sometimes increased Co resistance; Ni-induced rather than Co-induced. | (siunova2025potentialofnickel pages 5-7) |
| NcrA | Genes/proteins/complexes | label-only candidate | NreB orthologue in Serratia marcescens providing both Ni2+ and Co2+ resistance. | (siunova2025potentialofnickel pages 5-7) |
| ZniCBA | Genes/proteins/complexes | label-only candidate | Chromid-encoded transenvelope exporter upregulated under EDTA/metal starvation; likely homeostasis rather than primary cobalt resistance. | (galea2024linkingthetranscriptome pages 9-10) |
| CDF family | Genes/proteins/complexes | label-only candidate | Transporter family including CzcD, DmeF, and FieF, often moving Co/Zn/Ni/Cd/Fe. | (siunova2025potentialofnickel pages 5-7) |
| MFS family | Genes/proteins/complexes | label-only candidate | Transporter family including NreB/CnrT/NcrA-like low-level Ni/Co resistance proteins. | (siunova2025potentialofnickel pages 5-7) |
| HME-RND pump | Genes/proteins/complexes | label-only candidate | Tripartite Gram-negative heavy-metal exporter spanning inner membrane, periplasm, and outer membrane. | (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 9-11) |
| CzcR | Regulators | label-only candidate | Response regulator activating czc promoters and integrating multiple two-component inputs. | (olenska2025bacteriaundermetal pages 9-11, grosse2023interplaybetweentwocomponent pages 1-3) |
| CzcS | Regulators | label-only candidate | Membrane histidine kinase sensing periplasmic metal signals and activating CzcR. | (olenska2025bacteriaundermetal pages 9-11, grosse2023interplaybetweentwocomponent pages 1-3) |
| czcRS | Regulators | label-only candidate | Canonical two-component regulatory system controlling czc locus expression. | (olenska2025bacteriaundermetal pages 9-11, grosse2023interplaybetweentwocomponent pages 1-3) |
| CzcR2S2 | Regulators | label-only candidate | Closely related two-component system that cross-talks with CzcRS to shape czc expression. | (grosse2023interplaybetweentwocomponent pages 1-3) |
| AgrRS | Regulators | label-only candidate | Additional two-component system interacting with CzcRS/CzcR2S2 in control of czc-associated promoters. | (grosse2023interplaybetweentwocomponent pages 1-3) |
| RcnR | Regulators | label-only candidate | Ni/Co-responsive regulator controlling rcnA-family efflux expression. | (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 14-15) |
| CsoR/RcnR family | Regulators | label-only candidate | Metal-releasable derepressor family highlighted as useful for sensing/engineering metal-responsive circuits including Co/Ni systems. | (olenska2025bacteriaundermetal pages 14-15, bai2023shootrootsignalcircuit pages 2-4) |
| CoaR | Regulators | label-only candidate | Cobalt-sensing transcription factor family member highlighted for biosensor design. | (olenska2025bacteriaundermetal pages 14-15) |
| mex operon | Regulators | label-only candidate | Antibiotic efflux operon reportedly co-induced by CzcS-CzcR activation in co-selection literature; context node for cross-resistance. | (balta2025theinterplaybetween pages 7-7) |
| pMOL28 | Mobile genetic elements/contexts | label-only candidate | Large plasmid carrying the cnr cobalt/nickel resistance determinant in C. metallidurans CH34. | (siunova2025potentialofnickel pages 5-7, galea2024linkingthetranscriptome pages 9-10) |
| pMOL30 | Mobile genetic elements/contexts | label-only candidate | Large plasmid carrying the czc cobalt/zinc/cadmium resistance determinant in C. metallidurans CH34. | (olenska2025bacteriaundermetal pages 9-11, houdt2021adaptationofcupriavidus pages 1-2) |
| mobile genetic elements | Mobile genetic elements/contexts | GO:0006313 | General context for plasmids/transposons/integron-linked spread of heavy-metal resistance genes. | (balta2025theinterplaybetween pages 7-7, gillieatt2024unravellingthemechanisms pages 9-10) |
| intI1 | Mobile genetic elements/contexts | label-only candidate | Class 1 integron marker correlated with heavy-metal resistance genes including czcA in environmental studies. | (gillieatt2024unravellingthemechanisms pages 14-15, gillieatt2024unravellingthemechanisms pages 9-10) |
| transposase tnpA | Mobile genetic elements/contexts | label-only candidate | Mobile-element marker correlated with heavy-metal resistance genes in co-selection studies. | (gillieatt2024unravellingthemechanisms pages 9-10) |
| Cupriavidus metallidurans CH34 | Taxa/examples | NCBITaxon:266264 | Canonical model for cobalt tolerance determinants czc, cnr, DmeF, FieF and recent proteomic/regulatory studies. | (grosse2023interplaybetweentwocomponent pages 1-3, galea2024linkingthetranscriptome pages 9-10) |
| Escherichia coli | Taxa/examples | NCBITaxon:562 | Foundational model for single-gene cobalt/nickel efflux via RcnA/YohM. | (rodrigue2005identificationofrcna pages 1-2) |
| Achromobacter xylosoxidans 31A | Taxa/examples | label-only candidate | Historical strain carrying ncc determinant with high Co resistance; later reclassified in related literature. | (siunova2025potentialofnickel pages 5-7) |
| Serratia marcescens C-1 | Taxa/examples | NCBITaxon:615 | Example organism with NcrA-mediated Ni/Co resistance. | (siunova2025potentialofnickel pages 5-7) |
| Pseudomonas aeruginosa | Taxa/examples | NCBITaxon:287 | Important co-selection example where CzcS-CzcR links metal and antibiotic resistance regulation. | (balta2025theinterplaybetween pages 7-7) |
| cobalt biosensor | Applications | label-only candidate | Synthetic-biology application using cobalt-responsive transcription factors to detect bioavailable cobalt. | (olenska2025bacteriaundermetal pages 14-15, bai2023shootrootsignalcircuit pages 2-4) |
| bioremediation of cobalt/heavy metals | Applications | GO:1990748 | Environmental use-case for cobalt-tolerant microbes and engineered modules in contaminated soils/waters. | (olenska2025bacteriaundermetal pages 14-15, olaya‐abril2024bacterialtoleranceand pages 13-14) |
| biomining / metal recovery | Applications | label-only candidate | Applied context where heavy-metal-resistant bacteria may aid selective metal recovery. | (olenska2025bacteriaundermetal pages 14-15) |


*Table: This table lists curation-ready candidate nodes for a TraitMech causal graph of microbial cobalt tolerance, organized by node type and grounded where possible. It emphasizes experimentally supported transporters, regulators, assay factors, mobile elements, and application contexts drawn from the provided evidence.*

### 4) Evidence-backed candidate causal edges (triples)

A curation-ready edge table (with verbatim snippets, DOI-first references, publication dates/URLs, and uncertainty flags) is provided in the embedded artifact.

| Subject node (suggested ID) | Predicate (causal) | Object node (suggested ID) | Evidence snippet (verbatim quote) | Reference (DOI, publication date, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| CzcS/CzcR two-component system (label-only; HK/RR) | senses and activates transcription of | czcCBA operon (label-only) | “The czcRS consists of the inner membrane protein CzcS, which detects levels of periplasmic Zn2+ or Cd2+, and activates the response regulator CzcR. Activated CzcR functions as a transcriptional activator of czcCBA expression” | 10.3390/ijms26125716; 2025-06; https://doi.org/10.3390/ijms26125716 | Strong for czc regulation, but sensing evidence is for periplasmic Zn2+/Cd2+, not directly Co2+; useful upstream edge for cobalt-tolerance graph because czcCBA mediates Co export. (olenska2025bacteriaundermetal pages 9-11) |
| CzcCBA efflux system (label-only; HME-RND/CBA complex) | exports | cobalt(2+) / zinc(2+) / cadmium(2+) (CHEBI:48828 / CHEBI:29105 / CHEBI:22977) | “The CzcCBA system is an example of an RND superfamily transporter. As a chemiosmotic divalent cation/proton antiporter, it deals with the efflux of Cd2+, Zn2+, and Co2+.” | 10.3390/ijms26125716; 2025-06; https://doi.org/10.3390/ijms26125716 | Strong mechanistic edge for cobalt export; appropriate core TraitMech edge. (olenska2025bacteriaundermetal pages 9-11) |
| czc determinant / czcCBADRSNI operon (label-only) | confers resistance to | cobalt tolerance (traitmech:000015) | “pMOL30 (250 kb), harbors the czcCBADRSNI operon, which encodes resistance to 20 mM Co, 12 mM Zn, and 2.5 mM Cd” | 10.1007/s44274-025-00301-y; 2025-07; https://doi.org/10.1007/s44274-025-00301-y | Strong quantitative trait edge; concentration is explicit. Assay context is strain-level growth resistance in Cupriavidus metallidurans CH34. (siunova2025potentialofnickel pages 5-7) |
| cnr determinant / cnrCBAYXHT operon (label-only) | confers resistance to | cobalt tolerance (traitmech:000015) | “This strain exhibits resistance to 3 mM Ni and 5 mM Co, conferred by the cnrCBAYXHT operon located on plasmid pMOL28” | 10.1007/s44274-025-00301-y; 2025-07; https://doi.org/10.1007/s44274-025-00301-y | Strong quantitative edge for Co tolerance in C. metallidurans CH34; could also split into cnr operon → cobalt resistance. (siunova2025potentialofnickel pages 5-7) |
| ncc determinant / nccCBAYXN operon (label-only) | confers resistance to | cobalt tolerance (traitmech:000015) | “This strain demonstrates resistance to high concentrations of Ni (40 mM), Co (20 mM), and Cd (1 mM). Resistance to heavy metals in this strain is mediated by the nccCBAYXN operon” | 10.1007/s44274-025-00301-y; 2025-07; https://doi.org/10.1007/s44274-025-00301-y | Strong quantitative edge; taxon-specific to strain 31A/Achromobacter xylosoxidans (later Cupriavidus metallidurans). (siunova2025potentialofnickel pages 5-7) |
| DmeF (CDF-family exporter; label-only) | preferentially exports | cobalt(2+) (CHEBI:48828) | “Co2⁺ is the preferred substrate for the DmeF protein in Cupriavidus metallidurans CH34.” | 10.1007/s44274-025-00301-y; 2025-07; https://doi.org/10.1007/s44274-025-00301-y | Strong for substrate preference; downstream trait linkage to tolerance/homeostasis is inferred from exporter role and repeated review statements, but direct MIC shift from a DmeF mutant is not quoted here. Curate with mild caution. (siunova2025potentialofnickel pages 5-7, siunova2025potentialofnickel pages 3-5) |
| DmeF (CDF-family exporter; label-only) | contributes to | cobalt homeostasis / cobalt tolerance (label-only / traitmech:000015) | “DmeF in C. metallidurans preferentially exports Co2+, FieF exports Fe2+ and contributes to Co2+ and Ni2+ homeostasis” | 10.1007/s44274-025-00301-y; 2025-07; https://doi.org/10.1007/s44274-025-00301-y | Mechanism-to-trait edge supported by review synthesis rather than a directly quoted mutant phenotype in-context; mark as somewhat inferred. (siunova2025potentialofnickel pages 3-5, siunova2025potentialofnickel pages 5-7) |
| rcnA / YohM (label-only) | encodes efflux system for and increases resistance to | cobalt(2+) and nickel(2+) (CHEBI:48828 / CHEBI:28112) | “yohM encodes a membrane-bound polypeptide conferring increased nickel and cobalt resistance in E. coli.” / “Our data support the hypothesis that YohM is the first described efflux system for nickel and cobalt in E. coli.” | 10.1128/JB.187.8.2912-2916.2005; 2005-04; https://doi.org/10.1128/JB.187.8.2912-2916.2005 | Strong primary evidence in E. coli. Gene renamed rcnA. Suitable core edge for single-protein Co/Ni efflux. (rodrigue2005identificationofrcna pages 1-2) |
| rcnA loss-of-function mutant (E. coli yohM::uidA) | decreases tolerance to | cobalt(2+) (CHEBI:48828) | “growth arrest occurred at 4 μM NiCl2 and 30 μM CoCl2 for ARY023 (yohM) compared with 10 μM NiCl2 and 50 μM CoCl2 for MC4100 (wt).” | 10.1128/JB.187.8.2912-2916.2005; 2005-04; https://doi.org/10.1128/JB.187.8.2912-2916.2005 | Strong quantitative phenotype edge from primary study. Directionality here is mutant loss causing lower tolerance; can support inverse edge rcnA → enables cobalt tolerance. (rodrigue2005identificationofrcna pages 1-2) |
| multicopy rcnA / yohM overexpression (label-only) | increases resistance to | cobalt(2+) (CHEBI:48828) | “when expressed in trans from the multicopy plasmid pAR020, yohM conferred a marked enhancement of nickel and cobalt resistance” / “ARY023/pAR020 was able to resist nickel or cobalt concentrations 100-fold higher.” | 10.1128/JB.187.8.2912-2916.2005; 2005-04; https://doi.org/10.1128/JB.187.8.2912-2916.2005 | Strong overexpression edge; quantitative statement is relative (“100-fold higher”) rather than an absolute Co concentration in the quoted sentence. (rodrigue2005identificationofrcna pages 1-2) |
| CzcP (PIB4-type ATPase; label-only) | rapidly exports and enhances resistance to | zinc(2+) (CHEBI:29105) | “The second cluster codes for CzcP, a PIB4-type ATPase, which functions as a resistance enhancer exporting Zn2+ much more rapidly than PIB2-type ATPases” | 10.3390/microorganisms9020309; 2021-02-02; https://doi.org/10.3390/microorganisms9020309 | Boundary-case node for cobalt_tolerant graph: direct in-context evidence is for Zn export/resistance enhancement, not explicit Co export in the quoted passage. Include only as uncertain/supporting architecture unless paired with external primary CzcP evidence. (houdt2021adaptationofcupriavidus pages 1-2) |
| CzcP (PIB4-type ATPase; label-only) | may contribute to | cobalt tolerance (traitmech:000015) | “Deletion of czcP decreases the zinc resistance of C.” | 10.1128/jb.00343-22; 2023-04; https://doi.org/10.1128/jb.00343-22 | Very weak for cobalt specifically; useful only as boundary-case/supporting node within czc locus. Do not curate as cobalt-specific causal edge without stronger direct Co evidence. (grosse2023interplaybetweentwocomponent pages 1-3) |


*Table: This table compiles candidate causal edges for curating the microbial trait 'cobalt tolerant' into a TraitMech graph. It prioritizes mechanistic transport and regulation edges with quantitative resistance evidence where available, while flagging uncertain boundary-case claims such as CzcP's cobalt relevance.*

### 5) Recent developments and latest research (prioritizing 2023–2024)

#### 5.1 Regulation network complexity in *Cupriavidus metallidurans* (2023)
A 2023 *Journal of Bacteriology* study shows that expression of czc-associated promoters is governed not only by **CzcRS** but also by **interacting two-component systems (CzcR2S2 and AgrRS)**; cross-talk can repress or activate czc promoter responses depending on zinc conditions. This is directly relevant to curation because it motivates graph edges beyond “metal→czcCBA expression,” capturing **regulatory-layer emergence after horizontal gene transfer** (grosse2023interplaybetweentwocomponent pages 1-3).

#### 5.2 Systems-level proteomics and homeostasis framing (2024)
A 2024 *Metallomics* proteomics study links transcript-level responses to physiology and provides quantitative estimates of efflux complex abundance. It reports CzcCBA and CnrCBA as prominent transenvelope resistance determinants; notably, “Czc-CBA proteins were also present in control cells cultivated without added metals so that Czc has also a function in metal homeostasis” (galea2024linkingthetranscriptome pages 9-10). For curators, this supports representing **cobalt tolerance as layered resistance + homeostasis**, and suggests edges where efflux complexes contribute to both stress defense and baseline metal management.

#### 5.3 Co-selection with antibiotic resistance and the need for functional validation (2024)
A 2024 *FEMS Microbiology Reviews* synthesis emphasizes that correlations between metal resistance genes (including czcA/czcD) and antibiotic resistance genes are widespread, but warns about correlational bias and calls for **functional validation**: expression measurement (RT-qPCR/transcriptomics), proteomics, plasmid capture/characterization, heterologous expression, and knockouts/knockdowns (gillieatt2024unravellingthemechanisms pages 14-15, gillieatt2024unravellingthemechanisms pages 9-10). This is directly actionable for TraitMech curation policy: edges connecting metal exposure→ARG abundance should be marked **uncertain** unless demonstrated mechanistically.

### 6) Current applications and real-world implementations

#### 6.1 Bioremediation and phytoremediation support
Cobalt- (and nickel-) resistant microorganisms are discussed as enabling partners for remediation strategies, with efflux systems and sequestration/adsorption as key mechanisms. Quantitative resistance benchmarks are reported for classic plasmid determinants (e.g., 20 mM Co via czc; 5 mM Co via cnr; 20 mM Co via ncc), supporting strain selection and engineering targets (siunova2025potentialofnickel pages 5-7).

#### 6.2 Synthetic biology biosensors and engineered remediation modules
Recent reviews of bioremediation design emphasize engineered metalloregulators and whole-cell biosensors, with explicit mention that cobalt sensing can be built using regulator families including **CoaR** and **CsoR/RcnR-family regulators**, which naturally control efflux/sequestration circuits (olenska2025bacteriaundermetal pages 14-15, bai2023shootrootsignalcircuit pages 2-4, olaya‐abril2024bacterialtoleranceand pages 13-14). For TraitMech, these applications motivate treating “metal sensor → efflux gene expression” as a reusable causal motif.

### 7) Relevant statistics and quantitative data points (from cited studies)

**Resistance concentrations for canonical determinants (reviewed benchmarks):**
- *C. metallidurans* CH34 cnr determinant: “resistance to … **5 mM Co**” (siunova2025potentialofnickel pages 5-7).
- *C. metallidurans* CH34 czc determinant: “resistance to **20 mM Co**” (siunova2025potentialofnickel pages 5-7).
- Strain 31A ncc determinant: “resistance to … **Co (20 mM)**” (siunova2025potentialofnickel pages 5-7).

**Primary MIC-like growth arrest thresholds (single-gene exporter in *E. coli*):**
- rcnA/yohM mutant vs wild type: “growth arrest occurred at … **30 µM CoCl2** … compared with … **50 µM CoCl2**” (rodrigue2005identificationofrcna pages 1-2).
- Multicopy expression: “able to resist … concentrations **100-fold higher**” (relative statement) (rodrigue2005identificationofrcna pages 1-2).

**Quantitative cellular abundance of efflux complexes (2024 proteomics, CH34):**
- Copy-number–derived estimates suggest on the order of “**200 copies** of the CnrC3B6A3 and **250 copies** of the CzcC3B6A3 complexes per cell” (galea2024linkingthetranscriptome pages 9-10).

### 8) Ontology grounding recommendations

> Recommended grounding for the cobalt-tolerant graph includes METPO:traitmech:000015 for the trait; CHEBI:48828 cobalt(2+), CHEBI:28112 nickel(2+), CHEBI:29105 zinc(2+), CHEBI:22977 cadmium(2+), and CHEBI:42191 EDTA for core chemicals; ENVO:01000814 for microplastics; and GO terms such as GO:0043215 (active metal ion transmembrane transporter activity / efflux-related use), GO:0030002 (metal ion transport/export context), and GO:0018995 (horizontal gene transfer) for process-level nodes. These identifiers fit the current evidence base and support immediate curation of trait, chemical, environmental, and process nodes. (houdt2021adaptationofcupriavidus pages 1-2, balta2025theinterplaybetween pages 15-15, olenska2025bacteriaundermetal pages 14-15)
>
> Key mechanistic gene/protein nodes still lack stable organism-specific identifiers in the current evidence excerpts and should remain label-only until curated against UniProt, NCBI Gene, KEGG, or locus-specific plasmid annotations: czcA/czcB/czcC, cnrA/cnrB/cnrC, nccA/nccB/nccC, czcD, czcP, DmeF, FieF, and RcnA/YohM. This is especially important because the same family names recur across taxa and may refer to non-orthologous or differently specialized transporters. (galea2024linkingthetranscriptome pages 9-10, siunova2025potentialofnickel pages 5-7, rodrigue2005identificationofrcna pages 1-2)
>
> The czc, cnr, and ncc determinants are often plasmid-borne and should also be represented with mobile-genetic-context nodes when relevant, especially for pMOL30 (czc) and pMOL28 (cnr), with related HGT/co-selection context captured separately from the protein entities themselves. This will help distinguish mechanistic efflux nodes from genomic-location and transferability metadata in TraitMech curation. (siunova2025potentialofnickel pages 5-7, olenska2025bacteriaundermetal pages 9-11, grosse2023interplaybetweentwocomponent pages 1-3)


*Blockquote: This blockquote summarizes which identifiers are ready for immediate use in the cobalt tolerance graph and which important transporter/regulator nodes still need organism-specific grounding. It also highlights plasmid/mobile-context annotation needs for czc/cnr/ncc determinants.*

### 9) Warnings / non-curatable or uncertain claims (for TraitMech)

1. **CzcP as a cobalt-tolerance edge is not directly supported in the provided excerpts.** Evidence here supports Zn export/resistance enhancement; cobalt relevance remains plausible by locus association but should be marked uncertain until direct cobalt phenotype/export evidence is cited (houdt2021adaptationofcupriavidus pages 1-2).
2. **Co-selection and cross-resistance edges (metal exposure → antibiotic resistance) require careful curation.** Strong literature supports co-occurrence and plausible mechanisms, but the 2024 review emphasizes the frequent lack of direct functional confirmation; such edges should be marked uncertain unless backed by mechanistic experiments in the same study system (gillieatt2024unravellingthemechanisms pages 14-15, gillieatt2024unravellingthemechanisms pages 9-10).
3. **Gene/protein identifiers are taxon-dependent.** Many node labels (czcA, cnrA, DmeF, etc.) recur across taxa; without organism-specific accessions, avoid asserting equivalence across species (artifact-02) (galea2024linkingthetranscriptome pages 9-10, siunova2025potentialofnickel pages 5-7).

---

## DOI-first bibliography (with URLs and publication dates)

1. Große C, Scherer J, Schleuder G, Nies DH. **Interplay between Two-Component Regulatory Systems Is Involved in Control of Cupriavidus metallidurans Metal Resistance Genes.** *Journal of Bacteriology* (Published 2023-03-09 online / Apr 2023 issue). DOI: **10.1128/jb.00343-22**. https://doi.org/10.1128/jb.00343-22 (grosse2023interplaybetweentwocomponent pages 1-3)
2. Galea D, Herzberg M, Dobritzsch D, Fuszard M, Nies DH. **Linking the transcriptome to physiology: response of the proteome of Cupriavidus metallidurans to changing metal availability.** *Metallomics* (2024-11). DOI: **10.1093/mtomcs/mfae058**. https://doi.org/10.1093/mtomcs/mfae058 (galea2024linkingthetranscriptome pages 9-10)
3. Gillieatt BF, Coleman NV. **Unravelling the mechanisms of antibiotic and heavy metal resistance co-selection in environmental bacteria.** *FEMS Microbiology Reviews* (2024-06). DOI: **10.1093/femsre/fuae017**. https://doi.org/10.1093/femsre/fuae017 (gillieatt2024unravellingthemechanisms pages 14-15, gillieatt2024unravellingthemechanisms pages 9-10)
4. Olaya-Abril A, et al. **Bacterial tolerance and detoxification of cyanide, arsenic and heavy metals: Holistic approaches applied to bioremediation of industrial complex wastes.** *Microbial Biotechnology* (2024-01). DOI: **10.1111/1751-7915.14399**. https://doi.org/10.1111/1751-7915.14399 (olaya‐abril2024bacterialtoleranceand pages 13-14, olaya‐abril2024bacterialtoleranceand pages 11-13)
5. Van Houdt R, et al. **Adaptation of Cupriavidus metallidurans CH34 to Toxic Zinc Concentrations Involves an Uncharacterized ABC-Type Transporter.** *Microorganisms* (2021-02-02). DOI: **10.3390/microorganisms9020309**. https://doi.org/10.3390/microorganisms9020309 (houdt2021adaptationofcupriavidus pages 1-2)
6. Rodrigue A, Effantin G, Mandrand-Berthelot M-A. **Identification of rcnA (yohM), a Nickel and Cobalt Resistance Gene in Escherichia coli.** *Journal of Bacteriology* (2005-04). DOI: **10.1128/JB.187.8.2912-2916.2005**. https://doi.org/10.1128/JB.187.8.2912-2916.2005 (rodrigue2005identificationofrcna pages 1-2)
7. Siunova TV, et al. **Potential of nickel and cobalt resistant microorganisms for effective phytoremediation of heavy metal contaminated soils.** *Discover Environment* (2025-07). DOI: **10.1007/s44274-025-00301-y**. https://doi.org/10.1007/s44274-025-00301-y (siunova2025potentialofnickel pages 5-7)
8. Oleńska E, et al. **Bacteria Under Metal Stress—Molecular Mechanisms of Metal Tolerance.** *International Journal of Molecular Sciences* (2025-06). DOI: **10.3390/ijms26125716**. https://doi.org/10.3390/ijms26125716 (olenska2025bacteriaundermetal pages 9-11)
9. Balta I, et al. **The interplay between antimicrobial resistance, heavy metal pollution, and the role of microplastics.** *Frontiers in Microbiology* (2025-02). DOI: **10.3389/fmicb.2025.1550587**. https://doi.org/10.3389/fmicb.2025.1550587 (balta2025theinterplaybetween pages 15-15, balta2025theinterplaybetween pages 7-7)
10. Bai S, Han X-N, Feng D. **Shoot-root signal circuit: Phytoremediation of heavy metal contaminated soil.** *Frontiers in Plant Science* (2023-02). DOI: **10.3389/fpls.2023.1139744**. https://doi.org/10.3389/fpls.2023.1139744 (bai2023shootrootsignalcircuit pages 2-4)


References

1. (rodrigue2005identificationofrcna pages 1-2): Agnès Rodrigue, Géraldine Effantin, and Marie-Andrée Mandrand-Berthelot. Identification of rcna (yohm), a nickel and cobalt resistance gene in escherichia coli. Journal of Bacteriology, 187:2912-2916, Apr 2005. URL: https://doi.org/10.1128/jb.187.8.2912-2916.2005, doi:10.1128/jb.187.8.2912-2916.2005. This article has 250 citations and is from a peer-reviewed journal.

2. (siunova2025potentialofnickel pages 5-7): Tatiana V. Siunova, Andrey E. Filonov, Andrey V. Gorovtsov, Lenar I. Akhmetov, Fedor D. Ivanov, Vishnu D. Rajput, Tatiana M. Minkina, Svetlana N. Sushkova, Ming Hung Wong, and Jayanta Kumar Biswas. Potential of nickel and cobalt resistant microorganisms for effective phytoremediation of heavy metal contaminated soils. Discover Environment, Jul 2025. URL: https://doi.org/10.1007/s44274-025-00301-y, doi:10.1007/s44274-025-00301-y. This article has 5 citations and is from a peer-reviewed journal.

3. (olenska2025bacteriaundermetal pages 9-11): Ewa Oleńska, Wanda Małek, Izabela Swiecicka, Małgorzata Wójcik, Sofie Thijs, and Jaco Vangronsveld. Bacteria under metal stress—molecular mechanisms of metal tolerance. International Journal of Molecular Sciences, 26:5716, Jun 2025. URL: https://doi.org/10.3390/ijms26125716, doi:10.3390/ijms26125716. This article has 31 citations.

4. (galea2024linkingthetranscriptome pages 9-10): Diana Galea, Martin Herzberg, Dirk Dobritzsch, Matt Fuszard, and Dietrich H Nies. Linking the transcriptome to physiology: response of the proteome of cupriavidus metallidurans to changing metal availability. Metallomics: Integrated Biometal Science, Nov 2024. URL: https://doi.org/10.1093/mtomcs/mfae058, doi:10.1093/mtomcs/mfae058. This article has 8 citations.

5. (siunova2025potentialofnickel pages 1-3): Tatiana V. Siunova, Andrey E. Filonov, Andrey V. Gorovtsov, Lenar I. Akhmetov, Fedor D. Ivanov, Vishnu D. Rajput, Tatiana M. Minkina, Svetlana N. Sushkova, Ming Hung Wong, and Jayanta Kumar Biswas. Potential of nickel and cobalt resistant microorganisms for effective phytoremediation of heavy metal contaminated soils. Discover Environment, Jul 2025. URL: https://doi.org/10.1007/s44274-025-00301-y, doi:10.1007/s44274-025-00301-y. This article has 5 citations and is from a peer-reviewed journal.

6. (grosse2023interplaybetweentwocomponent pages 1-3): Cornelia Große, Judith Scherer, Grit Schleuder, and Dietrich H. Nies. Interplay between two-component regulatory systems is involved in control of cupriavidus metallidurans metal resistance genes. Journal of Bacteriology, Apr 2023. URL: https://doi.org/10.1128/jb.00343-22, doi:10.1128/jb.00343-22. This article has 12 citations and is from a peer-reviewed journal.

7. (houdt2021adaptationofcupriavidus pages 1-2): Rob Van Houdt, Joachim Vandecraen, Natalie Leys, Pieter Monsieurs, and Abram Aertsen. Adaptation of cupriavidus metallidurans ch34 to toxic zinc concentrations involves an uncharacterized abc-type transporter. Microorganisms, 9:309, Feb 2021. URL: https://doi.org/10.3390/microorganisms9020309, doi:10.3390/microorganisms9020309. This article has 15 citations.

8. (grosse2024antisensetranscriptionis pages 2-2): Cornelia Große, Jan Grau, Martin Herzberg, and Dietrich H Nies. Antisense transcription is associated with expression of metal resistance determinants in <i>cupriavidus metallidurans</i> ch34. Metallomics, Nov 2024. URL: https://doi.org/10.1093/mtomcs/mfae057, doi:10.1093/mtomcs/mfae057. This article has 5 citations and is from a peer-reviewed journal.

9. (balta2025theinterplaybetween pages 15-15): Igori Balta, Joanne Lemon, Anna Gadaj, Iuliana Cretescu, Ducu Stef, Ioan Pet, Lavinia Stef, David McCleery, Alastair Douglas, and Nicolae Corcionivoschi. The interplay between antimicrobial resistance, heavy metal pollution, and the role of microplastics. Frontiers in Microbiology, Feb 2025. URL: https://doi.org/10.3389/fmicb.2025.1550587, doi:10.3389/fmicb.2025.1550587. This article has 78 citations and is from a peer-reviewed journal.

10. (gillieatt2024unravellingthemechanisms pages 14-15): Brodie F Gillieatt and Nicholas V. Coleman. Unravelling the mechanisms of antibiotic and heavy metal resistance co-selection in environmental bacteria. FEMS Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1093/femsre/fuae017, doi:10.1093/femsre/fuae017. This article has 226 citations and is from a domain leading peer-reviewed journal.

11. (balta2025theinterplaybetween pages 7-7): Igori Balta, Joanne Lemon, Anna Gadaj, Iuliana Cretescu, Ducu Stef, Ioan Pet, Lavinia Stef, David McCleery, Alastair Douglas, and Nicolae Corcionivoschi. The interplay between antimicrobial resistance, heavy metal pollution, and the role of microplastics. Frontiers in Microbiology, Feb 2025. URL: https://doi.org/10.3389/fmicb.2025.1550587, doi:10.3389/fmicb.2025.1550587. This article has 78 citations and is from a peer-reviewed journal.

12. (siunova2025potentialofnickel pages 3-5): Tatiana V. Siunova, Andrey E. Filonov, Andrey V. Gorovtsov, Lenar I. Akhmetov, Fedor D. Ivanov, Vishnu D. Rajput, Tatiana M. Minkina, Svetlana N. Sushkova, Ming Hung Wong, and Jayanta Kumar Biswas. Potential of nickel and cobalt resistant microorganisms for effective phytoremediation of heavy metal contaminated soils. Discover Environment, Jul 2025. URL: https://doi.org/10.1007/s44274-025-00301-y, doi:10.1007/s44274-025-00301-y. This article has 5 citations and is from a peer-reviewed journal.

13. (olenska2025bacteriaundermetal pages 14-15): Ewa Oleńska, Wanda Małek, Izabela Swiecicka, Małgorzata Wójcik, Sofie Thijs, and Jaco Vangronsveld. Bacteria under metal stress—molecular mechanisms of metal tolerance. International Journal of Molecular Sciences, 26:5716, Jun 2025. URL: https://doi.org/10.3390/ijms26125716, doi:10.3390/ijms26125716. This article has 31 citations.

14. (bai2023shootrootsignalcircuit pages 2-4): Shiyan Bai, Xiao-na Han, and Dan Feng. Shoot-root signal circuit: phytoremediation of heavy metal contaminated soil. Frontiers in Plant Science, Feb 2023. URL: https://doi.org/10.3389/fpls.2023.1139744, doi:10.3389/fpls.2023.1139744. This article has 18 citations.

15. (gillieatt2024unravellingthemechanisms pages 9-10): Brodie F Gillieatt and Nicholas V. Coleman. Unravelling the mechanisms of antibiotic and heavy metal resistance co-selection in environmental bacteria. FEMS Microbiology Reviews, Jun 2024. URL: https://doi.org/10.1093/femsre/fuae017, doi:10.1093/femsre/fuae017. This article has 226 citations and is from a domain leading peer-reviewed journal.

16. (olaya‐abril2024bacterialtoleranceand pages 13-14): Alfonso Olaya‐Abril, Karolina Biełło, Gema Rodríguez‐Caballero, Purificación Cabello, Lara P. Sáez, Conrado Moreno‐Vivián, Víctor Manuel Luque‐Almagro, and María Dolores Roldán. Bacterial tolerance and detoxification of cyanide, arsenic and heavy metals: holistic approaches applied to bioremediation of industrial complex wastes. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14399, doi:10.1111/1751-7915.14399. This article has 38 citations and is from a peer-reviewed journal.

17. (olaya‐abril2024bacterialtoleranceand pages 11-13): Alfonso Olaya‐Abril, Karolina Biełło, Gema Rodríguez‐Caballero, Purificación Cabello, Lara P. Sáez, Conrado Moreno‐Vivián, Víctor Manuel Luque‐Almagro, and María Dolores Roldán. Bacterial tolerance and detoxification of cyanide, arsenic and heavy metals: holistic approaches applied to bioremediation of industrial complex wastes. Microbial Biotechnology, Jan 2024. URL: https://doi.org/10.1111/1751-7915.14399, doi:10.1111/1751-7915.14399. This article has 38 citations and is from a peer-reviewed journal.