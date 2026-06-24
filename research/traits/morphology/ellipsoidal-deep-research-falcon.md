---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:35:11.322301'
end_time: '2026-06-18T08:04:01.189274'
duration_seconds: 1729.87
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: ellipsoidal
  trait_identifier: METPO:1000673
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: ellipsoidal
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has an oval or ellipse morphology,
    elongated along one axis with rounded ends, intermediate between spherical and
    rod-shaped.
  parent_traits: METPO:1000666
  synonyms: ''
  evidence_summary: 'DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports
    ellipsoidal bacterial morphology as a named ovococcal shape class.)'
  causal_graph_summary: 'ellipsoidal_ovococcal_elongation: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 66
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ellipsoidal
- **METPO identifier:** METPO:1000673
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an oval or ellipse morphology, elongated along one axis with rounded ends, intermediate between spherical and rod-shaped.
- **Parent traits:** METPO:1000666
- **Synonyms:** 
- **Existing evidence:** DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports ellipsoidal bacterial morphology as a named ovococcal shape class.)
- **Existing causal graph summary:** ellipsoidal_ovococcal_elongation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **ellipsoidal** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ellipsoidal.yaml`.

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
- **Trait label:** ellipsoidal
- **METPO identifier:** METPO:1000673
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an oval or ellipse morphology, elongated along one axis with rounded ends, intermediate between spherical and rod-shaped.
- **Parent traits:** METPO:1000666
- **Synonyms:** 
- **Existing evidence:** DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports ellipsoidal bacterial morphology as a named ovococcal shape class.)
- **Existing causal graph summary:** ellipsoidal_ovococcal_elongation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **ellipsoidal** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/ellipsoidal.yaml`.

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


# Research Report: Microbial trait **ellipsoidal** (METPO:1000673) as a TraitMech causal graph candidate

## 0. Scope summary (curation intent)
The METPO trait **ellipsoidal** (METPO:1000673) corresponds to the *ovococcal/ovoid* bacterial morphology class: elongated ellipsoids (often described as “egg” or “rugby-ball” shaped) that are intermediate between spherical cocci and rods. Authoritative reviews explicitly describe ovococci as “elongated ellipsoids” (e.g., streptococci, enterococci, lactococci) and distinguish them from truly round cocci by the presence of **two coordinated peptidoglycan (PG) synthesis modes**—septal and peripheral—rather than septal-only synthesis (zapun2008thedifferentshapes pages 1-2, pinho2013howtoget pages 2-3). Mechanistically, ellipsoidal shape is maintained by the balance, spatial organization, and regulation of these two PG-synthesis systems at midcell (perez2021organizationofpeptidoglycan pages 1-5, perez2021organizationofpeptidoglycan pages 43-53).

**Boundary cases and distinctions.**
* Ellipsoidal (ovococcal) vs spherical cocci: spherical cocci are described as relying mainly on septal PG synthesis, whereas ovococci use both septal and peripheral synthesis, giving an elongated ellipsoid shape (pinho2013howtoget pages 2-3).  
* Ellipsoidal vs rods: many ovococci lack MreB-like proteins; rod elongation typically involves MreB-directed lateral wall synthesis, whereas ovococci organize elongation differently (tavares2019determinationofcell pages 46-50, tavares2019determinationofcella pages 46-50).  
* Ellipsoidal shape vs capsule-driven apparent shape: capsule polysaccharide (CPS) localization can be organized by the divisome independent of the elongasome, meaning external appearance can change without altering the underlying PG synthesis program (nakamoto2023thedivisomebut pages 6-7, nakamoto2023thedivisomebut pages 2-3).

## 1. Key concepts and current understanding (definitions + mechanistic model)
### 1.1 Definition (phenotype)
Ovococci are defined in the literature as **ellipsoid-shaped cocci** (“elongated ellipsoids”) including *Enterococcus*, *Streptococcus*, and *Lactococcus* (zapun2008thedifferentshapes pages 1-2). In a widely cited review, “Ovococcal cells, with an ellipsoid shape” are contrasted with spherical cocci, and the shape difference is linked to distinct modes of cell-wall synthesis (pinho2013howtoget pages 2-3).

### 1.2 Mechanistic definition (what produces ellipsoidal shape)
Ellipsoidal/ovococcal shape in *Streptococcus pneumoniae* is classically described as arising from a combination of **septal** and **peripheral (sidewall-like)** PG synthesis that are both active at midcell and can be resolved as separate spatial structures (straume2017identificationofpneumococcal pages 1-5, perez2021organizationofpeptidoglycan pages 1-5). A primary super-resolution study demonstrates that septal vs peripheral synthesis segregate into **two concentric rings at midcell** (inner septal ring vs outer peripheral ring), providing a physical basis for simultaneously generating a septum while maintaining a prolate/ellipsoid sidewall geometry (perez2021organizationofpeptidoglycan pages 1-5, perez2021organizationofpeptidoglycan pages 43-53).

## 2. Candidate causal-graph nodes (grouped; with ontology grounding suggestions)
A curation-oriented node inventory (including proposed CURIEs where possible) is provided here:

| Node label | Node type | Suggested CURIE(s) | Evidence context | Grounding confidence | Notes |
|---|---|---|---|---|---|
| Peptidoglycan biosynthesis | process | GO:0009252 | Core determinant of ovococcal/ellipsoidal shape across *Streptococcus pneumoniae* and related ovococci; shape maintained by PG synthesis/remodeling (pinho2013howtoget pages 2-3, tsui2016suppressionofa pages 1-3, zapun2008thedifferentshapes pages 1-2, perez2021organizationofpeptidoglycan pages 1-5) | high | Central parent process for most candidate edges |
| Septal peptidoglycan synthesis | process | GO:0009252 | Inner-ring/leading-edge synthesis at division septum in *S. pneumoniae*; more sensitive to Und-P limitation (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12, perez2021organizationofpeptidoglycan pages 43-53, perez2021organizationofpeptidoglycan pages 1-5) | medium | GO term for septal-specific subtype not confidently assigned here; label-level subtype useful |
| Peripheral peptidoglycan synthesis | process | GO:0009252 | Outer-ring/peripheral synthesis linked to elongation in ovococci; controlled by PBP2b/RodA/MreCD/DivIVA (pinho2013howtoget pages 2-3, jiang2023divivainteractswith pages 2-4, straume2017identificationofpneumococcal pages 1-5, perez2021organizationofpeptidoglycan pages 43-53) | medium | Label-level subtype recommended if no stable GO subtype is curated |
| Ellipsoidal morphology | process | METPO:1000673 | Trait node; ovococci described as elongated ellipsoids shaped by septal + peripheral PG synthesis (pinho2013howtoget pages 2-3, zapun2008thedifferentshapes pages 1-2) | high | Target trait |
| Elongasome / Rod complex | complex | GO:0043190 | Peripheral PG machinery containing PBP2b/RodA/MreD/DivIVA and accessory proteins in pneumococcus (straume2017identificationofpneumococcal pages 1-5, straume2017identificationofpneumococcal pages 47-54, perez2021organizationofpeptidoglycan pages 43-53) | medium | Complex label acceptable; GO cellular-component mapping approximate |
| Divisome | complex | GO:0043190 | Septal PG synthesis machinery organizing inner ring and CPS recruitment (nakamoto2023thedivisomebut pages 1-2, nakamoto2023thedivisomebut pages 2-3, perez2021organizationofpeptidoglycan pages 43-53) | medium | Complex label acceptable; no single universally used stable complex CURIE identified here |
| FtsEX:PcsB complex/system | complex |  | Outer pPG machine model includes FtsEX:PcsB; PcsB linked to splitting/elongation balance (perez2021organizationofpeptidoglycan pages 43-53, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 20-21) | low | Keep as label-level complex unless curated identifiers are added later |
| CpsCD tyrosine-kinase capsule organizer | complex |  | Capsule system recruited by divisome, not elongasome (nakamoto2023thedivisomebut pages 1-2, nakamoto2023thedivisomebut pages 2-3) | low | Useful boundary node; identifier left blank |
| FtsZ | gene/protein |  | Central divisome protein; localizes with inner septal ring and coordinates septation/elongation geometry (xiang2019regulationofcell pages 24-30, perez2021organizationofpeptidoglycan pages 43-53, perez2021organizationofpeptidoglycan pages 7-10, perez2021organizationofpeptidoglycan pages 1-5) | medium | Sequence-specific IDs are taxon-specific; leave blank in generic trait graph |
| FtsW | gene/protein |  | Septal glycosyltransferase partner in inner sPG machine with PBP2x (nakamoto2023thedivisomebut pages 3-4, perez2021organizationofpeptidoglycan pages 43-53) | medium | SEDS family division synthase |
| RodA | gene/protein |  | Peripheral glycosyltransferase partner with PBP2b; elongasome core (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 15-16, straume2017identificationofpneumococcal pages 1-5, perez2021organizationofpeptidoglycan pages 43-53) | medium | SEDS family elongation synthase |
| PBP2b | gene/protein | EC:3.4.16.- | Essential peripheral/transpeptidase component for elongasome and ovoid shape (straume2017identificationofpneumococcal pages 12-16, straume2017identificationofpneumococcal pages 1-5, straume2017identificationofpneumococcal pages 5-9, perez2021organizationofpeptidoglycan pages 13-16) | medium | Class B PBP; EC broad because exact substrate-specific EC not curated here |
| PBP2x | gene/protein | EC:3.4.16.- | Inner septal-ring transpeptidase in divisome/sPG machine (nakamoto2023thedivisomebut pages 3-4, perez2021organizationofpeptidoglycan pages 43-53, perez2021organizationofpeptidoglycan pages 13-16, perez2021organizationofpeptidoglycan pages 5-7) | medium | Septal class B PBP |
| PBP1a | gene/protein | EC:3.4.16.- | Localization and activity restricted by CozE/MreCD; implicated in peripheral/zonal PG patterning (fenton2016cozeisa pages 2-4, xiang2019regulationofcell pages 24-30) | medium | Class A PBP |
| MreC | gene/protein |  | Peripheral PG regulator; part of MreCD/CozE system; loss causes shape defects (fenton2016cozeisa pages 2-4, xiang2019regulationofcell pages 24-30, land2011therequirementfor pages 1-2) | medium | Generic label favored over taxon-specific accession |
| MreD | gene/protein |  | Peripheral PG regulator; functionally linked to PBP2b and elongasome (straume2017identificationofpneumococcal pages 12-16, straume2017identificationofpneumococcal pages 1-5, land2011therequirementfor pages 1-2) | medium | Generic label favored |
| CozE | gene/protein |  | Member of MreCD complex directing cell elongation and PBP1a localization (fenton2016cozeisa pages 2-4) | medium | Taxon-specific but mechanistically informative |
| DivIVA | gene/protein | GO:0005524 | Regulates peripheral PG synthesis and aspect ratio; localizes elongation machinery; phosphorylation-sensitive in streptococci (jiang2023divivainteractswith pages 2-4, fleurie2014interplayofthe pages 7-10, straume2017identificationofpneumococcal pages 16-19) | medium | Generic protein node; GO chosen only for molecular-function grounding is weak, so label may be preferable |
| StkP (Ser/Thr kinase) | gene/protein | EC:2.7.11.1 | Phosphorylates DivIVA / linked regulator of septal-peripheral balance and shape (xiang2019regulationofcell pages 24-30, fleurie2014interplayofthe pages 7-10, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 19-20) | high | Conserved bacterial Ser/Thr protein kinase |
| MltG | gene/protein | EC:4.2.2.- | Cell-wall hydrolase interacting with DivIVA; affects peripheral PG synthesis and roundness (jiang2023divivainteractswith pages 9-11, jiang2023divivainteractswith pages 7-9, jiang2023divivainteractswith pages 1-2) | medium | Lytic transglycosylase/hydrolase; EC approximate |
| FtsX | gene/protein |  | Outer peripheral ring component; part of FtsEX:PcsB module in pPG machine (perez2021organizationofpeptidoglycan pages 43-53, perez2021organizationofpeptidoglycan pages 7-10, perez2021organizationofpeptidoglycan pages 1-5) | medium | Generic membrane division protein |
| PcsB | gene/protein |  | PG hydrolase/splitting factor affecting elongation balance; part of FtsEX:PcsB system (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 20-21, perez2021organizationofpeptidoglycan pages 43-53) | medium | Keep as label-level unless accession added later |
| Spr0777 | gene/protein |  | Accessory elongasome component/functionally linked to PBP2b and DivIVA localization in *S. pneumoniae* (straume2017identificationofpneumococcal pages 47-54, straume2017identificationofpneumococcal pages 12-16) | low | Locus-specific; grounding unresolved |
| CpsC | gene/protein |  | Capsule machinery organizer recruited by divisome; not dependent on elongasome (nakamoto2023thedivisomebut pages 2-3, nakamoto2023thedivisomebut pages 3-4, nakamoto2023thedivisomebut pages 4-6) | medium | Boundary/control node for non-shape appearance effects |
| Capsule polysaccharide synthesis | process | GO:0033692 | Organized by divisome, not elongasome; can affect appearance without changing PG shape program (nakamoto2023thedivisomebut pages 1-2, nakamoto2023thedivisomebut pages 6-7) | medium | Important warning node |
| Mevalonate pathway | pathway | KEGG:map00900 | Downregulation causes elongation through Und-P limitation in pneumococcus (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 2-3, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 7-9) | high | Pathway-level driver of precursor supply |
| Isoprenoid biosynthesis | pathway | GO:0008299 | Supplies precursors for Und-P; implicated by mevalonate depletion phenotype (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 7-9) | high | Broader parent of mevalonate-derived precursor supply |
| Undecaprenyl phosphate (Und-P) | chemical | CHEBI:16460 | Lipid carrier limiting cell-wall precursor transport; preferentially impacts septal synthesis (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 2-3, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12) | high | Key chemical mediator of precursor limitation |
| UppS (undecaprenyl diphosphate synthase) | gene/protein | EC:2.5.1.31 | Depletion phenocopies mevalonate depletion and causes unconstricted elongated cells (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12) | high | Strong mechanistic node for Und-P synthesis |
| Clomiphene | chemical | CHEBI:3747 | Chemical perturbant that blocks Und-P production and elongates cells; potentiates amoxicillin in vitro (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 20-21, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 2-3, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 15-16) | high | Drug node; mechanism partly cross-validated across taxa |
| Amoxicillin | chemical | CHEBI:2676 | β-lactam whose activity is potentiated by clomiphene/Und-P limitation; elongation-associated phenotype comparator (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 20-21, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 18-19, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 15-16) | high | Application node, not core morphology determinant |
| Capsule polysaccharide (CPS) | chemical |  | External envelope component whose localization can change without affecting core shape/FDAA pattern (nakamoto2023thedivisomebut pages 1-2, nakamoto2023thedivisomebut pages 6-7) | low | Label-level chemical/material node |
| HADA labeling | assay |  | FDAA probe used to visualize peripheral/nascent PG and DivIVA/MltG phenotypes (jiang2023divivainteractswith pages 7-9, jiang2023divivainteractswith pages 4-6, jiang2023divivainteractswith pages 2-4) | low | Assay node; chemical identity not grounded here |
| TADA labeling | assay |  | Short-pulse FDAA assay resolving nodal TP activity and concentric rings (fenton2016cozeisa pages 2-4, perez2021organizationofpeptidoglycan pages 43-53, perez2021organizationofpeptidoglycan pages 13-16, perez2021organizationofpeptidoglycan pages 7-10) | low | Assay node |
| FDAA labeling | assay |  | General fluorescent D-amino-acid labeling of nascent PG in septal/peripheral synthesis studies (nakamoto2023thedivisomebut pages 1-2, nakamoto2023thedivisomebut pages 2-3, perez2021organizationofpeptidoglycan pages 5-7, perez2021organizationofpeptidoglycan pages 1-5) | low | Group assay node |
| 3D-SIM imaging | assay |  | Used to resolve concentric rings and nodal organization in ovococci (perez2021organizationofpeptidoglycan pages 13-16, perez2021organizationofpeptidoglycan pages 5-7, perez2021organizationofpeptidoglycan pages 1-5) | low | Imaging-method node |
| dSTORM imaging | assay |  | Used to quantify nanoscale septal vs peripheral PG dynamics and band geometry (trouve2021nanoscaledynamicsof pages 10-11, trouve2021nanoscaledynamicsof pages 20-20) | low | Imaging-method node |
| Negative membrane curvature at septal–lateral interface | environment |  | Region where DivIVA localizes elongasome in pneumococcus (straume2017identificationofpneumococcal pages 16-19, straume2017identificationofpneumococcal pages 1-5) | low | Spatial/contextual node useful for localization edges |
| *Streptococcus pneumoniae* | environment | NCBITaxon:1313 | Main mechanistic model for ovococcal/ellipsoidal morphology (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2, straume2017identificationofpneumococcal pages 1-5, perez2021organizationofpeptidoglycan pages 43-53, perez2021organizationofpeptidoglycan pages 1-5) | high | Consider as taxon context, not mechanistic node |
| *Streptococcus suis* | environment | NCBITaxon:1307 | 2023 DivIVA phosphorylation–MltG–aspect-ratio evidence (jiang2023divivainteractswith pages 9-11, jiang2023divivainteractswith pages 2-4, jiang2023divivainteractswith pages 1-2) | high | Consider as taxon context, not mechanistic node |
| *Enterococcus faecalis* | environment | NCBITaxon:1351 | Conserved nodal spacing in another ovococcus (perez2021organizationofpeptidoglycan pages 16-18, perez2021organizationofpeptidoglycan pages 13-16) | high | Supports broader generality of geometry |
| *Streptococcus mitis* | environment | NCBITaxon:28037 | Conserved nodal spacing in related ovococcus (perez2021organizationofpeptidoglycan pages 16-18, perez2021organizationofpeptidoglycan pages 13-16) | high | Supports broader generality of geometry |


*Table: This table lists candidate causal-graph nodes for ellipsoidal/ovococcal morphology, with suggested ontology grounding, evidence context, and confidence notes. It is designed to support curation of node inventories before final edge selection.*

## 3. Evidence-backed candidate causal edges (triples)
A curation-oriented table of candidate edges (subject–predicate–object) with supporting snippets, DOI/year/URL, context, and curation flags is provided here:

| Edge (S–P–O) | Evidence snippet (verbatim short quote) | Reference (DOI, year, URL) | Taxon/context | Notes/curation flags |
|---|---|---|---|---|
| DivIVA phosphorylation state → regulates → peripheral PG synthesis length | “peripheral PG is longer in DivIVA3A and shorter in DivIVA3E” (jiang2023divivainteractswith pages 4-6) | 10.1128/Spectrum.04750-22, 2023, https://doi.org/10.1128/spectrum.04750-22 | *Streptococcus suis* | Strong; direct mutant phenotype; assay-specific to HADA/TADA labeling |
| DivIVA phosphorylation state → affects → cell length/aspect ratio | “DivIVA3A cells are significantly longer, whereas DivIVA3E cells are shorter but wider” (jiang2023divivainteractswith pages 4-6) | 10.1128/Spectrum.04750-22, 2023, https://doi.org/10.1128/spectrum.04750-22 | *S. suis* | Strong; direct morphology phenotype |
| DivIVA deletion → decreases → aspect ratio / causes rounder cells | “smaller cell length and larger width, resulting in a significantly decreased aspect ratio,” and “signiﬁcantly rounder” (jiang2023divivainteractswith pages 2-4) | 10.1128/Spectrum.04750-22, 2023, https://doi.org/10.1128/spectrum.04750-22 | *S. suis* | Strong; direct loss-of-function evidence |
| DivIVA deletion → aborts → peripheral PG synthesis | “nearly no peripheral PG was synthesized in the DdivIVA cells” (jiang2023divivainteractswith pages 2-4) | 10.1128/Spectrum.04750-22, 2023, https://doi.org/10.1128/spectrum.04750-22 | *S. suis* | Strong; direct microscopy evidence |
| DivIVA → regulates → MltG localization | “GFP-MltG localizes to mid-cell in wild type but is dispersed in DdivIVA” (jiang2023divivainteractswith pages 7-9) | 10.1128/Spectrum.04750-22, 2023, https://doi.org/10.1128/spectrum.04750-22 | *S. suis* | Strong; localization-based |
| DivIVA phosphomimetic state (DivIVA3E) → impairs → MltG mid-cell localization | “mid-cell localization is impaired in DivIVA3E while normal in DivIVA3A” (jiang2023divivainteractswith pages 7-9) | 10.1128/Spectrum.04750-22, 2023, https://doi.org/10.1128/spectrum.04750-22 | *S. suis* | Strong; direct comparison of phosphomutants |
| DivIVA → interacts with → MltG | “identified an interaction between DivIVA and the cell wall hydrolase MltG” (jiang2023divivainteractswith pages 4-6) | 10.1128/Spectrum.04750-22, 2023, https://doi.org/10.1128/spectrum.04750-22 | *S. suis* | Strong; co-IP/B2H context |
| MltG loss/disruption → causes → shorter, wider, rounder cells | “DmltG and DivIVA3E cells are also shorter and wider” and “formed significantly rounder cells” (jiang2023divivainteractswith pages 9-11, jiang2023divivainteractswith pages 1-2) | 10.1128/Spectrum.04750-22, 2023, https://doi.org/10.1128/spectrum.04750-22 | *S. suis* | Strong; direct morphology phenotype |
| Mevalonate pathway downregulation → causes → extensive cell elongation | “downregulation of the mevalonate pathway leads to extensive cell elongation” (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2) | 10.7554/eLife.75607, 2022, https://doi.org/10.7554/eLife.75607 | *Streptococcus pneumoniae* | Strong; CRISPRi and follow-up validation |
| Mevalonate pathway perturbation → limits → Und-P production | “caused by insufficient transport of cell wall precursors… due to a limitation in the production of undecaprenyl phosphate (Und-P)” (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2) | 10.7554/eLife.75607, 2022, https://doi.org/10.7554/eLife.75607 | *S. pneumoniae* | Strong; mechanistic inference supported by genetics |
| Und-P limitation → reduces preferentially → septal PG synthesis / constriction | “septal peptidoglycan synthesis is more sensitive to reduced Und-P levels than peripheral peptidoglycan synthesis” (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2) | 10.7554/eLife.75607, 2022, https://doi.org/10.7554/eLife.75607 | *S. pneumoniae* | Strong; key mechanistic edge |
| Mevalonate depletion → reduces → septal PG synthesis while peripheral synthesis continues | “drastically reduces septal (constriction-associated) peptidoglycan synthesis while peripheral (elongation-associated) synthesis continues” (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12) | 10.7554/eLife.75607, 2022, https://doi.org/10.7554/eLife.75607 | *S. pneumoniae* | Strong; FDAA pulse-labeling |
| uppS depletion → phenocopies → mevalonate depletion elongation phenotype | “deletion/depletion of uppS… phenocopies mevalonate depletion, producing elongated cells with multiple unconstricted Z-rings” (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12) | 10.7554/eLife.75607, 2022, https://doi.org/10.7554/eLife.75607 | *S. pneumoniae* | Strong; direct phenocopy |
| Clomiphene → inhibits/limits → Und-P synthesis | “clomiphene, an FDA-approved drug shown to block Und-P production” (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 2-3) | 10.7554/eLife.75607, 2022, https://doi.org/10.7554/eLife.75607 | *S. pneumoniae* (building on prior *S. aureus* evidence) | Moderate; partly cross-taxon mechanism |
| Clomiphene → causes → elongation phenotype | “clomiphene… was able to increase cell length” (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 15-16) | 10.7554/eLife.75607, 2022, https://doi.org/10.7554/eLife.75607 | *S. pneumoniae* | Strong; direct chemical perturbation |
| Clomiphene + amoxicillin → potentiates → amoxicillin activity | “amoxicillin MICs for resistant strains dropped 16–64-fold” (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 18-19) | 10.7554/eLife.75607, 2022, https://doi.org/10.7554/eLife.75607 | *S. pneumoniae* resistant clinical strains | Strong in vitro; in vivo negative/limited due to lung exposure |
| PBP2b → required for → elongasome function / lateral PG synthesis | “PBP2b is identified as indispensable for lateral PG synthesis and is a key component/marker of the elongasome” (straume2017identificationofpneumococcal pages 1-5) | 10.1111/mmi.13543, 2017, https://doi.org/10.1111/mmi.13543 | *S. pneumoniae* R6 | Strong; direct text + depletion phenotype |
| RodA → functionally linked with → PBP2b in elongasome | “Four proteins, RodA, MreD, DivIVA and Spr0777, were identified… Together with PBP2b these proteins are essential for the normal function of the elongasome” (straume2017identificationofpneumococcal pages 1-5) | 10.1111/mmi.13543, 2017, https://doi.org/10.1111/mmi.13543 | *S. pneumoniae* R6 | Strong; phenotype-matching screen |
| MreD → functionally linked with → PBP2b in elongasome | “RodA, MreD, DivIVA and Spr0777… Together with PBP2b these proteins are essential for the normal function of the elongasome” (straume2017identificationofpneumococcal pages 1-5) | 10.1111/mmi.13543, 2017, https://doi.org/10.1111/mmi.13543 | *S. pneumoniae* R6 | Strong |
| DivIVA → localizes/enables localization of → elongasome at negatively curved septal–lateral interface | “DivIVA… is required to correctly localize the elongasome to the negatively curved membrane region between the septal and lateral cell wall” (straume2017identificationofpneumococcal pages 1-5) | 10.1111/mmi.13543, 2017, https://doi.org/10.1111/mmi.13543 | *S. pneumoniae* R6 | Strong; localization mechanism |
| Spr0777 → cooperates with → PBP2b/RodA/MreD/DivIVA in elongasome | “deletion or depletion of PBP2b, RodA, MreD, DivIVA and Spr0777 produce very similar phenotypes… strong evidence these proteins cooperate to form a functional elongasome” (straume2017identificationofpneumococcal pages 47-54) | 10.1111/mmi.13543, 2017, https://doi.org/10.1111/mmi.13543 | *S. pneumoniae* R6 | Strong; accessory factor; identifier uncertain |
| Loss of PBP2b/RodA/MreD/DivIVA/Spr0777 → shifts cells toward → spherical/chain phenotypes | “deletion or depletion… produce the same set of phenotypes: … long chains of longitudinally compressed cells” (straume2017identificationofpneumococcal pages 12-16) | 10.1111/mmi.13543, 2017, https://doi.org/10.1111/mmi.13543 | *S. pneumoniae* R6 | Strong; phenotype bundle supports shape-maintenance role |
| MreC/MreD → regulate → peripheral PG synthesis | “the authors conclude ‘MreCD regulates peripheral PG synthesis in S. pneumoniae.’” (xiang2019regulationofcell pages 24-30) | 10.21775/CIMB.032.259, 2019, https://doi.org/10.21775/cimb.032.259 | *S. pneumoniae* | Moderate; review quoting primary results |
| CozE + MreCD → direct/restrict → PBP1a midcell localization | “Loss of CozE or MreC causes GFP-PBP1a to lose its tight midcell localization” (fenton2016cozeisa pages 2-4) | 10.1038/nmicrobiol.2016.237, 2016, https://doi.org/10.1038/nmicrobiol.2016.237 | *S. pneumoniae* | Strong; direct localization phenotype |
| CozE/MreCD loss → broadens → peripheral PG pattern | “TADA labeling shifts from a midcell-restricted zone to a widely distributed peripheral pattern” (fenton2016cozeisa pages 2-4) | 10.1038/nmicrobiol.2016.237, 2016, https://doi.org/10.1038/nmicrobiol.2016.237 | *S. pneumoniae* | Strong; direct PG-pattern evidence |
| Divisome (FtsZ/PBP2x/FtsW) → carries out → septal PG synthesis | “an inner sPG machine (bPBP2x TP with FtsW GT)” (perez2021organizationofpeptidoglycan pages 43-53) | 10.1111/mmi.14659, 2021, https://doi.org/10.1111/mmi.14659 | *S. pneumoniae* | Strong; spatial model from primary imaging |
| Elongasome/peripheral machine (PBP2b/RodA/FtsX) → carries out → peripheral PG synthesis | “an outer pPG machine (bPBP2b TP with RodA GT plus Rod complex proteins and FtsEX:PcsB)” (perez2021organizationofpeptidoglycan pages 43-53) | 10.1111/mmi.14659, 2021, https://doi.org/10.1111/mmi.14659 | *S. pneumoniae* | Strong; mechanistic model from primary imaging |
| PBP2x → localizes to → inner septal ring | “bPBP2x localizes to an inner ring (sPG/constricting leading edge)” (perez2021organizationofpeptidoglycan pages 13-16) | 10.1111/mmi.14659, 2021, https://doi.org/10.1111/mmi.14659 | *S. pneumoniae* | Strong; imaging-based |
| PBP2b → localizes to → outer peripheral ring | “bPBP2b localizes primarily to an outer pPG synthesis ring” (perez2021organizationofpeptidoglycan pages 13-16) | 10.1111/mmi.14659, 2021, https://doi.org/10.1111/mmi.14659 | *S. pneumoniae* | Strong; imaging-based |
| Spatial separation of inner sPG and outer pPG rings → enables → concurrent septal and peripheral PG synthesis underlying ellipsoidal shape | “septal and peripheral peptidoglycan (PG) synthesis are spatially separated at midcell into two concentric structures” (perez2021organizationofpeptidoglycan pages 1-5) | 10.1111/mmi.14659, 2021, https://doi.org/10.1111/mmi.14659 | *S. pneumoniae* | Strong; direct mechanistic support for ovococcal shape model |
| Regular nodal organization of TP activity/PBPs → maintains → ordered PG insertion geometry | “about ≈10 nodes per ring in WT, with an average arc spacing of 0.27 ± 0.07 μm” (perez2021organizationofpeptidoglycan pages 16-18) | 10.1111/mmi.14659, 2021, https://doi.org/10.1111/mmi.14659 | *S. pneumoniae*; conserved in *S. mitis*, *Enterococcus faecalis* | Strong; quantitative organization feature |
| Capsule synthesis complex (CpsC/CPS machinery) → organized by → divisome, not elongasome | “capsule (CPS) synthesis in Streptococcus pneumoniae is organized by the divisome, not the elongasome” (nakamoto2023thedivisomebut pages 2-3) | 10.1038/s41467-023-38904-9, 2023, https://doi.org/10.1038/s41467-023-38904-9 | *S. pneumoniae* | Strong; use as warning/boundary rather than core morphology edge |
| Elongasome component deletions (mreC/pbp2B/rodA) → do not alter → CpsC localization | “deletions of elongasome/peripheral PG synthesis components (mreC, pbp2B, rodA)… did not change CpsC localization” (nakamoto2023thedivisomebut pages 3-4) | 10.1038/s41467-023-38904-9, 2023, https://doi.org/10.1038/s41467-023-38904-9 | *S. pneumoniae* | Strong negative edge; supports boundary from capsule pattern |
| Polar re-routing of capsule synthesis → does not affect → overall cell shape/FDAA PG pattern | “overall cell shape and the FDAA labeling pattern remained unaffected” (nakamoto2023thedivisomebut pages 6-7) | 10.1038/s41467-023-38904-9, 2023, https://doi.org/10.1038/s41467-023-38904-9 | *S. pneumoniae* | Strong warning: apparent surface/capsule distribution should not be curated as shape determinant |
| DivIVA deletion → yields → shorter, rounder pneumococci | “ΔdivIVA cells are shorter and rounder” (xiang2019regulationofcell pages 24-30) | 10.21775/CIMB.032.259, 2019, https://doi.org/10.21775/cimb.032.259 | *S. pneumoniae* | Moderate; review summarizes primary data |
| DivIVA → promotes → peripheral PG synthesis | “peripheral PG is impaired in DdivIVA cells” (fleurie2014interplayofthe pages 7-10) | 10.1371/journal.pgen.1004275, 2014, https://doi.org/10.1371/journal.pgen.1004275 | *S. pneumoniae* | Strong; foundational primary evidence |
| Ovococcal/ellipsoidal shape → results from → combined septal and peripheral PG synthesis | “Ovococcal cells, with an ellipsoid shape” and “ovococci use both septal and peripheral peptidoglycan synthesis” (pinho2013howtoget pages 2-3) | 10.1038/nrmicro3088, 2013, https://doi.org/10.1038/nrmicro3088 | Ovococci broadly (*Streptococcus*, *Enterococcus*, *Lactococcus*) | Strong scope edge; review-level, not a single-gene edge |


*Table: This table lists candidate subject–predicate–object edges for curating the ellipsoidal/ovococcal morphology trait, with short evidence quotes, source metadata, taxon context, and curation flags. It prioritizes mechanistic edges around peripheral vs septal peptidoglycan synthesis, regulatory proteins, precursor limitation, and boundary warnings about capsule-driven appearance.*

## 4. Recent developments and latest research (prioritize 2023–2024 where available)
### 4.1 2023: phosphorylation-based regulation of ovococcal aspect ratio via DivIVA–MltG
A 2023 *Microbiology Spectrum* study in *Streptococcus suis* provides a detailed and directly curation-usable mechanistic regulatory module: **DivIVA controls peripheral PG synthesis and cell aspect ratio, with regulation dependent on DivIVA phosphorylation and interaction/localization of the hydrolase MltG**. The work reports that ΔdivIVA cells have “significantly decreased aspect ratio” and “nearly no peripheral PG” and that DivIVA phosphomimetic vs phosphoablative mutants shift cell length/width and the apparent length of peripheral PG incorporation (jiang2023divivainteractswith pages 2-4, jiang2023divivainteractswith pages 4-6). DivIVA phosphorylation state alters interaction with MltG and MltG midcell localization; ΔmltG and DivIVA3E (phosphomimic) yield “significantly rounder cells,” supporting a causal chain from phosphorylation → protein–protein interaction/localization → peripheral PG synthesis → ellipsoidal aspect ratio (jiang2023divivainteractswith pages 7-9, jiang2023divivainteractswith pages 1-2).

### 4.2 2023: capsule synthesis organized by divisome, highlighting a shape-vs-surface-appearance decoupling
A 2023 *Nature Communications* paper demonstrates that in *S. pneumoniae* capsular polysaccharide synthesis is initiated at the septum and is recruited/organized by the **divisome** (FtsZ-dependent), not the elongasome; deletions of elongasome components (mreC, pbp2B, rodA) do not delocalize capsule organizer CpsC (nakamoto2023thedivisomebut pages 2-3, nakamoto2023thedivisomebut pages 3-4). Importantly for trait-scoping, artificially re-routing the capsule anchor CpsC to poles produced polar CPS while “overall cell shape and the FDAA labeling pattern remained unaffected,” emphasizing that **capsule distribution can change without changing the PG morphogenetic program** (nakamoto2023thedivisomebut pages 6-7).

### 4.3 2023: structural basis for SEDS–bPBP PG synthase coupling (contextual mechanistic support)
A 2023 *Nature Communications* structure of the **RodA–PBP2 complex** (in *E. coli*) provides up-to-date support for the general model that a SEDS glycosyltransferase (RodA) and a class B PBP transpeptidase form a coupled core PG assembly machine (doi:10.1038/s41467-023-40483-8; retrieved but not evidence-extracted in detail). While not ovococcus-specific, it strengthens mechanistic plausibility for analogous RodA–PBP2b coupling in ovococci.

**Note on 2024:** a highly relevant 2024 pneumococcal elongasome-dynamics paper (PNAS, doi:10.1073/pnas.2401831121) was listed as unobtainable in this run; thus, the “latest” ovococcus-specific evidence in the accessible corpus is 2023.

## 5. Quantitative data & statistics useful for curation
### 5.1 Nodal geometry of PG synthesis (super-resolution)
In *S. pneumoniae*, transpeptidase activity and PBPs at midcell are organized into **regularly spaced nodes**, with **≈10 nodes per ring** in wild type and **average arc spacing 0.27 ± 0.07 µm**; the nodal pattern is reported as conserved in other ovococci such as *S. mitis* and *Enterococcus faecalis* (perez2021organizationofpeptidoglycan pages 16-18). Node number scales with ring diameter while maintaining characteristic spacing, supporting a potentially conserved geometric organizing principle for ovococcal PG insertion (perez2021organizationofpeptidoglycan pages 13-16).

### 5.2 Precursor-limitation phenotypes and drug synergy metrics
A 2022 *eLife* study reports: 
* **Mevalonate pathway downregulation → extensive elongation** in *S. pneumoniae* (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2).  
* Elongation is attributed to **Undecaprenyl phosphate (Und-P) limitation**, with septal PG synthesis more sensitive than peripheral PG synthesis (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12).  
* **uppS depletion** phenocopies mevalonate depletion (elongated cells with unconstricted Z-rings) (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12).  
* **Clomiphene** (Und-P synthesis inhibitor) has an MIC of **16 µg/ml** for D39V and potentiates amoxicillin about **8-fold** in a sensitive strain and **16–64-fold** in amoxicillin-resistant clinical strains in vitro (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 20-21). 

## 6. Current applications and real-world implementations
### 6.1 Antibiotic adjuvant strategies targeting precursor supply
The Und-P/precursor limitation axis is directly tied to antibiotic potentiation: inhibition of Und-P synthesis (clomiphene) synergizes with amoxicillin and can resensitize resistant pneumococcal strains in vitro (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 18-19, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 2-3). While in vivo efficacy was limited by drug exposure in the cited mouse model (noted in the evidence summary), the mechanistic principle is directly actionable for antimicrobial discovery/optimization efforts (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 18-19).

### 6.2 Capsule localization and vaccine/immune evasion implications (boundary to shape)
Because capsule synthesis is organized by the divisome and septal capsule positioning affects complement deposition (“vulnerable to complement attacks”), understanding the divisome–capsule coordination is relevant to virulence and vaccine design, but it should be curated as a *capsule localization* causal module rather than a direct ellipsoidal-shape determinant (nakamoto2023thedivisomebut pages 6-7, nakamoto2023thedivisomebut pages 1-2).

## 7. Expert opinions / authoritative synthesis (for curatorial framing)
High-citation reviews emphasize that coccal/ovococcal morphology is a consequence of the spatiotemporal control of PG synthesis machineries (divisome vs peripheral/elongation-associated synthesis), and that ovococci are ellipsoidal because they retain a peripheral synthesis mode in addition to septal synthesis (pinho2013howtoget pages 2-3, zapun2008thedifferentshapes pages 1-2). This framing supports curating “ellipsoidal” primarily as a PG-morphogenesis trait rather than as a surface-layer (capsule) trait.

## 8. Visual evidence (figures)
Super-resolution images and summary schematics demonstrating (i) the **concentric rings** (“Saturn-like” pattern) and (ii) **nodal organization** of PG synthesis at midcell in ovococci were retrieved from Perez et al. 2021 (perez2021organizationofpeptidoglycan media 5cd05702, perez2021organizationofpeptidoglycan media a0892114, perez2021organizationofpeptidoglycan media c19ed114). These visuals are useful to justify mechanistic nodes/edges such as “inner septal ring vs outer peripheral ring” and “nodal PG insertion geometry.”

## 9. Warnings / claims not yet ready for TraitMech curation
1. **Do not conflate capsule distribution with ellipsoidal morphology.** Capsule synthesis can be re-routed without affecting FDAA PG-labeling patterns or “overall cell shape,” and elongasome deletions may not alter capsule organizer localization (nakamoto2023thedivisomebut pages 6-7, nakamoto2023thedivisomebut pages 3-4). If curating capsule-related nodes, treat them as separate from the ellipsoidal shape module.
2. **Taxon specificity:** DivIVA phosphorylation control via MltG is directly shown in *S. suis*; curating it as a universal ovococcus mechanism should be marked **uncertain** until replicated in additional taxa (jiang2023divivainteractswith pages 1-2).
3. **Complex identifiers:** several complexes (e.g., “elongasome”, “divisome”, “CpsCD system”) lack a single stable ontology identifier in this extraction; curate as label-level nodes unless a controlled vocabulary mapping is added.
4. **Accessory gene Spr0777:** functionally linked to pneumococcal elongasome but poorly grounded; keep as label-level until a stable identifier/annotation is obtained (straume2017identificationofpneumococcal pages 47-54).

---

# DOI-first bibliography (publication date; URL)
* Jiang Q, et al. **DivIVA Interacts with the Cell Wall Hydrolase MltG To Regulate Peptidoglycan Synthesis in Streptococcus suis.** *Microbiology Spectrum* (Jun 2023). https://doi.org/10.1128/spectrum.04750-22 (jiang2023divivainteractswith pages 2-4, jiang2023divivainteractswith pages 4-6)
* Nakamoto R, et al. **The divisome but not the elongasome organizes capsule synthesis in Streptococcus pneumoniae.** *Nature Communications* (Jun 2023). https://doi.org/10.1038/s41467-023-38904-9 (nakamoto2023thedivisomebut pages 2-3, nakamoto2023thedivisomebut pages 6-7)
* Dewachter L, et al. **Amoxicillin-resistant Streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by sCRilecs-seq.** *eLife* (Jun 2022). https://doi.org/10.7554/eLife.75607 (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2, dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12)
* Perez AJ, et al. **Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of Streptococcus pneumoniae.** *Molecular Microbiology* (Dec 2021). https://doi.org/10.1111/mmi.14659 (perez2021organizationofpeptidoglycan pages 16-18, perez2021organizationofpeptidoglycan pages 1-5)
* Trouve J, et al. **Nanoscale dynamics of peptidoglycan assembly during the cell cycle of Streptococcus pneumoniae.** *Current Biology* (Jul 2021). https://doi.org/10.1016/j.cub.2021.04.041 (trouve2021nanoscaledynamicsof pages 10-11, trouve2021nanoscaledynamicsof pages 20-20)
* Straume D, et al. **Identification of pneumococcal proteins that are functionally linked to penicillin-binding protein 2b (PBP2b).** *Molecular Microbiology* (Jan 2017). https://doi.org/10.1111/mmi.13543 (straume2017identificationofpneumococcal pages 1-5, straume2017identificationofpneumococcal pages 12-16)
* Fenton AK, et al. **CozE is a member of the MreCD complex that directs cell elongation in Streptococcus pneumoniae.** *Nature Microbiology* (Dec 2016). https://doi.org/10.1038/nmicrobiol.2016.237 (fenton2016cozeisa pages 2-4)
* Zapun A, et al. **The different shapes of cocci.** *FEMS Microbiology Reviews* (Mar 2008). https://doi.org/10.1111/j.1574-6976.2007.00098.x (zapun2008thedifferentshapes pages 1-2)
* Pinho MG, et al. **How to get (a)round: mechanisms controlling growth and division of coccoid bacteria.** *Nature Reviews Microbiology* (Aug 2013). https://doi.org/10.1038/nrmicro3088 (pinho2013howtoget pages 2-3, pinho2013howtoget pages 1-2)

(Additional contextual/secondary sources used in evidence extraction include Fleurie et al. 2014 PLoS Genetics https://doi.org/10.1371/journal.pgen.1004275 and Xiang et al. 2019 https://doi.org/10.21775/cimb.032.259.) (fleurie2014interplayofthe pages 7-10, xiang2019regulationofcell pages 24-30)

References

1. (zapun2008thedifferentshapes pages 1-2): André Zapun, Thierry Vernet, and Mariana G. Pinho. The different shapes of cocci. FEMS microbiology reviews, 32 2:345-60, Mar 2008. URL: https://doi.org/10.1111/j.1574-6976.2007.00098.x, doi:10.1111/j.1574-6976.2007.00098.x. This article has 273 citations and is from a domain leading peer-reviewed journal.

2. (pinho2013howtoget pages 2-3): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.

3. (perez2021organizationofpeptidoglycan pages 1-5): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

4. (perez2021organizationofpeptidoglycan pages 43-53): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

5. (tavares2019determinationofcell pages 46-50): AFC Tavares. Determination of cell shape in staphylococcus aureus. Unknown journal, 2019.

6. (tavares2019determinationofcella pages 46-50): AFC Tavares. Determination of cell shape in staphylococcus aureus. Unknown journal, 2019.

7. (nakamoto2023thedivisomebut pages 6-7): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 13 citations and is from a highest quality peer-reviewed journal.

8. (nakamoto2023thedivisomebut pages 2-3): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 13 citations and is from a highest quality peer-reviewed journal.

9. (straume2017identificationofpneumococcal pages 1-5): Daniel Straume, Gro Anita Stamsås, Kari Helene Berg, Zhian Salehian, and Leiv Sigve Håvarstein. Identification of pneumococcal proteins that are functionally linked to penicillin‐binding protein 2b (pbp2b). Molecular Microbiology, 103:99-116, Jan 2017. URL: https://doi.org/10.1111/mmi.13543, doi:10.1111/mmi.13543. This article has 45 citations and is from a domain leading peer-reviewed journal.

10. (tsui2016suppressionofa pages 1-3): Ho‐Ching Tiffany Tsui, Jiaqi J. Zheng, Ariel N. Magallon, John D. Ryan, Rachel Yunck, Britta E. Rued, Thomas G. Bernhardt, and Malcolm E. Winkler. Suppression of a deletion mutation in the gene encoding essential pbp2b reveals a new lytic transglycosylase involved in peripheral peptidoglycan synthesis in streptococcus pneumoniae d39. Molecular Microbiology, 100:1039-1065, Jun 2016. URL: https://doi.org/10.1111/mmi.13366, doi:10.1111/mmi.13366. This article has 109 citations and is from a domain leading peer-reviewed journal.

11. (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 1-2): Liselot Dewachter, Julien Dénéréaz, Xue Liu, Vincent de Bakker, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, and Jan-Willem Veening. Amoxicillin-resistant streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by scrilecs-seq. eLife, Jun 2022. URL: https://doi.org/10.7554/elife.75607, doi:10.7554/elife.75607. This article has 30 citations and is from a domain leading peer-reviewed journal.

12. (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 10-12): Liselot Dewachter, Julien Dénéréaz, Xue Liu, Vincent de Bakker, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, and Jan-Willem Veening. Amoxicillin-resistant streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by scrilecs-seq. eLife, Jun 2022. URL: https://doi.org/10.7554/elife.75607, doi:10.7554/elife.75607. This article has 30 citations and is from a domain leading peer-reviewed journal.

13. (jiang2023divivainteractswith pages 2-4): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

14. (straume2017identificationofpneumococcal pages 47-54): Daniel Straume, Gro Anita Stamsås, Kari Helene Berg, Zhian Salehian, and Leiv Sigve Håvarstein. Identification of pneumococcal proteins that are functionally linked to penicillin‐binding protein 2b (pbp2b). Molecular Microbiology, 103:99-116, Jan 2017. URL: https://doi.org/10.1111/mmi.13543, doi:10.1111/mmi.13543. This article has 45 citations and is from a domain leading peer-reviewed journal.

15. (nakamoto2023thedivisomebut pages 1-2): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 13 citations and is from a highest quality peer-reviewed journal.

16. (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 20-21): Liselot Dewachter, Julien Dénéréaz, Xue Liu, Vincent de Bakker, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, and Jan-Willem Veening. Amoxicillin-resistant streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by scrilecs-seq. eLife, Jun 2022. URL: https://doi.org/10.7554/elife.75607, doi:10.7554/elife.75607. This article has 30 citations and is from a domain leading peer-reviewed journal.

17. (xiang2019regulationofcell pages 24-30): Zhenting Xiang, Zongbo Li, Jumei Zeng, Yuqing Li, and Jiyao Li. Regulation of cell division in streptococci: comparing with the model rods. Current issues in molecular biology, 32:259-326, Jun 2019. URL: https://doi.org/10.21775/cimb.032.259, doi:10.21775/cimb.032.259. This article has 3 citations.

18. (perez2021organizationofpeptidoglycan pages 7-10): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

19. (nakamoto2023thedivisomebut pages 3-4): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 13 citations and is from a highest quality peer-reviewed journal.

20. (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 15-16): Liselot Dewachter, Julien Dénéréaz, Xue Liu, Vincent de Bakker, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, and Jan-Willem Veening. Amoxicillin-resistant streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by scrilecs-seq. eLife, Jun 2022. URL: https://doi.org/10.7554/elife.75607, doi:10.7554/elife.75607. This article has 30 citations and is from a domain leading peer-reviewed journal.

21. (straume2017identificationofpneumococcal pages 12-16): Daniel Straume, Gro Anita Stamsås, Kari Helene Berg, Zhian Salehian, and Leiv Sigve Håvarstein. Identification of pneumococcal proteins that are functionally linked to penicillin‐binding protein 2b (pbp2b). Molecular Microbiology, 103:99-116, Jan 2017. URL: https://doi.org/10.1111/mmi.13543, doi:10.1111/mmi.13543. This article has 45 citations and is from a domain leading peer-reviewed journal.

22. (straume2017identificationofpneumococcal pages 5-9): Daniel Straume, Gro Anita Stamsås, Kari Helene Berg, Zhian Salehian, and Leiv Sigve Håvarstein. Identification of pneumococcal proteins that are functionally linked to penicillin‐binding protein 2b (pbp2b). Molecular Microbiology, 103:99-116, Jan 2017. URL: https://doi.org/10.1111/mmi.13543, doi:10.1111/mmi.13543. This article has 45 citations and is from a domain leading peer-reviewed journal.

23. (perez2021organizationofpeptidoglycan pages 13-16): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

24. (perez2021organizationofpeptidoglycan pages 5-7): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

25. (fenton2016cozeisa pages 2-4): Andrew K. Fenton, Lamya El Mortaji, Derek T. C. Lau, David Z. Rudner, and Thomas G. Bernhardt. Coze is a member of the mrecd complex that directs cell elongation in streptococcus pneumoniae. Nature Microbiology, Dec 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.237, doi:10.1038/nmicrobiol.2016.237. This article has 84 citations and is from a highest quality peer-reviewed journal.

26. (land2011therequirementfor pages 1-2): Adrian D. Land and Malcolm E. Winkler. The requirement for pneumococcal mrec and mred is relieved by inactivation of the gene encoding pbp1a. Aug 2011. URL: https://doi.org/10.1128/jb.05245-11, doi:10.1128/jb.05245-11. This article has 126 citations and is from a peer-reviewed journal.

27. (fleurie2014interplayofthe pages 7-10): Aurore Fleurie, Sylvie Manuse, Chao Zhao, Nathalie Campo, Caroline Cluzel, Jean-Pierre Lavergne, Céline Freton, Christophe Combet, Sébastien Guiral, Boumediene Soufi, Boris Macek, Erkin Kuru, Michael S. VanNieuwenhze, Yves V. Brun, Anne-Marie Di Guilmi, Jean-Pierre Claverys, Anne Galinier, and Christophe Grangeasse. Interplay of the serine/threonine-kinase stkp and the paralogs diviva and gpsb in pneumococcal cell elongation and division. PLoS Genetics, 10:e1004275, Apr 2014. URL: https://doi.org/10.1371/journal.pgen.1004275, doi:10.1371/journal.pgen.1004275. This article has 204 citations and is from a domain leading peer-reviewed journal.

28. (straume2017identificationofpneumococcal pages 16-19): Daniel Straume, Gro Anita Stamsås, Kari Helene Berg, Zhian Salehian, and Leiv Sigve Håvarstein. Identification of pneumococcal proteins that are functionally linked to penicillin‐binding protein 2b (pbp2b). Molecular Microbiology, 103:99-116, Jan 2017. URL: https://doi.org/10.1111/mmi.13543, doi:10.1111/mmi.13543. This article has 45 citations and is from a domain leading peer-reviewed journal.

29. (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 19-20): Liselot Dewachter, Julien Dénéréaz, Xue Liu, Vincent de Bakker, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, and Jan-Willem Veening. Amoxicillin-resistant streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by scrilecs-seq. eLife, Jun 2022. URL: https://doi.org/10.7554/elife.75607, doi:10.7554/elife.75607. This article has 30 citations and is from a domain leading peer-reviewed journal.

30. (jiang2023divivainteractswith pages 9-11): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

31. (jiang2023divivainteractswith pages 7-9): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

32. (jiang2023divivainteractswith pages 1-2): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

33. (nakamoto2023thedivisomebut pages 4-6): Rei Nakamoto, Sarp Bamyaci, Karin Blomqvist, Staffan Normark, Birgitta Henriques-Normark, and Lok-To Sham. The divisome but not the elongasome organizes capsule synthesis in streptococcus pneumoniae. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-38904-9, doi:10.1038/s41467-023-38904-9. This article has 13 citations and is from a highest quality peer-reviewed journal.

34. (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 2-3): Liselot Dewachter, Julien Dénéréaz, Xue Liu, Vincent de Bakker, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, and Jan-Willem Veening. Amoxicillin-resistant streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by scrilecs-seq. eLife, Jun 2022. URL: https://doi.org/10.7554/elife.75607, doi:10.7554/elife.75607. This article has 30 citations and is from a domain leading peer-reviewed journal.

35. (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 7-9): Liselot Dewachter, Julien Dénéréaz, Xue Liu, Vincent de Bakker, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, and Jan-Willem Veening. Amoxicillin-resistant streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by scrilecs-seq. eLife, Jun 2022. URL: https://doi.org/10.7554/elife.75607, doi:10.7554/elife.75607. This article has 30 citations and is from a domain leading peer-reviewed journal.

36. (dewachter2022amoxicillinresistantstreptococcuspneumoniae pages 18-19): Liselot Dewachter, Julien Dénéréaz, Xue Liu, Vincent de Bakker, Charlotte Costa, Mara Baldry, Jean-Claude Sirard, and Jan-Willem Veening. Amoxicillin-resistant streptococcus pneumoniae can be resensitized by targeting the mevalonate pathway as indicated by scrilecs-seq. eLife, Jun 2022. URL: https://doi.org/10.7554/elife.75607, doi:10.7554/elife.75607. This article has 30 citations and is from a domain leading peer-reviewed journal.

37. (jiang2023divivainteractswith pages 4-6): Qinggen Jiang, Boxi Li, Liangsheng Zhang, Tingting Li, Qiao Hu, Haotian Li, Wen-Qian Zou, Zhe Hu, Qi Huang, and Rui Zhou. Diviva interacts with the cell wall hydrolase mltg to regulate peptidoglycan synthesis in streptococcus suis. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.04750-22, doi:10.1128/spectrum.04750-22. This article has 12 citations and is from a domain leading peer-reviewed journal.

38. (trouve2021nanoscaledynamicsof pages 10-11): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

39. (trouve2021nanoscaledynamicsof pages 20-20): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

40. (perez2021organizationofpeptidoglycan pages 16-18): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

41. (perez2021organizationofpeptidoglycan media 5cd05702): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

42. (perez2021organizationofpeptidoglycan media a0892114): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

43. (perez2021organizationofpeptidoglycan media c19ed114): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

44. (pinho2013howtoget pages 1-2): Mariana G. Pinho, Morten Kjos, and Jan-Willem Veening. How to get (a)round: mechanisms controlling growth and division of coccoid bacteria. Nature Reviews Microbiology, 11:601-614, Aug 2013. URL: https://doi.org/10.1038/nrmicro3088, doi:10.1038/nrmicro3088. This article has 380 citations and is from a highest quality peer-reviewed journal.