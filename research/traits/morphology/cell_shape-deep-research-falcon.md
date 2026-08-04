---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:40:26.863730'
end_time: '2026-08-04T07:51:08.619023'
duration_seconds: 641.76
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell shape
  trait_identifier: METPO:1000666
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_shape
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that describes the characteristic three-dimensional morphological
    form of a microbial cell, determined by cell wall structure, cytoskeletal elements,
    and environmental factors.
  parent_traits: METPO:1000059
  synonyms: Morphology.cell morphology.cell shape, cell_shape
  evidence_summary: 'DOI:10.1038/nrmicro1205: bacterial cell wall ... primary role
    in maintaining cell shape (Supports bacterial cell shape as determined by cell
    wall and cytoskeletal elements.)'
  causal_graph_summary: 'cell_shape_peptidoglycan_cytoskeleton: 14 nodes, 12 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 55
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell shape
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000666
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes the characteristic three-dimensional morphological form of a microbial cell, determined by cell wall structure, cytoskeletal elements, and environmental factors.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.cell shape, cell_shape
- **Existing evidence:** DOI:10.1038/nrmicro1205: bacterial cell wall ... primary role in maintaining cell shape (Supports bacterial cell shape as determined by cell wall and cytoskeletal elements.)
- **Existing causal graph summary:** cell_shape_peptidoglycan_cytoskeleton: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **cell shape** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_shape.yaml`.

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
- **Trait label:** cell shape
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000666
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that describes the characteristic three-dimensional morphological form of a microbial cell, determined by cell wall structure, cytoskeletal elements, and environmental factors.
- **Parent traits:** METPO:1000059
- **Synonyms:** Morphology.cell morphology.cell shape, cell_shape
- **Existing evidence:** DOI:10.1038/nrmicro1205: bacterial cell wall ... primary role in maintaining cell shape (Supports bacterial cell shape as determined by cell wall and cytoskeletal elements.)
- **Existing causal graph summary:** cell_shape_peptidoglycan_cytoskeleton: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **cell shape** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_shape.yaml`.

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


# Curation report: microbial cell shape

## Target and scope

- **Trait:** cell shape
- **Trait CURIE:** **METPO:1000666**
- **Category / kind / status:** MORPHOLOGY / CLASS / REVIEWED
- **Parent:** METPO:1000059

This trait should represent the characteristic three-dimensional geometry of an individual microbial cell—e.g., coccus, straight rod, curved/vibrioid, helical, filamentous/branched, or archaeal disk/polyhedral form. In bacteria, the immediate load-bearing determinant is usually the peptidoglycan (PG) sacculus; shape emerges from the spatial and temporal pattern of PG synthesis, cross-linking, cleavage, and repair rather than merely from the presence of PG. MreB/elongasome or DivIVA/polar-growth systems organize these reactions, while specialized modules generate curvature, helicity, branches, or stalks (teeseling2017determinantsofbacterial pages 3-4, kysela2016diversitytakesshape pages 4-5, shlosman2023allostericactivationof pages 1-2).

Archaea require a separate mechanistic branch: many lack PG and instead use S-layers and archaeal cytoskeletal systems. In *Haloferax volcanii*, rod and disk states are growth-condition-dependent and genetically separable, with RdfA, DdfA, volactin, and CetZ1 implicated in shape determination (brown2024mindproteinsregulate pages 1-2, schiller2024identificationofstructural pages 1-2).

### Boundary cases

Do **not** treat the following as synonymous with cell shape:

1. **Cell size**—length, width, area, or volume may change without a categorical geometry change.
2. **Cell arrangement**—chains, clusters, diplococci, or biofilm architecture describe relations among cells.
3. **Division and separation**—filamentation caused by failed septation is a shape phenotype only when the individual-cell geometry endpoint is explicitly measured; otherwise it is primarily a division phenotype.
4. **Growth mode**—lateral, polar, or zonal PG insertion is an upstream process, not the trait itself.
5. **Polarity, motility, branching, stalks, and appendages**—curate as shape only where they alter the cell body or a source explicitly links them to morphogenesis.
6. **Spheroplast, protoplast, and L-form states**—these are induced envelope-deficient states and should carry assay/environment qualifiers. The *Vibrio cholerae* recovery study is useful mechanistically but is not evidence for unperturbed vegetative morphogenesis (goudin2023recoveryofvibrio pages 1-2).
7. **Pleomorphism**—a distribution or capacity to transition among shapes; it should not be collapsed into any one terminal shape.

## Current mechanistic model

The best-supported bacterial core is:

**lipid II → PG polymerization and peptide cross-linking → patterned PG insertion/remodeling → sacculus mechanical anisotropy → cell shape.**

RodA–PBP2 provides coupled glycan polymerization/transpeptidation in the elongasome, while MreB aligns with membrane curvature and orients circumferential synthesis. Divisome synthesis, centered on FtsW–FtsI and FtsZ organization, creates septa and new poles. PG hydrolases permit controlled expansion by cleaving existing bonds; unbalanced synthesis or hydrolysis produces deformation or lysis (teeseling2017determinantsofbacterial pages 3-4, hussain2018mrebfilamentsalign pages 1-2, shlosman2023allostericactivationof pages 1-2).

This model is not universal. MreB-less Actinomycetota and Rhizobiales can elongate from poles or tips using DivIVA/polarisome or bactofilin-associated machinery. Specialized cytoskeletal or envelope-patterning systems superimpose curvature or helicity on a basal rod-building program (richter2023interactingbactofilinsimpact pages 1-2, sen2024adispensablesepiva pages 1-2, pohl2024anoutermembrane pages 1-2).

## Candidate nodes grouped by type

### Trait and morphology nodes

- **cell shape — METPO:1000666**
- rod shape
- spherical/coccoid shape
- curved or vibrioid shape
- helical shape
- filamentous/hyphal shape
- branched morphology
- disk/polyhedral shape
- pleomorphic shape transition

Child-shape CURIEs should be added only after lookup in METPO or another approved phenotype ontology; labels are safer than guessed identifiers.

### Chemicals and envelope structures

- **peptidoglycan — CHEBI:8005**
- **potassium cation — CHEBI:29103**
- lipid II — grounding should be verified against ChEBI before curation
- glycan chains and peptide cross-links
- cytoplasmic/plasma membrane
- outer membrane
- periplasm
- archaeal S-layer

### Processes and modules

- peptidoglycan biosynthesis — **GO:0009252**
- cell-wall organization or biogenesis — **GO:0071555**
- cell morphogenesis — **GO:0000902**
- cell division — **GO:0051301**
- elongasome/Rod complex
- divisome
- lateral cell-wall growth
- polar or apical growth
- PG polymerization, transpeptidation, hydrolysis, and repair
- MreB filament assembly/disassembly
- membrane-curvature sensing
- osmotic-stress response

The broad GO terms are appropriate anchors, but finer process IDs should be ontology-verified before YAML insertion.

### Genes, proteins, and complexes

**Core bacterial rod system**

- MreB; MreC; MreD; RodZ
- RodA/MrdB; PBP2/MrdA
- class-A PBPs, including PBP1a/PBP1b
- FtsZ; FtsW; FtsI/PBP3; FtsQLB; FtsN
- PG synthases and hydrolases/endopeptidases

**Specialized bacterial morphogenesis**

- crescentin/CreS in *Caulobacter crescentus*
- Por39, Por41, and PapS in *Rhodospirillum rubrum*
- bactofilins in *Rhodomicrobium vannielii* and other taxa
- DivIVA/Wag31, Scy, FilP, SepIVA in Actinomycetota
- PBP2SAL and PBP3SAL in *Salmonella*

**Archaeal systems**

- CetZ1
- MinD2 and MinD4
- RdfA and DdfA
- volactin
- LonB, ArtA, PssA, and PssD as possible upstream regulators requiring source-specific qualification

Gene/product identifiers should be taxon-specific UniProt or locus-tag CURIEs, not generic symbols. The evidence reviewed here does not support assigning a single UniProt identifier across species.

### Environmental and experimental factors

- acidic versus neutral pH
- osmotic upshift
- intracellular potassium influx
- nutrient-rich versus nutrient-poor medium
- growth phase
- cell-wall-targeting antibiotics
- MreB inhibitors such as A22
- osmotic stabilization
- induced spheroplast/protoplast state
- gene deletion, depletion, or catalytic-site mutation
- fluorescent D-amino-acid PG labeling, live-cell microscopy, cryo-EM, single-molecule FRET, and proteomics

## Candidate causal edges

The following table separates direct perturbational evidence from upstream or interpretive edges. Taxon and assay qualifiers are essential.

| subject | predicate | object | taxon/context | supporting snippet (short direct quotation) | DOI/date | evidence strength and curation note |
|---|---|---|---|---|---|---|
| peptidoglycan (PG) cell wall | determines | cell shape | broad bacteria | “The peptidoglycan (PG) cell wall protects bacteria against osmotic lysis and determines cell shape” (shlosman2023allostericactivationof pages 1-2) | 10.1038/s41467-023-39037-9; 2023-06 | **Strong, broad.** Good high-level trait edge for bacteria; endpoint is shape, not specific geometry. |
| RodA–PBP2 structural opening | couples activation of | PG polymerization and crosslinking | bacterial elongation complex | “Structural opening couples the activation of polymerization and crosslinking and is essential in vivo.” (shlosman2023allostericactivationof pages 1-2) | 10.1038/s41467-023-39037-9; 2023-06 | **Strong mechanistic.** Direct biochemical mechanism upstream of shape via elongasome function; curate as process-level edge rather than direct shape edge. |
| RodA–PBP2 PG synthase | responsible for | bacterial elongation | broad rod-shaped bacteria | “an essential PG synthase (RodA-PBP2) responsible for bacterial elongation” (shlosman2023allostericactivationof pages 1-2) | 10.1038/s41467-023-39037-9; 2023-06 | **Strong.** Supports elongation module as core morphogenetic entity. |
| MreB filament alignment to greatest principal membrane curvature | orients | cell wall synthesis | *Bacillus subtilis* / rod regeneration | “MreB orients along the greatest principal membrane curvature” and “MreB filament alignment to shape-reinforcing peptidoglycan synthesis” (hussain2018mrebfilamentsalign pages 1-2) | 10.7554/eLife.32471; 2018-02-22 | **Strong.** Foundational geometry-sensing mechanism; broadly relevant to rod shape but experimentally shown in *B. subtilis*. |
| coupling of MreB filament alignment to PG synthesis | allows establishment and maintenance of | rod shape | *Bacillus subtilis* | “creates a locally-acting, self-organizing mechanism allowing the rapid establishment and stable maintenance of emergent rod shape” (hussain2018mrebfilamentsalign pages 1-2) | 10.7554/eLife.32471; 2018-02-22 | **Strong.** Direct rod-shape edge. |
| acidic pH | promotes assembly of | PBP2SAL-directed elongasome | *Salmonella enterica* serovar Typhimurium | “The PBP2-elongasome responds to neutral pH whereas that directed by PBP2SAL assembles in acidic conditions.” (castanheira2023evidenceoftwo pages 1-2) | 10.1038/s42003-023-05308-w; 2023-09 | **Strong but taxon-specific.** Curate with *Salmonella* context. |
| PBP2SAL-directed elongasome | contributes to preservation of | rod shape | *Salmonella* in acidic host-like conditions | “two elongasomes that generate (rod) shape in the same bacterium” and “bacteria growing in PCN pH 4.6 produce essentially PBP2SAL/PBP3SAL” with “genuine rod shape” (castanheira2023evidenceoftwo pages 1-2) | 10.1038/s42003-023-05308-w; 2023-09 | **Strong but taxon/environment-specific.** Links alternative elongasome to rod morphology under acidic conditions. |
| loss of PBP2 at neutral pH | causes | giant spherical cells / loss of rod shape | *Salmonella* ΔmrdA at neutral pH | “ΔmrdA cells appear at neutral pH as giant spherical cells” and “The loss of rod shape” (castanheira2023evidenceoftwo pages 1-2) | 10.1038/s42003-023-05308-w; 2023-09 | **Strong perturbational.** Useful negative edge showing requirement of canonical elongasome at neutral pH. |
| osmotic upshift | causes | MreB filament disassembly | *Bacillus subtilis* | “In response to osmotic upshift, MreB molecules were released from filaments” (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309; 2024-06-27 | **Strong.** Environmental regulation edge. |
| potassium influx after osmotic shock | promotes | MreB filament disassembly | *Bacillus subtilis* | “mutant strains that prevent efficient potassium influx into cells following osmotic shock show a failure to disassemble MreB filaments” (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309; 2024-06-27 | **Strong.** Direct ion-mediated mechanism. |
| MreB filament disassembly | is associated with | slowed cell wall extension | *Bacillus subtilis* under osmotic stress | “failure to disassemble MreB filaments, accompanied by less perturbed cell wall extension than is observed in wild type cells” and disassembly “may ensure slowed-down cell wall extension” (dersch2024adaptationofbacillus pages 1-2) | 10.3390/microorganisms12071309; 2024-06-27 | **Moderate-strong.** Mechanistic interpretation is partly inferential; mark as stress-response context. |
| Por39/Por41 helical ribbon + PapS | promotes | cell curvature | *Rhodospirillum rubrum* | “Por39 and Por41 form a helical ribbon-like structure at the outer curve of the cell that recruits… PapS, with PapS inactivation… resulting in cell straightening.” (pohl2024anoutermembrane pages 1-2) | 10.1038/s41467-024-51790-z; 2024-09 | **Strong.** Direct specialized curvature module. |
| porin–PapS assemblies | bias | cell growth towards outer curve | *R. rubrum* | “porin-PapS assemblies act as molecular cages that entrap the cell elongation machinery, thus biasing cell growth towards the outer curve” (pohl2024anoutermembrane pages 1-2) | 10.1038/s41467-024-51790-z; 2024-09 | **Strong.** Good intermediate edge from envelope patterning to curvature. |
| crescentin | is required for | cell curvature | *Caulobacter crescentus* | “the loss of cell curvature associated with impaired crescentin function” (cabeen2011thedomainorganization pages 1-2) | 10.1002/cm.20505; 2011-03 | **Strong but taxon-specific.** Foundational curvature determinant. |
| crescentin structure along inner curvature | mechanically constrains | cell wall synthesis to impart curvature | *C. crescentus* | “mechanically constrains cell wall synthesis to impart cell curvature” (cabeen2011thedomainorganization pages 1-2) | 10.1002/cm.20505; 2011-03 | **Moderate.** Mechanistic model stated in discussion/background; useful but partly interpretive. |
| bactofilins | impact | cell shape / proper hyphae formation | *Rhodomicrobium vannielii* (MreB-less) | “bactofilins are associated with the hyphal growth zones and… one of them is essential to form proper hyphae” (richter2023interactingbactofilinsimpact pages 1-2) | 10.1371/journal.pgen.1010788; 2023-05 | **Strong but taxon-specific.** Good edge for non-MreB tip-growing bacteria. |
| aPBPs | drive | periplasm elimination during de novo morphogenesis | *Vibrio cholerae* spheroplast recovery | “Periplasm elimination was driven by bifunctional peptidoglycan synthases involved in cell-wall maintenance, the aPBPs.” (goudin2023recoveryofvibrio pages 1-2) | 10.1371/journal.pone.0293276; 2023-10-26 | **Strong but assay-specific.** Relevant for shape recovery from spheroplast state, not normal growth. |
| PBP2 | drives | elongation and branching during rod-shape recovery | *Vibrio cholerae* spheroplast recovery | “Elongation and branching relied on the MreB-associated monofunctional peptidoglycan synthase PBP2.” (goudin2023recoveryofvibrio pages 1-2) | 10.1371/journal.pone.0293276; 2023-10-26 | **Strong but assay-specific.** Supports PBP2 as direct shape-recovery determinant. |
| DivIVA | is necessary for | polar growth | Actinomycetota / *Streptomyces* context | “DivIVA, a protein necessary for polar growth” and “In Actinomycetota, divIVA orthologues are essential for polar growth.” (sen2024adispensablesepiva pages 1-2) | 10.1186/s12866-024-03625-6; 2024-11 | **Strong for polar growth, indirect for shape.** Use upstream edge unless morphology phenotype is explicit in species-specific sources. |
| DivIVA-dependent polar growth | maintains | rod or filamentous morphology | Actinomycetota | “They grow as rods or filamentous cells by building the cell wall sacculus at the cell poles, and this polar mode of growth is dependent on the cell polarity determinant protein DivIVA.” (sen2024adispensablesepiva pages 1-2) | 10.1186/s12866-024-03625-6; 2024-11 | **Moderate.** Review-style background in primary paper; broad but should be marked indirect. |
| RdfA | is required for formation of | rods | *Haloferax volcanii* | “rod-determining factor A (RdfA)… [is] required for the formation of rods” (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0; 2024-02 | **Strong.** Direct archaeal shape determinant. |
| DdfA | is required for formation of | disks | *Haloferax volcanii* | “disk-determining factor A (DdfA) [is] required for the formation of… disks” (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0; 2024-02 | **Strong.** Direct archaeal shape determinant. |
| volactin | plays a role in | disk-shape morphogenesis | *Haloferax volcanii* | “an actin homolog that plays a role in disk-shape morphogenesis, which we named volactin” (schiller2024identificationofstructural pages 1-2) | 10.1038/s41467-024-45196-0; 2024-02 | **Strong.** Direct archaeal cytoskeletal morphogenesis edge. |
| CetZ1 | contributes to development of | rod shape | *Haloferax volcanii* | “CetZ1 contributes to the development of rod shape and motility” and “CetZ1… is necessary for rod-shape development” (brown2024mindproteinsregulate pages 1-2) | 10.3389/fmicb.2024.1474697; 2024-11-22 | **Strong.** Direct archaeal rod-shape factor. |
| MinD2 | regulates localization of | CetZ1 | *Haloferax volcanii* | “minD2 has a strong influence on… the localization of CetZ1” and “Knockout of the minD2 gene… inhibited the localization of CetZ1-mTq2 at the cell poles.” (brown2024mindproteinsregulate pages 1-2) | 10.3389/fmicb.2024.1474697; 2024-11-22 | **Strong upstream but indirect for shape.** Best curated as localization/control edge feeding into CetZ1-mediated rod shape. |
| MinD proteins | position machinery contributing to | rod shape formation | *Haloferax volcanii* | “distinct roles for CetZ1 in rod shape formation… that are positioned through the action of the MinD proteins” (brown2024mindproteinsregulate pages 1-2) | 10.3389/fmicb.2024.1474697; 2024-11-22 | **Moderate, indirect.** Good hypothesis-supported upstream edge; mark as indirect. |


*Table: This table compiles curation-ready candidate causal edges for microbial cell shape from the gathered evidence, emphasizing direct mechanistic statements, perturbation phenotypes, and environmental dependencies. It is useful as a starting point for selecting nodes and edges for TraitMech while flagging taxon-specific or indirect claims.*

## Priority graph architecture for `cell_shape.yaml`

A compact first revision should preserve the existing PG–cytoskeleton core while adding context-specific branches:

1. **Bacterial basal branch:** PG wall → cell shape.
2. **Rod branch:** MreB curvature alignment → Rod-complex orientation → spatially patterned PG synthesis → rod shape.
3. **Enzymatic activation branch:** RodA–PBP2 opening → coupled polymerization/cross-linking → elongation.
4. **Division branch:** FtsZ/divisome → septal PG synthesis → new-pole geometry; do not equate this automatically with overall shape.
5. **Polar-growth branch:** DivIVA/polarisome → polar PG insertion → rod/hyphal morphology in MreB-lacking Actinomycetota.
6. **Special-shape branches:** crescentin → *Caulobacter* curvature; Por39/Por41/PapS → outer-curve-biased growth → *R. rubrum* curvature; bactofilins → local growth-zone control → hyphal/complex morphology.
7. **Environmental branch:** acidic pH → PBP2SAL elongasome assembly → rod-shape maintenance in *Salmonella*; osmotic upshift → potassium influx → MreB disassembly → reduced wall extension in *B. subtilis*.
8. **Archaeal branch:** CetZ1/RdfA → rods; DdfA/volactin → disks; MinD2/MinD4 → CetZ1 localization. This branch must not pass through bacterial PG unless a specific archaeon actually possesses the relevant wall chemistry.

## Recent developments, 2023–2024

### Coupled activation of elongasome synthesis

Shlosman et al. used single-molecule FRET and cryo-EM to show that RodA–PBP2 exchanges between closed and open conformations. Opening couples glycan polymerization and peptide cross-linking and is essential in vivo, refining the graph from “elongasome makes PG” to a regulatory conformational mechanism (published June 2023; DOI [10.1038/s41467-023-39037-9](https://doi.org/10.1038/s41467-023-39037-9)) (shlosman2023allostericactivationof pages 1-2).

### Environment-specific alternative elongasomes

*Salmonella Typhimurium* contains independently regulated PBP2- and PBP2SAL-directed elongasomes. PBP2 operates at neutral pH, whereas PBP2SAL assembles and functions under acidic conditions. Deleting canonical PBP2 at neutral pH generated giant spherical cells and reduced viability by approximately five logs in rich LB and two to three logs in nutrient-poor PCN medium; at pH 4.6, the alternative machinery could support genuine rods (published September 2023; DOI [10.1038/s42003-023-05308-w](https://doi.org/10.1038/s42003-023-05308-w)) (castanheira2023evidenceoftwo pages 1-2).

### Ion-mediated remodeling under osmotic stress

In *B. subtilis*, osmotic upshift increases freely diffusive MreB and RodZ and disorders PG synthesis. Potassium-transporter mutants fail to disassemble MreB efficiently, indicating that early K⁺ influx physically couples osmoadaptation to cytoskeletal remodeling. The authors interpret MreB disassembly as a mechanism for slowing wall extension during adaptation; that last link should be marked partly inferential (published 27 June 2024; DOI [10.3390/microorganisms12071309](https://doi.org/10.3390/microorganisms12071309)) (dersch2024adaptationofbacillus pages 15-17, dersch2024adaptationofbacillus pages 1-2).

### Outer-membrane control of intracellular elongation

Pöhl et al. identified a mechanistically distinct curvature module in *R. rubrum*: Por39/Por41 form a helical outer-membrane ribbon, recruit PG-binding PapS, and cage elongasome motion so growth is biased toward the outer curve. PapS inactivation, porin delocalization, or disruption of the interface straightens cells (published September 2024; DOI [10.1038/s41467-024-51790-z](https://doi.org/10.1038/s41467-024-51790-z)) (pohl2024anoutermembrane pages 1-2).

### Expanded archaeal cell-shape machinery

A 2024 genetics/proteomics/live-imaging study established that RdfA and DdfA are required for rods and disks, respectively, and identified dynamic actin homolog volactin as a disk-morphogenesis factor in *H. volcanii* (published February 2024; DOI [10.1038/s41467-024-45196-0](https://doi.org/10.1038/s41467-024-45196-0)) (schiller2024identificationofstructural pages 1-2). A second study showed that MinD2 strongly controls CetZ1 localization, although early-log minD2/4 mutants still formed rods; thus MinD→shape is indirect, whereas CetZ1→rod development is stronger (published 22 November 2024; DOI [10.3389/fmicb.2024.1474697](https://doi.org/10.3389/fmicb.2024.1474697)) (brown2024mindproteinsregulate pages 1-2).

## Applications and expert interpretation

Cell-shape machinery is an established antimicrobial target space because animal cells lack PG, while PBPs, SEDS proteins, and divisome components are essential or conditionally essential in many pathogens. The RodA–PBP2 and FtsW–FtsI activation mechanisms provide structural frameworks for inhibitor development, but broad-spectrum claims must account for alternative synthases and taxon-specific bypasses (shlosman2023allostericactivationof pages 1-2, castanheira2023evidenceoftwo pages 1-2).

Morphology is also a useful screening phenotype. Fluorescent D-amino-acid labeling, single-cell microscopy, imaging flow cytometry, and CRISPR perturbation can connect genetic or chemical interventions to spatial PG synthesis and geometry. Spheroplast recovery offers an experimentally tractable assay for de novo morphogenesis, although it is highly artificial and must not be generalized uncritically (goudin2023recoveryofvibrio pages 1-2).

From an ecological perspective, shape influences nutrient capture, motility through viscous media, surface colonization, host interaction, and predation. These are plausible selective explanations, not direct molecular edges to **METPO:1000666**, unless experiments demonstrate that a particular environmental factor changes shape through a defined mechanism (teeseling2017determinantsofbacterial pages 3-4, pohl2024anoutermembrane pages 1-2).

## Curation warnings

1. **Do not assert that MreB is universally required for rods.** Actinomycetes and several Rhizobiales are MreB-less and use polar/tip growth (richter2023interactingbactofilinsimpact pages 1-2, sen2024adispensablesepiva pages 1-2).
2. **Do not assert that PG determines all microbial shapes.** This is broadly valid for bacteria but not for many archaea or wall-less microbes.
3. **Keep taxon-specific curvature systems separate.** Crescentin, Por39/Por41/PapS, CrvA/CrvAB, and bactofilins are not interchangeable universal modules.
4. **Mark MinD→cell shape as indirect.** The 2024 *Haloferax* minD mutants altered CetZ1 localization but retained early-log rods (brown2024mindproteinsregulate pages 1-2).
5. **Mark potassium influx→shape as incomplete.** The demonstrated endpoint is MreB disassembly and altered wall extension under osmotic stress, not a fully quantified terminal geometry change (dersch2024adaptationofbacillus pages 1-2).
6. **Qualify DivIVA by lineage.** DivIVA is essential for polar growth in many Actinomycetota, but SepIVA deletion in *S. venezuelae* produced no detectable phenotype; SepIVA should not be curated as a necessary shape determinant there (sen2024adispensablesepiva pages 1-2).
7. **Qualify bactofilin paralogs individually.** One *R. vannielii* paralog was required for proper hyphae, while other paralogs or taxa can have different effects (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 2-4).
8. **Separate direct evidence from mechanistic models.** Crescentin-mediated mechanical constraint and stress-protective slowing after MreB disassembly are supported interpretations but less direct than knockout-induced straightening or loss of rods (dersch2024adaptationofbacillus pages 1-2, cabeen2011thedomainorganization pages 1-2).
9. **Avoid unverified CURIEs.** RdfA, DdfA, volactin, PapS, and species-specific bactofilins should remain label/locus-tag nodes until authoritative UniProt or genome identifiers are checked.
10. **Do not merge cell size with cell shape.** The *Salmonella* PBP2 deletion produced both spherical geometry and increased size; these should be represented as distinct phenotypic outcomes (castanheira2023evidenceoftwo pages 1-2).

## DOI-first bibliography

1. Shlosman I. et al. “Allosteric activation of cell wall synthesis during bacterial growth.” *Nature Communications* 14, 3439. Published June 2023. DOI: [10.1038/s41467-023-39037-9](https://doi.org/10.1038/s41467-023-39037-9) (shlosman2023allostericactivationof pages 1-2).
2. Castanheira S., García-del Portillo F. “Evidence of two differentially regulated elongasomes in Salmonella.” *Communications Biology* 6, 923. Published September 2023. DOI: [10.1038/s42003-023-05308-w](https://doi.org/10.1038/s42003-023-05308-w) (castanheira2023evidenceoftwo pages 1-2).
3. Richter P., Melzer B., Müller F.D. “Interacting bactofilins impact cell shape of the MreB-less multicellular Rhodomicrobium vannielii.” *PLOS Genetics* 19. Published May 2023. DOI: [10.1371/journal.pgen.1010788](https://doi.org/10.1371/journal.pgen.1010788) (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 2-4).
4. Goudin A. et al. “Recovery of Vibrio cholerae polarized cellular organization after exit from a non-proliferating spheroplast state.” *PLOS ONE* 18:e0293276. Published 26 October 2023. DOI: [10.1371/journal.pone.0293276](https://doi.org/10.1371/journal.pone.0293276) (goudin2023recoveryofvibrio pages 1-2).
5. Schiller H. et al. “Identification of structural and regulatory cell-shape determinants in Haloferax volcanii.” *Nature Communications* 15, 1414. Published February 2024. DOI: [10.1038/s41467-024-45196-0](https://doi.org/10.1038/s41467-024-45196-0) (schiller2024identificationofstructural pages 1-2).
6. Dersch S., Graumann P.L. “Adaptation of Bacillus subtilis MreB Filaments to Osmotic Stress Depends on Influx of Potassium Ions.” *Microorganisms* 12:1309. Published 27 June 2024. DOI: [10.3390/microorganisms12071309](https://doi.org/10.3390/microorganisms12071309) (dersch2024adaptationofbacillus pages 1-2).
7. Pöhl S. et al. “An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in Rhodospirillum rubrum.” *Nature Communications* 15, 7616. Published September 2024. DOI: [10.1038/s41467-024-51790-z](https://doi.org/10.1038/s41467-024-51790-z) (pohl2024anoutermembrane pages 1-2).
8. Brown H.J., Duggin I.G. “MinD proteins regulate CetZ1 localization in Haloferax volcanii.” *Frontiers in Microbiology* 15:1474697. Published 22 November 2024. DOI: [10.3389/fmicb.2024.1474697](https://doi.org/10.3389/fmicb.2024.1474697) (brown2024mindproteinsregulate pages 1-2).
9. Sen B.C. et al. “A dispensable SepIVA orthologue in Streptomyces venezuelae is associated with polar growth and not cell division.” *BMC Microbiology* 24:481. Published November 2024. DOI: [10.1186/s12866-024-03625-6](https://doi.org/10.1186/s12866-024-03625-6) (sen2024adispensablesepiva pages 1-2).
10. Hussain S. et al. “MreB filaments align along greatest principal membrane curvature to orient cell wall synthesis.” *eLife* 7:e32471. Published 22 February 2018. DOI: [10.7554/eLife.32471](https://doi.org/10.7554/eLife.32471) (hussain2018mrebfilamentsalign pages 1-2).
11. van Teeseling M.C.F., de Pedro M.A., Cava F. “Determinants of Bacterial Morphology: From Fundamentals to Possibilities for Antimicrobial Targeting.” *Frontiers in Microbiology* 8:1264. Published July 2017. DOI: [10.3389/fmicb.2017.01264](https://doi.org/10.3389/fmicb.2017.01264) (teeseling2017determinantsofbacterial pages 3-4).
12. Kysela D.T. et al. “Diversity Takes Shape: Understanding the Mechanistic and Adaptive Basis of Bacterial Morphology.” *PLOS Biology* 14:e1002565. Published October 2016. DOI: [10.1371/journal.pbio.1002565](https://doi.org/10.1371/journal.pbio.1002565) (kysela2016diversitytakesshape pages 4-5).
13. Cabeen M.T., Herrmann H., Jacobs-Wagner C. “The domain organization of the bacterial intermediate filament-like protein crescentin is important for assembly and function.” *Cytoskeleton* 68:205–219. Published March 2011. DOI: [10.1002/cm.20505](https://doi.org/10.1002/cm.20505) (cabeen2011thedomainorganization pages 1-2).

References

1. (teeseling2017determinantsofbacterial pages 3-4): Muriel C. F. van Teeseling, Miguel A. de Pedro, and Felipe Cava. Determinants of bacterial morphology: from fundamentals to possibilities for antimicrobial targeting. Frontiers in Microbiology, Jul 2017. URL: https://doi.org/10.3389/fmicb.2017.01264, doi:10.3389/fmicb.2017.01264. This article has 225 citations and is from a peer-reviewed journal.

2. (kysela2016diversitytakesshape pages 4-5): David T. Kysela, Amelia M. Randich, Paul D. Caccamo, and Yves V. Brun. Diversity takes shape: understanding the mechanistic and adaptive basis of bacterial morphology. PLOS Biology, 14:e1002565, Oct 2016. URL: https://doi.org/10.1371/journal.pbio.1002565, doi:10.1371/journal.pbio.1002565. This article has 150 citations and is from a highest quality peer-reviewed journal.

3. (shlosman2023allostericactivationof pages 1-2): Irina Shlosman, Elayne M. Fivenson, Morgan S. A. Gilman, Tyler A. Sisley, Suzanne Walker, Thomas G. Bernhardt, Andrew C. Kruse, and Joseph J. Loparo. Allosteric activation of cell wall synthesis during bacterial growth. Nature Communications, Jun 2023. URL: https://doi.org/10.1038/s41467-023-39037-9, doi:10.1038/s41467-023-39037-9. This article has 47 citations and is from a highest quality peer-reviewed journal.

4. (brown2024mindproteinsregulate pages 1-2): Hannah J. Brown and Iain G. Duggin. Mind proteins regulate cetz1 localization in haloferax volcanii. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1474697, doi:10.3389/fmicb.2024.1474697. This article has 6 citations and is from a peer-reviewed journal.

5. (schiller2024identificationofstructural pages 1-2): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 37 citations and is from a highest quality peer-reviewed journal.

6. (goudin2023recoveryofvibrio pages 1-2): Anthony Goudin, Jean-Luc Ferat, Christophe Possoz, François-Xavier Barre, and Elisa Galli. Recovery of vibrio cholerae polarized cellular organization after exit from a non-proliferating spheroplast state. PLOS ONE, 18:e0293276, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293276, doi:10.1371/journal.pone.0293276. This article has 3 citations and is from a peer-reviewed journal.

7. (hussain2018mrebfilamentsalign pages 1-2): Saman Hussain, Carl N Wivagg, Piotr Szwedziak, Felix Wong, Kaitlin Schaefer, Thierry Izoré, Lars D Renner, Matthew J Holmes, Yingjie Sun, Alexandre W Bisson-Filho, Suzanne Walker, Ariel Amir, Jan Löwe, and Ethan C Garner. Mreb filaments align along greatest principal membrane curvature to orient cell wall synthesis. eLife, Feb 2018. URL: https://doi.org/10.7554/elife.32471, doi:10.7554/elife.32471. This article has 251 citations and is from a domain leading peer-reviewed journal.

8. (richter2023interactingbactofilinsimpact pages 1-2): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

9. (sen2024adispensablesepiva pages 1-2): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 6 citations and is from a peer-reviewed journal.

10. (pohl2024anoutermembrane pages 1-2): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 8 citations and is from a highest quality peer-reviewed journal.

11. (castanheira2023evidenceoftwo pages 1-2): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 16 citations and is from a peer-reviewed journal.

12. (dersch2024adaptationofbacillus pages 1-2): Simon Dersch and Peter L. Graumann. Adaptation of bacillus subtilis mreb filaments to osmotic stress depends on influx of potassium ions. Microorganisms, 12:1309, Jun 2024. URL: https://doi.org/10.3390/microorganisms12071309, doi:10.3390/microorganisms12071309. This article has 5 citations.

13. (cabeen2011thedomainorganization pages 1-2): Matthew T. Cabeen, Harald Herrmann, and Christine Jacobs‐Wagner. The domain organization of the bacterial intermediate filament‐like protein crescentin is important for assembly and function. Cytoskeleton, 68:205-219, Mar 2011. URL: https://doi.org/10.1002/cm.20505, doi:10.1002/cm.20505. This article has 31 citations and is from a peer-reviewed journal.

14. (dersch2024adaptationofbacillus pages 15-17): Simon Dersch and Peter L. Graumann. Adaptation of bacillus subtilis mreb filaments to osmotic stress depends on influx of potassium ions. Microorganisms, 12:1309, Jun 2024. URL: https://doi.org/10.3390/microorganisms12071309, doi:10.3390/microorganisms12071309. This article has 5 citations.

15. (richter2023interactingbactofilinsimpact pages 2-4): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.