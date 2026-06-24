---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:47:46.050256'
end_time: '2026-06-18T11:59:57.108495'
duration_seconds: 731.06
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: natural competence
  trait_identifier: traitmech:000087
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: natural_competence
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A physiological state in which a cell takes up free extracellular DNA
    from the environment and integrates it into its genome (natural genetic transformation).
  parent_traits: METPO:1000059
  synonyms: natural transformation
  evidence_summary: 'DOI:10.1038/nrmicro3199:  (Johnston et al. review the distribution,
    shared mechanisms, and control of natural bacterial transformation (competence
    for DNA uptake).) | DOI:10.1038/s41579-021-00650-4:  (Review of horizontal gene
    transfer supports natural transformation as a major route of bacterial DNA acquisition.)'
  causal_graph_summary: 'natural_competence_dna_uptake: 3 nodes, 2 edges'
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
- **Trait label:** natural competence
- **METPO identifier:** traitmech:000087
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological state in which a cell takes up free extracellular DNA from the environment and integrates it into its genome (natural genetic transformation).
- **Parent traits:** METPO:1000059
- **Synonyms:** natural transformation
- **Existing evidence:** DOI:10.1038/nrmicro3199:  (Johnston et al. review the distribution, shared mechanisms, and control of natural bacterial transformation (competence for DNA uptake).) | DOI:10.1038/s41579-021-00650-4:  (Review of horizontal gene transfer supports natural transformation as a major route of bacterial DNA acquisition.)
- **Existing causal graph summary:** natural_competence_dna_uptake: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **natural competence** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/natural_competence.yaml`.

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
- **Trait label:** natural competence
- **METPO identifier:** traitmech:000087
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological state in which a cell takes up free extracellular DNA from the environment and integrates it into its genome (natural genetic transformation).
- **Parent traits:** METPO:1000059
- **Synonyms:** natural transformation
- **Existing evidence:** DOI:10.1038/nrmicro3199:  (Johnston et al. review the distribution, shared mechanisms, and control of natural bacterial transformation (competence for DNA uptake).) | DOI:10.1038/s41579-021-00650-4:  (Review of horizontal gene transfer supports natural transformation as a major route of bacterial DNA acquisition.)
- **Existing causal graph summary:** natural_competence_dna_uptake: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **natural competence** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/natural_competence.yaml`.

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


## Research report: Natural competence (METPO traitmech:000087)

### Scope summary (trait definition, phenotype boundaries)
Natural competence (syn. natural transformation) is a **transient physiological state** in which bacteria express a dedicated machinery that **captures extracellular DNA, transports it across envelope barriers, converts it to single-stranded DNA (ssDNA), and recombines it into the chromosome** (natural genetic transformation). (mazzamurro2024intragenomicconflictswith pages 1-2, zuke2024productiondynamicsand pages 56-60, prudhomme2024pneumococcalcompetenceis pages 1-2)

A key boundary condition emphasized in recent synthesis is that **natural transformation is recipient-controlled** (the recipient regulates entry into competence and the uptake machinery), distinguishing it from donor-driven transfer such as conjugation and from phage-mediated transduction. (mazzamurro2024intragenomicconflictswith pages 1-2)

Operationally, the trait is typically assayed as **transformability / transformation rate** under defined conditions. Recent population-scale data show many strains are **below detection under “standard conditions,”** highlighting that competence is often **condition- and strain-dependent** rather than a fixed species property. (mazzamurro2024intragenomicconflictswith pages 1-2, toussaint2024unveilingtheregulatory pages 6-9)

**Nearby traits to distinguish from:**
- **Artificial/induced competence (chemical/electroporation):** not the trait here; TraitMech scope is **naturally regulated competence programs**.
- **General DNA uptake without integration:** competence as defined here includes uptake plus integration by homologous recombination. (mazzamurro2024intragenomicconflictswith pages 1-2)
- **DNA uptake as nutrition:** extracellular DNA can be used as a nutrient in some contexts, but the defining feature here is **genetic transformation** (integration and heritable change). (mazzamurro2024intragenomicconflictswith pages 1-2)

---

### Current mechanistic understanding (key concepts)
#### Canonical mechanistic steps (recipient-side)
Recent review synthesis (2024) consolidates a mechanistic model in which DNA must traverse the cell envelope by coordinated action of **(i) a type IV–like competence pilus**, **(ii) surface/periplasmic DNA receptors**, and **(iii) an inner-membrane channel and ATPase-driven translocation**, followed by **(iv) RecA-mediated homologous recombination**. (zuke2024fromisotopicallylabeled pages 9-12, zuke2024fromisotopicallylabeled media 57140c68, mazzamurro2024intragenomicconflictswith pages 1-2)

A curator-relevant, stepwise decomposition supported across the evidence set is:
1) **Pilus biogenesis and exposure:** competent cells produce pilus biogenesis proteins; pili extend into the extracellular space. (zuke2024fromisotopicallylabeled media 57140c68)
2) **DNA capture:** competence pili bind free extracellular DNA; live-cell imaging supports DNA localization to pilus tips. (zuke2024fromisotopicallylabeled pages 9-12)
3) **Pilus retraction-driven delivery:** retraction/disassembly pulls DNA through the outer layers (outer membrane in diderms or cell wall in monoderms) toward the membrane-localized uptake apparatus; obstruction of retraction reduces transformation rate. (zuke2024fromisotopicallylabeled pages 9-12, zuke2024fromisotopicallylabeled media 57140c68)
4) **Membrane translocation:** ComEA is a DNA receptor implicated in binding/transfer, ComEC is a membrane channel required for uptake, and ComFA is an ATPase that aids DNA entry via ATP hydrolysis. (hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60, zuke2024productiondynamicsand pages 158-161)
5) **Processing to ssDNA and recombination:** one strand is degraded to produce ssDNA; ssDNA-binding proteins and DprA protect/process incoming ssDNA and promote RecA loading; RecA catalyzes recombination into the chromosome. (zuke2024productiondynamicsand pages 56-60, mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24)

A schematic summary figure supporting the competence pilus and DNA transport model is provided in Zuke & Burton (Microbiology and Molecular Biology Reviews, **Mar 2024**, doi: **10.1128/mmbr.00125-23**, URL https://doi.org/10.1128/mmbr.00125-23), notably a figure depicting competence pilus capture and retraction-mediated DNA translocation across Gram-negative and Gram-positive envelopes. (zuke2024fromisotopicallylabeled media 57140c68)

#### Core molecular entities (high-confidence, broadly conserved)
Evidence consistently supports the following as central “core” modules for many naturally competent bacteria:
- **Competence pilus / type IV pilus-like machinery (ComG operon; major pilin ComGC):** mediates DNA capture and delivery to the cell surface; in *Bacillus subtilis* the ComG system is required for DNA binding to intact cells and for wall breaching. (zuke2024fromisotopicallylabeled pages 9-12, zuke2024productiondynamicsand pages 34-38, zuke2024productiondynamicsand pages 23-28)
- **DNA receptor and membrane channel:** ComEA (DNA receptor/binding and transport) and ComEC (membrane uptake channel). (hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 23-28, zuke2024productiondynamicsand pages 158-161)
- **Translocation ATPase:** ComFA supports DNA entry by ATP hydrolysis. (zuke2024productiondynamicsand pages 56-60, hardy2024yranisa pages 22-24)
- **Recombination module:** DprA recruits/loads RecA onto incoming ssDNA; RecA mediates homologous recombination. (mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24)

#### Emerging/2024 development: additional recombination processing factor (YraN)
A 2024 comparative genetics and functional study (bioRxiv **Feb 2024**, doi: **10.1101/2024.02.06.579203**, URL https://doi.org/10.1101/2024.02.06.579203) reports a **conserved gene, yraN**, required for natural transformation in two distantly related diderm species and proposes that **YraN is a nuclease associated with the competence helicase ComM**, promoting extended recombination events by processing intermediates formed during integration. (hardy2024yranisa pages 22-24)

Because this is currently a preprint and mechanistic generality across taxa remains to be validated, curations of YraN-related edges should be flagged as **provisional**. (hardy2024yranisa pages 22-24)

---

### Recent developments (prioritizing 2023–2024)
#### 1) Quantitative, within-species evolution of transformability (2024)
A large-scale study in PLOS Biology (**Oct 2024**, doi: **10.1371/journal.pbio.3002814**, URL https://doi.org/10.1371/journal.pbio.3002814) measured transformation rates across **1,282 strains** (786 *Legionella pneumophila*; 496 *Acinetobacter baumannii*) and found:
- Transformation rates vary by **~6 orders of magnitude** across strains. (mazzamurro2024intragenomicconflictswith pages 1-2)
- Under standard laboratory conditions, **nearly half** of *L. pneumophila* strains and **>1/3** of *A. baumannii* strains were **below detection** (likely non-transformable in those conditions). (mazzamurro2024intragenomicconflictswith pages 1-2)
- Transformability is associated with **intragenomic conflict**: transformable strains have **fewer mobile genetic elements (MGEs)**, and negative associations are observed between transformation and MGEs. (mazzamurro2024intragenomicconflictswith pages 1-2)

These results are directly curator-relevant for TraitMech because they imply that “natural competence” should often be modeled as an **interaction between genetic capacity and permissive conditions**, not a binary taxonomic trait. (mazzamurro2024intragenomicconflictswith pages 1-2)

#### 2) Competence as a stress- and quorum-sensing–driven population program (2024)
A Nature Communications study (**Jul 2024**, doi: **10.1038/s41467-024-49853-2**, URL https://doi.org/10.1038/s41467-024-49853-2) reframes *Streptococcus pneumoniae* competence as a “**populational health sensor**” with a biphasic **Self-Induction and Propagation (SI&P)** quorum-sensing mechanism:
- The ComABCDE quorum-sensing system uses CSP (competence-stimulating peptide): CSP activates ComD → phosphorylates ComE → ComE~P induces the early competence regulon (including comABCDE), creating positive feedback. (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 8-8)
- A minority of “self-induced” cells can arise stochastically under stress (including antibiotics) and, above a threshold, competence **propagates through the population**. (prudhomme2024pneumococcalcompetenceis pages 2-3, prudhomme2024pneumococcalcompetenceis pages 5-6)
- The competence-induced effector **ComM** promotes a division delay and is linked to competence-associated antibiotic survival/tolerance phenotypes. (prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 7-8)

These findings strengthen the view that competence is not only a DNA-uptake phenotype but also a **co-regulated physiological state** with stress-response consequences in some taxa. (prudhomme2024pneumococcalcompetenceis pages 1-2)

#### 3) Global metabolism/stress regulators controlling ComX and competence (2024)
A 2024 lactococcal regulatory analysis (preprint deposited **Feb 2024**, doi: **10.1101/2024.02.08.579460**, URL https://doi.org/10.1101/2024.02.08.579460) identifies **carbon source, nitrogen supply, and pH** as key factors controlling competence in *Lactococcus lactis* via repression of comX:
- **CcpA, CodY, and CovR/CovRS** directly repress comX transcription; CovR binds the comX promoter region. (toussaint2024unveilingtheregulatory pages 1-6, toussaint2024unveilingtheregulatory pages 39-41)
- **MecA–ClpCP** proteolysis degrades ComX, providing strong post-translational repression of competence. (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 16-19)
- A **diauxic shift** (glucose exhaustion with subsequent maltose use) increases comX expression and transformability; low pH suppresses transformability in wild-type strains. (toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 9-13)

This provides a concrete, evidence-backed regulatory subgraph linking **nutritional/stress sensing to competence** in a biotechnologically relevant lactic acid bacterium. (toussaint2024unveilingtheregulatory pages 16-19)

---

### Current applications and real-world implementations
1) **Genetic engineering by natural transformation (allelic exchange) in pyogenic streptococci**
A peer-reviewed mSphere study (**Jul 2024**, doi: **10.1128/msphere.00214-24**, URL https://doi.org/10.1128/msphere.00214-24) established an in vitro natural transformation protocol for *Streptococcus dysgalactiae* enabling construction of deletion mutants by allelic exchange and functional testing (e.g., lactose utilization deletions). (marli2024geneticmodificationof pages 1-2)

2) **Competence-informed chassis development and multiplex editing workflows (contextual)**
A 2024 dissertation-style synthesis on *Vibrio natriegens* as a synthetic biology chassis cites practical methods that exploit natural transformation, including multiplex genome editing by natural transformation (MuGENT) and related approaches in vibrios. (stukenberg2024establishingthefastgrowing pages 38-39)

3) **Competence regulation as a targetable phenotype in pathogenesis contexts (conceptual)**
In *S. pneumoniae*, competence is linked to antibiotic stress responses and population heterogeneity, implying potential translational relevance (e.g., effects on survival/tolerance and transformation potential under stress), although direct clinical interventions are not established in the cited work. (prudhomme2024pneumococcalcompetenceis pages 7-8, prudhomme2024pneumococcalcompetenceis pages 9-10)

---

### Recent statistics and data (2024)
- **Across 1,282 strains** (*L. pneumophila* n=786; *A. baumannii* n=496), transformation rates vary by **~6 orders of magnitude**; under standard conditions **~50% of *L. pneumophila*** and **>33% of *A. baumannii*** are below detection. (mazzamurro2024intragenomicconflictswith pages 1-2)
- In *S. dysgalactiae* (n=179 genomes), **64.2%** of strains carry an **intact competence gene set**; stratified: **54.2%** of SDSD isolates (59 genomes) and **69.2%** of SDSE isolates (120 genomes) have complete intact competence genes. (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5)
- In *L. lactis*, transformation rates are strongly condition-dependent; an optimized medium (CDM*-DEB) increases transformation rate to approximately **4.5×10^-5**, and a less optimized condition is ~**5×10^-6** (context-specific assay). (toussaint2024unveilingtheregulatory pages 6-9)

---

### Candidate nodes for TraitMech curation
The following table compiles candidate nodes grounded where possible and grouped for curation.

| Group | Label | Node type | Brief role in competence | Suggested grounding CURIE(s) |
|---|---|---|---|---|
| Phenotype/Process | natural competence | phenotype/process | Transient physiological state in which cells express machinery for uptake of extracellular DNA and subsequent recombination/integration (mazzamurro2024intragenomicconflictswith pages 1-2, zuke2024productiondynamicsand pages 56-60, prudhomme2024pneumococcalcompetenceis pages 1-2) | GO:0030420 |
| Phenotype/Process | natural transformation | biological process | Recipient-controlled horizontal gene transfer via uptake of exogenous DNA followed by chromosomal integration by homologous recombination (mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24) | GO:0030420 |
| Phenotype/Process | extracellular DNA uptake | biological process | Import of environmental DNA across the cell envelope; core mechanistic component of competence (hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60, zuke2024fromisotopicallylabeled media 57140c68) | GO:0019295 |
| Phenotype/Process | homologous recombination of transforming DNA | biological process | Incoming ssDNA is recombined into the chromosome, typically after RecA loading (mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60) | GO:0000724 |
| Phenotype/Process | competence pilus biogenesis | biological process | Assembly of a type IV-like filament required for DNA capture and/or translocation through outer layers (zuke2024productiondynamicsand pages 56-60, zuke2024productiondynamicsand pages 23-28, zuke2024fromisotopicallylabeled media 57140c68) | GO:0046260 |
| Phenotype/Process | pilus retraction-driven DNA transport | biological process | Retraction/disassembly of DNA-bound competence pili pulls DNA toward the cell surface/periplasm/cell wall interface (zuke2024fromisotopicallylabeled pages 9-12, zuke2024fromisotopicallylabeled media 57140c68) |  |
| Cellular structures | competence pilus / type IV competence pilus | cellular structure | Extracellular filament that binds DNA and mediates initial uptake steps in several competent bacteria (hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60, zuke2024fromisotopicallylabeled pages 9-12) | GO:0046260 |
| Cellular structures | cell wall | cellular structure | Gram-positive barrier that competence pili must breach to deliver DNA to membrane uptake proteins (zuke2024productiondynamicsand pages 56-60, zuke2024productiondynamicsand pages 34-38, zuke2024fromisotopicallylabeled media 57140c68) | GO:0005618 |
| Cellular structures | periplasm | cellular compartment | Intermediate compartment for DNA transfer in diderm bacteria before inner-membrane import (hardy2024yranisa pages 22-24, zuke2024fromisotopicallylabeled media 57140c68) | GO:0042597 |
| Cellular structures | cytoplasmic membrane | cellular structure | Location of ComEA/ComEC-associated uptake and final translocation to cytosol (hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60, zuke2024fromisotopicallylabeled media 57140c68) | GO:0005886 |
| Core proteins/complexes | ComGC major pilin | protein | Major structural pilin of competence pili in Bacillus subtilis and Streptococcus pneumoniae; forms retractile DNA-binding filaments (zuke2024productiondynamicsand pages 56-60, zuke2024productiondynamicsand pages 23-28, zuke2024fromisotopicallylabeled pages 9-12) |  |
| Core proteins/complexes | ComG operon / ComG machinery | protein complex/system | Encodes pilus biogenesis proteins required for DNA binding/uptake during competence (zuke2024productiondynamicsand pages 56-60, zuke2024productiondynamicsand pages 34-38, zuke2024productiondynamicsand pages 23-28, zuke2024productiondynamicsand pages 158-161) |  |
| Core proteins/complexes | ComC prepilin peptidase | enzyme/protein | Processes ComGC/pilin precursors for competence pilus assembly (zuke2024productiondynamicsand pages 23-28) | EC:3.4.23.- |
| Core proteins/complexes | ComEA | DNA receptor/protein | Membrane-associated DNA receptor required for DNA binding and transport to downstream uptake machinery (hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 23-28, zuke2024productiondynamicsand pages 161-163, zuke2024productiondynamicsand pages 158-161) | GO:0003677 |
| Core proteins/complexes | ComEC | membrane channel/protein | Membrane channel required for DNA uptake into the cytoplasm (mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60, marli2024geneticmodificationof pages 1-2) |  |
| Core proteins/complexes | ComFA | ATPase/translocase | DNA-dependent ATPase that assists DNA entry through the membrane-associated uptake apparatus (hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60, prudhomme2024pneumococcalcompetenceis pages 12-13) | GO:0016887 |
| Core proteins/complexes | ComFC | uptake-associated protein | Part of the ComFA/ComFC/DprA-associated uptake and processing module in transformation (hardy2024yranisa pages 22-24) |  |
| Core proteins/complexes | DprA | ssDNA-processing protein | Protects incoming ssDNA, promotes/mediates RecA loading, and in pneumococcus contributes to competence shut-off (mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60, prudhomme2024pneumococcalcompetenceis pages 13-14) |  |
| Core proteins/complexes | RecA | recombinase | Catalyzes homologous recombination of incoming transforming ssDNA (mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24, zuke2024productiondynamicsand pages 56-60, prudhomme2024pneumococcalcompetenceis pages 12-13) | GO:0000150 |
| Core proteins/complexes | SsbA / SsbB | ssDNA-binding proteins | Bind incoming ssDNA before or during DprA-mediated RecA loading (zuke2024productiondynamicsand pages 56-60) | GO:0003697 |
| Core proteins/complexes | ComM | helicase/recombination factor | Competence-associated helicase that promotes recombination/branch migration of transforming DNA; in pneumococcus also drives division delay/tolerance phenotypes (mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24, prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 7-8) |  |
| Core proteins/complexes | YraN | nuclease | Conserved helicase-associated nuclease proposed to cooperate with ComM to foster extended recombination events during transformation (hardy2024yranisa pages 22-24) |  |
| Core proteins/complexes | BdbDC | oxidoreductase pair | Required for ComGC oligomerization/stability during competence pilus formation in B. subtilis (zuke2024productiondynamicsand pages 34-38, zuke2024productiondynamicsand pages 23-28) |  |
| Regulatory proteins/systems | ComABCDE quorum-sensing system | regulatory system | Pneumococcal peptide-signaling system controlling transient competence induction and positive feedback (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 2-3) |  |
| Regulatory proteins/systems | CSP (competence-stimulating peptide) | signaling peptide | Autoinducing pheromone that triggers competence through the ComD/ComE pathway in pneumococcus (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 2-3, prudhomme2024pneumococcalcompetenceis pages 12-13) | CHEBI:16670 |
| Regulatory proteins/systems | ComD | sensor histidine kinase | Detects CSP and phosphorylates ComE to activate the early competence regulon (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 2-3) | GO:0000155 |
| Regulatory proteins/systems | ComE | response regulator | Unphosphorylated/phosphorylated balance controls pneumococcal competence thresholding; ComE~P activates early competence genes (prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 9-10) | GO:0000156 |
| Regulatory proteins/systems | ComX / σX | alternative sigma factor | Master competence regulator that activates late competence genes in lactococci/streptococci (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 1-6, marli2024geneticmodificationof pages 1-2) | GO:0003677 |
| Regulatory proteins/systems | ComRS | regulatory system | Pheromone-based system present in S. dysgalactiae controlling competence activation through ComX (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) |  |
| Regulatory proteins/systems | XIP peptide | signaling peptide | Competence-inducing pheromone used experimentally to induce comX and ssbB expression in S. dysgalactiae (marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) |  |
| Regulatory proteins/systems | CcpA | transcriptional regulator | Carbon catabolite regulator that directly represses comX under glucose conditions in L. lactis (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 1-6, toussaint2024unveilingtheregulatory pages 9-13) |  |
| Regulatory proteins/systems | CodY | transcriptional regulator | Nutrient-responsive repressor that binds PcomX and represses competence in response to nitrogen/BCAA status (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 9-13) |  |
| Regulatory proteins/systems | CovR/CovRS | two-component stress regulator | Stress-responsive direct repressor of comX; mediates pH sensitivity of competence in L. lactis (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 13-16, toussaint2024unveilingtheregulatory pages 9-13) |  |
| Regulatory proteins/systems | MecA-ClpCP proteolytic machinery | proteolysis complex | Degrades ComX and thereby limits activation of late competence genes and transformability (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 1-6, toussaint2024unveilingtheregulatory pages 6-9) | GO:0030163 |
| Regulatory proteins/systems | MecA | adaptor protein | Delivers ComX to ClpCP for degradation; natural substitutions alter transformability (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 6-9) |  |
| Environmental/experimental factors | extracellular DNA | substrate | Free environmental DNA that is captured by competence pili and imported during transformation (mazzamurro2024intragenomicconflictswith pages 1-2, zuke2024productiondynamicsand pages 56-60, zuke2024fromisotopicallylabeled pages 9-12) | CHEBI:16991 |
| Environmental/experimental factors | antibiotic stress | environmental/experimental factor | Can induce or modulate competence in pneumococcus and alter transformation/survival outcomes (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 13-14, prudhomme2024pneumococcalcompetenceis pages 7-8, prudhomme2024pneumococcalcompetenceis pages 5-6) | CHEBI:33281 |
| Environmental/experimental factors | replication stress | environmental/experimental factor | Reported trigger of bacterial competence by increasing origin-proximal gene dosage in pneumococcus (prudhomme2024pneumococcalcompetenceis pages 13-14) |  |
| Environmental/experimental factors | cell chaining | cellular state | Antibiotic-induced chaining can promote competence by altering quorum-sensing signal distribution (prudhomme2024pneumococcalcompetenceis pages 13-14) |  |
| Environmental/experimental factors | carbon source composition | environmental/experimental factor | Sugar identity and diauxic shifts control comX expression and transformability in L. lactis (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 6-9, toussaint2024unveilingtheregulatory pages 9-13) |  |
| Environmental/experimental factors | glucose starvation / diauxic shift | environmental/experimental factor | Glucose exhaustion followed by use of alternative sugars stimulates comX expression and spontaneous transformation in L. lactis (toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 6-9, toussaint2024unveilingtheregulatory pages 9-13) |  |
| Environmental/experimental factors | maltose | chemical/nutrient | Alternative sugar associated with competence induction during diauxic shift in L. lactis (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 6-9) | CHEBI:17306 |
| Environmental/experimental factors | nitrogen supply / amino acid status | environmental/experimental factor | Nitrogen conditions, including isoleucine abundance and medium composition, regulate CodY-dependent repression of comX (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 9-13, toussaint2024unveilingtheregulatory pages 32-39) |  |
| Environmental/experimental factors | isoleucine | chemical/nutrient | Excess isoleucine promotes CodY-mediated repression of comX and decreases transformability in L. lactis (toussaint2024unveilingtheregulatory pages 16-19, toussaint2024unveilingtheregulatory pages 9-13, toussaint2024unveilingtheregulatory pages 32-39) | CHEBI:24898 |
| Environmental/experimental factors | pH | environmental/experimental factor | Initial pH strongly affects transformability; CovRS contributes to pH-dependent repression in L. lactis (toussaint2024unveilingtheregulatory pages 39-41, toussaint2024unveilingtheregulatory pages 13-16, toussaint2024unveilingtheregulatory pages 9-13) |  |
| Environmental/experimental factors | mobile genetic elements (MGEs) | genomic factor | Plasmids, prophages, conjugative elements, and transposons are negatively associated with transformability and can disrupt competence genes (mazzamurro2024intragenomicconflictswith pages 1-2, marli2024geneticmodificationof pages 2-5) |  |
| Outputs/fitness consequences | transformability / transformation rate | assay phenotype | Quantitative measurable output varying across strains and conditions; used as the key competence assay readout (mazzamurro2024intragenomicconflictswith pages 1-2, marli2024geneticmodificationof pages 1-2, marli2024geneticmodificationof pages 2-5) |  |
| Outputs/fitness consequences | competence propagation in population | population process | Self-Induction and Propagation (SI&P) spreads competence from a minority self-induced subpopulation under stress (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 2-3, prudhomme2024pneumococcalcompetenceis pages 5-6, prudhomme2024pneumococcalcompetenceis pages 9-10) |  |
| Outputs/fitness consequences | division delay | cellular phenotype | Competence-induced ComM-dependent delay linked to fratricide immunity and antibiotic tolerance in pneumococcus (prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 1-2) |  |
| Outputs/fitness consequences | fratricide immunity | cellular phenotype | Competent pneumococci are protected from CbpD-mediated sibling killing by ComM (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 8-8) |  |
| Outputs/fitness consequences | antibiotic tolerance/survival | fitness consequence | Competence can improve survival of lethal stress in some contexts, especially via ComM in pneumococcus (prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 7-8, prudhomme2024pneumococcalcompetenceis pages 5-6) |  |
| Outputs/fitness consequences | reduced genetic linkage / adaptive evolution | evolutionary consequence | Natural transformation decreases linkage and can accelerate adaptation within species (mazzamurro2024intragenomicconflictswith pages 1-2) |  |
| Outputs/fitness consequences | fewer MGEs in transformable strains | genomic/evolutionary consequence | Transformable strains tend to harbor fewer mobile genetic elements, consistent with conflict-driven evolution of competence (mazzamurro2024intragenomicconflictswith pages 1-2) |  |
| Outputs/fitness consequences | genetic engineering by allelic exchange | application | Natural transformation can be exploited to build deletion mutants in S. dysgalactiae and other bacteria (marli2024geneticmodificationof pages 1-2, stukenberg2024establishingthefastgrowing pages 38-39) | GO:0016441 |


*Table: This table lists curator-ready candidate nodes for a TraitMech causal graph of natural competence, grouped by biological role and grounded where possible to standard ontologies. It is restricted to entities supported by the gathered evidence and highlights both core transformation machinery and major regulatory/environmental modulators.*

---

### Evidence-backed candidate causal edges (triples)
The table below proposes curator-ready subject–predicate–object edges directly supported by the retrieved sources, with notes on taxon specificity and uncertainty.

| Subject node | Predicate | Object node | Taxon/context | Evidence snippet | Reference (DOI/URL, year) | Notes/uncertainty |
|---|---|---|---|---|---|---|
| competence pilus / type IV competence pilus | binds | extracellular DNA | Broad bacterial competence model; shown in *Vibrio cholerae*, *Streptococcus pneumoniae*, *Bacillus subtilis* | “produce retractile, DNA-binding pili” and “these T4P filaments co-localized DNA at their tips” (zuke2024fromisotopicallylabeled pages 9-12) | Zuke & Burton 2024, https://doi.org/10.1128/mmbr.00125-23 | Broad/general edge supported across multiple taxa; likely core but architecture differs by clade. |
| pilus retraction | promotes | extracellular DNA uptake | Broad competence-pilus model | “Physical obstruction of T4P retraction... resulted in a similar decrease in transformation rate” (zuke2024fromisotopicallylabeled pages 9-12) | Zuke & Burton 2024, https://doi.org/10.1128/mmbr.00125-23 | Supported experimentally in diderms; generalized to Gram-positives in review/model, so mildly uncertain across all taxa. |
| competence pilus retraction ATPase | transports | DNA through outer layers | Broad model; Gram-negative and Gram-positive cartoon model | “Retraction ATPases... facilitate pilus disassembly, pulling the bound DNA through the outer membrane or cell wall” (zuke2024fromisotopicallylabeled media 57140c68) | Zuke & Burton 2024, https://doi.org/10.1128/mmbr.00125-23 | Model-based synthesis from review figure; curate as mechanistic summary with caution. |
| ComEA | binds | extracellular DNA | *B. subtilis* and broad transformation literature | “ComEA... is needed for both DNA binding and transport” (zuke2024productiondynamicsand pages 158-161) | cited in Zuke 2024 synthesis, no direct article DOI in retrieved metadata | Strong canonical edge, but snippet comes via secondary synthesis. |
| ComEA | required_for | DNA transport | *B. subtilis* and broad transformation literature | “ComEA... is needed for both DNA binding and transport” (zuke2024productiondynamicsand pages 158-161) | cited in Zuke 2024 synthesis, no direct article DOI in retrieved metadata | Strong canonical edge, but snippet comes via secondary synthesis. |
| ComEA | mediates_transfer_to | periplasm / downstream uptake apparatus | Broad | “ComEA functions as an external DNA receptor and mediates transfer into the periplasm” (hardy2024yranisa pages 22-24) | Hardy et al. 2024 preprint, https://doi.org/10.1101/2024.02.06.579203 | More applicable to diderms; use context note. |
| ComEC | required_for | DNA uptake | Broad | “ComEC is a membrane channel required for DNA uptake” (hardy2024yranisa pages 22-24) | Hardy et al. 2024 preprint, https://doi.org/10.1101/2024.02.06.579203 | Core uptake edge; broad but secondary synthesis in preprint intro. |
| ComFA | promotes | DNA entry | Broad; membrane-associated uptake step | “ComFA aiding entry via ATP hydrolysis” (zuke2024productiondynamicsand pages 56-60) | Zuke 2024 work summarized in evidence; no clear journal DOI in retrieved metadata | Mechanistic edge supported in *B. subtilis* model; species-specific context advisable. |
| DprA | recruits | RecA | Broad | “DprA and recruitment of RecA” and “DprA hands incoming ssDNA to RecA” (mazzamurro2024intragenomicconflictswith pages 1-2, hardy2024yranisa pages 22-24) | Mazzamurro et al. 2024, https://doi.org/10.1371/journal.pbio.3002814; Hardy et al. 2024, https://doi.org/10.1101/2024.02.06.579203 | Core post-uptake recombination edge; broad. |
| RecA | mediates | homologous recombination of transforming DNA | Broad | “protection of incoming ssDNA by DprA and recruitment of RecA” and transformation followed by “homologous recombination” (mazzamurro2024intragenomicconflictswith pages 1-2) | Mazzamurro et al. 2024, https://doi.org/10.1371/journal.pbio.3002814 | Core edge; broad/general. |
| ComG operon / ComG machinery | required_for | DNA binding across cell wall | *Bacillus subtilis* | “comG mutants abolish DNA binding to intact competent cells while protoplasts still bind DNA,” implying “comG expression is necessary for DNA breaching the cell wall” (zuke2024productiondynamicsand pages 34-38) | Zuke 2024 work summarized in evidence; no clear journal DOI in retrieved metadata | Strong but taxon-specific to Gram-positive wall translocation. |
| ComG operon | required_for | transformability | *Bacillus subtilis* | mutants were “completely non-transformable and unable to bind exogenous DNA during natural competence” (zuke2024productiondynamicsand pages 23-28) | Zuke 2024 work summarized in evidence; no clear journal DOI in retrieved metadata | Strong taxon-specific edge. |
| BdbDC | required_for | ComGC oligomerization | *Bacillus subtilis* | “Expression of the genes encoding the dithiol oxidoreductase pair bdbDC was also required for ComGC oligomerization” (zuke2024productiondynamicsand pages 23-28) | Zuke 2024 work summarized in evidence; no clear journal DOI in retrieved metadata | Strong species-specific assembly edge. |
| ComC prepilin peptidase | processes | ComGC major pilin | *Bacillus subtilis* | “ComGC proteolytic processing was, indeed, later found to be dependent on ComC” (zuke2024productiondynamicsand pages 23-28) | Zuke 2024 work summarized in evidence; no clear journal DOI in retrieved metadata | Strong species-specific maturation edge. |
| CSP (competence-stimulating peptide) | activates | ComD | *Streptococcus pneumoniae* | “CSP activates ComD” (prudhomme2024pneumococcalcompetenceis pages 1-2) | Prudhomme et al. 2024, https://doi.org/10.1038/s41467-024-49853-2 | Strong pneumococcal regulatory edge. |
| ComD | phosphorylates | ComE | *Streptococcus pneumoniae* | “CSP activates ComD, which phosphorylates ComE” (prudhomme2024pneumococcalcompetenceis pages 1-2) | Prudhomme et al. 2024, https://doi.org/10.1038/s41467-024-49853-2 | Strong pneumococcal regulatory edge. |
| ComE~P | induces | early competence regulon | *Streptococcus pneumoniae* | “ComE~P induces the early competence regulon” (prudhomme2024pneumococcalcompetenceis pages 1-2) | Prudhomme et al. 2024, https://doi.org/10.1038/s41467-024-49853-2 | Strong pneumococcal regulatory edge. |
| ComE~P | induces | comABCDE genes | *Streptococcus pneumoniae* | “ComE~P induces the early competence regulon, which includes the comABCDE genes” (prudhomme2024pneumococcalcompetenceis pages 8-8) | Prudhomme et al. 2024, https://doi.org/10.1038/s41467-024-49853-2 | Strong positive-feedback edge in pneumococcus. |
| ComM | promotes | division delay | *Streptococcus pneumoniae* | “promotes a division delay in competent cells” (prudhomme2024pneumococcalcompetenceis pages 8-8) | Prudhomme et al. 2024, https://doi.org/10.1038/s41467-024-49853-2 | Strong pneumococcal physiological edge. |
| ComM | increases | antibiotic tolerance/survival | *Streptococcus pneumoniae* | “comM deletion abolishes or reduces tolerance; complementation restores it” and “with ComM key to increased survival” (prudhomme2024pneumococcalcompetenceis pages 8-8, prudhomme2024pneumococcalcompetenceis pages 7-8) | Prudhomme et al. 2024, https://doi.org/10.1038/s41467-024-49853-2 | Strong but stress-context dependent. |
| antibiotic stress | increases | competence self-induction | *Streptococcus pneumoniae* | “A self-induced subpopulation exists, and is increased upon antibiotic exposure” (prudhomme2024pneumococcalcompetenceis pages 5-6) | Prudhomme et al. 2024, https://doi.org/10.1038/s41467-024-49853-2 | Strong pneumococcal stress-response edge. |
| increased self-induced subpopulation | promotes | competence propagation in population | *Streptococcus pneumoniae* | “increased upon antibiotic exposure, leading to propagation of competence throughout a population” (prudhomme2024pneumococcalcompetenceis pages 5-6) | Prudhomme et al. 2024, https://doi.org/10.1038/s41467-024-49853-2 | Strong SI&P-model edge; pneumococcal context. |
| CcpA | represses | comX transcription | *Lactococcus lactis* | “CcpA directly represses PcomX in glucose conditions” (toussaint2024unveilingtheregulatory pages 9-13) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Strong lactococcal edge; not necessarily generalizable. |
| CodY | represses | comX transcription | *Lactococcus lactis* | “Nitrogen sensing via CodY represses comX” (toussaint2024unveilingtheregulatory pages 9-13) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Strong lactococcal edge. |
| CovRS / CovR | represses | comX transcription | *Lactococcus lactis* | “The transcription of comX... is repressed by three regulators... CcpA and CodY... or stress conditions (CovRS...)” (toussaint2024unveilingtheregulatory pages 39-41) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Strong lactococcal edge. |
| CovR | binds | PcomX promoter region | *Lactococcus lactis* | “CovR directly interacts with the comX promoter region” and “EMSA... on PcomX” (toussaint2024unveilingtheregulatory pages 39-41) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Strong direct regulatory edge. |
| MecA-ClpCP proteolytic machinery | degrades | ComX | *Lactococcus lactis* | “ComX can interact with the adaptor protein MecA ... for its degradation by the ClpCP machinery” (toussaint2024unveilingtheregulatory pages 39-41) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Strong post-translational repression edge. |
| glucose starvation plus maltose / diauxic shift | increases | comX expression | *Lactococcus lactis* | “A diauxic shift from glucose to maltose activates comX expression and transformability” (toussaint2024unveilingtheregulatory pages 16-19) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Strong but species-specific environmental regulation. |
| diauxic shift | increases | transformability | *Lactococcus lactis* | “transformation events occurred at the diauxic shift” (toussaint2024unveilingtheregulatory pages 9-13) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Species-specific assay-context edge. |
| excess isoleucine | decreases | comX expression | *Lactococcus lactis* | “excess isoleucine decreases comX and transformation” (toussaint2024unveilingtheregulatory pages 9-13) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Strong nutrient-response edge. |
| excess isoleucine | decreases | transformability | *Lactococcus lactis* | “excess isoleucine represses comX and transformation” (toussaint2024unveilingtheregulatory pages 16-19) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Species-specific nutrient-response edge. |
| low pH | decreases | transformability | *Lactococcus lactis* | “wild-type transformation abolished below pH 6.6” (toussaint2024unveilingtheregulatory pages 9-13) | Toussaint et al. 2024 preprint, https://doi.org/10.1101/2024.02.08.579460 | Strong species-specific environmental edge. |
| mobile genetic elements (MGEs) | decrease | transformability | *Legionella pneumophila* and *Acinetobacter baumannii* population study | “negative associations between transformation and MGEs” and “some MGEs inactivate genes involved in transformation” (mazzamurro2024intragenomicconflictswith pages 1-2) | Mazzamurro et al. 2024, https://doi.org/10.1371/journal.pbio.3002814 | Strong association/evolutionary edge; causality partly inferred except where gene disruption shown. |
| transformable strains | have_fewer | MGEs | *L. pneumophila* and *A. baumannii* | “transformable strains harbor fewer mobile genetic elements (MGEs)” (mazzamurro2024intragenomicconflictswith pages 1-2) | Mazzamurro et al. 2024, https://doi.org/10.1371/journal.pbio.3002814 | Association, not direct mechanism; curate as statistical/evolutionary relationship. |
| standard laboratory conditions | associated_with | ~half of *L. pneumophila* strains non-transformable | *Legionella pneumophila* | “nearly half of L. pneumophila strains... fall below the detection limit and are thus considered likely non-transformable” (mazzamurro2024intragenomicconflictswith pages 1-2) | Mazzamurro et al. 2024, https://doi.org/10.1371/journal.pbio.3002814 | Statistical observation, not mechanistic edge; useful assay-context warning. |
| standard laboratory conditions | associated_with | >1/3 of *A. baumannii* strains non-transformable | *Acinetobacter baumannii* | “over one-third of A. baumannii strains fall below the detection limit and are thus considered likely non-transformable” (mazzamurro2024intragenomicconflictswith pages 1-2) | Mazzamurro et al. 2024, https://doi.org/10.1371/journal.pbio.3002814 | Statistical observation, not mechanistic edge; useful assay-context warning. |


*Table: This table lists evidence-backed candidate subject-predicate-object edges for curating a TraitMech causal graph of natural competence. It combines core uptake machinery, regulatory control, environmental modulation, and recent population-scale observations, with direct snippets and uncertainty notes.*

---

### Expert opinions and analysis (authoritative synthesis)
- A 2024 Microbiology and Molecular Biology Reviews article (ASM; **Mar 2024**, doi: **10.1128/mmbr.00125-23**) synthesizes a contemporary consensus model in which competence pili are dynamic, DNA-binding structures and pilus retraction is mechanistically coupled to DNA delivery to the uptake apparatus. (zuke2024fromisotopicallylabeled pages 9-12, zuke2024fromisotopicallylabeled media 57140c68)
- A 2024 PLOS Biology study (doi: **10.1371/journal.pbio.3002814**) argues (using population-scale quantitative data) that transformability evolves rapidly within species and that **intragenomic conflicts** with MGEs can drive repeated losses of transformability, implying competence is under variable selection and often conditional. (mazzamurro2024intragenomicconflictswith pages 1-2)
- A 2024 Nature Communications study (doi: **10.1038/s41467-024-49853-2**) interprets pneumococcal competence as a **stress-sensing population decision system** (SI&P) rather than a purely density-threshold, synchronous quorum-sensing switch, with downstream physiological consequences (e.g., ComM-linked survival/tolerance heterogeneity). (prudhomme2024pneumococcalcompetenceis pages 1-2, prudhomme2024pneumococcalcompetenceis pages 8-8)

---

### Ontology grounding notes (CURIE suggestions)
- **GO:0030420** (natural transformation) can represent the core process/trait in GO. (artifact-00)
- ENVO terms (e.g., environmental DNA, pH, nutrient limitation) are appropriate where the environment is modeled explicitly; however, several factors here are **assay conditions** rather than natural habitat descriptors (e.g., “CDM*-DEB medium,” synthetic CSP/XIP additions). (toussaint2024unveilingtheregulatory pages 6-9, prudhomme2024pneumococcalcompetenceis pages 2-3)
- CHEBI groundings are appropriate for small molecules explicitly evidenced (e.g., maltose, isoleucine); peptide pheromones (CSP/XIP) may not have stable CHEBI entries in this evidence set and should be left ungrounded unless verified. (toussaint2024unveilingtheregulatory pages 9-13, marli2024geneticmodificationof pages 2-5)

---

### Warnings / claims that may be premature for TraitMech curation
1) **Condition dependence and assay bias:** “Non-transformable” classification is often **condition-specific** (below detection in “standard conditions” does not imply absolute inability). Curate edges linking environment/assay conditions to competence state to avoid overgeneralization. (mazzamurro2024intragenomicconflictswith pages 1-2)
2) **Taxon specificity of regulatory architectures:** Pneumococcal ComABCDE/CSP signaling and lactococcal CcpA/CodY/CovRS control of comX are well supported but should be represented as **taxon-scoped subgraphs** rather than universal competence regulation. (prudhomme2024pneumococcalcompetenceis pages 1-2, toussaint2024unveilingtheregulatory pages 1-6)
3) **Preprint-only mechanistic entities:** The YraN–ComM nuclease/helicase model is promising but currently supported by a 2024 preprint; flag as **uncertain/provisional** until peer-reviewed validation and broader taxonomic confirmation. (hardy2024yranisa pages 22-24)
4) **Secondary-synthesis snippets without primary DOI in retrieved metadata:** Some strong mechanistic statements are currently supported here via synthesis text (e.g., Zuke 2024 competence pili document without clear journal/DOI in retrieved metadata). For final TraitMech commits, trace these edges back to the primary experimental papers where possible. (zuke2024productiondynamicsand pages 23-28, zuke2024productiondynamicsand pages 158-161)

---

## DOI-first bibliography (prioritized 2024 sources; publication dates and URLs)
1) Zuke JD, Burton BM. **From isotopically labeled DNA to fluorescently labeled dynamic pili: building a mechanistic model of DNA transport to the cytoplasmic membrane.** *Microbiology and Molecular Biology Reviews*. **Mar 2024**. DOI: **10.1128/mmbr.00125-23**. URL: https://doi.org/10.1128/mmbr.00125-23 (zuke2024fromisotopicallylabeled pages 9-12)
2) Mazzamurro F, et al. **Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species.** *PLOS Biology*. **Oct 2024**. DOI: **10.1371/journal.pbio.3002814**. URL: https://doi.org/10.1371/journal.pbio.3002814 (mazzamurro2024intragenomicconflictswith pages 1-2)
3) Prudhomme M, et al. **Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics.** *Nature Communications*. **Jul 2024**. DOI: **10.1038/s41467-024-49853-2**. URL: https://doi.org/10.1038/s41467-024-49853-2 (prudhomme2024pneumococcalcompetenceis pages 1-2)
4) Toussaint F, et al. **Unveiling the regulatory network controlling natural transformation in lactococci.** bioRxiv preprint deposited **Feb 2024** (publisher listed as Cold Spring Harbor Laboratory in retrieved metadata). DOI: **10.1101/2024.02.08.579460**. URL: https://doi.org/10.1101/2024.02.08.579460 (toussaint2024unveilingtheregulatory pages 1-6)
5) Mårli MT, et al. **Genetic modification of *Streptococcus dysgalactiae* by natural transformation.** *mSphere*. **Jul 2024**. DOI: **10.1128/msphere.00214-24**. URL: https://doi.org/10.1128/msphere.00214-24 (marli2024geneticmodificationof pages 1-2)
6) Hardy L, et al. **YraN is a helicase-associated nuclease fostering extended recombination events by natural transformation.** bioRxiv preprint deposited **Feb 2024**. DOI: **10.1101/2024.02.06.579203**. URL: https://doi.org/10.1101/2024.02.06.579203 (hardy2024yranisa pages 22-24)

Additional (contextual, implementation-oriented) source retrieved:
- Stukenberg D. **Establishing the fast-growing bacterium *Vibrio natriegens* as a next-generation chassis for synthetic biology.** **May 2024**. DOI: **10.17192/z2024.0096**. URL: https://doi.org/10.17192/z2024.0096 (stukenberg2024establishingthefastgrowing pages 38-39)


References

1. (mazzamurro2024intragenomicconflictswith pages 1-2): Fanny Mazzamurro, Jason Baby Chirakadavil, Isabelle Durieux, Ludovic Poiré, Julie Plantade, Christophe Ginevra, Sophie Jarraud, Gottfried Wilharm, Xavier Charpentier, and Eduardo P. C. Rocha. Intragenomic conflicts with plasmids and chromosomal mobile genetic elements drive the evolution of natural transformation within species. PLOS Biology, 22:e3002814, Oct 2024. URL: https://doi.org/10.1371/journal.pbio.3002814, doi:10.1371/journal.pbio.3002814. This article has 21 citations and is from a highest quality peer-reviewed journal.

2. (zuke2024productiondynamicsand pages 56-60): JD Zuke. Production, dynamics, and dna binding capabilities of bacillus subtilis natural competence associated pili. Unknown journal, 2024.

3. (prudhomme2024pneumococcalcompetenceis pages 1-2): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 17 citations and is from a highest quality peer-reviewed journal.

4. (toussaint2024unveilingtheregulatory pages 6-9): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 5 citations and is from a domain leading peer-reviewed journal.

5. (zuke2024fromisotopicallylabeled pages 9-12): Jason D. Zuke and Briana M. Burton. From isotopically labeled dna to fluorescently labeled dynamic pili: building a mechanistic model of dna transport to the cytoplasmic membrane. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00125-23, doi:10.1128/mmbr.00125-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

6. (zuke2024fromisotopicallylabeled media 57140c68): Jason D. Zuke and Briana M. Burton. From isotopically labeled dna to fluorescently labeled dynamic pili: building a mechanistic model of dna transport to the cytoplasmic membrane. Microbiology and Molecular Biology Reviews, Mar 2024. URL: https://doi.org/10.1128/mmbr.00125-23, doi:10.1128/mmbr.00125-23. This article has 4 citations and is from a domain leading peer-reviewed journal.

7. (hardy2024yranisa pages 22-24): Léo Hardy, Julie Plantade, Violette Morales, Fanny Mazzamuro, Eduardo P. C. Rocha, Patrice Polard, and Xavier Charpentier. Yran is a helicase-associated nuclease fostering extended recombination events by natural transformation. bioRxiv, Feb 2024. URL: https://doi.org/10.1101/2024.02.06.579203, doi:10.1101/2024.02.06.579203. This article has 4 citations.

8. (zuke2024productiondynamicsand pages 158-161): JD Zuke. Production, dynamics, and dna binding capabilities of bacillus subtilis natural competence associated pili. Unknown journal, 2024.

9. (zuke2024productiondynamicsand pages 34-38): JD Zuke. Production, dynamics, and dna binding capabilities of bacillus subtilis natural competence associated pili. Unknown journal, 2024.

10. (zuke2024productiondynamicsand pages 23-28): JD Zuke. Production, dynamics, and dna binding capabilities of bacillus subtilis natural competence associated pili. Unknown journal, 2024.

11. (prudhomme2024pneumococcalcompetenceis pages 8-8): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 17 citations and is from a highest quality peer-reviewed journal.

12. (prudhomme2024pneumococcalcompetenceis pages 2-3): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 17 citations and is from a highest quality peer-reviewed journal.

13. (prudhomme2024pneumococcalcompetenceis pages 5-6): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 17 citations and is from a highest quality peer-reviewed journal.

14. (prudhomme2024pneumococcalcompetenceis pages 7-8): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 17 citations and is from a highest quality peer-reviewed journal.

15. (toussaint2024unveilingtheregulatory pages 1-6): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 5 citations and is from a domain leading peer-reviewed journal.

16. (toussaint2024unveilingtheregulatory pages 39-41): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 5 citations and is from a domain leading peer-reviewed journal.

17. (toussaint2024unveilingtheregulatory pages 16-19): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 5 citations and is from a domain leading peer-reviewed journal.

18. (toussaint2024unveilingtheregulatory pages 9-13): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 5 citations and is from a domain leading peer-reviewed journal.

19. (marli2024geneticmodificationof pages 1-2): Marita Torrissen Mårli, Oddvar Oppegaard, Davide Porcellato, Daniel Straume, and Morten Kjos. Genetic modification of <i>streptococcus dysgalactiae</i> by natural transformation. Jul 2024. URL: https://doi.org/10.1128/msphere.00214-24, doi:10.1128/msphere.00214-24. This article has 5 citations and is from a peer-reviewed journal.

20. (stukenberg2024establishingthefastgrowing pages 38-39): Daniel Stukenberg. Establishing the fast-growing bacterium vibrio natriegens as a next-generation chassis for synthetic biology. Text, May 2024. URL: https://doi.org/10.17192/z2024.0096, doi:10.17192/z2024.0096. This article has 0 citations and is from a peer-reviewed journal.

21. (prudhomme2024pneumococcalcompetenceis pages 9-10): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 17 citations and is from a highest quality peer-reviewed journal.

22. (marli2024geneticmodificationof pages 2-5): Marita Torrissen Mårli, Oddvar Oppegaard, Davide Porcellato, Daniel Straume, and Morten Kjos. Genetic modification of <i>streptococcus dysgalactiae</i> by natural transformation. Jul 2024. URL: https://doi.org/10.1128/msphere.00214-24, doi:10.1128/msphere.00214-24. This article has 5 citations and is from a peer-reviewed journal.

23. (zuke2024productiondynamicsand pages 161-163): JD Zuke. Production, dynamics, and dna binding capabilities of bacillus subtilis natural competence associated pili. Unknown journal, 2024.

24. (prudhomme2024pneumococcalcompetenceis pages 12-13): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 17 citations and is from a highest quality peer-reviewed journal.

25. (prudhomme2024pneumococcalcompetenceis pages 13-14): Marc Prudhomme, Calum H. G. Johnston, Anne-Lise Soulet, Anne Boyeldieu, David De Lemos, Nathalie Campo, and Patrice Polard. Pneumococcal competence is a populational health sensor driving multilevel heterogeneity in response to antibiotics. Nature Communications, Jul 2024. URL: https://doi.org/10.1038/s41467-024-49853-2, doi:10.1038/s41467-024-49853-2. This article has 17 citations and is from a highest quality peer-reviewed journal.

26. (toussaint2024unveilingtheregulatory pages 13-16): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 5 citations and is from a domain leading peer-reviewed journal.

27. (toussaint2024unveilingtheregulatory pages 32-39): Frédéric Toussaint, Marie Henry de Frahan, Félix Poncelet, Jean-Marc Ladrière, Philippe Horvath, Christophe Fremaux, and Pascal Hols. Unveiling the regulatory network controlling natural transformation in lactococci. PLOS Genetics, Feb 2024. URL: https://doi.org/10.1101/2024.02.08.579460, doi:10.1101/2024.02.08.579460. This article has 5 citations and is from a domain leading peer-reviewed journal.