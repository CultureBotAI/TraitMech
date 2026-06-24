---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:18:48.880218'
end_time: '2026-06-18T10:34:56.153160'
duration_seconds: 967.27
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: vibrio shaped
  trait_identifier: METPO:1000686
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: vibrio_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a curved rod or comma morphology,
    characterized by a short curved cylindrical form with a single arc.
  parent_traits: METPO:1000666
  synonyms: vibrio, vibrio-shaped
  evidence_summary: 'DOI:10.1016/j.cell.2016.12.019: V. cholerae has a characteristic
    curved rod morphology (Supports vibrio/comma morphology and a source-backed curvature
    mechanism in Vibrio cholerae.)'
  causal_graph_summary: 'vibrio_shaped_crvA_curvature: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** vibrio shaped
- **METPO identifier:** METPO:1000686
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved rod or comma morphology, characterized by a short curved cylindrical form with a single arc.
- **Parent traits:** METPO:1000666
- **Synonyms:** vibrio, vibrio-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2016.12.019: V. cholerae has a characteristic curved rod morphology (Supports vibrio/comma morphology and a source-backed curvature mechanism in Vibrio cholerae.)
- **Existing causal graph summary:** vibrio_shaped_crvA_curvature: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **vibrio shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/vibrio_shaped.yaml`.

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
- **Trait label:** vibrio shaped
- **METPO identifier:** METPO:1000686
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved rod or comma morphology, characterized by a short curved cylindrical form with a single arc.
- **Parent traits:** METPO:1000666
- **Synonyms:** vibrio, vibrio-shaped
- **Existing evidence:** DOI:10.1016/j.cell.2016.12.019: V. cholerae has a characteristic curved rod morphology (Supports vibrio/comma morphology and a source-backed curvature mechanism in Vibrio cholerae.)
- **Existing causal graph summary:** vibrio_shaped_crvA_curvature: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **vibrio shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/vibrio_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **vibrio shaped** (METPO:1000686)

**Target trait:** vibrio shaped (METPO:1000686) — MORPHOLOGY — curved-rod / comma-shaped short curved cylindrical form with a single arc.

### 1) Scope summary (trait meaning, boundaries, distinctions)

**Current understanding.** “Vibrio shaped” (often “vibrioid”) refers to a **curved rod** morphology: a rod-shaped cell body with a single, smooth curvature (comma-like). In *Vibrio cholerae*, this morphology is described as a “characteristic curved rod morphology” and is mechanistically linked to a dedicated curvature determinant (CrvA) and its regulators. (nikolai2020rnamediatedcontrolof pages 1-2)

**Boundary cases / nearby traits.** Vibrioid morphology is explicitly treated as a **derivative of rod shape**, distinct from straight rods and from more complex **helical/spiral** morphologies (multiple turns/periodic helicity). In *V. cholerae*, vibrioid curvature is plastic and can be shifted toward **straight rods** by genetic or signaling perturbations (e.g., c-di-GMP elevation) without necessarily changing basic rod growth machinery. (fernandez2020vibriocholeraeadapts pages 5-6, fernandez2020vibriocholeraeadapts pages 4-5)

**What the trait is not.** The trait should not be conflated with:
- **Helical/spiral** morphologies (e.g., *Helicobacter*, *Campylobacter*), which often involve distinct PG hydrolase/editing pathways and multi-turn helicity rather than a single arc. (fernandez2020vibriocholeraeadapts pages 5-6)
- **General rod shape**: rod morphology can exist without curvature, as shown by straight-rod mutants (e.g., ΔcrvA, ΔpapS) that remain rods. (fernandez2020vibriocholeraeadapts pages 5-6, pohl2024anoutermembrane pages 1-2)

### 2) Candidate causal-graph entities (nodes) grouped by type

The table below includes conservative ontology grounding where available; gene/protein accessions are flagged unresolved because UniProt/NCBI IDs were not present in the retrieved excerpts.

| Node label | Node type | Suggested identifier(s) | Evidence organism(s) | Notes |
|---|---|---|---|---|
| vibrio shaped | phenotype | METPO:1000686 | *Vibrio cholerae*; *Rhodospirillum rubrum* (comparative curved-rod morphology) | Target trait; curved/comma-shaped rod morphology distinct from straight rods and helical cells (nikolai2020rnamediatedcontrolof pages 1-2, pohl2024anoutermembrane pages 1-2, fernandez2020vibriocholeraeadapts pages 5-6) |
| peptidoglycan | chemical | CHEBI:53295 | *V. cholerae*; *R. rubrum* | Cell-wall polymer repeatedly identified as the structural basis of bacterial morphology (pohl2024anoutermembrane pages 1-2, nikolai2020rnamediatedcontrolof pages 1-2) |
| peptidoglycan biosynthetic process | process | GO:0009252 | *V. cholerae*; *R. rubrum* | Useful process node for wall growth/remodeling underlying rod and curved morphogenesis (pohl2024anoutermembrane pages 1-2, goudin2023recoveryofvibrio pages 6-8) |
| elongasome | complex | unresolved | *V. cholerae*; *R. rubrum* | Conserved lateral-growth complex organized by MreB; no stable ontology ID used here with confidence (pohl2024anoutermembrane pages 1-2, goudin2023recoveryofvibrio pages 1-2) |
| divisome | complex | unresolved | *V. cholerae*; *R. rubrum* | Division complex organized by FtsZ; relevant mainly as rod-shape prerequisite rather than direct curvature determinant (pohl2024anoutermembrane pages 1-2, goudin2023recoveryofvibrio pages 6-8) |
| MreB | protein | unresolved | *V. cholerae*; *R. rubrum* | Actin homolog organizing elongasome/helical wall growth; leave unresolved because no UniProt accession is evidenced here (pohl2024anoutermembrane pages 1-2, schiller2024identificationofstructural pages 1-2) |
| PBP2 | protein | unresolved | *V. cholerae* | Monofunctional peptidoglycan synthase associated with Rod complex in recovery to rod shape (goudin2023recoveryofvibrio pages 1-2) |
| class A PBPs / aPBPs | protein class | unresolved | *V. cholerae* | Required for periplasmic engulfment during rod-shape recovery; useful prerequisite node (goudin2023recoveryofvibrio pages 6-8) |
| CrvA | gene/protein | unresolved | *V. cholerae* | Periplasmic curvature determinant; polymer/filament-forming factor; no accession supported in current evidence set (nikolai2020rnamediatedcontrolof pages 1-2, martin2020theevolutionof pages 5-9) |
| CrvB | gene/protein | unresolved | *V. cholerae* | Partner in CrvAB curvature module; promotes higher-order CrvA assembly; unresolved identifier (martin2020theevolutionof pages 5-9, fernandez2020vibriocholeraeadapts pages 1-2) |
| CrvAB curvature module | complex | unresolved | *V. cholerae* | Candidate causal complex node; periplasmic inner-curve module sufficient/required for curvature in available evidence summaries (martin2020theevolutionof pages 5-9, schiller2024identificationofstructural pages 1-2) |
| VadR sRNA | gene/RNA | unresolved | *V. cholerae* | Hfq-dependent sRNA that post-transcriptionally represses crvA; unresolved because no stable RNA accession is in evidence (nikolai2020rnamediatedcontrolof pages 1-2, nikolai2020rnamediatedcontrolof pages 4-6) |
| Hfq | protein | unresolved | *V. cholerae* | RNA chaperone required for VadR stability/function; accession not evidenced (nikolai2020rnamediatedcontrolof pages 1-2) |
| VxrAB two-component system | complex | unresolved | *V. cholerae* | Upstream regulator activating vadR; include as regulatory complex node (nikolai2020rnamediatedcontrolof pages 1-2) |
| VxrA | protein | unresolved | *V. cholerae* | Histidine kinase component of VxrAB; unresolved identifier (nikolai2020rnamediatedcontrolof pages 1-2) |
| VxrB | protein | unresolved | *V. cholerae* | Response regulator component of VxrAB; unresolved identifier (nikolai2020rnamediatedcontrolof pages 1-2) |
| cyclic di-GMP | chemical | CHEBI:23411 | *V. cholerae* | Second messenger that decreases curvature/straightens cells by lowering CrvA expression (fernandez2020vibriocholeraeadapts pages 4-5, fernandez2020vibriocholeraeadapts pages 1-2) |
| diguanylate cyclase (QrgB) | protein | unresolved | *V. cholerae* | Experimental DGC used to elevate c-di-GMP and reduce curvature; keep unresolved (fernandez2020vibriocholeraeadapts pages 1-2) |
| VpsR | protein | unresolved | *V. cholerae* | Biofilm-promoting regulator implicated in c-di-GMP-dependent straightening; unresolved identifier (fernandez2020vibriocholeraeadapts pages 4-5, fernandez2020vibriocholeraeadapts pages 5-6) |
| VpsT | protein | unresolved | *V. cholerae* | c-di-GMP-dependent transcription factor sufficient to inhibit curvature in planktonic cells (fernandez2020vibriocholeraeadapts pages 5-6) |
| Por39 | protein | unresolved | *R. rubrum* | Outer-membrane porin curvature determinant; part of Por39/Por41/PapS module; unresolved identifier (pohl2024anoutermembrane pages 1-2) |
| Por41 | protein | unresolved | *R. rubrum* | Dominant outer-membrane porin contributing to PapS localization; unresolved identifier (pohl2024anoutermembrane pages 10-11, pohl2024anoutermembrane pages 1-2) |
| PapS | protein | unresolved | *R. rubrum* | PG-binding outer-membrane lipoprotein required for curvature; no accession evidenced (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 10-11) |
| Por39/Por41–PapS module | complex | unresolved | *R. rubrum* | Comparative curved-rod morphogenetic module that recruits/entraps elongasome at outer curve (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 10-11) |
| Rod complex | complex | unresolved | *V. cholerae* | Prerequisite morphogenetic machinery for elongation/branching during rod-shape recovery (goudin2023recoveryofvibrio pages 1-2, goudin2023recoveryofvibrio pages 6-8) |
| cell wall | cellular structure | GO:0005618 | *V. cholerae*; *R. rubrum* | Broad structural node often used in supporting literature; can complement PG-specific nodes (nikolai2020rnamediatedcontrolof pages 1-2, pohl2024anoutermembrane pages 1-2) |
| periplasm | cellular component | GO:0042597 | *V. cholerae*; *R. rubrum* | Relevant localization for CrvA/CrvB and PapS (martin2020theevolutionof pages 5-9, pohl2024anoutermembrane pages 1-2) |
| outer membrane | cellular component | GO:0019867 | *R. rubrum* | Relevant localization for porins and PapS curvature module (pohl2024anoutermembrane pages 1-2) |
| cefalexin | chemical | CHEBI:34739 | *V. cholerae* | Sub-inhibitory treatment amplifies curvature phenotypes in VadR study; assay-specific factor (nikolai2020rnamediatedcontrolof pages 4-6) |
| penicillin G | chemical | CHEBI:17334 | *V. cholerae* | Cell-wall-targeting antibiotic used in survival assays linked to shape regulation (nikolai2020rnamediatedcontrolof pages 1-2) |
| cell-wall-targeting antibiotics | chemical class | unresolved | *V. cholerae* | Useful environmental/experimental class node; keep label-only unless a specific ontology term is chosen later (nikolai2020rnamediatedcontrolof pages 1-2) |
| surface attachment | environment/process | unresolved | *V. cholerae* | Increases c-di-GMP during biofilm development and is associated with straightening; useful but indirect node (fernandez2020vibriocholeraeadapts pages 5-6) |
| biofilm formation | process | GO:0042710 | *V. cholerae* | Not the trait itself, but a key downstream process linked to c-di-GMP-mediated straightening (fernandez2020vibriocholeraeadapts pages 4-5, nikolai2020rnamediatedcontrolof pages 1-2) |
| swimming motility | process | GO:0097588 | *V. cholerae* | Downstream phenotype improved by curvature; useful consequence node, not determinant (fernandez2020vibriocholeraeadapts pages 5-6) |


*Table: This table maps candidate nodes for a vibrio-shaped causal graph to conservative identifiers where confidence is high and flags unresolved gene/protein entities for later curation. It is useful for turning literature-supported mechanisms into ontology-grounded TraitMech nodes.*

**Key mechanistic modules to represent in TraitMech (recommended):**
- **Periplasmic curvature module (CrvA/CrvB; *V. cholerae*):** CrvA is a periplasmic curvature determinant; CrvB promotes higher-order CrvA assembly and curvature dynamics (strong mechanistic candidate but some details here come from a preprint excerpt). (nikolai2020rnamediatedcontrolof pages 1-2, martin2020theevolutionof pages 5-9)
- **Regulatory module coupling wall stress → sRNA → curvature (VxrAB → VadR ⊣ crvA; *V. cholerae*):** provides a direct link between cell-wall stress/antibiotics and curvature repression. (nikolai2020rnamediatedcontrolof pages 1-2, nikolai2020rnamediatedcontrolof pages 4-6)
- **Second-messenger module coupling lifestyle switching to shape (c-di-GMP → VpsT/VpsR → decreased curvature; *V. cholerae*):** links biofilm development to straightening. (fernandez2020vibriocholeraeadapts pages 4-5, fernandez2020vibriocholeraeadapts pages 5-6)
- **Outer-membrane patterning module (Por39/Por41 → PapS → elongasome entrapment → curvature; *R. rubrum*):** a mechanistically distinct but highly relevant curved-rod module demonstrating OM control over elongasome positioning. (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 10-11)

### 3) Evidence-backed causal edges (triples) for candidate TraitMech graph

The following table compiles **candidate edges** as subject–predicate–object triples with verbatim supporting snippets and curation notes.

| Edge (S–P–O) | Evidence organism | Evidence type | Reference (DOI + URL + year/month) | Supporting snippet (verbatim from evidence) | Notes/curation flags |
|---|---|---|---|---|---|
| CrvA — promotes — vibrio shaped / cell curvature | *Vibrio cholerae* | KO / functional summary | 10.1038/s41467-020-19890-8 — https://doi.org/10.1038/s41467-020-19890-8 — 2020-11 | "Periplasmic protein CrvA determines cell curvature in V. cholerae" (nikolai2020rnamediatedcontrolof pages 1-2) | Strong, direct. Taxon-specific to *V. cholerae* evidence, but likely central TraitMech node. |
| crvA deletion — causes loss of — curvature / straight-rod morphology | *Vibrio cholerae* | KO phenotype | 10.1038/s41598-023-40897-w — https://doi.org/10.1038/s41598-023-40897-w — 2023-08 | "removal of crvA results in rod-shaped cells" (nikolai2020rnamediatedcontrolof pages 1-2) | Strong, direct phenotype. Snippet comes from cited context summary of the paper. |
| CrvA — required for assembly/localization of — CrvB filament | *Vibrio cholerae* | KO + localization | 10.1101/2020.02.20.954503 — https://doi.org/10.1101/2020.02.20.954503 — 2020-02 | "Deleting crvA resulted in diffuse CrvB-GFP localization, indicating that CrvA is required for CrvB assembly" (martin2020theevolutionof pages 5-9) | Direct mechanistic evidence, but from preprint and likely superseded by later Nature Microbiology paper not directly available in context. Curate with caution. |
| CrvB — promotes higher-order assembly of — CrvA filament | *Vibrio cholerae* | KO + inducible overexpression + localization | 10.1101/2020.02.20.954503 — https://doi.org/10.1101/2020.02.20.954503 — 2020-02 | "We thus hypothesized that CrvA can form small structures on its own and that CrvB promotes the higher-order assembly of CrvA." (martin2020theevolutionof pages 5-9) | Mechanistically useful but partly inferential wording. Keep as uncertain until backed by peer-reviewed direct text. |
| crvB expression — increases — CrvA assembly | *Vibrio cholerae* | Overexpression | 10.1101/2020.02.20.954503 — https://doi.org/10.1101/2020.02.20.954503 — 2020-02 | "crvB expression increased CrvA-GFP assembly" (martin2020theevolutionof pages 5-9) | Direct experimental statement; preprint source. |
| crvB expression — increases — cell curvature | *Vibrio cholerae* | Overexpression | 10.1101/2020.02.20.954503 — https://doi.org/10.1101/2020.02.20.954503 — 2020-02 | "crvB expression increased CrvA-GFP assembly (Figs. 4B and 4C) as well as cell curvature (Figs. 4B and 4D) in a dose-dependent manner." (martin2020theevolutionof pages 5-9) | Good causal edge; preprint. |
| CrvA and CrvB — colocalize in — periplasmic inner-curve filament | *Vibrio cholerae* | Localization | 10.1101/2020.02.20.954503 — https://doi.org/10.1101/2020.02.20.954503 — 2020-02 | "both proteins localized to the same structure" and "CrvB-GFP filaments also colocalized with DsbA-mCherry, indicating that CrvB is periplasmic" (martin2020theevolutionof pages 5-9) | Best represented as localization/supporting context node rather than causal morphology edge by itself. |
| VadR sRNA — post-transcriptionally represses — crvA mRNA | *Vibrio cholerae* | Regulatory repression / reporter validation | 10.1038/s41467-020-19890-8 — https://doi.org/10.1038/s41467-020-19890-8 — 2020-11 | "Here, we discover the VadR small RNA (sRNA) as a post-transcriptional inhibitor of the crvA mRNA." (nikolai2020rnamediatedcontrolof pages 1-2) | Strong, direct regulatory edge. |
| vadR mutation — increases — cell curvature | *Vibrio cholerae* | KO phenotype | 10.1038/s41467-020-19890-8 — https://doi.org/10.1038/s41467-020-19890-8 — 2020-11 | "Mutation of vadR increases cell curvature, whereas overexpression has the inverse effect." (nikolai2020rnamediatedcontrolof pages 1-2) | Strong phenotype edge. |
| VadR overexpression — reduces — CrvA protein level | *Vibrio cholerae* | Overexpression / protein quantification | 10.1038/s41467-020-19890-8 — https://doi.org/10.1038/s41467-020-19890-8 — 2020-11 | "VadR overexpression led to a ~2-fold reduction in CrvA production" (nikolai2020rnamediatedcontrolof pages 4-6) | Quantitative and direct. |
| VxrAB two-component system — activates transcription of — vadR | *Vibrio cholerae* | Regulatory induction / mutant + complementation | 10.1038/s41467-020-19890-8 — https://doi.org/10.1038/s41467-020-19890-8 — 2020-11 | "We show that vadR transcription is activated by the VxrAB two-component system" (nikolai2020rnamediatedcontrolof pages 1-2) | Strong upstream regulatory edge. |
| cell-wall-targeting antibiotics — induce — vadR expression | *Vibrio cholerae* | Regulatory induction / stress response | 10.1038/s41467-020-19890-8 — https://doi.org/10.1038/s41467-020-19890-8 — 2020-11 | "vadR transcription is activated by the VxrAB two-component system and triggered by cell-wall-targeting antibiotics" (nikolai2020rnamediatedcontrolof pages 1-2) | Useful environmental/experimental factor node. Antibiotic-specific, not basal physiology. |
| elevated c-di-GMP — decreases — cell curvature | *Vibrio cholerae* | Signaling perturbation / DGC induction | 10.1073/pnas.2010199117 — https://doi.org/10.1073/pnas.2010199117 — 2020-11 | "high c-di-GMP concentrations decrease cell curvature to generate straight rods" (fernandez2020vibriocholeraeadapts pages 4-5) | Strong, direct. Important trait-modulation edge. |
| elevated c-di-GMP — decreases expression of — CrvA | *Vibrio cholerae* | Signaling perturbation | 10.1073/pnas.2010199117 — https://doi.org/10.1073/pnas.2010199117 — 2020-11 | "The paper states elevated c-di-GMP straightens V. cholerae by decreasing CrvA expression." (fernandez2020vibriocholeraeadapts pages 1-2) | Strong but snippet is from evidence summary rather than quoted article text; curate with caution if strict verbatim is required. |
| VpsT — inhibits — curvature in planktonic cells | *Vibrio cholerae* | Regulatory sufficiency | 10.1073/pnas.2010199117 — https://doi.org/10.1073/pnas.2010199117 — 2020-11 | "The c-di-GMP-dependent transcription factor VpsT was sufficient to inhibit curvature in planktonic cells." (fernandez2020vibriocholeraeadapts pages 5-6) | Strong sufficiency claim. Useful edge from regulator to morphology. |
| VpsR/VpsT regulatory node — mediates straightening of — cells during microcolony formation | *Vibrio cholerae* | Regulatory inference from genetics/phenotype | 10.1073/pnas.2010199117 — https://doi.org/10.1073/pnas.2010199117 — 2020-11 | "These data suggest that the VpsR/VpsT regulatory node is responsible for the straightening of cells during microcolony formation." (fernandez2020vibriocholeraeadapts pages 5-6) | Moderately indirect/inferential wording; mark uncertain. |
| Por39/Por41 porins — recruit — PapS | *Rhodospirillum rubrum* | Localization / mutant perturbation | 10.1038/s41467-024-51790-z — https://doi.org/10.1038/s41467-024-51790-z — 2024-09 | "the R. rubrum porins Por39 and Por41 form a helical ribbon-like structure at the outer curve of the cell that recruits the peptidoglycan-binding lipoprotein PapS" (pohl2024anoutermembrane pages 1-2) | Strong, recent, non-*Vibrio* evidence for a distinct curved-rod module. Taxon-specific analog, not same mechanism as *V. cholerae*. |
| PapS inactivation — results in — cell straightening | *Rhodospirillum rubrum* | KO phenotype | 10.1038/s41467-024-51790-z — https://doi.org/10.1038/s41467-024-51790-z — 2024-09 | "with PapS inactivation, porin delocalization or disruption of the porin-PapS interface resulting in cell straightening" (pohl2024anoutermembrane pages 1-2) | Strong direct morphology edge. Non-*Vibrio* but very relevant comparative mechanism. |
| porin delocalization/disrupted porin–PapS interface — results in — cell straightening | *Rhodospirillum rubrum* | Mutational disruption | 10.1038/s41467-024-51790-z — https://doi.org/10.1038/s41467-024-51790-z — 2024-09 | "with PapS inactivation, porin delocalization or disruption of the porin-PapS interface resulting in cell straightening" (pohl2024anoutermembrane pages 1-2) | Strong. Could be split into two edges if graph granularity requires. |
| porin–PapS assemblies — entrap — cell elongation machinery / elongasome | *Rhodospirillum rubrum* | Mechanistic localization | 10.1038/s41467-024-51790-z — https://doi.org/10.1038/s41467-024-51790-z — 2024-09 | "porin-PapS assemblies act as molecular cages that entrap the cell elongation machinery" (pohl2024anoutermembrane pages 1-2) | Strong mechanistic edge. Useful process node between module and curvature. |
| porin–PapS assemblies — bias growth toward — outer curve | *Rhodospirillum rubrum* | Mechanistic inference / imaging | 10.1038/s41467-024-51790-z — https://doi.org/10.1038/s41467-024-51790-z — 2024-09 | "thus biasing cell growth towards the outer curve" (pohl2024anoutermembrane pages 1-2) | Strong process edge; links module to asymmetric growth. |
| PapS — promotes enrichment of — elongasome complexes at outer curve | *Rhodospirillum rubrum* | Localization | 10.1038/s41467-024-51790-z — https://doi.org/10.1038/s41467-024-51790-z — 2024-09 | "PapS promotes the enrichment of elongasome complexes at the outer curve." (pohl2024anoutermembrane pages 10-11) | Strong figure-caption level evidence; useful if process nodes are desired. |
| aPBPs — required for — periplasmic engulfment during rod-shape recovery | *Vibrio cholerae* | Chemical inhibition / recovery assay | 10.1371/journal.pone.0293276 — https://doi.org/10.1371/journal.pone.0293276 — 2023-10 | "inhibiting aPBPs prevented the periplasmic engulfment process and successive cell shape recovery steps" (goudin2023recoveryofvibrio pages 6-8) | Relevant prerequisite edge for rebuilding rod/vibrioid morphology after spheroplast state; not curvature-specific. |
| Rod-complex — required for — cell elongation and branching during rod-shape recovery | *Vibrio cholerae* | Chemical inhibition / recovery assay | 10.1371/journal.pone.0293276 — https://doi.org/10.1371/journal.pone.0293276 — 2023-10 | "inhibiting the Rod-complex precluded cell elongation and branching" (goudin2023recoveryofvibrio pages 6-8) | Relevant prerequisite morphology edge; supports rod scaffold needed before vibrioid curvature can be imposed. |
| FtsK — localizes to — periplasmic engulfment / vesicle extrusion sites | *Vibrio cholerae* | Localization | 10.1371/journal.pone.0293276 — https://doi.org/10.1371/journal.pone.0293276 — 2023-10 | "FtsK-YGFP localized also at the site of periplasmic engulfment and encircled the periplasmic excess until its elimination. Furthermore, FtsK-YGFP accumulated at the sites of extrusion of new periplasmic vesicles" (goudin2023recoveryofvibrio pages 6-8) | Accessory/recovery-specific. Not enough to curate as direct vibrio-shape determinant. |
| curved morphology — increases — swimming speed | *Vibrio cholerae* | Phenotype / single-cell tracking | 10.1073/pnas.2010199117 — https://doi.org/10.1073/pnas.2010199117 — 2020-11 | "curved rods swim on average 5.5% faster than straight rods" (fernandez2020vibriocholeraeadapts pages 5-6) | Fitness/application edge, not a mechanistic determinant of the trait; useful for phenotype consequences rather than TraitMech core. |
| curvature retention — reduces — biofilm biomass / microcolony formation | *Vibrio cholerae* | Morphology manipulation / biofilm assay | 10.1073/pnas.2010199117 — https://doi.org/10.1073/pnas.2010199117 — 2020-11 | "The curved mutant had reduced biofilm biomass compared to the other strains" (fernandez2020vibriocholeraeadapts pages 4-5) | Consequence edge, not determinant. Useful context for adaptive significance. |


*Table: This table compiles candidate subject–predicate–object edges for curating the vibrio-shaped morphology trait, using only supported snippets from the provided contexts. It highlights direct determinants, regulators, and prerequisite morphogenetic processes, while flagging taxon-specific or inference-based claims.*

#### Visual evidence (curved vs straight phenotypes)
The 2024 *Nature Communications* study provides figure evidence that disrupting the PapS/porin module straightens cells. (pohl2024anoutermembrane media cdacfcd4, pohl2024anoutermembrane media f7693807)

### 4) Recent developments (prioritizing 2023–2024)

**2024: Outer-membrane porin–lipoprotein module controlling curvature (comparative mechanism).** Pöhl et al. (2024) identify Por39/Por41 (outer-membrane porins) forming a ribbon-like structure that recruits the PG-binding lipoprotein PapS; **PapS inactivation or disrupting porin–PapS interactions causes straightening**, and assemblies “entrap the cell elongation machinery,” biasing growth to generate curvature. This expands curvature mechanisms beyond inner-curve filament systems and emphasizes OM spatial patterning as a morphogenetic control layer. (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 10-11)

**2023: Cell-wall synthesis system requirements for restoring rod morphogenesis after envelope loss.** Goudin et al. (2023) study *V. cholerae* exiting a spheroplast state and show that **inhibiting aPBPs prevents periplasmic engulfment and downstream shape recovery**, while **inhibiting the Rod-complex blocks elongation/branching**, highlighting how core PG synthesis machineries are prerequisites for rod (and thus vibrioid) shape programs. (goudin2023recoveryofvibrio pages 6-8)

**2023: sRNA regulatory programs in *V. cholerae* (expert synthesis).** While the detailed mechanistic edges here come from the 2020 primary paper, the existence of sRNA regulation over curvature determinants (e.g., crvA mRNA) is also summarized in *V. cholerae* sRNA review literature (retrieved but not deeply excerpted here); this is consistent with the modern view that post-transcriptional regulation coordinates envelope state, morphology, and lifestyle. (nikolai2020rnamediatedcontrolof pages 1-2)

### 5) Current applications and real-world implementations

**Lifestyle adaptation and pathogenesis-relevant phenotypes.** In *V. cholerae*, curvature is treated as functionally meaningful: curved morphology is associated with motility advantages, while straightening is advantageous for sessile/biofilm states under high c-di-GMP. (fernandez2020vibriocholeraeadapts pages 4-5, fernandez2020vibriocholeraeadapts pages 5-6)

**Antibiotic-response coupling.** The VadR pathway provides a direct implementation-like example where **cell-wall-targeting antibiotics trigger a regulatory cascade** (via VxrAB) that represses crvA; failure to repress crvA decreases survival under penicillin G. This suggests cell shape is part of an integrated envelope-stress response affecting antibiotic resistance phenotypes. (nikolai2020rnamediatedcontrolof pages 1-2)

**Biophysical and microfluidic implementations (mechanosensing context).** Mechanically induced envelope stress pathways (e.g., VxrAB activation under mechanical loading) have been investigated in *V. cholerae* as part of envelope homeostasis; this provides experimental frameworks (microfluidics/compression) to perturb wall mechanics and monitor morphology-linked signaling. (pohl2024anoutermembrane pages 10-11)

### 6) Relevant statistics and quantitative data (from the retrieved evidence)

- **Motility advantage of curvature (single-cell tracking):** curved rods swim **~5.5% faster** than straight rods (95% CI [5.5%, 5.9%], P < 1e-5); reversal frequency difference not significant (95% CI [−0.87%, 2.8%]). (fernandez2020vibriocholeraeadapts pages 5-6)
- **Biofilm biomass effect sizes:** WT and straight populations had indistinguishable biomass (difference 95% CI [−0.40, 0.22]); a curved mutant showed reduced biomass (difference 95% CI [−0.91, −0.28], P = 1.8e-3). (fernandez2020vibriocholeraeadapts pages 4-5)
- **VadR control of CrvA protein levels:** CrvA levels **~1.5-fold higher** in ΔvadR and **~2-fold lower** with VadR overexpression. (nikolai2020rnamediatedcontrolof pages 4-6)
- **CrvB’s effect on CrvA filament assembly:** in ΔcrvB, only **~6%** of cells had long CrvA filaments similar to wild type, supporting CrvB’s role in higher-order assembly. (martin2020theevolutionof pages 5-9)

### 7) Expert opinions / authoritative synthesis (within retrieved sources)

- **Cell shape derives from peptidoglycan and morphogenetic complexes.** The 2024 *Nature Communications* paper frames curved shapes as widespread and important for “motility, virulence and fitness,” and describes curvature mechanisms as often relying on polymer-forming proteins that associate with the envelope and alter local PG remodeling. (pohl2024anoutermembrane pages 1-2)
- **Regulatory integration (envelope integrity ↔ shape ↔ biofilm).** The VadR study explicitly concludes that VadR coordinates “peptidoglycan integrity, cell shape, and biofilm formation,” reflecting a broader expert consensus that morphology is part of adaptive regulatory programs rather than a fixed static feature. (nikolai2020rnamediatedcontrolof pages 1-2)

### 8) Warnings / curation cautions (do not over-curate)

1. **CrvAB structural/assembly edges from preprints:** Some fine-grained mechanistic claims about CrvA/CrvB filament assembly dynamics in the provided evidence are from a 2020 bioRxiv preprint excerpt. These edges are valuable but should be flagged **uncertain** until corroborated with peer-reviewed full text (a later Nature Microbiology paper exists but was unobtainable in this run). (martin2020theevolutionof pages 5-9)
2. **c-di-GMP → CrvA expression wording:** One edge in the candidate table uses a summary sentence (“paper states…”) rather than a direct quotation line from the PDF excerpt; treat that edge as **needs-verbatim confirmation** before strict curation. (fernandez2020vibriocholeraeadapts pages 1-2)
3. **Rod-shape recovery vs curvature per se:** aPBPs/Rod-complex evidence is strongly causal for rod morphogenesis recovery after spheroplasting, but not curvature-specific; curate these as **prerequisite morphogenesis** nodes rather than direct vibrio-shape determinants. (goudin2023recoveryofvibrio pages 6-8)
4. **Cross-taxon transferability:** The Por39/Por41/PapS module is a strong 2024 curved-rod mechanism but is in *R. rubrum*; treat as **comparative module** unless trait curation is intended to include non-*Vibrio* curved-rod bacteria. (pohl2024anoutermembrane pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates)

1. Pöhl S, et al. **An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in *Rhodospirillum rubrum*.** *Nature Communications* (Sep 2024). DOI: **10.1038/s41467-024-51790-z**. https://doi.org/10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 1-2)
2. Schiller H, et al. **Identification of structural and regulatory cell-shape determinants in *Haloferax volcanii*.** *Nature Communications* (Feb 2024). DOI: **10.1038/s41467-024-45196-0**. https://doi.org/10.1038/s41467-024-45196-0 (contextual bacterial curvature framing) (schiller2024identificationofstructural pages 1-2)
3. Goudin A, et al. **Recovery of *Vibrio cholerae* polarized cellular organization after exit from a non-proliferating spheroplast state.** *PLOS ONE* (Oct 26, 2023). DOI: **10.1371/journal.pone.0293276**. https://doi.org/10.1371/journal.pone.0293276 (goudin2023recoveryofvibrio pages 6-8)
4. Harper CE, et al. **Mechanical stimuli activate gene expression via a cell envelope stress sensing pathway.** *Scientific Reports* (Aug 2023). DOI: **10.1038/s41598-023-40897-w**. https://doi.org/10.1038/s41598-023-40897-w (mechanical loading → VxrAB; includes crvA/shape background) (pohl2024anoutermembrane pages 10-11)
5. Peschek N, et al. **RNA-mediated control of cell shape modulates antibiotic resistance in *Vibrio cholerae*.** *Nature Communications* (Nov 2020). DOI: **10.1038/s41467-020-19890-8**. https://doi.org/10.1038/s41467-020-19890-8 (nikolai2020rnamediatedcontrolof pages 1-2, nikolai2020rnamediatedcontrolof pages 4-6)
6. Fernandez NL, et al. ***Vibrio cholerae* adapts to sessile and motile lifestyles by cyclic di-GMP regulation of cell shape.** *PNAS* (Nov 2020). DOI: **10.1073/pnas.2010199117**. https://doi.org/10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 4-5, fernandez2020vibriocholeraeadapts pages 5-6)
7. Martin NR, et al. **The evolution of bacterial shape complexity by a curvature-inducing module.** *bioRxiv* (Feb 2020). DOI: **10.1101/2020.02.20.954503**. https://doi.org/10.1101/2020.02.20.954503 (preprint; use cautiously) (martin2020theevolutionof pages 5-9)

Unobtainable but highly relevant primary reference (already in your template evidence list): Bartlett TM, et al. *Cell* (Jan 2017). DOI: **10.1016/j.cell.2016.12.019** (not directly retrievable here; do not add edges requiring verbatim snippets from it in this run).


References

1. (nikolai2020rnamediatedcontrolof pages 1-2): Nikolai Peschek, Roman Herzog, Praveen K. Singh, Marcel Sprenger, Fabian Meyer, Kathrin S. Fröhlich, Luise Schröger, Marc Bramkamp, Knut Drescher, and Kai Papenfort. Rna-mediated control of cell shape modulates antibiotic resistance in vibrio cholerae. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19890-8, doi:10.1038/s41467-020-19890-8. This article has 44 citations and is from a highest quality peer-reviewed journal.

2. (fernandez2020vibriocholeraeadapts pages 5-6): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 51 citations and is from a highest quality peer-reviewed journal.

3. (fernandez2020vibriocholeraeadapts pages 4-5): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 51 citations and is from a highest quality peer-reviewed journal.

4. (pohl2024anoutermembrane pages 1-2): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

5. (goudin2023recoveryofvibrio pages 6-8): Anthony Goudin, Jean-Luc Ferat, Christophe Possoz, François-Xavier Barre, and Elisa Galli. Recovery of vibrio cholerae polarized cellular organization after exit from a non-proliferating spheroplast state. PLOS ONE, 18:e0293276, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293276, doi:10.1371/journal.pone.0293276. This article has 3 citations and is from a peer-reviewed journal.

6. (goudin2023recoveryofvibrio pages 1-2): Anthony Goudin, Jean-Luc Ferat, Christophe Possoz, François-Xavier Barre, and Elisa Galli. Recovery of vibrio cholerae polarized cellular organization after exit from a non-proliferating spheroplast state. PLOS ONE, 18:e0293276, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293276, doi:10.1371/journal.pone.0293276. This article has 3 citations and is from a peer-reviewed journal.

7. (schiller2024identificationofstructural pages 1-2): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

8. (martin2020theevolutionof pages 5-9): Nicholas R. Martin, Edith Blackman, Benjamin P. Bratton, Thomas M. Bartlett, and Zemer Gitai. The evolution of bacterial shape complexity by a curvature-inducing module. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.20.954503, doi:10.1101/2020.02.20.954503. This article has 4 citations.

9. (fernandez2020vibriocholeraeadapts pages 1-2): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 51 citations and is from a highest quality peer-reviewed journal.

10. (nikolai2020rnamediatedcontrolof pages 4-6): Nikolai Peschek, Roman Herzog, Praveen K. Singh, Marcel Sprenger, Fabian Meyer, Kathrin S. Fröhlich, Luise Schröger, Marc Bramkamp, Knut Drescher, and Kai Papenfort. Rna-mediated control of cell shape modulates antibiotic resistance in vibrio cholerae. Nature Communications, Nov 2020. URL: https://doi.org/10.1038/s41467-020-19890-8, doi:10.1038/s41467-020-19890-8. This article has 44 citations and is from a highest quality peer-reviewed journal.

11. (pohl2024anoutermembrane pages 10-11): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

12. (pohl2024anoutermembrane media cdacfcd4): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

13. (pohl2024anoutermembrane media f7693807): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.