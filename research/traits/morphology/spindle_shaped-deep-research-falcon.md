---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:39:08.386667'
end_time: '2026-06-18T09:58:16.574180'
duration_seconds: 1148.19
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: spindle shaped
  trait_identifier: METPO:1000692
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: spindle_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape that is widest at the middle and tapers symmetrically toward
    pointed poles.
  parent_traits: METPO:1000666
  synonyms: spindle
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports symmetric tapered shapes as a genetically
    determined outcome of polar wall patterning.)'
  causal_graph_summary: 'spindle_shaped_symmetric_taper: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** spindle shaped
- **METPO identifier:** METPO:1000692
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is widest at the middle and tapers symmetrically toward pointed poles.
- **Parent traits:** METPO:1000666
- **Synonyms:** spindle
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports symmetric tapered shapes as a genetically determined outcome of polar wall patterning.)
- **Existing causal graph summary:** spindle_shaped_symmetric_taper: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **spindle shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spindle_shaped.yaml`.

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
- **Trait label:** spindle shaped
- **METPO identifier:** METPO:1000692
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape that is widest at the middle and tapers symmetrically toward pointed poles.
- **Parent traits:** METPO:1000666
- **Synonyms:** spindle
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports symmetric tapered shapes as a genetically determined outcome of polar wall patterning.)
- **Existing causal graph summary:** spindle_shaped_symmetric_taper: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **spindle shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/spindle_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **spindle shaped** (METPO:1000692)

### Scope summary (trait meaning and boundaries)
**Trait definition (curation target).** *Spindle shaped* (syn. *spindle*, *fusiform*) refers to a microbial **cell shape** that is **widest at mid-cell and tapers symmetrically toward pointed poles** (METPO:1000692). This is a whole-cell morphology (not an appendage) and should be curated as a morphology-class phenotype node.

**What it is not (boundary cases).**
- **Rod-shaped** cells maintain near-constant diameter along most of the longitudinal axis; spindle-shaped cells require **systematic pole tapering** (operationally: the width profile decreases toward both poles rather than ending in hemispherical caps).
- **Vibrioid/crescent** shapes are primarily defined by **single-axis curvature** (bent rods) rather than symmetric tapering; in *Caulobacter*, the canonical description is “curved rod-shaped”/“vibrioid,” not fusiform (barrows2023synchronizedswarmersand pages 1-3).
- **Helical/spirochete** shapes include helicity/pitch and often skeletal roles for internal structures; these are geometrically distinct from fusiform tapering and should be separately curated.
- **Filamentous/hyphal** forms (e.g., long hyphae/stalks) can taper locally at tips but represent **appendage/extensional morphogenesis** and multicellular differentiation rather than the spindle outline of the main cell body (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 15-16).

**Current mechanistic understanding relevant to spindle shape.** Across bacteria, cell shape is ultimately constrained by the **peptidoglycan (PG) sacculus**, but **precise morphology is generated by where and when PG is inserted and cleaved** rather than by a “shape code” in the existing sacculus. A key principle is that **non-spherical shapes require spatially and temporally non-uniform insertion/remodeling** (teeseling2017determinantsofbacterial pages 3-4). For spindle-shaped cells specifically, this implies a mechanistic requirement for **pole-specific modulation** of PG growth/remodeling to produce tapered ends (in contrast to uniform lateral insertion that yields rods).

### Recent developments (prioritizing 2023–2024)
#### 1) A 2024 mechanistic module for localized envelope growth: **Bactofilin (BacA) + M23 endopeptidase (LmdC)**
A key recent advance is detailed experimental evidence that a **bactofilin cytoskeleton** controls **where** cell-wall synthesis/remodeling occurs, via cooperation with an **M23 family endopeptidase**.

- In the stalked budding alphaproteobacterium *Hyphomonas neptunium*, **BacA** is required for proper morphology; ΔbacA or ΔbacAD causes severe morphological abnormalities, quantified at **n=100 cells/strain**, while **doubling time is not strongly affected** (mean±SD across **three independent experiments**) (pohl2024adynamicbactofilin pages 3-4).
- **Fluorescent D-amino-acid (HADA) labeling** shows that in wild type, growth modes transition (dispersed → zonal at stalk base → bud growth), whereas in ΔbacAD cells the switch is abolished and labeling becomes **diffuse across the envelope**, indicating loss of confinement of new PG insertion (pohl2024adynamicbactofilin pages 4-6).
- The M23 peptidase **LmdC** is a **DD-endopeptidase** that cleaves crosslinks to **reduce PG cross-linkage**, and appears essential/tightly regulated in *H. neptunium*; inducible **CRISPRi knockdown of lmdC phenocopies ΔbacA** with many distorted/amorphous cells but near-normal growth (pohl2024adynamicbactofilin pages 13-15).
- **BacA binds LmdC’s N-terminal cytoplasmic peptide** (KD ~ **15 μM** by biolayer interferometry), providing a direct physical interaction suitable for a causal edge (pohl2024adynamicbactofilin pages 13-15).
- A model synthesis in the same work proposes that a **bactofilin polymer barrier** plus high positive curvature zones restrict **elongasome movement** into specialized compartments, thereby restricting PG biosynthesis and maintaining compartment geometry (pohl2024adynamicbactofilin pages 19-21).

Although the *Hyphomonas* phenotype is not labeled “fusiform/spindle-shaped” in the paper, it provides **high-confidence mechanistic entities and edges** for a TraitMech causal graph representing *symmetric tapering outcomes as an emergent property of localized envelope growth/remodeling*.

#### 2) 2023 evidence for bactofilins in tip-growing morphologies (comparative but relevant)
In the MreB-less, tip-growing alphaproteobacterium *Rhodomicrobium vannielii* (PLOS Genetics, 2023), bactofilins are presented as **accessory cytoskeletal elements** required for complex morphogenesis:
- The authors show bactofilins are **associated with hyphal growth zones** and that one is **essential to form proper hyphae** (richter2023interactingbactofilinsimpact pages 1-2). This is not spindle-shaped whole-cell morphology, but it supports a generalizable link between **bactofilin scaffolds** and **polar/tip-localized morphogenesis**, an important concept for taper formation.
- The discussion highlights that stalk PG can have more **3–3 crosslinks** due to elevated **LD-transpeptidase** activity, likely yielding a **stiffer** polar extension wall than the cell body; disorganized LD-TPase spatial control is proposed as a mechanism for deformed hyphae (richter2023interactingbactofilinsimpact pages 15-16). This is **taxon- and structure-specific** (stalk/hypha), but suggests candidate chemical-state nodes influencing taper.

#### 3) Environmental modulation and regulatory context (2024)
A 2024 Communications Biology study in *Caulobacter crescentus* shows that **cytoplasmic phosphate level** controls **morphological adaptation** under global phosphate limitation (billini2024thecytoplasmicphosphate pages 1-2). While not spindle-shape-specific, it supports the general curation concept that **environmental nutrient limitation can trigger morphology programs**, and provides a plausible upstream **environment→morphogenesis** edge class for future spindle-shape evidence.

### Current applications / real-world implementations
1. **Mechanistic inference for morphology traits in genome-annotated datasets.** The BacA–LmdC module provides a genome-grounded mechanism (bactofilin + M23 peptidase adjacency and interaction) that can be used to **prioritize candidate shape-determinant genes** in comparative genomics of morphologically complex bacteria (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 13-15).
2. **Microscopy-based assays for curating morphology mechanisms.** Fluorescent D-amino-acid labeling (e.g., HADA) gives a practical readout of **localized vs dispersed PG insertion**, which is directly relevant for discriminating mechanisms consistent with tapered-pole generation (localized remodeling) versus those that would yield rods or amorphous swelling (pohl2024adynamicbactofilin pages 4-6).

### Authoritative interpretations / expert analysis
- **Peptidoglycan insertion must be spatially patterned to create non-spherical shapes.** The morphogenesis review emphasizes that uniform insertion plus cleavage would yield homogeneous expansion; thus “to generate shapes other than a sphere, incorporation must occur at distinct rates in different locations and for defined periods of time” (teeseling2017determinantsofbacterial pages 3-4). This is the core theoretical justification for spindle-shape curation focusing on **pole-localized synthesis/remodeling**.
- **Bactofilins as spatial organizers of wall biosynthesis.** The 2024 eLife work explicitly interprets bactofilins as regulators of **spatiotemporal localization** of wall biosynthesis, with their absence yielding “unconstrained growth” and loss of confinement (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 4-6).

### Relevant statistics and quantitative data (from recent studies)
- **Morphology scoring:** ΔbacA / ΔbacAD abnormal morphology fractions were quantified with **n=100 cells per strain** (pohl2024adynamicbactofilin pages 3-4).
- **Growth impact:** Despite severe morphological defects, mutants “did not have any major defects on the doubling time,” quantified as mean±SD over **3 independent experiments** (pohl2024adynamicbactofilin pages 3-4).
- **Binding affinity:** BacA–LmdC cytoplasmic peptide interaction: **KD ~15 μM** (pohl2024adynamicbactofilin pages 13-15).
- **Enzymology:** LmdC treatment causes a “strong decrease” in dimeric muropeptides (Tetra–Tetra, Tetra–Penta), consistent with DD-endopeptidase activity reducing crosslinking; higher in vitro activity at **pH 5** (physiological relevance uncertain) (pohl2024adynamicbactofilin pages 13-15).

### Visual evidence (figures)
Microscopy and model panels in the Pöhl et al. study illustrate the morphological defects and spatial control of growth consistent with a localized-insertion mechanism (pohl2024adynamicbactofilin media d3fd9524, pohl2024adynamicbactofilin media bb17b39b, pohl2024adynamicbactofilin media e2d74463, pohl2024adynamicbactofilin media f4b7bd6f, pohl2024adynamicbactofilin media 26454f85).

---

## Candidate nodes (grouped by type)
| Node label | Node type | Suggested ontology grounding | Notes/relevance to spindle-shaped (tapered poles) trait |
|---|---|---|---|
| **Phenotype/assay** |  |  |  |
| spindle-shaped (fusiform) cell morphology | phenotype | METPO:1000692 | Target morphology: widest at mid-cell and tapering toward pointed poles; useful as the curated trait node for symmetric tapering morphology. Mechanistically likely arises from spatially restricted envelope growth/remodeling rather than uniform rod elongation (teeseling2017determinantsofbacterial pages 3-4, pohl2024adynamicbactofilin pages 1-2). |
| pointed/tapered cell poles | morphology subfeature |  | Boundary-defining subfeature separating fusiform cells from constant-diameter rods; candidate child/part node for graph structure. Local curvature-generating wall remodeling is a plausible proximate mechanism (pohl2024adynamicbactofilin pages 19-21, pohl2024adynamicbactofilin pages 13-15). |
| cell curvature / helicity | phenotype | PATO:0001591 | Important boundary-case node: distinguishes fusiform tapering from curved/helical shapes; in R. rubrum, BacA/LmdC modulate curvature rather than symmetric tapering per se, so should be treated as related but not equivalent evidence (pohl2024adynamicbactofilin pages 19-21, pohl2024adynamicbactofilin pages 13-15). |
| localized HADA incorporation | assay readout |  | Fluorescent D-amino-acid labeling reports active peptidoglycan insertion zones; useful assay node for inferring localized growth underlying tapered morphologies (pohl2024adynamicbactofilin pages 4-6). |
| diffuse HADA incorporation | assay readout |  | Indicates loss of growth-zone restriction; observed when bactofilin control is lost, supporting a mechanism in which localized insertion is required for defined morphologies instead of amorphous widening (pohl2024adynamicbactofilin pages 4-6). |
| **Cell wall processes** |  |  |  |
| peptidoglycan biosynthesis | biological process | GO:0009252 | Core shape-determining process in most bacteria; species-specific morphology depends on where and when PG is inserted (teeseling2017determinantsofbacterial pages 3-4, pohl2024adynamicbactofilin pages 1-2). |
| peptidoglycan remodeling | biological process | GO:0009253 | Remodeling/hydrolysis plus synthesis can create local curvature and tapering; key candidate mechanism for narrowing poles or stalk/bud transition zones (pohl2024adynamicbactofilin pages 19-21, pohl2024adynamicbactofilin pages 13-15). |
| localized peptidoglycan insertion | morphogenetic process |  | Non-uniform insertion is required to generate shapes other than spheres; likely essential for tapered poles/fusiform outlines (teeseling2017determinantsofbacterial pages 3-4, pohl2024adynamicbactofilin pages 4-6). |
| dispersed lateral peptidoglycan insertion | morphogenetic process |  | Canonical elongation mode for rods; useful contrast node because uniform dispersed insertion alone would not explain symmetric tapering (teeseling2017determinantsofbacterial pages 3-4, pohl2024adynamicbactofilin pages 1-2). |
| polar growth | growth mode | GO:0048762 | Polar or tip-focused growth is a strong candidate route to tapered/pointed morphologies in alphaproteobacteria and other prosthecate/tip-growing taxa (richter2023interactingbactofilinsimpact pages 15-16, pohl2024adynamicbactofilin pages 1-2). |
| growth-zone restriction / spatial confinement of cell wall synthesis | biological process |  | Central concept from H. neptunium: constraining biosynthesis to specific zones prevents widening and preserves specialized morphologies; conceptually relevant to maintaining taper (pohl2024adynamicbactofilin pages 4-6, pohl2024adynamicbactofilin pages 1-2). |
| local reduction in PG crosslinking | cell wall state/process |  | LmdC lowers cross-linkage locally; local softening/remodeling can alter curvature and shape transitions that could contribute to pointed poles (pohl2024adynamicbactofilin pages 13-15). |
| 3–3 peptidoglycan crosslinks | cell wall chemical feature |  | Enriched in stalk PG in related alphaproteobacterial systems and proposed to stiffen polar extensions; candidate wall-state node relevant to tapered outgrowths, but evidence for spindle cells is indirect/taxon-specific (richter2023interactingbactofilinsimpact pages 15-16). |
| DD-crosslink cleavage | enzymatic process |  | Specific PG-remodeling activity executed by LmdC; relevant if local cleavage facilitates narrowing/curving of the envelope (pohl2024adynamicbactofilin pages 13-15). |
| **Cytoskeleton/polarity proteins** |  |  |  |
| bactofilin | protein family / cytoskeletal element | InterPro:IPR007607 | Widely implicated accessory cytoskeleton for local shape modification; strong candidate superfamily node for fusiform-shape mechanisms (pohl2024adynamicbactofilin pages 1-2, richter2023interactingbactofilinsimpact pages 1-2). |
| BacA | protein |  | Best-supported specific morphogenetic node from H. neptunium; required to constrain growth zones and maintain defined morphology (pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 4-6). |
| BacD | protein |  | Secondary bactofilin homolog in H. neptunium; weaker direct evidence for morphology control than BacA, but may act as auxiliary factor (pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 4-6). |
| MreB | protein / actin-like cytoskeleton |  | Organizes elongasome-mediated lateral growth in many rods; useful contrast node because accessory systems must locally override or complement MreB-like growth to create non-rod shapes (richter2023interactingbactofilinsimpact pages 1-2, teeseling2017determinantsofbacterial pages 3-4, pohl2024adynamicbactofilin pages 1-2). |
| FtsZ | protein / tubulin-like cytoskeleton |  | Organizes divisome and new pole formation; included as a generic morphology determinant though not spindle-specific (pohl2024adynamicbactofilin pages 1-2). |
| RodZ | protein |  | Elongasome component mentioned in relation to growth-zone exclusion by bactofilin barriers; candidate mechanistic node for localization of elongation machinery (pohl2024adynamicbactofilin pages 19-21, richter2023interactingbactofilinsimpact pages 15-16). |
| polarity localization hub | cellular module |  | Proposed for tip-growing R. vannielii to sustain distant apical growth zones; candidate abstract node when no specific determinant is known (richter2023interactingbactofilinsimpact pages 15-16). |
| PhoR-PhoB system | signaling system |  | Not a direct shape generator, but phosphate-responsive regulation intersects morphology programs in Caulobacter and may indirectly affect shape-associated genes (billini2024thecytoplasmicphosphate pages 1-2). |
| **Enzymes—PG synthases/remodelers** |  |  |  |
| LmdC | enzyme / M23 endopeptidase | EC:3.4.-.- | Strong candidate causal node: directly interacts with BacA, is required for proper shape, and locally modulates PG crosslinking/curvature (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 13-15, pohl2024adynamicbactofilin pages 19-21). |
| M23 peptidase family | enzyme family |  | Conserved family linked genomically and functionally to bactofilins across morphologically complex bacteria; useful family-level node when species-specific ortholog is unknown (pohl2024adynamicbactofilin pages 1-2, pohl2023adynamicbactofilin pages 9-12). |
| penicillin-binding proteins (PBPs) | enzyme family |  | Canonical PG synthases/crosslinkers; background node for shape determination and potential partners or excluded machinery in taper-generating systems (teeseling2017determinantsofbacterial pages 3-4). |
| RodA / SEDS glycosyltransferase | enzyme |  | Core PG polymerization factor in elongation; included as generic node for wall synthesis machinery that may need local modulation to create fusiform shapes (teeseling2017determinantsofbacterial pages 3-4). |
| LD-transpeptidases | enzyme family |  | Candidate contributors to polar wall stiffening and specialized outgrowth geometry; evidence for tapered hypha/stalk morphology is indirect and taxon-specific (richter2023interactingbactofilinsimpact pages 15-16). |
| elongasome complex | protein complex / process module |  | Major lateral-growth machinery whose movement can be blocked by curvature/bactofilin barriers; confinement or exclusion is central to specialized shapes (pohl2024adynamicbactofilin pages 19-21, pohl2024adynamicbactofilin pages 1-2). |
| divisome | protein complex / process module |  | Generic morphology module for pole creation and cytokinesis; relevant as background mechanism but not specific enough for curation without direct taper evidence (pohl2024adynamicbactofilin pages 1-2). |
| **Environmental/experimental factors** |  |  |  |
| phosphate limitation / low cytoplasmic phosphate | environmental condition | CHEBI:43474 | In Caulobacter, low cytoplasmic phosphate controls morphological adaptation and upregulates bacA; potentially relevant upstream environmental driver for morphology programs, but not specifically spindle-shape-proven (billini2024thecytoplasmicphosphate pages 1-2). |
| copper induction/depletion system | experimental factor |  | Used to modulate bacA or CRISPRi constructs in H. neptunium; assay-specific, not a natural cause of spindle morphology (pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 13-15). |
| CRISPRi knockdown of lmdC | experimental perturbation |  | Experimental factor producing shape defects resembling bacA loss; useful evidence node, not a natural biological cause (pohl2024adynamicbactofilin pages 13-15). |
| pH 5 | experimental condition |  | LmdC activity was higher at pH 5 in vitro; could affect local PG remodeling, but physiological relevance remains uncertain (pohl2024adynamicbactofilin pages 13-15). |
| environmental cues | abstract upstream factor |  | Reviews note that bacterial morphology can shift with environmental cues; useful abstract node when modeling context dependence of shape programs (teeseling2017determinantsofbacterial pages 3-4, pohl2024adynamicbactofilin pages 1-2). |
| **Taxa/examples** |  |  |  |
| Hyphomonas neptunium | taxon | NCBITaxon:228405 | Strongest direct source for bactofilin/LmdC-mediated growth-zone control and complex morphogenesis relevant to tapered cellular extensions (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 4-6). |
| Rhodospirillum rubrum | taxon | NCBITaxon:1085 | Supports conserved BacA-LmdC module affecting curvature; valuable comparative evidence but more about helicity/curvature than fusiform symmetry (pohl2024adynamicbactofilin pages 19-21, pohl2024adynamicbactofilin pages 13-15). |
| Rhodomicrobium vannielii | taxon | NCBITaxon:1064 | Tip-growing, MreB-less alphaproteobacterium in which bactofilins mark hyphal growth zones; comparative evidence for polar/tapered morphogenesis modules (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 15-16). |
| Caulobacter crescentus | taxon | NCBITaxon:190650 | Classic curved/stalked alphaproteobacterial model for morphogenesis and phosphate-responsive stalk programs; useful comparative, not spindle-shaped exemplar (barrows2023synchronizedswarmersand pages 1-3, billini2024thecytoplasmicphosphate pages 1-2). |
| Asticcacaulis biprosthecum | taxon | NCBITaxon:118460 | Mentioned as related stalk morphogenesis system with pseudostalk phenotypes upon bactofilin loss; comparative evidence for conserved stalk/taper control (pohl2024adynamicbactofilin pages 19-21, pohl2024adynamicbactofilin pages 3-4). |


*Table: This table lists curation-ready candidate nodes for a causal graph of spindle-shaped (fusiform) microbial morphology. It groups phenotype, process, protein, enzyme, environmental, and taxon nodes most plausibly relevant to symmetric tapered cell shape, while flagging comparative or indirect nodes.*

---

## Candidate causal edges (evidence-backed triples)
| Subject node | Predicate | Object node | Evidence (first author year + DOI + URL) | Publication date | Supporting snippet | Notes/uncertainty/curation flags |
|---|---|---|---|---|---|---|
| BacA | required_for | spatial confinement of peptidoglycan biosynthesis to growth zones | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “These findings support the notion that the bactofilin cytoskeleton is required to limit cell wall biosynthesis to the different growth zones of *H. neptunium*.” (pohl2024adynamicbactofilin pages 4-6) | Strong, direct in *Hyphomonas neptunium*; morphology is complex budding/stalked rather than explicitly fusiform. |
| ΔbacAD / BacA loss | increases | diffuse HADA incorporation throughout cell envelope | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “all other cell types… only displayed diffuse fluorescence, which points to uncontrolled growth by dispersed incorporation of new peptidoglycan throughout the entire cell envelope.” (pohl2024adynamicbactofilin pages 4-6) | Strong assay-backed edge; useful proxy for loss of localized taper-generating growth. |
| BacA | restricts | stalk cell wall growth / polar growth zone | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “BacA appears to be required to maintain the polar growth zone at the stalk base, with its absence leading to unconstrained growth of the stalk cell wall.” (pohl2024adynamicbactofilin pages 4-6) | Strong, direct; supports graph edge from cytoskeleton to localized wall growth. |
| BacA | localizes_to | stalk base and bud neck | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “bactofilin polymers localize dynamically to the stalk base and the bud neck” (pohl2024adynamicbactofilin pages 1-2) | Strong localization edge; taxon-specific. |
| BacA | interacts_with | LmdC | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “BacA interacts with the LmdC peptide with an apparent equilibrium dissociation constant (KD) of ~15 µM.” (pohl2024adynamicbactofilin pages 13-15) | Strong biochemical interaction; direct in vitro binding. |
| LmdC | decreases | peptidoglycan cross-linkage | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “LmdC is a DD-endopeptidase… thereby reducing the degree of cross-linkage within the peptidoglycan layer.” (pohl2024adynamicbactofilin pages 13-15) | Strong enzymatic edge; mechanism likely portable across taxa with homologs. |
| LmdC | required_for | proper cell shape | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “the *H. neptunium* M23 peptidase homolog LmdC… is required for proper cell shape in vivo.” (pohl2024adynamicbactofilin pages 1-2) | Strong, though phrased from abstract summary rather than single experiment panel. |
| CRISPRi knockdown of lmdC | increases | distorted/amorphous cell morphology | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “the block of *lmdC* expression led to cell shape defects very similar to those observed for the ΔbacA mutant, as reflected by a large proportion of distorted and amorphous cells” (pohl2024adynamicbactofilin pages 13-15) | Strong perturbation evidence; assay-specific experimental edge. |
| BacA | recruits | LmdC to inner curve of cell | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “BacARs (yellow) recruits LmdCRs (red) to the inner curve of the cell.” (pohl2024adynamicbactofilin pages 19-21) | Strong in *Rhodospirillum rubrum*; comparative/curvature evidence, not direct spindle-shape evidence. |
| LmdC hydrolytic activity | stimulates | local peptidoglycan biosynthesis at inner curve | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “The hydrolytic activity of LmdC ultimately stimulates the insertion of new peptidoglycan at the inner curve of the cell” (pohl2024adynamicbactofilin pages 19-21) | Direct for curvature model in *R. rubrum*; indirect for symmetric tapering/fusiform morphology. |
| BacA/bactofilin polymer | prevents_movement_of | elongasome complexes into stalk | Pöhl 2024, DOI:10.7554/eLife.86577, https://doi.org/10.7554/eLife.86577 | 2024-01-31 | “the physical barrier constituted by the bactofilin polymer prevent[s] the movement of elongasome complexes from the mother cell body into the stalk” (pohl2024adynamicbactofilin pages 19-21) | Mechanistic model figure-text; strong but partially inferential. |
| localized peptidoglycan insertion | required_for | non-spherical / differentiated morphology | van Teeseling 2017, DOI:10.3389/fmicb.2017.01264, https://doi.org/10.3389/fmicb.2017.01264 | 2017-07 | “To generate shapes other than a sphere, incorporation must occur at distinct rates in different locations and for defined periods of time.” (teeseling2017determinantsofbacterial pages 3-4) | Broad mechanistic principle; curate as general background edge, not spindle-specific. |
| hypha/stalk-specific 3–3 PG crosslinks | increases | wall stiffness of polar extension | Richter 2023, DOI:10.1371/journal.pgen.1010788, https://doi.org/10.1371/journal.pgen.1010788 | 2023-05-31 | “a higher proportion of 3–3 crosslinks due to elevated LD-Transpeptidase activity… likely cause a stiffer stalk wall compared to the cell body” (richter2023interactingbactofilinsimpact pages 15-16) | Indirect and taxon-specific; relevant to tapered extensions, uncertain for spindle cells. |
| BacARvan | required_for | proper hypha morphology | Richter 2023, DOI:10.1371/journal.pgen.1010788, https://doi.org/10.1371/journal.pgen.1010788 | 2023-05-31 | “the R. vannielii bactofilins are associated with the hyphal growth zones and… one of them is essential to form proper hyphae.” (richter2023interactingbactofilinsimpact pages 1-2) | Comparative tip-growth evidence only; not direct support for spindle-shaped whole-cell morphology. |


*Table: This table compiles curation-ready causal triples linking bactofilins, LmdC, and localized peptidoglycan remodeling to microbial morphogenesis. It emphasizes direct experimental edges from 2023-2024 studies while flagging broader or taxon-specific inferences that should be curated cautiously.*

---

## Warnings / claims not yet ready for curation into a **spindle-shaped** TraitMech graph
1. **Direct exemplars of whole-cell spindle (fusiform) morphology are limited in the retrieved 2023–2024 mechanistic corpus.** The strongest mechanistic studies here focus on **stalk/bud morphogenesis** (*H. neptunium*) or **hypha/tip growth** (*R. vannielii*) or **curvature modulation** (*R. rubrum*), not explicitly on fusiform whole-cell outlines (pohl2024adynamicbactofilin pages 4-6, richter2023interactingbactofilinsimpact pages 1-2, pohl2024adynamicbactofilin pages 19-21). These are still valuable because they provide **grounded entities (BacA, LmdC, PG insertion restriction)** likely reusable in spindle-shape graphs, but edges should be marked as **inferred-to-fusiform** unless corroborated in a fusiform species.
2. **3–3 crosslink / LD-transpeptidase edges are indirect for spindle shape.** The 3–3 crosslink argument is specifically about stalk PG stiffness and is discussed as speculative for *R. vannielii* hypha deformation; curate as **uncertain/taxon-specific** (richter2023interactingbactofilinsimpact pages 15-16).
3. **Environmental edges (phosphate limitation) are upstream and not spindle-specific.** The phosphate study supports a general “environment→morphological adaptation” framing; do not curate it as a spindle-shape determinant without trait-specific evidence (billini2024thecytoplasmicphosphate pages 1-2).

---

## DOI-first bibliography (with URLs and publication dates where available)
1. **Pöhl S, Osorio-Valeriano M, Cserti E, et al.** *A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.* **eLife**. Version of Record published **2024-01-31**. DOI: **10.7554/eLife.86577**. URL: https://doi.org/10.7554/eLife.86577 (pohl2024adynamicbactofilin pages 1-2, pohl2024adynamicbactofilin pages 3-4, pohl2024adynamicbactofilin pages 4-6, pohl2024adynamicbactofilin pages 13-15, pohl2024adynamicbactofilin pages 19-21)
2. **Richter P, Melzer B, Müller FD.** *Interacting bactofilins impact cell shape of the MreB-less multicellular Rhodomicrobium vannielii.* **PLOS Genetics**. Published **2023-05-31**. DOI: **10.1371/journal.pgen.1010788**. URL: https://doi.org/10.1371/journal.pgen.1010788 (richter2023interactingbactofilinsimpact pages 1-2, richter2023interactingbactofilinsimpact pages 15-16)
3. **Barrows JM, Goley ED.** *Synchronized Swarmers and Sticky Stalks: Caulobacter crescentus as a Model for Bacterial Cell Biology.* **Journal of Bacteriology**. Published **2023-01-30**. DOI: **10.1128/jb.00384-22**. URL: https://doi.org/10.1128/jb.00384-22 (barrows2023synchronizedswarmersand pages 1-3)
4. **Billini M, Hoffmann T, Kühn J, Bremer E, Thanbichler M.** *The cytoplasmic phosphate level has a central regulatory role in the phosphate starvation response of Caulobacter crescentus.* **Communications Biology**. Published **2024** (article 7:772). DOI: **10.1038/s42003-024-06469-y**. URL: https://doi.org/10.1038/s42003-024-06469-y (billini2024thecytoplasmicphosphate pages 1-2)
5. **van Teeseling MCF, de Pedro MA, Cava F.** *Determinants of Bacterial Morphology: From Fundamentals to Possibilities for Antimicrobial Targeting.* **Frontiers in Microbiology**. Published **2017-07**. DOI: **10.3389/fmicb.2017.01264**. URL: https://doi.org/10.3389/fmicb.2017.01264 (teeseling2017determinantsofbacterial pages 3-4)


References

1. (barrows2023synchronizedswarmersand pages 1-3): Jordan M. Barrows and Erin D. Goley. Synchronized swarmers and sticky stalks: caulobacter crescentus as a model for bacterial cell biology. Journal of Bacteriology, Feb 2023. URL: https://doi.org/10.1128/jb.00384-22, doi:10.1128/jb.00384-22. This article has 59 citations and is from a peer-reviewed journal.

2. (richter2023interactingbactofilinsimpact pages 1-2): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (richter2023interactingbactofilinsimpact pages 15-16): Pia Richter, Brigitte Melzer, and Frank D. Müller. Interacting bactofilins impact cell shape of the mreb-less multicellular rhodomicrobium vannielii. PLOS Genetics, May 2023. URL: https://doi.org/10.1371/journal.pgen.1010788, doi:10.1371/journal.pgen.1010788. This article has 7 citations and is from a domain leading peer-reviewed journal.

4. (teeseling2017determinantsofbacterial pages 3-4): Muriel C. F. van Teeseling, Miguel A. de Pedro, and Felipe Cava. Determinants of bacterial morphology: from fundamentals to possibilities for antimicrobial targeting. Frontiers in Microbiology, Jul 2017. URL: https://doi.org/10.3389/fmicb.2017.01264, doi:10.3389/fmicb.2017.01264. This article has 224 citations and is from a peer-reviewed journal.

5. (pohl2024adynamicbactofilin pages 3-4): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

6. (pohl2024adynamicbactofilin pages 4-6): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

7. (pohl2024adynamicbactofilin pages 13-15): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

8. (pohl2024adynamicbactofilin pages 19-21): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

9. (billini2024thecytoplasmicphosphate pages 1-2): Maria Billini, Tamara Hoffmann, Juliane Kühn, Erhard Bremer, and Martin Thanbichler. The cytoplasmic phosphate level has a central regulatory role in the phosphate starvation response of caulobacter crescentus. Communications Biology, Jun 2024. URL: https://doi.org/10.1038/s42003-024-06469-y, doi:10.1038/s42003-024-06469-y. This article has 15 citations and is from a peer-reviewed journal.

10. (pohl2024adynamicbactofilin pages 1-2): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

11. (pohl2024adynamicbactofilin media d3fd9524): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

12. (pohl2024adynamicbactofilin media bb17b39b): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

13. (pohl2024adynamicbactofilin media e2d74463): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

14. (pohl2024adynamicbactofilin media f4b7bd6f): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

15. (pohl2024adynamicbactofilin media 26454f85): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

16. (pohl2023adynamicbactofilin pages 9-12): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. BioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.02.27.530196, doi:10.1101/2023.02.27.530196. This article has 0 citations.