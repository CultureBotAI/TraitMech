---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:23:55.491114'
end_time: '2026-08-04T07:38:34.534271'
duration_seconds: 879.04
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: capsule
  trait_identifier: traitmech:000063
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: capsule
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A morphology trait in which the cell is surrounded by a well-organized
    layer of polysaccharide (or rarely polypeptide) external to the cell envelope,
    mediating adhesion, desiccation resistance, and immune evasion.
  parent_traits: METPO:1000059
  synonyms: capsulated, capsular polysaccharide
  evidence_summary: 'DOI:10.1146/annurev.micro.50.1.285:  (Roberts, "The biochemistry
    and genetics of capsular polysaccharide production in bacteria", treats the capsule
    as an organized external polysaccharide layer.) | DOI:10.1146/annurev.biochem.75.103004.142545:  (Whitfield
    reviews biosynthesis and assembly of capsular polysaccharides in Escherichia coli.)'
  causal_graph_summary: 'capsule_polysaccharide_protection: 11 nodes, 8 edges'
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
- **Trait label:** capsule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000063
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell is surrounded by a well-organized layer of polysaccharide (or rarely polypeptide) external to the cell envelope, mediating adhesion, desiccation resistance, and immune evasion.
- **Parent traits:** METPO:1000059
- **Synonyms:** capsulated, capsular polysaccharide
- **Existing evidence:** DOI:10.1146/annurev.micro.50.1.285:  (Roberts, "The biochemistry and genetics of capsular polysaccharide production in bacteria", treats the capsule as an organized external polysaccharide layer.) | DOI:10.1146/annurev.biochem.75.103004.142545:  (Whitfield reviews biosynthesis and assembly of capsular polysaccharides in Escherichia coli.)
- **Existing causal graph summary:** capsule_polysaccharide_protection: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **capsule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/capsule.yaml`.

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
- **Trait label:** capsule
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000063
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A morphology trait in which the cell is surrounded by a well-organized layer of polysaccharide (or rarely polypeptide) external to the cell envelope, mediating adhesion, desiccation resistance, and immune evasion.
- **Parent traits:** METPO:1000059
- **Synonyms:** capsulated, capsular polysaccharide
- **Existing evidence:** DOI:10.1146/annurev.micro.50.1.285:  (Roberts, "The biochemistry and genetics of capsular polysaccharide production in bacteria", treats the capsule as an organized external polysaccharide layer.) | DOI:10.1146/annurev.biochem.75.103004.142545:  (Whitfield reviews biosynthesis and assembly of capsular polysaccharides in Escherichia coli.)
- **Existing causal graph summary:** capsule_polysaccharide_protection: 11 nodes, 8 edges

## Research Objective

Research the microbial trait **capsule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/capsule.yaml`.

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


## Microbial Trait Causal Graph Report: Capsule (traitmech:000063)

---

### Executive Summary

The microbial capsule trait (traitmech:000063) describes a morphology in which a cell is surrounded by a well-organized polysaccharide (or rarely polypeptide) matrix tightly associated with the cell surface—distinguishable from secreted, loosely bound exopolysaccharide (slime) by strong cell anchoring, discrete surface organization, and coherent visibility by microscopy (roberts1996thebiochemistryand pages 1-3, whitfield2020assemblyofbacterial pages 1-2). This trait mediates adhesion, desiccation resistance, and immune evasion. Causal graph curation is grounded in authoritative, pathway-focused, and cutting-edge (2023–2024) literature.

### Trait Scope and Discrimination
- **Phenotype:** Capsule is a visible, surface-retained, often covalently anchored structure distinct from secreted EPS/slime.
- **Boundaries:** Slime and biofilm matrix—lack tight cell association/organization; capsule is more structured and directly cell-bound.
- **Anchor and Organization:** Anchored via lipid/phospholipid/lipid-A in Gram-negatives, or covalently to peptidoglycan/plasma membrane in Gram-positives (roberts1996thebiochemistryand pages 1-3, whitfield2020assemblyofbacterial pages 9-10).

---

### Candidate Graph Entities (Nodes)

Entities are drawn from recent research, canonical reviews, and comprise biosynthetic modules, molecular components, pathway intermediates, regulatory processes, environmental and assay phenotypes.

| node label | node type | suggested CURIE / stable identifier | notes on ontology grounding or label-only curation |
|---|---|---|---|
| capsule | function | traitmech:000063 | Target trait; morphology class for organized cell-associated capsule rather than diffusible slime (roberts1996thebiochemistryand pages 1-3, whitfield2020assemblyofbacterial pages 2-4) |
| capsular polysaccharide | chemical |  | Label-only; broad polymer class spanning many serotype-specific structures (gao2024bacterialcapsulesoccurrence pages 1-3, whitfield2020assemblyofbacterial pages 2-4) |
| capsular polypeptide | chemical |  | Label-only; needed for rare protein capsules such as Bacillus anthracis polyglutamate capsules (gao2024bacterialcapsulesoccurrence pages 1-3) |
| secreted exopolysaccharide / slime | chemical |  | Boundary-case comparator, not the same as organized capsule; keep as label-only node for negative distinction (roberts1996thebiochemistryand pages 1-3, whitfield2020assemblyofbacterial pages 1-2) |
| Wzx/Wzy-dependent capsule biosynthesis pathway | pathway |  | Canonical pathway class; pathway-level label supported across many taxa (whitfield2020assemblyofbacterial pages 5-6, gao2024bacterialcapsulesoccurrence pages 1-3) |
| ABC-transporter-dependent capsule biosynthesis pathway | pathway |  | Canonical pathway class for group II/III-like capsules and related systems (kuklewicz2024molecularinsightsinto pages 1-2, whitfield2020assemblyofbacterial pages 10-11) |
| synthase-dependent capsule biosynthesis pathway | pathway |  | Canonical pathway class; taxon-restricted examples include pneumococcal serotypes 3 and 37 (gao2024bacterialcapsulesoccurrence pages 3-3) |
| repeat-unit assembly | process | GO:0009255 | Closest generic GO process is polysaccharide biosynthetic process; use more specific label-only child if needed (whitfield2020assemblyofbacterial pages 5-6) |
| capsular polysaccharide export | process | GO:0015774 | GO term likely too generic for polysaccharide transport; label-only may be safer unless exact GO term is verified (kuklewicz2024molecularinsightsinto pages 1-2, whitfield2020assemblyofbacterial pages 9-10) |
| capsule organization on cell surface | process |  | Label-only morphology process; supported by Wzi-dependent coherent capsule organization (whitfield2020assemblyofbacterial pages 9-10) |
| undecaprenyl diphosphate-linked repeat unit | chemical |  | Label-only lipid-linked oligosaccharide intermediate; grounding depends on exact repeat chemistry (whitfield2020assemblyofbacterial pages 5-6) |
| undecaprenyl phosphate | chemical | CHEBI:16460 | Conservative CHEBI for undecaprenyl phosphate carrier lipid; verify if diphosphate form is needed in curation (rendueles2020decipheringtherole pages 2-4, whitfield2020assemblyofbacterial pages 5-6) |
| phosphatidylglycerol | chemical | CHEBI:17517 | Conserved lipid acceptor for Kdo-linked ABC-pathway anchors (whitfield2020assemblyofbacterial pages 10-11, kuklewicz2024molecularinsightsinto pages 1-2) |
| Kdo | chemical | CHEBI:58711 | 3-deoxy-D-manno-oct-2-ulosonic acid; central in ABC-pathway linker glycolipid (kuklewicz2024molecularinsightsinto pages 1-2, whitfield2020assemblyofbacterial pages 10-11) |
| Kdo oligosaccharide linker | chemical |  | Label-only because exact oligomer length/linkage varies; adaptor for CPS biosynthesis (whitfield2020assemblyofbacterial pages 10-11, kuklewicz2024molecularinsightsinto pages 1-2) |
| glycolipid anchor | chemical |  | Generic anchor node spanning Kdo-phosphatidylglycerol and related anchors; label-only (kuklewicz2024molecularinsightsinto pages 1-2, whitfield2020assemblyofbacterial pages 10-11) |
| WcaJ | protein |  | Polyisoprenyl-phosphate hexose-1-phosphate transferase initiating some Wzy pathways; protein-specific accession varies by taxon (rendueles2020decipheringtherole pages 2-4, whitfield2020assemblyofbacterial pages 7-9) |
| WbaP | protein |  | Alternate initiating phosphoglycosyltransferase; label-only unless taxon-specific protein accession is curated (rendueles2020decipheringtherole pages 2-4, whitfield2020assemblyofbacterial pages 5-6) |
| phosphoglycosyltransferase activity | function | GO:0004576 | Broad transferase-on-phosphorus-containing-groups term may be imperfect; keep label-only if exact GO not verified (whitfield2020assemblyofbacterial pages 5-6, whitfield2020assemblyofbacterial pages 7-9) |
| glycosyltransferase | protein |  | Generic enzyme class completing repeat-unit assembly; ground taxon-specific members only if exact genes known (rendueles2020decipheringtherole pages 2-4, whitfield2020assemblyofbacterial pages 5-6) |
| Wzx flippase | protein |  | MOP-family flippase exporting Und-PP-linked repeat units; taxon-specific protein accessions vary (whitfield2020assemblyofbacterial pages 5-6, rendueles2020decipheringtherole pages 2-4) |
| lipid-linked oligosaccharide flipping | process | GO:0097502 | Candidate GO for membrane translocation of lipid-linked oligosaccharides; verify exact applicability before formal curation (whitfield2020assemblyofbacterial pages 5-6) |
| Wzy polymerase | protein |  | Polymerase for blockwise CPS chain extension in Wzy systems; label-only across taxa (whitfield2020assemblyofbacterial pages 5-6, rendueles2020decipheringtherole pages 2-4) |
| polysaccharide polymerization | process | GO:0033692 | Candidate generic GO; verify exact term fit for capsule polymerization (whitfield2020assemblyofbacterial pages 5-6, lee2024singlemissensemutations pages 1-2) |
| Wzc | protein |  | BY-kinase/chain-length regulator associated with Wza and capsule assembly (rendueles2020decipheringtherole pages 2-4, whitfield2020assemblyofbacterial pages 9-10) |
| bacterial tyrosine kinase activity | function | GO:0004713 | Broad kinase activity term; usable for Wzc-like phosphorylation with caution (whitfield2020assemblyofbacterial pages 7-9, whitfield2020assemblyofbacterial pages 9-10) |
| Wza | protein |  | Outer-membrane polysaccharide export protein/opx translocon; label-only unless family ID curated (whitfield2020assemblyofbacterial pages 7-9, whitfield2020assemblyofbacterial pages 9-10) |
| outer-membrane octameric translocon | protein |  | Structural complex state of Wza; label-only complex node (whitfield2020assemblyofbacterial pages 7-9, whitfield2020assemblyofbacterial pages 9-10) |
| Wzi | protein |  | Outer-membrane lectin-like organizer of coherent capsule structure (whitfield2020assemblyofbacterial pages 9-10) |
| coherent capsule structure | process |  | Morphology-relevant process/phenotype node for organized surface-retained capsule (whitfield2020assemblyofbacterial pages 9-10, whitfield2020assemblyofbacterial pages 1-2) |
| KpsS | protein |  | CMP-Kdo-dependent glycosyltransferase initiating Kdo linker synthesis (whitfield2020assemblyofbacterial pages 10-11, kuklewicz2024molecularinsightsinto pages 1-2) |
| KpsC | protein |  | GT107 family Kdo glycosyltransferase extending Kdo linker with alternating linkages (whitfield2020assemblyofbacterial pages 10-11, kuklewicz2024molecularinsightsinto pages 1-2) |
| KpsM | protein |  | Transmembrane domain of ABC exporter recognizing glycolipid substrate (kuklewicz2024molecularinsightsinto pages 1-2, kuklewicz2024molecularinsightsinto pages 2-3) |
| KpsT | protein |  | Nucleotide-binding ATPase subunit of KpsMT exporter (kuklewicz2024molecularinsightsinto pages 1-2, kuklewicz2024molecularinsightsinto pages 2-3) |
| KpsMT ABC transporter | protein |  | Functional exporter complex; use complex label unless exact stable complex ID is available (kuklewicz2024molecularinsightsinto pages 1-2, kuklewicz2024molecularinsightsinto pages 2-3) |
| ATP hydrolysis | process | GO:0016887 | Mechanistic driver of KpsMT conformational rearrangements (kuklewicz2024molecularinsightsinto pages 1-2) |
| KpsE | protein |  | Periplasmic/inner-membrane-anchored PCP-like subunit; structural cage around KpsMT (kuklewicz2024molecularinsightsinto pages 1-2, kuklewicz2024molecularinsightsinto pages 2-3) |
| KpsD | protein |  | Outer-membrane/periplasmic export factor needed for surface exposure beyond inner-membrane translocation (kuklewicz2024molecularinsightsinto pages 1-2, kuklewicz2024molecularinsightsinto pages 2-3) |
| KpsE cage | protein |  | Structural complex/state from 2024 cryo-EM; label-only but mechanistically informative (kuklewicz2024molecularinsightsinto pages 1-2) |
| periplasmic CPS accumulation | process |  | Assay phenotype when KpsD or KpsE is absent in engineered system (kuklewicz2024molecularinsightsinto pages 2-3) |
| HyaD | protein |  | Pasteurella multocida hyaluronan synthase used as model CPS synthase; taxon-specific evidence (kuklewicz2024molecularinsightsinto pages 2-3, kuklewicz2024molecularinsightsinto pages 1-2) |
| hyaluronan capsule | chemical |  | Taxon-specific CPS exemplar used in reconstituted export experiments (kuklewicz2024molecularinsightsinto pages 2-3, kuklewicz2024molecularinsightsinto pages 1-2) |
| TviB | protein |  | Salmonella Typhi Vi donor-substrate biosynthesis enzyme (lee2024singlemissensemutations pages 1-2) |
| TviC | protein |  | Salmonella Typhi Vi donor-substrate biosynthesis enzyme (lee2024singlemissensemutations pages 1-2) |
| TviD | protein |  | Vi O-acetylation enzyme; missense variants alter capsule properties (lee2024singlemissensemutations pages 1-2, lee2024singlemissensemutations pages 5-6) |
| TviE | protein |  | Vi polymerization enzyme; missense variants alter length/intensity and virulence phenotypes (lee2024singlemissensemutations pages 1-2, lee2024singlemissensemutations pages 5-6) |
| VexA-D ABC transporter | protein |  | Vi export complex in S. Typhi; label-only transporter complex (lee2024singlemissensemutations pages 1-2) |
| TviA | protein |  | Regulatory factor controlling tviB-vexE operon via RcsB/OmpR interactions (lee2024singlemissensemutations pages 1-2) |
| RcsB | protein |  | Regulatory partner for TviA in Vi expression; also part of broader envelope-stress regulation (lee2024singlemissensemutations pages 1-2) |
| OmpR | protein |  | Regulatory partner for TviA in Vi expression (lee2024singlemissensemutations pages 1-2) |
| RmpA | protein |  | Positive capsule regulator in Klebsiella literature summarized in 2024 review (gao2024bacterialcapsulesoccurrence pages 9-10) |
| RcsA | protein |  | Positive capsule regulator in Klebsiella literature summarized in 2024 review (gao2024bacterialcapsulesoccurrence pages 9-10) |
| cAMP-dependent catabolite repression | process | GO:0045861 | Regulatory input reported for K. pneumoniae capsule synthesis; GO term may require verification (gao2024bacterialcapsulesoccurrence pages 9-10) |
| quorum sensing | process | GO:0009372 | Regulatory input affecting capsule synthesis in some taxa (gao2024bacterialcapsulesoccurrence pages 9-10) |
| iron availability | environmental_factor |  | Environmental regulator linked to Fur/IscR capsule control; label-only condition node (gao2024bacterialcapsulesoccurrence pages 9-10) |
| NaCl concentration | environmental_factor | CHEBI:26710 | Experimental factor modulating Vi expression and O-acetylation in S. Typhi; chemical grounding for NaCl is straightforward (lee2024singlemissensemutations pages 1-2) |
| complement resistance | function | GO:0098542 | Candidate host-defense evasion function; verify exact GO before formal grounding (whitfield2020assemblyofbacterial pages 2-4, yang2025identificationofa pages 1-2) |
| phagocytosis resistance | function | GO:0050777 | GO may be too generic; label-only may be safer for capsule-mediated anti-phagocytic phenotype (whitfield2020assemblyofbacterial pages 2-4, lee2024singlemissensemutations pages 1-2) |
| desiccation resistance | function | GO:0009269 | Broad stress-response grounding may be possible, but phenotype node may be best kept label-only (roberts1996thebiochemistryand pages 1-3, haudiquet2024capsulesandtheir pages 1-2) |
| adhesion to host cells | function | GO:0044406 | Broad host-cell adhesion process; capsule can increase or mask adhesion depending on taxon, so annotate carefully (gao2024bacterialcapsulesoccurrence pages 9-10, lee2024singlemissensemutations pages 5-6) |
| biofilm formation | process | GO:0042710 | Widely used GO term; capsule contributes in some systems but not universally (gao2024bacterialcapsulesoccurrence pages 3-3, yang2025identificationofa pages 1-2) |
| phage susceptibility | function |  | Label-only assay phenotype strongly shaped by capsule serotype in K. pneumoniae (haudiquet2024capsulesandtheir pages 1-2, cheetham2024specificityanddiversity pages 1-2) |
| plasmid conjugation efficiency | function | GO:0000746 | GO covers conjugation, but 'efficiency' is assay-level phenotype; use label-only phenotype if preferred (haudiquet2024capsulesandtheir pages 1-2) |
| capsule depolymerase | protein |  | Broad phage-encoded enzyme class selectively degrading capsule; often tail fiber/tail spike associated (cheetham2024specificityanddiversity pages 1-2, yang2025identificationofa pages 1-2) |
| serum killing susceptibility | function |  | Assay phenotype increased after capsule removal/depolymerase treatment; label-only (cheetham2024specificityanddiversity pages 1-2, yang2025identificationofa pages 1-2) |


*Table: This table lists conservative candidate graph nodes for curating the microbial capsule trait, spanning pathways, proteins, chemicals, processes, regulatory inputs, and assay phenotypes. It is designed to help populate a TraitMech causal graph while distinguishing well-grounded entities from label-only placeholders.*

---

### Evidence-Backed Causal Edges

The following are primary, conservative, curation-ready candidate causal edges (subject–predicate–object) with evidence tag, scope, and notes. Taxon- or assay-specific mechanistic details are explicitly annotated.

| subject node | predicate | object node | pathway/taxon scope | evidence strength | DOI reference | short verbatim supporting snippet | curation note |
|---|---|---|---|---|---|---|---|
| capsule | is_distinguished_from | secreted exopolysaccharide/slime | broad bacterial surface polysaccharides | strong | 10.1146/annurev.micro.50.1.285 | “capsule. In contrast, extracellular polysaccharide (EPS) molecules appear to be released onto the cell surface with no visible means of attachment and are often sloughed off to form slime” (roberts1996thebiochemistryand pages 1-3) | Good boundary-setting edge for trait scope; morphology trait should require organized, cell-associated layer. |
| capsular polysaccharide | has_function | desiccation resistance | broad, historical capsule function | moderate | 10.1146/annurev.micro.50.1.285 | “FUNCTIONS OF BACTERIAL CAPSULES … Prevention of Desiccation” (roberts1996thebiochemistryand pages 1-3) | Strong as review-level functional claim, but mechanism/context varies by taxon. |
| capsular polysaccharide | has_function | adhesion | broad, historical capsule function | moderate | 10.1146/annurev.micro.50.1.285 | “FUNCTIONS OF BACTERIAL CAPSULES … Adherence” (roberts1996thebiochemistryand pages 1-3) | Broad claim; curate as high-level function, not as universal positive effect in every taxon. |
| capsular polysaccharide | suppresses | complement-mediated killing | pathogens broadly; especially encapsulated pathogens | moderate | 10.1146/annurev-micro-011420-075607 | “Capsules protect pathogens by suppressing inflammatory responses and providing resistance to antimicrobial peptides, complement-mediated killing, and phagocytosis” (whitfield2020assemblyofbacterial pages 2-4) | Broad but canonical review evidence; taxon-generalized, so keep as trait-level protection function. |
| capsular polysaccharide | suppresses | phagocytosis | pathogens broadly; especially encapsulated pathogens | moderate | 10.1146/annurev-micro-011420-075607 | “providing resistance to antimicrobial peptides, complement-mediated killing, and phagocytosis” (whitfield2020assemblyofbacterial pages 2-4) | Broad review statement; suitable as a generic protective function edge. |
| capsule | supports | biofilm formation | broad; not universal | moderate | 10.1146/annurev-micro-011420-075607 | “These polymers afford the producing bacteria protection from a wide range of physical, chemical, and biological stresses, support biofilms” (whitfield2020assemblyofbacterial pages 1-2) | Keep broad and non-universal; many capsules aid biofilm but some can impede early adhesion. |
| WcaJ/WbaP | initiates synthesis of | Und-PP-linked repeat unit | Wzy-dependent capsules in E. coli/K. pneumoniae prototypes | strong | 10.1146/annurev-micro-011420-075607 | “PGT enzymes (including WbaP and WcaJ in E. coli and K. pneumoniae) initiate synthesis of undecaprenyl diphosphate (Und-PP)-linked repeat units” (whitfield2020assemblyofbacterial pages 5-6) | Core mechanistic edge for Wzy pathway. |
| glycosyltransferases | extends | Und-PP-linked repeat unit | Wzy-dependent pathway | strong | 10.1111/mmi.14474 | “Glycosyltransferases add oligosaccharides” (rendueles2020decipheringtherole pages 2-4) | Taxon example is K. pneumoniae K1; broadly consistent with Wzy pathway. |
| Wzx flippase | translocates | Und-PP-linked repeat units across inner membrane | Wzy-dependent pathway | strong | 10.1146/annurev-micro-011420-075607 | “Wzx, a MOP family transporter, exports Und-PP-repeat units across the membrane” (whitfield2020assemblyofbacterial pages 5-6) | Fundamental edge; broad across Wzy pathway users. |
| Wzy polymerase | polymerizes | repeat units into CPS chain | Wzy-dependent pathway | strong | 10.1111/mmi.14474 | “Wzy polymerase extends trisaccharide units” (rendueles2020decipheringtherole pages 2-4) | K. pneumoniae K1 example; canonical Wzy function. |
| Wzc | regulates chain length of | capsule polysaccharide | K. pneumoniae K1 Wzy pathway; likely broader in Group 1 systems | moderate | 10.1111/mmi.14474 | “Wzc regulates capsule length” (rendueles2020decipheringtherole pages 2-4) | Good mechanistic edge, but chain-length regulation details vary by system. |
| Wza | exports | mature capsule polysaccharide | Gram-negative Wzy-dependent systems | strong | 10.1111/mmi.14474 | “Wza secretin exports the mature capsule to the extracellular space” (rendueles2020decipheringtherole pages 2-4) | Strong path step; broadly curatable for Wza-containing systems. |
| Wza | forms | outer-membrane octameric translocon | Gram-negative Wzy-dependent systems | strong | 10.1146/annurev-micro-011420-075607 | “Wza functions as a lipoprotein forming a stable octamer with internal diameter of 17 Å” (whitfield2020assemblyofbacterial pages 7-9) | Structural support for export node/edge. |
| Wzi | organizes | coherent capsule structure | Gram-negative capsules with Wzi, e.g. E. coli/Klebsiella | strong | 10.1146/annurev-micro-011420-075607 | “Wzi, an outer membrane lectin-like protein, organizes capsule structure; wzi mutants lose coherent capsules and release more CPS” (whitfield2020assemblyofbacterial pages 9-10) | Useful morphology-specific edge because it links polymer to visible capsule organization. |
| KpsS | adds | single Kdo residue to phosphatidylglycerol acceptor | ABC-transporter-dependent Group 2/3-like capsules | strong | 10.1146/annurev-micro-011420-075607 | “KpsS adds a single Kdo residue” (whitfield2020assemblyofbacterial pages 10-11) | Core anchor-biosynthesis edge. |
| KpsC | extends | Kdo linker oligosaccharide | ABC-transporter-dependent Group 2/3-like capsules | strong | 10.1146/annurev-micro-011420-075607 | “KpsC contains two catalytic sites for adding alternating β2,7- and β2,4-linked residues” (whitfield2020assemblyofbacterial pages 10-11) | Curate with note that linkage stereochemistry belongs in annotation. |
| Kdo oligosaccharide linker | serves_as_acceptor_for | CPS biosynthesis | ABC-transporter-dependent capsules | strong | 10.1146/annurev-micro-011420-075607 | “The Kdo oligosaccharide serves as acceptor for different repeat-unit structures” (whitfield2020assemblyofbacterial pages 10-11) | Important bridge from anchor biosynthesis to polymer biosynthesis. |
| KpsMT ABC transporter | translocates | capsular polysaccharide across inner membrane | Gram-negative ABC-transporter-dependent capsules | strong | 10.1038/s41586-024-07248-9 | “KpsMT has broad substrate specificity and is sufficient for the translocation of CPSs across the inner bacterial membrane” (kuklewicz2024molecularinsightsinto pages 1-2) | High-priority 2024 primary evidence. |
| ATP hydrolysis by KpsMT | drives | conformational rearrangements during CPS translocation | Gram-negative ABC-transporter-dependent capsules | strong | 10.1038/s41586-024-07248-9 | “rigid-body conformational rearrangements of KpsMT during ATP hydrolysis” (kuklewicz2024molecularinsightsinto pages 1-2) | Mechanistic, directly supported by cryo-EM states. |
| KpsM | recognizes | glycolipid substrate in electropositive canyon | Gram-negative ABC-transporter-dependent capsules | strong | 10.1038/s41586-024-07248-9 | “recognition of a glycolipid inside a membrane-exposed electropositive canyon” (kuklewicz2024molecularinsightsinto pages 1-2) | Useful molecular-recognition edge; node could be “capsule glycolipid anchor”. |
| KpsD absence | causes | periplasmic CPS accumulation without surface exposure | engineered E. coli expressing Pasteurella/Schlegelella components | strong | 10.1038/s41586-024-07248-9 | “in the absence of an outer-membrane pore, any translocated CPS would accumulate in the periplasm” (kuklewicz2024molecularinsightsinto pages 2-3) | Assay-specific but strong evidence for KpsD role in trans-envelope export. |
| synthase-dependent pathway | produces | capsule polysaccharide | S. pneumoniae serotypes 3 and 37 | moderate | 10.1038/s41522-024-00497-6 | “The synthase-dependent pathway is exemplified by S. pneumoniae serotypes 3 and 37, which use single enzyme mechanisms” (gao2024bacterialcapsulesoccurrence pages 3-3) | Keep taxon-specific; insufficient detail here for enzyme-specific nodes. |
| capsule serotype | determines | phage infectivity/host range | Klebsiella pneumoniae capsule swaps | strong | 10.1038/s41467-024-46147-5 | “Capsule swaps systematically invert phage susceptibility” (haudiquet2024capsulesandtheir pages 1-2) | Strong 2024 causal evidence; taxon-specific to K. pneumoniae. |
| phage depolymerase activity | degrades | capsule polysaccharide | Klebsiella-targeting phages | strong | 10.1042/EBC20240015 | “specific polysaccharide depolymerases with the ability to selectively degrade the highly varied protective capsules” (cheetham2024specificityanddiversity pages 1-2) | Good edge for phage-capsule interaction graph branch. |
| depolymerase-mediated capsule removal | increases susceptibility to | complement/serum killing | K. pneumoniae; review plus K64 example | strong | 10.1042/EBC20240015 | “Capsule removal by phage depolymerases subjects K. pneumoniae to complement-mediated killing in vivo” (cheetham2024specificityanddiversity pages 1-2) | Strong functional application edge. |
| capsule type/volume | modulates | plasmid conjugation efficiency | K. pneumoniae, donor and recipient effects | strong | 10.1038/s41467-024-46147-5 | “Capsule types also influence conjugation efficiency in both donor and recipient cells, a mechanism shaped by capsule volume and conjugative pilus structure” (haudiquet2024capsulesandtheir pages 1-2) | Strong but taxon-specific; avoid broad generalization to all bacteria. |
| TviE/TviD missense mutations | alter | Vi intensity/length/acetylation | Salmonella Typhi Vi capsule variants | strong | 10.1038/s41467-024-49590-6 | “single point mutations leads to the variant form of Vi, whose intensity, length, and/or acetylation are different from WT Vi” (lee2024singlemissensemutations pages 1-2) | Important trait-variation edge in capsule subtype branch. |
| hypo Vi capsule variants | increase | host-cell invasion | Salmonella Typhi; microscopy infection assays | strong | 10.1038/s41467-024-49590-6 | “hypo Vi capsule variants significantly enhanced the infectivity of S. Typhi by 2-3 fold” (lee2024singlemissensemutations pages 5-6) | Quantitative and taxon-specific; curate with assay note (Henle-407 / mouse infection context). |
| hyper Vi capsule variant tviE P263S | increases | mouse mortality/hypervirulence | Salmonella Typhi in Cmah null mice | strong | 10.1038/s41467-024-49590-6 | “resulting in the death of 50% of the infected mice by day 3 post infection” (lee2024singlemissensemutations pages 5-6) | Strong but very specific genotype/host-model edge; not a generic capsule rule. |


*Table: This table lists conservative, curation-ready candidate causal edges for the microbial capsule trait, grounded in DOI-backed evidence from canonical and recent sources. It emphasizes pathway mechanics, export, regulation-relevant functions, and taxon-specific host interaction effects while flagging where generalization should be cautious.*

---

### Current Understanding (2023–2024) and Latest Research
- **Wzx/Wzy Pathway:** Key steps include initiation by WcaJ/WbaP (Und-PP-linked sugar), flippase-mediated membrane transit (Wzx), repeat unit polymerization (Wzy), chain-length regulation (Wzc), outer membrane export (Wza), and surface organization (Wzi). These processes are structurally documented (whitfield2020assemblyofbacterial pages 5-6, whitfield2020assemblyofbacterial pages 7-9, whitfield2020assemblyofbacterial pages 9-10, rendueles2020decipheringtherole pages 2-4).
- **ABC Transporter Pathway:** Recent cryo-EM (Kuklewicz & Zimmer, 2024) reveals that the ABC transporter KpsMT recognizes a Kdo-glycolipid anchor and is sufficient to drive inner-membrane CPS translocation via ATP hydrolysis. KpsE forms a periplasmic cage helping to organize translocation; KpsD outer-membrane export is required for full surface expression (kuklewicz2024molecularinsightsinto pages 1-2, kuklewicz2024molecularinsightsinto pages 2-3).
- **Regulatory Network:** Capsule biosynthesis is regulated by metabolic status, oxygen, iron, cAMP, quorum sensing, small RNAs, and global factors (TviA, RcsA, RcsB, OmpR in S. Typhi and K. pneumoniae) (gao2024bacterialcapsulesoccurrence pages 9-10, lee2024singlemissensemutations pages 1-2).
- **Serotype Effects and Host Interaction:** Capsule serotype determines phage susceptibility and conjugation efficiency via structural/volumetric properties (Haudiquet et al, 2024). Missense mutations in Vi biosynthesis genes modulate S. Typhi virulence and invasion (Lee & Song, 2024). Capsule loss, swap, or enzymatic depolymerization dramatically impacts immune evasion and biofilm capacity (haudiquet2024capsulesandtheir pages 1-2, lee2024singlemissensemutations pages 5-6, cheetham2024specificityanddiversity pages 1-2).
- **Phage, Depolymerase, and Conjugation:** Capsule depolymerases degrade the layer, increasing susceptibility to serum/complement and enabling new antimicrobial strategies (Cheetham et al, 2024; Yang et al, 2025) (cheetham2024specificityanddiversity pages 1-2, yang2025identificationofa pages 1-2).

---

### Real-World Implementations and Applications
- **Vaccines:** Capsule polysaccharides and conjugates form the basis for prominent vaccines (e.g., S. pneumoniae, N. meningitidis, K. pneumoniae experimental), though serotype diversity and compensatory mechanisms create design challenges.
- **Phage Therapy & Glycoengineering:** Capsule depolymerase enzymes and engineered phages show efficacy against multidrug-resistant pathogens (clinical K64 CRKP, K1/K2 hypervirulent Klebsiella), with recombinant depolymerase raising larval survival to 73% (yang2025identificationofa pages 1-2).
- **Antimicrobial Resistance:** Capsule structure modulates acquisition and spread of conjugative plasmids (including those conferring resistance) and convergence of AMR and virulence via capsule-permissive F-pili (haudiquet2024capsulesandtheir pages 1-2).

---

### Statistics and Recent DataHighlights
- **Capsule Loss/Swap:** Capsule locus swaps invert phage susceptibility in Klebsiella; capsule loss increases conjugation rates by up to an order of magnitude in controlled swaps (haudiquet2024capsulesandtheir pages 2-3).
- **Vi Capsule Alterations:** S. Typhi clinical missense variants are globally distributed; hypo- and hyper-Vi variants alter mouse virulence (mortality ≥50% with hyper-Vi S. Typhi; invasion up 2–3x with hypo-Vi) (lee2024singlemissensemutations pages 5-6).
- **Antimicrobial Effect:** Phage depolymerase plus kanamycin treated K64 CRKP biofilms boosts larval survival to >70% in infection model; capsule removal increases serum killing (yang2025identificationofa pages 1-2).

---

### Ontology Grounding
A majority of biochemical steps may be grounded to GO, CHEBI, EC, and UniProt accessions as contextualized in the artifact-01 table. Many nodes require label-only curation due to taxon/assay-specificity or lack of universal ontology coverage.

---

### Warnings and Outstanding Uncertainties
- Capsule function, structure, and export are highly taxon- and serotype-dependent; do not generalize fine mechanistic claims across distant bacteria.
- Synthase-dependent systems and protein capsules need more taxon-focused curation.
- Some enzyme assignments, regulatory interactions, and structural attributes remain experimentally unresolved or node-label only (esp. in recent environmental or clinical isolates) (gao2024bacterialcapsulesoccurrence pages 3-3, gao2024bacterialcapsulesoccurrence pages 1-3).

---

### DOI-First Bibliography

#### Canonical/canonical reviews:
- Roberts, IS. Annual Review of Microbiology, 1996. https://doi.org/10.1146/annurev.micro.50.1.285 (roberts1996thebiochemistryand pages 1-3)
- Whitfield, C. et al. Annual Review of Microbiology, 2020. https://doi.org/10.1146/annurev-micro-011420-075607 (whitfield2020assemblyofbacterial pages 1-2, whitfield2020assemblyofbacterial pages 5-6)

#### Recent developments (2023–2024 primary research):
- Kuklewicz, J. & Zimmer, J. Nature, 2024. https://doi.org/10.1038/s41586-024-07248-9 (kuklewicz2024molecularinsightsinto pages 1-2, kuklewicz2024molecularinsightsinto pages 2-3)
- Gao, S. et al. npj Biofilms and Microbiomes, 2024. https://doi.org/10.1038/s41522-024-00497-6 (gao2024bacterialcapsulesoccurrence pages 1-3, gao2024bacterialcapsulesoccurrence pages 9-10, gao2024bacterialcapsulesoccurrence pages 3-3)
- Haudiquet, M. et al. Nature Communications, 2024. https://doi.org/10.1038/s41467-024-46147-5 (haudiquet2024capsulesandtheir pages 1-2, haudiquet2024capsulesandtheir pages 2-3)
- Lee, G.Y. & Song, J. Nature Communications, 2024. https://doi.org/10.1038/s41467-024-49590-6 (lee2024singlemissensemutations pages 1-2, lee2024singlemissensemutations pages 5-6)
- Cheetham, M.J. et al. Essays in Biochemistry, 2024. https://doi.org/10.1042/EBC20240015 (cheetham2024specificityanddiversity pages 1-2)
- Yang, P. et al. Journal of Bacteriology, 2025. https://doi.org/10.1128/jb.00387-24 (yang2025identificationofa pages 1-2)

---

This curation report is designed for direct transfer to TraitMech YAML curation and as a guide for mechanistic graph expansion, pathway curation, and phenotype modeling for the capsule trait.


References

1. (roberts1996thebiochemistryand pages 1-3): Ian S. Roberts. The biochemistry and genetics of capsular polysaccharide production in bacteria. Annual review of microbiology, 50:285-315, Oct 1996. URL: https://doi.org/10.1146/annurev.micro.50.1.285, doi:10.1146/annurev.micro.50.1.285. This article has 977 citations and is from a peer-reviewed journal.

2. (whitfield2020assemblyofbacterial pages 1-2): Chris Whitfield, Samantha S. Wear, and Caitlin Sande. Assembly of bacterial capsular polysaccharides and exopolysaccharides. Sep 2020. URL: https://doi.org/10.1146/annurev-micro-011420-075607, doi:10.1146/annurev-micro-011420-075607. This article has 346 citations and is from a peer-reviewed journal.

3. (whitfield2020assemblyofbacterial pages 9-10): Chris Whitfield, Samantha S. Wear, and Caitlin Sande. Assembly of bacterial capsular polysaccharides and exopolysaccharides. Sep 2020. URL: https://doi.org/10.1146/annurev-micro-011420-075607, doi:10.1146/annurev-micro-011420-075607. This article has 346 citations and is from a peer-reviewed journal.

4. (whitfield2020assemblyofbacterial pages 2-4): Chris Whitfield, Samantha S. Wear, and Caitlin Sande. Assembly of bacterial capsular polysaccharides and exopolysaccharides. Sep 2020. URL: https://doi.org/10.1146/annurev-micro-011420-075607, doi:10.1146/annurev-micro-011420-075607. This article has 346 citations and is from a peer-reviewed journal.

5. (gao2024bacterialcapsulesoccurrence pages 1-3): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, L. Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. npj Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 88 citations and is from a peer-reviewed journal.

6. (whitfield2020assemblyofbacterial pages 5-6): Chris Whitfield, Samantha S. Wear, and Caitlin Sande. Assembly of bacterial capsular polysaccharides and exopolysaccharides. Sep 2020. URL: https://doi.org/10.1146/annurev-micro-011420-075607, doi:10.1146/annurev-micro-011420-075607. This article has 346 citations and is from a peer-reviewed journal.

7. (kuklewicz2024molecularinsightsinto pages 1-2): Jeremi Kuklewicz and Jochen Zimmer. Molecular insights into capsular polysaccharide secretion. Nature, 628:901-909, Apr 2024. URL: https://doi.org/10.1038/s41586-024-07248-9, doi:10.1038/s41586-024-07248-9. This article has 38 citations and is from a highest quality peer-reviewed journal.

8. (whitfield2020assemblyofbacterial pages 10-11): Chris Whitfield, Samantha S. Wear, and Caitlin Sande. Assembly of bacterial capsular polysaccharides and exopolysaccharides. Sep 2020. URL: https://doi.org/10.1146/annurev-micro-011420-075607, doi:10.1146/annurev-micro-011420-075607. This article has 346 citations and is from a peer-reviewed journal.

9. (gao2024bacterialcapsulesoccurrence pages 3-3): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, L. Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. npj Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 88 citations and is from a peer-reviewed journal.

10. (rendueles2020decipheringtherole pages 2-4): Olaya Rendueles. Deciphering the role of the capsule of <i>klebsiella pneumoniae</i> during pathogenesis: a cautionary tale. Molecular Microbiology, 113:883-888, Feb 2020. URL: https://doi.org/10.1111/mmi.14474, doi:10.1111/mmi.14474. This article has 91 citations and is from a domain leading peer-reviewed journal.

11. (whitfield2020assemblyofbacterial pages 7-9): Chris Whitfield, Samantha S. Wear, and Caitlin Sande. Assembly of bacterial capsular polysaccharides and exopolysaccharides. Sep 2020. URL: https://doi.org/10.1146/annurev-micro-011420-075607, doi:10.1146/annurev-micro-011420-075607. This article has 346 citations and is from a peer-reviewed journal.

12. (lee2024singlemissensemutations pages 1-2): Gi Young Lee and Jeongmin Song. Single missense mutations in vi capsule synthesis genes confer hypervirulence to salmonella typhi. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49590-6, doi:10.1038/s41467-024-49590-6. This article has 19 citations and is from a highest quality peer-reviewed journal.

13. (kuklewicz2024molecularinsightsinto pages 2-3): Jeremi Kuklewicz and Jochen Zimmer. Molecular insights into capsular polysaccharide secretion. Nature, 628:901-909, Apr 2024. URL: https://doi.org/10.1038/s41586-024-07248-9, doi:10.1038/s41586-024-07248-9. This article has 38 citations and is from a highest quality peer-reviewed journal.

14. (lee2024singlemissensemutations pages 5-6): Gi Young Lee and Jeongmin Song. Single missense mutations in vi capsule synthesis genes confer hypervirulence to salmonella typhi. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49590-6, doi:10.1038/s41467-024-49590-6. This article has 19 citations and is from a highest quality peer-reviewed journal.

15. (gao2024bacterialcapsulesoccurrence pages 9-10): Shuji Gao, Wenjie Jin, Yingying Quan, Yue Li, Yamin Shen, Shuo Yuan, L. Yi, Yuxin Wang, and Yang Wang. Bacterial capsules: occurrence, mechanism, and function. npj Biofilms and Microbiomes, Mar 2024. URL: https://doi.org/10.1038/s41522-024-00497-6, doi:10.1038/s41522-024-00497-6. This article has 88 citations and is from a peer-reviewed journal.

16. (yang2025identificationofa pages 1-2): Peini Yang, Bin Shan, Xing Hu, Li Xue, Guibo Song, Pingan He, and Xu Yang. Identification of a novel phage depolymerase against st11 k64 carbapenem-resistant <i>klebsiella pneumoniae</i> and its therapeutic potential. Journal of Bacteriology, Apr 2025. URL: https://doi.org/10.1128/jb.00387-24, doi:10.1128/jb.00387-24. This article has 15 citations and is from a peer-reviewed journal.

17. (haudiquet2024capsulesandtheir pages 1-2): Matthieu Haudiquet, Julie Le Bris, Amandine Nucci, Rémy A. Bonnin, Pilar Domingo-Calap, Eduardo P. C. Rocha, and Olaya Rendueles. Capsules and their traits shape phage susceptibility and plasmid conjugation efficiency. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46147-5, doi:10.1038/s41467-024-46147-5. This article has 79 citations and is from a highest quality peer-reviewed journal.

18. (cheetham2024specificityanddiversity pages 1-2): Max J. Cheetham, Yunlong Huo, Maria Stroyakovski, Li Cheng, Daniel Wan, Anne Dell, and Joanne M. Santini. Specificity and diversity of klebsiella pneumoniae phage-encoded capsule depolymerases. Essays in Biochemistry, 68:661-677, Dec 2024. URL: https://doi.org/10.1042/ebc20240015, doi:10.1042/ebc20240015. This article has 36 citations and is from a peer-reviewed journal.

19. (haudiquet2024capsulesandtheir pages 2-3): Matthieu Haudiquet, Julie Le Bris, Amandine Nucci, Rémy A. Bonnin, Pilar Domingo-Calap, Eduardo P. C. Rocha, and Olaya Rendueles. Capsules and their traits shape phage susceptibility and plasmid conjugation efficiency. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46147-5, doi:10.1038/s41467-024-46147-5. This article has 79 citations and is from a highest quality peer-reviewed journal.