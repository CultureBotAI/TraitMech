---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T08:15:32.825884'
end_time: '2026-08-04T08:25:29.033873'
duration_seconds: 596.21
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
  causal_graph_summary: 'ellipsoidal_ovococcal_elongation: 13 nodes, 11 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ellipsoidal
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000673
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an oval or ellipse morphology, elongated along one axis with rounded ends, intermediate between spherical and rod-shaped.
- **Parent traits:** METPO:1000666
- **Synonyms:** 
- **Existing evidence:** DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports ellipsoidal bacterial morphology as a named ovococcal shape class.)
- **Existing causal graph summary:** ellipsoidal_ovococcal_elongation: 13 nodes, 11 edges

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
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000673
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has an oval or ellipse morphology, elongated along one axis with rounded ends, intermediate between spherical and rod-shaped.
- **Parent traits:** METPO:1000666
- **Synonyms:** 
- **Existing evidence:** DOI:10.1089/mdr.2014.0032: ovococci that are ellipsoid (Supports ellipsoidal bacterial morphology as a named ovococcal shape class.)
- **Existing causal graph summary:** ellipsoidal_ovococcal_elongation: 13 nodes, 11 edges

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


# Curation-focused research report: ellipsoidal microbial morphology

## Executive assessment

**Target:** `METPO:1000673` (“ellipsoidal”); morphology class; reviewed mapping; parent `METPO:1000666`.

The strongest curatable mechanism is an **ovococcal elongation module**, best demonstrated in *Streptococcus pneumoniae*: FtsZ organizes peptidoglycan (PG) synthesis at midcell; a PBP2x–FtsW septal machine builds the cross-wall, while a PBP2b–RodA-centered peripheral machine adds the longitudinal component. Their coordinated activities generate a prolate ellipsoid. MreC/MreD, CozE, DivIVA, Spr0777, PBP1a, and MltG regulate or support the peripheral pathway. Loss or inhibition of peripheral synthesis produces compressed or nearly spherical cells, whereas impaired septation can permit excessive longitudinal growth. This is a mechanistic graph for **ovococcal ellipsoids**, not necessarily every microbial cell described microscopically as ellipsoidal. (zapun2008thedifferentshapes pages 3-5, tsui2016suppressionofa pages 1-3, straume2017identificationofpneumococcal pages 1-5, perez2021organizationofpeptidoglycan pages 1-5)

## 1. Trait scope and boundaries

### Definition

The supplied definition is consistent with the literature: an ellipsoidal cell is oval or prolate-ellipsoid, elongated along one axis with rounded ends, and intermediate between a sphere and a rod. Ovococci—including streptococci, lactococci, and enterococci—are described as “elongated ellipsoids” that divide in successive parallel planes perpendicular to their long axis. They may occur singly, as diplococci, or in chains depending on daughter-cell separation. (tan2021streptococcussuismsmk pages 1-2, zapun2008thedifferentshapes pages 1-2, tsui2016suppressionofa pages 1-3)

The phenotype should be represented as **cell geometry**, ideally measured by long-axis length, width, and length:width ratio, rather than inferred merely from a taxonomic name such as “coccus.” *S. pneumoniae* is explicitly described as neither a rod nor a true coccus, but as having an intermediate ovoid morphology. (straume2017identificationofpneumococcal pages 1-5)

### Boundary cases

1. **True spherical cocci:** staphylococci, many *Neisseria*, pediococci, micrococci, and deinococci are genuinely round and commonly use alternating division planes. Classical models assign them septal synthesis without the ovococcal longitudinal/peripheral component. They should not be annotated as ellipsoidal solely because they are cocci. (zapun2008thedifferentshapes pages 1-2, zapun2008thedifferentshapes pages 3-5)
2. **Rod-shaped cells:** rods possess an extended cylindrical sidewall and typically use an MreB-organized elongation system over the cell body. Ovococci lack MreB and confine peripheral growth near midcell. Rod-like mutants or antibiotic-induced filaments are state transitions, not evidence that the baseline trait is rod-shaped. (straume2017identificationofpneumococcal pages 12-16, perez2021organizationofpeptidoglycan pages 1-5, trouve2021nanoscaledynamicsof pages 1-3)
3. **Ovoid versus ellipsoid:** in the cited bacterial literature these terms are often operationally interchangeable. “Prolate ellipsoid” is the more precise geometry; “ovoid” may be less symmetric and should be accepted only when images or measurements support the intended class.
4. **Chains versus shape:** chaining is an arrangement/separation phenotype, not cell shape. Individual cells in a chain may be ellipsoidal, compressed, lentil-shaped, or nearly spherical.
5. **Condition-dependent morphology:** medium composition, ionic ratios, growth phase, PG inhibitors, and mutations can move cells along a sphere–ellipsoid–rod/filament continuum. For example, historical *Streptococcus mutans* observations reported length:width ratios from 1 to 5 depending on potassium/bicarbonate conditions. Such claims should be represented with environmental qualifiers. (zapun2008thedifferentshapes pages 3-5)
6. **Taxonomic reach:** the present evidence base is overwhelmingly bacterial and Gram-positive. It does not establish that archaeal, fungal, or other microbial ellipsoids use the same mechanism.

## 2. Current mechanistic understanding

The PG sacculus is the proximate structural determinant of ovococcal shape. In *S. pneumoniae*, septal and peripheral synthesis begin at the same midcell region. Septal synthesis produces the daughter-separating cross-wall; concurrent peripheral synthesis elongates the daughters from midcell and creates the ovoid contour. Peripheral growth is therefore not equivalent to the distributed MreB-dependent sidewall elongation of rods. (tsui2016suppressionofa pages 1-3, perez2021organizationofpeptidoglycan pages 1-5)

High-resolution work refined the older “two successive phases” model. Single-molecule localization showed that septal and peripheral synthesis initially share one annular region, later separate into concentric zones, and that peripheral synthesis can persist after septation is complete. The authors consequently argued that shape emerges from relative rates of PG synthesis and cleavage/remodeling, not simply from two temporally discrete programs. (trouve2021nanoscaledynamicsof pages 1-3)

Three-dimensional structured-illumination microscopy independently resolved an inner ring enriched for PBP2x and FtsZ and an outer ring containing PBP2b and FtsX. Fluorescent D-amino-acid incorporation further revealed regularly spaced nodes of transpeptidase activity. This supports spatially distinct but coordinated septal and peripheral machines. (perez2021organizationofpeptidoglycan pages 1-5)

## 3. Candidate nodes

The following matrix gives conservative grounding. Protein accessions are intentionally left label-only where strain-specific UniProt identifiers were not verified.

| candidate node or module | type | taxon | proposed grounding | mechanistic role | evidence strength/caveat |
|---|---|---|---|---|---|
| ellipsoidal morphology | trait/phenotype | ovococci incl. *Streptococcus pneumoniae*, *Lactococcus lactis*, *Streptococcus suis* | METPO:1000673 | Oval/prolate-ellipsoid cell shape, elongated along one axis; intermediate between spherical cocci and rods; typically divides in parallel planes perpendicular to long axis | Strong trait definition and boundary support from reviews and primary papers; broad across ovococci, not universal to all cocci (tan2021streptococcussuismsmk pages 1-2, zapun2008thedifferentshapes pages 1-2, tsui2016suppressionofa pages 1-3) |
| FtsZ | protein / cytoskeletal organizer | ovococci | label-only | Midcell Z-ring scaffold that organizes division proteins; in ovococci also linked to elongation/peripheral growth dynamics | Strong for localization and organizer role; exact causal direction to ellipsoidal shape is indirect and taxon-specific (tan2021streptococcussuismsmk pages 1-2, david2018pbp2bplaysa pages 16-18, perez2021organizationofpeptidoglycan pages 1-5) |
| septal PG synthesis | biological process | ovococci, especially *S. pneumoniae* | GO:0009252 | Produces septal cross-wall separating daughter cells | Strong process-level support; shape contribution inferred from balance with peripheral synthesis rather than single direct edge to trait (perez2021organizationofpeptidoglycan pages 1-5, trouve2021nanoscaledynamicsof pages 1-3) |
| peripheral PG synthesis | biological process | ovococci, especially *S. pneumoniae*, *L. lactis*, *S. suis* | label-only | Midcell-confined elongation/peripheral wall insertion that lengthens daughters and supports ovoid/ellipsoid shape | Strong central mechanism for ovococci; GO grounding not safely established from conversation, so left label-only (tan2021streptococcussuismsmk pages 1-2, tsui2016suppressionofa pages 1-3, perez2021organizationofpeptidoglycan pages 1-5) |
| PBP2x:FtsW | protein complex/module | *S. pneumoniae* | label-only | Septal PG synthesis machine; PBP2x localizes primarily to inner septal ring and interacts with FtsW for sPG synthesis | Strong in *S. pneumoniae*; taxon-specific and complex grounding unresolved here (perez2021organizationofpeptidoglycan pages 1-5) |
| PBP2b:RodA | protein complex/module | *S. pneumoniae* | label-only | Core peripheral/elongasome transpeptidase-glycosyltransferase pair supporting elongation and maintenance of ellipsoid shape | Strong in *S. pneumoniae*; depletion/defect causes rounding/compressed-chain phenotypes; direct complex support includes strong interaction evidence for PBP2b-RodA (straume2017identificationofpneumococcal pages 16-19, tsui2016suppressionofa pages 1-3, straume2017identificationofpneumococcal pages 12-16, straume2017identificationofpneumococcal pages 1-5) |
| MreC/MreD | protein pair/module | *S. pneumoniae* | label-only | Elongasome-associated factors required for zonal/peripheral elongation and normal morphology | Strong for MreD and broader MreCD function; exact stoichiometry and graph direction should be curated cautiously (tsui2016suppressionofa pages 1-3, straume2017identificationofpneumococcal pages 1-5, fenton2016cozeisa pages 1-2) |
| CozE | protein | *S. pneumoniae* | label-only | Member of MreCD complex; directs cell elongation and activity of PBP1a at midcell plane | Strong primary evidence in pneumococcus; safest as taxon-specific elongation regulator node (fenton2016cozeisa pages 1-2) |
| DivIVA | protein | *S. pneumoniae* | label-only | Accessory factor linked to PBP2b elongasome; proposed to localize elongasome to negatively curved membrane region between septal and lateral wall | Moderate-to-strong; functional/genetic evidence strong, localization role somewhat interpretive/model-based (straume2017identificationofpneumococcal pages 16-19, straume2017identificationofpneumococcal pages 12-16, straume2017identificationofpneumococcal pages 1-5) |
| Spr0777 | protein | *S. pneumoniae* | label-only | Accessory elongasome factor functionally linked to PBP2b, RodA, MreD, DivIVA | Moderate; clear phenotypic linkage and some interaction support, but molecular function unresolved (straume2017identificationofpneumococcal pages 12-16, straume2017identificationofpneumococcal pages 1-5) |
| PBP1a | protein/enzyme | *S. pneumoniae* | label-only | Class A PBP supplying glycan-strand synthesis coordinated with elongation machinery; implicated in peripheral PG biogenesis and CozE-dependent zonal growth | Moderate-to-strong in pneumococcus; role is mechanistically important but often embedded in genetic/model interpretations (tsui2016suppressionofa pages 1-3, fenton2016cozeisa pages 1-2) |
| MltG | protein/enzyme | *S. pneumoniae* | label-only | Lytic transglycosylase involved in peripheral PG synthesis; depletion or mutant increases sphericity and genetically bypasses PBP2b requirement | Strong for peripheral-PG involvement and shape effect in *S. pneumoniae*; mechanism modeled as strand release for crosslinking (tsui2016suppressionofa pages 1-3) |
| MsmK | protein | *S. suis* | label-only | FtsZ-interacting ATPase/GTPase that promotes FtsZ bundling and supports peripheral PG synthesis and maintenance of elongated ellipsoid shape | Strong but taxon-specific to *S. suis*; promising node, not yet generalized across ovococci (tan2021streptococcussuismsmk pages 8-11, tan2021streptococcussuismsmk pages 1-2) |
| amoxicillin | chemical / beta-lactam antibiotic | *L. lactis* assay context | CHEBI:28971 | Experimental inhibitor that selectively inhibits peripheral growth under tested conditions, causing significantly rounder cells without obvious septation misplacement | Strong assay-specific perturbation in *L. lactis*; not a natural causal determinant of trait, best as experimental factor node (david2018pbp2bplaysa pages 16-18) |
| methicillin | chemical / beta-lactam antibiotic | *L. lactis* assay context | CHEBI:6827 | Experimental perturbation used to uncouple elongation from division and induce filamentation while tracking PBP2b/FtsZ dynamics | Strong as assay factor; mechanism and targets complex, so avoid over-curating as direct trait cause (david2018pbp2bplaysa pages 1-2, david2018pbp2bplaysa pages 11-13) |


*Table: This table summarizes candidate nodes and modules for curating METPO:1000673, emphasizing safe grounding, mechanistic role, and evidence caveats. It is useful for deciding which entities are ready for TraitMech inclusion versus those that remain taxon-specific or assay-specific.*

Additional useful node classes are:

- **Structural chemicals:** peptidoglycan; lipid II; N-acetylglucosamine; N-acetylmuramic acid; peptide stems and cross-links.
- **Processes:** glycan polymerization/transglycosylation; transpeptidation; PG cleavage/remodeling; septation; peripheral cell-wall growth; daughter-cell separation; Z-ring assembly.
- **Locations:** cytoplasmic membrane; midcell/equator; septal leading edge/inner ring; peripheral outer ring; negatively curved septal–lateral junction.
- **Assays:** fluorescent D-amino-acid incorporation, click-chemistry metabolic labeling, dSTORM, 3D-SIM, TEM/SEM, time-lapse fluorescence microscopy, bacterial two-hybrid, co-immunoprecipitation, and PG muropeptide analysis. (tan2021streptococcussuismsmk pages 8-11, david2018pbp2bplaysa pages 11-13, straume2017identificationofpneumococcal pages 12-16, perez2021organizationofpeptidoglycan pages 1-5, fenton2016cozeisa pages 6-7, trouve2021nanoscaledynamicsof pages 1-3)

## 4. Candidate causal edges

Predicates below are curation-oriented rather than assertions that a particular relation ontology already contains the exact predicate.

| Subject–predicate–object | Taxon/status | Reference | Supporting snippet | Curation note |
|---|---|---|---|---|
| Peripheral PG synthesis — **promotes** → longitudinal elongation | Ovococci; strong | 10.1128/mSphere.00119-21 | “Peripheral cell wall synthesis leads to the slight longitudinal elongation of ovococci.” | Core process edge. (tan2021streptococcussuismsmk pages 1-2) |
| Coordinated peripheral + septal PG synthesis — **produces** → ellipsoidal/ovoid morphology | *S. pneumoniae*; strong | 10.1111/mmi.13543 | “The oval shape of pneumococci results from a combination of septal and lateral peptidoglycan synthesis.” | Best high-level edge into `METPO:1000673`; qualify by taxon. (straume2017identificationofpneumococcal pages 1-5) |
| Septal PG synthesis — **produces** → daughter-separating cross-wall | *S. pneumoniae*; strong | 10.1111/mmi.14659 | “sPG synthesis produces the cross wall that separates daughter cells.” | Process edge, not sufficient alone for ellipsoidal shape. (perez2021organizationofpeptidoglycan pages 1-5) |
| Peripheral PG synthesis — **forms** → ovoid daughter cells | *S. pneumoniae*; strong | 10.1111/mmi.14659 | “Concurrent pPG synthesis elongates daughter cells from midcell to form ovoid-shaped cells.” | Direct shape-generating edge. (perez2021organizationofpeptidoglycan pages 1-5) |
| FtsZ ring — **organizes/localizes** → midcell PG machinery | Ovococci; strong | 10.1128/mSphere.00119-21 | “The ring composed of FtsZ protofilaments provides a scaffold for the binding of dozens of cell division proteins.” | FtsZ’s direct edge to shape is mediated through machinery organization. (tan2021streptococcussuismsmk pages 1-2) |
| PBP2x:FtsW — **catalyzes** → septal PG synthesis | *S. pneumoniae*; strong | 10.1111/mmi.14659 | PBP2x “interacts with the FtsW SEDS glycosyltransferase … to carry out sPG synthesis.” | Curate as a taxon-qualified functional complex/module. (perez2021organizationofpeptidoglycan pages 1-5) |
| PBP2b — **catalyzes/supports** → peripheral PG synthesis | *S. pneumoniae* and *L. lactis*; strong | 10.1111/mmi.13366; 10.1371/journal.pone.0198014 | Peripheral PG synthesis “is catalyzed by the essential class B … PBP2b”; in *L. lactis*, PBP2b is “dedicated to cell elongation.” | Essentiality differs by species: essential in pneumococcus, dispensable but important in *L. lactis*. (david2018pbp2bplaysa pages 1-2, tsui2016suppressionofa pages 1-3) |
| PBP2b loss/depletion — **decreases** → ellipsoidal elongation | *S. pneumoniae*, *L. lactis*; strong | 10.1111/mmi.13543; 10.1371/journal.pone.0198014 | Depleted pneumococci form “long chains of cells that are compressed in the direction of their long axes”; *L. lactis* mutant cells are “rounder than WT.” | Encode perturbation-to-phenotype, not a universal null phenotype. (david2018pbp2bplaysa pages 11-13, straume2017identificationofpneumococcal pages 1-5) |
| PBP2b — **interacts with** → RodA | *S. pneumoniae*; strong interaction assay | 10.1111/mmi.13543 | “PBP2b interacts strongly with RodA.” | Bacterial two-hybrid evidence; interaction does not by itself establish direct biochemical activation. (straume2017identificationofpneumococcal pages 12-16) |
| RodA/MreD/DivIVA/Spr0777 — **supports** → functional elongasome | *S. pneumoniae*; strong functional, mixed mechanistic certainty | 10.1111/mmi.13543 | Shared depletion traits “provide strong evidence that these five proteins cooperate to build a functional elongasome.” | A module edge is safer than separate direct edges to shape for every component. (straume2017identificationofpneumococcal pages 12-16) |
| DivIVA — **localizes** → elongasome at negatively curved septal–lateral junction | *S. pneumoniae*; moderate/model-supported | 10.1111/mmi.13543 | DivIVA is “required to correctly localize the elongasome at the negatively curved membrane region.” | Mark **uncertain/model-based** until direct localization causality is independently replicated. (straume2017identificationofpneumococcal pages 1-5) |
| CozE/MreCD — **directs** → PBP1a activity at midcell | *S. pneumoniae*; strong, taxon-specific | 10.1038/nmicrobiol.2016.237 | CozE is a member of the MreCD complex that “directs the activity of PBP1a to the midcell plane.” | Suitable regulatory edge; do not generalize to all ellipsoidal microbes. (fenton2016cozeisa pages 1-2) |
| CozE–MreCD–PBP1a module — **promotes** → zonal elongation and normal morphology | *S. pneumoniae*; strong | 10.1038/nmicrobiol.2016.237 | PBP1a at midcell “promotes zonal cell elongation and normal morphology.” | Curate taxon-qualified. (fenton2016cozeisa pages 1-2) |
| MltG — **participates in** → peripheral PG synthesis | *S. pneumoniae*; strong | 10.1111/mmi.13366 | MltG is identified as an “endo-lytic transglycosylase”; its depletion “increases sphericity,” and it localizes with peripheral synthesis proteins. | Strong node; exact substrate handoff remains a model. (tsui2016suppressionofa pages 1-3) |
| MltG — **releases** → PBP1a-synthesized glycan strands for PBP2b:RodA cross-linking | *S. pneumoniae*; uncertain/model | 10.1111/mmi.13366 | “These results fit a model in which MltG releases anchored PG glycan strands … for crosslinking by a PBP2b:RodA complex.” | Preserve as explicitly **inferred**, not established catalytic sequence. (tsui2016suppressionofa pages 1-3) |
| MsmK — **interacts with** → FtsZ | *S. suis*; strong, taxon-specific | 10.1128/mSphere.00119-21 | MsmK “interact[s] with FtsZ via the N terminus” and forms a complex in vivo. | Supported by in-vitro assays, co-IP, and colocalization. (tan2021streptococcussuismsmk pages 8-11, tan2021streptococcussuismsmk pages 1-2) |
| MsmK — **promotes** → GTP-dependent FtsZ protofilament bundling | *S. suis*; strong in vitro | 10.1128/mSphere.00119-21 | MsmK can “promote the bundling of FtsZ protofilaments in a GTP-dependent manner in vitro.” | Mark assay-specific; in-vivo bundling causality is less direct. (tan2021streptococcussuismsmk pages 1-2) |
| MsmK — **supports** → peripheral PG synthesis and ellipsoidal shape | *S. suis*; strong, taxon-specific | 10.1128/mSphere.00119-21 | MsmK absence caused disturbed “cell elongation and peripheral peptidoglycan synthesis” and nearly spherical cells. | Good species-specific branch, not yet a pan-ovococcal mechanism. (tan2021streptococcussuismsmk pages 8-11, tan2021streptococcussuismsmk pages 1-2) |
| Amoxicillin exposure — **inhibits** → peripheral growth | *L. lactis* assay; strong | 10.1371/journal.pone.0198014 | “Amoxicillin treatment selectively inhibits peripheral growth.” | Experimental-factor edge; targets were multiple and mechanism complex. (david2018pbp2bplaysa pages 16-18) |
| Amoxicillin exposure — **decreases** → length:width ratio/ellipsoidality | *L. lactis* assay; strong | 10.1371/journal.pone.0198014 | Treated cells were “significantly rounder,” ratio 1.21±0.19 versus 1.37±0.17. | Concentration-specific: 0.1 μg mL⁻¹; reversible after drug removal. (david2018pbp2bplaysa pages 16-18) |
| Methicillin inhibition of septation — **permits** → elongation/filamentation | *L. lactis* assay; strong | 10.1371/journal.pone.0198014 | Methicillin-generated filaments underwent growth and later successive divisions after drug removal. | Use as an assay perturbation, not part of the native causal path. (david2018pbp2bplaysa pages 11-13) |

## 5. Quantitative evidence

The strongest quantitative genetic evidence is from *S. suis*. Wild-type cells were concentrated at 0.8–1.4 μm long, whereas Δ*msmK* cells ranged from 0.4–1.3 μm. Mean cell length fell from approximately 1.05±0.14 μm to 0.89±0.20 μm, and length:width ratio from 1.58±0.21 to 1.35±0.28, while width did not significantly change. Cells shorter than 0.8 μm rose from 0/370 wild-type cells to 95/352 mutant cells (26.99%). Chains of at least three cells increased from 14/290 (4.8%) to 108/374 (28.9%). Complementation restored morphology, supporting causality. The source text reports an apparent inconsistency between stated mean wall thicknesses and the phrase “significantly thinner”; that particular wall-thickness interpretation should therefore not be curated without checking the typeset article. (tan2021streptococcussuismsmk pages 8-11)

In *L. lactis*, 0.1 μg mL⁻¹ amoxicillin reduced mean length:width ratio from 1.37±0.17 to 1.21±0.19 (approximately 50 cells; *P*<0.01), producing nearly spherical cells but no obvious septum-positioning defect. Thus ellipsoidality itself is not required to select the next division site in this assay. (david2018pbp2bplaysa pages 16-18)

Pneumococcal PG chemistry also tracked elongasome perturbation. A reported wild-type unbranched/branched muropeptide peak ratio of 2.6 fell to 0.8 after PBP2b depletion, 1.2 after RodA depletion, and 1.7 after Spr0777 depletion or *mreD* deletion. These values support functional coupling but should not be represented as direct causes of ellipsoid shape without an intermediate PG-composition node. (straume2017identificationofpneumococcal pages 12-16)

## 6. Recent developments and current applications

The latest directly retrievable mechanistic full text in this search was from 2021. It established nanoscale separation and persistence of septal versus peripheral synthesis and node/ring organization, substantially refining the classical two-site model. (perez2021organizationofpeptidoglycan pages 1-5, trouve2021nanoscaledynamicsof pages 1-3)

A relevant **2024** primary study is Perez et al., “Elongasome core proteins and class A PBP1a display zonal, processive movement at the midcell of *Streptococcus pneumoniae*,” *PNAS*, DOI [10.1073/pnas.2401831121](https://doi.org/10.1073/pnas.2401831121), published June 2024. Its title/metadata indicate direct tracking of elongasome dynamics and PBP1a, but its full text was unavailable to the retrieval tools; no new edge from it should be curated until its methods, mutants, and quantitative results are checked.

Practical applications include:

- **Antibacterial target discovery:** PBPs are established β-lactam targets, while RodA/FtsW SEDS enzymes, MltG, CozE/MreCD, and FtsZ-associated regulators provide potential noncanonical intervention points. The literature explicitly frames better understanding of PBP regulation and cell division as relevant to combating resistant pneumococci and streptococci. (tan2021streptococcussuismsmk pages 1-2, tsui2016suppressionofa pages 1-3, fenton2016cozeisa pages 1-2)
- **Mechanism-of-action phenotyping:** shifts from ellipsoid to sphere, compressed chains, lemons, or filaments can distinguish impaired peripheral growth, septation, or separation. However, morphology alone is not target-specific because different perturbations converge on similar shapes. (tan2021streptococcussuismsmk pages 8-11, david2018pbp2bplaysa pages 11-13, david2018pbp2bplaysa pages 16-18, straume2017identificationofpneumococcal pages 1-5)
- **Pathogenesis research:** pneumococcal shape/chaining influence colonization and infection, while PG also scaffolds capsule, wall teichoic acid, and surface virulence factors. These links are biologically important but are downstream contextual effects rather than defining edges of the morphology graph. (tsui2016suppressionofa pages 1-3, perez2021organizationofpeptidoglycan pages 1-5)
- **Imaging benchmarks:** FDAA labeling, dSTORM, and pole-on 3D-SIM provide real implementations for separating septal and peripheral activity at nanometre-scale midcell zones. (perez2021organizationofpeptidoglycan pages 1-5, fenton2016cozeisa pages 6-7, trouve2021nanoscaledynamicsof pages 1-3)

## 7. Ontology recommendations

Use `METPO:1000673` verbatim for the target. Safe general candidates include GO terms for peptidoglycan biosynthesis, cell division, cell-cycle processes, transpeptidase activity, glycosyltransferase activity, cytoplasmic membrane, and cell septum, but exact GO accessions should be validated against the current ontology release before committing the YAML. Use taxon-qualified protein labels, such as “PBP2b [*S. pneumoniae* D39],” until a specific strain/proteoform and UniProt accession are verified.

Potential taxon groundings to verify in NCBI Taxonomy are *S. pneumoniae*, *Lactococcus lactis*, and *Streptococcus suis*. Chemical nodes may use ChEBI after release-level verification; the working candidates in the matrix are amoxicillin `CHEBI:28971` and methicillin `CHEBI:6827`. Label-only nodes are preferable to an unverified CURIE.

## 8. Claims not yet ready for TraitMech

1. Do not assert a universal ellipsoidal mechanism across all microbes; evidence here concerns bacterial ovococci.
2. Do not treat “ovoid,” “ellipsoid,” “lemon-shaped,” and “lentil-shaped” as perfectly equivalent without measurements or images.
3. Do not encode chaining as ellipsoidal morphology.
4. Do not make MsmK a universal ovococcal component; its shape role is currently demonstrated in *S. suis*. (tan2021streptococcussuismsmk pages 8-11, tan2021streptococcussuismsmk pages 1-2)
5. Do not curate MltG-to-PBP1a-to-PBP2b:RodA substrate transfer as established fact; the authors call it a model. (tsui2016suppressionofa pages 1-3)
6. Treat bacterial two-hybrid interactions as interaction evidence, not proof of direct contact in the native pneumococcal complex. (straume2017identificationofpneumococcal pages 12-16)
7. Do not infer that spherical shape causes septum misplacement. Amoxicillin made *L. lactis* nearly spherical without obvious septation defects; PBP2b mutants had both defects, indicating separable functions. (david2018pbp2bplaysa pages 16-18)
8. Do not encode β-lactams as native causes of the trait; they are experimental perturbations with concentration-, species-, and target-dependent effects.
9. Do not curate detailed claims from the 2024 PNAS paper until full text is reviewed.
10. Verify the *S. suis* wall-thickness numbers against the final article because the retrieved text contains a direction/value inconsistency. (tan2021streptococcussuismsmk pages 8-11)

## 9. DOI-first bibliography

- Perez AJ et al. **Elongasome core proteins and class A PBP1a display zonal, processive movement at the midcell of *Streptococcus pneumoniae*.** *PNAS*. June 2024. DOI: [10.1073/pnas.2401831121](https://doi.org/10.1073/pnas.2401831121). Full text not retrieved.
- Tan M-F et al. **Streptococcus suis MsmK: Novel Cell Division Protein Interacting with FtsZ and Maintaining Cell Shape.** *mSphere*. Published 17 March 2021. DOI: [10.1128/mSphere.00119-21](https://doi.org/10.1128/mSphere.00119-21). (tan2021streptococcussuismsmk pages 1-2)
- Trouve J et al. **Nanoscale dynamics of peptidoglycan assembly during the cell cycle of *Streptococcus pneumoniae*.** *Current Biology*. 12 July 2021. DOI: [10.1016/j.cub.2021.04.041](https://doi.org/10.1016/j.cub.2021.04.041). (trouve2021nanoscaledynamicsof pages 1-3)
- Perez AJ et al. **Organization of Peptidoglycan Synthesis in Nodes and Separate Rings at Different Stages of Cell Division of *Streptococcus pneumoniae*.** *Molecular Microbiology*. 2021. DOI: [10.1111/mmi.14659](https://doi.org/10.1111/mmi.14659). (perez2021organizationofpeptidoglycan pages 1-5)
- David B et al. **PBP2b plays a key role in both peripheral growth and septum positioning in *Lactococcus lactis*.** *PLOS ONE*. Published 23 May 2018. DOI: [10.1371/journal.pone.0198014](https://doi.org/10.1371/journal.pone.0198014). (david2018pbp2bplaysa pages 1-2)
- Straume D et al. **Identification of pneumococcal proteins that are functionally linked to penicillin-binding protein 2b.** *Molecular Microbiology*. January 2017. DOI: [10.1111/mmi.13543](https://doi.org/10.1111/mmi.13543). (straume2017identificationofpneumococcal pages 1-5)
- Fenton AK et al. **CozE is a member of the MreCD complex that directs cell elongation in *Streptococcus pneumoniae*.** *Nature Microbiology*. Final article 2017; DOI registered/published online in 2016. DOI: [10.1038/nmicrobiol.2016.237](https://doi.org/10.1038/nmicrobiol.2016.237). (fenton2016cozeisa pages 1-2)
- Tsui H-CT et al. **Suppression of a Deletion Mutation in the Gene Encoding Essential PBP2b Reveals a New Lytic Transglycosylase Involved in Peripheral Peptidoglycan Synthesis in *Streptococcus pneumoniae* D39.** *Molecular Microbiology*. June 2016. DOI: [10.1111/mmi.13366](https://doi.org/10.1111/mmi.13366). (tsui2016suppressionofa pages 1-3)
- Philippe J, Vernet T, Zapun A. **The elongation of ovococci.** *Microbial Drug Resistance*. June 2014. DOI: [10.1089/mdr.2014.0032](https://doi.org/10.1089/mdr.2014.0032). This is the supplied existing evidence and supports the named ovococcal shape class.
- Zapun A, Vernet T, Pinho MG. **The different shapes of cocci.** *FEMS Microbiology Reviews*. First published February 2008. DOI: [10.1111/j.1574-6976.2007.00098.x](https://doi.org/10.1111/j.1574-6976.2007.00098.x). (zapun2008thedifferentshapes pages 1-2)

## Recommended graph core

For `data/traits/morphology/ellipsoidal.yaml`, the safest initial core is:

**FtsZ-organized midcell PG synthesis → coordinated septal and peripheral PG synthesis → longitudinal elongation plus cross-wall formation → `METPO:1000673`**, with taxon-qualified mechanistic branches for **PBP2x:FtsW** and **PBP2b:RodA–MreCD–CozE/DivIVA/Spr0777**, plus **PBP1a/MltG-mediated PG synthesis and remodeling**. Add MsmK and β-lactam perturbations only as explicitly taxon- or assay-specific subgraphs.

References

1. (zapun2008thedifferentshapes pages 3-5): André Zapun, Thierry Vernet, and Mariana G. Pinho. The different shapes of cocci. FEMS microbiology reviews, 32 2:345-60, Mar 2008. URL: https://doi.org/10.1111/j.1574-6976.2007.00098.x, doi:10.1111/j.1574-6976.2007.00098.x. This article has 275 citations and is from a domain leading peer-reviewed journal.

2. (tsui2016suppressionofa pages 1-3): Ho‐Ching Tiffany Tsui, Jiaqi J. Zheng, Ariel N. Magallon, John D. Ryan, Rachel Yunck, Britta E. Rued, Thomas G. Bernhardt, and Malcolm E. Winkler. Suppression of a deletion mutation in the gene encoding essential pbp2b reveals a new lytic transglycosylase involved in peripheral peptidoglycan synthesis in streptococcus pneumoniae d39. Molecular Microbiology, 100:1039-1065, Jun 2016. URL: https://doi.org/10.1111/mmi.13366, doi:10.1111/mmi.13366. This article has 112 citations and is from a domain leading peer-reviewed journal.

3. (straume2017identificationofpneumococcal pages 1-5): Daniel Straume, Gro Anita Stamsås, Kari Helene Berg, Zhian Salehian, and Leiv Sigve Håvarstein. Identification of pneumococcal proteins that are functionally linked to penicillin‐binding protein 2b (pbp2b). Molecular Microbiology, 103:99-116, Jan 2017. URL: https://doi.org/10.1111/mmi.13543, doi:10.1111/mmi.13543. This article has 44 citations and is from a domain leading peer-reviewed journal.

4. (perez2021organizationofpeptidoglycan pages 1-5): Amilcar J. Perez, Michael J. Boersma, Kevin E. Bruce, Melissa M. Lamanna, Sidney L. Shaw, Ho‐Ching T. Tsui, Atsushi Taguchi, Erin E. Carlson, Michael S. VanNieuwenhze, and Malcolm E. Winkler. Organization of peptidoglycan synthesis in nodes and separate rings at different stages of cell division of <i>streptococcus pneumoniae</i>. Dec 2021. URL: https://doi.org/10.1111/mmi.14659, doi:10.1111/mmi.14659. This article has 40 citations and is from a domain leading peer-reviewed journal.

5. (tan2021streptococcussuismsmk pages 1-2): Mei-Fang Tan, Qiao Hu, Zhe Hu, Chun-Yan Zhang, Wan-Quan Liu, Ting Gao, Liang-Sheng Zhang, Lun Yao, Hai-Qin Li, Yan-Bin Zeng, and Rui Zhou. Streptococcus suis msmk: novel cell division protein interacting with ftsz and maintaining cell shape. Apr 2021. URL: https://doi.org/10.1128/msphere.00119-21, doi:10.1128/msphere.00119-21. This article has 7 citations and is from a peer-reviewed journal.

6. (zapun2008thedifferentshapes pages 1-2): André Zapun, Thierry Vernet, and Mariana G. Pinho. The different shapes of cocci. FEMS microbiology reviews, 32 2:345-60, Mar 2008. URL: https://doi.org/10.1111/j.1574-6976.2007.00098.x, doi:10.1111/j.1574-6976.2007.00098.x. This article has 275 citations and is from a domain leading peer-reviewed journal.

7. (straume2017identificationofpneumococcal pages 12-16): Daniel Straume, Gro Anita Stamsås, Kari Helene Berg, Zhian Salehian, and Leiv Sigve Håvarstein. Identification of pneumococcal proteins that are functionally linked to penicillin‐binding protein 2b (pbp2b). Molecular Microbiology, 103:99-116, Jan 2017. URL: https://doi.org/10.1111/mmi.13543, doi:10.1111/mmi.13543. This article has 44 citations and is from a domain leading peer-reviewed journal.

8. (trouve2021nanoscaledynamicsof pages 1-3): Jennyfer Trouve, André Zapun, Christopher Arthaud, Claire Durmort, Anne Marie Di Guilmi, Bill Söderström, Anais Pelletier, Christophe Grangeasse, Dominique Bourgeois, Yung-Sing Wong, and Cecile Morlot. Nanoscale dynamics of peptidoglycan assembly during the cell cycle of streptococcus pneumoniae. Current Biology, 31:2844-2856.e6, Jul 2021. URL: https://doi.org/10.1016/j.cub.2021.04.041, doi:10.1016/j.cub.2021.04.041. This article has 46 citations and is from a highest quality peer-reviewed journal.

9. (david2018pbp2bplaysa pages 16-18): Blandine David, Marie-Clémence Duchêne, Gabrielle Laurie Haustenne, Daniel Pérez-Núñez, Marie-Pierre Chapot-Chartier, Xavier De Bolle, Eric Guédon, Pascal Hols, and Bernard Hallet. Pbp2b plays a key role in both peripheral growth and septum positioning in lactococcus lactis. PLoS ONE, 13:e0198014, May 2018. URL: https://doi.org/10.1371/journal.pone.0198014, doi:10.1371/journal.pone.0198014. This article has 15 citations and is from a peer-reviewed journal.

10. (straume2017identificationofpneumococcal pages 16-19): Daniel Straume, Gro Anita Stamsås, Kari Helene Berg, Zhian Salehian, and Leiv Sigve Håvarstein. Identification of pneumococcal proteins that are functionally linked to penicillin‐binding protein 2b (pbp2b). Molecular Microbiology, 103:99-116, Jan 2017. URL: https://doi.org/10.1111/mmi.13543, doi:10.1111/mmi.13543. This article has 44 citations and is from a domain leading peer-reviewed journal.

11. (fenton2016cozeisa pages 1-2): Andrew K. Fenton, Lamya El Mortaji, Derek T. C. Lau, David Z. Rudner, and Thomas G. Bernhardt. Coze is a member of the mrecd complex that directs cell elongation in streptococcus pneumoniae. Nature Microbiology, Dec 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.237, doi:10.1038/nmicrobiol.2016.237. This article has 91 citations and is from a highest quality peer-reviewed journal.

12. (tan2021streptococcussuismsmk pages 8-11): Mei-Fang Tan, Qiao Hu, Zhe Hu, Chun-Yan Zhang, Wan-Quan Liu, Ting Gao, Liang-Sheng Zhang, Lun Yao, Hai-Qin Li, Yan-Bin Zeng, and Rui Zhou. Streptococcus suis msmk: novel cell division protein interacting with ftsz and maintaining cell shape. Apr 2021. URL: https://doi.org/10.1128/msphere.00119-21, doi:10.1128/msphere.00119-21. This article has 7 citations and is from a peer-reviewed journal.

13. (david2018pbp2bplaysa pages 1-2): Blandine David, Marie-Clémence Duchêne, Gabrielle Laurie Haustenne, Daniel Pérez-Núñez, Marie-Pierre Chapot-Chartier, Xavier De Bolle, Eric Guédon, Pascal Hols, and Bernard Hallet. Pbp2b plays a key role in both peripheral growth and septum positioning in lactococcus lactis. PLoS ONE, 13:e0198014, May 2018. URL: https://doi.org/10.1371/journal.pone.0198014, doi:10.1371/journal.pone.0198014. This article has 15 citations and is from a peer-reviewed journal.

14. (david2018pbp2bplaysa pages 11-13): Blandine David, Marie-Clémence Duchêne, Gabrielle Laurie Haustenne, Daniel Pérez-Núñez, Marie-Pierre Chapot-Chartier, Xavier De Bolle, Eric Guédon, Pascal Hols, and Bernard Hallet. Pbp2b plays a key role in both peripheral growth and septum positioning in lactococcus lactis. PLoS ONE, 13:e0198014, May 2018. URL: https://doi.org/10.1371/journal.pone.0198014, doi:10.1371/journal.pone.0198014. This article has 15 citations and is from a peer-reviewed journal.

15. (fenton2016cozeisa pages 6-7): Andrew K. Fenton, Lamya El Mortaji, Derek T. C. Lau, David Z. Rudner, and Thomas G. Bernhardt. Coze is a member of the mrecd complex that directs cell elongation in streptococcus pneumoniae. Nature Microbiology, Dec 2016. URL: https://doi.org/10.1038/nmicrobiol.2016.237, doi:10.1038/nmicrobiol.2016.237. This article has 91 citations and is from a highest quality peer-reviewed journal.