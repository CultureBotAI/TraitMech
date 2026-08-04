---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T00:34:20.250502'
end_time: '2026-06-30T01:03:49.163805'
duration_seconds: 1768.91
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: swarming motility
  trait_identifier: traitmech:000062
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: swarming_motility
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagella-dependent, multicellular surface motility in which cells
    move rapidly and coordinately across a surface, typically accompanied by hyperflagellation
    and secretion of a wetting surfactant.
  parent_traits: METPO:1000702
  synonyms: swarming
  evidence_summary: 'DOI:10.1038/nrmicro2405:  (Kearns, "A field guide to bacterial
    swarming motility", defines swarming via increased flagella per cell, surfactant
    secretion, and movement in multicellular groups.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey,
    "Bacterial motility on a surface", places swarming among the surface-motility
    modes of bacteria.)'
  causal_graph_summary: 'swarming_hyperflagellation_surfactant: 6 nodes, 6 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** swarming motility
- **METPO identifier:** traitmech:000062
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-dependent, multicellular surface motility in which cells move rapidly and coordinately across a surface, typically accompanied by hyperflagellation and secretion of a wetting surfactant.
- **Parent traits:** METPO:1000702
- **Synonyms:** swarming
- **Existing evidence:** DOI:10.1038/nrmicro2405:  (Kearns, "A field guide to bacterial swarming motility", defines swarming via increased flagella per cell, surfactant secretion, and movement in multicellular groups.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places swarming among the surface-motility modes of bacteria.)
- **Existing causal graph summary:** swarming_hyperflagellation_surfactant: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **swarming motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/swarming_motility.yaml`.

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
- **Trait label:** swarming motility
- **METPO identifier:** traitmech:000062
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-dependent, multicellular surface motility in which cells move rapidly and coordinately across a surface, typically accompanied by hyperflagellation and secretion of a wetting surfactant.
- **Parent traits:** METPO:1000702
- **Synonyms:** swarming
- **Existing evidence:** DOI:10.1038/nrmicro2405:  (Kearns, "A field guide to bacterial swarming motility", defines swarming via increased flagella per cell, surfactant secretion, and movement in multicellular groups.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places swarming among the surface-motility modes of bacteria.)
- **Existing causal graph summary:** swarming_hyperflagellation_surfactant: 6 nodes, 6 edges

## Research Objective

Research the microbial trait **swarming motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/swarming_motility.yaml`.

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


# Swarming Motility: Curation-Focused Research Report for TraitMech Causal Graph

## 1. Trait Scope Summary

**Swarming motility** (traitmech:000062) is a flagella-dependent, multicellular surface motility in which bacteria move rapidly and coordinately across semi-solid surfaces. It is distinguished from other surface motility modes (twitching, sliding, gliding) by its absolute requirement for functional flagella, its collective/multicellular nature, and its typical association with hyperflagellation and secretion of wetting surfactants (partridge2013swarmingflexibleroaming pages 1-2, partridge2022surveyingaswarm pages 5-7). Swarming occurs on semi-solid agar (typically 0.5–1.5% w/v) and requires sufficient surface hydration for flagella-driven propulsion (partridge2013swarmingflexibleroaming pages 2-4, partridge2022surveyingaswarm pages 3-5).

**Boundary cases and distinctions:**
- **Swimming** is individual, liquid-phase flagellar motility; swarming is collective and surface-associated (partridge2022surveyingaswarm pages 5-7).
- **Sliding** is passive, flagella-independent surface spreading driven by colony growth pressure and surfactant secretion (partridge2013swarmingflexibleroaming pages 5-6).
- **Twitching** is type IV pilus–dependent and does not require flagella.
- Species vary in swarming strategy: "robust swarmers" (e.g., *Proteus mirabilis*) display dramatic cell elongation and hyperflagellation on hard agar (≥1.5%), while "temperate swarmers" (e.g., *E. coli*, *Salmonella*) require softer agar (0.5–0.8%) and depend more on surfactant secretion (partridge2013swarmingflexibleroaming pages 4-5, partridge2013swarmingflexibleroaming pages 4-4).

---

## 2. Candidate Causal Graph Nodes

The following table groups all proposed nodes by type, with suggested ontology CURIEs and taxon scope.

| Node Label | Node Type | Suggested CURIE | Taxon Scope | Notes |
|---|---|---|---|---|
| FlhDC (FlhD4C2 master regulator complex) | gene/protein complex | label-only candidate | Proteus mirabilis; Enterobacterales; broad Gram-negative flagellar regulon | Class I/master regulator of flagellar gene hierarchy; central to swarmer differentiation and swarming-associated flagellar expression (yang2024unveilingthehidden pages 6-7, lee2015lossofflil pages 1-2) |
| FliA (sigma-28, σ28) | sigma factor protein | GO:0001130 | Broad bacteria; documented in Proteus mirabilis | Flagellar sigma factor activated downstream of FlhDC; drives class III flagellar/chemotaxis genes (yang2024unveilingthehidden pages 6-7, lee2015lossofflil pages 1-2) |
| FlgM | anti-sigma factor protein | label-only candidate | Broad bacteria | Anti-σ28 factor in class II regulon; included in canonical flagellar hierarchy linked to swarming competence (yang2024unveilingthehidden pages 6-7) |
| FliL | motor accessory protein | label-only candidate | Broad bacteria; especially Proteus mirabilis, Pseudomonas aeruginosa | Supports high-torque motor function and surface sensing; implicated in swarming and mechanosensory signaling (lee2015lossofflil pages 12-13, wu2024torquespeedrelationshipof pages 13-15) |
| FliC | flagellin | GO:0009288 | Broad bacteria | Major filament subunit; flagellar output required for swarming; loss perturbs surface sensing programs in P. aeruginosa (kuchma2025geneticanalysisof pages 1-2) |
| MotAB | stator complex | label-only candidate | Broad bacteria; especially Pseudomonas aeruginosa | Proton-driven stator; favors low-load swimming and can repress swarming in P. aeruginosa relative to MotCD (anda2024howp.aeruginosa pages 2-4, anda2024howp.aeruginosa pages 8-10, anda2024howp.aeruginosa pages 1-2) |
| MotCD | stator complex | label-only candidate | Pseudomonas aeruginosa and related dual-stator bacteria | High-load stator critical for swarming on surfaces; deletion abolishes swarming in P. aeruginosa (anda2024howp.aeruginosa pages 2-4, wu2024torquespeedrelationshipof pages 13-15, anda2024howp.aeruginosa pages 1-2) |
| FliG | rotor switch protein | label-only candidate | Broad bacteria; documented in Pseudomonas aeruginosa | Rotor/switch component transmitting stator torque; implicated in flagellar-mediated surface sensing circuitry (kuchma2025geneticanalysisof pages 1-2) |
| RhlA | enzyme | label-only candidate | Pseudomonas aeruginosa | Required for HAA production; key swarming-linked surfactant biosynthesis determinant (deziel2003rhlaisrequired pages 1-2, deziel2003rhlaisrequired pages 8-9) |
| RhlB | rhamnosyltransferase 1 | label-only candidate | Pseudomonas aeruginosa | Catalyzes mono-rhamnolipid synthesis with RhlA-derived substrates; part of rhlAB operon (kohler2000swarmingofpseudomonas pages 3-6, deziel2003rhlaisrequired pages 8-9) |
| RhlC | rhamnosyltransferase 2 | label-only candidate | Pseudomonas aeruginosa | Converts mono-rhamnolipids to dirhamnolipids; quorum-sensing-regulated surfactant pathway member (daniels2004quorumsensingand pages 8-11, deziel2003rhlaisrequired pages 8-9) |
| RhlI | autoinducer synthase | label-only candidate | Pseudomonas aeruginosa | Synthesizes C4-HSL; activates rhl quorum-sensing branch controlling swarming surfactants (daniels2004quorumsensingand pages 8-11, daniels2004quorumsensingand pages 11-12) |
| RhlR | transcriptional regulator | label-only candidate | Pseudomonas aeruginosa | C4-HSL-responsive QS activator controlling rhlAB/rhlC and swarming outputs (daniels2004quorumsensingand pages 8-11, daniels2004quorumsensingand pages 11-12) |
| LasI | autoinducer synthase | label-only candidate | Pseudomonas aeruginosa | Synthesizes 3-oxo-C12-HSL; upstream QS layer influencing swarming via rhl pathway (kohler2000swarmingofpseudomonas pages 3-6, kohler2000swarmingofpseudomonas pages 6-6) |
| LasR | transcriptional regulator | label-only candidate | Pseudomonas aeruginosa | QS activator in las system; las mutants show reduced/delayed swarming (kohler2000swarmingofpseudomonas pages 3-6, daniels2004quorumsensingand pages 8-11, kohler2000swarmingofpseudomonas pages 6-6) |
| SwrA | regulatory protein | label-only candidate | Bacillus subtilis | Swarming activator that cooperates with DegU~P to activate fla/che transcription (mordini2013theroleof pages 5-7, mordini2013theroleof pages 1-2) |
| DegU | response regulator | label-only candidate | Bacillus subtilis | Phosphorylated DegU acts as dual regulator; with SwrA it promotes motility regulon expression (mordini2013theroleof pages 5-7, mordini2013theroleof pages 2-3, mordini2013theroleof pages 9-10) |
| DegS | sensor histidine kinase | label-only candidate | Bacillus subtilis | Phosphorylates DegU, enabling SwrA-DegU~P control of fla/che and swarming (mordini2013theroleof pages 2-3, mordini2013theroleof pages 3-5) |
| DgcO | diguanylate cyclase | label-only candidate | Escherichia coli | Major DGC promoting swarming via colanic acid production; defines c-di-GMP threshold for swarming (hwang2025cdigmpisrequired pages 8-11, hwang2025cdigmpisrequired pages 2-5, hwang2025cdigmpisrequired pages 11-14) |
| DgcM | diguanylate cyclase | label-only candidate | Escherichia coli | Secondary DGC contributing to swarming-associated c-di-GMP signaling (hwang2025cdigmpisrequired pages 8-11, hwang2025cdigmpisrequired pages 11-14) |
| YcgR | c-di-GMP effector / flagellar brake | label-only candidate | Escherichia coli; Salmonella enterica | c-di-GMP receptor that slows/brakes flagellar motor and opposes motility at elevated c-di-GMP (partridge2013swarmingflexibleroaming pages 6-7, liu2022theeffectof pages 1-2) |
| YhjH (PdeH) | phosphodiesterase | label-only candidate | Escherichia coli; Salmonella enterica | Lowers c-di-GMP to preserve flagellar motility/swarming competence (partridge2013swarmingflexibleroaming pages 6-7) |
| SrfA operon (surfactin synthetase) | operon / NRPS system | label-only candidate | Bacillus subtilis | Biosynthetic locus for surfactin, a canonical swarming wetting agent in B. subtilis (partridge2022surveyingaswarm pages 5-7, mordini2013theroleof pages 1-2) |
| WcaJ | glycosyltransferase | label-only candidate | Escherichia coli | Initiates colanic acid biosynthesis; required for CA-dependent swarming in E. coli (hwang2025cdigmpisrequired pages 5-8, hwang2025cdigmpisrequired pages 11-14) |
| c-di-GMP (cyclic di-GMP) | chemical / second messenger | CHEBI:17950 | Broad bacteria | Central signaling molecule balancing swarming versus sessility; low/intermediate levels can support swarming, high levels inhibit motility and favor biofilm (partridge2013swarmingflexibleroaming pages 7-8, hwang2025cdigmpisrequired pages 1-2, liu2022theeffectof pages 1-2) |
| Surfactin | lipopeptide biosurfactant | CHEBI:29375 | Bacillus subtilis | Wetting agent essential or strongly supportive for B. subtilis swarming on standard media (daniels2004quorumsensingand pages 6-7, partridge2022surveyingaswarm pages 5-7) |
| Rhamnolipids | glycolipid biosurfactant | CHEBI:63748 | Pseudomonas aeruginosa | Canonical swarming surfactants; pathway and abundance modulate swarm expansion/patterning (kohler2000swarmingofpseudomonas pages 3-6, caiazza2005rhamnolipidsmodulateswarming pages 5-6) |
| HAAs (3-(3-hydroxyalkanoyloxy)alkanoic acids) | surfactant precursor metabolites | label-only candidate | Pseudomonas aeruginosa | RhlA-derived precursors that can themselves serve as minimal surfactants for swarming (caiazza2005rhamnolipidsmodulateswarming pages 5-6, deziel2003rhlaisrequired pages 1-2) |
| C4-HSL (N-butyryl-L-homoserine lactone) | quorum-sensing autoinducer | CHEBI:78425 | Pseudomonas aeruginosa | Autoinducer produced by RhlI; activates RhlR-dependent surfactant/swarming program (daniels2004quorumsensingand pages 8-11, kohler2000swarmingofpseudomonas pages 6-6) |
| 3-oxo-C12-HSL | quorum-sensing autoinducer | CHEBI:65033 | Pseudomonas aeruginosa | LasI/LasR signal upstream of rhl QS network affecting swarming (kohler2000swarmingofpseudomonas pages 3-6, kohler2000swarmingofpseudomonas pages 6-6) |
| Colanic acid | exopolysaccharide / surfactant | label-only candidate | Escherichia coli | Acts as surfactant and wetting agent enabling E. coli swarming under specific c-di-GMP conditions (hwang2025cdigmpisrequired pages 1-2, hwang2025cdigmpisrequired pages 5-8, hwang2025cdigmpisrequired pages 11-14) |
| PQS (Pseudomonas quinolone signal) | quorum-sensing signal molecule | CHEBI:134179 | Pseudomonas aeruginosa | Links las and rhl systems and can influence swarming-associated regulatory flow (daniels2004quorumsensingand pages 11-12) |
| Serrawettin | biosurfactant | label-only candidate | Serratia marcescens | Serratia wetting agent; useful comparative swarming surfactant node (partridge2022surveyingaswarm pages 5-7) |
| Swarming motility | biological process / trait | GO:0000331 | Broad bacteria | Target trait: flagella-dependent, multicellular surface translocation on semi-solid surfaces (partridge2013swarmingflexibleroaming pages 5-6, partridge2022surveyingaswarm pages 5-7) |
| Hyperflagellation | biological process | label-only candidate | Broad bacteria | Increased flagellar number is a common swarmer-cell adaptation in multiple taxa (partridge2013swarmingflexibleroaming pages 5-6, partridge2022surveyingaswarm pages 5-7) |
| Cell elongation (swarmer differentiation) | biological process | GO:0032989 | Especially Proteus mirabilis; also other robust swarmers | Surface-associated differentiation into elongated swarm cells (daniels2004quorumsensingand pages 6-7, lee2015lossofflil pages 1-2) |
| Surface sensing / mechanosensing | biological process | GO:0009593 | Broad bacteria | Flagellar load/surface contact sensing triggers swarming or biofilm-related responses (kuchma2025geneticanalysisof pages 1-2, lee2015lossofflil pages 12-13) |
| Quorum sensing | biological process | GO:0009372 | Broad bacteria | Cell-density signaling controlling surfactant and other swarm-related outputs (daniels2004quorumsensingand pages 6-7, daniels2004quorumsensingand pages 8-11) |
| Surfactant secretion | biological process | label-only candidate | Broad bacteria | Release of wetting agents such as rhamnolipids/surfactin/serrawettin to reduce surface tension (partridge2022surveyingaswarm pages 5-7, deziel2003rhlaisrequired pages 1-2) |
| Flagellar rotation / motor function | biological process | GO:0001539 | Broad bacteria | Torque generation and switching required for propulsion and surface adaptation (kuchma2025geneticanalysisof pages 1-2, lee2015lossofflil pages 12-13) |
| Chemotaxis signaling | biological process | GO:0006935 | Broad bacteria | Required or mechanically repurposed in some swarmers; part of class III regulon in enterics (partridge2013swarmingflexibleroaming pages 5-6, yang2024unveilingthehidden pages 6-7) |
| Biofilm formation | biological process | GO:0042710 | Broad bacteria | Often antagonistic to swarming; elevated c-di-GMP shifts cells toward biofilm (partridge2013swarmingflexibleroaming pages 7-8, liu2022theeffectof pages 1-2) |
| Semi-solid surface (agar 0.5-1.5%) | environmental factor | ENVO:00000105 | Assay/environmental condition | Canonical assay substrate; agar concentration strongly determines whether swarming occurs (partridge2013swarmingflexibleroaming pages 4-4, partridge2022surveyingaswarm pages 3-5) |
| Surface hydration / water availability | environmental factor | label-only candidate | Broad bacteria | Critical physical requirement for swarm expansion and flagellar propulsion on surfaces (yang2017influenceofphysical pages 6-8, partridge2013swarmingflexibleroaming pages 2-4) |
| Surface tension | environmental factor | label-only candidate | Broad bacteria | Barrier to colony spreading; reduced by secreted/exogenous surfactants (yang2017influenceofphysical pages 6-8, yang2017influenceofphysical pages 1-2) |
| Iron limitation | environmental factor | label-only candidate | Multiple taxa; documented in Pseudomonas | Reported cue influencing swarming and surfactant-linked regulation (deziel2003rhlaisrequired pages 1-2, partridge2022surveyingaswarm pages 5-7, partridge2013swarmingflexibleroaming pages 1-2) |
| Glucose availability | environmental factor / nutrient | CHEBI:17234 | Especially Escherichia coli, Salmonella enterica | Often required or stimulatory in swarming media; can bypass some regulatory defects in E. coli CA-dependent swarming (hwang2025cdigmpisrequired pages 5-8, partridge2022surveyingaswarm pages 5-7) |
| Phosphate starvation | environmental factor / nutrient limitation | label-only candidate | Pseudomonas aeruginosa | Reported trigger for swarming in P. aeruginosa assay conditions (partridge2022surveyingaswarm pages 5-7) |
| Temperature | environmental factor | PATO:0000146 | Broad bacteria | Standard swarming assays often at ~30°C; some regulators show temperature-dependent swarming phenotypes (partridge2022surveyingaswarm pages 3-5, lee2015lossofflil pages 1-2) |


*Table: This table lists candidate nodes for a swarming motility causal graph, grouped across molecular, process, and environmental categories. It is useful for TraitMech curation because it pairs each node with tentative ontology grounding, taxon scope, and evidence-backed notes.*

---

## 3. Mechanistic Overview and Evidence-Backed Causal Edges

### 3.1 Flagellar Gene Hierarchy

The flagellar regulon is organized in a three-tiered transcriptional hierarchy conserved across Gram-negative bacteria. The **FlhDC** (FlhD₄C₂) master regulator complex (class I) activates class II promoters, including *fliA* encoding the flagellar sigma factor σ²⁸ (FliA) and *flgM* encoding its anti-sigma factor (yang2024unveilingthehidden pages 6-7, lee2015lossofflil pages 1-2). FliA in turn activates class III genes encoding flagellin (FliC), stator complexes (MotAB), and chemotaxis components (yang2024unveilingthehidden pages 6-7). In *Proteus mirabilis*, FlhDC additionally drives swarmer cell differentiation, producing hyperflagellated, hyperelongated, multinucleated cells (daniels2004quorumsensingand pages 6-7).

### 3.2 Surfactant Production and Quorum Sensing

Surfactant secretion is essential or strongly supportive for swarming across species:

- **In *Pseudomonas aeruginosa*:** The Rhl quorum sensing (QS) system controls rhamnolipid biosynthesis. RhlI synthesizes C4-HSL, which activates RhlR, driving transcription of the *rhlAB* operon (kohler2000swarmingofpseudomonas pages 3-6, daniels2004quorumsensingand pages 8-11). RhlA produces HAAs (3-(3-hydroxyalkanoyloxy)alkanoic acids), which function as the minimal surfactants required for swarming even without full rhamnolipid production (deziel2003rhlaisrequired pages 1-2). The Las QS system (LasI/LasR) sits hierarchically upstream of the Rhl system, and PQS links the two (daniels2004quorumsensingand pages 8-11, daniels2004quorumsensingand pages 11-12). Rhamnolipids also serve as swarm-modulating signals, with excess rhamnolipid inhibiting swarming motility (caiazza2005rhamnolipidsmodulateswarming pages 5-6).

- **In *Bacillus subtilis*:** Surfactin, a lipopeptide biosurfactant produced by the SrfA NRPS system, is essential for swarming—*B. subtilis* is completely non-motile on surfaces without surfactin (partridge2013swarmingflexibleroaming pages 5-6, partridge2022surveyingaswarm pages 5-7). Surfactin production is linked to the ComQXPA QS system (daniels2004quorumsensingand pages 6-7).

- **In *E. coli*:** Colanic acid, an exopolysaccharide, was recently shown to function as a surfactant with wetting agent properties, enabling swarming (hwang2025cdigmpisrequired pages 1-2, hwang2025cdigmpisrequired pages 11-14). This is a novel 2025 finding from Hwang et al.

### 3.3 c-di-GMP Signaling

Cyclic-di-GMP is a central second messenger governing the swarming–biofilm switch. Low c-di-GMP levels promote flagellar motility, while elevated c-di-GMP inhibits motility and promotes biofilm formation (partridge2013swarmingflexibleroaming pages 7-8, partridge2013swarmingflexibleroaming pages 6-7). The phosphodiesterase YhjH (PdeH) maintains low c-di-GMP to sustain swarming competence (partridge2013swarmingflexibleroaming pages 6-7). At elevated concentrations, c-di-GMP binds the effector protein YcgR, which acts as a "backstop brake" on the flagellar motor by inducing CCW bias and reducing motor speed (partridge2013swarmingflexibleroaming pages 6-7, liu2022theeffectof pages 1-2).

A groundbreaking finding from Hwang et al. (2025) demonstrated that, contrary to the simple inhibitory model, a threshold level of c-di-GMP is actually *required* for swarming in *E. coli*. The diguanylate cyclase DgcO is the major enzyme producing this threshold c-di-GMP, which specifically drives colanic acid (CA) synthesis via the *wca* operon. DgcO expression is upregulated 3–8 fold during swarming. The auto-inhibitory sites on swarming-associated DGCs help maintain c-di-GMP at a "sweet spot"—sufficient to produce surfactant polysaccharides but below the level that activates YcgR-mediated motor braking or biofilm programs (hwang2025cdigmpisrequired pages 8-11, hwang2025cdigmpisrequired pages 1-2, hwang2025cdigmpisrequired pages 2-5).

### 3.4 Stator Proteins and Motor Mechanics

In *P. aeruginosa*, the flagellar motor contains two stator systems: MotAB (dominant in low-viscosity swimming) and MotCD (essential for high-load swarming). MotAB is produced at ~40-fold higher levels but MotCD stators generate higher torque under high-load conditions and cells with MotCD are ~10× more likely to have active motors (anda2024howp.aeruginosa pages 2-4, anda2024howp.aeruginosa pages 1-2). Deletion of MotCD eliminates swarming, while deletion of MotAB enhances it (anda2024howp.aeruginosa pages 8-10). The accessory protein FliL functions as a "molecular governor" regulating proton flow through stators during high-torque conditions, providing structural reinforcement essential for surface motility (lee2015lossofflil pages 12-13, wu2024torquespeedrelationshipof pages 13-15).

### 3.5 Surface Mechanosensing

The flagellar motor functions as a mechanosensor. When bacteria contact a surface, inhibition of flagellar rotation is detected through changes in mechanical load on stator proteins, triggering signaling cascades (lee2015lossofflil pages 1-2, kuchma2025geneticanalysisof pages 1-2). In *P. aeruginosa*, stator-mediated surface sensing stimulates c-di-GMP production via diguanylate cyclases SadC and RoeA, linking flagellar function to biofilm initiation (kuchma2025geneticanalysisof pages 1-2). In *P. mirabilis*, surface contact signals through the Umo proteins (UmoA, UmoD) and Rcs pathway to increase FlhDC expression and trigger swarmer cell differentiation (lee2015lossofflil pages 12-13).

### 3.6 Species-Specific Regulatory Modules

In *B. subtilis*, the SwrA protein cooperates with phosphorylated DegU (DegU~P) to activate the *fla/che* operon at its σᴬ-dependent promoter PA(*fla/che*). SwrA lacks a DNA-binding domain but forms a complex with DegU~P on the promoter, converting DegU~P from a repressor into an activator of flagellar gene transcription (mordini2013theroleof pages 5-7, mordini2013theroleof pages 2-3, mordini2013theroleof pages 9-10). DegS kinase phosphorylates DegU, and the level of phosphorylation determines the outcome: with SwrA present, even high DegU phosphorylation supports motility; without SwrA, DegU~P represses flagellar genes (mordini2013theroleof pages 1-2).

### 3.7 Environmental and Experimental Factors

Multiple environmental factors modulate swarming:
- **Agar concentration** is the primary experimental determinant; increasing agar percentage increases surface friction and decreases water permeability, reducing swarming (yang2017influenceofphysical pages 6-8, yang2017influenceofphysical pages 1-2, yang2017influenceofphysical pages 3-4).
- **Surface hydration** is critical; water supply rate from the agar gel limits swarm growth (yang2017influenceofphysical pages 6-8, partridge2013swarmingflexibleroaming pages 2-4).
- **Osmolarity** negatively affects swarming; NaCl or sucrose additions decrease swarm area (yang2017influenceofphysical pages 3-4). Bacteria counter this by producing osmolytes (glutamate, proline) to attract water (partridge2013swarmingflexibleroaming pages 4-4).
- **Iron limitation** and **phosphate starvation** serve as swarming-triggering cues in some species (deziel2003rhlaisrequired pages 1-2, partridge2022surveyingaswarm pages 5-7, partridge2013swarmingflexibleroaming pages 1-2).
- **Glucose** supplementation is required for swarming in *E. coli* and *Salmonella*; glucose can also stimulate the Rcs regulon controlling colanic acid synthesis (hwang2025cdigmpisrequired pages 5-8, partridge2022surveyingaswarm pages 5-7).
- **Temperature** affects swarming; standard assays are typically at ~30°C, and some regulators show temperature-dependent swarming phenotypes (partridge2022surveyingaswarm pages 3-5, lee2015lossofflil pages 1-2).

---

## 4. Candidate Causal Edges Table

The following table presents 26 evidence-backed causal edges for the swarming motility graph, each with DOI reference, supporting snippet, and confidence assessment.

| Edge # | Subject | Predicate | Object | Reference (DOI) | Supporting Snippet | Notes/Confidence |
|---|---|---|---|---|---|---|
| 1 | FlhDC (FlhD4C2) | activates | FliA (σ28) transcription | DOI:10.3389/fcimb.2024.1465460 | "FlhD4C2 activates class 2 promoters that transcribe fliA" (yang2024unveilingthehidden pages 6-7) | Core flagellar hierarchy; strong, broadly conserved in enterics |
| 2 | FliA (σ28) | activates | class III flagellar genes (flagellin, chemotaxis, stators) | DOI:10.3389/fcimb.2024.1465460 | "FliA then activates class 3 promoters for genes necessary for flagellum production, stator complexes, and chemotaxis" (yang2024unveilingthehidden pages 6-7) | Core hierarchy; strong |
| 3 | Surface contact | inhibits, triggering | flagellar rotation, swarmer cell differentiation | DOI:10.1128/jb.02235-14 | "swarmer cell differentiation occurs when swimmer cells encounter a solid surface and experience inhibition of flagellar rotation" (lee2015lossofflil pages 1-2) | Mechanosensory trigger; strong for Proteus mirabilis |
| 4 | FlhDC | promotes | hyperflagellation | DOI:10.1128/jb.02063-12 | "some bacteria increase flagellar numbers genetically" (partridge2013swarmingflexibleroaming pages 4-5, partridge2013swarmingflexibleroaming pages 1-2) | Broad review support; mechanistically inferred to pass through master regulon; medium confidence |
| 5 | FlhDC | promotes | cell elongation (via cell division inhibition) | DOI:10.1016/j.femsre.2003.09.004 | "The flhDC master operon regulates swarmer cell differentiation... producing hyperflagellated, elongated, multinucleated cells" (daniels2004quorumsensingand pages 6-7) | Proteus-centric and differentiation-linked; strong but taxon-specific |
| 6 | RhlI | produces | C4-HSL | DOI:10.1128/jb.182.21.5990-5996.2000 | "The rhlAB operon is regulated by a quorum sensing system composed of rhlI (encoding N-butyrylhomoserine lactone autoinducer synthase)" (deziel2003rhlaisrequired pages 1-2) | P. aeruginosa QS; strong |
| 7 | C4-HSL + RhlR | activates | rhlAB transcription | DOI:10.1128/jb.182.21.5990-5996.2000 | "the rhl cell-to-cell signaling system controls rhamnolipid production by regulating transcription of the rhlAB operon" (kohler2000swarmingofpseudomonas pages 3-6) | P. aeruginosa; strong |
| 8 | RhlA | produces | HAAs (surfactant precursors) | DOI:10.1099/mic.0.26154-0 | "rhlA is required to produce HAAs—the precursors of rhamnolipids—which function as potent surface-active compounds" (deziel2003rhlaisrequired pages 1-2) | P. aeruginosa; strong |
| 9 | HAAs / rhamnolipids | reduces, enabling | surface tension, swarming motility | DOI:10.1099/mic.0.26154-0; DOI:10.1128/jb.187.21.7351-7361.2005 | "HAAs themselves serve as surfactants"; "These data suggest HAAs are the minimal surfactant required for swarming in P. aeruginosa" (deziel2003rhlaisrequired pages 1-2, caiazza2005rhamnolipidsmodulateswarming pages 5-6) | Strong for P. aeruginosa; surfactant chemistry central |
| 10 | LasI/LasR | activates | rhl quorum-sensing system | DOI:10.1016/j.femsre.2003.09.004 | "The las and rhl systems form a hierarchical regulatory circuit"; "las system can mildly activate rhlA expression" (daniels2004quorumsensingand pages 8-11) | P. aeruginosa QS cascade; strong |
| 11 | SwrA + DegU~P | activates | fla/che operon (PA promoter) | DOI:10.1371/journal.pone.0085065 | "SwrA forms a complex with DegU~P at PA(fla/che)" and acts as "a positive stimulator of fla/che transcription" (mordini2013theroleof pages 5-7, mordini2013theroleof pages 7-9) | B. subtilis specific; strong |
| 12 | DegS | phosphorylates | DegU | DOI:10.1371/journal.pone.0085065 | "DegU undergoes phosphorylation by DegS kinase" (mordini2013theroleof pages 2-3) | B. subtilis; strong |
| 13 | DgcO | synthesizes/promotes | c-di-GMP threshold, colanic acid production | DOI:10.1128/mbio.00916-25 | "DgcO is the major DGC promoting swarming" and "specifically promotes colanic acid synthesis" (hwang2025cdigmpisrequired pages 8-11, hwang2025cdigmpisrequired pages 11-14) | E. coli; recent 2025; strong but taxon-specific |
| 14 | Colanic acid | acts as, enabling | surfactant, swarming | DOI:10.1128/mbio.00916-25 | "colanic acid has hitherto-unknown surfactant properties that are expected to aid swarming" (hwang2025cdigmpisrequired pages 1-2) | E. coli; novel 2025 finding; strong but recent/single-study |
| 15 | YcgR + c-di-GMP (high) | brakes | flagellar motor | DOI:10.1128/jb.02063-12 | "YcgR::c-di-GMP complex directly binds flagellar motor components to induce counter-clockwise bias and slow motor rotation" (partridge2013swarmingflexibleroaming pages 6-7) | E. coli/Salmonella; strong |
| 16 | YhjH (PdeH) | degrades/permits | c-di-GMP, swarming | DOI:10.1128/jb.02063-12 | "the phosphodiesterase YhjH is required to keep c-di-GMP levels low during swarming" (partridge2013swarmingflexibleroaming pages 6-7) | E. coli/Salmonella; strong |
| 17 | MotCD | provides/enables | high-load torque, swarming | DOI:10.1128/mbio.03322-23 | "Deletion of MotCD eliminates swarming" and "MotCD stators are preferred during swarming" (anda2024howp.aeruginosa pages 1-2, anda2024howp.aeruginosa pages 8-10) | P. aeruginosa; strong |
| 18 | MotAB | inhibits/attenuates | swarming | DOI:10.1128/mbio.03322-23 | "deletion of the MotAB stator enhances swarming" (anda2024howp.aeruginosa pages 8-10) | P. aeruginosa; strong |
| 19 | FliL | supports/enables | motor function under high load, swarming | DOI:10.1128/jb.02235-14 | "FliL is proposed to function as a molecular governor that regulates proton flow through the stator during high-torque conditions" (lee2015lossofflil pages 12-13) | P. mirabilis with broader relevance; medium-high confidence |
| 20 | Surfactin (SrfA) | reduces/enables | surface tension, swarming | DOI:10.1128/jb.02063-12 | "B. subtilis completely nonmotile without surfactin" (partridge2013swarmingflexibleroaming pages 5-6) | B. subtilis; strong phenotype support |
| 21 | Agar concentration | modulates | swarming difficulty | DOI:10.1016/j.bpj.2017.02.019 | "increasing agar percentage decreases swarming" (yang2017influenceofphysical pages 3-4, yang2017influenceofphysical pages 1-2) | Experimental factor; strong |
| 22 | Water availability | required for | swarming | DOI:10.1016/j.bpj.2017.02.019 | "water supply rate from the agar gel limits swarm growth" (yang2017influenceofphysical pages 1-2) | Physical requirement; strong |
| 23 | Quorum sensing | regulates/enables | surfactant production, swarming | DOI:10.1016/j.femsre.2003.09.004 | "QS systems integrated into regulatory networks controlling biosurfactant production and other swarming genes" (daniels2004quorumsensingand pages 6-7, daniels2004quorumsensingand pages 8-11) | Broadly conserved concept; strong review support |
| 24 | Elevated c-di-GMP | promotes/inhibits | biofilm formation, swarming | DOI:10.1128/jb.02063-12 | "low levels promoting motility while high levels inhibit it and promote biofilm formation" (partridge2013swarmingflexibleroaming pages 7-8, partridge2013swarmingflexibleroaming pages 6-7) | Broadly conserved; strong |
| 25 | Flagellar motor | senses/triggers | surface contact, c-di-GMP signaling | DOI:10.1128/jb.00520-24 | "MotAB and MotCD stators play key roles in stimulating c-di-GMP signaling upon surface contact" (kuchma2025geneticanalysisof pages 1-2) | P. aeruginosa; recent 2025; strong |
| 26 | PQS | links | las system to rhl system | DOI:10.1016/j.femsre.2003.09.004 | "PQS acts as a link between the las and rhl systems by transcriptionally regulating rhlI" (daniels2004quorumsensingand pages 11-12) | P. aeruginosa; strong |


*Table: This table lists candidate causal edges for curating a swarming motility TraitMech graph, with DOI-linked support snippets and confidence notes. It emphasizes mechanistic relationships spanning flagellar hierarchy, surfactants, quorum sensing, c-di-GMP signaling, stator function, and environmental factors.*

---

## 5. DOI-First Bibliography

1. Partridge JD, Harshey RM. "Swarming: Flexible Roaming Plans." *J Bacteriol*. 2013;195:909–918. DOI:10.1128/jb.02063-12
2. Daniels R, Vanderleyden J, Michiels J. "Quorum sensing and swarming migration in bacteria." *FEMS Microbiol Rev*. 2004;28(3):261–289. DOI:10.1016/j.femsre.2003.09.004
3. Köhler T et al. "Swarming of *Pseudomonas aeruginosa* is dependent on cell-to-cell signaling and requires flagella and pili." *J Bacteriol*. 2000;182:5990–5996. DOI:10.1128/jb.182.21.5990-5996.2000
4. Caiazza NC, Shanks RMQ, O'Toole GA. "Rhamnolipids modulate swarming motility patterns of *Pseudomonas aeruginosa*." *J Bacteriol*. 2005;187:7351–7361. DOI:10.1128/jb.187.21.7351-7361.2005
5. Déziel E et al. "*rhlA* is required for the production of a novel biosurfactant promoting swarming motility in *Pseudomonas aeruginosa*." *Microbiology*. 2003;149:2005–2013. DOI:10.1099/mic.0.26154-0
6. Mordini S et al. "The role of SwrA, DegU and PD3 in *fla/che* expression in *B. subtilis*." *PLoS ONE*. 2013;8:e85065. DOI:10.1371/journal.pone.0085065
7. Hwang Y et al. "c-di-GMP is required for swarming in *E. coli*, producing colanic acid that acts as surfactant." *mBio*. 2025;16(6). DOI:10.1128/mbio.00916-25
8. de Anda J et al. "How *P. aeruginosa* cells with diverse stator composition collectively swarm." *mBio*. 2024;15(4). DOI:10.1128/mbio.03322-23
9. Kuchma SL et al. "Genetic analysis of flagellar-mediated surface sensing by *Pseudomonas aeruginosa* PA14." *J Bacteriol*. 2025;207(7). DOI:10.1128/jb.00520-24
10. Lee Y-Y, Belas R. "Loss of FliL alters *Proteus mirabilis* surface sensing and temperature-dependent swarming." *J Bacteriol*. 2015;197:159–173. DOI:10.1128/jb.02235-14
11. Yang A et al. "Influence of physical effects on the swarming motility of *Pseudomonas aeruginosa*." *Biophys J*. 2017;112(7):1462–1471. DOI:10.1016/j.bpj.2017.02.019
12. Partridge JD. "Surveying a swarm: Experimental techniques to establish and examine bacterial collective motion." *Appl Environ Microbiol*. 2022;88(3). DOI:10.1128/aem.01853-21
13. Wu H et al. "Torque-speed relationship of the flagellar motor with dual-stator systems in *Pseudomonas aeruginosa*." *mBio*. 2024;15(12). DOI:10.1128/mbio.00745-24
14. Yang A et al. "Unveiling the hidden arsenal: new insights into *Proteus mirabilis* virulence in UTIs." *Front Cell Infect Microbiol*. 2024;14. DOI:10.3389/fcimb.2024.1465460
15. Liu X et al. "The effect of the second messenger c-di-GMP on bacterial chemotaxis in *Escherichia coli*." *Appl Environ Microbiol*. 2022;88(9). DOI:10.1128/aem.00373-22
16. Bru J-L et al. "Swarming of *P. aeruginosa*: Through the lens of biophysics." *Biophys Rev*. 2023;4(3). DOI:10.1063/5.0128140
17. Rütschlin S, Böttcher T. "Inhibitors of bacterial swarming behavior." *Chemistry*. 2020;26:964–979. DOI:10.1002/chem.201901961
18. Warrell DL et al. "Interspecies surfactants serve as public goods enabling surface motility in *Pseudomonas aeruginosa*." *J Bacteriol*. 2024;206(10). DOI:10.1128/jb.00281-24

---

## 6. Warnings for TraitMech Curation

1. **Taxon specificity:** Many edges are species-specific. The MotCD stator requirement (edges 17–18) is specific to *P. aeruginosa* and dual-stator organisms. SwrA/DegU regulation (edges 11–12) is *B. subtilis*-specific. The colanic acid/DgcO pathway (edges 13–14) is currently documented only in *E. coli*. These should be annotated with taxon constraints.

2. **Novel/single-study claims:** The colanic acid surfactant function (edge 14, Hwang et al. 2025) is a very recent finding with only 2 citations to date. While published in *mBio*, independent replication would strengthen confidence before full curation.

3. **Rhamnolipid dispensability on non-agar surfaces:** Morin & Déziel (2021, DOI:10.3390/biom11101468) showed that rhamnolipids are dispensable for surface motility on alternative gelling agents (gellan gum, carrageenan), suggesting the rhlA→swarming edge may be assay-specific rather than universally required.

4. **Swarming vs. surfing distinction:** Warrell et al. (2024) demonstrated that exogenous surfactants from other species enable a "surfing-like" motility in *P. aeruginosa* distinct from canonical swarming. Edges involving interspecies surfactant-driven motility should not be curated as swarming without further validation.

5. **c-di-GMP "sweet spot" model:** The threshold model (intermediate c-di-GMP promotes swarming via surfactant EPS production while high c-di-GMP inhibits via YcgR motor braking) is compelling but may oversimplify compartmentalized c-di-GMP signaling. Some DGCs have auto-inhibitory sites that maintain local pools (hwang2025cdigmpisrequired pages 8-11).

6. **FlhDC → cell elongation edge:** The mechanism by which FlhDC promotes cell elongation (potentially through suppression of cell division) is mechanistically unclear and may involve indirect pathways not yet fully elucidated (partridge2013swarmingflexibleroaming pages 5-6).

7. **Chemotaxis role ambiguity:** Chemotaxis has both a canonical signaling role and a "mechanical" role in swarming (maintaining flagellar motor bias for bundling). The mechanistic distinction should be preserved in causal graph annotation (partridge2013swarmingflexibleroaming pages 5-6, partridge2013swarmingflexibleroaming pages 7-8).


References

1. (partridge2013swarmingflexibleroaming pages 1-2): Jonathan D. Partridge and R. Harshey. Swarming: flexible roaming plans. Journal of Bacteriology, 195:909-918, Dec 2013. URL: https://doi.org/10.1128/jb.02063-12, doi:10.1128/jb.02063-12. This article has 249 citations and is from a peer-reviewed journal.

2. (partridge2022surveyingaswarm pages 5-7): Jonathan D. Partridge. Surveying a swarm: experimental techniques to establish and examine bacterial collective motion. Feb 2022. URL: https://doi.org/10.1128/aem.01853-21, doi:10.1128/aem.01853-21. This article has 24 citations and is from a peer-reviewed journal.

3. (partridge2013swarmingflexibleroaming pages 2-4): Jonathan D. Partridge and R. Harshey. Swarming: flexible roaming plans. Journal of Bacteriology, 195:909-918, Dec 2013. URL: https://doi.org/10.1128/jb.02063-12, doi:10.1128/jb.02063-12. This article has 249 citations and is from a peer-reviewed journal.

4. (partridge2022surveyingaswarm pages 3-5): Jonathan D. Partridge. Surveying a swarm: experimental techniques to establish and examine bacterial collective motion. Feb 2022. URL: https://doi.org/10.1128/aem.01853-21, doi:10.1128/aem.01853-21. This article has 24 citations and is from a peer-reviewed journal.

5. (partridge2013swarmingflexibleroaming pages 5-6): Jonathan D. Partridge and R. Harshey. Swarming: flexible roaming plans. Journal of Bacteriology, 195:909-918, Dec 2013. URL: https://doi.org/10.1128/jb.02063-12, doi:10.1128/jb.02063-12. This article has 249 citations and is from a peer-reviewed journal.

6. (partridge2013swarmingflexibleroaming pages 4-5): Jonathan D. Partridge and R. Harshey. Swarming: flexible roaming plans. Journal of Bacteriology, 195:909-918, Dec 2013. URL: https://doi.org/10.1128/jb.02063-12, doi:10.1128/jb.02063-12. This article has 249 citations and is from a peer-reviewed journal.

7. (partridge2013swarmingflexibleroaming pages 4-4): Jonathan D. Partridge and R. Harshey. Swarming: flexible roaming plans. Journal of Bacteriology, 195:909-918, Dec 2013. URL: https://doi.org/10.1128/jb.02063-12, doi:10.1128/jb.02063-12. This article has 249 citations and is from a peer-reviewed journal.

8. (yang2024unveilingthehidden pages 6-7): Aoyu Yang, Yuchong Tian, and Xiancheng Li. Unveiling the hidden arsenal: new insights into proteus mirabilis virulence in utis. Frontiers in Cellular and Infection Microbiology, Nov 2024. URL: https://doi.org/10.3389/fcimb.2024.1465460, doi:10.3389/fcimb.2024.1465460. This article has 23 citations.

9. (lee2015lossofflil pages 1-2): Yi-Ying Lee and Robert Belas. Loss of flil alters proteus mirabilis surface sensing and temperature-dependent swarming. Journal of Bacteriology, 197:159-173, Jan 2015. URL: https://doi.org/10.1128/jb.02235-14, doi:10.1128/jb.02235-14. This article has 50 citations and is from a peer-reviewed journal.

10. (lee2015lossofflil pages 12-13): Yi-Ying Lee and Robert Belas. Loss of flil alters proteus mirabilis surface sensing and temperature-dependent swarming. Journal of Bacteriology, 197:159-173, Jan 2015. URL: https://doi.org/10.1128/jb.02235-14, doi:10.1128/jb.02235-14. This article has 50 citations and is from a peer-reviewed journal.

11. (wu2024torquespeedrelationshipof pages 13-15): Haolin Wu, Zhengyu Wu, Maojin Tian, Rongjing Zhang, and Junhua Yuan. Torque-speed relationship of the flagellar motor with dual-stator systems in <i>pseudomonas aeruginosa</i>. Dec 2024. URL: https://doi.org/10.1128/mbio.00745-24, doi:10.1128/mbio.00745-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

12. (kuchma2025geneticanalysisof pages 1-2): Sherry L. Kuchma, C. J. Geiger, Shanice S. Webster, Yu Fu, Robert Montoya, and George A. O’Toole. Genetic analysis of flagellar-mediated surface sensing by <i>pseudomonas aeruginosa</i> pa14. Jul 2025. URL: https://doi.org/10.1128/jb.00520-24, doi:10.1128/jb.00520-24. This article has 4 citations and is from a peer-reviewed journal.

13. (anda2024howp.aeruginosa pages 2-4): Jaime de Anda, Sherry L. Kuchma, Shanice S. Webster, Arman Boromand, Kimberley A. Lewis, Calvin K. Lee, Maria Contreras, Victor F. Medeiros Pereira, William Schmidt, Deborah A. Hogan, Corey S. O’Hern, George A. O’Toole, and Gerard C. L. Wong. How <i>p. aeruginosa</i> cells with diverse stator composition collectively swarm. Apr 2024. URL: https://doi.org/10.1128/mbio.03322-23, doi:10.1128/mbio.03322-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

14. (anda2024howp.aeruginosa pages 8-10): Jaime de Anda, Sherry L. Kuchma, Shanice S. Webster, Arman Boromand, Kimberley A. Lewis, Calvin K. Lee, Maria Contreras, Victor F. Medeiros Pereira, William Schmidt, Deborah A. Hogan, Corey S. O’Hern, George A. O’Toole, and Gerard C. L. Wong. How <i>p. aeruginosa</i> cells with diverse stator composition collectively swarm. Apr 2024. URL: https://doi.org/10.1128/mbio.03322-23, doi:10.1128/mbio.03322-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

15. (anda2024howp.aeruginosa pages 1-2): Jaime de Anda, Sherry L. Kuchma, Shanice S. Webster, Arman Boromand, Kimberley A. Lewis, Calvin K. Lee, Maria Contreras, Victor F. Medeiros Pereira, William Schmidt, Deborah A. Hogan, Corey S. O’Hern, George A. O’Toole, and Gerard C. L. Wong. How <i>p. aeruginosa</i> cells with diverse stator composition collectively swarm. Apr 2024. URL: https://doi.org/10.1128/mbio.03322-23, doi:10.1128/mbio.03322-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

16. (deziel2003rhlaisrequired pages 1-2): Eric Déziel, François Lépine, Sylvain Milot, and Richard Villemur. Rhla is required for the production of a novel biosurfactant promoting swarming motility in pseudomonas aeruginosa: 3-(3-hydroxyalkanoyloxy)alkanoic acids (haas), the precursors of rhamnolipids. Microbiology, 149 Pt 8:2005-13, Aug 2003. URL: https://doi.org/10.1099/mic.0.26154-0, doi:10.1099/mic.0.26154-0. This article has 698 citations and is from a peer-reviewed journal.

17. (deziel2003rhlaisrequired pages 8-9): Eric Déziel, François Lépine, Sylvain Milot, and Richard Villemur. Rhla is required for the production of a novel biosurfactant promoting swarming motility in pseudomonas aeruginosa: 3-(3-hydroxyalkanoyloxy)alkanoic acids (haas), the precursors of rhamnolipids. Microbiology, 149 Pt 8:2005-13, Aug 2003. URL: https://doi.org/10.1099/mic.0.26154-0, doi:10.1099/mic.0.26154-0. This article has 698 citations and is from a peer-reviewed journal.

18. (kohler2000swarmingofpseudomonas pages 3-6): Thilo Köhler, Lasta Kocjancic Curty, Francisco Barja, Christian van Delden, and Jean-Claude Pechère. Swarming of pseudomonas aeruginosa is dependent on cell-to-cell signaling and requires flagella and pili. Journal of Bacteriology, 182:5990-5996, Nov 2000. URL: https://doi.org/10.1128/jb.182.21.5990-5996.2000, doi:10.1128/jb.182.21.5990-5996.2000. This article has 1233 citations and is from a peer-reviewed journal.

19. (daniels2004quorumsensingand pages 8-11): Ruth Daniels, Jos Vanderleyden, and Jan Michiels. Quorum sensing and swarming migration in bacteria. FEMS microbiology reviews, 28 3:261-89, Jun 2004. URL: https://doi.org/10.1016/j.femsre.2003.09.004, doi:10.1016/j.femsre.2003.09.004. This article has 841 citations and is from a domain leading peer-reviewed journal.

20. (daniels2004quorumsensingand pages 11-12): Ruth Daniels, Jos Vanderleyden, and Jan Michiels. Quorum sensing and swarming migration in bacteria. FEMS microbiology reviews, 28 3:261-89, Jun 2004. URL: https://doi.org/10.1016/j.femsre.2003.09.004, doi:10.1016/j.femsre.2003.09.004. This article has 841 citations and is from a domain leading peer-reviewed journal.

21. (kohler2000swarmingofpseudomonas pages 6-6): Thilo Köhler, Lasta Kocjancic Curty, Francisco Barja, Christian van Delden, and Jean-Claude Pechère. Swarming of pseudomonas aeruginosa is dependent on cell-to-cell signaling and requires flagella and pili. Journal of Bacteriology, 182:5990-5996, Nov 2000. URL: https://doi.org/10.1128/jb.182.21.5990-5996.2000, doi:10.1128/jb.182.21.5990-5996.2000. This article has 1233 citations and is from a peer-reviewed journal.

22. (mordini2013theroleof pages 5-7): Serena Mordini, Cecilia Osera, Simone Marini, Francesco Scavone, Riccardo Bellazzi, Alessandro Galizzi, and Cinzia Calvio. The role of swra, degu and pd3 in fla/che expression in b. subtilis. PLoS ONE, 8:e85065, Dec 2013. URL: https://doi.org/10.1371/journal.pone.0085065, doi:10.1371/journal.pone.0085065. This article has 56 citations and is from a peer-reviewed journal.

23. (mordini2013theroleof pages 1-2): Serena Mordini, Cecilia Osera, Simone Marini, Francesco Scavone, Riccardo Bellazzi, Alessandro Galizzi, and Cinzia Calvio. The role of swra, degu and pd3 in fla/che expression in b. subtilis. PLoS ONE, 8:e85065, Dec 2013. URL: https://doi.org/10.1371/journal.pone.0085065, doi:10.1371/journal.pone.0085065. This article has 56 citations and is from a peer-reviewed journal.

24. (mordini2013theroleof pages 2-3): Serena Mordini, Cecilia Osera, Simone Marini, Francesco Scavone, Riccardo Bellazzi, Alessandro Galizzi, and Cinzia Calvio. The role of swra, degu and pd3 in fla/che expression in b. subtilis. PLoS ONE, 8:e85065, Dec 2013. URL: https://doi.org/10.1371/journal.pone.0085065, doi:10.1371/journal.pone.0085065. This article has 56 citations and is from a peer-reviewed journal.

25. (mordini2013theroleof pages 9-10): Serena Mordini, Cecilia Osera, Simone Marini, Francesco Scavone, Riccardo Bellazzi, Alessandro Galizzi, and Cinzia Calvio. The role of swra, degu and pd3 in fla/che expression in b. subtilis. PLoS ONE, 8:e85065, Dec 2013. URL: https://doi.org/10.1371/journal.pone.0085065, doi:10.1371/journal.pone.0085065. This article has 56 citations and is from a peer-reviewed journal.

26. (mordini2013theroleof pages 3-5): Serena Mordini, Cecilia Osera, Simone Marini, Francesco Scavone, Riccardo Bellazzi, Alessandro Galizzi, and Cinzia Calvio. The role of swra, degu and pd3 in fla/che expression in b. subtilis. PLoS ONE, 8:e85065, Dec 2013. URL: https://doi.org/10.1371/journal.pone.0085065, doi:10.1371/journal.pone.0085065. This article has 56 citations and is from a peer-reviewed journal.

27. (hwang2025cdigmpisrequired pages 8-11): YuneSahng Hwang, Marta Perez, Rebecca Holzel, and Rasika M. Harshey. C-di-gmp is required for swarming in <i>e. coli</i> , producing colanic acid that acts as surfactant. mBio, Jun 2025. URL: https://doi.org/10.1128/mbio.00916-25, doi:10.1128/mbio.00916-25. This article has 2 citations and is from a domain leading peer-reviewed journal.

28. (hwang2025cdigmpisrequired pages 2-5): YuneSahng Hwang, Marta Perez, Rebecca Holzel, and Rasika M. Harshey. C-di-gmp is required for swarming in <i>e. coli</i> , producing colanic acid that acts as surfactant. mBio, Jun 2025. URL: https://doi.org/10.1128/mbio.00916-25, doi:10.1128/mbio.00916-25. This article has 2 citations and is from a domain leading peer-reviewed journal.

29. (hwang2025cdigmpisrequired pages 11-14): YuneSahng Hwang, Marta Perez, Rebecca Holzel, and Rasika M. Harshey. C-di-gmp is required for swarming in <i>e. coli</i> , producing colanic acid that acts as surfactant. mBio, Jun 2025. URL: https://doi.org/10.1128/mbio.00916-25, doi:10.1128/mbio.00916-25. This article has 2 citations and is from a domain leading peer-reviewed journal.

30. (partridge2013swarmingflexibleroaming pages 6-7): Jonathan D. Partridge and R. Harshey. Swarming: flexible roaming plans. Journal of Bacteriology, 195:909-918, Dec 2013. URL: https://doi.org/10.1128/jb.02063-12, doi:10.1128/jb.02063-12. This article has 249 citations and is from a peer-reviewed journal.

31. (liu2022theeffectof pages 1-2): Xiang Liu, Chi Zhang, Rongjing Zhang, and Junhua Yuan. The effect of the second messenger c-di-gmp on bacterial chemotaxis in escherichia coli. May 2022. URL: https://doi.org/10.1128/aem.00373-22, doi:10.1128/aem.00373-22. This article has 11 citations and is from a peer-reviewed journal.

32. (hwang2025cdigmpisrequired pages 5-8): YuneSahng Hwang, Marta Perez, Rebecca Holzel, and Rasika M. Harshey. C-di-gmp is required for swarming in <i>e. coli</i> , producing colanic acid that acts as surfactant. mBio, Jun 2025. URL: https://doi.org/10.1128/mbio.00916-25, doi:10.1128/mbio.00916-25. This article has 2 citations and is from a domain leading peer-reviewed journal.

33. (partridge2013swarmingflexibleroaming pages 7-8): Jonathan D. Partridge and R. Harshey. Swarming: flexible roaming plans. Journal of Bacteriology, 195:909-918, Dec 2013. URL: https://doi.org/10.1128/jb.02063-12, doi:10.1128/jb.02063-12. This article has 249 citations and is from a peer-reviewed journal.

34. (hwang2025cdigmpisrequired pages 1-2): YuneSahng Hwang, Marta Perez, Rebecca Holzel, and Rasika M. Harshey. C-di-gmp is required for swarming in <i>e. coli</i> , producing colanic acid that acts as surfactant. mBio, Jun 2025. URL: https://doi.org/10.1128/mbio.00916-25, doi:10.1128/mbio.00916-25. This article has 2 citations and is from a domain leading peer-reviewed journal.

35. (daniels2004quorumsensingand pages 6-7): Ruth Daniels, Jos Vanderleyden, and Jan Michiels. Quorum sensing and swarming migration in bacteria. FEMS microbiology reviews, 28 3:261-89, Jun 2004. URL: https://doi.org/10.1016/j.femsre.2003.09.004, doi:10.1016/j.femsre.2003.09.004. This article has 841 citations and is from a domain leading peer-reviewed journal.

36. (caiazza2005rhamnolipidsmodulateswarming pages 5-6): Nicky C. Caiazza, Robert M. Q. Shanks, and G. A. O'Toole. Rhamnolipids modulate swarming motility patterns of pseudomonas aeruginosa. Journal of Bacteriology, 187:7351-7361, Nov 2005. URL: https://doi.org/10.1128/jb.187.21.7351-7361.2005, doi:10.1128/jb.187.21.7351-7361.2005. This article has 671 citations and is from a peer-reviewed journal.

37. (yang2017influenceofphysical pages 6-8): Alexander Yang, Wai Shing Tang, Tieyan Si, and Jay X. Tang. Influence of physical effects on the swarming motility of pseudomonas aeruginosa. Biophysical journal, 112 7:1462-1471, Apr 2017. URL: https://doi.org/10.1016/j.bpj.2017.02.019, doi:10.1016/j.bpj.2017.02.019. This article has 118 citations and is from a domain leading peer-reviewed journal.

38. (yang2017influenceofphysical pages 1-2): Alexander Yang, Wai Shing Tang, Tieyan Si, and Jay X. Tang. Influence of physical effects on the swarming motility of pseudomonas aeruginosa. Biophysical journal, 112 7:1462-1471, Apr 2017. URL: https://doi.org/10.1016/j.bpj.2017.02.019, doi:10.1016/j.bpj.2017.02.019. This article has 118 citations and is from a domain leading peer-reviewed journal.

39. (yang2017influenceofphysical pages 3-4): Alexander Yang, Wai Shing Tang, Tieyan Si, and Jay X. Tang. Influence of physical effects on the swarming motility of pseudomonas aeruginosa. Biophysical journal, 112 7:1462-1471, Apr 2017. URL: https://doi.org/10.1016/j.bpj.2017.02.019, doi:10.1016/j.bpj.2017.02.019. This article has 118 citations and is from a domain leading peer-reviewed journal.

40. (mordini2013theroleof pages 7-9): Serena Mordini, Cecilia Osera, Simone Marini, Francesco Scavone, Riccardo Bellazzi, Alessandro Galizzi, and Cinzia Calvio. The role of swra, degu and pd3 in fla/che expression in b. subtilis. PLoS ONE, 8:e85065, Dec 2013. URL: https://doi.org/10.1371/journal.pone.0085065, doi:10.1371/journal.pone.0085065. This article has 56 citations and is from a peer-reviewed journal.