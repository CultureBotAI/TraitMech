---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:44:35.015067'
end_time: '2026-08-04T07:59:28.040869'
duration_seconds: 893.03
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width
  trait_identifier: METPO:1000882
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that inheres in a cell by virtue of its shorter dimension
    when viewed on a plane.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan
    synthesis (Bacterial rod-shape review identifies MreB-directed lateral wall synthesis
    as the control point governing cell width.) | DOI:10.1038/nrmicro3088: rod-shape
    is maintained (Cell-wall biosynthesis review supports lateral peptidoglycan assembly
    as the cellular machinery setting rod width.)'
  causal_graph_summary: 'cell_width_mreb_lateral_wall: 9 nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000882
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its shorter dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Bacterial rod-shape review identifies MreB-directed lateral wall synthesis as the control point governing cell width.) | DOI:10.1038/nrmicro3088: rod-shape is maintained (Cell-wall biosynthesis review supports lateral peptidoglycan assembly as the cellular machinery setting rod width.)
- **Existing causal graph summary:** cell_width_mreb_lateral_wall: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **cell width** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width.yaml`.

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
- **Trait label:** cell width
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000882
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its shorter dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Bacterial rod-shape review identifies MreB-directed lateral wall synthesis as the control point governing cell width.) | DOI:10.1038/nrmicro3088: rod-shape is maintained (Cell-wall biosynthesis review supports lateral peptidoglycan assembly as the cellular machinery setting rod width.)
- **Existing causal graph summary:** cell_width_mreb_lateral_wall: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **cell width** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width.yaml`.

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


# Microbial Trait Causal Graph Research Report: Cell Width (METPO:1000882)

## 1. Trait Scope Summary

**Trait:** Cell width (METPO:1000882)  
**Definition:** A phenotype that inheres in a cell by virtue of its shorter dimension when viewed on a plane.  
**Category:** MORPHOLOGY  
**Parent trait:** METPO:1000059

Cell width is the lateral or radial dimension of rod-shaped bacterial cells, perpendicular to the long axis. It is mechanistically distinct from cell length (axial elongation), although both dimensions contribute to overall rod shape and aspect ratio. Width is primarily controlled by the orientation and activity of circumferential peptidoglycan (PG) synthesis machinery, specifically the MreB-directed Rod complex (elongasome). Width excludes processes governing septation, cell division septum thickness, or specialized stalk width in organisms like *Caulobacter crescentus*.

The most direct mechanistic insight is provided by Hussain et al. (2018, DOI:10.1101/197475), who demonstrate that MreB filaments orient along the greatest principal membrane curvature—the circumference of rod-shaped cells—and propose a model where "bacterial width may be specified by opposing actions... a decreasing, 'thinning' activity from the action of MreB and its associated SEDS family PG synthases, and an increasing 'fattening' activity from the non-MreB associated Class A PG synthases" (hussain2017mrebfilamentscreate pages 35-39). This establishes width as a dynamic equilibrium phenotype determined by spatially distinct PG synthesis systems.

---

## 2. Candidate Causal Graph Entities

Evidence-backed entities grouped by type are catalogued below with suggested ontology grounding where robust identifiers exist.

### 2.1 Genes, Proteins, Enzymes, Transporters, and Complexes

| Entity | Function/Role | Taxon Context | Suggested Grounding | Notes |
|--------|---------------|---------------|---------------------|-------|
| **MreB** | Bacterial actin homolog; cytoplasmic filament aligning to membrane curvature | *E. coli*, *B. subtilis*, *Salmonella*, *Geobacillus* | Label-only (species-specific IDs not verified) | Central scaffolding protein directing lateral PG synthesis orientation (hussain2017mrebfilamentscreate pages 35-39, morgenstein2015rodzlinksmreb pages 5-6, mao2023ontherole pages 2-3) |
| **RodZ** | Transmembrane linker protein coupling cytoplasmic MreB to periplasmic PG synthesis machinery | *E. coli* | Label-only | Dual role: direct width regulation and mediating MreB rotation; loss increases width (morgenstein2015rodzlinksmreb pages 5-6, ago2023relationshipbetweenthe pages 14-16, morgenstein2015rodzlinksmreb pages 2-4) |
| **RodA (MrdB)** | SEDS-family glycosyltransferase; polymerizes PG glycan strands | *E. coli*, *Salmonella* | Label-only | Forms complex with PBP2; mutations (e.g., RodA^A234T) enhance PG synthesis activity and suppress RodZ defects (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 10-11, ago2023relationshipbetweenthe media c5a06158) |
| **PBP2 (MrdA)** | Class B penicillin-binding protein; transpeptidase crosslinking PG | *E. coli*, *Salmonella* | Label-only | Partner enzyme in RodA-PBP2 synthase; structural opening regulated by interface II contacts and MreC (shlosman2023allostericactivationof pages 2-3, shlosman2023allostericactivationof pages 8-9) |
| **PBP2^SAL** | Homolog of PBP2 expressed under acidic pH | *Salmonella* Typhimurium | Label-only | Forms pH-dependent alternative elongasome independent of canonical PBP2; alters cell dimensions at low pH (castanheira2023evidenceoftwo pages 7-8, castanheira2023evidenceoftwo pages 2-3, castanheira2023evidenceoftwo pages 13-14) |
| **MreC** | Periplasmic Rod complex component | *E. coli*, *Salmonella* | Label-only | Activates RodA-PBP2 by inducing conformational change; suppressor mutations rescue RodZ defects (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 10-11, shlosman2023allostericactivationof pages 2-3) |
| **MreD** | Periplasmic Rod complex component | *E. coli* | Label-only | Function less clear; suppressor mutations also identified (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 10-11) |
| **Rod complex (elongasome)** | Multiprotein assembly including MreB, RodZ, MreC, MreD, RodA, PBP2 | *E. coli*, *Salmonella*, *B. subtilis* | Label-only or GO:0032153 (cell division site) partially relevant | Dynamic, membrane-associated machine inserting lateral PG to maintain rod shape; activity inversely correlates with PG structural defects (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe media c5a06158) |
| **LpxC** | UDP-3-O-acyl-N-acetylglucosamine deacetylase; first committed step in LPS synthesis | *E. coli* | Label-only | Overexpression rescues rod shape in *mreC* hypomorphs by increasing outer membrane stiffness (fivenson2023arolefor pages 3-5, fivenson2023arolefor pages 2-3) |
| **FtsH** | Inner membrane metalloprotease | *E. coli* | Label-only | Degrades LpxC; hypomorphic alleles (e.g., FtsH^V41G) stabilize LpxC and increase LPS, indirectly restoring rod width (fivenson2023arolefor pages 3-5, fivenson2023arolefor pages 2-3) |
| **Class A PBPs (aPBPs)** | Bifunctional PG synthases with glycosyltransferase and transpeptidase domains | Gram-negative bacteria | GO:0008955 (peptidoglycan glycosyltransferase activity) | Proposed "fattening" activity opposing MreB-directed thinning (hussain2017mrebfilamentscreate pages 35-39) |

### 2.2 Chemicals, Metabolites, and Inhibitors

| Entity | Function | Suggested Grounding | Notes |
|--------|----------|---------------------|-------|
| **Peptidoglycan (PG)** | Bacterial cell wall polymer of glycan chains crosslinked by peptide bridges | GO:0009274 (peptidoglycan-based cell wall) | Structural scaffold resisting turgor; PG pore size inversely correlates with Rod complex activity (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe media c5a06158) |
| **Lipid II** | Lipid-linked PG precursor | CHEBI:64722 (undecaprenyl diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine) | Substrate for RodA polymerization | Extracellular precursor flipped across inner membrane; polymerized by RodA (indirect relevance to width) |
| **Lipopolysaccharide (LPS)** | Outer leaflet lipid of Gram-negative outer membrane | CHEBI:25017 (lipopolysaccharide) | Increasing LPS concentration stiffens outer membrane, enabling proper MreB orientation in *mreC* mutants (fivenson2023arolefor pages 3-5, fivenson2023arolefor pages 2-3, fivenson2023arolefor pages 7-8) |
| **O-antigen** | Polysaccharide extension of LPS core | Label-only | Restoring O-antigen increases OM stiffness, rescuing rod shape defects (fivenson2023arolefor pages 7-8) |
| **ATP/GTP** | Nucleotides | CHEBI:15422 (ATP), CHEBI:15996 (GTP) | Required for MreB polymerization on lipid surfaces; hydrolysis sustains dynamic filament turnover (mao2023ontherole pages 2-3, mao2023ontherole pages 14-15) |

### 2.3 Environmental Factors and Experimental Factors

| Factor | Effect | Evidence |
|--------|--------|----------|
| **Acidic pH (pH 4.6)** | Switches expression from PBP2/PBP3 to PBP2^SAL/PBP3^SAL elongasome; alters cell length and width | *Salmonella* Typhimurium acidic intracellular niche; measured in PCN medium pH 4.6 vs. pH 7.4 (castanheira2023evidenceoftwo pages 7-8, castanheira2023evidenceoftwo pages 2-3) |
| **Osmotic stress (NaCl ~1.1 Osm, sucrose ~1.0 Osm)** | Cells lacking MreB rotation (MreB^S14A ΔrodZ) lose rod shape under elevated osmolarity | *E. coli* grown in LB + osmotica (morgenstein2015rodzlinksmreb pages 5-6) |
| **Membrane fluidity** | Low fluidity impairs MreB localization; high fluidity associated with functional elongasome activity | Indirect relevance: fatty acid desaturation modulates membrane fluidity; not directly width-specific but affects Rod complex function |

### 2.4 Organelles, Cellular Localizations, and Biological Processes

| Entity | Description | Suggested Grounding | Notes |
|--------|-------------|---------------------|-------|
| **Inner (cytoplasmic) membrane** | Lipid bilayer housing MreB filaments and Rod complex | GO:0016020 (membrane), GO:0005886 (plasma membrane) | MreB binds via N-terminal amphipathic helix or hydrophobic loop (mao2023ontherole pages 2-3) |
| **Periplasmic space** | Compartment between inner and outer membranes in Gram-negatives | GO:0030288 (outer membrane-bounded periplasmic space) | Site of PG synthesis and crosslinking by PBP2 (shlosman2023allostericactivationof pages 2-3) |
| **Outer membrane (OM)** | Second lipid bilayer unique to Gram-negatives | GO:0009279 (cell outer membrane) | Provides mechanical stability; stiffness modulates MreB-directed PG synthesis (fivenson2023arolefor pages 3-5, fivenson2023arolefor pages 7-8) |
| **Cell shape determination** | Biological process | GO:0008360 (regulation of cell shape) | Overarching process integrating PG synthesis, membrane mechanics, and MreB dynamics |
| **Peptidoglycan biosynthetic process** | Metabolic process | GO:0009252 (peptidoglycan biosynthetic process) | Core pathway; lateral synthesis by Rod complex determines width |

---

## 3. Evidence-Backed Causal Edges

A curated table of mechanistic relationships is presented below. Each edge is supported by at least one primary source with exact supporting snippet, DOI, and publication date.

| Subject | Predicate | Object | Taxon | Evidence Type | Supporting Snippet | Publication | Notes |
|---------|-----------|--------|-------|---------------|--------------------|-------------|-------|
| MreB filaments | orient along | greatest principal membrane curvature | *B. subtilis*, *E. coli* | Fluorescence microscopy, biophysical modeling | "MreB orients along the greatest principal membrane curvature... The tendency of MreB to align and move along the direction of greatest principal curvature may also explain the absence of MreB at cell poles." | Hussain et al., 2017, 10.1101/197475 (hussain2017mrebfilamentscreate pages 35-39) | MreB alignment along the shorter dimension (circumference) establishes the path for lateral PG synthesis, thus regulating cell diameter. |
| MreB and SEDS family PG synthases | decrease | cell diameter | *B. subtilis*, *E. coli* | Theoretical model | "bacterial width may be specified by opposing actions... a decreasing, 'thinning' activity from the action of MreB and its associated SEDS family PG synthases" | Hussain et al., 2017, 10.1101/197475 (hussain2017mrebfilamentscreate pages 35-39) | Proposes a dynamic equilibrium where elongasome activity "thins" the cell width, opposing the "fattening" activity of Class A PBPs. |
| RodZ | couples | MreB to cell wall synthesis (PBP2/RodA) | *E. coli* | 3D particle tracking, BiFC | "RodZ couples MreB to cell wall synthesis by interacting with MreB in the cytoplasm and PBP2 and/or RodA in the periplasm." | Morgenstein et al., 2015, 10.1073/pnas.1509610112 (morgenstein2015rodzlinksmreb pages 5-6, morgenstein2015rodzlinksmreb pages 2-4) | Mediates a dual role: robust rod shape maintenance via helix-turn-helix, and MreB rotation via juxta-membrane site. |
| MreB rotation | increases | robustness of rod shape | *E. coli* | Mutagenesis, osmotic stress assay | "When MreB is unable to rotate (MreBS14AΔrodZ), cells that grew as rods in LB media... became spheroid under the osmotic stress" | Morgenstein et al., 2015, 10.1073/pnas.1509610112 (morgenstein2015rodzlinksmreb pages 5-6) | Rotation is not strictly essential for basic rod shape initiation, but prevents local defects from amplifying under osmotic/PG stress. |
| RodZ deletion (ΔrodZ) | increases | cell width | *E. coli* | Cell-shape analysis, phase contrast | "MreBS14A ΔrodZ had less deviation than ΔrodZ alone, indicating it restores rod shape... These cells did not fully phenocopy WT cells in so far as they had an increase in width" | Morgenstein et al., 2015, 10.1073/pnas.1509610112 (morgenstein2015rodzlinksmreb pages 2-4) | Independent of driving rotation, RodZ has a separable direct role in restricting cell width. |
| RMR mutation in RodZ | alters | peptidoglycan hole size | *E. coli* | QFDE-EM | "The peptidoglycan purified from the RMR cells clearly had larger holes (42.2 ± 81.0 nm2), and the number of holes was higher than that of the peptidoglycan purified from WT cells" | Ago et al., 2023, 10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe media c5a06158) | WT PG pore size is 19.7 nm², whereas RMR mutant is 42.1 nm². Impaired Rod complex activity structurally compromises PG integrity. |
| MreB, MreC, MreD, PBP2, RodA suppressor mutations | restore | peptidoglycan structure and cell shape | *E. coli* | Mutagenesis, sequencing, EM | "most of the suppressor mutations... were found in the components of the Rod complex... The N-terminal cytoplasmic region interacts with MreB, and the C-terminal periplasmic region interacts with RodZ, MreC, MreD, and PBP2" | Ago et al., 2023, 10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe pages 10-11, ago2023relationshipbetweenthe media c5a06158) | Suppressor mutations (e.g., MreBA125V) rescue the RMR defect, shrinking PG holes back to ~23.6 nm² and restoring normal rod morphology. |
| PBP2 Interface II | inhibits | PG polymerization by RodA | *E. coli* | smFRET, Mutagenesis | "interface II acts as an inhibitor of catalysis, repressing polymerization and sequestering PBP2 away from its PG substrate" | Shlosman et al., 2023, 10.1038/s41467-023-39037-9 (shlosman2023allostericactivationof pages 2-3, shlosman2023allostericactivationof pages 8-9) | Autoinhibition mechanism within the RodA-PBP2 synthase. Structural opening is facilitated by MreC within the active Rod complex. |
| Outer membrane stiffness (LPS/O-antigen) | reinforces | rod shape | *E. coli* | Epifluorescence microscopy, genetic suppression | "LPS packing in the OM is required for the overexpression of lpxC to improve the growth of mreC hypormorphs... OM contributes to shape determination by providing sufficient envelope stability for MreB-directed PG synthesis to be properly oriented" | Fivenson et al., 2023, 10.1073/pnas.2301987120 (fivenson2023arolefor pages 3-5, fivenson2023arolefor pages 7-8) | Increased outer membrane LPS stiffness rescues rod shape (including width regulation) in spherical mreC mutants (mreCR292H, mreCG156D). |
| Acidic pH | activates | PBP2SAL elongasome | *S.* Typhimurium | Proteomics, Immunoprecipitation | "bacteria growing in PCN pH 4.6 produce essentially PBP2SAL/PBP3SAL instead of PBP2/PBP3... loss in S. Typhimurium of PBP2 or PBP2SAL in cells growing in acidic pH results in changes in length and width" | Castanheira & García-del Portillo, 2023, 10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 7-8, castanheira2023evidenceoftwo pages 2-3) | Pathogens deploy alternative, functionally independent elongasomes (PBP2 vs PBP2SAL) depending on environmental pH, shifting cellular dimensions. |


*Table: This table catalogs specific, source-backed causal relationships governing microbial cell width and morphology. It covers MreB curvature sensing, elongasome coordination via RodZ, outer membrane mechanics, and peptidoglycan pore dynamics.*

### 3.1 Additional High-Priority Edges

**Edge 1:** Principal membrane curvature → MreB filament orientation  
- **Taxon:** *E. coli*, *B. subtilis*  
- **Reference:** Hussain et al., 2018, DOI:10.1101/197475 (hussain2017mrebfilamentscreate pages 35-39)  
- **Snippet:** "MreB orients along the greatest principal membrane curvature... The tendency of MreB to align and move along the direction of greatest principal curvature may also explain the absence of MreB at cell poles."  
- **Notes:** MreB filaments (200 nm curvature) align circumferentially around rod-shaped cells (900 nm diameter), thus directing lateral PG insertion perpendicular to the long axis and maintaining/reducing diameter. Biophysical model supported by experimental data in spherical vs. rod-shaped cells.  
- **Assay:** Fluorescence microscopy of MreB-mNeon, 3D cell contouring, microfluidics, biophysical modeling.

**Edge 2:** RodA-PBP2 interface II contacts → Inhibition of PG polymerization  
- **Taxon:** *E. coli*, *Thermus thermophilus*  
- **Reference:** Shlosman et al., 2023, DOI:10.1038/s41467-023-39037-9 (shlosman2023allostericactivationof pages 2-3, shlosman2023allostericactivationof pages 8-9)  
- **Snippet:** "interface II acts as an inhibitor of catalysis, repressing polymerization and sequestering PBP2 away from its PG substrate"  
- **Notes:** Autoinhibitory mechanism within RodA-PBP2 synthase; disruption of interface II (e.g., PBP2^T52A, PBP2^L61R) shifts ensemble to open state, hyperactivating PG synthesis. MreC relieves inhibition in the assembled Rod complex. Single-molecule FRET and cryo-EM structural evidence.  
- **Assay:** smFRET, cryo-EM, in vitro polymerization assays, mecillinam sensitivity, cell morphology quantification (length-to-width ratio).

**Edge 3:** Impaired Rod complex activity (RodZ^RMR mutant) → Increased peptidoglycan pore size  
- **Taxon:** *E. coli*  
- **Reference:** Ago et al., 2023, DOI:10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 14-16, ago2023relationshipbetweenthe media c5a06158)  
- **Snippet:** "The peptidoglycan purified from the RMR cells clearly had larger holes (42.2 ± 81.0 nm²), and the number of holes was higher than that of the peptidoglycan purified from WT cells"  
- **Quantitative data:** WT PG pore size 19.7 ± 28.6 nm² (n=3353 holes); ΔrodZ 30.0 ± 51.0 nm² (n=9809); RMR 42.1 ± 81.1 nm² (n=7574); suppressor RodA^A234T 11.7 ± 11.5 nm² (n=347).  
- **Notes:** RMR is a transmembrane-truncated RodZ (MalF^17-39 substitution) with reduced Rod complex integrity; suppressor mutations in MreB, MreC, MreD, PBP2, RodA restore normal PG structure. Direct EM visualization of PG architecture using quick-freeze deep-etch electron microscopy (QFDE-EM).  
- **Assay:** QFDE-EM, LC/MS muropeptide analysis, cell morphology (width measured), growth rate.

**Edge 4:** Outer membrane LPS stiffness → Stabilization of MreB-directed PG synthesis orientation  
- **Taxon:** *E. coli*  
- **Reference:** Fivenson et al., 2023, DOI:10.1073/pnas.2301987120 (fivenson2023arolefor pages 3-5, fivenson2023arolefor pages 2-3, fivenson2023arolefor pages 7-8)  
- **Snippet:** "OM contributes to shape determination by providing sufficient envelope stability for MreB-directed PG synthesis to be properly oriented and self-reinforcing"  
- **Notes:** Spherical *mreC* hypomorphs (mreC^R292H, mreC^G156D) are rescued by: (1) hypomorphic FtsH alleles stabilizing LpxC, (2) lpxC overexpression, or (3) restoring O-antigen. Rod shape (including width) is restored without activating Rod complex directly. Chelating Mg²⁺ with EDTA reverses suppression. Mechanism: increased LPS packing stiffens OM, enabling proper MreB localization and PG feedback.  
- **Assay:** Spot dilutions, immunoblot (LpxC), silver stain (lipid A-core LPS), phase microscopy + MicrobeJ aspect ratio quantification, radiolabeling of nascent PG turnover.

**Edge 5:** Acidic pH → Expression of PBP2^SAL elongasome (independent of PBP2)  
- **Taxon:** *Salmonella enterica* serovar Typhimurium  
- **Reference:** Castanheira & García-del Portillo, 2023, DOI:10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 7-8, castanheira2023evidenceoftwo pages 2-3, castanheira2023evidenceoftwo pages 13-14)  
- **Snippet:** "bacteria growing in PCN pH 4.6 produce essentially PBP2^SAL/PBP3^SAL instead of PBP2/PBP3... loss in S. Typhimurium of PBP2 or PBP2^SAL in cells growing in acidic pH results in changes in length and width"  
- **Notes:** Two functionally independent elongasomes coexist but are differentially regulated: PBP2 at neutral pH, PBP2^SAL at acidic pH. ΔmrdA cells (lacking PBP2) maintain rod shape in acidic conditions via PBP2^SAL. Immunoprecipitation and proteomics confirm physically separate complexes. Quantitative measurements of length and width performed with ObjectJ on phase images.  
- **Assay:** Western blot, immunoprecipitation with DSS crosslinking, LC-MS/MS proteomics (Skyline quantification), fluorescent D-amino acid (FDAA) incorporation, cell dimension analysis.

---

## 4. Ontology Grounding Recommendations

The following CURIEs are suggested for high-confidence grounding. **Label-only nodes are acceptable where stable species-specific protein identifiers are unavailable.**

| Node Label | Suggested CURIE | Rationale |
|------------|----------------|-----------|
| Cell width | **METPO:1000882** | User-provided trait identifier; use verbatim |
| Peptidoglycan-based cell wall | GO:0009274 | Established GO term |
| Regulation of cell shape | GO:0008360 | Overarching biological process |
| Peptidoglycan biosynthetic process | GO:0009252 | Core metabolic pathway |
| Outer membrane-bounded periplasmic space | GO:0030288 | Cellular component |
| Membrane | GO:0016020 | Generic membrane term |
| Lipopolysaccharide | CHEBI:25017 | Chemical entity |
| Lipid II (full name) | CHEBI:64722 | PG precursor |
| ATP | CHEBI:15422 | Nucleotide energy source |
| GTP | CHEBI:15996 | Alternative nucleotide |
| *Escherichia coli* | NCBITaxon:562 | Primary experimental organism |
| *Salmonella enterica* | NCBITaxon:28901 | pH-dependent elongasome studies |
| *Bacillus subtilis* | NCBITaxon:1423 | Gram-positive model |

**Do not ground the following without species-specific validation:**  
- MreB, RodZ, PBP2, RodA, MreC, MreD proteins → Use label-only until UniProt or species-specific locus tags are verified.  
- Rod complex / elongasome → Label-only; GO:0032153 (cell division site) is imprecise.

---

## 5. Warnings and Curation Cautions

### 5.1 Indirect Width Evidence

Several studies provide strong indirect evidence for width regulation through morphological readouts such as:
- Aspect ratio (length/width) quantified by MicrobeJ or ObjectJ (fivenson2023arolefor pages 3-5, fivenson2023arolefor pages 7-8, castanheira2023evidenceoftwo pages 2-3).  
- Qualitative "spherical" versus "rod-shaped" classifications (morgenstein2015rodzlinksmreb pages 5-6, ago2023relationshipbetweenthe pages 14-16).  
- Rod shape restoration without explicitly reporting width measurements.

**Recommendation:** Flag these edges as "indirect—rod shape restoration implies width regulation" in TraitMech curation. Direct width or diameter measurements are rare outside Ago et al. 2023 (ago2023relationshipbetweenthe media c5a06158) and Hussain et al. 2018 model (hussain2017mrebfilamentscreate pages 35-39).

### 5.2 Taxon-Specific Mechanisms

- **PBP2^SAL elongasome:** Specific to *Salmonella* and closely related *Enterobacterales*; not found in *E. coli* K-12 or *B. subtilis* (castanheira2023evidenceoftwo pages 7-8, castanheira2023evidenceoftwo pages 13-14).  
- **MreB membrane anchoring:** Gram-negative MreB uses N-terminal amphipathic helix (*E. coli*) or small hydrophobic loop (*T. maritima*, *Spiroplasma*); Gram-positive MreB (*G. stearothermophilus*) may differ (mao2023ontherole pages 2-3).  
- **Outer membrane mechanics:** Relevant only to Gram-negative bacteria; Gram-positive analogs involve wall teichoic acids and thicker PG layers.

**Recommendation:** Annotate taxon restrictions explicitly; avoid extrapolating Gram-negative OM findings to Gram-positives.

### 5.3 Mechanistic Uncertainty

- **MreB "thinning" vs. aPBP "fattening" model:** Proposed by Hussain et al. 2018 (hussain2017mrebfilamentscreate pages 35-39) as a theoretical framework; not yet directly validated by quantitative width measurements of single/double mutants.  
- **RodZ dual role:** Separable functions (MreB rotation vs. direct width control) are inferred from suppressor genetics (morgenstein2015rodzlinksmreb pages 2-4, morgenstein2015rodzlinksmreb pages 5-6), but the molecular mechanism of the direct width-restriction activity remains unclear.  
- **Membrane fluidity effects:** Indirect; reduced fluidity affects Rod complex function (MreB localization, elongasome mobility), but causal path to width alteration is not demonstrated.

**Recommendation:** Mark these edges as "inferred" or "model-based" until experimental perturbations directly measure width changes.

### 5.4 Assay-Specific Limitations

- **PG pore size (Ago et al. 2023):** Reflects Rod complex activity/PG integrity but is not a direct measurement of live-cell width; purified PG analyzed post-extraction (ago2023relationshipbetweenthe media c5a06158).  
- **smFRET (Shlosman et al. 2023):** In vitro reconstitution of RodA-PBP2; conformational dynamics validated, but direct link to cellular width requires in vivo correlation (shlosman2023allostericactivationof pages 2-3, shlosman2023allostericactivationof pages 8-9).  
- **Aspect ratio:** Conflates length and width changes; suppressor strains may restore rod shape by altering length rather than (or in addition to) width.

**Recommendation:** When curating edges, note whether width is measured directly (rare), inferred from aspect ratio (common), or modeled (Hussain et al. 2018).

### 5.5 Claims Not Yet Supported for Curation

The following mechanisms are discussed in the literature but lack sufficient direct width evidence:
- Membrane fluidity modulation (Willdigg et al. 2021, 2023; Gohrbandt et al. 2022) → Affects Rod complex but no direct width measurements.  
- Fatty acid synthesis balance (Willdigg et al. 2023) → Rescues PG-limited cells but effect on width not quantified.  
- MreB polymerization dynamics (Mao et al. 2023) → ATP-dependent turnover demonstrated in vitro; relevance to width control in vivo not established.

**Recommendation:** Do not curate these into `cell_width.yaml` without additional validation.

---

## 6. DOI-First Bibliography

All references are ordered by first author surname, then year. Publication dates and DOI URLs are provided.

1. **Ago, R., Tahara, Y. O., Yamaguchi, H., Saito, M., Ito, W., Yamasaki, K., Kasai, T., Okamoto, S., Chikada, T., Oshima, T., Osaka, I., Miyata, M., Niki, H., & Shiomi, D.** (2023). Relationship between the Rod complex and peptidoglycan structure in *Escherichia coli*. *MicrobiologyOpen*, 12(5), e1385. DOI:[10.1002/mbo3.1385](https://doi.org/10.1002/mbo3.1385). Published: October 2023.

2. **Castanheira, S., & García-del Portillo, F.** (2023). Evidence of two differentially regulated elongasomes in *Salmonella*. *Communications Biology*, 6, 923. DOI:[10.1038/s42003-023-05308-w](https://doi.org/10.1038/s42003-023-05308-w). Published: September 2023.

3. **Fivenson, E. M., Rohs, P. D. A., Vettiger, A., Sardis, M. F., Torres, G., Forchoh, A., & Bernhardt, T. G.** (2023). A role for the Gram-negative outer membrane in bacterial shape determination. *Proceedings of the National Academy of Sciences*, 120(35), e2301987120. DOI:[10.1073/pnas.2301987120](https://doi.org/10.1073/pnas.2301987120). Published: August 2023.

4. **Hussain, S., Wivagg, C. N., Szwedziak, P., Wong, F., Schaefer, K., Izoré, T., Renner, L. D., Sun, Y., Bisson Filho, A. W., Walker, S., Amir, A., Löwe, J., & Garner, E. C.** (2018). MreB filaments create rod shape by aligning along principal membrane curvature. *eLife*, 7, e32471. DOI:[10.7554/eLife.32471](https://doi.org/10.7554/eLife.32471). [Also available as bioRxiv preprint: DOI:10.1101/197475, October 2017].

5. **Mao, W., Renner, L. D., Cornilleau, C., de la Sierra-Gallay, I. L., Afensiss, S., Benlamara, S., Ah-Seng, Y., van Tilbeurgh, H., Nessler, S., Bertin, A., Chastanet, A., & Carballido-Lopez, R.** (2023). On the role of nucleotides and lipids in the polymerization of the actin homolog MreB from a Gram-positive bacterium. *eLife*, 12, e84505. DOI:[10.7554/eLife.84505](https://doi.org/10.7554/eLife.84505). Published: October 2023.

6. **Morgenstein, R. M., Bratton, B. P., Nguyen, J. P., Ouzounov, N., Shaevitz, J. W., & Gitai, Z.** (2015). RodZ links MreB to cell wall synthesis to mediate MreB rotation and robust morphogenesis. *Proceedings of the National Academy of Sciences*, 112(40), 12510–12515. DOI:[10.1073/pnas.1509610112](https://doi.org/10.1073/pnas.1509610112). Published: September 2015.

7. **Shlosman, I., Fivenson, E. M., Gilman, M. S. A., Sisley, T. A., Walker, S., Bernhardt, T. G., Kruse, A. C., & Loparo, J. J.** (2023). Allosteric activation of cell wall synthesis during bacterial growth. *Nature Communications*, 14, 3439. DOI:[10.1038/s41467-023-39037-9](https://doi.org/10.1038/s41467-023-39037-9). Published: June 2023.

8. **Willdigg, J. R., Patel, Y., & Helmann, J. D.** (2023). A decrease in fatty acid synthesis rescues cells with limited peptidoglycan synthesis capacity. *mBio*, 14(2), e00475-23. DOI:[10.1128/mbio.00475-23](https://doi.org/10.1128/mbio.00475-23). Published: April 2023.

### Additional Supporting References (2024, not extensively analyzed)

9. **Costa, S. F., Saraiva, B. M., Veiga, H., Marques, L. B., Schäper, S., Sporniak, M., Vega, D. E., Jorge, A. M., Duarte, A. M., Brito, A. D., Tavares, A. C., Reed, P., & Pinho, M. G.** (2024). The role of GpsB in *Staphylococcus aureus* cell morphogenesis. *mBio*, 15(3), e03235-23. DOI:[10.1128/mbio.03235-23](https://doi.org/10.1128/mbio.03235-23). Published: March 2024.

10. **Zambri, M. P., Baglio, C. R., Irazoki, O., Jones, S. E., Garner, E. C., Cava, F., & Elliot, M. A.** (2024). Bacteria combine polar- and dispersed-growth to power cell elongation and wall width dynamics. *bioRxiv*. DOI:[10.1101/2024.07.30.605496](https://doi.org/10.1101/2024.07.30.605496). Published: July 2024. [Preprint; not peer-reviewed.]

---

## 7. Summary and Recommendations for `data/traits/morphology/cell_width.yaml`

### Key Mechanistic Nodes (High Confidence)
- **MreB** (label-only): Central curvature sensor and scaffold
- **RodZ** (label-only): Cytoplasm–periplasm linker; dual function in width and robustness
- **RodA** (label-only): SEDS glycosyltransferase
- **PBP2** (label-only): Transpeptidase
- **MreC, MreD** (label-only): Activator proteins
- **Peptidoglycan** (GO:0009274): Structural output
- **Outer membrane LPS** (CHEBI:25017): Mechanical constraint
- **Acidic pH** (environmental perturbation): Activates alternative elongasome in pathogens

### Core Causal Edges (Curate with Confidence)
1. MreB filaments → orient along greatest principal curvature → direct lateral PG synthesis circumferentially → maintain/reduce cell width (Hussain 2018, DOI:10.7554/eLife.32471).
2. RodZ → couples MreB (cytoplasm) to RodA-PBP2 (periplasm) → robust rod shape; loss increases width (Morgenstein 2015, DOI:10.1073/pnas.1509610112).
3. Impaired Rod complex (e.g., RodZ^RMR) → larger PG pores → compromised structural integrity → aberrant width/shape (Ago 2023, DOI:10.1002/mbo3.1385).
4. RodA-PBP2 interface II → autoinhibits polymerization; relief by MreC → activated PG synthesis (Shlosman 2023, DOI:10.1038/s41467-023-39037-9).
5. Increased OM LPS stiffness → stabilizes MreB-directed synthesis → rescues width in *mreC* hypomorphs (Fivenson 2023, DOI:10.1073/pnas.2301987120).
6. Acidic pH → upregulates PBP2^SAL elongasome → alters cell dimensions (*Salmonella*-specific; Castanheira 2023, DOI:10.1038/s42003-023-05308-w).

### Edge Uncertainties and Exclusions
- **Do not curate:** Membrane fluidity, fatty acid synthesis balance, or in vitro MreB polymerization dynamics until direct width measurements are available.
- **Flag as indirect:** Aspect ratio / rod shape restoration evidence where explicit width is not measured.
- **Taxon-restrict:** PBP2^SAL to *Enterobacterales*; OM mechanics to Gram-negatives.

This report is ready for expert curation into the TraitMech YAML format.

References

1. (hussain2017mrebfilamentscreate pages 35-39): Saman Hussain, Carl N. Wivagg, Piotr Szwedziak, Felix Wong, Kaitlin Schaefer, Thierry Izoré, Lars D. Renner, Yingjie Sun, Alexandre W. Bisson Filho, Suzanne Walker, Ariel Amir, Jan Löwe, and Ethan C. Garner. Mreb filaments create rod shape by aligning along principal membrane curvature. bioRxiv, Oct 2017. URL: https://doi.org/10.1101/197475, doi:10.1101/197475. This article has 6 citations.

2. (morgenstein2015rodzlinksmreb pages 5-6): Randy M. Morgenstein, Benjamin P. Bratton, Jeffrey P. Nguyen, Nikolay Ouzounov, Joshua W. Shaevitz, and Zemer Gitai. Rodz links mreb to cell wall synthesis to mediate mreb rotation and robust morphogenesis. Proceedings of the National Academy of Sciences, 112:12510-12515, Sep 2015. URL: https://doi.org/10.1073/pnas.1509610112, doi:10.1073/pnas.1509610112. This article has 162 citations and is from a highest quality peer-reviewed journal.

3. (mao2023ontherole pages 2-3): Wei Mao, Lars D Renner, Charlène Cornilleau, Ines Li de la Sierra-Gallay, Sana Afensiss, Sarah Benlamara, Yoan Ah-Seng, Herman Van Tilbeurgh, Sylvie Nessler, Aurélie Bertin, Arnaud Chastanet, and Rut Carballido-Lopez. On the role of nucleotides and lipids in the polymerization of the actin homolog mreb from a gram-positive bacterium. eLife, Oct 2023. URL: https://doi.org/10.7554/elife.84505, doi:10.7554/elife.84505. This article has 12 citations and is from a domain leading peer-reviewed journal.

4. (ago2023relationshipbetweenthe pages 14-16): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 17 citations and is from a peer-reviewed journal.

5. (morgenstein2015rodzlinksmreb pages 2-4): Randy M. Morgenstein, Benjamin P. Bratton, Jeffrey P. Nguyen, Nikolay Ouzounov, Joshua W. Shaevitz, and Zemer Gitai. Rodz links mreb to cell wall synthesis to mediate mreb rotation and robust morphogenesis. Proceedings of the National Academy of Sciences, 112:12510-12515, Sep 2015. URL: https://doi.org/10.1073/pnas.1509610112, doi:10.1073/pnas.1509610112. This article has 162 citations and is from a highest quality peer-reviewed journal.

6. (ago2023relationshipbetweenthe pages 10-11): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 17 citations and is from a peer-reviewed journal.

7. (ago2023relationshipbetweenthe media c5a06158): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 17 citations and is from a peer-reviewed journal.

8. (shlosman2023allostericactivationof pages 2-3): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 47 citations and is from a highest quality peer-reviewed journal.

9. (shlosman2023allostericactivationof pages 8-9): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 47 citations and is from a highest quality peer-reviewed journal.

10. (castanheira2023evidenceoftwo pages 7-8): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 16 citations and is from a peer-reviewed journal.

11. (castanheira2023evidenceoftwo pages 2-3): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 16 citations and is from a peer-reviewed journal.

12. (castanheira2023evidenceoftwo pages 13-14): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 16 citations and is from a peer-reviewed journal.

13. (fivenson2023arolefor pages 3-5): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 98 citations and is from a highest quality peer-reviewed journal.

14. (fivenson2023arolefor pages 2-3): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 98 citations and is from a highest quality peer-reviewed journal.

15. (fivenson2023arolefor pages 7-8): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 98 citations and is from a highest quality peer-reviewed journal.

16. (mao2023ontherole pages 14-15): Wei Mao, Lars D Renner, Charlène Cornilleau, Ines Li de la Sierra-Gallay, Sana Afensiss, Sarah Benlamara, Yoan Ah-Seng, Herman Van Tilbeurgh, Sylvie Nessler, Aurélie Bertin, Arnaud Chastanet, and Rut Carballido-Lopez. On the role of nucleotides and lipids in the polymerization of the actin homolog mreb from a gram-positive bacterium. eLife, Oct 2023. URL: https://doi.org/10.7554/elife.84505, doi:10.7554/elife.84505. This article has 12 citations and is from a domain leading peer-reviewed journal.